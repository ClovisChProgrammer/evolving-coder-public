# Lição 21 — Import que passa porque o `.pyc` órfão ficou para trás

**Data:** 2026-10-07 · **Origem:** INPI-4 do SIGMAFLOW (Achado R55) · **Tags:** import, bytecode, migracao, fronteira, bug-latente, instrumento-vs-alvo

## O sintoma

`backend/app/clients/prazos.py` importava `from src.prazos import ...`. Mas `src/prazos.py`
**nao existe** desde a migracao I60 (prazos foram para `src/dominio/`). O import continuava
verde na maquina de desenvolvimento — por causa de **bytecodes orfaos nao-rastreados**
(`src/prazos.pyc` + `__pycache__/`). A maquina "sabia" importar um modulo que o
repositorio nao tinha mais. Em **checkout ou CI limpo**, a rota `/api/v1/prazos` quebrava
com `ModuleNotFoundError`.

## A causa raiz

O Python prioriza/carrega bytecode compilado em `__pycache__` sem exigir que o `.py`
fonte correspondente ainda exista (em versoes/cenarios com o `.pyc` legado no lugar certo,
ou quando um `.pyc` orfao permanece apos a remocao do fonte). Como `__pycache__` e'
gitignored, o defeito era **invisivel no git** e **presente no disco**. O `import` verde
nao provava que o modulo existia — provava apenas que *algo* com aquele nome foi encontrado.

## Por que isso e' a mesma familia de L15/L17/L18

- **L15** — verificacao que passa sem provar.
- **L17** — arquivo congelado nunca e' ancora de dado.
- **L18** — fixture no lugar do registro real (prove by removal).

Aqui a forma e' nova: o que mascarava a realidade era um **artefato compilado obsoleto**,
fora do controle de versao. Um `import` verde nao prova que o modulo existe — prova apenas
que *algo* com aquele nome foi encontrado no `sys.path`/`__pycache__`.

## Como detectar e corrigir

1. **Prova por remocao** (a tecnica que fechou o caso): remover os `.pyc`/`__pycache__`
   orfaos e rodar de novo. Se o import passa a falhar, o modulo nunca existiu — havia so
   o artefato.
   - `Remove-Item -Recurse -Force` nos `__pycache__` do pacote antes da prova.
   - Confirmar: `import src.prazos` deve falhar; `import app.api.v1.prazos` deve passar
     pelo caminho correto (`src.dominio.prazos`).
2. **Varredura de fronteira**: para cada `src.X` importado no backend, verificar que o
   arquivo fonte existe no repo (0 faltando). Fronteiras de pacote (backend x raiz) sao
   o habitat natural desse fantasma.
3. **Correcao de manutencao**: reexportar do caminho canonico (`src.dominio.prazos`),
   docstring honesta, sem tocar em regra/versao.

## Licao

**Um import verde prova que *algo* foi encontrado, nao que o modulo existe.** O
`__pycache__` e' gitignored por desenho — e por isso pode guardar um mundo que o
repositorio ja' abandonou. Terceira sessao seguida (L15 → L20 → R55) em que o defeito
morava **no instrumento**: primeiro um teste que pulava BOM, depois um repositorio que
aceitava kwargs, agora o proprio ambiente de import contaminado por bytecode obsoleto.

Descartar `__pycache__`/`.pyc` orfaos **antes** de concluir que uma fronteira esta' sã.

## Metadata

**Logged:** 2026-10-07
**Priority:** high
**Status:** active
**Project:** inpi-marcas-patentes
**Area:** testing / infraestrutura
**Pattern-Key:** import-verde-artefato-obsoleto
**Source:** REX `## Bloco:INPI-4-manutencao` (Achado R55); commit `0a35b75`
**Related Files:** `backend/app/clients/prazos.py`, `src/dominio/prazos.py`, `src/prazos.pyc`
**Tags:** import, bytecode-orfao, pycache, fronteira, backend, migracao-i60, r55, instrumento-vs-alvo