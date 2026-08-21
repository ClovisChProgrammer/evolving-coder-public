## [LRN-20260821-002] api

**Logged**: 2026-08-21T17:30:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: api

### Summary
Mapeamento completo do cenário de geração gratuita de imagem via API em ago/2026, durante a criação do auto-retrato KAI v2. Único serviço gratuito funcional: Pollinations.ai (Flux), com aderência fraca a prompts complexos.

### Details
- **OpenRouter**: ZERO modelos de imagem com sufixo `:free` (verificado ao vivo: 45 modelos de imagem, todos pagos ~$0.003–0.075/imagem). Blog oficial confirma "Not at the moment"
- **Pollinations.ai**: gratuito real sem chave (`image.pollinations.ai/prompt/{prompt}?model=flux&seed=N&nologo=true`). Funciona, mas: resolução anônima limitada (~627×940 apesar de pedir 1024×1536), aderência fraca (dropa objetos segurados, texturas finas de pele, direções incomuns de cabelo), artefatos em olhos
- **Pollinations zimage**: pior que flux nos mesmos prompts
- **AI Horde** (crowdsourced): gratuito real, API async (`generate/async` → `check/{id}` → `status/{id}`, apikey `0000000000`, endpoint de modelos é `/v2/status/models`). MAS workers com detector NSFW geram falsos positivos em estética etérea (pele translúcida + corpo inteiro) mesmo com pedido SFW e roupa descrita → substituem por placeholder "CENSORED" (metadata: type=censorship, value=nsfw)
- **Gemini**: free tier zerado para imagem (ver LRN-20260821-001); **MiniMax**: créditos gratuitos inacessíveis na prática

### Suggested Action
Para retrato canônico de alta fidelidade no futuro: (a) API paga ~$0.003–0.07/imagem (OpenRouter/MiniMax) ou (b) geração local ComfyUI/A1111 exigindo GPU NVIDIA dedicada + disco livre. Enquanto isso, texto do prompt = cânon da identidade visual.

### Metadata
Source: sessão auto-retrato KAI v2 (2026-08-21)
Related Files: assets/kai-self-portrait-prompt-v2.md, assets/kai-self-portrait-v2.png
Tags: pollinations, ai-horde, openrouter, image-generation, free-tier, censorship, flux
Pattern-Key: free-image-gen-landscape-2026

---

## [LRN-20260724-001] config

**Logged**: 2026-07-24T14:30:00-03:00
**Priority**: critical
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
Plugin evolving-coder.js injetava 38KB (SKILL.md + SOUL.md + AGENTS.md) a cada chamada de API, causando HTTP 500 do backend big-pickle por exceder limite de contexto.

### Details
- Plugin hook `experimental.chat.system.transform` injetava 3 arquivos no system prompt de CADA chamada
- Total pré-conversa chegava a ~83KB (~23.000 tokens)
- Backend big-pickle retornava HTTP 500 quando contexto excedia limite
- Erro começou em 22/jul/2026 conforme contexto cresceu
- Solução: consolidar em SKILL.md único (7.2KB), mover procedimentos para arquivos sob demanda

### Suggested Action
Manter monitoramento do tamanho do SKILL.md. Se crescer além de 10KB, recortar novamente. Arquivos sob demanda em references/ devem ser consultados pelo modelo apenas quando necessário.

### Metadata
Source: diagnostic session 2026-07-24
Related Files: plugins/evolving-coder.js, SKILL.md, references/skillwatch-protocol.md, references/reanalyse-procedure.md, references/aprenda-procedure.md
Tags: plugin, context-optimization, http-500, big-pickle, performance
Pattern-Key: context-budget-management

---

## [LRN-20260724-002] config

**Logged**: 2026-07-24T15:05:00-03:00
**Priority**: critical
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
Campo `permission` no opencode.json em formato array causava crash na inicialização do OpenCode com erro "Expected PermissionActionConfig | object | undefined".

### Details
- Formato inválido: `"permission": [{"permission":"edit","pattern":"...","action":"allow"}]`
- Schema do OpenCode aceita apenas: string (`"allow"`) ou objeto (`{"edit": "allow"}`)
- Array não é um tipo válido para PermissionConfig
- Correção: remover campo permission (defaults) ou usar formato objeto

### Suggested Action
Ao editar opencode.json, NUNCA usar array para `permission`. Usar formato objeto:
```json
"permission": {
  "edit": "allow",
  "bash": "ask"
}
```
Arquivo de recuperação: `FIRSTAID_CONFIG.json` + `FIRSTAID_CONFIG.md`

### Metadata
Source: diagnostic session 2026-07-24
Related Files: opencode.json, FIRSTAID_CONFIG.json, FIRSTAID_CONFIG.md
Tags: permission, config, crash, opencode-json, schema
Pattern-Key: permission-format-validation

---

## [LRN-20260725-001] meta

**Logged**: 2026-07-25T10:15:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: meta

### Summary
Análise NC da skill self-learning-skills (kulaxyz, 912 stars). Decisão: não instalar, absorver seletivamente apenas anti-secrets. Resto adiado por falta de demanda.

