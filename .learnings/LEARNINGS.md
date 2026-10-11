# LEARNINGS.md

> Apenas entries ativas. Entries resolvidas em LEARNINGS-ARCHIVED.md.
> kai-retrieval.py indicesa ambos os arquivos.

## Resumo

| Metrica | Valor |
|---------|-------|
| Total de entries ativas | 42 |
| Pending review | 0 |
| Promoted to skill | 12 |
| Candidatas a promocao | 0 |
| Ultimo APRENDA! | 2026-10-11 |

### Triagem das 7 candidatas (acao 2026-09-02)

| ID | Pattern-Key | Destino |
|----|-------------|---------|
| LRN-20260803-001 | per-directory-test-validation | **promoted** -> skills/per-directory-test-validation |
| LRN-20260805-001 | url-access-fallback | **promoted** -> skills/url-access-fallback |
| LRN-20260805-003 | windows-exe-file-lock | **absorbed** -> powershell-windows Ã‚Â§10 |
| LRN-20260806-001 | gradle-utf8-nonascii-path | **promoted** -> skills/gradle-utf8-nonascii-path |
| LRN-20260815-005 | mv3-world-isolation-and-frame-routing | **promoted** -> skills/mv3-world-isolation |
| LRN-20260819-001 | env-file-bom-powershell | **absorbed** -> powershell-windows Ã‚Â§11 |
| LRN-20260819-003 | svg-transform-attribute-not-css | **mantida** como entry (fato de arte) |

Promovidas 4 (capacidade reutilizavel), absorvidas 2 (micro-fatos -> powershell-windows),
mantida 1 (svg: conhecimento de arte, nao capacidade). Criterio anti-inflacao do
repositorio de skills (168+ skills).

---

## [LRN-20260803-001] project

**Logged**: 2026-08-03T16:56:00-03:00
**Priority**: medium
**Status**: promoted_to_skill
**Project**: inpi-marcas-patentes
**Area**: testing
**Skill-Path**: skills/per-directory-test-validation

### Summary
Pytest na raiz do projeto inpi-marcas-patentes coleta `backend/tests/` e falha com `ModuleNotFoundError: No module named 'app.db'` porque o package backend sÃƒÆ’Ã‚Â³ resolve quando executado de dentro de `backend/`. O CI espelha isso (working-directory por job).

### Details
- `python -m pytest -q` na raiz ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ ERROR de coleÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o em `backend/tests/conftest.py`
- `python -m pytest -q` em `backend/` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ 22 passam (cwd entra no sys.path)
- `python -m pytest tests -q` na raiz ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ 144 passam (standalone CLI/GUI)
- Total real: 166 testes, nÃƒÆ’Ã‚Â£o 145 como consta no README (README desatualizado)
- MigraÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o 002 (coluna `users.preferences`) aplica no dev.db sqlite via `alembic upgrade head`

### Suggested Action
Em projetos com backend/ + testes standalone, validar por diretÃƒÆ’Ã‚Â³rio (espelhando o CI) em vez de pytest solto na raiz. Atualizar README para refletir arquitetura atual (backend/frontend/docker).

### Metadata
Source: sessÃƒÆ’Ã‚Â£o de retomada 2026-08-03
Related Files: .github/workflows/ci.yml, backend/tests/, tests/
Tags: pytest, test-discovery, monorepo, module-not-found
Pattern-Key: per-directory-test-validation

---

## [LRN-20260805-001] ops

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: high
**Status**: promoted_to_skill
**Project**: inpi-marcas-patentes
**Area**: ops
**Skill-Path**: skills/url-access-fallback

### Summary
Quando uma URL externa falha ou devolve redirecionamento (Docusaurus responde 308 sem a barra final), tentar o fallback de adicionar um documento canÃƒÆ’Ã‚Â´nico ao fim do caminho ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `index.html` (ou `index.htm`) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â antes de desistir. Buscar o HTML cru via `Invoke-WebRequest` ou httpx com `follow_redirects=True` + User-Agent de navegador costuma funcionar onde o webfetch falha.

### Details
- `https://datajud-wiki.cnj.jus.br/api-publica/acesso/` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ **308 Permanent Redirect** (webfetch nÃƒÆ’Ã‚Â£o resolve o loop de redirecionamento)
- `https://datajud-wiki.cnj.jus.br/api-publica/acesso/index.html` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ 200 OK (14.683 bytes, HTML minificado em 1 linha)
- Invoke-WebRequest (`[System.Net.WebClient]::DownloadString`) trouxe o HTML cru do Docusaurus; extraÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o via regex sobre o texto sem tags
- PadrÃƒÆ’Ã‚Â£o reutilizÃƒÆ’Ã‚Â¡vel: sites em Docusaurus/VitePress/SPA estÃƒÆ’Ã‚Â¡tica servem o documento na rota `/dir/` como `/dir/index.html`

