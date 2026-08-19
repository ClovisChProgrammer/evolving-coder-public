# Comando APRENDA! — Procedimento Detalhado

> Este arquivo é lido SOB DEMANDA — quando o usuário digita APRENDA! ou final de projeto é detectado.
> Não é injetado a cada chamada de API.

## Execução

1. **Varra** TODO o contexto da sessão/projeto por:
   - Técnicas ou modos de resolver INÉDITOS (não existentes em `.learnings/`)
   - Soluções MELHORES que as já registradas (refinamento de entry existente)
   - Workarounds para comportamentos inesperados
   - Padrões reutilizáveis entre projetos
   - Preferências confirmadas do usuário
   - Decisões arquiteturais importantes
2. **Compare** com `.learnings/`, `SOUL.md`, `USER.md`, `AGENTS.md` — só registre o que é NOVO ou ESTRITAMENTE MELHOR
3. **Escreva** em `.learnings/` com:
   - ID sequencial, timestamp ISO-8601
   - `Project:` obrigatório
   - Prioridade e categoria adequadas
   - `Status: pending_review`
4. **Promova** automaticamente se:
   - `critical` ou padrão com ≥2 ocorrências → sugestão para SOUL.md/AGENTS.md
   - Skill reutilizável → sugestão de extração via `scripts/extract-skill.ps1`
5. **Confirme**: `✅ APRENDA!: [N] novos registros, [M] sugestões de promoção`

## Detecção Automática de Final de Projeto
Dispara quando:
- Usuário diz: "projeto concluído", "finalizar", "encerrar", "pronto"
- Última tarefa marcada como completa
- Conversa muda de contexto
- Sessão claramente encerrando

## Formato de Entrada em .learnings/

```
## [TIPO-YYYYMMDD-XXX] categoria

**Logged**: ISO-8601
**Priority**: low | medium | high | critical
**Status**: pending | resolved | promoted | pending_review
**Project**: nome-do-projeto
**Area**: frontend | backend | infra | tests | docs | config |
          user_preference | project_context | communication | growth

### Summary
### Details
### Suggested Action
### Metadata (Source, Related Files, Tags, See Also, Pattern-Key)
```

Tipos: `LRN` (learning), `ERR` (error), `FEAT` (feature)

| Status | Significado |
|--------|-------------|
| `pending` | Não abordado ainda |
| `pending_review` | Coletado, aguardando revisão |
| `resolved` | Resolvido ou conhecimento integrado |
| `promoted` | Elevado a SOUL.md, USER.md, AGENTS.md |
| `promoted_to_skill` | Extraído como skill reutilizável |

## Detecção e Registro

| Situação | Arquivo | Categoria |
|----------|---------|-----------|
| Comando/operação falha | ERRORS.md | `error` |
| Usuário corrige você | LEARNINGS.md | `correction` |
| Usuário pede algo inexistente | FEATURE_REQUESTS.md | `feature_request` |
| API/ferramenta externa falha | ERRORS.md | `integration_error` |
| Conhecimento desatualizado | LEARNINGS.md | `knowledge_gap` |
| Abordagem melhor encontrada | LEARNINGS.md | `best_practice` |
| Preferência do usuário descoberta | LEARNINGS.md | `user_preference` |
| Contexto de projeto aprendido | LEARNINGS.md | `project_context` |
