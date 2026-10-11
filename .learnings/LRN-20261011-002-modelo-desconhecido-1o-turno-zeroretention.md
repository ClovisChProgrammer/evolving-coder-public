# LRN-20261011-002 — Modelo desconhecido no 1º turno exige sucessor zero-retention

- **Data:** 2026-10-11
- **Status:** active
- **Priority:** high
- **Project:** evolving-coder
- **Area:** meta / model-routing / privacidade
- **Pattern-Key:** modelo-desconhecido-1o-turno-zeroretention
- **Tags:** model-routing, privacidade, zero-retention, fallback, primeiro-turno, plugin

## Contexto

`model-fallback.js` registra o modelo real de uma sessão via `message.updated`
(`props.primaryModel`). No **primeiro turno**, nenhuma mensagem de assistente
existe ainda → `s.primaryModel` vazio → o código usava `DEFAULT_MODEL`
(`mimo-v2.6-flash-free`, privacy=training). Se esse turno falhava com erro
retryable (429/5xx), o `selectSuccessor` partia de "mimo falhou" e podia escolher
qualquer modelo training/trial — inclusive para uma sessão do agente `privado`
(SB/LC), cujo replay carrega o **prompt original do usuário** (dado sensível).

## Verificação no SDK

`@opencode-ai/sdk/dist/gen/types.gen.d.ts`:
- `EventSessionCreated/Updated` → `properties.info: Session`.
- `Session` NÃO possui `modelID`/`providerID` (só id, projectID, directory, title,
  time, summary). Ou seja: o plugin não consegue saber o modelo configurado pelos
  eventos de sessão.

## Fix aplicado (falha-fechada)

1. `unknownModel = !s.primaryModel` no handler de `session.error`.
2. Quando desconhecido: `selectSuccessor(..., requireZeroRetention=true)` → só
   candidatos com `privacy === "zeroretention"` (SB/LC).
3. `need = {text, image}` (teto dos zeroretention) quando desconhecido, evitando
   "nenhum sucessor" falso para turnos texto-only.
4. Bloco `[RETOMADA]` identifica o modelo como "configurado, ID ainda não
   registrado" em vez do sentinela mimo.

## Trade-offs aceitos

- Sessão **normal** com 1º turno falho também vai para SB/LC até o primeiro
  `message.updated` registrar o modelo real → depois segue o fluxo normal.
- SB/LC são capazes (1M ctx, text+image) — degradação aceitável para esse caso raro.

## Aplicação futura

- Se o SDK passar a expor o modelo configurado na `Session`, trocar a heurística
  por captura direta em `session.created` (código mais preciso, mesmo trade-off).

## Metadata

Source: sessão 2026-10-11 (eliminação total de pendências)
Related Files: `~/.config/opencode/plugins/model-fallback.js`, `skills/evolving-coder/.learnings/LRN-20261011-001`