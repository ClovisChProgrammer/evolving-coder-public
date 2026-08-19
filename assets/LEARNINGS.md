# Learnings

> ⚠️ **TEMPLATE** — Este arquivo contém o formato de referência. Os registros reais ficam em `.learnings/LEARNINGS.md` (dentro do diretório da skill).

Corrections, insights, and knowledge gaps captured during development.

## Categories

**Technical:** correction | insight | knowledge_gap | best_practice

**Personal/Context:** user_preference | project_context | communication | growth

## Areas

frontend | backend | infra | tests | docs | config | user_preference | project_context | communication | growth

## Status Definitions

| Status | Meaning |
|--------|---------|
| `pending` | Not yet addressed |
| `pending_review` | Collected, awaiting user review |
| `in_progress` | Actively being worked on |
| `resolved` | Issue fixed or knowledge integrated |
| `wont_fix` | Decided not to address (reason in Resolution) |
| `promoted` | Elevated to SOUL.md, USER.md, AGENTS.md, or CLAUDE.md |
| `promoted_to_skill` | Extracted as a reusable skill |

## Entry Format (Template — use este formato em .learnings/)

Toda entrada DEVE incluir o campo `Project:` para identificar o contexto de origem:

```markdown
## [LRN-YYYYMMDD-XXX] categoria

**Logged**: ISO-8601
**Priority**: low | medium | high | critical
**Status**: pending | pending_review | resolved | promoted | promoted_to_skill
**Project**: nome-do-projeto (obrigatório)
**Area**: frontend | backend | infra | tests | docs | config | user_preference | project_context | communication | growth

### Summary
### Details
### Suggested Action
### Metadata (Source, Related Files, Tags, See Also, Pattern-Key)

---
```

## Skill Extraction Fields

When a learning is promoted to a skill, add these fields:

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

Example:
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Project**: protomize
**Area**: infra

### Summary
Docker build fails on Apple Silicon due to platform mismatch
...
```