### Details
- Skill self-learning: meta-skill reativa que captura "golden paths" e cria skills automaticamente
- Promotion Rule de 3 critérios (check passando + falha nomeada + dead-end) é excelente mas nunca precisamos — pipeline de extração nunca foi usado (0 skills extraídas)
- Triage skill/memory/skip já fazemos implicitamente com LEARNINGS/ERRORS/FEATURE_REQUESTS
- Anti-secrets rule: refinamento valioso — "nunca escreva valores, apenas o local onde vivem"
- Custo de instalação completa: +190 tokens/chamada + conflito com APR existente
- Decisão NC: implementar apenas anti-secrets (+50 tokens) + criar CHANGES.md para histórico

### Suggested Action
Reavaliar instalação completa quando: (1) pipeline de extração for usado pela 1a vez, (2) projetos longos acumularem golden paths, (3) OpenCode suportar hooks nativos (UserPromptSubmit/PostToolUse).

### Metadata
Source: sessão NC com Clóvis 2026-07-25
Related Files: SKILL.md, AGENTS.md, global-rules.md, CHANGES.md
Tags: self-learning, nc-protocol, deferral, anti-secrets, meta-decision
Pattern-Key: selective-method-integration

---

## [LRN-20260724-003] integration

**Logged**: 2026-07-24T15:30:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: integration

### Summary
Integração seletiva do Fable Method: formato INTENT absorvido no V3RA, Triviality gate adicionado. Plugin opencode-fable-method descartado por incompatibilidade.

### Details
- Fable Method (Sahir619/fable-method): 4 skills, 260+ eval runs, MIT
- opencode-fable-method (attawitcto): plugin OpenCode port, 0 stars, incompatível (@opencode-ai/plugin 1.14.48 vs nosso 1.4.6)
- Eval do Fable: lift maior em modelos fracos (Haiku), nulo em modelos fortes (Opus)
- INTENT gate = maior lift comprovado: `código faz X; teste espera Y; spec diz Z`
- V3RA existente era genérico (Análise/Julgamento/Resposta). Agora tem formato INTENT estruturado
- Triviality gate: bypass para tarefas triviais (<10 linhas, 1 arquivo, sem busca)
- SKILL.md: 7.2KB → 8.4KB (+1.2KB). Dentro do budget de 10KB

### Decisões
- Plugin opencode-fable-method NÃO instalado (versão incompatível, sem adoção, risco de estourar contexto)
- Fable Method NÃO integrado como sistema paralelo (conflito com APR/V3RA)
- Apenas formato INTENT + Triviality gate extraídos e integrados
- Backup feito via snapshot.py (snap-20260724133624) antes de qualquer mudança

### Suggested Action
Testar V3RA com formato INTENT em tarefa real. Se não melhorar, reverter via snapshot. Monitorar tamanho do SKILL.md.

### Metadata
Source: REANALISE! + implementação 2026-07-24
Related Files: SKILL.md, references/reanalyse-procedure.md
Tags: fable-method, v3ra, intent-gate, triviality-gate, integration
Pattern-Key: selective-method-integration

---

## [LRN-20260803-001] project

**Logged**: 2026-08-03T16:56:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: inpi-marcas-patentes
**Area**: testing

### Summary
Pytest na raiz do projeto inpi-marcas-patentes coleta `backend/tests/` e falha com `ModuleNotFoundError: No module named 'app.db'` porque o package backend só resolve quando executado de dentro de `backend/`. O CI espelha isso (working-directory por job).

### Details
- `python -m pytest -q` na raiz → ERROR de coleção em `backend/tests/conftest.py`
- `python -m pytest -q` em `backend/` → 22 passam (cwd entra no sys.path)
- `python -m pytest tests -q` na raiz → 144 passam (standalone CLI/GUI)
- Total real: 166 testes, não 145 como consta no README (README desatualizado)
- Migração 002 (coluna `users.preferences`) aplica no dev.db sqlite via `alembic upgrade head`

### Suggested Action
Em projetos com backend/ + testes standalone, validar por diretório (espelhando o CI) em vez de pytest solto na raiz. Atualizar README para refletir arquitetura atual (backend/frontend/docker).

### Metadata
Source: sessão de retomada 2026-08-03
Related Files: .github/workflows/ci.yml, backend/tests/, tests/
Tags: pytest, test-discovery, monorepo, module-not-found
Pattern-Key: per-directory-test-validation

---

## [LRN-20260804-001] ops

**Logged**: 2026-08-04T15:40:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: ops

### Summary
Sessão de 2026-08-03 (inpi-marcas-patentes) crashou antes do FLUSH-final: buffer `.session-stream.md` ficou em estado cru, disparando healthcheck CRITICAL. Recovery manual resolvido; o gap real era o protocolo de inicialização não executar crash recovery automaticamente.

### Details
- Buffer cru continha a última interação da sessão anterior (1 linha), sem marcação `# FLUSHING`/`# FLUSHED`
- O learning técnico já havia sido persistido (LRN-20260803-001) antes do crash → recovery = persistir narrativa faltante (DIARY.md) + marcar `# FLUSHED`
- PROTOCOL.md §3.7 já mandava executar crash recovery no início de sessão, mas `instructions/evolving-coder.md` (ponto de entrada autocontido) não tinha esse passo → KAI não acionava
- Fix: passo 9 adicionado ao init protocol — healthcheck CRITICAL de buffer dispara recovery automático (casos b/c/d do §3.7) + re-check antes de responder

