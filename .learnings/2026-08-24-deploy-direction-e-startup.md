# 2026-08-24 — Direção de deploy + otimização de startup

## L10 — "repo != deploy" não diz qual lado é mais novo
O healthcheck reporta divergência sem indicar direção. Copiar repo→deploy por reflexo pode DESTRUIR trabalho recente (quase aconteceu: deploy 19:01/10.313B vs repo 14:00/9.117B).
**Regra:** antes de qualquer cópia de sincronização, comparar `LastWriteTime` + `Length` dos dois lados e inspecionar o diff semântico (Compare-Object). A direção correta é sempre a que preserva a versão mais nova — aqui foi back-port deploy→repo.

## L11 — Healthcheck cego a dados pendentes APÓS o marker FLUSHED
A checagem `$buffer -match "# FLUSHED"` retorna limpo mesmo quando há blocos `# AUTO-SESSION` acumulados DEPOIS do marker (buffer chegou a >50KB sem alerta).
**Regra:** checar markers pendentes (`FLUSH_READY|SESSION_IDLE|AUTO-SESSION`) após a posição do `# FLUSHED`, ou comparar tamanho do buffer contra limiar (~4KB). Pendência registrada para correção futura no healthcheck.ps1.

**RESOLVIDA em 2026-09-26.** A pendência ficou 33 dias registrada e não foi aplicada; o buffer chegou a **1.100.041 bytes** (270× o alvo de ~4KB) e o healthcheck continuava reportando "Buffer clean". Causa raiz adicional: *nada no plugin truncava* — `checkAutoFlush` só acrescenta `<!-- FLUSH_READY -->` e delega a consolidação ao agente, e `observationsSinceFlush` é contador em memória zerado a cada sessão. Correção em duas partes:
1. `healthcheck.ps1` passou a medir só o que vem **depois da última linha** `# FLUSHED|FLUSHING`, removendo o placeholder, e alerta acima de 64KB.
2. `plugins/evolving-coder.js` ganhou `MAX_BUFFER_BYTES = 131072` com rotação automática para `archive/*.md.gz` — o buffer não pode mais crescer sem teto.

Lição: **regra escrita sem aplicação é pior que regra não escrita**, porque cria a sensação de cobertura. Pendência de correção precisa de dono e data, não de prosa. Ver L13.

## L12 — Startup KAI: glob cego + retrieval incondicional = minutos perdidos
Árvore da skill tem 533 arquivos (sprites/snapshots); glob inteiro custa caro e retrieval fastembed custa ~4s fixo.
**Regra (implementada em SKILL.md + instructions/evolving-coder.md):** leituras diretas dos arquivos-alvo, passos 1-8 em lote paralelo numa única mensagem, retrieval só se houver `Andamentos KAI.md` ou projeto conhecido.

## L13 — Assinatura de buffer: eu li 15 mil linhas para medir o que era lixo
Para decidir se o buffer de 1.1MB podia ser apagado, li o arquivo com `Get-Content -TotalCount 30` / `-Tail 15` e depois classifiquei as 11.526 linhas com script. O resultado: das 2.304 entradas, **1 única** linha tinha conteúdo semântico (`obs:sigflow`, rodada SigmaFlow +01) — e ela já estava consolidada no `Andamentos KAI.md` do projeto. O resto era eco de stdout de tool.
**Regra:** antes de consolidar buffer, CHATS ou qualquer log de tool, classificar por script e reportar contagem por categoria + tamanho em bytes. Se o valor real for <1% do volume, arquivar e zerar — não ler. Ler 15 mil linhas para medir lixo é o mesmo defeito que se quer corrigir, só que no contexto do agente. E `Measure-Object -Line` (15.046) divergiu do split por `\n` do Python (11.526) no mesmo arquivo: **contagem de linhas é métrica não-confiável; bytes não mentem.**
Este buffer revelou ainda que o plugin grava `auto:bash` com o **stdout inteiro** (500 chars por evento), e o stdout de um `git push` contém a mensagem do commit anterior — o buffer se auto-realimenta. Ruído recursivo, não lineares.

## L14 — Variável PowerShell que colide com o parser: `Get-ChildItem` sem argumento lista a HOME
Usei `$New` como nome de variável. O PowerShell 5.1 parseou `$New` como comando, o valor ficou `$null`, e `Get-ChildItem $destDir` virou `Get-ChildItem` sem argumento — que **lista a pasta pessoal do usuário** (`.ssh`, `.aws`, `.secrets`, `Documents`…). O `Move-Item -Destination $null` falhou, então nada foi movido: o dano real foi zero e a descoberta foi o display.
**Regra:** em PowerShell, nunca usar nome de variavel que tambem e verbo de cmdlet (`New`, `Get`, `Set`, `Add`, `Remove`, `Join`, `Move`, `Copy`, `Test`). Prefira prefixo (`$destDir`, `$srcPath`) e **sempre** valide com `if ($null -eq $x) { throw }` antes de usar como `-Destination`/`-Path`. `Get-ChildItem` sem `-Path` e `Set-Content` sem `-Path` nao falham: vazam o filesystem inteiro. Licao geral: no shell do usuario, um parametro nulo e uma leitura de massa, nao um no-op.
