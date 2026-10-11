# 2026-08-24 — Lições do build REFATORE (opencode 1.18.21, Windows)

## L1 — PowerShell 5.1 grava UTF-8 COM BOM
`Set-Content -Encoding UTF8` / `Add-Content` emitem BOM (EF BB BF). `JSON.parse` quebra ("Unexpected token '���'").
**Regra:** gravar JSON sempre com `[System.IO.File]::WriteAllText($p, $s, [System.Text.UTF8Encoding]::new($false))`; no leitor JS, `.replace(/^\uFEFF/, "")`. Detectado porque o guard passava tudo em silêncio (fail-open) — teste offline 5/5 pegou.

## L2 — permission.ask NÃO dispara com defaults allow
O hook só é invocado quando a resolução de permissão resulta em "ask". Config global sem bloco permission = edits/bash allow = zero asks = plugin mudo.
**Regra:** enforcement real de política independente da config usa `tool.execute.before` + `throw new Error(...)` (mecanismo oficial, docs/plugins exemplo .env-protection). Manter permission.ask como camada extra quando houver asks configurados.

## L3 — Subagentes custom não aparecem em sessões abertas antes do registro
Agentes criados em ~/.config/opencode/agents/ só entram no Task tool de sessões iniciadas depois. Fallback: orquestrador executa com disciplina documentada + independência preservada na re-auditoria via `opencode run` headless (sessão LLM separada de verdade).

## L4 — chat.message vs skill-matching
Run headless com "REFATORE ." executou o fluxo mesmo sem evidência de trigger.log: o modelo carrega a skill pela descrição quando a mensagem bate. Trigger plugin = camada determinística extra (dedupe por id `refatore-${messageID}` contra dupla injeção).

## L5 — Guard EXECUTE: escopo de destruição
Destructive bash liberado APENAS dentro do bkpDir DA execução (nunca irmãos em BKP/) — protege execuções vizinhas. Edits em EXECUTE: projectRoot + bkpDir; fora disso bloqueado.

## L6 — opencode run headless carrega skill E agente registrados (CONFIRMADO em produção)
Na re-audit do kai-presence, a sessão `opencode run` exibiu "Skill refatore" + agente `refatore-reauditor` carregados e executando checklist adversarial real (leu BASELINE/AUDIT/PLAN, rodou diff, conferiu SHA256 dos blindados vs BASELINE). Valida a arquitetura L2/L3 do REFATORE end-to-end.

## L7 — opencode run falha intermitente de infraestrutura
Tentativa 1: UnknownError server (err_27470db5). Tentativa 2: timeout 120s (agente carregou mas não terminou). Tentativa 3 (~4min): sucesso completo. **Regra:** registrar cada tentativa em MANIFEST.commands (FAIL_xxx/PASS); até 3 tentativas antes de fallback orquestrador-disciplinado; avisar o usuário ANTES ("pode levar ~N min") — regra global de feedback longo.

## L8 — Gate parcial: "ACEITO, execute tudo." ≠ token puro
Mensagem com sufixo não constitui token literal (§27), mas ACEITO sem objeção permite aprovar o PLANO PRINCIPAL; item OPCIONAL que exige escolha explícita (a/b/c sobre conflito pre-existing §18) permanece bloqueado — "tudo" não supre escolha não feita. Executar o inequívoco, declarar premissa, deixar o condicionado pendente.

## L9 — Pre-existing nos alvos ⇒ correção documental primeiro
Com mudanças não commitadas nos arquivos-alvo, editar por cima mistura autorias no diff final (§18). Mitigação conservadora: corrigir o SINTOMA documental (README instruindo layout correto) e deixar a correção estrutural de código (env unificado R-104) condicionada à limpeza do git (commit prévio).