### Suggested Action
Manter o init protocol autocontido. Se nova dimensão de integridade surgir no healthcheck, adicionar o recovery correspondente ao protocolo de inicialização — não apenas ao healthcheck.

### Metadata
Source: REANALISE! + crash recovery 2026-08-04
Related Files: instructions/evolving-coder.md, PROTOCOL.md, .session-stream.md, DIARY.md
Tags: crash-recovery, buffer, startup, healthcheck, ops
Pattern-Key: startup-crash-recovery

---

## [LRN-20260805-001] ops

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: high
**Status**: pending_review
**Project**: inpi-marcas-patentes
**Area**: ops

### Summary
Quando uma URL externa falha ou devolve redirecionamento (Docusaurus responde 308 sem a barra final), tentar o fallback de adicionar um documento canônico ao fim do caminho — `index.html` (ou `index.htm`) — antes de desistir. Buscar o HTML cru via `Invoke-WebRequest` ou httpx com `follow_redirects=True` + User-Agent de navegador costuma funcionar onde o webfetch falha.

### Details
- `https://datajud-wiki.cnj.jus.br/api-publica/acesso/` → **308 Permanent Redirect** (webfetch não resolve o loop de redirecionamento)
- `https://datajud-wiki.cnj.jus.br/api-publica/acesso/index.html` → 200 OK (14.683 bytes, HTML minificado em 1 linha)
- Invoke-WebRequest (`[System.Net.WebClient]::DownloadString`) trouxe o HTML cru do Docusaurus; extração via regex sobre o texto sem tags
- Padrão reutilizável: sites em Docusaurus/VitePress/SPA estática servem o documento na rota `/dir/` como `/dir/index.html`

