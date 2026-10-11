# LRN-20261010-001 — Fallback de modelo free com handoff adaptativo

- **Data:** 2026-10-10
- **Status:** active
- **Tags:** opencode, plugin, fallback, model-routing, handoff, zen-free

## Contexto

Modelos free do OpenCode Zen falham sem aviso (`FreeUsageLimitError`/429) e congelam o processamento. Clóvis queria: (1) detecção da falha, (2) troca automática para o próximo free, (3) o sucessor "pegar o fio da meada" — retomando no ponto exato, com um log dos últimos passos para o novo modelo consultar.

## O que foi aprendido

1. **Free ≠ créditos.** Free do Zen é $0/token; o modo de falha real é rate-limit (429), não saldo esgotado. Detector de "créditos" nunca dispararia.
2. **O SDK do OpenCode permite o replay completo:** `session.error` (evento), `client.session.promptAsync` com `model:{providerID,modelID}` explícito (replay com modelo trocado), `client.tui.showToast`, e `tool.execute.after`/`message.part.updated`/`todo.updated` como fontes de handoff. Verificado nos `.d.ts` locais de `@opencode-ai/sdk`, não em README de terceiro.
3. **Handoff contínuo > log manual.** Capturar passos (tool), texto em voo (part.updated) e plano (todos) continuamente, e congelar o snapshot no erro, resolve o "fio da meada" sem depender de o usuário escrever checkpoint.
4. **Sucessor por capacidades, não por ordem fixa:** matriz (modalidade, ctx/saída, privacidade, especialidade) + regra "nunca rebaixar classe de privacidade" (decisão de Clóvis). Tarefa com vídeo → só successors omni; zero-retention nunca cai para training.
5. **Limitação de plataforma é dura:** OpenCode não troca modelo dentro de stream falho. A retomada possível é: histórico preservado + bloco [RETOMADA] instruindo reiniciar a unidade em voo. Turno interrompido não volta.

## Erro de premissa do usuário (e meu, antes)

"Acabar os créditos" — inexistente no free. "Novo modelo entra cego" — não entirely: a sessão é preservada; só o turno falho se perde. Corrigir a premissa antes de projetar é obrigatório (formato INTENT).

## REANALISE! pós-fase (3 defeitos reais em plugin "testado")

- (P0) Captura gravava em bucket `global` mas replay lia por `sessionID` → handoff sairia vazio. Lesson: **testar o caminho de leitura E escrita com o mesmo identificador**.
- (P1) `message.updated` properties tem só `info`; `sessionID` vive dentro de `info.sessionID`. Meu teste passou `sessionID` inventado em properties → **falso positivo**. Lesson: simular eventos com a forma EXATA dos `.d.ts` locais, nunca com a forma que eu acho que existe.
- (P2) Mapa de sessões sem TTL → vazamento em processo longo. Lesson: todo cache em plugin de processo longo precisa de cleanup.

## Aplicação futura

- Se Clóvis relatar "troca de modelo sozinha" → é o plugin funcionando; ver `plugins/model-fallback-debug.log` e `.model-fallback-handoff.json`.
- Se relatar "falhou e não trocou" → checar: erro era retryable? cadeia esgotada (anti-loop 3/10min)? toast de erro mostra o caso.
- Modelo default é `opencode/mimo-v2.6-flash-free`; trocar default exige editar `opencode.json` (backup naming: `opencode.json.bak-<motivo>-<data>`).
