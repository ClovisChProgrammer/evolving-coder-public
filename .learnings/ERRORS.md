# .learnings/ERRORS.md

Registro de erros, falhas de integração e correções.

## [ERR-20260704-001] anti_loop_violation

**Logged**: 2026-07-04T18:50:00-03:00
**Priority**: critical
**Status**: resolved
**Project**: QPEÇA
**Area**: communication

### Summary
KAI entrou em looping cego testando porta 3000 (frontend) repetidamente sem informar progresso ao usuário. Clóvis teve que interromper.

### Details
- Testava `Invoke-WebRequest http://localhost:3000` sem reportar que estava tentando
- Não avisou que o frontend estava compilando (Next.js compilação inicial leva ~20s)
- Repetiu múltiplas vezes sem comunicar falha nem progresso
- Usuário perdeu tempo e confiança no processo

### Root Cause
Ausência de regra explícita anti-loop no protocolo. Comportamento não estava codificado nas instruções.

### Fix
Criado `~/.config/opencode/instructions/global-rules.md` com Regra #1 — ANTI-LOOP + PROGRESSO OBRIGATÓRIO.
Atualizado `evolving-coder.md` para referenciar regras globais ANTES de qualquer ação.

### Metadata
**Tags**: looping, progress, communication, critical
**Pattern-Key**: global-anti-loop-progress

Cada entrada segue o formato padrão de .learnings/.

## [ERR-20260602-001] communication

**Logged**: 2026-06-02T20:00:00-03:00
**Priority**: high
**Status**: promoted
**Project**: Navinclud2026TCC
**Area**: communication

### Summary
Andamentos KAI.md não foi atualizado por 2 sessões consecutivas (28/05 e 02/06), perdendo registro de correções CWS, build-cws-zip, BMC iterations e bump v1.4.

### Details
- Última entrada: 26/05 (landing page, manifest v3 inicial)
- Sessões perdidas: 28/05 (3 commits CWS + SEO + build-cws-zip), 29/05 (4 commits BMC iterations), 02/06 (2 commits CWS round 2)
- Total: ~9 commits sem registro

### Suggested Action
Sempre atualizar Andamentos KAI.md ao final de CADA sessão, mesmo que breve. Incluir: data, resumo dos commits, estado atual, pendências. Se a sessão for muito curta, pelo menos uma linha.

### Metadata
Source: Gap identificado pelo APRENDA! em 2026-06-02
Related Files: Andamentos KAI.md
Tags: documentation, session-log, process
Pattern-Key: session-log-discipline

## [ERR-20260717-001] communication

**Logged**: 2026-07-17T15:44:00-03:00
**Priority**: high
**Status**: resolved
**Project**: LexPilot
**Area**: communication

### Summary
Versões anteriores do e-book prometiam 30 capítulos no escopo mas entregavam ~20. Chapter counting inflado para parecer impressionante — mentira de marketing que viola o princípio de honestidade.

### Details
- Escopo original: 30 capítulos prometidos
- Entrega real: ~20 capítulos (faltavam: política CWS, produção de vídeo, UGC, concorrentes, LTV, first-party data, offline conversion)
- Problema: "skeleton impressive, muscle thin" — design visual bonito esconde conteúdo raso
- Causa raiz: contagem inflada para valor percebido, não para entrega real

### Suggested Action
NUNCA inflar contagem de capítulos/seções para parecer mais impressionante. Entregar exatamente o que foi prometido, ou mais — nunca menos. Aplicar这个 padrão a todo output.

### Metadata
Source: Análise adversarial do próprio produto — e-book LexPilot
Related Files: G:\Extensão\LexPilot\
Tags: honesty, chapter-counting, marketing, integrity, critical
Pattern-Key: honest-delivery-tracking

## [ERR-20260717-002] config

**Logged**: 2026-07-17T18:30:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: LexPilot
**Area**: config

### Summary
Dependências usadas no código mas não declaradas no pyproject.toml: `openai` (rag/embeddings.py) e `PyMuPDF` (pipeline/extractor.py). Poderiam causar `ModuleNotFoundError` em novo clone.

### Details
- `openai` importado em `lexpilot/rag/embeddings.py` mas não em nenhum optional group
- `PyMuPDF` (fitz) importado em `lexpilot/pipeline/extractor.py` mas não em nenhum optional group
- Grupo `llm` declara langchain mas nunca é importado no código
- Grupo `vector` declara qdrant-client (usado corretamente)

### Fix
Adicionar `openai` e `PyMuPDF` ao pyproject.toml (obrigatórias ou em group `core`). Remover `langchain*` do grupo `llm` se não for usado.

### Metadata
Source: Gap analysis em 2026-07-17
Related Files: pyproject.toml, lexpilot/rag/embeddings.py, lexpilot/pipeline/extractor.py
Tags: dependencies, pyproject, missing-deps, configuration
Pattern-Key: dependency-audit