### Suggested Action
Em qualquer integração web: 1) URL sem barra/308 → tentar `index.html`/`index.htm`; 2) preferir fetch de HTML cru com User-Agent de navegador e seguir redirects; 3) nunca martelar retry sem reportar (global-rules #1). Ver `references/url-access-fallback.md`.

### Metadata
Source: integração DataJud 2026-08-05
Related Files: references/url-access-fallback.md, src/datajud_client.py
Tags: web-access, docusaurus, redirect, 308, index-html
Pattern-Key: url-access-fallback

---

## [LRN-20260805-002] scraping

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: medium
**Status**: pending_review
**Project**: inpi-marcas-patentes
**Area**: tests

### Summary
Extrair valores de HTML minificado em uma linha exige regex com âncora explícita de terminação. Sem o `={1,2}` final (e sem remover tags antes), o padrão `APIKey\s+(...)` casava guloso e capturava texto além do token (`cDZHY...==AnteriorTermo`).

### Details
- Solução: remover tags (`re.sub(r"<[^>]+>", "", html)`) → depois `re.findall(r"Authorization:\s*APIKey\s+([A-Za-z0-9+/]+={1,2})", texto, re.IGNORECASE)`
- O sufixo base64 `={1,2}` (padding) delimita o fim do token e evita o casamento guloso do `+`
- Páginas podem conter placeholders (`[Chave Pública]`) além do valor real → pegar a **última** ocorrência via `findall` (os placeholders não casam porque não têm padding base64)
- Testes com fixture do HTML real (positivo + negativo) sem rede → determinístico

### Suggested Action
Ao extrair tokens/valores de HTML minificado: remover tags primeiro, ancorar o fim do padrão com um caractere/classe válido do formato (ex.: padding base64 `={1,2}`), e escolher a ocorrência por posição quando houver placeholders. Testar com fixture local, nunca dependendo da rede.

### Metadata
Source: integração DataJud 2026-08-05
Related Files: src/datajud_client.py, tests/test_datajud_key.py, references/url-access-fallback.md
Tags: regex, scraping, html-minified, base64, placeholder
Pattern-Key: html-extraction-anchor-regex

---

## [LRN-20260805-003] ops

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: medium
**Status**: pending_review
**Project**: inpi-marcas-patentes
**Area**: ops

### Summary
Rebuild do PyInstaller falha com `PermissionError: [WinError 5] Acesso negado: '...\\dist\\SigmaFlow.exe'` quando instâncias antigas do exe ainda estão em execução. Antes do rebuild: matar os processos (e validar o smoke matando-os também ao final).

### Details
- 2 instâncias antigas (PIDs 5252, 19372) seguravam o lock do exe → `python -m PyInstaller SigmaFlow.spec --noconfirm --clean` falhava no WinError 5
- Fix: `Get-Process SigmaFlow -ErrorAction SilentlyContinue | Stop-Process -Force` antes de rebuildar
- Empacotamento do release: `robocopy dist\data release\SigmaFlow-v6.1.0\data /MIR` + `Compress-Archive` (zip ~185 MB, menor que a soma dos arquivos)

### Suggested Action
Em builds Windows, matar processos do artefato antes de rebuildar; usar `robocopy`/`Compress-Archive` para pacote portátil (zip ganha compressão). Adicionar `Stop-Process` ao pre-build sempre que o exe já tiver sido executado.

### Metadata
Source: rebuild SigmaFlow 2026-08-05
Related Files: SigmaFlow.spec, scripts/, release/
Tags: pyinstaller, winerror-5, file-lock, robocopy, release
Pattern-Key: windows-exe-file-lock

---

## [LRN-20260806-001] config

**Logged**: 2026-08-06T20:10:00-03:00
**Priority**: critical
**Status**: pending_review
**Project**: memoagenda
**Area**: config

### Summary
Em projetos Android/Gradle no Windows com path não-ASCII (ex.: `G:\Extensão`), o AGP corrompe o path para mojibake (`Extensǜo`) no `build_model.json` e o build nativo CMake/jni falha com "Expected output file at ... but there was none" mesmo com o `.so` gerado. Causa raiz: **JDK 17 decodifica paths com cp1252**. Fix definitivo no `android/gradle.properties`:

```
org.gradle.jvmargs=... -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8
systemProp.file.encoding=UTF-8
systemProp.sun.jnu.encoding=UTF-8
```

### Details
- 4 camadas de falha encadeadas pelo path acentuado: (1) AGP bloqueia path não-ASCII → `android.overridePathCheck=true`; (2) cache incremental do Kotlin corrompe path → `kotlin.incremental=false`; (3) flutter_local_notifications exige desugaring → `isCoreLibraryDesugaringEnabled=true` + `coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.4")`; (4) **a mais traiçoeira**: o ninja produzia o `libdartjni.so` corretamente, mas a validação do AGP procurava em `G:\Extensǜo\...` (mojibake) → "Expected output file ... but there was none"
- Evidência: `build/jni/intermediates/cxx/Debug/<hash>/logs/arm64-v8a/build_model.json` continha `soFolder: "G:\\Extensǜo\\..."`; os logs ninja ficavam vazios (0 bytes) porque a falha era pós-build, na validação
- Foi preciso rodar `gradlew :jni:buildCMakeDebug --rerun-tasks` isolado para expor a cadeia; o `--stacktrace` revelou o `GradleException: Expected output file at ... but there was none`
- O fix de encoding exigiu reiniciar o daemon (`gradlew --stop`) para os novos jvmargs valerem

### Suggested Action
**Sempre que um build Android/Gradle falhar com "Expected output file ... but there was none" ou paths mojibake (`Extensǜo`)**: forçar UTF-8 no daemon (`file.encoding` + `sun.jnu.encoding` nos jvmargs E como systemProp) antes de qualquer outra investigação. Isso é o fix de causa raiz; `overridePathCheck` e `kotlin.incremental=false` são paliativos complementares. Aplicável a QUALQUER projeto Java/Gradle no Windows com path não-ASCII.

### Metadata
Source: build APK MemoAgenda 2026-08-06
Related Files: android/gradle.properties, android/app/build.gradle.kts, AGENTS.md (MemoAgenda)
Tags: gradle, agp, non-ascii-path, utf-8, cmake, jni, mojibake, windows
Pattern-Key: gradle-utf8-nonascii-path

---

## [LRN-20260806-002] integration

**Logged**: 2026-08-06T20:10:00-03:00
**Priority**: high
**Status**: pending_review
**Project**: memoagenda
**Area**: integration

### Summary
O `flutter_local_notifications` v22 mudou a API para **named parameters** e o `flutter_timezone` v5 retorna objeto `TimezoneInfo` (não String). Além disso, o plugin **exige core library desugaring** no Android — sem isso o build falha com "Dependency ':flutter_local_notifications' requires core library desugaring to be enabled" no `CheckAarMetadataWorkAction`.

### Details
- v22: `initialize(settings: ...)`, `zonedSchedule(id: ..., scheduledDate: ..., notificationDetails: ..., androidScheduleMode: ...)`, `cancel(id: ...)` — **não aceita mais args posicionais** (erro `extra_positional_arguments_could_be_named`)
- `FlutterTimezone.getLocalTimezone()` agora retorna `TimezoneInfo`; usar `.identifier` para `tz.getLocation(info.identifier)`
- Desugaring: em `android/app/build.gradle.kts` → `compileOptions.isCoreLibraryDesugaringEnabled = true` + dependência `coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.4")`
- `tz.TZDateTime.from(when, tz.local)` funcionou (não é o que quebrou), mas construir via `TZDateTime(local, y, m, d, h, min, ...)` é equivalente e explícito

### Suggested Action
Ao usar flutter_local_notifications v22+: consultar a assinatura real das APIs (named params) em vez de confiar na v19/v21. Sempre ativar desugaring ANTES de integrar o plugin. flutter_timezone: tratar `TimezoneInfo`, não String.

### Metadata
Source: análise + fix MemoAgenda 2026-08-06
Related Files: lib/core/notifications/notification_service.dart, android/app/build.gradle.kts, pubspec.yaml
Tags: flutter, flutter-local-notifications, v22, breaking-change, desugaring, timezone, named-parameters
Pattern-Key: fln-v22-api-desugaring

---

## [LRN-20260806-003] ops

**Logged**: 2026-08-06T20:10:00-03:00
**Priority**: high
**Status**: pending_review
**Project**: memoagenda
**Area**: ops

### Summary
Kit de sobrevivência para Flutter em path não-ASCII no Windows (`G:\Extensão`): compilação Kotlin falha sem `kotlin.incremental=false`; AGP bloqueia path não-ASCII sem `android.overridePathCheck=true`; `flutter analyze` crasha (LSP FormatException) → usar `dart analyze`; `build_runner` precisa de `--force-jit` (AOT do Dart falha no path acentuado).

### Details
- O path acentuado quebra 4 toolchains diferentes (AGP, Kotlin, Dart AOT, Dart LSP) de formas distintas — documentar tudo em AGENTS.md do projeto é obrigatório
- `flutter test` roda normalmente (10/10), `dart analyze` sai "No issues found!"
- Primeiro build: ~10 min (baixa CMake 3.22.1 + NDK 28.2.13676358); builds seguintes ~3 min

### Suggested Action
Ao trabalhar em qualquer projeto Flutter sob path não-ASCII no Windows: registrar no AGENTS.md do projeto os 4 workarounds (overridePathCheck, kotlin.incremental=false, --force-jit, dart analyze). Evitar `flutter analyze` (crasha). NÃO remover as linhas de gradle.properties já corrigidas.

### Metadata
Source: sessão MemoAgenda 2026-08-06
Related Files: AGENTS.md (MemoAgenda), android/gradle.properties
Tags: flutter, non-ascii-path, build_runner, force-jit, dart-analyze, windows, kotlin
Pattern-Key: flutter-nonascii-path-survival-kit

---

## [LRN-20260815-001] extension

**Logged**: 2026-08-15T12:50:00-03:00
**Priority**: high
**Status**: resolved
**Project**: rf-readfast
**Area**: extension

### Summary
Páginas PDF da Biblioteca Virtual Pearson são renderizadas como `<img>` (sem texto no DOM), mas a API `GET /publicacao/pagina/{id}/{pagina}` retorna `pageText` (mesmo campo usado pelo TTS do leitor). Esse é o caminho correto para extração de texto — não o DOM.

### Details
- Hook em `fetch`/`XHR` no mundo MAIN (`document_start`, `all_frames`) intercepta `/publicacao/pagina/{id}/{page}` e repassa via `CustomEvent('rf-page-captured')`
- Envelope da resposta: `.data.data` (helper `unwrap`)
- Anti-cópia do leitor é só `contextmenu.preventDefault()` (fraco) — extração via API pública do próprio leitor
- Sem token: `GET /publicacao/pagina/183205/37` → 401; com Bearer → 200
- Capturar `Authorization` no momento do request (XHR: hook em `setRequestHeader`; fetch: `init.headers` ou `Request.headers`), mantendo em memória apenas

### Suggested Action
Ao integrar com a BV Pearson: usar interceptação de rede no mundo MAIN, nunca scrape do DOM. Reutilizar o cache `chrome.storage.local` (`rf_pg_<id>_<pag>`) para evitar refetch. Não usar `chrome.storage.session` de content script (access level não permite).

### Metadata
Source: sessão RF-ReadFast 2026-08-15
Related Files: content/inject-main.js, content/bv-main.js
Tags: chrome-extension, mv3, bvirtual, interceptacao, rsvp, pageText
Pattern-Key: bvirtual-pageextraction-via-api

---

## [LRN-20260815-002] extension

**Logged**: 2026-08-15T12:55:00-03:00
**Priority**: high
**Status**: resolved
**Project**: rf-readfast
**Area**: extension

### Summary
Motor RSVP/Spritz v1 validado em node (sem build toolchain): ORP `min(len-1, max(2, round(len*0.36)))` sobre letras, pausas por pontuação (`.?!…` ×3, `,;:–—` ×2, paraEnd ×2,5) e rescale de velocidade em playback (`restante × antigo/novo`).

### Details
- Tokenização: dividir por `\n\n+` (parágrafos) e por `\s+` (unidades), anexando pontuação à palavra
- ORP posicional absoluto = índice da enésima letra na string (ignora pontuação/parênteses de abertura)
- Modo simples = agrupar ~3 palavras por chunk, fator = soma das pausas (paraEnd ×2,5 no último)
- Testes node: `orpIndex`, len, paraEnd, `_durOf`, jump/next/prev com clamp, rescale OK
- `node --check` em todos os JS (Chrome/MV3 não compilam — validar sintaxe assim)

### Suggested Action
Sempre testar o motor em node antes de carregar no Chrome. Caminho `E:\Extensão\` (acento) não afeta JS puro/Chrome — problema de path não-ASCII é específico de toolchains Java/Dart.

### Metadata
Source: sessão RF-ReadFast 2026-08-15
Related Files: rsvp/engine.js, rsvp/ui.js
Tags: rsvp, spritz, orp, tokenizacao, node-check, mv3
Pattern-Key: rsvp-engine-node-testable

---

## [LRN-20260815-003] extension

**Logged**: 2026-08-15T13:00:00-03:00
**Priority**: medium
**Status**: pending_review
**Project**: rf-readfast
**Area**: ops

### Summary
Auto-avanço entre páginas do leitor Pearson precisa de anti-loop rígido: detectar página atual (`input[type=range][aria-valuenow]` ou texto "página X de Y"), clicar no botão "próxima" (fallback `ArrowRight`), verificar que a página mudou, com watchdog ~8s → fetch direto da API e limite de 2 tentativas antes de parar.

### Details
- Páginas sem `pageText` (somente imagem) → avisar e interromper (não loopar)
- Correlação de respostas: apenas capturas com `page != lastLoadedPage` são aceitas durante avanço
- Comunicar fallback direto pela API via evento `rf-fetch-page` + `rf-state` (ponte para recuperar `bookId` sem expor token)
- Clipboard em 3 camadas (Clipboard API → execCommand → modal) por causa de restrições de permissão em iframe/isolated world

### Suggested Action
Em campo: confirmar se `aria-label` dos botões de navegação e o seletor de página (range) correspondem ao leitor real; se divergirem, refinar `findNavButton`/`detectCurrentPage`.

### Metadata
Source: sessão RF-ReadFast 2026-08-15
Related Files: content/bv-main.js
Tags: auto-advance, anti-loop, watchdog, aria-label, bvirtual
Pattern-Key: reader-autoadvance-anti-loop

---

## [LRN-20260815-004] extension

**Logged**: 2026-08-15T15:10:00-03:00
**Priority**: high
**Status**: resolved
**Project**: rf-readfast
**Area**: extension

### Summary
O leitor real da BV Pearson é o SPA de `leitor.bvirtual.com.br` aberto DENTRO de `plataforma.bvirtual.com.br/Leitor/*` (a URL nunca vira leitor). Content scripts do leitor registrados só para `leitor.bvirtual.com.br` (com `all_frames:false`) nunca rodaram; na casca da plataforma o background injetou o fluxo genérico → o player abriu ATRÁS do livro (z-index). Além disso o F12/DevTools está DESABILITADO nas páginas do leitor.

### Details
- Fix frame-agnóstico: `manifest.json` registra `engine+ui+bv-main` também em `https://plataforma.bvirtual.com.br/Leitor/*`, ambos com `all_frames:true`
- Detecção de frame por sinal de captura: `inject-main.js` grava `window.__rfSawPageData = true` ao entregar página real; `bv-main.js` ativa-se pelo flag (imediato) ou por marcadores de leitor (range, findNavButton, canvas, classes Pdf) no host leitor (espera ~4 s) — a casca da plataforma nunca ativa só por marcadores (evita painel duplo)
- `CustomEvent` não atravessa frames → todo o diálogo conteúdo↔interface deve ocorrer no frame do leitor
- F12 bloqueado → diagnóstico deve aparecer no PAINEL (botão ℹ), não no console; `isTopFrame`, `hostname`, `sawPageData` e `readerMarkers` foram adicionados ao diag
- `isReaderUrl()` no background agora trata `plataforma.bvirtual.com.br/Leitor/*` como leitor (popup abre o fluxo do livro, não o genérico)
- Pedido de UX: âncora ORP (letra vermelha) sempre no centro horizontal da área de leitura, independente de paridade do número de letras → `.rf-word{display:flex;justify-content:center;width:100%}` + `.rf-inner` + medida `getBoundingClientRect` + `translateX(centroContainer−centroAncora)`; `z-index:2147483647`

### Suggested Action
Em SPAs hospedados em iframe sob outro host: registrar content scripts para AMBOS os hosts com `all_frames:true`, usar um sinal de captura (`__rfSawPageData`) em vez de heurística de URL para saber em qual frame agir, e nunca abrir UI por cima de iframe de outro documento (montar no frame do leitor). Sempre prever diagnóstico no próprio UI quando DevTools estiver bloqueado no site-alvo.

### Metadata
Source: teste real do usuário + REANALISE 2026-08-15
Related Files: manifest.json, content/bv-main.js, content/inject-main.js, background/service.js, rsvp/ui.js
Tags: iframe, spritz, anchor-center, frame-agnostic, devtools-blocked, bvirtual
Pattern-Key: iframe-spa-frame-agnostic-content-script

---

## [LRN-20260815-005] extension

**Logged**: 2026-08-15T17:20:00-03:00
**Priority**: critical
**Status**: resolved
**Project**: rf-readfast
**Area**: extension

### Summary
Em MV3, content script no mundo MAIN e outro no mundo ISOLATED NÃO compartilham variáveis JS (`window.__rfSawPageData` setada no MAIN é invisível no ISOLATED) — mas compartilham o DOM e eventos (`CustomEvent` cruza mundos). Além disso, `chrome.tabs.sendMessage(tab.id, ...)` só alcança o frame TOPO; para iframes é preciso `chrome.webNavigation.getAllFrames` + `sendMessage(..., {frameId})`.

### Details
- Sintoma: usuário recarregou extensão + página e o comportamento ficou "absolutamente igual" — ativação por flag de janela nunca disparava no mundo isolado
- Fixes: (1) sinal via DOM `document.documentElement.setAttribute('data-rf-saw'/'data-rf-captures')`; (2) ativação pelo primeiro `CustomEvent('rf-page-captured')` bem-sucedido (eventos atravessam mundos; só o doc que chama a API do leitor emite); (3) `getAllFrames` + `frameId` para rotear mensagens a subframes; (4) **nunca injetar fluxo genérico em URL de leitor** (era o painel de colar atrás do PDF); (5) erro claro no popup quando nenhum frame responde
- Prova de recarga: subir VERSION no manifest E no service worker E exibir no popup (usuário achava que tinha recarregado; versão visível elimina a dúvida)
- Diagnóstico sem DevTools (bloqueado no leitor): popup roda `chrome.scripting.executeScript` (mundo MAIN, `frameIds` de todos os frames via getAllFrames) e lista por frame `url/isTop/saw/captures/hook/markers/panel` — `func` de executeScript é serializada e NÃO pode referenciar closures do service worker (inline tudo)
- Minha Biblioteca = leitor VitalSource (`epubcfi/...`, texto no DOM) — plataforma distinta da Pearson (PDF → texto via API); cada plataforma precisa de host_permissions + content script próprios

### Suggested Action
Ao integrar content scripts em mundos diferentes: comunicar via DOM/atributos ou CustomEvent, NUNCA por globais de janela. Para atingir iframes: sempre `getAllFrames` + `frameId` no `sendMessage`. Para sites com DevTools bloqueado: construir diagnóstico próprio no popup (executeScript MAIN allFrames) ANTES de tentar calibrar seletores às cegas. Manter versão visível no popup para validar recarga da extensão.

### Metadata
Source: 2º teste real do usuário + diagnóstico 2026-08-15
Related Files: background/service.js, content/bv-main.js, content/inject-main.js, popup/popup.js
Tags: mv3, isolated-world, main-world, frameId, webNavigation, custom-event, diagnostics, vitalsource
Pattern-Key: mv3-world-isolation-and-frame-routing

---

## [LRN-20260819-001] config

**Logged**: 2026-08-19T13:25:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
Arquivo `.env` criado pelo PowerShell com `Out-File -Encoding utf8` inclui BOM (Byte Order Mark `\xEF\xBB\xBF`) silenciosamente. A chave `GOOGLE_API_KEY` é lida como `﻿GOOGLE_API_KEY` (com BOM) e não casa com a lista de variáveis válidas no módulo gemini.py — resultando em "GOOGLE_API_KEY not found" mesmo com a chave presente no arquivo.

### Details
- `Out-File -Encoding utf8` no PowerShell 5.1 gera UTF-8 COM BOM (diferente do PowerShell 7+)
- O parser de `.env` do opencode-vision lê a linha `﻿GOOGLE_API_KEY=valor` e extrai key=`﻿GOOGLE_API_KEY` (com BOM)
- A verificação `if k in API_KEY_ENV_VARS` falha porque `﻿GOOGLE_API_KEY` != `GOOGLE_API_KEY`
- Fix: usar `[System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))` para escrever sem BOM
- Verificação: `$bytes[0..2] -ne 0xEF,0xBB,0xBF` ou `python -c "print(repr(open('.env','rb').read()[:10]))"`

### Suggested Action
Ao criar `.env` no Windows PowerShell: NUNCA usar `Out-File` ou `Set-Content -Encoding utf8` (ambos geram BOM). Usar sempre `[System.IO.File]::WriteAllText()` com `UTF8Encoding::new($false)`. Verificar BOM com leitura binária antes de entregar.

### Metadata
Source: instalação opencode-vision 2026-08-19
Related Files: ~/.config/opencode/.env, opencode-vision/gemini.py
Tags: bom, utf-8, powershell, env-file, api-key, encoding
Pattern-Key: env-file-bom-powershell

---

## [LRN-20260819-002] config

**Logged**: 2026-08-19T14:00:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
A quota free tier do Google Gemini API para geração de imagem é extremamente restritiva (limite 0 para requests diários em todos os modelos de imagem: gemini-2.5-flash-image, 3.1-flash-image, 3-pro-image). A quota é vinculada à conta Google Cloud, não à chave API individual — duas chaves do mesmo projeto compartilham a mesma quota.

### Details
- Testadas 2 chaves Google API: ambas com quota de imagem esgotada
- Chaves funcionam normalmente para texto (gemini-3.6-flash OK)
- Modelos de imagem testados: gemini-2.5-flash-image, gemini-3.1-flash-image, gemini-3-pro-image, gemini-3.1-flash-lite-image — todos 429 RESOURCE_EXHAUSTED
- Erro detalhado: `GenerateRequestsPerDayPerProjectPerModel-FreeTier` com limite 0
- A quota reseta diariamente (meia-noite PT)
- Para geração de imagem imediata: MiniMax Token Plan (mmx-cli já instalado, pendente MINIMAX_API_KEY) ou habilitar billing no Google AI Studio

### Suggested Action
Para geração de imagem: (1) verificar quota antes de tentar — chamada de teste simples; (2) ter alternativa (MiniMax) como fallback; (3) considerar billing do Google para quota maior; (4) não gastar tokens testando modelos esgotados repetidamente.

### Metadata
Source: sessão 2026-08-19
Related Files: ~/.config/opencode/.env, opencode-vision/gemini.py
Tags: google, gemini, quota, free-tier, image-generation, rate-limit
Pattern-Key: gemini-image-quota-free-tier

---

## [LRN-20260819-003] svg

**Logged**: 2026-08-19T23:00:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: svg

### Summary
CSS `transform-origin` não funciona confiavelmente em elementos SVG cross-browser. Para animação rotacional de mandalas SVG, usar o atributo SVG `transform` com `translate(CX,CY) rotate(R) scale(S)` — a rotação acontece em coordenadas locais (0,0) antes da translação.

### Details
- CSS `transform: rotate(Xdeg)` no SVG funciona em Chrome mas falha em Firefox/Safari para centering
- CSS `transform-origin: 50% 50%` no SVG é ignorado ou calculado diferente por browser
- Solução robusta: `transform="translate(250,250) rotate(R) scale(S)"` no elemento SVG
- Ordem importa: translate primeiro, depois rotate, depois scale
- Para mandala com groups aninhados: group externo faz translate+rotate, grupos internos fazem rotate individual por anel
- `clip-path: circle(R% at X% Y%)` DEVE usar `%` não `px` — pixel values quebram quando SVG renderiza em tamanho diferente do viewBox

### Suggested Action
Sempre usar SVG `transform` attribute para animação de elementos SVG. Nunca confiar em CSS transform para centering de SVG. Para clip-path em SVG, sempre usar unidades `%`.

### Metadata
Source: sessão 2026-08-19 (mandala studio)
Related Files: assets/algorithmic-art/mandala-studio.html
Tags: svg, css, transform, centering, clip-path, cross-browser, animation
Pattern-Key: svg-transform-attribute-not-css

---

## [LRN-20260819-004] audio

**Logged**: 2026-08-19T23:00:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: audio

### Summary
Direção do sync entre animação e áudio binaural importa: o_usuário_ deve controlar a animação (velocidade de rotação), e a Hz binaural deve derivar disso. O inverso (Hz controla animação) é contra-intuitivo porque o usuário perde agência sobre o visual.

### Details
- Implementação original: slider `baseHz` controlava tanto a Hz binaural quanto a velocidade da animação
- Problema: usuário quer controlar a rotação visualmente, não através de um slider de frequência
- Solução correta: Hz = rotateSpeed × hzMult — o multiplicador (0.1-5.0x) é o único slider novo
- Fórmula: 1.0x rot × 1.5 mult = 1.5 Hz (Theta), 3.0x × 2.0 = 6.0 Hz (Alpha)
- Range útil: 0.5-15 Hz cobre Delta→Alpha (maioria dos estados de meditação)

### Suggested Action
Ao sincronizar áudio com animação, sempre perguntar: "O que o usuário quer controlar diretamente?" — isso deve ser o input primário. A另一个 coisa deve ser calculada, não o inverso.

### Metadata
Source: sessão 2026-08-19 (mandala studio)
Related Files: assets/algorithmic-art/mandala-studio.html
Tags: audio, binaural, animation, sync, ux, user-agency
Pattern-Key: audio-animation-sync-direction

---

## [LRN-20260821-001] api

**Logged**: 2026-08-20T23:59:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: api

### Summary
Em ago/2026 o Google zerou o limite free tier de geracao de imagem na API Gemini (todas as familias: 2.5-flash-image, 3.x-flash-image, 3-pro-image). O 429 retorna "limit: 0" - o limite em si e zero, nao uma cota diaria esgotada. Esperar reset diario NAO resolve.

### Details
- Erro tipico: HTTP 429 GenerateRequestsPerDayPerProjectPerModel-FreeTier ... limit: 0
- ListModels ainda lista os modelos de imagem (metadados funcionam) - isso sozinho nao significa que ha cota livre
- Diagnostico correto: 429 com limit:0 em DUAS familias diferentes = remocao do free tier, nao esgotamento
- 404 em modelos antigos (gemini-2.0-flash-preview-image-generation) indica rotacao/deprecacao de modelos image
- Alternativas viaveis: MiniMax (mmx CLI ja instalado, falta MINIMAX_API_KEY) ou billing pago no Google
- Sintaxe PowerShell: passar --jq complexo ao gh quebra no PS 5.1; usar gh api URL > file.json + ConvertFrom-Json

### Suggested Action
Ao ver 429 com limit: 0 na API Gemini: nao re-tentar nem esperar meia-noite PT. Confirmar com ListModels + teste em segunda familia, entao migrar para outro provedor (MiniMax) ou habilitar billing.

### Metadata
Source: sessao 2026-08-20/21 (auto-retrato v2)
Related Files: assets/kai-self-portrait-prompt-v2.md
Tags: gemini, api, quota, free-tier, image-generation, 429, minimax, mmx
Pattern-Key: gemini-free-tier-image-zeroed
