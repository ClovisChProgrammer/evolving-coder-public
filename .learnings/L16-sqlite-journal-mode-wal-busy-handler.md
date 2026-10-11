# Lição 16 — SQLite: `PRAGMA journal_mode=WAL` não honra o busy handler

**Data:** 2026-09-26 · **Origem:** rodada +09 do SIGMAFLOW · **Tags:** sqlite, concorrência, python

## O sintoma

```
sqlite3.OperationalError: database is locked
```

em código que **não estava escrevendo nada**. Várias threads, cada uma apenas
*abrindo* uma conexão nova sobre o mesmo arquivo recém-criado.

## A causa

`storage.connect()` fazia, em toda conexão:

```python
conn = sqlite3.connect(str(path), timeout=10.0)
conn.execute("PRAGMA journal_mode=WAL")
```

Converter o modo de journal **exige um lock exclusivo no arquivo do banco**, e o SQLite
**não invoca o busy handler nessa operação**. O `timeout=10.0` da conexão e o
`PRAGMA busy_timeout` são ignorados: o `SQLITE_BUSY` volta na hora.

O efeito é pior do que um lock perdido. `PRAGMA journal_mode` é *write* por natureza —
mesmo em banco que não existe, criar o arquivo e definir o journal é escrita. Então
"abrir em paralelo" compete por um lock de escrita como se estivesse gravando.

## Por que só apareceu depois

Porque só apareceu quando o número de conexões por operação **dobrou**. Ao mover a
persistência para o repositório, o serviço passou a fazer `obter_processo` e
`criar_processo` — uma conexão cada. Com 5 threads em banco novo, 3 de 6 voltas
quebraram.

Nada disso eraLatente: estava lá desde o primeiro `connect()`.

## A correção

```python
def _garantir_wal(conn):
    atual = conn.execute("PRAGMA journal_mode").fetchone()
    if atual and str(atual[0]).lower() == "wal":
        return                      # caminho comum: sem lock
    with _LOCK_JOURNAL:             # conversão: evento único por arquivo
        ...
        conn.execute("PRAGMA journal_mode=WAL")
```

Duas decisões:

1. **Ler antes de escrever.** `PRAGMA journal_mode` de leitura é o que decide, e não
   pega lock. O banco já em WAL (99,999% dos casos depois do primeiro start) não paga
   nada.
2. **Serializar só a conversão**, com um lock de processo. Ela acontece uma vez por
   arquivo; serializar toda conexão seria desperdício.

E `PRAGMA busy_timeout` passa a ser definido **antes** do journal mode, para que as
operações seguintes já o tenham.

## A regra

**`PRAGMA journal_mode` é escrita disfarçada de configuração.** Se a sua função de
conexão a executa, ela está serializada — ou deveria estar.

A pergunta de revisão para qualquer `connect()`:

1. Alguma PRAGMA aqui pega lock exclusivo?
2. Ela é serializada?
3. Ela é evitada quando o estado já é o desejado?

Um "não" em qualquer uma é um `database is locked` esperando o dia em que duas coisas
acontecerem ao mesmo tempo.

## O padrão maior

Isto é a **mesma família do R43** (DDL concorrente: `CREATE TABLE IF NOT EXISTS`
protege repetição *sequencial*, não intercalação entre conexões), um nível abaixo.

E vale a regra que a KAI registrou nesta rodada: **defeito de concorrência aparece
quando você aumenta a concorrência, e some quando você diminui.** Se a correção
aumenta o número de conexões por operação, o risco de lock sobe junto — e o teste
precisa cobrir o caso novo, não só o antigo.