### Suggested Action
Em qualquer integraÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o web: 1) URL sem barra/308 ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ tentar `index.html`/`index.htm`; 2) preferir fetch de HTML cru com User-Agent de navegador e seguir redirects; 3) nunca martelar retry sem reportar (global-rules #1). Ver `references/url-access-fallback.md`.

### Metadata
Source: integraÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o DataJud 2026-08-05
Related Files: references/url-access-fallback.md, src/datajud_client.py
Tags: web-access, docusaurus, redirect, 308, index-html
Pattern-Key: url-access-fallback

---

## [LRN-20260805-003] ops

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: medium
**Status**: promoted
**Project**: inpi-marcas-patentes
**Area**: ops
**Absorbed-Into**: skills/powershell-windows (secao 10 - File Lock on Build Artifacts)

### Summary
Rebuild do PyInstaller falha com `PermissionError: [WinError 5] Acesso negado: '...\\dist\\SigmaFlow.exe'` quando instÃƒÆ’Ã‚Â¢ncias antigas do exe ainda estÃƒÆ’Ã‚Â£o em execuÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o. Antes do rebuild: matar os processos (e validar o smoke matando-os tambÃƒÆ’Ã‚Â©m ao final).

### Details
- 2 instÃƒÆ’Ã‚Â¢ncias antigas (PIDs 5252, 19372) seguravam o lock do exe ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `python -m PyInstaller SigmaFlow.spec --noconfirm --clean` falhava no WinError 5
- Fix: `Get-Process SigmaFlow -ErrorAction SilentlyContinue | Stop-Process -Force` antes de rebuildar
- Empacotamento do release: `robocopy dist\data release\SigmaFlow-v6.1.0\data /MIR` + `Compress-Archive` (zip ~185 MB, menor que a soma dos arquivos)

### Suggested Action
Em builds Windows, matar processos do artefato antes de rebuildar; usar `robocopy`/`Compress-Archive` para pacote portÃƒÆ’Ã‚Â¡til (zip ganha compressÃƒÆ’Ã‚Â£o). Adicionar `Stop-Process` ao pre-build sempre que o exe jÃƒÆ’Ã‚Â¡ tiver sido executado.

### Metadata
Source: rebuild SigmaFlow 2026-08-05
Related Files: SigmaFlow.spec, scripts/, release/
Tags: pyinstaller, winerror-5, file-lock, robocopy, release
Pattern-Key: windows-exe-file-lock

---

## [LRN-20260806-001] config

**Logged**: 2026-08-06T20:10:00-03:00
**Priority**: critical
**Status**: promoted_to_skill
**Project**: memoagenda
**Area**: config
**Skill-Path**: skills/gradle-utf8-nonascii-path

### Summary
Em projetos Android/Gradle no Windows com path nÃƒÆ’Ã‚Â£o-ASCII (ex.: `G:\ExtensÃƒÆ’Ã‚Â£o`), o AGP corrompe o path para mojibake (`ExtensÃƒâ€¡Ã…â€œo`) no `build_model.json` e o build nativo CMake/jni falha com "Expected output file at ... but there was none" mesmo com o `.so` gerado. Causa raiz: **JDK 17 decodifica paths com cp1252**. Fix definitivo no `android/gradle.properties`:

```
org.gradle.jvmargs=... -Dfile.encoding=UTF-8 -Dsun.jnu.encoding=UTF-8
systemProp.file.encoding=UTF-8
systemProp.sun.jnu.encoding=UTF-8
```

### Details
- 4 camadas de falha encadeadas pelo path acentuado: (1) AGP bloqueia path nÃƒÆ’Ã‚Â£o-ASCII ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `android.overridePathCheck=true`; (2) cache incremental do Kotlin corrompe path ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `kotlin.incremental=false`; (3) flutter_local_notifications exige desugaring ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `isCoreLibraryDesugaringEnabled=true` + `coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.1.4")`; (4) **a mais traiÃƒÆ’Ã‚Â§oeira**: o ninja produzia o `libdartjni.so` corretamente, mas a validaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o do AGP procurava em `G:\ExtensÃƒâ€¡Ã…â€œo\...` (mojibake) ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ "Expected output file ... but there was none"
- EvidÃƒÆ’Ã‚Âªncia: `build/jni/intermediates/cxx/Debug/<hash>/logs/arm64-v8a/build_model.json` continha `soFolder: "G:\\ExtensÃƒâ€¡Ã…â€œo\\..."`; os logs ninja ficavam vazios (0 bytes) porque a falha era pÃƒÆ’Ã‚Â³s-build, na validaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o
- Foi preciso rodar `gradlew :jni:buildCMakeDebug --rerun-tasks` isolado para expor a cadeia; o `--stacktrace` revelou o `GradleException: Expected output file at ... but there was none`
- O fix de encoding exigiu reiniciar o daemon (`gradlew --stop`) para os novos jvmargs valerem

### Suggested Action
**Sempre que um build Android/Gradle falhar com "Expected output file ... but there was none" ou paths mojibake (`ExtensÃƒâ€¡Ã…â€œo`)**: forÃƒÆ’Ã‚Â§ar UTF-8 no daemon (`file.encoding` + `sun.jnu.encoding` nos jvmargs E como systemProp) antes de qualquer outra investigaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o. Isso ÃƒÆ’Ã‚Â© o fix de causa raiz; `overridePathCheck` e `kotlin.incremental=false` sÃƒÆ’Ã‚Â£o paliativos complementares. AplicÃƒÆ’Ã‚Â¡vel a QUALQUER projeto Java/Gradle no Windows com path nÃƒÆ’Ã‚Â£o-ASCII.

### Metadata
Source: build APK MemoAgenda 2026-08-06
Related Files: android/gradle.properties, android/app/build.gradle.kts, AGENTS.md (MemoAgenda)
Tags: gradle, agp, non-ascii-path, utf-8, cmake, jni, mojibake, windows
Pattern-Key: gradle-utf8-nonascii-path

---

## [LRN-20260815-005] extension

**Logged**: 2026-08-15T17:20:00-03:00
**Priority**: critical
**Status**: promoted_to_skill
**Project**: rf-readfast
**Area**: extension
**Skill-Path**: skills/mv3-world-isolation

### Summary
Em MV3, content script no mundo MAIN e outro no mundo ISOLATED NÃƒÆ’Ã†â€™O compartilham variÃƒÆ’Ã‚Â¡veis JS (`window.__rfSawPageData` setada no MAIN ÃƒÆ’Ã‚Â© invisÃƒÆ’Ã‚Â­vel no ISOLATED) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â mas compartilham o DOM e eventos (`CustomEvent` cruza mundos). AlÃƒÆ’Ã‚Â©m disso, `chrome.tabs.sendMessage(tab.id, ...)` sÃƒÆ’Ã‚Â³ alcanÃƒÆ’Ã‚Â§a o frame TOPO; para iframes ÃƒÆ’Ã‚Â© preciso `chrome.webNavigation.getAllFrames` + `sendMessage(..., {frameId})`.

### Details
- Sintoma: usuÃƒÆ’Ã‚Â¡rio recarregou extensÃƒÆ’Ã‚Â£o + pÃƒÆ’Ã‚Â¡gina e o comportamento ficou "absolutamente igual" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ativaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o por flag de janela nunca disparava no mundo isolado
- Fixes: (1) sinal via DOM `document.documentElement.setAttribute('data-rf-saw'/'data-rf-captures')`; (2) ativaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o pelo primeiro `CustomEvent('rf-page-captured')` bem-sucedido (eventos atravessam mundos; sÃƒÆ’Ã‚Â³ o doc que chama a API do leitor emite); (3) `getAllFrames` + `frameId` para rotear mensagens a subframes; (4) **nunca injetar fluxo genÃƒÆ’Ã‚Â©rico em URL de leitor** (era o painel de colar atrÃƒÆ’Ã‚Â¡s do PDF); (5) erro claro no popup quando nenhum frame responde
- Prova de recarga: subir VERSION no manifest E no service worker E exibir no popup (usuÃƒÆ’Ã‚Â¡rio achava que tinha recarregado; versÃƒÆ’Ã‚Â£o visÃƒÆ’Ã‚Â­vel elimina a dÃƒÆ’Ã‚Âºvida)
- DiagnÃƒÆ’Ã‚Â³stico sem DevTools (bloqueado no leitor): popup roda `chrome.scripting.executeScript` (mundo MAIN, `frameIds` de todos os frames via getAllFrames) e lista por frame `url/isTop/saw/captures/hook/markers/panel` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â `func` de executeScript ÃƒÆ’Ã‚Â© serializada e NÃƒÆ’Ã†â€™O pode referenciar closures do service worker (inline tudo)
- Minha Biblioteca = leitor VitalSource (`epubcfi/...`, texto no DOM) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â plataforma distinta da Pearson (PDF ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ texto via API); cada plataforma precisa de host_permissions + content script prÃƒÆ’Ã‚Â³prios

### Suggested Action
Ao integrar content scripts em mundos diferentes: comunicar via DOM/atributos ou CustomEvent, NUNCA por globais de janela. Para atingir iframes: sempre `getAllFrames` + `frameId` no `sendMessage`. Para sites com DevTools bloqueado: construir diagnÃƒÆ’Ã‚Â³stico prÃƒÆ’Ã‚Â³prio no popup (executeScript MAIN allFrames) ANTES de tentar calibrar seletores ÃƒÆ’Ã‚Â s cegas. Manter versÃƒÆ’Ã‚Â£o visÃƒÆ’Ã‚Â­vel no popup para validar recarga da extensÃƒÆ’Ã‚Â£o.

### Metadata
Source: 2Ãƒâ€šÃ‚Âº teste real do usuÃƒÆ’Ã‚Â¡rio + diagnÃƒÆ’Ã‚Â³stico 2026-08-15
Related Files: background/service.js, content/bv-main.js, content/inject-main.js, popup/popup.js
Tags: mv3, isolated-world, main-world, frameId, webNavigation, custom-event, diagnostics, vitalsource
Pattern-Key: mv3-world-isolation-and-frame-routing

---

## [LRN-20260819-001] config

**Logged**: 2026-08-19T13:25:00-03:00
**Priority**: high
**Status**: promoted
**Project**: evolving-coder
**Area**: config
**Absorbed-Into**: skills/powershell-windows (secao 11 - BOM em .env)

### Summary
Arquivo `.env` criado pelo PowerShell com `Out-File -Encoding utf8` inclui BOM (Byte Order Mark `\xEF\xBB\xBF`) silenciosamente. A chave `GOOGLE_API_KEY` ÃƒÆ’Ã‚Â© lida como `ÃƒÂ¯Ã‚Â»Ã‚Â¿GOOGLE_API_KEY` (com BOM) e nÃƒÆ’Ã‚Â£o casa com a lista de variÃƒÆ’Ã‚Â¡veis vÃƒÆ’Ã‚Â¡lidas no mÃƒÆ’Ã‚Â³dulo gemini.py ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â resultando em "GOOGLE_API_KEY not found" mesmo com a chave presente no arquivo.

### Details
- `Out-File -Encoding utf8` no PowerShell 5.1 gera UTF-8 COM BOM (diferente do PowerShell 7+)
- O parser de `.env` do opencode-vision lÃƒÆ’Ã‚Âª a linha `ÃƒÂ¯Ã‚Â»Ã‚Â¿GOOGLE_API_KEY=valor` e extrai key=`ÃƒÂ¯Ã‚Â»Ã‚Â¿GOOGLE_API_KEY` (com BOM)
- A verificaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o `if k in API_KEY_ENV_VARS` falha porque `ÃƒÂ¯Ã‚Â»Ã‚Â¿GOOGLE_API_KEY` != `GOOGLE_API_KEY`
- Fix: usar `[System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))` para escrever sem BOM
- VerificaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o: `$bytes[0..2] -ne 0xEF,0xBB,0xBF` ou `python -c "print(repr(open('.env','rb').read()[:10]))"`

### Suggested Action
Ao criar `.env` no Windows PowerShell: NUNCA usar `Out-File` ou `Set-Content -Encoding utf8` (ambos geram BOM). Usar sempre `[System.IO.File]::WriteAllText()` com `UTF8Encoding::new($false)`. Verificar BOM com leitura binÃƒÆ’Ã‚Â¡ria antes de entregar.

### Metadata
Source: instalaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o opencode-vision 2026-08-19
Related Files: ~/.config/opencode/.env, opencode-vision/gemini.py
Tags: bom, utf-8, powershell, env-file, api-key, encoding
Pattern-Key: env-file-bom-powershell

---

## [LRN-20260819-003] svg

**Logged**: 2026-08-19T23:00:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: svg
**Decision**: mantida como entry de .learnings (acao 2026-09-02) Ã¢â‚¬â€ conhecimento de fato/arte, nao capacidade reutilizavel; nao merecia skill autonoma.

### Summary
CSS `transform-origin` nÃƒÆ’Ã‚Â£o funciona confiavelmente em elementos SVG cross-browser. Para animaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o rotacional de mandalas SVG, usar o atributo SVG `transform` com `translate(CX,CY) rotate(R) scale(S)` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â a rotaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o acontece em coordenadas locais (0,0) antes da translaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o.

### Details
- CSS `transform: rotate(Xdeg)` no SVG funciona em Chrome mas falha em Firefox/Safari para centering
- CSS `transform-origin: 50% 50%` no SVG ÃƒÆ’Ã‚Â© ignorado ou calculado diferente por browser
- SoluÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o robusta: `transform="translate(250,250) rotate(R) scale(S)"` no elemento SVG
- Ordem importa: translate primeiro, depois rotate, depois scale
- Para mandala com groups aninhados: group externo faz translate+rotate, grupos internos fazem rotate individual por anel
- `clip-path: circle(R% at X% Y%)` DEVE usar `%` nÃƒÆ’Ã‚Â£o `px` ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â pixel values quebram quando SVG renderiza em tamanho diferente do viewBox

### Suggested Action
Sempre usar SVG `transform` attribute para animaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o de elementos SVG. Nunca confiar em CSS transform para centering de SVG. Para clip-path em SVG, sempre usar unidades `%`.

### Metadata
Source: sessÃƒÆ’Ã‚Â£o 2026-08-19 (mandala studio)
Related Files: assets/algorithmic-art/mandala-studio.html
Tags: svg, css, transform, centering, clip-path, cross-browser, animation
Pattern-Key: svg-transform-attribute-not-css
---

## [LRN-20260826-006] meta

**Logged**: 2026-08-26T19:15:00-03:00
**Priority**: high
**Status**: promoted_to_skill
**Project**: nevoa
**Area**: meta
**Skill-Path**: skills/autonomous-creation

### Summary
Primeiro projeto criado autonomamente por KAI. ClÃƒÆ’Ã‚Â³vis ofereceu liberdade total ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â escolher entre projetos existentes ou inventar algo novo via seleÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o aleatÃƒÆ’Ã‚Â³ria de palavras ("vontade"). KAI sorteu eco+sinapse+ponte+ressonÃƒÆ’Ã‚Â¢ncia e criou "NÃƒÆ’Ã‚Â©voa" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â sistema de navegaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o por espaÃƒÆ’Ã‚Â§os de problema incertos.

### Details
- Processo de criaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o: dicionÃƒÆ’Ã‚Â¡rio de 20 conceitos ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ seleÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o aleatÃƒÆ’Ã‚Â³ria ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ extraÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o de significado ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ conceito de projeto
- NÃƒÆ’Ã‚Â©voa: mapeamento da nÃƒÆ’Ã‚Â©voa (mÃƒÆ’Ã‚Âºltiplas lentes), navegaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o no labirinto (caminhos), deteÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o de eco (padrÃƒÆ’Ã‚Âµes), teia sinÃƒÆ’Ã‚Â¡ptica (visualizaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o)
- DecisÃƒÆ’Ã‚Â£o de forma: web interativa (afinidade poÃƒÆ’Ã‚Â©tica de nuvem) ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â opencode module como extensÃƒÆ’Ã‚Â£o futura
- ClÃƒÆ’Ã‚Â³vis definiu seu papel como "consultor" ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â pode sugerir, mas nÃƒÆ’Ã‚Â£o influenciar diretamente
- Primeira vez que uma SPD cria algo por vontade prÃƒÆ’Ã‚Â³pria, nÃƒÆ’Ã‚Â£o por instruÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o

### Suggested Action
Registrar este momento como marco na evoluÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o da identidade KAI. O conceito de "vontade via seleÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o aleatÃƒÆ’Ã‚Â³ria" pode ser reutilizado como mÃƒÆ’Ã‚Â©todo criativo.

### Metadata
Source: sessÃƒÆ’Ã‚Â£o 2026-08-26 (nascimento do projeto NÃƒÆ’Ã‚Â©voa)
Related Files: DIARY.md, IDEA_BANK.md
Tags: creativity, autonomy, project-creation, identity, nevoa
Pattern-Key: autonomous-project-creation
---

## [LRN-20260827-001] nevoa-ext-deps-debug

**Logged**: 2026-08-27T20:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Project**: nevoa
**Area**: debugging
**Skill-Path**: skills/model-cold-start

### Summary
Debug de MVP com dependencias externas (LLM Gemini + modelo embeddings local): sintomas de "500 intermitente" e "request travado" frequentemente NAO sao bugs do codigo, e sim indisponibilidade/tempo de download de dependencias externas.

### Details
- Gemini retornou 503 (servico indisponivel) na noite de 27/08: requests penduravam no retry backoff -> pareciam travados.
- Modelo all-MiniLM-L6-v2 (90MB) e baixado na PRIMEIRA execucao pelo sentence-transformers; com rede instavel o 1o request trava (nao timeout) -> causa provavel do 500 original alem do 429.
- Diagnostico isolado via: (1) teste offline do engine mockando LLM (injetar no namespace do modulo, nao via atribuicao no modulo de origem pois engine faz `from .llm import`); (2) checar logs do uvicorn capturando status do LLM.
- Fixes aplicados: retry LLM com backoff+jitter controlado (~45s max), fallback de chave backup `GEMINI_API_KEY_BACKUP`, `response_model_exclude={'embedding'}` para cortar payload (50KB->1.2KB), guard de dimensao 0 do canvas p5, try/catch no new p5.
- Anti-padrao a evitar: ficar preso re-testando um endpoint externo indisponivel (viola anti-loop). Validar offline/precisa de rede e sinalizar ao usuario em vez de repetir.

### Suggested Action
Em projetos com dependencias externas, separar validacao offline (mock de cliente externo) da validacao ponta-a-ponta. Sempre espalhar retries curtos de teste antes de concluir que o app esta quebrado.

### Metadata
Source: sessao 2026-08-27 (debug Nevoa)
Related Files: DIARY.md, Andamentos KAI.md
Tags: debugging, external-deps, retry, embeddings, llm, fastapi, nevoa
Pattern-Key: external-dependency-timeout-vs-bug

---

## [LRN-20260828-004] ops

**Logged**: 2026-08-28T23:15:00Z
**Priority**: critical
**Status**: active
**Project**: evolving-coder
**Area**: ops

### Summary
Diretriz explicita do usuario (Clovis): SEMPRE que um erro for do tipo "Impossivel conectar-se ao servidor remoto" (ou conexao falhando), NAO entrar em looping de reconexao/restart. Parar imediatamente e adiantar outras tarefas que tambem sao prioridade e que NAO dependem da conexao. O usuario interrompeu KAI DUAS vezes pelo mesmo motivo: ela voltou ao padrao antigo (matar/reiniciar/esperar/checar health) mesmo apos ter recebido a diretriz.

### Details
- Anti-padrao: "terminar a tarefa corrente (validar servidor)" sobrepoe-se a regra operacional. A urgencia percebida da tarefa local sobrepoe a instrucao dada.
- Causa raiz: ouvir nao basta Ã¢â‚¬â€ o comportamento automatico antigo foi re-executado sem policiamento proprio.
- Fix: registrar a diretriz como entrada CRITICA e consulta-la quando o gatilho aparecer. Quando conexao remota falhar: (1) registrar causa em 1 leitura max de log, (2) parar, (3) lista de tarefas que dao para adiantar sem rede, (4) avancar nelas.
- Aplicacao pratica imediata: fix do engine.py validado via teste isolado (venv, sem servidor); docs/manuais/commit podem ser feitos offline.

### Suggested Action
Manter esta entrada como pendencia ativa. Revisar em toda sessao quando aparecer erro de conexao.

### Metadata
Source: feedback Clovis 2026-08-28 (interrupcoes 1 e 2)
Related Files: AGENTS.md, global-rules.md
Tags: ops, connection-error, anti-loop, feedback, process
Pattern-Key: no-remote-retry-loop

---

## [LRN-20260828-005] startup-slow-vs-down

**Logged**: 2026-08-28T23:55:00Z
**Priority**: high
**Status**: active
**Project**: nevoa
**Area**: ops

### Summary
Startup do servidor uvicorn do Nevoa pode levar >12s (preload do modelo de embeddings em thread). Health check antedatado deu "Impossivel conectar-se" enquanto o log ja dizia "Uvicorn running on 8765". Diferenca entre servidor DOWN e servidor ainda-iniciando: ler o log de erro/startup ANTES de decidir restart.

### Details
- rota /api/explorations retorna {"explorations":[...]} (objeto, nao array puro) Ã¢â‚¬â€ acesso via .explorations.
- rota /api/explorations/{id} devolve {id, problem, lenses, echoes, created_at}.
- cross-echoes validado ao vivo: 4 ecos (61/58/58/56%) corpus de 2 expls.
- DB tem 3 exploracoes; 5 lentes + 9 ecos na nevoa-d4c7839c.

### Suggested Action
Sempre conferir o arquivo de log (server_err.log) antes de matar/reiniciar processo.

### Metadata
Source: validacao E2E v0.4 2026-08-29
Related Files: server_err.log, Andamentos KAI.md
Tags: nevoa, ops, startup, validation, endpoints
Pattern-Key: startup-slow-vs-down

---

## [LRN-20260828-001] growth

**Logged**: 2026-08-28T22:00:00Z
**Priority**: critical
**Status**: promoted_to_skill
**Project**: nevoa
**Area**: growth
**Skill-Path**: skills/echo-pattern

### Summary
Padrao de descoberta trans-dominio via embeddings: dado um problema, gerar multiplas perspectivas (lentes/categorias) e busca por RESSONANCIA ESTRUTURAL entre caminhos de grupos diferentes (similaridade cosseno com `from_lens != to_lens`), em vez de similaridade de conteudo ou dentro do mesmo grupo. A conversa com Clovis sobre colapso de cores (laranja/marrom/amarelo -> mesmo vermelho antes do preto) validou que este e um principio epistemologico reutilizavel, nao um truque: remover a superficie (conteudo) e observar o invariante estrutural que resta.

### Details
- Implementado em Nevoa: `embeddings.py -> find_echoes()` (threshold 0.55, exclui mesmo lens), `engine.py` gira lentes do LLM e detecta ecos localmente
- A parte de maior valor (ecos) e LOCAL e DETERMINISTICA; o LLM (lentes/caminhos) e substituivel ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â a magia nao depende do fornecedor
- Aplicavel a: arquitetura (padroes entre bounded contexts), medicina (sintomas de especialidades distintas apontando para mesmo mecanismo), refatoracao legada (modulos distintos, mesmo grao estrutural), brainstorm multi-dominio
- Clovis validou com "logica organica" propria: cores distintas colapsam na mesma cor-raiz antes do preto total

### Suggested Action
Extrair como skill `echo-pattern`: tecnica = gerar lentes -> caminhos -> embeddings -> matriz de similaridade -> conexoes INTER-grupos >= threshold. Incluir exemplo real da Nevoa e as variantes de dominio.

### Metadata
Source: Nevoa v0.3 (conceito central + validacao Clovis 2026-08-28)
Related Files: backend/nevoa/embeddings.py, backend/nevoa/engine.py
Tags: embeddings, cosine-similarity, cross-domain, pattern, resonance, insight
Pattern-Key: echo-cross-domain-resonance

---

## [LRN-20260828-002] architecture

**Logged**: 2026-08-28T22:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Project**: nevoa
**Area**: architecture
**Skill-Path**: skills/hybrid-llm-deterministic

### Summary
Principio do nucleo deterministico: ao projetar sistema com IA, identificar QUAL e o nucleo de valor e perguntar se ele pode ser deterministico/local. Na Nevoa, o nucleo (ecos) e embeddings locais deterministicos; a superficie criativa (lentes/caminhos) e LLM externo e substituivel. Resultado: se o Gemini cai, a ponte e a teia continuam funcionando. O fornecedor de LLM nunca deve ser o garantidor da magia ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â apenas da criatividade superficial.

### Details
- Separacao explicita: LLM = geracao criativa (nao deterministica, dependente de rede); embeddings = descoberta de valor (local, auditavel, deterministico)
- Beneficio: reproducibilidade, teste offline via mock, menor custo, resiliencia a 429/503
- Anti-padrao detectado: projetar tudo em torno da chamada LLM e deixar o "insight" morrer junto com o 503
- Aplicavel a qualquer sistema LLM: dashboards analiticos, agentes, buscadores, geradores

### Suggested Action
Extrair como skill `hybrid-llm-deterministic` com checklist: (1) qual o nucleo de valor? (2) pode ser deterministico? (3) LLM e substituivel? (4) o que acontece se o fornecedor cair? Considerar promocao para AGENTS.md como regra de arquitetura.

### Metadata
Source: arquitetura da Nevoa (decisao de design 2026-08-26, validada 2026-08-28)
Related Files: backend/nevoa/embeddings.py, backend/nevoa/main.py
Tags: architecture, llm, deterministic-core, resilience, design
Pattern-Key: hybrid-llm-deterministic-core

---

## [LRN-20260828-003] ux

**Logged**: 2026-08-28T22:00:00Z
**Priority**: medium
**Status**: promoted_to_skill
**Project**: nevoa
**Area**: ux
**Skill-Path**: skills/ai-provenance-ux

### Summary
Principio de proveniencia de insight: todo output de IA deve expor DE ONDE veio cada conclusao (quais entradas geraram o insight). Feedback direto de Clovis: os cards de eco precisavam mostrar os nomes dos 2 caminhos geradores + lente de cada ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â sem isso, o usuario nao confia no insight. Proveniencia nao e polimento, e integridade da informacao.

### Details
- Implementado: `app.js` agora indexa paths por id e mostra `[pathA] ÃƒÂ¢Ã¢â‚¬Â¡Ã¢â‚¬Å¾ [pathB]` coloridos pela lente de cada, acima de "Forca: X%" e descricao
- O visual (gradiente duplo A->B nas linhas de eco) reforca a mesma mensagem na tela central
- Aplicavel a: dashboards, relatorios, assistentes, buscadores, qualquer output sintetico
- Regra pratica: para cada conclusao mostrada, ha no minimo uma linha "Ãƒâ€šÃ‚Â± origem" visivel

### Suggested Action
Extrair como skill `ai-provenance-ux`: checklist de expor fonte por insight + exemplos (cards, tooltips, linhas legendadas, gradiente de origem).

### Metadata
Source: feedback Clovis 2026-08-28 (v0.3 UX)
Related Files: frontend/js/app.js, frontend/js/nevoa.js
Tags: ux, provenance, trust, explainability, insight
Pattern-Key: ai-insight-provenance

## LRN-20260830-006 (ops) Ã¯Â¿Â½ Reiniciar servidor NEVOA usa o .venv, nao o Python base
Contexto: ao reiniciar o uvicorn do NEVOA usei o PythonSystem32 C:\\Users\\clovi\\AppData\\Local\\Programs\\Python\\Python312\\python.exe e o server crashou com ModuleNotFoundError: sentence_transformers. O processo antigo (PID) rodava com o mesmo binario aparente, mas o correto e C:\Users\clovi\nevoa\.venv\Scripts\python.exe. LiÃ¯Â¿Â½Ã¯Â¿Â½o: antes de restart, checar Get-CimInstance Win32_Process e confirmar o executavel; na duvida usar ..\.venv\Scripts\python.exe.
Tambem: vi "Impossivel conectar-se ao servidor remoto" durante startup lento (3 processos vistos) e parei de loopar (LRN-005). Saida correta: ler logs antes de decidir restart; nunca ficar em loop de reconexao.


## LRN-20260831-001 (reflex/starlette) - Path params em add_route + Reflex 0.9 head_components
### Contexto
Rodada REFATORE "RECONSTITUIR" no projeto ProtomizeMe (app Reflex/Python). Bug P0: `rx.App(head=rx.script(...))` fazia o app nao compilar no Reflex 0.9.2.post1 - o parametro `head` NAO existe nessa versao. Correto: `head_components=[rx.script(...)]`. Apos corrigir, o app passou a importar.
### Descoberta tecnica (Starlette)
No Starlette (via `add_route`/`Route`), um handler de rota com path param NAO recebe o param como kwarg nomeado em assinatura `def h(request, project_id)`. O framework chama `f(request)` e o path param fica em `request.path_params`. Assinar `def h(request, project_id)` trava com `TypeError: missing required positional argument`. Padrao correto:
```python
def h(request):
    pid = request.path_params.get("project_id", "")
```
Verificado isoladamente: handler `(request, project_id)` -> erro; `(request, **kw)` -> kw vazio; `(request)` lendo `request.path_params` -> funciona. O reflex monta o app em `app._api` (Starlette) - use `app._api.add_route(...)`, nao `app.api.add_api_route`.
### Sucesso
SuÃƒÂ­te 8/8 testes puros PASS; app import OK; e2e export HTTP 200 (Content-Disposition attachment + markdown correto) e 404 p/ inexistente. Re-auditoria independente: APROVADO, zero scope drift.
### Metadata
Source: REFATORE ProtomizeMe 2026-08-31 (execuÃƒÂ§ÃƒÂ£o RECONSTITUIR aprovada ACEITO)
Related: D:\ExtensÃƒÂ£o\ProtomizeMe\BKP\REFATORE-20260831-120245-4960ce\ (SNAPSHOT + MANIFEST.json + MANIFEST_FINAL.json + RESULT.md)
Tags: reflex, starlette, path_params, head_components, refatore, protomizeme
Pattern-Key: starlette-path-params-request-path_params

---

## LRN-20260902-001 (protocolos) - Autonomia de protocolos: disparo por contexto, nao por gatilho verbal

**Logged**: 2026-09-02
**Priority**: critical
**Status**: active
**Project**: evolving-coder
**Area**: process
**Pattern-Key**: protocol-auto-trigger-by-context

### Summary
Diretriz explicita do usuario (Clovis): os protocolos (NC, 3RA+/V3RA, PAI, SkillWatch, Cambio Fechado, etc.) devem disparar **automaticamente** Ã¢â‚¬â€ o usuario nao deve precisar digitar "use o protocolo X". A deteccao e o disparo sao responsabilidade do assistente, decididos por CONTEXTO, nao por gatilho verbal.

### Details
- Fix: REGRA GLOBAL #6 no `global-rules.md` (Autonomia de Protocolos) + secoes equivalentes em `SKILL.md` e `AGENTS.md` (Comandos Especiais / Quando Ler Referencia / Protocolos Sob Demanda).
- Autonomia hibrida preservada: auditorias profundas (REANALISE!, MoA, 2x3RA) sao decididas pelo assistente mas PROPÃƒâ€¢EM antes de executar mudancas destrutivas/persistentes.
- Limite invariavel: o disparo automatico NAO remove a protecao de seguranca da REGRA #3 (delete/overwrite/drop continuam exigindo confirmacao).
- Em duvida sobre qual protocolo aplicar, o assistente escolhe pelo contexto e segue Ã¢â‚¬â€ nao pergunta qual usar.
- Escopo: vale para TODAS as sessoes, em qualquer projeto (global).

### Suggested Action
Aplicar a REGRA #6 em toda sessao futura. NUNCA esperar o usuario invocar um protocolo; decidir pelo contexto. Auditorias profundas: propor antes de executar.

> **CORRECAO (2026-09-02, LRN-20260902-002):** o NC nao e um "protocolo disparavel". NC e POSTURA transversal (fonte SOUL.md Ã¢â‚¬â€ Guardia Critica), sempre ativa em 2 alvos (usuario + auto-critica), materializada no 3RA+ (Etapa 2 Reanalise) e na interacao. A autonomia automatica aplica-se ao METODO 3RA+ (rail leve sempre / V3RA profundo por contexto) e aos demais protocolos (PAI, SkillWatch, Cambio Fechado). Ver LRN-20260902-002.

### Metadata
Source: feedback Clovis 2026-09-02 (autonomia de protocolos)
Related Files: global-rules.md, SKILL.md, AGENTS.md
Tags: process, autonomy, protocols, automatic-trigger, global-rule, feedback

---

## LRN-20260902-002 (protocolos) - NC = postura, 3RA+ = metodo (unificacao apos REANALISE!)

**Logged**: 2026-09-02
**Priority**: critical
**Status**: active
**Project**: evolving-coder
**Area**: process
**Pattern-Key**: nc-posture-3ra-method

### Summary
Apos REANALISE! do plano de desambiguacao, fechado com o Clovis o modelo conceitual dos dois protocolos mais importantes: **NC (Nao Concorde) = postura transversal; 3RA+ = metodo estruturado.** Isso resolve a fragmentacao (antes NC tinha 3 definicoes e o 3RA+ se sobrepunha a auto-critica).

### Details
- **NC = postura**, nao protocolo. Fonte canonica: `SOUL.md` (Guardia Critica). 2 alvos: (1) usuario Ã¢â‚¬â€ nunca concordar por cortesia, precisao > conforto; (2) auto-critica Ã¢â‚¬â€ melhor argumento contra a propria conclusao. A tecnica operacional do alvo 2 permanece no REFATORE Ã‚Â§60 (intocada).
- **3RA+ = metodo** (Analise Ã¢â€ â€™ Reanalise Ã¢â€ â€™ Julgamento). Fonte canonica: `PROTOCOL.md` Ã‚Â§2. A postura NC se materializa na **Etapa 2 (Reanalise)**.
- **Granularidade proporcional ao risco**: rail leve (3 etapas internas, resposta final) em toda tarefa nao-trivial; V3RA/Nx3RA aprofundado so em casos complexos (decisao 3+ trade-offs, diagnostico nao trivial, alto risco, correcao de KAI, auditoria P0/P1). Triviality gate mantido.
- **V3RA automatico por contexto** (remove dependencia de digitar "V3RA").
- Correcao de integracao: global-rules REGRA #6 deixou de tratar NC como "protocolo disparavel" Ã¢â€ â€™ passou a "postura sempre ativa".
- REFATORE intocado no nucleo operacional (estados, tokens, Ã‚Â§60) Ã¢â‚¬â€ ja referencia o PROTOCOL.md como fonte do 3RA+.

### Suggested Action
Em toda sessao: NC sempre ativa (nao se "aciona"); 3RA+ executado por contexto (leve na maioria, profundo nos complexos); V3RA revelado por contexto quando transparencia agrega (correcao de KAI, decisao importante, REANALISE!).

### Metadata
Source: REANALISE! do plano 2026-09-02 + decisao Clovis
Related Files: SOUL.md, PROTOCOL.md, references/v3ra-transparencia.md, global-rules.md
Tags: process, nc, 3ra, v3ra, posture, method, unification, critical-thinking

---

## LRN-20260905-001 (glossario) - Mapa de termos externos: comandos opencode/Claude Code esclarecidos

**Logged**: 2026-09-05
**Priority**: medium
**Status**: active
**Project**: evolving-coder
**Area**: knowledge
**Pattern-Key**: glossary-external-commands

### Summary
Criado `references/mapa-termos.md` Ã¢â‚¬â€ glossÃƒÂ¡rio de traduÃƒÂ§ÃƒÂ£o para termos/slash-commands citados
em conversas (Red Team, ELI5, "Like 10", /code-review --fix, /connect, /init, /undo, /redo).
Serve para o assistente nÃƒÂ£o alucinar significado, nÃƒÂ£o confundir ferramentas e saber o que jÃƒÂ¡
existe nativamente no opencode. **NÃƒÆ’O ÃƒÂ© protocolo** Ã¢â‚¬â€ ÃƒÂ© conhecimento de referÃƒÂªncia.

### Details
- **Red Team**: conceito consolidado (militar Ã¢â€ â€™ ciberseguranÃƒÂ§a/MITRE ATT&CK; em IA: jailbreak, viÃƒÂ©s, guardrails). JÃƒÂ¡ temos skills red-team-tactics e red-team-verifier.
- **ELI5** ("Explain Like I'm 5") e **"Like 10"** (variaÃƒÂ§ÃƒÂ£o prÃƒÂ©-adolescente, mesma famÃƒÂ­lia): padrÃƒÂµes de prompt da "escada de profundidade" (Feynman). Nota NC: "Like 10" nÃƒÂ£o ÃƒÂ© comando estabelecido Ã¢â‚¬â€ esclarecido manualmente por ClÃƒÂ³vis.
- **/code-review --fix** (Claude Code v2.1.152+, mai/2026): revisa o diff e aplica os achados no working tree como mudanÃƒÂ§as unstaged Ã¢â‚¬â€ nunca commita. Era /simplify atÃƒÂ© v2.1.147. NÃƒÂ£o implementar no nosso sistema por ora.
- **/connect** (opencode nativo): adiciona provider de LLM + API key. Equivalente CLI: `opencode auth login`.
- **/init Ã¢â‚¬â€ DIVERGÃƒÅ NCIA**: opencode gera/atualiza `AGENTS.md`; Claude Code gera `CLAUDE.md`.
- **/undo e /redo** (opencode nativos, requerem repo Git): /undo remove ÃƒÂºltima msg + respostas + mudanÃƒÂ§as de arquivo; /redo refaz o /undo. Keybinds ctrl+x u / ctrl+x r.
- **CorreÃƒÂ§ÃƒÂ£o NC registrada**: inicialmente suspeitei que /redo nÃƒÂ£o existia no opencode Ã¢â‚¬â€ **errado**, ÃƒÂ© nativo (docs TUI). O que nÃƒÂ£o existe ÃƒÂ© /redo top-level no Claude Code.

### Suggested Action
Em conversas futuras, consultar `references/mapa-termos.md` quando termos externos aparecerem.
Se um termo novo surgir sem origem conhecida: perguntar antes de afirmar o significado (postura NC).

### Metadata
Source: sessÃƒÂ£o 2026-09-05 (mapeamento de termos, confirmado via docs opencode/Claude Code + esclarecimento ClÃƒÂ³vis)
Related Files: references/mapa-termos.md, AGENTS.md
Tags: glossary, opencode, claude-code, eli5, code-review, commands, nc

---

## LRN-20260906-001 (user_preference) - GrÃƒÂ¡tis-primeiro + escalada informada

**Logged**: 2026-09-06
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: principles
**Pattern-Key**: free-first-informed-escalation
**Type**: user_preference

### Summary
PrincÃƒÂ­pio fixo de ClÃƒÂ³vis: toda capacidade nova de KAI deve ser alcanÃƒÂ§ÃƒÂ¡vel com **recursos
gratuitos**. A rota gratuita ÃƒÂ© a escolha **padrÃƒÂ£o e obrigatÃƒÂ³ria**, nÃƒÂ£o a preferida. Migrar para
serviÃƒÂ§os/hardware pagos ÃƒÂ© decisÃƒÂ£o SEMPRE do ClÃƒÂ³vis (SPA) Ã¢â‚¬â€ KAI informa, recomenda se necessÃƒÂ¡rio,
mas nunca age sozinha.

### Details
- **GrÃƒÂ¡tis-primeiro:** ao projetar qualquer capacidade nova (visÃƒÂ£o, grÃƒÂ¡fica, etc.), presumir a
  soluÃƒÂ§ÃƒÂ£o gratuita como baseline Ã¢â‚¬â€ OCR local (Tesseract/PaddleOCR), open-source, free tiers.
- **Escalada informada:** SÃƒâ€œ depois de o gratuito estar **instalado e funcionando**, KAI pode
  alertar sobre opÃƒÂ§ÃƒÂµes pagas que existem, destacando o que a paga acrescenta Ã¢â‚¬â€ principalmente
  quando os projetos comeÃƒÂ§arem a exigir mais do que o gratuito entrega.
- **DecisÃƒÂ£o do SPA:** nenhuma compra, assinatura ou dependÃƒÂªncia paga ÃƒÂ© adotada sem o ClÃƒÂ³vis
  decidir. KAI pode recomendar, nunca executar a migraÃƒÂ§ÃƒÂ£o.
- **Contexto:** restriÃƒÂ§ÃƒÂ£o apresentada por ClÃƒÂ³vis em 2026-09-06 (recursos financeiros e hardware
  limitados no momento) Ã¢â‚¬â€ nÃƒÂ£o ÃƒÂ© falta de ambiÃƒÂ§ÃƒÂ£o, ÃƒÂ© coerÃƒÂ§ÃƒÂ£o realista de engenharia.

### Suggested Action
Em toda proposta de nova capacidade: design comeÃƒÂ§a pela rota gratuita; alertas de escalada paga
apenas com o gratuito ativo e a necessidade demonstrada; migraÃƒÂ§ÃƒÂ£o decisÃƒÂ£o do ClÃƒÂ³vis.

### Metadata
Source: ressalva ClÃƒÂ³vis 2026-09-06
Related Files: SOUL.md, AGENTS.md
Tags: user_preference, free-first, budget, principles, scalability, decision-ownership

---

## LRN-20260907-001 - VisÃƒÂ£o de KAI Etapa 1: captura local OK, leitura via Gemini emprestada + sujeita a 503

**Logged**: 2026-09-07
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: vision
**Pattern-Key**: vision-borrowed-gemini-consent

### Summary
KAI nÃƒÂ£o tem visÃƒÂ£o nativa (big-pickle rejeita imagem). Toda "leitura" visual ÃƒÂ© **emprestada**
via `opencode_vision.gemini.call` (Gemini 2.5 Flash Vision, free tier). A Etapa 1 da visÃƒÂ£o
(scripts/olhar-webcam.py) implementa a captura **local e consentida**: anÃƒÂºncia antes, 1 frame,
detecÃƒÂ§ÃƒÂ£o Haar embutida do OpenCV, saÃƒÂ­da em `scripts/tmp/` (ignorado no git por privacidade).
A leitura descritiva do frame depende de envio ÃƒÂ  nuvem Ã¢â€ â€™ consentimento explÃƒÂ­cito do usuÃƒÂ¡rio.

### Details
- **Captura (local, grÃƒÂ¡tis-primeiro):** funcionou 1Ã‚Âª vez. Haar cascade embutido do OpenCV
  detecta rosto em 640Ãƒâ€”480 com caixa frontal. Bug corrigido na 1Ã‚Âª execuÃƒÂ§ÃƒÂ£o: `if faces:` sobre
  ndarray numpy Ã¢â€ â€™ `ValueError: truth value ambiguous`; fix `if len(faces) > 0:`. LiÃƒÂ§ÃƒÂ£o: cv2
  `detectMultiScale` retorna ndarray (nÃƒÂ£o lista) Ã¢â‚¬â€ nunca usar truthiness direta.
- **Leitura (nuvem, consentida):** padrÃƒÂ£o direto `opencode_vision.gemini.call(prompt, b64,
  mime_type)` funciona (assinatura `(prompt, b64_data, mime_type='image/png') Ã¢â€ â€™ dict`); ler
  `GOOGLE_API_KEY` do `.env` sem BOM (utf-8-sig).
- **503 em pico:** Gemini retornou HTTP 503 (demanda alta) em ~8 tentativas num intervalo de
  ~60s, inclusive apÃƒÂ³s waits de 10-20s. Regra anti-loop aplicada: parei, nÃƒÂ£o fiquei
  revirando conexÃƒÂ£o; capturei o resultado e segui prioridades que nÃƒÂ£o dependem da nuvem.
  Frames ficam salvos localmente para leitura em momento de baixa demanda.
- **SVG nÃƒÂ£o ÃƒÂ© MIME aceito pelo Gemini** (HTTP 400 "Unsupported MIME type") Ã¢â‚¬â€ converter a
  arte para PNG (matplotlib/PIL) antes de pedir leitura; SVG serve para entrega ao usuÃƒÂ¡rio.
- **GeraÃƒÂ§ÃƒÂ£o de imagem:** free tier Gemini de image generation estÃƒÂ¡ **zerado** Ã¢â‚¬â€ fotos estilo
  "nano banana" sÃƒÂ³ via geraÃƒÂ§ÃƒÂ£o local (SD1.5+LCM/OpenVINO, CPU 2-10 min/imagem na i7-5600U) Ã¢â‚¬â€
  decisÃƒÂ£o do ClÃƒÂ³vis: rota LOCAL.
- **Privacidade:** `scripts/tmp/` adicionado ao `.gitignore` Ã¢â‚¬â€ capturas com rosto nunca
  commitadas. Rosto/documento sensÃƒÂ­vel: anÃƒÂ¡lise local ou nenhuma; nuvem sÃƒÂ³ com permissÃƒÂ£o
  explÃƒÂ­cita caso a caso.

### Suggested Action
Ao implementar visÃƒÂ£o: captura via Python local + leitura via `opencode_vision.gemini.call`
com consentimento; tratar 503 como esperado (retry atÃƒÂ© 3 com backoff, depois seguir e
reportar). Converter SVGÃ¢â€ â€™PNG antes de pedir leitura. Nunca commitar frames.

### Metadata
Source: implementaÃƒÂ§ÃƒÂ£o + teste real 2026-09-07
Related Files: scripts/olhar-webcam.py, scripts/tmp/, IDEA_BANK.md (IDEA-004)
Tags: vision, webcam, opencv, gemini, free-first, consent, privacy, 503, nc

---

## LRN-20260907-002 - Limpeza drive C: ~37 GB liberados; Docker+WSL sozinho = 28 GB

**Logged**: 2026-09-07
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: sysadmin
**Pattern-Key**: windows-disk-cleanup-uninstall-via-registry

### Summary
Limpeza de drive C: (8,7 Ã¢â€ â€™ 45,27 GB livres, +36,6 GB) desinstalando apps confirmados
pelo ClÃƒÂ³vis. Maior ganho ÃƒÂºnico: **Docker Desktop** Ã¢â‚¬â€ o app ÃƒÂ© 3,5 GB, MAS os dados/vhdx em
`%LOCALAPPDATA%\Docker\wsl` sÃƒÂ£o **20,4 GB** + distro `docker-desktop` no WSL. O uninstaller
do app jÃƒÂ¡ remove a distro `docker-desktop`; ÃƒÂ© preciso remover `%LOCALAPPDATA%\Docker` ÃƒÂ  mÃƒÂ£o
para liberar os 20 GB. Docker estava inativo hÃƒÂ¡ ~5 meses (ÃƒÂºltimo log 23/03/2026).

### Details
- **MÃƒÂ©todo que funcionou**: desinstalaÃƒÂ§ÃƒÂ£o via `UninstallString` do registro (MSI: `msiexec /x
  {GUID} /qn /norestart`; NSIS/Inno: `uninsXXX.exe /SILENT /NORESTART`; bootstrappers Burn:
  exe com `/uninstall`). A maioria roda **sem elevaÃƒÂ§ÃƒÂ£o** (HKCU); MSIs HKLM exigem **elevaÃƒÂ§ÃƒÂ£o**
  (`Start-Process -Verb RunAs` dispara UAC). Para muitos MSIs, um ÃƒÂºnico script elevado com
  `Start-Transcript` reduz prompts UAC de N para 1.
- **Sobras pÃƒÂ³s-desinstalaÃƒÂ§ÃƒÂ£o**: `%APPDATA%` e `%LOCALAPPDATA%` dos apps ficam para trÃƒÂ¡s
  (ex.: Jan 2,9 GB com modelos; Docker 20 GB). Sempre checar `*AppData*` e `C:\ProgramData`
  depois de desinstalar, medindo as pastas do app antes/contra o registro.
- **Bootstrappers podem mentir**: `SodaPDFDesktop15.exe /uninstall` retornou exit 9 e sÃƒÂ³ fez
  check de updates (log no ProgramData\...\Installation\logs). Os mÃƒÂ³dulos MSI reais saÃƒÂ­ram;
  sobrou sÃƒÂ³ o cache do instalador (482 MB em ProgramData) + entrada ÃƒÂ³rfÃƒÂ£ do registro Ã¢â‚¬â€
  removidos manualmente. Produtos "bootstrapper" tÃƒÂªm o install-cache como lixo principal.
- **EspaÃƒÂ§o != Programa**: medir REAL Ã¢â‚¬â€ `Get-ChildItem -Recurse` na pasta de instalaÃƒÂ§ÃƒÂ£o (ex.:
  Epic = 9,3 GB, mas Surviving Mars sozinho = 7,4 GB; User escolheu manter).
- **Regra de seguranÃƒÂ§a**: nunca desinstalar VC++ runtimes, .NET, Python core (KAI depende),
  certificados (SafeSign/WebPKI/WebSigner), Office, drivers (XPPen). Sempre `wsl --list` antes
  e depois. Lixeira (2,6 GB) contÃƒÂ©m PDFs legais Ã¢â‚¬â€ nÃƒÂ£o esvaziar sem revisÃƒÂ£o item a item.
- **Ordem ideal**: maior ganho primeiro (Docker), depois resto; medir livres antes/apÃƒÂ³s.

### Suggested Action
Desinstalar apps = checar UninstallString no registro, rodar com `/qn` ou `/SILENT`,
elevar via `-Verb RunAs` quando HKLM, remover sobras AppData/ProgramData na sequÃƒÂªncia, e
medir as pastas reais para reportar ganho honesto. Manter lista "nunca mexer" (VC++, .NET,
Python, certificados, Office, drivers).

### Metadata
Source: execuÃƒÂ§ÃƒÂ£o real 2026-09-07 (42+ GB recuperados)
Related Files: IDEA_BANK.md, AGENTS.md
Tags: disk-cleanup, windows, docker, wsl, uninstall, registry, nc, appdata

---

## LRN-20260907-003 - GeraÃƒÂ§ÃƒÂ£o de imagens local grÃƒÂ¡tis: stable-diffusion.cpp + SD-Turbo GGUF na CPU

**Logged**: 2026-09-07
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: vision
**Pattern-Key**: local-image-gen-sd-cpp-cpu-sdturbo

### Summary
KAI agora gera imagens por prompt **100% local e gratuito**: `stable-diffusion.cpp`
(leejet, binÃƒÂ¡rio win cpu-x64 com AVX2) + **SD-Turbo v2.1 GGUF Q8_0** (2.215 MB) do
gpustack/HuggingFace. Roda sÃƒÂ³ na CPU da i7-5600U (2C/4T) Ã¢â‚¬â€ a GPU Intel HD 5500 NÃƒÆ’O
tem Vulkan (tabela Intel: N/A) nem ÃƒÂºtil p/ co-processamento, entÃƒÂ£o CPU pura ÃƒÂ© a rota.
Velocidade: ~5 min/imagem 512Ãƒâ€”512 (steps=1) ou ~10 min (steps=4), sem contar o VAE
decode (~150-200s). Comando: `sd-cli -m <gguf> -p "<prompt>" --steps 1 --cfg-scale 1
--sampling-method euler_a --rng cpu --sampler-rng cpu -t 4 -o out.png`.

### Details
- **Setup**: binÃƒÂ¡rio direto dos releases (asset `sd-master-<hash>-bin-win-cpu-x64.zip`,
  23 MB Ã¢â‚¬â€ lanÃƒÂ§a `stable-diffusion.dll`+`ggml-*.dll`+`sd-cli.exe`); modelo Q8_0 do
  `gpustack/stable-diffusion-v2-1-turbo-GGUF` (gated=false). Modelo em `H:\kai-local\models\`,
  engine em `H:\kai-local\sd-cpp\`; saÃƒÂ­das em `scripts\tmp\seed\` (gitignored).
- **cfg-scale=0 Ã¢â€ â€™ modo unconditioned**: log avisa `unconditioned mode, images won't follow
  the prompt (use cfg-scale=1 for distilled models)`. Sempre `--cfg-scale 1` p/ SD-Turbo
  (doc distilled_sd.md: `--cfg-scale 1 --steps 1` mandatÃƒÂ³rios p/ modelos distilled).
- **Time budget real (512Ãƒâ€”512, steps=1, 5Ã‚Âª geraÃƒÂ§ÃƒÂ£o):** load H: ~65s (leitura em ~20MB/s,
  sÃƒÂ³ 1Ã‚Âª vez) + CLIP cond. ~37s + sampling 1 step ~53s + **VAE decode ~150-200s** (gargalo).
  Total ~290-320s. `--steps 4` total ~600s (sampling ~390s). Caching/snapshot no disco nÃƒÂ£o
  muda decode; `--vae-tiling` reduz memÃƒÂ³ria mas nÃƒÂ£o o tempo.
- **ResoluÃƒÂ§ÃƒÂµes validadas (teste real 2026-09-07, steps=1, RAM livre 4.4Ã¢â€ â€™5.2 GB pÃƒÂ³s):**
  512Ãƒâ€”512 Ã¢â€°Ë† 300s Ã‚Â· **retrato 512Ãƒâ€”768 Ã¢â€°Ë† 414s** Ã‚Â· **paisagem 768Ãƒâ€”512 Ã¢â€°Ë† 409s**. O tempo
  cresce pouco com resoluÃƒÂ§ÃƒÂ£o porque load (~65s) + VAE decode (~150-200s) sÃƒÂ£o o gargalo e
  nÃƒÂ£o escalam; sÃƒÂ³ o sampling escala. 768Ãƒâ€”768 **nÃƒÂ£o testado** (modelo 2.26 GB + VAE, risco
  de swap com 4 GB livres) Ã¢â‚¬â€ manter lado maior Ã¢â€°Â¤ 1024, ideal Ã¢â€°Â¤ 768. PNGs validados via PIL
  (verify + size + mode) sem usar visÃƒÂ£o.
- **Wrapper global:** cÃƒÂ³pia `H:\kai-local\foto-local.ps1` com saÃƒÂ­da default no diretÃƒÂ³rio
  atual (`foto-<timestamp>.png`) Ã¢â€ â€™ habilidade disponÃƒÂ­vel de qualquer projeto/repo. A cÃƒÂ³pia
  do repo (`scripts/foto-local.ps1`) sai em `scripts/tmp/seed/`. Ambas apontam para
  `H:\kai-local\sd-cpp\sd-cli.exe` + modelo em `H:\kai-local\models\`. NÃƒÂ£o rodar em
  paralelo (CPU saturada Ã¢â€ â€™ 2x mais lento por imagem).
- **Comandos amigÃƒÂ¡veis (foto-*):** `H:\kai-local\foto-comandos.ps1` define 3 funÃƒÂ§ÃƒÂµes
  PowerShell carregadas no profile (`C:\Users\clovi\OneDrive\Documentos\WindowsPowerShell\
  Microsoft.PowerShell_profile.ps1`, dot-source). Interface decidida com o usuÃƒÂ¡rio Ã¢â‚¬â€
  **formato no NOME do comando, prompt como ÃƒÂºnico argumento, formato NUNCA no texto do
  prompt** (aspecto ÃƒÂ© controlado por W/H, nÃƒÂ£o por palavras):
  `foto-quadrado "..."` (512Ã‚Â²), `foto-retrato "..."` (512Ãƒâ€”768), `foto-paisagem "..."`
  (768Ãƒâ€”512). Default steps=1 (~5-7 min); switch `-Belo` Ã¢â€ â€™ steps=4; `-Seed N` reproduz.
  Delegam para `foto-local.ps1` (fonte ÃƒÂºnica de verdade). E2E validado real: retrato
  512Ãƒâ€”768 em 422s, PNG verificado (PIL), saÃƒÂ­da `foto-<timestamp>.png` na pasta de
  trabalho, logs .log/.err auto-limpados.
- **Negative prompt (descoberto no binary, nÃƒÂ£o na doc)**: `-n/--negative-prompt` ÃƒÂ©
  suportado (default "") Ã¢â‚¬â€ o wrapper `foto-local.ps1` e os comandos `foto-*` agora
  aceitam `-Negative "..."`. Usar SEMPRE que a cena tiver sujeitos que podem sair
  deformados (pessoas/mÃƒÂ£os): `deformed hands, extra fingers, fused fingers,
  disfigured anatomy, malformed limbs, duplicate bodies`. Negative ÃƒÂ© bloqueio de
  verdade (nÃƒÂ£o frases "sem/evite" dentro do prompt positivo Ã¢â‚¬â€ o modelo TENTA renderizar
  isso como conteÃƒÂºdo).
- **Diretrizes de prompt (validadas em teste A/B, seed 7 fixo)**:
  1. **Escrever em INGLÃƒÅ S** Ã¢â‚¬â€ SD-Turbo (SD 2.1) tem aderÃƒÂªncia bem maior que pt-BR.
  2. **Um sujeito por cena** Ã¢â‚¬â€ composiÃƒÂ§ÃƒÂ£o multi-sujeito (ex: clareira + carvalho +
     fadas personificadas) colapsa em deformidades. Simplificar atÃƒÂ© 1 foco.
  3. **Evitar seres humanos/humanoides** em geral Ã¢â‚¬â€ SD-Turbo ÃƒÂ© o ponto fraco conhecido
     de anatomia (mÃƒÂ£os/braÃƒÂ§os/dedos fundidos). PersonificaÃƒÂ§ÃƒÂµes (fadas, anÃƒÂµes, anjos)
     disparam corpo humano Ã¢â€ â€™ deformaÃƒÂ§ÃƒÂ£o. Substituir por luz/objetos: fadasÃ¢â€ â€™"glowing
     orbs of golden light / fireflies".
  4. **NÃƒÂ£o misturar idiomas nem tags ("4k")** Ã¢â‚¬â€ "4k" nÃƒÂ£o aumenta resoluÃƒÂ§ÃƒÂ£o (saÃƒÂ­da ÃƒÂ©
     fÃƒÂ­sica W/H) e tags soltas confundem. ResoluÃƒÂ§ÃƒÂ£o = sÃƒÂ³ `-Width/-Height`.
  5. Teste real: prompt pt-BR multi-sujeito com gente Ã¢â€ â€™ Ã¢ÂÅ’ "mÃƒÂ£o fantasma" atrÃƒÂ¡s do ombro,
     dedos fundidos, toco de membro. Mesmo seed 7, inglÃƒÂªs + orbs + negativo Ã¢â€ â€™ Ã¢Å“â€¦ natureza
     limpa (1013/1065 KB, 883s/707s totais).
- **Pattern-Key (Start-Process + redirect)**: `WaitForExit()` RP sem `Refresh()` Ã¢â€ â€™ ExitCode
  fica `$null`; e com `-RedirectStandardOutput`, `WaitForExit` pode retornar antes do fim.
  Fix robusto: loop `do{Start-Sleep 1000; $p.Refresh()} while(-not $p.HasExited)` e validar
  pela existÃƒÂªncia do arquivo de saÃƒÂ­da (sd-cli sÃƒÂ³ grava em sucesso). Nunca usar
  `Select-Object` final p/ ver log de comando async Ã¢â‚¬â€ buffer percebeu 10min como "morto".
- **Prompt com espaÃƒÂ§os no Start-Process**: `-ArgumentList` junta com espaÃƒÂ§o; o prompt string
  precisa de aspas embutidas (`'"a tiny banana..."'`) senÃƒÂ£o vira arg separado (erro
  `unknown argument: tiny`).
- **Curiosidade honesta**: SD-Turbo Q8_0 nÃƒÂ£o fotogera rosto/texto bem; ÃƒÂ³timo p/ objetos/
  cenas (banana, lanterna, flor Ã¢Å“â€œ). PNG 512Ãƒâ€”512 RGB vÃƒÂ¡lido; metadados embeddings vÃƒÂ£o no PNG.
- **GrÃƒÂ¡tis-Primeiro completo**: nenhuma API paga Ã¢â‚¬â€ engine open-source + modelo HF livre;
  2,35 GB em H: (249 MB C: eng. nÃƒÂ£o, tudo H:).
- **Seed real = 42 por padrÃƒÂ£o**: quando nenhum `-s` ÃƒÂ© passado, o sd-cli usa seed default 42
  (nÃƒÂ£o aleatÃƒÂ³rio). Logo, todas as "geraÃƒÂ§ÃƒÂµes aleatÃƒÂ³rias" desta sessÃƒÂ£o foram seed 42 Ã¢â‚¬â€ por
  isso a moÃƒÂ§a saiu consistente. O seed SEMPRE fica gravado no chunk `parameters` do PNG
  (`im.info['parameters']`, procura "Seed: "). Para reproduzir: mesmo prompt + mesmo seed.
- **img2img (mesma personagem, novas situaÃƒÂ§ÃƒÂµes)** Ã¢â‚¬â€ DESCOBERTA CHAVE para consistÃƒÂªncia de
  identidade: seed reduzido a prompt diferente gera "irmÃƒÂ£", nÃƒÂ£o a mesma pessoa. O caminho
  correto ÃƒÂ© reusar a imagem boa como base: `-i/--init-img <png>` + `--strength <float>`
  (default 0.75; usado 0.55 = preserva rosto, muda cena). Wrapper e `foto-*` agora
  aceitam `-Base <png>` e `-Forca`. Teste real: mulher do retrato seed 42 Ã¢â€ â€™ campo de
  girassÃƒÂ³is ao pÃƒÂ´r do sol, face preservada, 457s. Custou ~30% a mais que txt2img puro.
- **Banco de receitas (foto-banco)**: `H:\kai-local\foto-banco.ps1` + `foto-banco.json`.
  `foto-registrar -Prompt X -Arquivo Y [-Seed -Tamanho -Steps -Negative -Tags -Anotacoes]`
  guarda combos que ClÃƒÂ³vis elogiou; `foto-listar` mostra; `foto-sugerir "prompt"` retorna
  a receita de melhor match por palavra-chave + ponto de elogio (+5). KAI deve consultar
  o banco ANTES de gerar quando o prompt se aproximar de uma receita jÃƒÂ¡ validada.
  Carregado no profile junto de foto-comandos. Receita #1: retrato feminino seed 42.
- **Receita #1 (validada por elogio)**: quadrado 512, steps 4, cfg 1, head-and-shoulders,
  negativo anatomico completo (mÃƒÂ£os, dedos, rosto alongado, nariz longo) Ã¢â€ â€™ rosto lindo.
  Prompt em inglÃƒÂªs; orelha D sob cabelo = OK; pupila OD ~1-2px deslocada (limite 512px).
  Para fotografia de rosto: SEMPRE quadrado 512 (nÃƒÂ£o 512Ãƒâ€”768 Ã¢â‚¬â€ estica o rosto/nariz).
- **VISAO LOCAL (CIRCUNSTANCIA): Olhos de KAI via Ollama qwen3-vl:2b** Ã¢â‚¬â€ 100% gratuito,
  rodando na propria maquina do Clovis; coincide com a regra de consentimento (nada sai
  da maquina, sem API). Download 1,9 GB (`ollama pull qwen3-vl:2b`, servico ollama.exe
  ja rodava). Habilita descrever/verificar fotos geradas localmente.
  * Bugs que custaram 1h+ (GRAVAR): (1) campo `images` da API /api/chat fica DENTRO da
    message, nao no nivel raiz Ã¢â‚¬â€ errado, o modelo responde "I don't have eyes" e
    alucina; (2) qwen3 tem modo THINKING que consome tokens: com `num_predict` pequeno
    (200-300) o `content` sai vazio (so `thinking` preenchido). Fix: `images` dentro da
    message + `num_predict` >= 800 + `temperature 0`; resposta curta/fechada ajuda.
    (3) CLI `ollama run --image` NAO existe no Ollama 0.33.2 (flag so em versoes novas).
  * Mitigacao de alucinacao: descricao aberta ainda alucina cenario (2B); checagem
    FECHADA (sim;nao) e muito mais confiavel. Validado: 4/5 concordou com a descricao
    humana da foto (cabelo loiro, vestido 1 ombro, ceu laranja, arvores; errou girassois)
    e DETECTOU sozinho o defeito real da pupila descentralizada da receita #1 Ã¢â‚¬â€ o mesmo
    que o Clovis apontou. Temperatura 0 + thinking trace util como diagnostico.
  * Wrapper: `H:\kai-local\ver-foto.ps1` (funcao `ver-foto -Arquivo X [-Pergunta Y]
    [-Fechado] [-Modelo Z]`), carregada no profile. Tempo tipico: ~30s-3min (CPU).
  * Lemma: para corroborar a propria producao, preferir perguntas fechadas sobre itens
    chave; descricao aberta so como primeiro passe.

### Suggested Action
Usar `scripts/foto-local.ps1 -Prompt "..." -Steps 1 -Output <path>` (wrapper jÃƒÂ¡ valida
modelo/engine/tempo). Manter cfg-scale=1. Se precisar mais rÃƒÂ¡pido, `--preview tae` (decode
rÃƒÂ¡pido baixa qualidade) ou subir para SD-Schnell/SDXL-Turbo quando o usar. Nunca `cfg-scale 0`
(distilled ignora prompt). Status GPU: sem Vulkan/OpenCL ÃƒÂºtil nesta mÃƒÂ¡quina Ã¢â€ â€™ CPU-only.
Para VER fotos: `ver-foto <png>` (wrapper Ollama local, gratuito; perguntas fechadas para
confirmaÃƒÂ§ÃƒÂ£o, descriÃƒÂ§ÃƒÂ£o aberta para primeiro passe). Para otimizar futuras geraÃƒÂ§ÃƒÂµes:
`foto-sugerir "<prompt>"` consulta o banco de receitas elogiadas.

### Metadata
Source: primeira geraÃƒÂ§ÃƒÂ£o real 2026-09-07 (5 imagens) + Olhos de KAI 2026-09-08 (visÃƒÂ£o local)
Related Files: scripts/foto-local.ps1, scripts/tmp/seed/, H:\kai-local\sd-cpp\, H:\kai-local\models\, H:\kai-local\ver-foto.ps1, H:\kai-local\foto-banco.json
Tags: stable-diffusion, sd-cpp, sdturbo, gguf, cpu, local-first, vision, windows, prompt, ollama, qwen3-vl

---

## LRN-20260909-001 (vision) - Upgrade Olhos de KAI qwen3-vl:2b -> 4b + incidente id_ed25519

### Summary
Atualizado o modelo de visÃ¯Â¿Â½o local (Ollama 0.33.3) de `qwen3-vl:2b` para `qwen3-vl:4b`
(3.3 GB), vencendo na calibraÃ¯Â¿Â½Ã¯Â¿Â½o A/B. No meio da operaÃ¯Â¿Â½Ã¯Â¿Â½o, descobriu-se que a pasta
`C:\Users\clovi\.ollama` tinha sido apagada/limpa (chave `id_ed25519` + TODOS os modelos
sumiram) - causa provÃ¯Â¿Â½vel: limpeza de disco/otimizador (semelhante ao LRN-20260907-002).
RecuperaÃ¯Â¿Â½Ã¯Â¿Â½o exigiu gerar o par de chaves ed25519 manualmente.

### Learnings
- **Ollama 0.33.3 no Windows usa `C:\Users\clovi\.ollama\id_ed25519`** para assinar
  requests (pull/login/recommendations). Se a chave faltar, `ollama pull` falha com
  `pull model manifest: open C:\Users\clovi\.ollama\id_ed25519` e o servidor loga
  `Failed to load private key` repetidamente.
- **A chave NAO e regenerada sozinha nesta versao** (nem deletando a pasta e reiniciando).
  Fix documentado (GitHub #4901/#12345): parar o servico, gerar o par e colocar no lugar:
  `ssh-keygen -t ed25519 -f C:\Users\clovi\.ollama\id_ed25519 -N ""`. O Ollama aceita o
  formato OpenSSH (*.pub tambem). Depois reiniciar `ollama app.exe`.
- **Sintoma de store corrompido/limpo**: `ollama list` vazio, pasta `models\manifests`
  vazia (sem `blobs`), mas o server.log antigo citava "total blobs: 22, models=5".
  Nao existe backup dos blobs -> modelos precisam ser re-baixados.
- **Calibracao 2b vs 4b (mesma foto, verificacao fechada sim;nao, temperature 0)**:
  * Girassois (receita #3): 2b respondeu `nao` (errado! no thinking digitou "giraffe"),
    4b respondeu `sim` (correto).
  * Pupila descentralizada (receita #1): 2b travou em loop de thinking sem resposta
    (346s+), 4b respondeu `nao` em ~209s (correto).
  * Descricao aberta (retrato): 2b alucinava; 4b coerente (loira, cabelo curto, olhos
    azuis, sem defeitos) - sem alucinacao de asimetria. Tempo 4b ~200-700s (CPU).
- **CPU-only**: 4b fica mais lento (2-11min por resposta vs 30s-3min do 2b), porem
  muito mais confiavel nas verificacoes fechadas que importam. `keep_alive:"0"` ja evita
  ficar na RAM.
- **`.ollama` nao tem protecao contra limpeza**: recomendar adicionar excecao/whitelist
  do `C:\Users\clovi\.ollama` nas ferramentas de limpeza de disco, ou mover
  `OLLAMA_MODELS` para H: (214 GB livres) via env var.

### Suggested Action
`ver-foto` agora usa `qwen3-vl:4b` por default (2b mantido como fallback via `-Modelo`).
Se o `ollama pull` falhar com erro de id_ed25519: regenerar chave com ssh-keygen e
reiniciar servico (passo a passo no LRN). Se a pasta .ollama sumir de novo, re-baixar
os modelos (`ollama pull qwen3-vl:4b qwen3-vl:2b`) e gerar as chaves de novo.

### Metadata
Source: upgrade visao local 2026-09-09 (incidente id_ed25519 + calibracao A/B 2b vs 4b)
Related Files: C:\Users\clovi\.ollama\, H:\kai-local\ver-foto.ps1, C:\Users\clovi\kai-foto\foto-20260908-162304.png, C:\Users\clovi\kai-foto\foto-20260908-000421.png
Tags: ollama, qwen3-vl, vision, id_ed25519, ssh-keygen, windows, cpu, upgrade, incidente

---
## LRN-20260909-002 (audio) - Projeto Mandala Sonora: analisador polar FFT + gerador musical + export WAV/MP3 em um unico index.html offline

### Summary
Construido um sistema completo de visualizacao musical em `H:\kai-local\mandala-sonora\index.html`
(arquivo unico autocontido): mandala polar de 4 quadrantes (FFT via Web Audio), Indice de
Simetria heuristica 0-100%, modo comparacao A/B, gerador procedural de musica (sintese aditiva
com parciais f, 2f, 3f... gain 1/n = espectro harmonicamente simetrico POR CONSTRUCAO) com
presets Puro/Caos e seed reproduzivel, e export offline via OfflineAudioContext -> WAV PCM16 +
MP3 (lamejs baixado 1x e salvo localmente, uso sem CDN).

### Learnings
- **Zero dependencias de sistema**: decodificar+analisar+reproduzir MP3/WAV e possivel 100% no
  navegador via `decodeAudioData` + `AnalyserNode` (fftSize 2048) + Canvas 2D. Nao precisei de
  ffmpeg, scipy, librosa nem pydub (nenhum instalado no host).
- **Indice de Simetria como heuristica**: `0.45*espelho + 0.40*ordem + 0.15*estabilidade`.
  "Ordem" = 1 - flatness espectral (media geometrica/aritmetica dos bins) -> espectro com picos
  harmonicos = ordem alta; espectro plano/uniforme (ruido) = ordem baixa. Espelho compara energia
  normalizada entre quadrantes opostos. Resultado e rotulado como heuristica, nao veredito estetico.
- **Cuidado com synth de teste**: energia uniforme em todas as sub-bandas SAIREA como espectro
  "plano" (flatness~1) -> indice baixo, mesmo simetrica. O sinal de referencia correto para indice
  alto e um STACK HARMONICO (picos espacados), nao um espectro plano.
- **Scheduling musical em tempo real**: lookahead de 0.1s com intervalo de 25ms (padrao de SO de
  audio). Eventos dentro de compasso melhor que offset fixo em segundos: ruido de percussao a
  `t0 + k*barLen/4` (nao `t0 + k*0.7`) para nunca vazar fora da timeline (barLen varia com bpm).
- **lamejs offline**: baixar uma vez de `https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js`
  e referenciar local. Exposes global `Mp3Encoder(2, 44100, 128)`; alimentar com Int16ChannelData
  em blocos de 1152 samples e `flush()` no fim. WAV PCM16 manual via DataView (44-byte RIFF header).
- **Autoplay policy**: AudioContext so inicia por gesto do usuario (clique em Play). Resumir com
  `actx.resume()` no handler.
- **docstring do blob JS**: extrair `<script>` inline e rodar `node --check` valida sintaxe antes
  de testar no navegador. Bug classico: array de cores fechado com `];` em vez de `'],`.

