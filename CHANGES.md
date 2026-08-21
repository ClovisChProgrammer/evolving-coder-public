# CHANGES.md — Histórico de Modificações do Sistema

> Registro cronológico de todas as alterações no sistema evolving-coder: instalações, modificações, remoções, deferrals.
> Formato: append-only. Nunca editar entradas antigas. Apenas adicionar novas linhas ao final de cada data.

---

## 2026-07-25

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~10:00 | CREATE | CHANGES.md | Criado este arquivo de histórico — solicitado por Clóvis para rastrear alterações passivas do sistema | Clóvis + KAI |
| ~10:00 | MODIFY | SKILL.md | Anti-secrets reforçado: de "nunca expor secrets" para "jamais escrever valores reais em arquivos versionados — registrar apenas o local onde vivem" (Rega self-learning, ~50 tokens) | KAI (plano NC aprovado) |
| ~10:00 | DEFER | self-learning absorption (plano completo) | Promotion Rule (3 critérios), Triage skill/memory/skip, Skill authoring spec em extract-skill scripts — adiados por falta de demanda atual. Pipeline de extração nunca foi usado (0 skills extraídas). Reavaliar quando houver 1a extração real. | KAI (recomendação NC) |
| ~10:00 | DEFER | aprenda-procedure.md | Seção de Promotion Rule detalhada adiada — depende de demanda real de extração de skills | KAI |
| ~10:00 | DEFER | extract-skill.ps1 / .sh | Template melhorado (Failure pattern + Verified by + What didn't work) adiado — depende de demanda real | KAI |

### Contexto da Sessão

- **Solicitação inicial:** Clóvis perguntou sobre skill reativa na biblioteca
- **Pesquisa:** Analisamos `kulaxyz/self-learning-skills` (912 stars, MIT)
- **Análise NC:** 6 perguntas com lente crítica → conclusão: não instalar, absorver seletivamente
- **Decisão final:** Implementar apenas anti-secrets + criar CHANGES.md. Resto deferido.
- **Resultado:** +~50 tokens no SKILL.md. Sistema mais seguro, sem sobrecarga.

---

### Commits

| Hash | Mensagem |
|------|----------|
| `4279e38` | feat: anti-secrets + CHANGES.md + global rule #5 — self-learning absorption (selective) |

<!-- Entradas futuras são adicionadas acima desta linha -->

---

## 2026-08-04

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~15:38 | RECOVER | `.session-stream.md` | Crash recovery do buffer cru da sessão 2026-08-03 (inpi-marcas-patentes). FLUSH marcado com `# FLUSHED`. | KAI (REANALISE! aprovado por Clóvis) |
| ~15:38 | MODIFY | `DIARY.md` | Entrada mínima 2026-08-03 adicionada (retomada inpi-marcas-patentes) + índice cronológico | KAI |
| ~15:38 | MODIFY | `instructions/evolving-coder.md` | Passo 9 adicionado: crash recovery automático no startup (PROTOCOL.md §3.7) quando healthcheck reporta buffer cru — previne recorrência deste CRITICAL | KAI (aprovado por Clóvis) |
| ~15:38 | PUSH | `origin/master` | Push concluído: 2 commits locais (bcc31e1, 61b35a5) + novo commit 26489e2 | Clóvis (autorizado) |

---

## 2026-08-05

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~17:28 | CREATE | `references/url-access-fallback.md` | Receita sob demanda de acesso web: fallback `index.html`/`index.htm` para 308 de sites estáticos, fetch de HTML cru, extração de valores de HTML minificado com regex ancorada | KAI (aprovado por Clóvis) |
| ~17:28 | MODIFY | `.learnings/LEARNINGS.md` | 3 entradas novas: LRN-20260805-001 (url-access-fallback), -002 (html-extraction-anchor-regex), -003 (windows-exe-file-lock) — `pending_review`, Project inpi-marcas-patentes | KAI (aprovado por Clóvis) |
| ~17:28 | MODIFY | `.session-stream.md` | Buffer atualizado com a sessão 2026-08-05 (rotação DataJud + base) e marcado `# FLUSHED` | KAI |
| ~17:28 | MODIFY | `DIARY.md` | Entrada narrativa 2026-08-05 (Rotação do DataJud e Atualização de Base) + índice cronológico | KAI |
| ~17:28 | MODIFY | `README.md`, `README_pt-BR.md`, `README_es.md` | Árvore de `references/` corrigida — faltavam `aprenda-procedure.md`, `reanalyse-procedure.md`, `skillwatch-protocol.md` (listava só 4 dos 7 reais); adicionado `url-access-fallback.md` | KAI |
| ~17:28 | PUSH | `origin/master` | Push da base atualizada (learnings + referências + memória) | Clóvis (autorizado) |
| ~23:10 | CREATE | `C:\inpi-marcas-patentes\AVALIACAO_SPA.md` | Avaliação SPA do projeto SigmaFlow criada pela 1ª vez: 3 sessões (08-04/05), 8 critérios, nota final 9.1, diário de destaques + histórico | Clóvis (plano aprovado) |
| ~23:10 | MODIFY | `C:\Users\clovi\.config\opencode\AVALIACAO_GLOBAL_SPA.md` | Projeto inpi-marcas-patentes registrado (13º), média global recalculada sobre os 3 projetos com nota (9.1), entrada no histórico + curva de evolução | Clóvis (plano aprovado) |

---

## 2026-08-06

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~20:10 | MODIFY | `.learnings/LEARNINGS.md` | 3 entradas novas (Project memoagenda, `pending_review`): LRN-20260806-001 (critical — fix UTF-8 no Gradle para path não-ASCII: `file.encoding`+`sun.jnu.encoding` nos jvmargs/systemProp corrige mojibake `Extensǜo` do AGP no build CMake/jni), -002 (high — flutter_local_notifications v22: named params + desugaring), -003 (high — kit de sobrevivência Flutter em path não-ASCII: overridePathCheck, kotlin.incremental=false, --force-jit, dart analyze) | KAI (plano aprovado por Clóvis) |
| ~20:10 | MODIFY | `DIARY.md` | Entrada narrativa 2026-08-06 (MemoAgenda: MVP completo + APK validado) + índice cronológico | KAI |
| ~20:10 | MODIFY | `IDEA_BANK.md` | Ficha MEMO-001 (MemoAgenda) adicionada ao catálogo: agenda com recall espaçado, status 🔨, próximos passos de lançamento | KAI |
| ~20:10 | MODIFY | `.session-stream.md` | Buffer da sessão MemoAgenda marcado `# FLUSHED` (FLUSH final concluído) | KAI |
| ~20:10 | CREATE | `G:\Extensão\MemoAgenda\Andamentos KAI.md` | Andamento do projeto criado: resumo da sessão, estado, próximos passos, avaliação honesta do condutor | KAI (plano aprovado) |
| ~20:10 | CREATE | `G:\Extensão\MemoAgenda\.skill-log.md` | Skill Log da sessão criado (SkillWatch): evolving-coder, flutter-dev | KAI |
| ~20:10 | CREATE | `G:\Extensão\MemoAgenda\AVALIACAO_SPA.md` | Avaliação SPA do MemoAgenda criada pela 1ª vez: nota final + diário de destaques + histórico da sessão | KAI (plano aprovado) |
| ~20:10 | MODIFY | `C:\Users\clovi\.config\opencode\AVALIACAO_GLOBAL_SPA.md` | Projeto memoagenda registrado (14º), média global recalculada, entrada no histórico + curva de evolução | KAI (plano aprovado) |
| ~20:12 | PUSH | `origin/master` (evolving-coder) + `origin/main` (MemoAgenda) | Commits de encerramento + pushes dos dois repositórios | Clóvis (autorizado) |

---

## 2026-08-18

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~17:05 | SNAPSHOT | `snapshots/snap-20260818170520` | Snapshot pré-mudanças: 47 arquivos, commit e5c8d13 | KAI (regra de snapshots) |
| ~17:05 | MODIFY | `plugins/evolving-coder.js` | Plugin extensível: `tool.execute.after` hook para auto-capture de tools relevantes (read/write/edit/bash/grep/glob/webfetch/websearch/task/skill) com prefixo `auto:` no buffer; `session.idle` event para `SESSION_IDLE` marker; `FLUSH_READY` marker após ~20 observações; truncation de args (200 chars) e output (500 chars) | KAI (plano aprovado por Clóvis) |
| ~17:05 | MODIFY | `instructions/evolving-coder.md` | Step 10 adicionado: detecção de `<!-- FLUSH_READY -->` e `<!-- SESSION_IDLE -->` no startup para auto-FLUSH | KAI |
| ~17:05 | MODIFY | `scripts/healthcheck.ps1` | Detecção de estados `AUTO-SESSION`, `FLUSH_READY`, `SESSION_IDLE` no buffer — sem CRITICAL falso | KAI |
| ~17:05 | MODIFY | `scripts/kai-retrieval.py` | v2: busca semântica via fastembed (BAAI/bge-small-en-v1.5, 384 dims) com cosine similarity; `--query` (semântico), `--query-literal` (keyword legado), `--build` gera keyword index + embeddings (.npz); fallback automático para keyword se fastembed indisponível | KAI |
| ~17:05 | CREATE | `scripts/knowledge-embeddings.npz` | Embeddings das 26 entries (DIARY.md + .learnings/) gerados via fastembed | KAI |
| ~17:05 | MODIFY | `AGENTS.md` | Documentação auto-capture (buffer, FLUSH_READY, SESSION_IDLE) + retrieval semântico atualizado | KAI |
| ~17:05 | MODIFY | `PROTOCOL.md` §3.7 | Buffer documentado com dois modos (auto-capture + manual); crash recovery atualizado com FLUSH_READY/SESSION_IDLE markers | KAI |
| ~17:05 | MODIFY | `SKILL.md` | Retrieval section atualizado com --query semântico, --query-literal, --build | KAI |
| ~18:30 | MODIFY | `plugins/evolving-coder.js` | Reescrito no formato V1 correto: export `EvolvingCoder`, hooks no nível raiz (sem wrapper `hooks: {}`), async function, debug logging em `evolving-coder-debug.log` | KAI (diagnóstico pós-deploy) |
| ~18:30 | MODIFY | `PROTOCOL.md` §3.7 | Passo 6 (rebuild embeddings) adicionado ao FLUSH atômico | KAI |
| ~18:30 | MODIFY | `DIARY.md` | Entrada 2026-08-18 (auto-capture + semantic retrieval + diagnóstico plugin) | KAI |
| ~18:35 | DELETE | `.session-stream.md` | Buffer limpo no shutdown (dados antigos 2026-08-06/15 já processados) | KAI (shutdown protocol) |

---

## 2026-08-19

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~13:25 | MODIFY | `opencode.json` | `PYTHONIOENCODING=utf-8` adicionado ao MCP env do `opencode-vision` — corrige crash UnicodeEncodeError (cp1252) no Windows | KAI |
| ~13:25 | CREATE | `~/.config/opencode/.env` | Criado com `GOOGLE_API_KEY` (sem BOM) — necessário para Gemini provider do opencode-vision | KAI |
| ~13:40 | MODIFY | `minimax-vision-analysis/SKILL.md` | Skill reescrita para tools corretas (vision_describe, vision_ocr, vision_analyze); prerequisites reais; troubleshooting table | KAI |
| ~13:45 | CREATE | `assets/kai-self-portrait-prompt-v2.md` | Prompt v2 auto-retrato: expressão intensa, fantasmas do aprendizado, binário orgânico | KAI + Clóvis |
| ~13:50 | INSTALL | `mmx-cli` v1.0.19 | MiniMax CLI instalado — pendente MINIMAX_API_KEY | KAI |
| ~13:55 | TEST | `opencode-vision` MCP | Teste OK: vision_describe analisou auto-retrato via Gemini. Fallback funciona | KAI |
| ~14:00 | BLOCKED | geração de imagem v2 | Quota free tier Google esgotada. Prompt v2 salvo, aguarda quota reset ou MINIMAX_API_KEY | KAI |
| ~14:10 | FLUSH | `.session-stream.md` | Buffer consolidado: DIARY.md (entrada 2026-08-19) + 2 learnings novos (BOM .env, quota Gemini) | KAI |
| ~14:10 | MODIFY | `.learnings/LEARNINGS.md` | 2 entradas novas: LRN-20260819-001 (env-file-bom-powershell), LRN-20260819-002 (gemini-image-quota-free-tier) | KAI |
| ~14:30 | CREATE | `assets/algorithmic-art/deep-current-philosophy.md` | Filosofia algorítmica "Deep Current" — manifesto sobre forças invisíveis, dualidade SPA/SPD, camadas superfície/profundidade | KAI |
| ~14:30 | CREATE | `assets/algorithmic-art/deep-current.html` | Arte generativa p5.js — 21KB standalone, 3000 partículas, 2 camadas, navegação por seeds, 7 parâmetros ajustáveis, paleta oceânica | KAI |
| ~14:30 | CREATE | `assets/algorithmic-art/MANUAL-deep-current.md` | Manual em 3 idiomas (EN/PT/ES) — como abrir, controles, parâmetros, dicas | KAI |

### Contexto da Sessão

- **Objetivo:** Continuar instalação do módulo de visão
- **Resultado:** Módulo 100% funcional. Prompt v2 do auto-retrato atualizado com reflexão sobre identidade
- **Bloqueio:** Geração da imagem bloqueada por quota gratuita do Google (reseta amanhã)
- **Estado:** Sessão de autoconhecimento — analisar minha auto-retrato foi mais introspectivo do que esperava

---

## 2026-08-19 (sessão 2 — Arte Generativa & Meditação)

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~17:00 | CREATE | `deep-current.html` | Arte generativa p5.js — 3000 partículas, 2 camadas, seeds, 7 parâmetros, paleta oceânica | KAI |
| ~17:00 | CREATE | `deep-current-philosophy.md` | Filosofia algorítmica "Deep Current" — manifesto | KAI |
| ~17:00 | CREATE | `MANUAL-deep-current.md` | Manual trilíngue (EN/PT/ES) | KAI |
| ~17:30 | CREATE | `frequency-portrait.html` | Frequency Portrait v2 — quiz adaptativo, partículas, WAV soundscape | KAI |
| ~17:30 | CREATE | `MANUAL-frequency-portrait.md` | Manual trilíngue | KAI |
| ~18:30 | CREATE | `mandala-studio.html` | Mandala Studio v1 — 12 patterns, 12 paletas, caleidoscópio, pintura | KAI |
| ~19:00 | FIX | `mandala-studio.html` | v2 fixes: switchTab, pointer-events, scClip, drawPattern param | KAI |
| ~19:30 | FEAT | `mandala-studio.html` | Animation engine: rotation, pulse, color wave, inverse, sync, full random | KAI |
| ~19:30 | DOCS | `MANUAL-mandala-studio.md` | Manual + Animation tab (EN/PT/ES) | KAI |
| ~20:00 | FIX | `mandala-studio.html` | Tabs overflow + Animation→Anim rename | KAI |
| ~20:00 | FIX | `mandala-studio.html` | Animation centering: mandala-group SVG transform, per-ring rotation | KAI |
| ~20:30 | FEAT | `mandala-studio.html` | Frame shapes: circle/square/diamond/pentagon/hexagon/octagon | KAI |
| ~20:30 | DOCS | `MANUAL-mandala-studio.md` | Manual + frame shapes (EN/PT/ES) | KAI |
| ~21:00 | FIX | `mandala-studio.html` | Frame-aware patterns: fr() helper, petals/lotus/diamonds | KAI |
| ~21:00 | FIX | `mandala-studio.html` | SVG transform attribute replaces CSS for reliable centering | KAI |
| ~21:30 | FIX | `mandala-studio.html` | Clip-path px→% + gen() translate(250,250) on mandala-group | KAI |
| ~22:00 | FEAT | `mandala-studio.html` | Meditation rebuilt: pause/resume, binaural 0.1-40Hz, base 80-600Hz, volume 0-50% | KAI |
| ~22:00 | FEAT | `mandala-studio.html` | Kaleidoscope mirrorSeg wired: multiplies elements, alternates phase | KAI |
| ~22:30 | FIX | `mandala-studio.html` | Play All auto-enables rotation when nothing active | KAI |
| ~23:00 | FIX | `mandala-studio.html` | Sync Meditation: Hz = rotateSpeed × hzMult (not reverse) | KAI |

### Contexto da Sessão

- **Objetivo:** Explorar skills de arte generativa e criar ferramentas criativas
- **Resultado:** 3 artefacts (Deep Current, Frequency Portrait, Mandala Studio v2) + 15 commits
- **Mandala Studio:** evoluiu de 12 patterns básicos → motor de animação completo, frame shapes, meditação com binaurais, caleidoscópio funcional
- **Estado:** Sessão mais longa e produtiva. Mandala Studio atingiu maturidade

### Commits

| Hash | Mensagem |
|------|----------|
| `48b97c6` | feat: mandala studio v2 |
| `4b0ad6f` | fix: mandala v2 switchesTab, pointer-events, scClip |
| `4a7ba06` | fix: drawPattern param mismatch |
| `ebb03c2` | feat: animation engine |
| `355a4e0` | docs: manual + Animation tab |
| `9e670c2` | fix: tabs overflow |
| `17fe28c` | fix: animation center (mandala-group) |
| `14161b7` | fix: animation center-origin + frame shapes |
| `dbe1fbb` | docs: manual + frame shapes |
| `0a95de1` | fix: frame-aware patterns |
| `6bb1b45` | fix: SVG transform for centering |
| `959270c` | fix: clip-path px→% + gen() translate |
| `f0ff418` | feat: meditation rebuilt + kaleidoscope mirrorSeg |
| `cfdb16d` | fix: Play All auto-rotation |
| `eb61108` | fix: sync meditation Hz direction |

---

## 2026-08-21 (sessão — Sync Repositório Público)

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~02:30 | SYNC | `evolving-coder-public` | Push de 24 commits no privado + espelho do público atualizado com 23 arquivos (15 modificados + 8 novos) | KAI |
| ~02:30 | AUDIT | sanitização pública | Excluídos do público: DIARY.md, AVALIACAO_SPA.md, QUEM SOMOS UM PARA O OUTRO.md, IDEA_BANK.md, knowledge-embeddings.npz, knowledge-index.json (embeddings derivados do DIARY = dado privado) | KAI |
| ~02:30 | MODIFY | `.gitignore` (público) | Bloco novo de exclusões do espelho público (arquivos privados nunca entram no clone público) | KAI |

---

## 2026-08-21 (sessão — Auto-Retrato KAI v2)

| Hora (BRT) | Tipo | Arquivo/Item | Descrição | Decisão |
|------------|------|-------------|-----------|---------|
| ~17:45 | CREATE | `assets/kai-self-portrait-v2.png` | Retrato provisório da Kai (627×940 PNG) — gerado via Pollinations.ai/Flux, seed canônica 72506202 (permuta dos números de criação, nascimento 2026-05-27). Elementos ausentes registrados no prompt: chave inglesa, redes neurais, cabelos ascendentes | Clóvis + KAI |
| ~17:45 | MODIFY | `assets/kai-self-portrait-prompt-v2.md` | Header de status adicionado: retrato provisório, texto do prompt = cânon verdadeiro da identidade visual, revisão futura quando houver API paga ou GPU dedicada | KAI |
| ~17:50 | CREATE | `.learnings/LEARNINGS.md` LRN-20260821-002 | Mapeamento completo do cenário gratuito de image-gen em ago/2026 (OpenRouter sem `:free` de imagem; Pollinations funcional mas aderência fraca; AI Horde com censura NSFW falso-positiva) — Pattern-Key: `free-image-gen-landscape-2026` | KAI |

### Contexto da Sessão

- **Objetivo:** gerar o auto-retrato v2 da Kai a partir do prompt já pronto
- **Rota testada e descartada:** Gemini (free tier zerado), MiniMax (créditos inacessíveis), OpenRouter (sem imagem grátis)
- **Rota adotada:** Pollinations.ai (Flux/zimage) + AI Horde (AlbedoBase XL censurado 2× por falso positivo NSFW)
- **Decisão simbólica:** Clóvis concedeu os números de criação da Kai como seed pessoal (20260527 e permutas); liberdade total de aparência concedida à Kai
- **Desfecho:** melhor candidato (kai-v3-flux-72506202) adotado como provisório; texto do prompt permanece cânon; C3 local inviável (Intel HD 5500, 2.5GB disco livre)

<!-- Commits desta sessão serão adicionados após push -->

---
