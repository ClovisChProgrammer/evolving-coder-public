# Lição 15 — Verificação que passa sem provar: o padrão R36/R46/R49/R53

**Data:** 2026-09-26 · **Origem:** rodada +09 do SIGMAFLOW · **Tags:** teste, prova, ci, persistência

## O padrão

Quatro vezes numa mesma sessão, um teste **verde** não provou o que parecia provar:

| ID | O que o verde afirmava | O que era verdade |
|---|---|---|
| R36 | contrato de criação canônica funciona | só funcionava por efeito colateral do startup da GUI; em banco novo dava `no such table` |
| R46 | a suíte não mexe no dado do usuário | escrevia no `data/processos.json` real, a cada execução |
| R49 | o gate de schema bloqueia schema defasado | o teste mexia no `PRAGMA user_version`, e a versão vive na tabela `schema_version` — nunca exercitou o gate |
| R53 | o CI endureceu, a linha "CI OK" do gate está verde | o CI **nunca rodou**: `pytest` não estava em `requirements.txt` |

## A regra

**Uma verificação que passa por leitura de texto não prova execução.**

`assert "guard_data.py check" in ci_yaml` confirma que a *string* existe no arquivo.
Não confirma que o pipeline executa, que a dependência está instalada, nem que o
caminho é importável a partir do diretório de trabalho do job.

O mesmo vale para aassertiva estrutural: um teste que faz `ast.parse` do código e
procura um padrão prova **a forma**, não o efeito. Quando a forma e o efeito podem
divergir — e podem —, prove o efeito.

## A armadilha mais cara

**Três dos quatro eram defeitos introduzidos por correções anteriores da mesma
sessão.** Nenhum estava no escopo do que a KAI estava olhando ao corrigir.

Escrever tensão *durante* a construção pega o que você está olhando. Não pega o que a
correção anterior quebrou. São campos de visão diferentes.

**Consequência prática:** a correção não está terminada quando o teste passa. Está
terminada quando você **repassa por ela com olho frio**, ou quando alguém faz.

## Como fechar o buraco

1. **Teste de efeito, não de texto.** Para o CI: exercitar dependências declaradas,
   comandos rodando, import a partir do `working-directory`, e o caminho invocado
   existindo de verdade.
2. **Provar que o teste pega.** Remover a correção e ver o teste ficar vermelho. Um
   teste que nunca foi visto vermelho não tem evidência de que detects o defeito.
3. **Executar o que você escreveu.** O R53 existia porque a KAI escreveu um CI e nunca
   o rodou. Escrever CI não é rodá-lo.
4. **Quando a verificação é cara, meça antes de decidir.** O R51/R52 foi uma decisão
   tomada duas vezes sem medir, e as duas vezes errada.

## O caso do `mtime` (R52), que generalize

Uma verificação pode falhar em **dois** sentidos opostos, e corrigir um pode criar o
outro:

- **R51:** comparar só o *tamanho* acima de 8 MB → **não detecta** mudança de conteúdo.
- **R52:** incluir o *mtime* na identidade → **detecta** mudança que não existe (um
  `touch` sem alterar byte algum), e a guarda passou a acusar ~200 falsos.

A pergunta certa não é "detectar mudança" nem "detectar rápido". É **"detectar mudança
de conteúdo"** — e `mtime` responde a "quando o arquivo foi escrito", que é outra
pergunta.

Quando a amostragem for a resposta, **declare o limite**. A guarda finalSampling
não vê alteração que mude bytes só no meio do arquivo, com o mesmo tamanho. Isso está
escrito no código, não escondido — porque limite não declarado vira garantia
falsa.
