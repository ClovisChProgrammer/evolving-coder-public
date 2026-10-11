# 2026-08-23 — Presence: Cache Negativo Perpétuo no Viewer + Estado Shutdown Sem Emissor

## Contexto
Dois relatos do Clóvis sobre KAI:Presence: (1) label PENSANDO com foto da calma persistindo mesmo após o asset `kai-expr-pensando.png` correto existir em disco (criado 11:22); (2) ao encerrar sessão (>SD + "CÂMBIO FECHADO · SESSÃO ENCERRADA"), a presença deveria mudar para sono (`kai-expr-sono.png`) e não fazia.

## Causa Raiz
Bug 1: `resolveAsset()` no kai-presence.html cacheava resultado negativo **para sempre** (`assetCache.set(expr, null)` sem TTL). Webview do VS Code vive enquanto a janela vive — página nunca recarrega quando só o JSON muda. Asset criado depois do load → cache já tinha `null` → `applyAsset(null)` não troca `portrait.src` → foto anterior (calma) ficava congelada sob o label novo. Agravante: sem cache-busting na URL, bytes velhos de placeholder podiam ser servidos pelo cache HTTP sob a mesma URL.
Bug 2: estado `"shutdown"` existia na tabela STATES dos dois viewers (HTML + sprite) mas **nenhum emissor o produzia** — plugin só emitia idle/reading/working/thinking/speaking/error.

## Solução Aplicada
- HTML: `CACHE_BUST` por load da página nas URLs probeadas (mata cache HTTP cross-restart); negative cache com TTL de 15s (`NEG_TTL_MS`) — asset adicionado é adotado em ≤15s sem reload; stale-watchdog não reverte `shutdown` → idle.
- Plugin v1.3: detector de assinatura final no stream de texto (`message.part.updated`, part.type="text") com buffer rolante de 400 chars + normalização NFD (resistente a split de delta e acentos): exige "cambio fechado" AND "sessao encerrada" (variantes "reta final" ou câmbio simples NÃO dormem). Emite `shutdown` force. `session.idle` suprimido enquanto lastWrite.state==="shutdown" (senão acordaria 2s depois).
- Sprite: paridade do stale-watchdog (`current_name not in ("idle","shutdown")`).
- QA: node --check (plugin + JS inline), py_compile, testes unitários do detector (4 casos), qa-expressoes.ps1, SHA256 pensando≠calma.

## Lição
**Cache negativo sem TTL em viewer longevo = estado fantasma permanente**: qualquer resolução lazy de asset precisa re-tentar (TTL curto), pois webviews/sidebar views vivem indefinidamente. **Estado declarado no consumer mas nunca emitido pelo producer é bug silencioso**: auditar paridade emitter↔consumer ao criar estado novo. Detecção de frase no stream exige buffer rolante + normalização (deltas quebram frases no meio).

## Status: resolved
