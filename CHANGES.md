# CHANGES.md — System Modification History

> Chronological record of all changes to the evolving-coder system: installations, modifications, removals, deferrals.
> Format: append-only. Never edit old entries. Only add new lines at the end of each date.

---

## 2026-07-25

| Time (UTC) | Type | File/Item | Description | Decision |
|------------|------|-----------|-------------|----------|
| ~13:00 | CREATE | CHANGES.md | Created this history file to track system changes | the developer + the AI |
| ~13:00 | MODIFY | SKILL.md | Anti-secrets reinforced: from "never expose secrets" to "never write real secret values in versioned files — only record where they live" (self-learning rule, ~50 tokens) | the AI (NC plan approved) |
| ~13:00 | DEFER | self-learning absorption (complete plan) | Promotion Rule (3 criteria), Triage skill/memory/skip, Skill authoring spec in extract-skill scripts — deferred due to lack of current demand. Extraction pipeline never used (0 skills extracted). Re-evaluate when first real extraction occurs. | the AI (NC recommendation) |
| ~13:00 | DEFER | aprenda-procedure.md | Detailed Promotion Rule section deferred — depends on actual demand for skill extraction | the AI |
| ~13:00 | DEFER | extract-skill.ps1 / .sh | Improved template (Failure pattern + Verified by + What didn't work) deferred — depends on actual demand | the AI |

### Session Context

- **Initial request:** The developer asked about reactive skills in the library
- **Research:** Analyzed `kulaxyz/self-learning-skills` (912 stars, MIT)
- **NC Analysis:** 6 questions with critical lens → conclusion: don't install, absorb selectively
- **Final decision:** Implement only anti-secrets + create CHANGES.md. Rest deferred.
- **Result:** +~50 tokens in SKILL.md. More secure system, no overload.

---

### Commits

| Hash | Message |
|------|---------|
| `4279e38` | feat: anti-secrets + CHANGES.md + global rule #5 — self-learning absorption (selective) |

<!-- Future entries are added above this line -->

---

## 2026-08-04

| Time (UTC) | Type | File/Item | Description | Decision |
|------------|------|-----------|-------------|----------|
| ~18:38 | RECOVER | `.session-stream.md` | Crash recovery of raw buffer from 2026-08-03 session. FLUSH marked as `# FLUSHED`. | the AI (REANALISE! approved) |
| ~18:38 | MODIFY | `instructions/evolving-coder.md` | Step 9 added: automatic crash recovery at startup (PROTOCOL.md §3.7) when healthcheck reports raw buffer — prevents recurrence of this CRITICAL | the AI (approved) |

---

## 2026-08-05

| Time (UTC) | Type | File/Item | Description | Decision |
|------------|------|-----------|-------------|----------|
| ~20:28 | CREATE | `references/url-access-fallback.md` | On-demand web access recipe: fallback `index.html`/`index.htm` for 308 redirects on static sites, raw HTML fetch, extraction of values from minified HTML with anchored regex | the AI (approved) |
| ~20:28 | MODIFY | `.learnings/LEARNINGS.md` | 3 new entries: LRN-20260805-001 (url-access-fallback), -002 (html-extraction-anchor-regex), -003 (windows-exe-file-lock) — `pending_review` | the AI (approved) |
| ~20:28 | MODIFY | `README.md`, `README_pt-BR.md`, `README_es.md` | `references/` tree corrected — was missing `aprenda-procedure.md`, `reanalyse-procedure.md`, `skillwatch-protocol.md` (listed only 4 of 7 real); added `url-access-fallback.md` | the AI |

---

## 2026-08-06

| Time (UTC) | Type | File/Item | Description | Decision |
|------------|------|-----------|-------------|----------|
| ~23:10 | MODIFY | `.learnings/LEARNINGS.md` | 3 new entries (`pending_review`): LRN-20260806-001 (critical — UTF-8 fix for Gradle non-ASCII paths), -002 (high — flutter_local_notifications v22: named params + desugaring), -003 (high — Flutter non-ASCII path survival kit) | the AI (approved) |

---

## 2026-08-18

| Time (UTC) | Type | File/Item | Description | Decision |
|------------|------|-----------|-------------|----------|
| ~20:05 | MODIFY | `plugins/evolving-coder.js` | Extensible plugin: `tool.execute.after` hook for auto-capture of relevant tools (read/write/edit/bash/grep/glob/webfetch/websearch/task/skill) with `auto:` prefix in buffer; `session.idle` event for `SESSION_IDLE` marker; `FLUSH_READY` marker after ~20 observations; truncation of args (200 chars) and output (500 chars) | the AI (approved) |
| ~20:05 | MODIFY | `instructions/evolving-coder.md` | Step 10 added: detection of `<!-- FLUSH_READY -->` and `<!-- SESSION_IDLE -->` at startup for auto-FLUSH | the AI |
| ~20:05 | MODIFY | `scripts/healthcheck.ps1` | Detection of `AUTO-SESSION`, `FLUSH_READY`, `SESSION_IDLE` states in buffer — no false CRITICAL | the AI |
| ~20:05 | MODIFY | `scripts/kai-retrieval.py` | v2: semantic search via fastembed (BAAI/bge-small-en-v1.5, 384 dims) with cosine similarity; `--query` (semantic), `--query-literal` (legacy keyword), `--build` generates keyword index + embeddings (.npz); automatic fallback to keyword if fastembed unavailable | the AI |
| ~20:05 | CREATE | `scripts/knowledge-embeddings.npz` | Embeddings of 26 entries (DIARY.md + .learnings/) generated via fastembed | the AI |
| ~20:05 | MODIFY | `AGENTS.md` | Auto-capture documentation (buffer, FLUSH_READY, SESSION_IDLE) + semantic retrieval updated | the AI |
| ~20:05 | MODIFY | `PROTOCOL.md` §3.7 | Buffer documented with two modes (auto-capture + manual); crash recovery updated with FLUSH_READY/SESSION_IDLE markers | the AI |
| ~20:05 | MODIFY | `SKILL.md` | Retrieval section updated with --query semantic, --query-literal, --build | the AI |
| ~21:30 | MODIFY | `plugins/evolving-coder.js` | Rewritten in correct V1 format: `EvolvingCoder` export, hooks at root level (no `hooks: {}` wrapper), async function, debug logging in `evolving-coder-debug.log` | the AI (post-deploy diagnosis) |
| ~21:30 | MODIFY | `PROTOCOL.md` §3.7 | Step 6 (rebuild embeddings) added to atomic FLUSH | the AI |