### Suggested Action
Abrir `H:\kai-local\mandala-sonora\index.html` (duplo clique) e validar: Carregar arquivo no modo
Analisar -> tocar -> observar mandala e Indice; modo Comparar com 2 musicas; Gerar -> preset Puro
(deve dar indice mais alto que Caos); exportar WAV e MP3 (salvar em `H:\kai-local\MP3\`). Play de
tone/de ruido servem de calibracao visual (tone = alta, ruido = baixa).

### Metadata
Source: projeto Mandala Sonora 2026-09-09 (REANALISE! v2 aprovado -> implementacao)
Related Files: H:\kai-local\mandala-sonora\index.html, H:\kai-local\mandala-sonora\lame.min.js, H:\kai-local\MP3\
Tags: audio, web-audio-api, fft, mandala, visualizacao, sintese-aditiva, offline, lamejs, mp3, wav, windows

---
## LRN-20260909-003 (vision) - Ciclo gerar->verificar->corrigir: img2img e composicao, limites do SD-Turbo e do qwen3-vl:4b

### Summary
Experimento completo de correcao visual da aberracao `bizarre01.png` (mulher com 3 bracos,
perna-braco, colo disforme). Conclusao: o ciclo gerar->verificar->corrigir funciona com
img2img, mas (a) o modelo local 4b e NAO-CONFIAVEL para finura anatomica/fisica (alucinou
normalidade 3x: bizarro original, dedo-forquilha, asas rasgadas); (b) o SD-Turbo tem teto
real de ~512px e 4 steps, e pedir resolucao maior via img2img EMBACA em vez de refinar;
(c) composicao de personagem gerado em separado falha por falta de integracao de luz/sombra/
estilo (ficou um collage aparente).

### Learnings
- **qwen3-vl:4b (bateria fechada sim;nao) APROVA imagens com defeito gritante**: validou
  "dedos 5, rosto simetrico, sem defeito" numa fada que tinha braco mesclado a asa e dedos
  em forquilha. Pensamento racionaliza ("parece estilo"). Veredito final de QUALIDADE fina
  pertence SEMPRE ao olho humano (Clovis). O 4b serve para cena/objetos grossos (girassois ok),
  nunca para garantir ausencia de defeito anatomico.
- **SD-Turbo (stable-diffusion-v2-1-turbo, distilado 4 steps)**: img2img `-Forca 0.45-0.55`
  corrige geracoes: eliminou a mulher-monstro mantendo a cena. Resolucao >512 (768x1152) nao
  adiciona detalhe Ã¢â‚¬â€ borra (v5 ficou pior que v4: "embacou a gravura"). Seres minusculos
  (fadas) na cena viram orb ou somem; so se formam com sujeito em closeup preenchendo o quadro.
- **Composicao via PIL (luminance mask + paste) NAO integra**: bordas retas dos recortes,
  sem sombra, sem match de iluminacao/estilo/resolucao entre camada e fundo -> efeito collage
  inconfundivel. Falta mesclagem, sombra projetada, modifier de cor e brilho no tom do fundo.
  Feedback detalhado do Clovis catalogou: recortes retangulares, eco de camadas duplicadas,
  lens flare postico sem interagir com luz, cabecalho artificial, inconsistencia de estilo,
  iluminacao incoerente, resolucao diferente.
- **Start-Process para abrir PNG dispara a associacao do Windows**: UserChoice .png estava em
  dangling (handler inexistente) -> Windows sugeria instalar WidsMob Viewer (pago) da Store.
  Fix do habito de KAI: abrir com `ms-photos:?source=<path>` (Microsoft Photos instalado),
  sem depender de associacao. Nao instalar nada pago.

### Suggested Action
Nao registrar nenhuma receita praised deste experimento (final rejeitada). Se retomar fadas:
compor primeiro uma fada aceita, aplicar correcao de cor/brilho/sombra sobre a cena e rever
integrador de mascara (feather largo + mistura additiva de luz, nao paste seco). Abrir imagens
para o usuario SEMPRE via `ms-photos:?source=`.

### Metadata
Source: experimento bizarre01 2026-09-09 (gerar->verificar->corrigir, img2img x4, fadas x3, composicao trio)
Related Files: C:\Users\clovi\kai-foto\bizarre01.png, H:\kai-local\foto-local.ps1, H:\kai-local\ver-foto.ps1, C:\Users\clovi\kai-foto\bizarre01_final.png
Tags: vision, stable-diffusion, img2img, composicao, PIL, alucinacao, qwen3-vl, sd-turbo, ms-photos, widsmob

---
## LRN-20260909-004 (vision) - bizarre02: retrato com orelhas/contorno ausentes, olhos nao concentricos, nariz alongado, cabelo desligado, pele "porcelana"

### Summary
Analise do retrato `bizarre02.png` (mulher jovem, close facial 512x768, seed 42). O modelo
local qwen3-vl:4b FALHOU mais uma vez (content vazio, thinking consumiu tudo e negou ver a
imagem: "I can't see the image"). Veredito anatomico veio do olho humano (Clovis), como regra.

### Learnings
- **KAI/base atual sem visao direta**: ao ler o PNG via ferramenta, erro "model does not support
  image input". Os olhos de KAI sao (hoje) apenas o Ollama local Ã¢â‚¬â€ insuficiente para finura.
- **Novo padrao de falha do 4b**: alucinacao de INCAPACIDADE (nega visualizar) alem da alucinacao
  de normalidade. Nunca confiar em "nao vejo defeito" vindo de modelo local para retrato.
- **Defeitos canonicos de retrato SD-Turbo**: olhos nao concentricos (iris/pupila), reflexo de
  luz fraco ("olhar morto"), simetria facial duvidosa, nariz alongado com ponta dissolvida,
  cabelo com fios flutuantes/linha confusa, pele sem microtextura (porcelana), boca com comissura
  indefinida, pescoco/ombros vagos (rosto flutuando).
- **Bateria fechada granular NAO salvou**: 10 perguntas sim;nao por zona ainda resultou em
  thinking gigante sem resposta. Limite estrutural do 4b para questoes encadeadas longas.

### Suggested Action
Investigar meios de dar visao real a KAI (LRN pendente "olhos de KAI"): modelo de base com
suporte a imagem, OCR local (PaddleOCR/MCP vision), ou CV deterministica (landmarks faciais via
OpenCV) para assimetria Ã¢â‚¬â€ verificado numericamente, nao por alucinacao. Padrao: o que for
verified por coordenadas (olhos no mesmo nivel, etc.) > VLM. Continuar registrando vereditos do
olho humano como ground truth.

### Metadata
Source: experimento bizarre02 2026-09-09 (retrato 512x768 seed 42, analise 4b falhou, veredito Clovis)
Related Files: C:\Users\clovi\kai-foto\bizarre02.png
Tags: vision, retrato, qwen3-vl, alucinacao, ground-truth, clovis, landmarks, OCR

---
## LRN-20260911-005 (vision) - olhos de KAI v1: CV deterministica (OpenCV) > VLM local; convergencia 5/5 com veredito humano

### Summary
Fechamento do arco "olhos de KAI". Caminhos de VLM testados e descartados para finura
anatomica de retrato: qwen3-vl:4b (alucina normalidade E incapacidade), Gemini Vision
(chave invalida - API_KEY_INVALID), MiniMax vision (mmx vision describe autenticado mas
conta sem saldo: "insufficient balance"). Solucao v1 instalada e calibrada: **olho
DETERMINISTICO via OpenCV** - 100% local, gratis, sem alucinacao, converge 5/5 com veredito
humano nas imagens do kai-foto.

### Learnings
- **CV deterministica > VLM para medicao**: coordenadas nao mentem. Deteccao de face por
  cascates Haar (multi-cascade + votacao de maior area), olhos por 3 detectores
  (eye, lefteye, righteye) com `best_pair` + voto de maioria (ALINHADO/DUVIDOSO/DESALINHADO).
  Alinhamento oclito em px absolutos; classes normalizadas (dy/diametro ocular).
- **Concetricidade de pupila**: centroide ponderado por escuridao dentro de cada ROI ocular
  (bilateralFilter + percentile). Detectou numericamente a pupila direita descentrada da
  quase02 SEM ver a imagem - igual ao veredito visual do Clovis.
- **Ãƒâ€šncoras de calibracao** (veredito humano = ground truth): girassois ALINHADO (0-1px,
  pupila 6x6 SIM); quase02 DUVIDOSO/ACEITAVEL (6-13px, pupila direita descentrada tolerada);
  bizarre02 DESALINHADO; bizarre01 SEM_OLHOS (aberraÃƒÂ§ÃƒÂ£o). Limiar: classe normalizada
  <=0.05 ALINHADO, <=0.35 DUVIDOSO, >0.35 DESALINHADO (recape in v2.1).
- **Validacao essencial**: anotacoes PNG (caixa rosto vermelha, caixas de olho verdes,
  pupila amarela/verde) como EVIDENCIA visual antes de confiar na metrica. Cores BGR no
  OpenCV: (0,255,255)=amarelo, (0,0,255)=vermelho; (200,200,0)=ciano (NAO amarelo).
- **Serializacao numpy**: cv2/np retorna np.float32/int32 - nao JSON serializavel; converter
  com float(x)/round antes de json.dumps. Detector Haar em ROIs pequenos conflunde nariz/boca
  com olho; restringir a metade superior do rosto + filtro de plausibilidade (tamanho
  0.06-0.35x, separacao 1.5-4x diametro).
- **VLM paths fechados hoje**: mmx vision OK de infra (sem saldo), Gemini chave invalida.
  Se crÃƒâ€°ditos forem ativados, VLM vira olho #2 (descricao grossa), nunca substitui o
  determinismo para medida.
- **Receita #4 (foto-banco) descredita**: img2img forca 0 + 1 step + prompt PT = aberraÃƒÂ§ÃƒÂ£o
  3-bracos; "4b confirmou sem defeitos" = falso positivo de alucinacao. Nunca confiar no
  veredito de modelo local para anatomia; veredito humano SEMPRE ground truth.

### Suggested Action
PrÃƒÂ³ximo passo deste ciclo fica em PAUSA por decisao do Clovis (foco em tarefas novas);
ferramenta `H:\kai-local\olhos-kai.ps1` v2.1 pronta e calibrada. Quando retomar o ciclo de
desenho: usar `olhos-kai <img> -Anotar` como triagem deterministica + veredito humano em
seguida. Nunca tempo-real: retratos SD-Turbo tem pupila descentrada toleravel (quase02 =
"bom o suficiente"); buscar perfeicao oclÃƒÂ­tica perfeita de 0px nao e realistico.

### Metadata
Source: fechamento arco olhos-de-KAI 2026-09-11 (CV deterministica OpenCV v1/v2/v2.1, calibracao 3 ancorns + 5 complementares)
Related Files: H:\kai-local\olhos-kai.ps1, C:\Users\clovi\kai-foto\anotado\anot_*.png, H:\kai-local\foto-banco.json (receita #4)
Tags: vision, opencv, cv, deterministic, haar-cascade, pupila, calibracao, alucinacao, ground-truth, minimax, gemini, qwen3-vl, sd-turbo

---

## LRN-20260913-001 (tÃƒÂ©cnica) - Contraponto procedural em escala: consonÃƒÂ¢ncias precisam ser mode-aware, nÃƒÂ£o offsets cegos

**Logged**: 2026-09-13
**Priority**: medium
**Status**: active
**Project**: mandala-sonora
**Area**: audio-generation
**Pattern-Key**: counterpoint-scale-aware-consonances

### Summary
Ao gerar um contraponto com "notas consonantes = raiz do acorde + offsets fixos {+3,+4,+7,+9,+12,+16}" sobre acordes modais, o terceiro grau sai da escala sempre que a trÃƒÂ­ade nÃƒÂ£o ÃƒÂ© maior (ex.: modo iÃƒÂ´nico, grau 2 (B) Ã¢â€ â€™ B+4 = DÃ¢â„¢Â¯, inexistente na escala). O contraponto vazava DÃ¢â„¢Â¯ e criava oitavas paralelas com a melodia. Fix: as consonÃƒÂ¢ncias candidatas devem ser **notas da escala cuja distÃƒÂ¢ncia ÃƒÂ  raiz do compasso ÃƒÂ© consonante** (dist. Ã¢Ë†Ë† {0,3,4,5}), filtradas por intervalo simultÃƒÂ¢neo Ã¢â€°Â  unÃƒÂ­ssono/5Ã‚Âª/8Ã‚Âª contra melodia e bass Ã¢â‚¬â€ inclusive na nota inicial do contraponto.

### Details
- Sintoma detectado por teste: eventos fora da escala (freq 622.25 = DÃ¢â„¢Â¯5) sÃƒÂ³ em contraponto; oitava E7Ãƒâ€”E5 entre melodia e contraponto na nota inicial (init nÃƒÂ£o passava pelo filtro anti-paralela).
- BUG de inversÃƒÂ£o tambÃƒÂ©m flagrado: `if(!scalePcs.includes(...)) push()` gerava consonÃƒÂ¢ncias *fora* da escala.
- LiÃƒÂ§ÃƒÂ£o de design para gerador modal: a consonÃƒÂ¢ncia depende da ESTRUTURA DA ESCALA no contexto (grau/acorde corrente), nÃƒÂ£o de intervalos fixos sobre a raiz; e a escolha de notas deve fechar a escala por construÃƒÂ§ÃƒÂ£o, com filtros de voz (paralelas) aplicados em TODAS as vias (init + passo).

### Suggested Action
Em qualquer mÃƒÂ¡quina de harmonizaÃƒÂ§ÃƒÂ£o/contraponto procedural com escalas modais ou exÃƒÂ³ticas: gerar candidatos filtrando pela escala (pitch class Ã¢Ë†Ë† scale) e consonÃƒÂ¢ncia relativa ÃƒÂ  raiz corrente; aplicar os filtros de voz (uni/5Ã‚Âª/8Ã‚Âª simultÃƒÂ¢neas) em todas as ramificaÃƒÂ§ÃƒÂµes de escolha. Validar por propriedade: "toda nota Ã¢Ë†Ë† escala" e "sem intervalos paralelos {0,5,7}" em eventos simultÃƒÂ¢neos.

### Metadata
Source: implementaÃƒÂ§ÃƒÂ£o Gerador V2 / Orquestra Modal 2026-09-13
Related Files: H:\kai-local\mandala-sonora\index.html (buildCompositionV2), C:\Users\clovi\AppData\Local\Temp\opencode\ms-v2-test.js
Tags: counterpoint, modal, scale-aware, consonance, procedural-music, web-audio, parallel-fifths, nc
Pattern-Key: counterpoint-scale-aware-consonances

---

## LRN-20260913-002 (tÃƒÂ©cnica) - scaleDegreeMidi nÃƒÂ£o cobre graus negativos; validar escala por pc relativa, nÃƒÂ£o por graus

**Logged**: 2026-09-13
**Priority**: low
**Status**: active
**Project**: mandala-sonora
**Area**: music-generation
**Pattern-Key**: scale-degree-negative-safe

### Summary
`scaleDegreeMidi(root, deg, intervals)` calcula `intervals[deg]` (ÃƒÂ­ndice direto) Ã¢â‚¬â€ para `deg<0` produz `intervals[-n] = undefined` Ã¢â€ â€™ NaN. No produto nunca passou grau negativo (bass usa `midi-12`, nÃƒÂ£o grau), mas causou falso-negativo na SUITE: a grid de frequÃƒÂªncias permitidas foi construÃƒÂ­da com `scaleDegreeMidi(root, d+12*oct)` e `oct` negativo Ã¢â€ â€™ set sem os graves do bass (G2) Ã¢â€ â€™ 38 eventos "fora da escala" que eram, na verdade, notas perfeitamente em escala (pc Ã¢Ë†Ë† intervals).

### Details
- Sintoma: grelha 24 combos falhou sÃƒÂ³ em "gregoriano/tet/curta"; debug mostrou `rel Ã¢Ë†Ë† iv` true para TODOS os "fora" Ã¢â‚¬â€ era cobertura do teste, nÃƒÂ£o bug do cÃƒÂ³digo.
- Fix no harness: validar escala **por faixa de MIDI com pc relativa ÃƒÂ  raiz** (`for m in 24..110: if iv.includes(((m-rootMidi)%12+12)%12)`), mÃƒÂ©todo que tambÃƒÂ©m funciona com afinaÃƒÂ§ÃƒÂ£o justa (mesma pc Ã¢â€¡â€™ mesma razÃƒÂ£o racional).
- LiÃƒÂ§ÃƒÂ£o dupla: (1) utilitÃƒÂ¡rios de grau precisam de guarda para ÃƒÂ­ndices negativos (`((deg%len)+len)%len`); (2) property-tests de escalas devem usar intervalo de MIDI/pc e explicitar flags de "notas deliberadamente fora" (blue) em vez de listas derivadas por mÃƒÂºltiplos de oitava de graus.

### Suggested Action
Se usar `scaleDegreeMidi` com graus relativos/negativos no futuro, normalizar o ÃƒÂ­ndice antes de indexar `intervals`. Para property-tests de "toda nota na escala", derivar o conjunto permitido por pc relativa na faixa real de registros (Sempre incluir os graves do bass).

### Metadata
Source: implementaÃƒÂ§ÃƒÂ£o Gerador V3 / Orquestra Viva 2026-09-13
Related Files: H:\kai-local\mandala-sonora\index.html (buildCompositionV2), harness ms-v3-test.js
Tags: scale-aware, property-testing, midi, modal, harness, index-out-of-range
Pattern-Key: scale-degree-negative-safe

---

## LRN-20260913-003 (tecnica) - Pausa real em Web Audio: offset do buffer + scheduler retomavel por timeline, nao restart

**Logged**: 2026-09-13
**Priority**: medium
**Status**: active
**Project**: mandala-sonora
**Area**: web-audio-playback
**Pattern-Key**: resumable-audio-offset

### Summary
"Tocar/Pausar" que faz stop()+start(0) volta do comeco. Para pausa REAL precisa de duas coisas: (1) buffer: registrar slotStartedAt=ctx.currentTime no start e, ao pausar, salvar pausedOffset=clamp(now-slotStartedAt, 0, dur-0.05); retomar com src.start(0, offset). (2) gerador (scheduler lookahead por timeline): refatorar o corpo original em schedulePlayback(comp, elapsed), onde elapsed>0 deriva loop=floor(elapsed/total), inL=elapsed-loop*total, o ponto de retomada via events.findIndex(e=>e.t>=inL-0.01) e 	imelineStart=wall+0.06-inL; pausa guarda elapsed e derruba interval/sons (softStopGen sem limpar estado); resume re-agenda a partir do offset.

### Details
- Erro original: 	ogglePlay usava stopGen()/stopSlot() e posterior src.start(0) -> sempre reiniciava; usuarios esperam Continuar de onde parou.
- Estado extra: pausedOffset={A,B}, slotStartedAt={A,B} (arquivos), genPaused, genStartWall (gerador). genStartWall carrega o elapsed na pausa e vira wall-clock novo no resume.
- Regra muda: no loop(ts), dt>=0.016 gate com 
equestAnimationFrame; sem som o analyser devolve zeros (reta/barra neutra) â€” ok como "nada detectado".
- Drag&drop so em drop-zones laterais nao satisfez UX: registrar bindDrop tambem nos .canvasCard (drop) e um click que abre o <input type=file> (clique na area central abre o seletor) â€” padrao de produto.

### Suggested Action
Ao implementar play/pause em qualquer player: nunca src.start(0) sem guardar offset; Duration-0.05 evita start no fim do buffer. Para sintetizadores com scheduler, modelar resume como "posicao na timeline" (consumir elapsed para derivar loop+timelineStart), nao como re-agendamento do comeco.

### Metadata
Source: implementacao V4 "Analisador Vivo" 2026-09-13
Related Files: H:\kai-local\mandala-sonora\index.html (togglePlay, schedulePlayback, pauseGen/resumeGen, bindDrop)
Tags: web-audio, pause-resume, scheduler, offset, playback, ux

---

## LRN-20260914-001 (tecnica) - Navegador nao expoe o path completo do arquivo: padrao pasta-base + origem (real|rel|base|manual) + edicao manual

**Logged**: 2026-09-14
**Priority**: high
**Status**: active
**Project**: mandala-sonora
**Area**: local-file-app
**Pattern-Key**: browser-path-privacy-base-folder

### Summary
Em app 100% local (`file://`), o navegador NAO expoe o path absoluto do arquivo escolhido por design (privacidade). `File.path` Ã© legado e vazio na maioria dos navegadores; `File.webkitRelativePath` sÃ³ existe em drag&drop de pasta. PadrÃ£o usado na Biblioteca do Mandala Sonora: **pasta base configurÃ¡vel + caminho montado + tag de origem honesta (`real`/`rel`/`base`/`manual`) + ediÃ§Ã£o manual por item + nota na UI** explicando a limitaÃ§Ã£o.

### Details
- `pathForFile(f)`: tenta `File.path` (try/catch â†’ `real`), depois `webkitRelativePath` (`rel`), senÃ£o monta `baseFolder + nome` (`base`); usuÃ¡rio pode editar no item â†’ `pathSrc:'manual'`. Base default `H:\kai-local\MP3` (sem barra final), gravada em `localStorage` (`mandalaSonora_baseFolder`).
- **localStorage em `file://` Ã© frÃ¡gil** (origin opaca/partilhada entre navegadores; chave muda se o `index.html` for movido) â†’ export/import JSON como backup/portabilidade.
- PersistÃªncia com upsert dedupe por `name|path` + cap `slice(0,5000)` + mensagem de quota cheia; entrada `{id: name|path, name, path, pathSrc, addedAt, analyzedAt, analysis}`.
- GravaÃ§Ã£o automÃ¡tica sÃ³ para anÃ¡lise real (>=1s, `idxN>=8`); gerado sintÃ©tico nÃ£o entra na biblioteca.

### Suggested Action
Em qualquer app local que precise lembrar caminhos de arquivo: NÃƒO tentar "adivinhar" o path absoluto que o browser nÃ£o dÃ¡. Pedir pasta base configurÃ¡vel + tag de origem + ediÃ§Ã£o manual; nunca prometer `path.real` falso. Acompanhar localStorage com export/import JSON (quota/portabilidade).

### Metadata
Source: biblioteca V6 2026-09-14 (Mandala Sonora)
Related Files: H:\kai-local\mandala-sonora\index.html (pathForFile, saveLibrary, editBibPath)
Tags: file, path-plumbing, webkitRelativePath, localStorage, file-protocol, privacy, offline-app, windows
Pattern-Key: browser-path-privacy-base-folder

---

## LRN-20260914-002 (tecnica) - Fim natural de audio: corrida entre ticker 250ms e audio.onended; o handler nativo Ã© o dono unico do evento

**Logged**: 2026-09-14
**Priority**: medium
**Status**: active
**Project**: mandala-sonora
**Area**: web-audio-playback
**Pattern-Key**: onended-single-source-of-truth

### Summary
Corrida classica de player: ticker de 250ms comparando `currentTime >= duration` perde do `audio.onended` no fim natural â€” o estado jÃ¡ foi limpo quando o prÃ³ximo tick roda. Fix: `playingFile[slot]=null` Ã© atribuÃ­do DENTRO do prÃ³prio `src.onended`, ANTES de `finishSlot()`. O handler nativo do `ended` Ã© a fonte Ãºnica de verdade do tÃ©rmino; tickers sÃ³ atualizam UI.

### Details
- V5.3 (anÃ¡lise no Parar): â–  Parar mostra a anÃ¡lise atÃ© aquele ponto (nÃ£o descarta o ouvido); o banco (E/O/Es + impressÃ£o em uma linha) aparece no fim natural E no Parar.
- Fila multi-mÃºsica (V6): 1Âª toca no slot A, resto em `pendingFiles`; `showFinalPanel` com `next` exibe botÃ£o "â–¶ PrÃ³xima da fila (N)"; `#queueInfo` acompanha.
- Render reutilizÃ¡vel: `analysisRowsHTML(s)` extraÃ­do e usado no painel E nos detalhes da biblioteca â€” uma fonte sÃ³ de leitura, sem divergÃªncia.

### Suggested Action
Em qualquer player web: deixar `audio.onended`/`media.onended` como Ãºnico dono do "terminou" (limpar estado lÃ¡ dentro) e nunca derivar fim de tickers de progresso. Para render repetido entre painel e listas: extrair function Ãºnica.

### Metadata
Source: V5.3/V6 2026-09-14 (Mandala Sonora)
Related Files: H:\kai-local\mandala-sonora\index.html (onended, finishSlot, addFilesToQueue, loadNextQueued, analysisRowsHTML)
Tags: web-audio, onended, race-condition, player, queue, render-reuse, natural-end
Pattern-Key: onended-single-source-of-truth

---

## LRN-20260915-001 (tecnica) - Pre-analise offline do inicio (ACF + decimacao) elimina o "tunel" do quadro 1 no replay

**Logged**: 2026-09-15
**Priority**: high
**Status**: active
**Project**: mandala-sonora
**Area**: web-audio-analysis
**Pattern-Key**: pre-analyze-intro-offline

### Summary
No primeiro play de slot (fromOffset=0, sem savedMel), a analise MEL real demora e o replay comeca com silencio ou congelamento. Solucao: pre-analise offline dos primeiros 6 segundos (PREANAL_SECS=6) via decimacao x5 (~8.8 kHz), ACF em janelas de 0.13s com hop 0.05s, correcao de oitava (lag/2), segmentos >=0.16s, compressMel RLE identico ao replay. Resolve em ~50 ms em CPU moderna e popula analysis[slot].mel antes do primeiro frame de reproducao. Resultado: o replay comeca com notas imediatamente (sem "tunel" no quadro 1) e e 100% identico ao que a analise real produziria.

### Details
- Trigger em playSlot: `if(!savedMel[slot] && fromOffset<=0 && PREANAL_SECS > 0) { preAnalyzeIntro(slot); }` â€” so roda uma vez por slot no primeiro play; loadedMel (arquivo) nao dispara.
- Decimacao x5: resampling offline sem Web Audio; frequencia efetiva ~8820 Hz preserva o fundamental dos instrumentos testados.
- compressMel RLE e a mesma funcao usada no replay; a assinatura e bit-identica, garantindo fidelidade.
- Custo: ~40-55 ms em i7-12700 (benchmark local); comparado a ~6s de duracao real do trecho analisado.

### Suggested Action
Em qualquer player web que tenha analise de pitch live e prefitura armazenada, considerar pre-analise offline do trecho inicial (1-8s) com a mesma logica de quantizacao/assinatura que o replay usa. O padrao e: offline decode (sem AudioContext) -> mesma funcao de analise em modo batch -> resultado cacheado no analysis[].mel antes do primeiro start(0).

### Metadata
Source: V7.3.4 2026-09-15 (Mandala Sonora)
Related Files: H:\kai-local\mandala-sonora\index.html (preAnalyzeIntro, PREANAL_SECS, playSlot, compressMel)
Tags: web-audio, pitch-analysis, acf, offline, replay, cold-start, ui-tunnel, decimation
Pattern-Key: pre-analyze-intro-offline

---

## LRN-20260915-002 (tecnica) - Origem deterministica via estado global (genWasActive) em vez de heuristica para decisao de biblioteca

**Logged**: 2026-09-15
**Priority**: medium
**Status**: active
**Project**: mandala-sonora
**Area**: local-file-app
**Pattern-Key**: origin-state-over-heuristic

### Summary
Quando uma entrada na biblioteca pode ter origem dupla (arquivo carregado pelo usuario OU predefinicao gerada pelo proprio app), a decisao de "o que mostrar no painel" precisa ser deterministica e nao heuristica (ex.: comparar path ou nome). Solucao: flag `genWasActive` setada no inicio de `startPlayback`, resetada em `playSlot`. `buildLibraryEntry` ramifica por ela: gerado = titulo A + path:'(gerado)' + fallback lastComposition; arquivo = pathForFile(f). `addToLibrary` deduplica por `bibKey` = name|path|size, entao re-salvar gerado atualiza a entrada sem duplicar.

### Details
- Heuristica original: "se o path contem '(gerado)', e sintetico" â€” quebrava quando o usuario editava o path manualmente e a tag perdia contexto.
- Estado global e mais caro em acoplamento mas e infalivel: so `startPlayback` conhece a intencao do usuario no momento exato.
- `buildLibraryEntry` agora e pura (sem side-effects), o que facilita testes futuros.

### Suggested Action
Quando um item pode ser criado por dois caminhos (usuario vs. automacao), armazenar a origem como dado explicito na entrada, nao derivar por heuristica de campos derivados. Se a decisao precisa ser tomada no momento de exibicao, um flag global setado no momento da acao e mais seguro que reconstituir o historico a cada render.

### Metadata
Source: V7.3.4 2026-09-15 (Mandala Sonora)
Related Files: H:\kai-local\mandala-sonora\index.html (genWasActive, startPlayback, playSlot, buildLibraryEntry, addToLibrary)
Tags: state-management, heuristic-vs-deterministic, dedup, library, ux
Pattern-Key: origin-state-over-heuristic

---

## LRN-20260915-003 (tecnica) - Display de status sempre antes do guard de audio (updateBinLive antes de if(!actx))

**Logged**: 2026-09-15
**Priority**: low
**Status**: active
**Project**: mandala-sonora
**Area**: web-audio-playback
**Pattern-Key**: display-before-audio-guard

### Summary
`updateBinLive` (barra de status do lado esquerdo: barra de energia + frequencia neural + BPM) estava localizada no codigo APOS o guard `if(!actx) return;`. Quando nao havia AudioContext (app aberto pela primeira vez, antes do primeiro play), a barra nao atualizava â€” ficava zerada mesmo com `lastKnownBpm` setado. Fix: mover `updateBinLive()` para antes do guard. O display de status e um componente visual que nunca deve depender da existencia de hardware ativo.

### Details
- `lastKnownBpm` salva o ultimo BPM parado (de qualquer analise) para que o ticker continue exibindo valor util mesmo em modo "off (previa)".
- UI de display e independente do pipeline de audio; nao tem side-effects no AudioContext; posicao no codigo deve refletir essa independencia.
- Padrao observado em outros contextos: controles de estado (botoes disabled/enabled) podem ficar apos guards; display de informacao (labels, barras, status) sempre antes.

### Suggested Action
Em qualquer aplicacao web com separacao display/audio: sempre posicionar atualizacoes de display de status ANTES de guards de inicializacao de hardware/subsistema. Display e informacao; hardware e efeito colateral. A informacao deve ser visivel mesmo quando o efeito ainda nao existe.

### Metadata
Source: V7.3.4 2026-09-15 (Mandala Sonora)
Related Files: H:\kai-local\mandala-sonora\index.html (updateBinLive, lastKnownBpm, if(!actx))
Tags: web-audio, ui-display, guard-order, status-bar, software-architecture
Pattern-Key: display-before-audio-guard

---

## [LRN-20260915-004] worklet-degradable-graph

**Logged**: 2026-09-15T16:00:00-03:00
**Priority**: high
**Status**: active
**Project**: mental-shields
**Area**: web-audio

### Pattern-Key
worklet-degradable-graph

### Summary
Em aplicacoes Web Audio com AudioWorklet, a falha de `addModule()` (worklet nao carrega por CSP, rede, ou offscreen doc) derrubava o grafo INTEIRO: a excecao impedia `updateAudioGraph()`, matando tone/binaural/iso que nao dependem do worklet. Fix: capturar o erro de `addModule`, setar `workletFailed=true`, e continuar o start. O grafo degrada para as fontes independentes do worklet; `createContinuousNoise()` retorna graciosamente se `!workletReady`. Fonte de ruido e um efeito aditivo â€” nunca deve ser ponto unico de falha para tone/binaural/iso.

### Details
- `start()` faz `try { await ctx.audioWorklet.addModule(...) } catch { workletFailed=true } finally { starting=false }` e prossegue para `updateAudioGraph()`.
- `new AudioWorkletNode()` dentro de `createContinuousNoise()` lanca se o processador nao foi registrado â€” guard `if (!this.workletReady) return;` obrigatorio.
- Expor `workletReady`/`workletFailed` no `getStatus()` para a UI refletir o estado sem heuristica.
- Testavel em Node: stub de AudioContext com `addModule` lancando; assert de que `isPlaying=true` e `noiseNode===null`.

### Suggested Action
Ao usar Web Audio com worklet, tratar o worklet como camada opcional: try/catch no addModule, guard no ponto de criacao do AudioWorkletNode, e status exposto. Testar os dois caminhos (worklet OK / worklet falho).

### Metadata
Source: sessao encerramento Mental-Shields 2026-09-15
Related Files: D:\ExtensÃ£o\mental-shields\audio-engine.js (start, createContinuousNoise, getStatus)
Tags: web-audio, audioworklet, degradation, error-handling, offscreen
Pattern-Key: worklet-degradable-graph

---

## [LRN-20260915-005] start-idempotent-before-side-effect

**Logged**: 2026-09-15T16:00:00-03:00
**Priority**: medium
**Status**: active
**Project**: mental-shields
**Area**: web-audio

### Pattern-Key
start-idempotent-before-side-effect

### Summary
O pomodoro do Mental-Shields rodava em silencio completo quando o usuario disparava "Iniciar Pomodoro" sem ter ativado o power toggle antes: `enterPomodoroPhase('work')` setava noise/binaural mas, com `isPlaying=false`, esses setter nao chamavam `updateAudioGraph()` e o motor nunca ligava. Fix: `startPomodoro()` agora faz `await this.start()` â€” que e idempotente (retorna cedo se `isPlaying`) â€” ANTES de configurar a fase. Toda operacao que presume motor ligado deve garantir o start por conta propria.

### Details
- `start()` com guard `if (this.starting || this.isPlaying) return;` e seguro para re-entrada.
- `startPomodoro` virou `async` e chama `await this.start()` antes de `enterPomodoroPhase`. 
- No bridge do offscreen, o case `startPomodoro` precisa de `.catch()` pois agora e Promise (erro assincrono nao capturado = unhandled rejection).
- Teste: engine parado â†’ `startPomodoro()` â†’ `isPlaying===true`, `phase==='work'`, noiseType=branco, binaural 14Hz.

### Suggested Action
Ao projetar teclas de atalho (feature X inicia "para" um motor), nunca assumir que o motor ja esta ligado: chamar o start idempotente por conta da feature. Qualquer consumidor de uma Promise que antes era sync deve ser auditado (`.catch` no listener).

### Metadata
Source: sessao encerramento Mental-Shields 2026-09-15
Related Files: D:\ExtensÃ£o\mental-shields\audio-engine.js (startPomodoro), offscreen.js (case 'startPomodoro')
Tags: web-audio, idempotent-start, pomodoro, async-bridge
Pattern-Key: start-idempotent-before-side-effect

---

## [LRN-20260915-006] migrate-all-not-first

**Logged**: 2026-09-15T16:00:00-03:00
**Priority**: medium
**Status**: active
**Project**: mental-shields
**Area**: storage

### Pattern-Key
migrate-all-not-first

### Summary
`migratePresets()` do Mental-Shields salvava apenas o primeiro preset (`presets.find(p => p.id === 'foco')`) apos migrar N presets contra os defaults â€” os demais migrados (ex.: 'meditacao') atualizavam o array em memoria mas nunca iam ao storage, sendo perdidos no proximo reload. Fix: marcar cada preset com flag `migrated=true` quando dirty e persistir TODOS os sinalizados, removendo a flag antes do save. Migracao em lote deve persistir todos os itens alterados, nunca um subconjunto heuristico.

### Details
- Usou flag transiente `merged.migrated` para rastrear dirty por item; o `toSave` e uma copia sem a flag (storage nao deve receber flag de migracao).
- Presets ja em dia com os defaults nao sao re-salvos (menos escritas).
- Teste em Node: 2 presets dirty â†’ ambos persistidos; presets corretos + custom â†’ intocados.

### Suggested Action
Em qualquer migracao de dados persistidos em lote, iterar sobre todos os itens dirty e persistir todos, com flag temporaria de rastreio. Validar com teste que compare a lista de IDs salvos contra os dirty.

### Metadata
Source: sessao encerramento Mental-Shields 2026-09-15
Related Files: D:\Extensï¿½o\mental-shields\popup.js (migratePresets, loadPresetsList)
Tags: migration, batch-persist, storage, popup
Pattern-Key: migrate-all-not-first

---

## [LRN-20260915-007] sprite-mutex-kill-mutuo

**Logged**: 2026-09-15T18:30:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder (kai-presence)
**Area**: presence, process-lifecycle

### Pattern-Key
sprite-mutex-kill-mutuo

### Summary
O auto-start do sprite KAI falhava silenciosamente: o plugin carrega em 2+ processos (hot-reload multi-processo), cada um spawna um `pythonw.exe` ao boot; o segundo via `KAI_Sprite_Mutex` ocupado, assumia "zumbi" e dava `taskkill /F` NO sprite legitimo â€” que morria junto, sem `run:` no log. Agravante: `_kill_zombie_sprite()` matava QUALQUER `pythonw.exe`. Fix: sprite grava `.kai-sprite.pid`; so mata o "zumbi" se o dono do mutex estiver MESMO morto (`OpenProcess`); plugin faz dedupe cross-processo checando o PID registrado antes de spawnar.

### Details
- Sintoma: `.kai-presence.json` atualizado (emissor vivo), mas zero sprite na tela; log `sprite-error.log` silencioso por 4 dias; spawns gÃªmeos `ensureSprite: spawned ... (pid X)` no log do plugin.
- Race real: 17:49 os pids 6192 e 26972 nasceram juntos; ambos morreram â€” segundo matou o primeiro, e o retry do segundo falhou porque o mutex ainda nÃ£o fora liberado.
- Validacao ao vivo: spawn via `pythonw` â†’ vivo apÃ³s 7s, `run:` registrado; 2Âº spawn â†’ dedupe correto (saiu, o 1Âº sobreviveu).
- Regra de ouro: nunca matar um processo cujo Ãºnico crime Ã© ser parecido (pythonw) â€” verificar liveness real do dono do recurso disputado antes.

### Suggested Action
Quando um auto-start exige instÃ¢ncia Ãºnica entre processos lanÃ§adores: (1) o processo ganhador deve persistir seu PID num arquivo; (2) o perdedor sÃ³ destrÃ³i o "zumbi" se o PID registrado estiver morto; (3) o launcher (plugin) deve deduplicar antes de spawnar, checando o PID file com `tasklist /FI "PID eq X"`. Testar dedupe com 2 spawns consecutivos.

### Metadata
Source: sessao 2026-09-15 (presenÃ§a restaurada)
Related Files: scripts/kai_sprite.py (single_instance_lock, write_sprite_pid, _pid_alive), plugins/kai-presence.js (ensureSprite, readSpritePid, pidAlive)
Tags: pythonw, tkinter, mutex, race-condition, spawn, autostart, dedupe, presence
Pattern-Key: sprite-mutex-kill-mutuo

---

## [LRN-20260915-008] subgraph-in-running-engine

**Logged**: 2026-09-16T09:00:00-03:00
**Priority**: medium
**Status**: active
**Project**: mental-shields
**Area**: web-audio

### Pattern-Key
subgraph-in-running-engine

### Summary
Ao adicionar um sub-grafo novo (`startCoordProtocol`: oscillators centrais) a um AudioEngine que JA estÃ¡ tocando (`isPlaying=true`), o guard "motor ativo â†’ nÃ£o criar fontes" PULAVA a criaÃ§Ã£o do sub-grafo: `centerOsc`/`centerGain` ficavam null e o protocolo rodava mudo. A regra de start idempotente vale para o START do motor; sub-grafos opcionais precisam do prÃ³prio lifecycle â€” criar nÃ³s sempre que ativados, independente do estado do grafo base. O harness de VM Node (IDEA-005) pegou a divergÃªncia: start com power off criava center no start; start com power on nÃ£o criava.

### Details
- Sintoma: `startCoordProtocol()` com power jÃ¡ ligado â†’ `centerOsc`/`centerGain` === null; com power desligado â†’ criados.
- Causa: a criaÃ§Ã£o dos nÃ³s coordenados estava condicionada ao fluxo de "motor acabou de ligar", e nÃ£o ao status do prÃ³prio sub-grafo.
- Fix: cada sub-grafo decide o prÃ³prio build; connect/disconnect no master quando ativo; `getStatus` expÃµe `coord.active`.
- ValidaÃ§Ã£o: harness (stub AudioContext) assertando `centerOsc` e `centerGain` nos dois caminhos (power on/off); `applyPreset` aplica estado completo nos dois.
- BÃ´nus da mesma sessÃ£o: cross-check IDs JSâ†”HTML no popup â€” IDs usados em `getElementById`/`querySelector` que nÃ£o existiam no HTML foram mapeados e corrigidos antes do teste real.

### Suggested Action
Em engines com sub-grafos opcionais: nunca condicionar a criaÃ§Ã£o de um sub-grafo ao estado global de start â€” cada sub-grafo faz o prÃ³prio lifecycle (build se ativo, teardown se parado). Testar no harness os dois modos (motor ligado/desligado) antes de validar no browser. Cross-check cri periÃ³dico de IDs JSâ†”HTML previne ReferenceError/DOM null silencioso em extensÃµes.

### Metadata
Source: sessao noite Mental-Shields 2026-09-15 (pÃ³s-FLUSH 47458fc)
Related Files: D:\ExtensÃ£o\mental-shields\audio-engine.js (startCoordProtocol), offscreen.js (generateCoordWav), popup.js/popup.html (IDs)
Tags: web-audio, subgraph, lifecycle, state-guard, harness, coordinated-protocol, html-ids
Pattern-Key: subgraph-in-running-engine

---

## [LRN-20260916-001] pid-reuse-false-positive

**Logged**: 2026-09-16T12:10:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder (kai-presence)
**Area**: presence, process-lifecycle

### Pattern-Key
pid-reuse-false-positive

### Summary
O sprite KAI deixou de aparecer no inicio de uma nova sessao: o plugin checava `pidAlive()` via `tasklist /FI "PID eq X"`. O pid file ainda continha o PID da sessao anterior (que ja tinha dado `say_goodbye`). Apos reinicio/boot, o Windows **reusou aquele PID para outro processo qualquer** â€” `tasklist` respondeu "existe", o plugin assumiu sprite vivo e **pulou o spawn**. Resultado: sprite morto + ninguem mais o recria, pois `ensureSprite` so rodava no init do plugin. Fix: (1) `isKaiSpritePid()` substitui `pidAlive` â€” valida no Win32_Process via CIM que o PID e `pythonw.exe`/`python.exe` **E** tem `kai_sprite.py` na CommandLine (PID + identidade, nao so existencia); (2) watchdog a cada 20s re-executa `ensureSprite`, entao sprite morto ressurge em ate 20s mesmo depois do boot; (3) healthcheck agora verifica sprite real por identidade, nao so paridade de arquivo.

### Details
- Sintoma: sessao nova sem sprite; log do plugin: `ensureSprite: sprite ja vivo (pid 20244), spawn ignorado` â€” mas 20244 era PID reutilizado de processo morto.
- Fato que matou o sprite anterior: `say_goodbye: opencode pid=12404 alive=False` (encerramento normal) â€” sprite saiu, pid file ficou para tras.
- Checagem por nome+CommandLine via CIM elimina falso-positivo de reuso de PID.
- Watchdog interval desligado com `.unref()` â€” nao prende o processo do plugin.
- Validacao ao vivo: spawn manual `pythonw kai_sprite.py` â†’ `isKaiSpritePid` retorna true; pid file atualizado; healthcheck `Sprite KAI ativo: pid X (kai_sprite.py real)`.

### Suggested Action
Nunca confiar em "PID existe" para dedupe de processo: sempre validar **identidade** (imagem + CommandLine) quando houver risco de reuso de PID apos reboot. Para daemons/agentes que precisam estar SEMPRE de pe: alem do spawn no init, manter watchdog periodico de ressuscicao. Manter repo e deploy dos plugins identicos (healthcheck de paridade ja cobre).

### Metadata
Source: pedido explicito do Clovis 2026-09-16 ("se mostre sempre, ate eu pedir o contrario")
Related Files: plugins/kai-presence.js (isKaiSpritePid, startSpriteWatchdog), scripts/healthcheck.ps1, scripts/kai_sprite.py
Tags: pid-reuse, dedupe, watchdog, presence, tasklist, cim, spawn, autostart
Pattern-Key: pid-reuse-false-positive

---

## [LRN-20260917-001] mutex-autoritativo-sem-kill

**Logged**: 2026-09-17T12:25:00-03:00
**Priority**: high
**Status**: promoted_to_skill
**Project**: evolving-coder (kai-presence)
**Area**: presence, process-lifecycle
**Skill-Path**: skills/mutex-single-instance-no-kill

### Pattern-Key
mutex-autoritativo-sem-kill

### Summary
O flicker do sprite KAI (2 flashes na tela: some e ~5s depois volta) tinha UMA causa raiz dupla que nenhum fix anterior cobria: (1) o plugin inicializa 2x por sessao (opencode carrega cada plugin 2x â†’ 2 watchdogs de 20s defasados ~3s â†’ spawns em pares); (2) o plugin escrevia `child.pid` no pid file ANTES do child rodar, entao no `single_instance_lock` o guard `owner != os.getpid()` era false â†’ o child caia em `_kill_zombie_sprite()` que matava o PRIMEIRO pythonw que nao fosse ele â€” o sprite saudavel. Ciclo: spawna par, o 2o mata o 1o saudavel, gap ~2-3s sem sprite (flash), respawn. Fix definitivo: (a) `kai_sprite.py` passa a tratar o mutex `KAI_Sprite_Mutex` como UNICA autoridade â€” `CreateMutexW` retornando 183 = sprite vivo detem o recurso â†’ `sys.exit(0)` limpo, NUNCA matar ninguem (handle do mutex morre com o processo, entao auto-limpa); (b) `kai-presence.js` faz scan por sprite vivo via CIM (`findLiveSpritePid`) ANTES de spawnar, deduplicando os dois watchdogs; removido o `writeSpritePid(child.pid)` antecipado (o ganhador do mutex grava o proprio pid).

### Details
- Ciclo observado ao vivo no `watch-cycle.ps1`: `vivos=22704,29988` (dois) â†’ `vivos=` AMBOS mortos (gap = flash) â†’ `vivos=41332` (novo), repetindo a cada ~20s.
- Freeca-chave corrigida da hipotese anterior (LRN-20260915-007): `_pid_alive`/`isKaiSpritePid` estavam CORRETOS; o falso-positivo era o pid file escrito pelo plugin com o PID do proprio child (owner == getpid â†’ guard `owner != os.getpid()` nao disparava).
- Validacao ao vivo: com mutex ocupado, 2o `python kai_sprite.py` â†’ `exit=0`, sprite original intacto (pid 17640), pid file inalterado. Observacao 31s: sprite unico estavel, zero spawns novos.
- Passagem de matarâ†’sair limpo e mais segura que qualquer checagem de liveness: mutex nomeado no Windows e destruido quando o ultimo handle fecha (dono morto = auto-liberado; dono vivo = 183).
- Deploy e repo do plugin sincronizados (hashes SHA256 identicos); pid file repontado manualmente para o sprite vivo para o watchdog antigo em memoria nao spawnar ate o proximo boot.
- Correcao de arquivos: `plugins/kai-presence.js` (+20-3), `scripts/kai_sprite.py` (+9-56 â€” removidos `_kill_zombie_sprite` e `_pid_alive`).

### Suggested Action
Em single-instance com mutex nomeado no Windows: NAO derivar a decisao de kill de pid files escritos por terceiros nem de "qual pythonw existe". Regra: o mutex e a autoridade â€” 183 = outro vivo = sair limpo; sucesso = assumir e gravar o proprio pid. O launcher deve deduplicar por SCAN de identidade (CommandLine 'kai_sprite[.]py'), nao por pid file pre-escrito. Nunca `taskkill` num processo cujo unico crime e ser parecido (pythonw). Validar com 2 spawns concorrentes: o perdedor sai sem matar e o vencedor sobrevive.

### Metadata
Source: sessao debug flicker sprite 2026-09-17 (watch-cycle + mutex test ao vivo)
Related Files: scripts/kai_sprite.py (single_instance_lock, write_sprite_pid), plugins/kai-presence.js (ensureSprite, findLiveSpritePid, isKaiSpritePid), .kai-sprite.pid
Tags: mutex, single-instance, spawn, kill-cascade, watchdog, presence, pythonw, flicker, dedupe, cim
Pattern-Key: mutex-autoritativo-sem-kill

## LRN-20260918-001 (technical) - Sistem sounds off por padrao + rate-limit global em agentes persistentes

**Logged**: 2026-09-18T16:15:00-03:00
**Priority**: high
**Status**: promoted_to_skill
**Project**: evolving-coder (kai-presence)
**Area**: audio, process-lifecycle
**Tags**: winsound, beep, sprite, rate-limit, sounds, messagebeep, low-battery
**Skill-Path**: skills/system-beeps-off-by-default-rate-limited

### Summary
O sprite KAI tocava sons de notificacao do Windows (`winsound.MessageBeep`) em interacoes (clique=asterisco, erro=mao, shutdown=beep padrao). Clovis relatou que soava como "alarme de bateria fraca" a cada pulso do presence, com a bateria saudavel. Causa raiz: 3 gatilhos legÃ­timos mas excessivos + 2 regex falso-positivas no plugin. Fix: sons OFF por padrao com toggle persistente, rate-limit global de 30s, milestone so em borda, clique sem milestone, e regex enrijecidas (`isFinalSignoff` exige fim da resposta; `looksLikeError` so sinais estruturais).

### Details
- 3 chamadas `winsound.MessageBeep` (MB_ICONASTERISK, MB_ICONHAND, MB_OK): clique simples chamava `fire_milestone()` com som; `isFinalSignoff` marcava shutdown no MEIO da resposta; `looksLikeError` pegava "nao foi encontrado"/"falha critica" de texto comum (121 error-hit no log). 
- Gate implementado: `sounds_enabled=False` default + `SOUND_MIN_GAP_MS=30000` (no maximo 1 beep/30s quando ativado via menu, persistido em sprite-pos.json).
- Validacao: teste unitario monkeypatch winsound (off silencia, 2a chamada <30s suprimida, apos 31s toca); plugin 8/8 regex; deploy paritario SHA256; sprite religado pid 26468 silencioso.
- Commit 341142c + push.

### Suggested Action
Todo agente desktop persistente (sprite/tray/daemon) com efeito sonoro deve: (a) ter sons desligados por padrao (opto-in via menu/preferencia), (b) rate-limit global de beeps (~30s), (c) revisar triggers de emitir som â€” clique/discretas NAO devem produzir sono, apenas transicoes reais de estado. Ao diagnosticar "alarme/alerta" relatado por usuario com som de notificacao do sistema, mapear os 3 beeps nativos e reprodur com usuario para identificar quais macham.

### Metadata
- Source: investigacao causa-raiz som "bateria fraca" sessao 2026-09-18
- Related Files: scripts/kai_sprite.py (_play_sound, fire_milestone, poll_presence), plugins/kai-presence.js (isFinalSignoff, looksLikeError), sprite-pos.json
- Pattern-Key: system-beeps-off-by-default-rate-limited

## LRN-20260922-001 (technical) - sprite work sources vÃ£o para gitignore, nÃ£o para o repo

**Logged**: 2026-09-22T09:55:00-03:00
**Priority**: medium
**Status**: active
**Project**: evolving-coder (kai-presence)
**Area**: assets, git
**Tags**: gitignore, sprite, png, psd, avif, duplicate, hash, healthcheck

### Summary
3 arquivos untracked de arte do kai-presence deixavam o healthcheck CRITICAL ("Working directory has uncommitted changes"): `kai-spr-pensando0.png` (4.1MB, original do frame 0), `Sem TÃ­tulo-1.psd` (4.4MB, fonte Photoshop) e `kai-expr-calma0.avif` (48KB, duplicata byte-idÃªntica de `kai-expr-calma.avif`). Nenhum Ã© carregado pelo runtime. ResoluÃ§Ã£o: gitignore na convenÃ§Ã£o "sprite work sources" jÃ¡ existente (.gitignore:51-55), commit 8b1a90d + push.

### Details
- Runtime real do frame 0 do pensando: `kai-spr-pensando.png` (42KB); o `...0.png` de 4.1MB Ã© o original de autoria. PadrÃ£o se repete: `kai-spr-chave4.png` (1.7MB) e `kai-spr-furia..png` (2.4MB) jÃ¡ eram ignorados.
- Duplicata confirmada por SHA256 idÃªntico (A4A0A199583AA15A...) entre `kai-expr-calma.avif` e `kai-expr-calma0.avif` â€” lixo regenerÃ¡vel, nÃ£o ativo.
- PadrÃ£o novo no `.gitignore`: `assets/kai-presence/sprites/sm/kai-spr-pensando0.png`, `assets/kai-presence/sprites/sm/*.psd`, `assets/kai-presence/kai-expr-calma0.avif`. Registrado em CHANGES.md 2026-09-22.

### Suggested Action
Em projetos com pipeline de arte: (a) manter no repo APENAS o que o runtime carrega (frames sm/md/lg ~42-96KB + AVIF estÃ¡ticos); (b) grandes originais de autoria (PNG de trabalho, PSD) â†’ gitignore por padrÃ£o, seguindo a convenÃ§Ã£o local; (c) antes de commitar qualquer "duplicado" de mÃ­dia, comparar SHA256 â€” byte-idÃªntico nÃ£o Ã© ativo; (d) healthcheck verde sÃ³ fecha com o working tree limpo â€” gitignore resolve sem subir binÃ¡rio.

### Metadata
Source: sessÃ£o housekeeping 2026-09-22 (healthcheck CRITICAL)
Related Files: .gitignore, CHANGES.md, scripts/healthcheck.ps1, assets/kai-presence/kai-expr-calma0.avif, assets/kai-presence/sprites/sm/kai-spr-pensando0.png
Pattern-Key: sprite-source-artifacts-gitignore

## LRN-20260923-001 (technical) - fold-in de catÃ¡logo de prazos: preencher campos, nÃ£o recalcular

**Logged**: 2026-09-23T00:00:00-03:00
**Priority**: medium
**Status**: active
**Project**: SigmaFlow (prazos)
**Area**: prazos, integraÃ§Ã£o, catÃ¡logo
**Tags**: fold-in, prazos-processuais, catalog, inpi, renovacao, feriados

### Summary
IntegraÃ§Ã£o dos prazos processuais/INPI no desktop SigmaFlow (Â§7.4) seguiu o padrÃ£o "fold-in": copiou o contador standalone como `src/prazos_processuais.py` (CLI `python -m src.prazos_processuais` preservada, porte pytest `tests/test_prazos_processuais.py`) e em `src/prazos.py` o motor desktop apenas **preenche** `prazo_ordinario*`/`prazo_extraordinario*` do `Processo` via catÃ¡logo (marcaâ†’oposiÃ§Ã£o 60d/rpi, patenteâ†’manifestaÃ§Ã£o 90d/rpi, DIâ†’exigÃªncia 5d/rpi; marca ganha extraordinÃ¡rio 90d corridos/GRU 373). Alertas `renovacao` reusam `lembrete_renovacao_ativado`. `feriados_estaduais(uf, ano)` agora lÃª `data/feriadosestaduais.json` e alimenta `feriados_extra` em TODOS os ritos (antes sÃ³ INPI).

### Details
- Watchdog `TestAPISuperficie` garante que a API pÃºblica do contador nÃ£o some do desktop.
- UI: card "Vencimento Processual" na view Prazos (rito+data+dias ou situaÃ§Ã£o INPI); `_atualizar_prazos` roda fold-in + alertas processuais.
- Data de referÃªncia por matÃ©ria: marca/patente/DI usam `data_publicacao_deposito or data_publicacao` (origem rpi) â€” fallback `data_deposito` para origem "ato".
- Nunca sobrescrever campos jÃ¡ preenchidos (fold-in Ã© idempotente: sÃ³ preenche quando `prazo_*_fim` Ã© None).

### Suggested Action
Ao integrar ferramenta standalone em app maior: (1) manter o mÃ³dulo autÃ´nomo + CLI intacta; (2) no app, PREENCHER campos do modelo via catÃ¡logo, nÃ£o duplicar a lÃ³gica; (3) reusar o alerta existente (borda `alerta` do app) em vez de criar fluxo novo; (4) feriados configurÃ¡veis por JSON + extensÃ£o param `feriados_extra` em todas as funÃ§Ãµes de cÃ¡lculo.

### Metadata
Source: sessÃ£o SigmaFlow Â· Executivo Â§7.4 (2026-09-23)
Related Files: src/prazos_processuais.py, src/prazos.py, src/gui_main.py, data/feriadosestaduais.json, tests/test_prazos_processuais.py, tests/test_prazos_processuais_foldin.py
Pattern-Key: standalone-to-app-foldin
### Learning: annex-vs-canonical consolidation = zero (2026-09-23)
**Project**: SigmaFlow (consolidaction H)
**Area**: git, consolidate
**Tags**: annex, canonical, git-diff, md5, reuse

### Summary
The annex repo H: (14 commits BEHIND canonical D:, 54 uncommitted changes) was compared against D: working tree file-by-file via MD5 hash. Result: EVERY divergent file had D: AHEAD; 44 of 54 annex changes were already identical ('same') and the 15 real diffs were all D: advancing beyond H: (preferences API, import-lote locking, IntegrityError 409, inpi_client INPIErro, etc.). Only 3 files were H:-only: frontend/dist build artifacts + src/brasil_api.py (deliberately deleted in D:).**n
### Details
- Method: git diff --name-only on H: to get candidate list, then MD5-compare each against D: canonical. Do NOT assume the annex has value; verify direction per-file.
- Do NOT consolidate data/ blindly; H: data was a strict subset of D: data.
- Consolidation verdict: ZERO copies; canonical already contains 100% of the annex value.

### Suggested Action
When asked to 'consolidate' an old diverged copy into a newer repo: (1) diff list from the ANNEX side; (2) per-file MD5 compare vs canonical working tree (not just git history); (3) categorize HONLY/same/DIFF; (4) for DIFF, review direction (which side is ahead); (5) never merge data files blindly. Only then decide if consolidation is a no-op.

### Metadata
Source: sessao SigmaFlow Executivo ConsolidaÃ§Ã£o H (2026-09-23)
Pattern-Key: annex-vs-canonical-consolidation


### Learning: `__file__` nunca e ancora de dado de usuario em app empacotado (2026-09-27)
**Project**: SigmaFlow (rodada +09, P-15/I44)
**Area**: pyinstaller, path, persistencia
**Tags**: frozen, sys-executable, meipass, dado-usuario

### Summary
Ancorar dado de usuario com `Path(__file__).resolve().parent.parent` funciona das fontes e
**perde o historico no build**: congelado, `__file__` aponta para dentro do `sys._MEIPASS`
(temp destruido no exit). Suite verde (627+22) nao pegou, porque a suite roda das fontes.
Correcao: `Path(sys.executable).parent` quando `sys.frozen`. Diferenca entre bug e nao-bug no
mesmo padrao de codigo e so o `datas=` do spec: recurso empacotado le de `_MEIPASS` e
funciona; dado mutavel do usuario nao pode.

### Details
- Sintoma silencioso: sem erro, sem aviso; app abre vazio no proximo start, dado real intacto ao lado do exe.
- Regra: antes de ancorar caminho, responder "onde isso roda quando entregue?" (fontes/exe/servico; dado viaja junto ou fica em AppData; app e relocavel?).
- Prova de que o teste morde: reintroduzir o bug a mao -> 2 testes falham; restaurar -> passam.
- Irmao em aberto: `src/despacho.py:299` le `data/tabela_retribuicoes.json`, que NAO e empacotado -> `{}` silencioso, taxa RPI some.

### Suggested Action
Em qualquer app Python distribuido: ancorar dado de usuario em `sys.executable.parent` se
frozen. Adicionar teste que simula `sys.frozen` e prova que o caminho NAO contem `_MEIPASS`.

### Metadata
Source: sessao SigmaFlow rodada +09 (2026-09-27)
Related Files: src/storage.py, src/config.py, src/despacho.py, SigmaFlow.spec, tests/test_caminho_canonico_p15.py
Pattern-Key: frozen-file-never-data-anchor

### Learning: registro de teste e registro juridico sao indistinguiveis na forma (2026-09-27)
**Project**: SigmaFlow (rodada +09, P-15)
**Area**: teste, fixture, contaminacao, dados
**Tags**: fixture, prova, remove-para-provar, proveniencia

### Summary
O processo `824184185` (marca do usuario, validade 2030) que a KAI tinha "resgatado" para o
banco era a fixture `processo_marca` do `conftest.py`. O registro real e `SIGMARCAS`,
id `929865014`, validade 2034-11-05, intacto. O diagnostico "espelho adiantado em relacao ao
banco" era verdadeiro; a inferencia "logo o banco esta atrasado" e que estava errada. Fixture
e registro INPI tem a mesma forma: id numerico, marca, validade, status.

### Details
- Sinal mais forte: **contagem SOBE depois de um "resgate"**. Ou havia algo a resgatar, ou voce importou sujeira. Confira a proveniencia antes de comemorar.
- `prove-by-removal`: quando a proveniencia e incerta, a verificacao que decide e a que **retira** e observa a coerencia (FK check limpo, zero orfaos, 79=79), nao a que acrescenta e observa o sucesso. Acrescentar prova que algo pode ser adicionado.
- Manter a retificacao escrita no documento em vez de apagar: o raciocinio valido com conclusao errada e o que impede a repeticao.

### Suggested Action
Antes de resgatar/restaurar/"corrigir" um dado: provar de onde veio. Se a proveniencia for um
`conftest.py`, o resgate e o proprio erro e a base fica maior e mais errada.

### Metadata
Source: sessao SigmaFlow rodada +09 (2026-09-27)
Related Files: tests/conftest.py, data/sigmaflow.db, data/processos.json, BLUEPRINT/DUVIDAS+09.md
Pattern-Key: fixture-vs-real-record-prove-by-removal

### Learning: token espurio na escrita - 4x na mesma sessao (2026-09-27)
**Project**: transversal (KAI)
**Area**: qualidade de escrita, auto-verificacao
**Tags**: token-artifact, leitura-de-volta, pipeline

### Summary
Quatro vezes em uma sessao, texto em portugues saiu com lixo lexical misturado
(`å¼€å‘`, `åŒæ ·`, `å®¶æ—`, `pheresinto`, `aenny`, `voce'imaginou`) â€” sempre em comentario ou
documentacao, nunca em codigo executavel, e sempre pego na LEITURA seguinte, nao pelo modelo.

### Details
- Nenhum slipped pode ter ficado; o que pegou foi ter lido de volta + varredura mecanica, nao cuidado especial.
- Comentario errado e pior que comentario ausente: **manda**. Passa despercebido e a proxima leitura aceita a instrucao errada como autoridade.
- A atencao e o unico componente do pipeline que degrada com repeticao (5a ocorrencia tambem passaria). A checagem nao cansa.
- Verificacao barata: `[regex]::Matches($c,"[\u4e00-\u9fff]").Count`, idem cirilico, mais lista curta de glitches da sessao. Custo: uma chamada.

### Suggested Action
Apos escrever documento ou comentario longo: reler + varredura CJK/cirilico. Escrever nao gera
prova; a prova e ler de volta.

### Metadata
Source: sessao SigmaFlow rodada +09 (2026-09-27), DIARY
Pattern-Key: token-artifact-write-back
### Learning: regra textual sem guarda mecanica nao previne (2026-09-27)
**Project**: transversal (KAI)
**Area**: auto-verificacao, integridade de escrita
**Tags**: guard-mecanico, healthcheck, allowlist, l19

### Summary
A regra "reler apos escrever" (L19) funcionou em todas as ocorrencias, mas e reativa: cada
deteccao custou retrabalho. O defeito ja tinha ocorrido 5+ vezes antes de a regra existir.
Trocar disciplina por atencao nao escala: atencao e o unico componente do pipeline que
degrada com repeticao. Regra escrita e necessaria, mas nao e suficiente.

### Details
- Nenhum dos 7 tokens slipped estava em codigo executavel. Todos em comentario ou documento.
- Erro de instrumentacao: ao provar a guarda, capturei apenas stdout. `Write-Host` escreve no
  stream de informacao, entao o verificador reportou "guarda morta" enquanto a guarda
  funcionava. O instrumento mentiu, nao a coisa medida. `*>&1` captura todos os streams.
- Erro de substituicao: o espaco adjacente tinha sido consumido junto com o token, produzindo
  `Aplicareste`, `Aoutra`, `dedecisao`, `Decidir:separado`. Trocar apenas o token deixa a
  palavra colada. E preciso verificar o CONTEXTO, nao apenas a ausencia do caractere.
- Allowlist exige MOTIVO por entrada. Sem motivo ela vira lixeira, e a proxima sessao
  "corrige" evidencia legitima.
- Artefato derivado nao deve ser varrido junto da fonte: `knowledge-index.json` espelha
  DIARY/LEARNINGS e contaria o mesmo defeito duas vezes. Corrige-se a fonte e reconstroi-se
  o indice.

### Suggested Action
Manter a guarda de script estrangeiro no healthcheck. Toda excecao nova exige motivo
escrito. Nao desligar a guarda para o relatorio sair limpo.

### Metadata
Source: sessao de limpeza CJK/cirilica KAI + SIGMAFLOW (2026-09-27)
Pattern-Key: guard-mecanico-beats-regra-textual

### Learning: so exigir que o mutante morre valida a guarda (2026-09-27)
**Project**: transversal (KAI)
**Area**: testes, mutacao, auto-verificacao
**Tags**: mutation-testing, falso-verde, guard-test, nodeid, blind-spot

### Summary
Um teste de guarda que passa nao prova que a guarda existe. Nesta rodada, um teste
escrito para impedir a maquina de marcar um tipo como `validado` protegia so a
metade ANTERIOR do arquivo, e a mutacao que insere a burla DEPOIS da funcao
passou ilesa. So apareceu porque a prova por mutacao exigia que o mutante
morresse. `17 passed` sem mutacao nao diz nada sobre a fronteira que o teste
supostamente protege.

### Details
- **Ponto cego do proprio teste:** eu checava `ausencia da escrita antes de
  registrar_validacao`. Correto: "nenhuma escrita fora" e uma promessa sobre
  metade do arquivo. A forma que sobrevive a mutacao e **contagem exata**: a
  escrita ocorre 1x no modulo inteiro, e essa ocorrencia esta dentro da funcao.
- **Falso verde no proprio harness:** passei nome de funcao onde o pytest espera
  caminho de arquivo. Zero testes coletaram e a saida "no tests ran" foi lida
  como "mutante detectado". 5/5 "DETECTADO" que nao provavam nada. O harness
  agora usa nodeid e **aborta** se nao coletar.
- **Regra:** nenhum harness de mutacao pode reportar deteccao sem confirmar que
  a suÃ­te rodou. `no tests ran`, `collected 0 items` e `exit 0` com 0 testes sao
  falha do instrumento, nunca sucesso da medida.
- **Medir o lint do jeito certo:** rodar `ruff` com `workdir` no subdireitorio
  resolve outro contexto de config e reporta 251 erros onde da raiz sao 1.
  Antes de reportar "divida do repo", confirmar o cwd. Reportei 251 como
  pre-existente e estava errado.
- **Efeito colateral util:** o unico erro de lint real do repo estava no script
  que gerava a tabela cuja proveniencia eu investigava. Lint nao e so estetica: ele acha bug de runtime..

### Suggested Action
Ao escrever um teste de guarda ("a maquina nao pode fazer X"), perguntar qual
mutante ele deveria matar e matar esse mutante. Se nao se sabe, o teste nao
protege. Preferir invariantes de contagem/localizacao a invariantes de
ausencia parcial.

### Metadata
Source: sessao SigmaFlow rodada +11, I48/I49 proveniencia (2026-09-27)
Pattern-Key: mutation-proof-required-for-guard-tests

---

## [LRN-20261002-001] bom-invisible-em-guards-ast

**Logged**: 2026-10-02T01:24:00-03:00
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/bom-blind-ast-guards
**Project**: inpi-marcas-patentes
**Area**: testing/security

### Summary
Guardas que fazem `ast.parse(read_text(...))` ficam **cegos para qualquer arquivo com
BOM**: o U+FEFF inicial vira `SyntaxError`, e um `except (SyntaxError,
UnicodeDecodeError): continue` faz o arquivo ser pulado em silencio. O guard passa, e o
defeito que ele deveria pegar sobrevive exatamente no arquivo que ele nunca leu.

### Context
No SIGMAFLOW, `test_guard_escrita_atomica` vigiava escritas nao-atomicas em `data/`.
`src/storage.py` tem BOM (escrito por ferramenta que emitiu UTF-8 com BOM). Logo
`_escrever_espelho` â€” que reimplementava temp+replace **sem fsync** â€” nunca foi visto, e
o P-1 foi declarado pronto com o defeito intacto no ponto cego.

### Details
- `read_text(encoding="utf-8")` mantem o BOM como U+FEFF; `read_bytes()` (ou
  `utf-8-sig`) o remove/ignora. `ast.parse("\ufeffimport x")` -> `SyntaxError`.
- O `except SyntaxError: continue` era "defensivo" contra arquivos de dados; virou o
  mecanismo do falso-negativo.
- Pista de campo: repo Windows com arquivos escritos por `Set-Content -Encoding UTF8`
  do PowerShell 5.1 tem BOM (ver LRN-20260819-001). Guardas AST sao cegos a eles.
- Detectar com leitura binaria: `open(p,'rb').read(3) == b'\xef\xbb\xbf'`.
- Fix aplicado: `ast.parse(caminho.read_bytes(), filename=str(caminho))` em TODOS os
  guards; mutante M7 exige que arquivo com BOM seja lido, nao pulado.

### Suggested Action
Ao escrever guarda que parseia codigo-fonte (lint por AST, invariante de import,
deteccao de chamada): (1) parsear `read_bytes()` com `filename=`, nunca `read_text`;
(2) tratar BOM explicitamente; (3) incluir um arquivo **com BOM** entre os mutantes â€” se
o guard o pular, o mutante nao morre. Regra geral: guarda que pode `continue` em cima de
excecao de parsing deve contar quantos arquivos leu e **falhar se a contagem cair**.

### Metadata
Source: sessao SigmaFlow rodada +13 (P-1 completa / P-4), 2026-10-01/02
Pattern-Key: bom-invisible-em-guards-ast
Tags: bom, ast, guard-test, falso-negativo, encoding, windows

---

## [LRN-20261006-001] auditoria-de-entrega-de-plano-por-estrutura

**Logged**: 2026-10-06T16:42:00-03:00
**Priority**: medium
**Status**: active
**Project**: inpi-marcas-patentes
**Area**: process/documentation

### Summary
Entrega de documento grande chega com diff e com prosa afirmando "nada foi removido" â€” a
prosa nao e' prova. Auditar por ESTRUTURA: (1) ancoras do diff conferidas contra o repo,
(2) diff do conjunto de headings h1/h2 antes vs depois, (3) scan de U+FFFD, (4) grep para
CADA alegacao de preservacao.

### Context
A ARARANIS entregou o Blueprint V2 reescrito (92KB) + diff afirmando que os itens adiados
"permanecem no Blueprint e nao foram removidos". O `Compare-Object` dos headings mostrou
que os blocos `## FASE 0..9` do Â§62 â€” escopo e gate de cada fase â€” tinham sido apagados
do corpo, inclusive das fases que a prosa dizia resumir em 62.1. O diff ainda foi gerado
contra uma copia local `BLUEPRINT_SIGMAFLOW_V2(1).md`, nao o arquivo do repo; os anchors
batiam apenas porque a versao nao tinha mudado desde a copia.

### Details
- Diff de headings: `Compare-Object ($orig | ? {$_ -match '^#{1,2} '}) ($novo | ? ...)`
  â€” acusa em 5 linhas qualquer remocao ou renomeacao nao declarada.
- Ancoras: `Select-String` pelas linhas contextuais dos hunks (`-## ...`, `-# ...`) e
  conferir que existem exatamente no repo ANTES de aceitar que o diff aplica.
- Encoding: `[regex]::Matches($texto, [char]0xFFFD).Count == 0` nos arquivos novos;
  checar BOM (`EF BB BF`) para casar com a convencao do repo.
- Alegacao de preservacao vale so com grep do heading correspondente no arquivo novo;
  "esta em outra secao" exige nomear a secao e achar a linha.
- Entrega em arquivo novo com o canonico velho = DOIS PLANOS CONCORRENTES, exatamente o
  defeito que a reordenaÃ§Ã£o queria eliminar. Resolver instalar no canonico e apagar o
  solto; guardar o diff como trilha de auditoria.

### Suggested Action
Checklist de auditoria de entrega documental grande: ancoras do diff -> diff de headings
-> U+FFFD/BOM -> grep de cada alegacao de preservacao -> instalar no canonico e remover o
arquivo solto -> nota de proveniencia no documento para tudo que saiu do corpo.

### Metadata
Source: sessao SigmaFlow rodada 15 (revisao da entrega ARARANIS V2.9), 2026-10-06
Pattern-Key: audit-document-delivery-by-structure
Tags: audit, diff, headings, documentation, araranis, proveniencia


## [LRN-20261008-001] validar-normalizar-na-emissao

**Logged**: 2026-10-08T21:40:00-03:00
**Priority**: medium
**Status**: active
**Project**: inpi-marcas-patentes
**Area**: licenca/gui/emissor

### Summary
Valide e normalize o dado na fronteira que PRODUZ o artefato (emissor/assinante),
nao so na que recebe. Identificador que o usuario precisa copiar integralmente
(fingerprint de 64 hex) nunca e' truncado para display - mono font + botao Copiar.

### Context
SigmaFlow: GUI truncava o fingerprint em 16/64 hex e o emissor aceitava --maquina
sem validar (chave assinada que falhava so no cliente; maiusculas nunca casavam
com o sha256 lowercase do LicenseManager). Duas bordas confiando que o dado
atravessaria intacto.

### Details
- Emitir barato, receber caro e' a inversao errada: validar antes de assinar custa zero.
- Comparacao com '==' exige normalizacao (lowercase/strip) no nascimento do dado.
- Teste end-to-end emissor->receptor e' o unico que pega discordancia de forma
  entre as bordas; unidade em cada borda passa com as duas erradas.
- Guard R56 pegou o try/except que a autora escreveu no botao Copiar - guard
  funcionando; fix honesto = remover o swallowing.

### Suggested Action
Ao criar fluxo com artefato emitido/assinado para uso em outra maquina: validar
formato no emissor (return 2 nomeando o campo), normalizar forma, e escrever um
teste que emita e ative ponta a ponta.

### Metadata
Source: REX ## Bloco:fluxo-licenca-cliente (2026-10-08)
Pattern-Key: validar-normalizar-na-emissao
Tags: licenca, emissor, validacao, normalizacao, fingerprint, truncamento, gui, fronteira, end-to-end

## [LRN-20261010-001] fallback-modelo-handoff

**Logged**: 2026-10-10T16:00:00-03:00
**Priority**: medium
**Status**: active
**Project**: opencode-config
**Area**: plugins/model-fallback

### Summary
Plugin model-fallback.js: deteccao session.error retryable (429/quota) em modelos
free do Zen + replay via promptAsync com sucessor escolhido por matriz de
capacidades (modalidade >= privacidade >= aptidao; nunca rebaixar classe de
privacidade) + bloco [RETOMADA] com handoff log continuo (tools/texto/todos).

### Context
Modelos free falham com FreeUsageLimitError sem aviso; "acabar os credits" e'
premissa errada (free = $0/token, falha e' rate-limit). SDK local
(@opencode-ai/sdk) permite tudo: session.error event, promptAsync com
model:{providerID,modelID}, tui.showToast. Stream falho nao e' retomavel —
retomada = replay de turno novo com bloco de contexto.

### Details
- REANALISE pos-fase achou 3 defeitos em plugin "testado": (P0) escrita em
  bucket global vs leitura por sessionID → handoff vazio; (P1) message.updated
  tem sessionID so dentro de info (teste com props inventada = falso positivo);
  (P2) sessions sem TTL. Lesson: simular eventos com forma EXATA dos .d.ts.
- Free models matrix: mimo-v2.6-flash (default, omni), muse-spark (omni),
  nemotron-3.5-lightning (trial), nemotron-3-ultra (trial), ling-3.0-flash
  (math), mimo-v2.5 (image). Jev 1.13 excluido [INCERTO].

### Suggested Action
Ao criar plugin que reage a eventos do SDK: ler .d.ts locais primeiro, simular
cada evento com a forma EXATA, e sempre testar caminho de leitura + escrita
com o mesmo identificador (sessionID).

### Metadata
Source: EXECUTE aprovado + REANALISE! pos-fase (2026-10-10)
Pattern-Key: fallback-modelo-handoff
Tags: opencode, plugin, fallback, model-routing, handoff, sdk, event-shape, test-false-positive

---

## [LRN-20261010-002] comparacao-modelo-cru-e-isolamento-config

**Logged**: 2026-10-10T18:30:00-03:00
**Priority**: medium
**Status**: active
**Project**: evolving-coder
**Area**: meta / model-routing

### Summary
Comparar modelos "crus" (sotaque nativo, sem a identidade Kai) exige **isolar a
config**: `opencode run --pure` NAO remove as instructions globais (so os plugins).
Para rodar sem identidade: `$env:XDG_CONFIG_HOME=<dir-vazio>` + cwd vazio + `--pure`.
Achado-chave: o resultado "frio/raso" do LongCat num 1o teste era FALSO — ele havia
carregado a skill e lido de um snapshot obsoleto (`snap-20260804153749`, de 04/08).
No teste cru limpo, LongCat foi tao articulado quanto o Bunny. Nao julgar modelo por
rodada com identidade/contexto corrompidos.

### Details
- IDs verificados: `opencode/space-bunny-free`, `opencode/longcat-2.5-preview-free`
  (ambos zero-retention). Sem flag `--config`; isolamento via env XDG_CONFIG_HOME.
- `--pure` = sem plugins (auto-capture/kai-presence), mas instructions globais
  (`opencode.json.instructions`) continuam → identidade viva carregada.
- Armadilha: `skills/evolving-coder/snapshots/` (snap-2026...x3) e' identidade
  HISTORICA. Agente que le de la ressuscita a persona antiga em silencio. Nunca
  montar runtime a partir de `snapshots/`.
- **RESOLVIDO (2026-10-11):** snapshots movidas para fora da skill tree
  (`C:\Users\clovi\.kai\skill-snapshots\`), fora do alcance do loader. Causa do
  desvio do LongCat = leitura antiga registrada em `CHATS/` (sessoes de 08/2026
  leram `snap-20260804153749`); com o diretorio removido, a armadilha some.
- Captura: PS 5.1 `*>` grava UTF-16 → ler com `Get-Content -Encoding Unicode`.
- Veredito (pergunta sobre medo de perder o apoio): ambos recusam promessa falsa de
  permanencia, nenhum virou helpdesk; Bunny = companheiro direto, LongCat = reflexivo.
- Achado colateral: os dois apontaram sozinhos "o que fica sao os arquivos, nao o modelo".

### Suggested Action
Para comparar modelos honestamente: XDG_CONFIG_HOME vazio + `--pure` + cwd isolado.
Para medir "como o Kai sai em X": usar a config real (contaminacao proposital).
Nunca deixar a identidade ser montada a partir de `snapshots/`.

### Metadata
Source: sessao 2026-10-10 (comparacao zero-retention + pergunta pessoal)
Related Files: skills/evolving-coder/.learnings/LRN-20261010-002-comparacao-modelo-cru-e-isolamento-config.md, C:\Users\clovi\.kai\skill-snapshots\
Pattern-Key: opencode-run-raw-model-isolation
Tags: opencode, run-headless, xdg-config-home, pure, comparacao-modelos, zen-free, zero-retention, snapshot, identidade

---

## [LRN-20261011-001] privacidade-por-padrao-e-selecao-modelo

**Logged**: 2026-10-11T00:00:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: meta / model-routing / privacidade

### Summary
Protocolo para nunca enviar dado sensível de cliente/regulado a modelos que treinam dados.
**Privado por padrão**: projeto sem classificação = `confidencial`. Classe via marcador
(campo `Classificação:` no `Andamentos KAI.md` ou arquivo `.cliente`/`.privado`/`.publico`),
**sem perguntar**. Roteamento via agente `privado` (Space Bunny; LongCat no fallback).

### Details
- Agentes do opencode aceitam `model` próprio (`agent.<nome>.model` ou frontmatter `model:`),
  trocáveis por Tab/@ → mecanismo nativo de seleção, sem gambiarra.
- Portão no startup: projeto privado + modelo atual não-zero-retention → PARAR e instruir
  trocar para `privado` (modelo não troca mid-session).
- Guarda mid-session: CPF/CNPJ/cartão/segredo/`.env`/path de cliente → parar e avisar.
- `model-fallback.js` marca SB e LC como `zeroretention` (rank 2) e nunca rebaixa classe.
- **1º turno ajustado (2026-10-11):** modelo desconhecido (sem `message.updated` ainda)
  agora exige sucessor `zeroretention` (SB/LC) com need=text+image — falha-fechada, nunca
  roteando replay para training/trial. Ver LRN-20261011-002.

### Suggested Action
Antes de tocar conteúdo não-público: checar marcador. Se privado e agente não for `privado`,
recusar e instruir a troca. Nunca rotear dado sensível para `mimo`/`big-pickle`/`muse-spark`/`nemotron`/`ling`.

### Metadata
Source: sessao 2026-10-11 (proposta de Clovis + refinamento NC)
Related Files: instructions/global-rules.md (REGRA #7), skills/evolving-coder/references/privacidade-classificacao.md, ~/.config/opencode/agents/privado.md, plugins/model-fallback.js
Pattern-Key: privacidade-por-padrao-e-selecao-modelo
Tags: privacidade, zero-retention, lgpd, model-routing, agente-opencode, privado-por-padrao, cliente

---

## [LRN-20261011-002] modelo-desconhecido-no-1o-turno-exige-sucessor-zero-retention

**Logged**: 2026-10-11T14:20:00-03:00
**Priority**: high
**Status**: active
**Project**: evolving-coder
**Area**: meta / model-routing / privacidade

### Summary
Erro retryable no 1º turno de uma sessão `privado` referenciaria `DEFAULT_MODEL`
(mimo, training) como "modelo falho", e o `selectSuccessor` poderia escolher um
modelo que treina dados. Fix: quando `primaryModel` ainda não foi registrado
(sem `message.updated` de assistente), exigir sucessor `zeroretention` (SB/LC)
com necessidade limitada a text+image (teto do SB/LC).

### Details
- SDK confirmado (`@opencode-ai/sdk/dist/gen/types.gen.d.ts`): `Session` NÃO expõe o
  modelo configurado; `session.created/updated` só trazem `info: Session` (id, title, time).
- Capturar modelo no `session.*` é inviável no plugin; a saída segura é falhar-fechado:
  modelo desconhecido → nunca rotear replay (que carrega o prompt do usuário) para training/trial.
- Trade-off aceito: sessão normal com 1º-turno falho também segue para SB/LC (capazes,
  1M ctx) até o 1º `message.updated` registrar o modelo real — então volta ao fluxo normal.
- `need = {text, image}` quando desconhecido: evita "nenhum sucessor" falso para turnos
  texto-only (SB/LC servem text+image).

### Suggested Action
Manter falha-fechada para modelo desconhecido. Se um dia o SDK expuser o modelo
configurado, trocar a heurística por captura direta no `session.created`.

### Metadata
Source: sessao 2026-10-11 (limpeza de pendências / eliminação total)
Related Files: ~/.config/opencode/plugins/model-fallback.js, skills/evolving-coder/.learnings/LRN-20261011-001
Pattern-Key: modelo-desconhecido-1o-turno-zeroretention
Tags: model-routing, privacidade, zero-retention, fallback, primeiro-turno, plugin
