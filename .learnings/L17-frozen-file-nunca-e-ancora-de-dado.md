# Lição 17 — `__file__` nunca é âncora de dado de usuário em app empacotado

**Data:** 2026-09-27 · **Origem:** rodada +09 do SIGMAFLOW (P-15/I44) · **Tags:** pyinstaller, sys-frozen, path, persistencia, dado-usuario

## O sintoma

A P-15 mandava ancorar o caminho do banco numa raiz única, imune ao `cwd`. A correção
natural é a que está em quase todo tutorial:

```python
RAIZ = Path(__file__).resolve().parent.parent
```

A suíte ficou **verde**: 627 testes na raiz, 22 no backend, lint limpo, guarda de `data/`
intacta. A âncora estava errada.

## A causa

O SigmaFlow é distribuído como portátil:

```
release\SigmaFlow-v6.1.0\
  SigmaFlow.exe
  data\
    sigmaflow.db        <- 132 KB, dados reais do usuário
    processos.json
```

Quando congelado pelo PyInstaller, `__file__` de `src/storage.py` aponta para **dentro
do bundle extraído**, e em modo one-file esse bundle é `%TEMP%\_MEIxxxxxx`, destruído no
exit do processo. Com a âncora em `__file__`:

```
DEFAULT_DB_PATH = %TEMP%\_MEIxxxxxx\data\sigmaflow.db
```

O histórico do usuário nasceria num temp descartável. **Sem erro, sem aviso, sem backup** —
o app abriria vazio no próximo start, e o `data/` real continuaria intacto ao lado do
exe, parecendo "que a GrabCAD perdeu meus processos".

## Por que nenhum teste pegaria

Porque a suíte roda **das fontes**, e das fontes `__file__` está certo. O erro não estava
entre teste e código: estava entre o cenário que a suíte exercita e o cenário real de uso.
Green suite, premissa errada.

## A correção

```python
if getattr(sys, "frozen", False):
    RAIZ_CANONICA = Path(sys.executable).resolve().parent   # data/ mora com o exe
else:
    RAIZ_CANONICA = Path(__file__).resolve().parent.parent  # raiz do repo
```

## A regra

**Antes de ancorar qualquer caminho de dado, responder "onde isso roda quando entregue?"**
Três perguntas, na ordem:

1. Roda das fontes, de um `.exe`, de um serviço, de um interpretador embedded?
2. Se `.exe`: o dado viaja **junto** (portátil) ou fica **fora** (AppData/ProgramData)?
3. O app pode ser relocado copiado para outra pasta? A âncora sobrevive?

Derivados do mesmo bug, que continuam abertos:

- `src/despacho.py:299` lê `data/tabela_retribuicoes.json` por `__file__`, arquivo que o
  spec **não** empacota → congelado devolve `{}` em silêncio, e a taxa RPI some.
- `src/prazos_processuais.py:280` lê `feriadosestaduais.json`, que **é** empacotado →
  funciona de `_MEIPASS`, e por isso não é bug. **A diferença entre os dois é só o
  `datas=` do spec** — o código é idêntico, o desfecho não.

Ou seja: `__file__` está certo para *recurso read-only empacotado* e errado para *dado
mutável do usuário*. Confundir os dois é o erro.

## Como os testes foram feitos para morder

Reintroduzi o bug à mão (voltei a âncora para `__file__`), rodei, e os 2 testes
congelados **falharam**; restaurei, passaram. Teste que nunca falha não é garantia — é
cinema. Ver Lição 15 (verificação que passa sem provar), que é a mesma família de erro por
outro caminho.

## Metadata

Source: sessão SigmaFlow rodada +09 (2026-09-27)
Related Files: src/storage.py, src/config.py, src/despacho.py, src/prazos_processuais.py, SigmaFlow.spec, tests/test_caminho_canonico_p15.py
Pattern-Key: frozen-file-never-data-anchor
