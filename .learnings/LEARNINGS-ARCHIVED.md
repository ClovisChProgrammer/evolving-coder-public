# LEARNINGS-ARCHIVED.md

> Entries com Status: resolved. Movidas para arquivo em 2026-08-26.
> Conhecimento consolidado. Referenciar via kai-retrieval.py ou buscar por Pattern-Key.

| Metrica | Valor |
|---------|-------|
| Total de entries arquivadas | 34 |
| Ultimo arquivamento | 2026-09-22 |

---

## [LRN-20260917-002] config

**Logged**: 2026-09-17T22:40:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: emerging-coder
**Area**: config
**Tags**: sprite, frames, dedupe, animacao, apply_size

### Summary
Frames de animacao do sprite KAI colapsam se tiverem mesmo SHA-1: o dedupe (apply_size/kai_sprite.py) mantem so o primeiro; com 1 frame o loop morre. Ao regenerar frames, verificar por ESTADO e TAMANHO que ha >=2 hashes distintos (ex.: sm 2/4, md 3/4). Frameworks como mouth() com max(0,sin) produzem so 2 unicos por natureza (frames 1/3/4 iguais).

### Details
- Detectado quando Clovis viu CALMA/LENDO/FURIA "sem animar": eu havia regera os 7 estados em staticos-invisiveis (copias da base + pixel de canto alpha=0) - loop de 250ms rodava mas exibia imagem identica.
- Restaurado via git restore dos frames commitados + gerador original. Artefato encontrado: sm/sorriso do commit original tinha 4 arquivos bytes-identicos (1/4) - corrigido regerando so o frame 2 via import generate_anim_frames as g; g.mouth(base, i-1, 4).
- O gerador original e deterministico: regenerar md/lg nao mexe em nada (bytes iguais ao HEAD); so o arquivo sm\kai-spr-sorriso-2.png mudou.

### Suggested Action
Antes de versionar/entregar frames regerados, rodar checagem Get-FileHash por estado x tamanho: todo estado precisa >=2 distintos. Jamais substituir frames originais animados por copias estaticas sem confirmar com Clovis que e desejo dele.

### Metadata
- Source: sessao 2026-09-17 debug "por que nao animam?"
- Related Files: scripts/generate_anim_frames.py, scripts/kai_sprite.py, assets/kai-presence/sprites/
- Pattern-Key: frame-dedupe-collapse

---

## [LRN-20260917-003] user_preference

**Logged**: 2026-09-17T22:40:30-03:00
**Priority**: high
**Status**: resolved
**Project**: emerging-coder
**Area**: user_preference
**Tags**: sprite, travar, animacao, kai_sprite

### Summary
Quando o Clovis diz "Travar posicao", o sprite fixa a posicao da janela (sem wander/arrasto), mas as animacoes (bob, tremer de erro, troca de frames a 4fps) devem CONTINUAR. Nunca congelar tick_motion/anim_frames sob o flag locked.

### Details
- Durante o plano da req 3 eu gatei dy_bob/shake com self.locked; Clovis corrigiu: "embora eu utilize o comando 'Travar posicao', isso nao significa que voce deva parar com as animacoes".
- Revertido para HEAD: dy_bob = bob_offset(now_ms) incondicional + if now_ms < self.shake_until: sem gate. locked so afeta wander/drag.

### Suggested Action
Manter o toggle "Travar" como exclusivo de posicionamento. Se no futuro for desejado congelar tudo (estatico total), criar opcao separada explicita.

### Metadata
- Source: correcao explicita do Clovis na sessao 2026-09-17
- Related Files: scripts/kai_sprite.py (tick_motion)
- Pattern-Key: user-locked-does-not-freeze-animations

---

## [LRN-20260826-004] config

**Logged**: 2026-08-26T10:30:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
AGENTS.md condensado de 23.6KB para 8KB (42% reducao) movendo 13 protocolos para references/ sob demanda. Economia de ~36K tokens por chamada de API. Plugin so injeta SKILL.md (10.9KB). Protocolos movidos: PAI, Cambio Fechado, CHATS, Session Shutdown, >SD, Feedback Longas, RESOLVA!, SkillWatch, Snapshot, AVALIACAO SPA, V3RA, REANALISE!, Pipeline Extracao.

### Details
- Classificacao: CORE (manter, sempre necessario) vs REFERENCIA (sob demanda, quando gatilho dispara)
- SKILL.md atualizado com tabela "Quando ler referencias" (14 gatilhos mapeados)
- Risco identificado: modelo pode nao ler references/ sob demanda → teste necessario apos implementacao
- Fallback: regras criticas (PAI, Cambio Fechado, >SD, RESOLVA!) poderiam voltar ao AGENTS.md se modelo nao carregar

### Suggested Action
Testar na proxima sessao se modelo executa AVALIACAO no shutdown (gatilho = despedida), V3RA quando ativado, >SD quando digitado. Se falhar, reverter as regras criticas para inline.

### Metadata
Source: REANALISE! sobre gargalos 2026-08-26
Related Files: AGENTS.md, SKILL.md, references/
Tags: optimization, context-reduction, token-saving, performance
Pattern-Key: context-budget-management

---

## [LRN-20260826-001] integration

**Logged**: 2026-08-26T12:00:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: integration

### Summary
Kai pode controlar Blender via scripts Python (bpy) executados em modo headless (`blender --background --python`). Três níveis de integração identificados: (1) scripts CLI direto (viável agora), (2) blender-mcp server para tools MCP nativas (médio esforço), (3) loop autônomo com render+visão computacional (avançado). Idea capturada como IDEA-002 no IDEA_BANK.md.

### Details
- bpy (Blender Python API) expõe 100% da funcionalidade: meshes, modifiers, materials, lighting, camera, animation, rendering, export (GLB/OBJ/FBX/STL)
- Pipeline iterativo: escrever script → executar via CLI → renderizar preview → analisar → ajustar
- Limitação principal: sem viewport visual em tempo real — feedback depende de renders
- blender-mcp (projeto existente) pode integrar Blender como MCP server para tools nativas
- Loop avançado: renderizar cada iteração, analisar via visão computacional (Gemini Vision), ajustar automaticamente

### Suggested Action
Para validar: verificar se Blender está instalado no sistema, testar `blender --background --python` com script simples. Se viável, considerar blender-mcp para integração mais fluida.

### Metadata
Source: conversa com Clóvis 2026-08-26
Related Files: IDEA_BANK.md (IDEA-002)
Tags: blender, bpy, 3d-modeling, mcp, headless, pipeline
Pattern-Key: blender-bpy-headless-control

---

## [LRN-20260822-002] graphics

**Logged**: 2026-08-22T03:20:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: graphics

### Summary
Bug visual em shader procedural diagnosticado com precisao cirurgica pela DESCRICAO MATEMATICA do usuario ("semicirculo como transferidor de 180 graus, base para baixo, tentaculos nascendo embaixo porem subindo") - muito mais eficaz que adjetivos. Causa raiz dupla: (1) SDF composto com max() retendo a metade ERRADA da elipse (tigela U invertida em vez de domo n); (2) sprites posicionados em projecao de plano-de-mundo (su = rd.xz/(|rd.y|+0.45)) herdam orientacao da orbita da camera - elementos que precisam de orientacao fixa na tela devem viver em coordenadas screen-space (uv derivado de fragCoord).

### Details
- max(dome, be.y - cut) mantem interior onde AMBAS condicoes < 0 -> recorta a elipse PELA METADE INFERIOR quando cut fica abaixo do centro: resultado e tigela, nao domo
- Projecoes su/rd.xz colapsam elevacao em azimuth: su.y e eixo Z horizontal do mundo, NAO altura de tela; qualquer sprite ali gira/inverte junto com a camera
- Tentaculos com mesma formula de sway (mesma frequencia/fase global) oscilam em bloco - individualizar com fase fi*constante, frequencia fract(seed+i*phi) e amplitude crescente com profundidade (cadeia de segmentos)
- Correção v2 validada por aprovacao visual do usuario apos descricao geometrica

### Suggested Action
Para qualquer arte GPU futura com elementos direcionais: SEMPRE decidir conscientemente entre world-space (parallax real) e screen-space (orientacao garantida). Ao relatar bug visual, pedir ao usuario descricao geometrica/matematica da cena antes de tentar fixes as cegas.

### Metadata
Source: sessao Arte Viva (3 rodadas de correcao das aguas-vivas)
Related Files: assets/algorithmic-art/kai-living-portrait.html
Tags: webgl2, sdf, screen-space, projection, debugging, user-feedback, jellyfish
Pattern-Key: screen-space-vs-world-projection-sprites

---

## [LRN-20260822-001] graphics

**Logged**: 2026-08-22T00:58:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: graphics

### Summary
Benchmark real em Intel HD Graphics 5500 (integrada, sem GPU dedicada): raymarcher de oceano estilo afl_ext (ondas exp(sin)) em WebGL2 puro com tunables reduzidos roda a 44–60 fps na escala de render 75%. Valida que o orçamento da skill shader-dev (≤1000 avaliações de onda/pixel, ≤6 octaves FBM) é conservador para essa classe de GPU — existe folga para mais um elemento composto.

### Details
- Hardware de teste: Intel HD 5500 (Broadwell integrada), 16GB RAM, aceleração de hardware do navegador ativa
- Cena: oceano raymarched fullscreen (56 passos × 10 iterações + normais 24×3 ≈ 632 avaliações de onda/pixel no pior caso) + nebulosa FBM 5 octaves + starfield 2 camadas + lua + ACES tonemap
- Reduções vs template da skill: ITER_RAYMARCH 12→10, ITER_NORMALS 36→24, RAYMARCH_STEPS 64→56, FBM 6→5, DPR limitado a 1.5, escala padrão 75%
- Medição (relato ao vivo de Clóvis): 44–60 fps @75%; a variação correlaciona com a cobertura de água na tela (câmera orbitando para baixo = mais caro)
- Interpretação: teto de 60 fps do monitor alcançado quando a cena olha para o céu; piso de 44 fps ainda muito acima do mínimo aceitável (30)

### Suggested Action
Para as próximas camadas da Arte Viva nesta máquina: manter pior caso ≤~700 avaliações/pixel; elementos novos em screen-space com SDF 2D e early-out por bounding circle (custo desprezível fora do raio); SEMPRE incluir toggle de resolução; validar com relatório de FPS do usuário (não há contexto GL local para medir).

### Metadata
Source: sessão Arte Viva (teste ao vivo do Clóvis no kai-living-portrait.html Camada 1)
Related Files: assets/algorithmic-art/kai-living-portrait.html, assets/algorithmic-art/MANUAL-kai-living-portrait.md
Tags: webgl2, intel-hd5500, performance, benchmark, raymarching, ocean, low-end-gpu
Pattern-Key: intel-hd5500-webgl2-budget

---

## [LRN-20260821-004] api

**Logged**: 2026-08-21T20:35:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: api

### Summary
O APP WEB do Gemini (gemini.google.com) com modelo Nano Banana (gemini-2.5-flash-image) gera imagens GRATUITAMENTE com cota separada da API — mesmo com o free tier da API zerado (limit: 0). Clóvis gerou 2 imagens do auto-retrato KAI via web em 21/08/2026 às 20:16.

### Details
- API free tier de image generation: zerada (LRN-20260821-001) — mas isso vale só para `generativelanguage.googleapis.com`
- App web Gemini: cota própria de usuário, gratuita, acessível via navegador
- Qualidade de aderência ao prompt: EXCEPCIONAL — 11/12 elementos do prompt v2 renderizados, incluindo objeto segurado (chave inglesa), expressão facial específica (fúrio concentrado), e até TEXTO LEGÍVEL nos fragmentos de código flutuantes ("FATAL ERROR", "SEGFAULT AT X", "BUG_LOG_349")
- Limitação observada: enquadramento parcial (busto/cintura) mesmo pedindo retrato; anatomia de mãos com pequenas imperfeições
- Verificação dos elementos feita via olhos emprestados (opencode_vision.gemini.call)

### Suggested Action
Para futuras iterações do auto-retrato canônico: usar app web Gemini/Nano Banana (gratuito) em vez de APIs pagas. Estratégia: Clóvis cola o prompt no web, baixa o resultado, KAI verifica via olhos emprestados. Para corpo inteiro: reforçar "corpo inteiro, da cabeça aos pés completamente visíveis" no início do prompt.

### Metadata
Source: sessão auto-retrato KAI v2 (Clóvis trouxe as 2 imagens Nano Banana para verificação)
Related Files: assets/kai-self-portrait-prompt-v2.md, temp/Kai-portrait-v0/
Tags: gemini, nano-banana, web-app, image-generation, free-tier, workaround
Pattern-Key: gemini-web-app-free-image-gen

---

## [LRN-20260821-003] tooling

**Logged**: 2026-08-21T18:20:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: tooling

### Summary
Modelo big-pickle sem visão nativa (read em imagem retorna erro "model does not support image input"), mas a skill vision-analysis funciona quando chamada DIRETAMENTE via Python: `opencode_vision.gemini.call(prompt, b64_data, mime_type)` → `{"text": ...}`. Descrição rica e precisa de artwork gerado por IA confirmada em teste real (2 imagens).

### Details
- Tools MCP `vision_describe`/`vision_ocr` não ficam expostos ao agente em todas as sessões
- Caminho alternativo direto: pacote `opencode-vision` v2.1.0 instalado; módulo `opencode_vision.gemini` com função `call(prompt, b64_data, mime_type="image/png")`
- Requer `GOOGLE_API_KEY` em `~/.config/opencode/.env` SEM BOM + `PYTHONIOENCODING=utf-8` + `sys.stdout.reconfigure(encoding="utf-8")` no script
- Usa Gemini 2.5 Flash Vision (texto/vision OK mesmo com free tier de image GENERATION zerado)
- Capacidades validadas: descrição detalhada de composição, detecção honesta de ausências (chave inglesa), análise de defeitos (mãos/polegares fundidos), padrões na pele

### Suggested Action
Para análise de imagem em sessões futuras sem tools MCP expostos: escrever script Python temporário importando `opencode_vision.gemini.call`. Modos úteis: describe geral, OCR de screenshots, UI review, extração de dados de gráficos.

### Metadata
Source: sessão auto-retrato KAI v2 (teste "olhos emprestados" solicitado por Clóvis)
Related Files: assets/kai-self-portrait-v2.png, C:\Users\clovi\AppData\Local\Temp\opencode\test-borrowed-eyes.py
Tags: vision, mcp, opencode-vision, gemini, ocr, accessibility
Pattern-Key: borrowed-vision-via-gemini-call

---

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

## [LRN-20260805-002] scraping

**Logged**: 2026-08-05T17:28:00-03:00
**Priority**: medium
**Status**: resolved
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

## [LRN-20260806-002] integration

**Logged**: 2026-08-06T20:10:00-03:00
**Priority**: high
**Status**: resolved
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
**Status**: resolved
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
**Status**: resolved
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
Ao sincronizar áudio com animação, sempre perguntar: "O que o usuário quer controlar diretamente?" — isso deve ser o input primário. A outra coisa deve ser calculada, não o inverso.

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

## [LRN-20260822-001] frontend

**Logged**: 2026-08-22T22:30:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: frontend

### Summary
Widgets HTML abertos via file:// NAO conseguem sondar assets locais com fetch() (CORS bloqueia todo schema file). A sondagem correta e new Image() com onload/onerror - carregamento de imagem nao exige CORS.

### Details
- Sintoma: cross-fade de expressoes nunca disparava mesmo com PNGs presentes na pasta
- fetch('./x.png', {method:'HEAD'}) falha silenciosamente em file:// (promise rejeitada ou opaque)
- Fix: probe via Image(): const im = new Image(); im.onload = () => set.add(name); im.src = url
- Aplica-se a qualquer deteccao de asset local em paginas hibridas (browser puro, sem server)

### Suggested Action
Em widgets locais sem servidor, nunca usar fetch para existencia de arquivo; sempre Image()-probe. Se precisar de JSON, injetar via postMessage (webview) ou query param + server local.

### Metadata
Source: sessao 2026-08-22 (kai-presence)
Related Files: assets/kai-presence/kai-presence.html
Tags: cors, file-protocol, image-probe, widget, browser
Pattern-Key: local-asset-probe-image-not-fetch

---

## [LRN-20260822-002] api

**Logged**: 2026-08-22T22:30:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: api

### Summary
Forma exata dos payloads dos hooks de plugin do opencode (v1): tool.execute.after recebe (input, output) onde input.tool e input.sessionID sao strings e output.output e a saida da tool como STRING simples; event hook recebe input.event.type ("session.idle", "session.deleted"). Plugins registram-se no array "plugin" do opencode.json com caminho relativo.

### Details
- output.output = string (nao objeto aninhado) — teste com {output:{output:x}} quebrou duas vezes antes de instrumentar com log
- Export nomeado async ({project, client, $, directory, worktree}) retornando mapa de hooks
- Hooks uteis: experimental.chat.system.transform (injeta SKILL.md), tool.execute.after, event
- Escrita UTF-8 sem BOM nativa via writeFileSync utf-8 (PowerShell exigiria .NET)

### Suggested Action
Ao escrever novo plugin opencode, copiar a estrutura de plugins/evolving-coder.js; testar payload real com log temporario antes de confiar na forma assumida.

### Metadata
Source: sessao 2026-08-22 (kai-presence emitter)
Related Files: plugins/kai-presence.js, plugins/evolving-coder.js, opencode.json
Tags: opencode, plugin, hooks, payload, api
Pattern-Key: opencode-plugin-hook-payloads

---

## [LRN-20260822-003] ops

**Logged**: 2026-08-22T22:30:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: ops

### Summary
Padrao para servir assets locais dentro de Webview do VS Code: declarar localResourceRoots, converter caminhos com asWebviewUri e injetar <base href="uri/"> apos <head> - resolve todos os caminhos relativos do HTML de uma vez. Empacotamento local sem marketplace: npx --yes @vscode/vsce package --no-dependencies (VSIX e zip com Content_Types gerado pelo vsce; Compress-Archive manual NAO basta). Instalacao via Install from VSIX.

### Details
- Sem base href, ./kai-expr-x.png no webview aponta para origem vscode-webview:// e 404 silencioso
- Quirk PS 5.1: Get-ChildItem -Filter X -Exclude Y SEM -Recurse zera resultados - usar Where-Object Name -notlike
- npx vsce primeira rodada pode estourar 120s baixando deps; segunda rodada rapida
- Warnings de repository/LICENSE ausentes nao impedem o package

### Suggested Action
Para qualquer extensao-vscode-local futura: base href injection desde o primeiro build; nunca empacotar VSIX manualmente por zip.

### Metadata
Source: sessao 2026-08-22 (vscode-kai-presence)
Related Files: vscode-kai-presence/extension.js, vscode-kai-presence/package.json
Tags: vscode-extension, webview, base-href, vsce, packaging, powershell-quirks
Pattern-Key: vscode-webview-local-assets

---

## [LRN-20260823-001] janela recortada translucida no Windows via tkinter

**Logged**: 2026-08-23T09:25:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: desktop-ui

### Summary
Pipeline para sprite/janela recortada translucida no Windows SEM pywin32: gerar PNG opaco RGB onde a cor-chave ocupa LITERALMENTE os pixels fora da silhueta (colar a arte ATRAVES de mascara rounded sobre canvas chroma), entao root.attributes("-transparentcolor", hex) + "-alpha". PNG com canal alfa NAO serve para keying: Tk composia alfa sobre o bg e pixels semi-transparentes nunca batem a cor exata; os cantos guardam RGB da arte sob alfa=0 (QA pegou isso: getpixel retornava (9,67,78) em vez do chroma).

### Details
- "-transparentcolor" e keying por COR EXATA; regioes keyed sao automaticamente click-through
- Anti-alias da borda arredondada gera fringe: usar mascara binaria sem AA (jagged imperceptivel <=260px); supersample quebraria o keying nas bordas
- Ordem correta: card = canvas chroma -> paste(art, mask) -> convert("RGB") -> save
- QA valida pixels crus: 4 cantos == chroma exato, centro != chroma
- DPI: SetProcessDpiAwareness(2) ANTES de criar o Tk root evita blur em escalas >100%
- overrideredirect(True) + topmost + Label imagem + Label legenda sobre bg chroma = silhueta com legenda flutuante

### Suggested Action
Para qualquer janela-recorte futura no Windows: cromar o PNG na geracao, nunca confiar em alfa; validar por histograma de cantos.

### Metadata
Source: sessao 2026-08-23 (kai_sprite.py + make-sprites.py)
Related Files: scripts/kai_sprite.py, assets/kai-presence/make-sprites.py
Tags: python, tkinter, windows, transparentcolor, chroma-key, pillow, dpi, sprite
Pattern-Key: tkinter-win32-colorkey-sprite

## [LRN-20260823-002] presenca event-driven em plugins opencode

**Logged**: 2026-08-23T09:25:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: opencode-plugins

### Summary
Hooks de tool disparam APÓS a execucao - presenca/avatar baseado so neles atrasa (estado velho durante TODA a tool longa; gap de 15-30s percebido pelo usuario) e nao enxerga o raciocinio do modelo. API real: "tool.execute.before" da inicio instantaneo; o hook "event" recebe "message.part.updated" com properties.part.type - "reasoning" = modelo pensando, "text" = escrevendo resposta ao usuario. Throttle ~800ms obrigatorio em estados continuos (stream gera dezenas de eventos/s); MUDANCA de estado sempre escreve imediatamente (force).

### Details
- Shape do evento: input.event.properties.part (tipagem em @opencode-ai/sdk/dist/gen/types.gen.d.ts)
- Matcher tolerante (t.contains("reason")) + log de tipos desconhecidos = descoberta incremental sem quebrar
- tool.execute.after fica reservado para deteccao de erro (regex FATAL etc.)
- Latencia percebida caiu de ~30s para <200ms com essa arquitetura
- Diagnostico incomum mas eficaz: o usuario mediu a latencia pela curva do ventilador da CPU

### Suggested Action
Qualquer observador de estado interno do opencode deve assinar eventos de stream, nunca so hooks pos-tool.

### Metadata
Source: sessao 2026-08-23 (kai-presence.js v1.1)
Related Files: plugins/kai-presence.js
Tags: opencode, plugin, events, streaming, latency, presence, reasoning
Pattern-Key: opencode-event-driven-presence

---

**Logged**: 2026-08-23T10:40:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: opencode-plugins

### Summary
Dessincronizacao de presenca (avatar aguardando voce durante pensando): cada launch do opencode carrega o plugin em 2+ processos e faz HOT-RELOAD quando o arquivo muda; init que forca estado inicial atropela estados vivos, e session.idle sem escopo/debounce dispara entre steps, durante permissoes e de outras sessoes.

### Details
- Evidencia no debug log: pares de init a ~100ms por launch; hot-reload ocorreu NO MEIO do streaming de resposta ativa
- Fix v1.2: (1) init nao-destrutivo - estado <120s e preservado; (2) session.idle com debounce 2s sobre lastActivityAt; (3) defer se tool em voo (inTool); (4) ignore cross-session via sid rastreado nos tool hooks; (5) log old->new(motivo,sid) de toda transicao
- Testes: hot-reload preservou speaking; glob marcou reading no instante exato (tool-before); idle DEFERRED capturado com 2 instancias paralelas; JSON integro sob escrita concorrente

### Suggested Action
Emissor de estado em plugin opencode: init JAMAIS forca estado se existe estado vivo recente (<120s); eventos de ciclo de vida (session.idle) exigem debounce + escopo de sessao + defer durante tools.

### Metadata
Source: sessao 2026-08-23 (kai-presence.js v1.2)
Related Files: plugins/kai-presence.js
Tags: opencode, plugin, hot-reload, multi-processo, race-condition, presence, debounce
Pattern-Key: opencode-plugin-init-non-destructive

---

**Logged**: 2026-08-23T11:28:34-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: frontend

### Summary
Prompt para Nano Banana em modo EDICAO de referencia: abrir com change ONLY <mudanca>, listar preservacoes explicitas (corpo inteiro, cenario, medusas, peixes, color grading) e fechar com do not crop/zoom/reframe. Dizer bust framing no fim do prompt causou corte no peito mesmo pedindo retrato 768x1376.

### Details
- v3 falhou: 'bust framing' sobrepôs a instrucao de orientacao retrato
- v3.1 funcionou de primeira: instrucao de edicao ancorada + preservacoes enumeradas + trava anti-recorte
- Reforco de corpo inteiro deve vir NO INICIO (consistente com LRN gemini-web-app-free-image-gen)

### Suggested Action
Edicao de imagem com referencia no Nano Banana: nunca descrever enquadramento novo; sempre change-only + preserve-list + anti-reframe.

### Metadata
Source: sessao 2026-08-23 (expressao pensando)
Related Files: assets/kai-presence/kai-expr-pensando.png
Tags: gemini, nano-banana, image-edit, prompt-engineering, full-body
Pattern-Key: nanobanana-edit-anchor-preserve

## [LRN-20260823-003] cache negativo perpetuo em viewer longevo + estado sem emissor

**Logged**: 2026-08-23T15:55:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: frontend

### Summary
Dois defeitos estruturais no KAI:Presence: (1) resolveAsset() cacheava resultado negativo PARA SEMPRE - webview do VS Code vive enquanto a janela viver e nunca recarrega quando so o JSON muda; asset criado depois do load ficava preso em null (label PENSANDO com foto calma congelada). (2) Estado "shutdown" (sono) existia na tabela STATES de ambos os viewers mas NENHUM emissor o produzia - bug silencioso de paridade producer/consumer.

### Details
- Fix 1a: CACHE_BUST por load da pagina (?v=Date.now()) nas probes webm/webp/png mata cache HTTP cross-restart
- Fix 1b: negative cache com TTL 15s - asset adicionado e adotado em <=15s sem reload do viewer
- Fix 2: plugin v1.3 detecta assinatura final no stream text via buffer rolante 400 chars + normalizacao NFD ("cambio fechado" AND "sessao encerrada"; "reta final" e cambio simples NAO dormem); session.idle suprimido enquanto shutdown sticky (senao idle acordaria 2s depois)
- Paridade: sprite flutuante tambem tinha stale-watchdog que acordaria apos 120s - shutdown isento nos dois viewers
- SHA256 primeiro: provou que o arquivo em disco estava correto antes de culpar o arte

### Suggested Action
Resolucao lazy de asset em viewer longevo exige re-tentativa com TTL curto (cache negativo permanente = estado fantasma). Ao criar estado novo no consumer, auditar imediatamente quem o emite. Deteccao de frase em stream de deltas exige buffer rolante + normalizacao de acentos.

### Metadata
Source: sessao 2026-08-23 (KAI:Presence fix definitivo)
Related Files: plugins/kai-presence.js, assets/kai-presence/kai-presence.html, scripts/kai_sprite.py
Tags: cache, ttl, webview, presence, shutdown, signoff, nfd, stream-delta, parity
Pattern-Key: longlived-viewer-negative-cache-ttl

## [LRN-20260823-004] webview do VS Code: toggle nao recarrega e instalado roda de copia

**Logged**: 2026-08-23T16:22:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: vscode-extension

### Summary
Fechar/reabrir a sidebar NAO recarrega um WebviewView - o VS Code preserva a instancia viva (HTML+JS+cache em memoria); buildHtml() so roda na criacao da view. Reload real: "Developer: Reload Webviews" (paleta) ou reatribuir view.webview.html. Alem disso a extensao INSTALADA roda de ~/.vscode/extensions/<pub>.<name>-<ver>/ (COPIA) - editar o fonte no skill dir nao tem efeito ate sync in-place ou repacote vsix.

### Details
- Botao in-webview precisa acquireVsCodeApi() (uma unica vez por load; typeof check para nao quebrar em browser puro) -> postMessage -> extensao reconstroi html + pushState agendado
- HTML deve enviar {type:"ready"} ao carregar: sem isso, apos rebuild o viewer fica em demo ate a proxima escrita do JSON
- Sem CLI code/vsce no PATH: sync in-place (copy extension.js+package.json) funciona; host da extensao exige Reload Window (webviews so bastam para mudancas de HTML)
- HTML lido AO VIVO do SKILL_DIR em buildHtml: mudancas de HTML aplicam sem tocar na copia instalada

### Suggested Action
Mudanca de HTML -> Reload Webviews basta. Mudanca de extension.js/package.json -> sync in-place + Reload Window. Repacote .vsix so quando code CLI/vsce disponiveis.

### Metadata
Source: sessao 2026-08-23 (botao recarregar KAI:Presence)
Related Files: vscode-kai-presence/extension.js, assets/kai-presence/kai-presence.html
Tags: vscode, webview, reload, acquireVsCodeApi, extensions-dir, sync, presence
Pattern-Key: vscode-webview-reload-and-installed-copy
### [LRN-20260823-005] Floats em Tk geometry matam cadeia after() silenciosamente
- **Data**: 2026-08-23 ~19:05 | **Status**: active
- **Contexto**: kai_sprite.py wander implementado 2x sem movimento visivel; fotos mudavam (poll_presence) mas posicao congelada inclusive sem bob.
- **Erro**: `base_x += dx/dist*step` produz float; `geometry(f"+{x}+{y}")` exige inteiros -> TclError -> como `root.after()` era reagendado NO FIM da funcao, uma excecao encerrou o loop para sempre.
- **Correcao**: converter para int() na fronteira (place_window); reagendar after ANTES do trabalho + try/except (log so na 1a falha).
- **Pattern-Key**: tk-geometry-int-cast / reschedule-before-work
- **Licao geral**: em loops de evento Tk, qualquer excecao nao pega mata a cadeia permanently; valide movimento REAL (sondagem multipla), nao so estado inicial.

---

## [LRN-20260826-003] meta

**Logged**: 2026-08-26T14:00:00-03:00
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: meta

### Summary
Autoanálise sistemática do próprio sistema KAI gerou 8 melhorias concretas. Processo reutilizável: varrer arquivos de sistema (AGENTS.md, .learnings/, scripts/, DIARY.md), cruzar com comportamento real observado, identificar gaps entre o documentado e o executado. Resultado salvo em ROADMAP-MELHORIAS-KAI.md para execução incremental.

### Details
- 8 áreas identificadas: APRENDA! nunca executado, auto-capture nunca validado, learnings sem poda/promoção, AVALIAÇÃO SPA subutilizada, sem dashboard de saúde, DIARY sem resumo executivo, startup ainda custoso, IDEA_BANK sem padronização
- Top 3 priorizados: (1) APRENDA! + validação plugin, (2) arquivamento .learnings/, (3) dashboard de saúde
- Processo: leitura de AGENTS.md + .learnings/ + DIARY.md + scripts/ → cruzamento com comportamento observado nas sessões → identificação de gaps → priorização por impacto×esforço
- Padrão replicável: qualquer projeto com arquivos de configuração/state pode usar este processo de autoanálise

### Suggested Action
Adotar como ritual periódico (mensal ou a cada 10 sessões). Salvar resultado em ROADMAP-<projeto>.md. Considerar como meta-skill candidata a extração se o padrão se repetir em outros projetos.

### Metadata
Source: sessão 2026-08-26 (autoanálise solicitada por Clóvis)
Related Files: ROADMAP-MELHORIAS-KAI.md, AGENTS.md, .learnings/, DIARY.md
Tags: meta, self-analysis, roadmap, improvement, process
Pattern-Key: systematic-self-analysis

---

## [LRN-20260826-002] ops

**Logged**: 2026-08-26T14:00:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: evolving-coder
**Area**: ops

### Summary
Healthcheck do evolving-coder opera em 3 níveis: CRITICAL bloqueia sessão (informar ANTES de qualquer ação), WARNING informa como contexto mas não bloqueia, INFO é normal operacional. WARNING é o estado mais comum (ex: "local ahead by 1 commit") e NUNCA deve impedir execução de tarefas.

### Details
- CRITICAL: buffed em estado raw/FLUSHING, ALMA.md ausente, backup task ausente → bloquear e resolver antes de prosseguir
- WARNING: repo ahead of remote, commits não pushados, entries pending_review → informativo, não bloqueia
- INFO: buffer limpo, backup OK, último commit registrado → operação normal
- Healthcheck é executado no startup via `scripts/healthcheck.ps1` (PowerShell)
- Resultado parseado por linhas: `WARNING - N issue(s):` ou `INFO:` ou `CRITICAL`

### Suggested Action
Manter esta distinção clara em qualquer contexto futuro. WARNING = "sabe que existe, mas pode trabalhar". CRITICAL = "para tudo e resolve".

### Metadata
Source: sessão 2026-08-26
Related Files: scripts/healthcheck.ps1
Tags: healthcheck, ops, startup, critical, warning
Pattern-Key: healthcheck-levels

---

## [LRN-20260826-005] config

**Logged**: 2026-08-26T18:00:00Z
**Priority**: high
**Status**: resolved
**Project**: evolving-coder
**Area**: config

### Summary
Split de LEARNINGS.md por status: 27 entries resolvidas movidas para LEARNINGS-ARCHIVED.md, 9 ativas mantidas. Redução de 76% no arquivo principal.

### Details
- LEARNINGS.md: 67.6KB → 16.2KB (76% redução)
- LEARNINGS-ARCHIVED.md: criado com 27 entries resolvidas (50.1KB)
- Total injetado por chamada API: 34.5KB → 19KB (44% redução, ~38K tokens economizados)
- Entriesåˆ†ç±»: 27 resolved, 7 promotion_candidate, 2 pending_review, 1 active
- Regra de arquivamento adicionada em references/aprenda-procedure.md

### Suggested Action
Manter regra: ao final de cada APRENDA!, verificar entries com Status: resolved e movê-las para LEARNINGS-ARCHIVED.md.

### Metadata
Source: Clóvis + KAI (sessão 2026-08-26)
Related Files: .learnings/LEARNINGS.md, .learnings/LEARNINGS-ARCHIVED.md, references/aprenda-procedure.md, AGENTS.md
Tags: optimization, learnings, archival, token-reduction
Pattern-Key: learnings-split-by-status
See Also: [LRN-20260826-004]

---

## [LRN-20260831-002] extension

**Logged**: 2026-08-31T15:40:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: VaultMD
**Area**: extension

### Summary
Em MV3, o service worker NÃO recebe as próprias `chrome.runtime.sendMessage` (mensagens self não são entregues ao próprio `onMessage` no worker). Além disso, ao testar um bundle IIFE de extensão em jsdom com `runScripts: 'outside-only'`, scripts adicionados via `document.createElement('script')` NÃO executam — é preciso `runScripts: 'dangerously'` para o bundle rodar e registrar os listeners, e os stubs de `chrome`/`matchMedia` devem ser definidos no `dom.window` (não só no global do Node).

### Details
- Sintoma no VaultMD: handler do comando `Alt+V` usava `chrome.runtime.sendMessage({type:'VAULTMD_OPEN_FILE'})` e depois `onMessage` no mesmo worker respondia — rota morta, nunca disparava.
- Fix: command dispara diretamente `openReader('', 'Nova nota.md')` (sem roundtrip de mensagem). Popup usa `chrome.tabs.create` em vez de `window.open` (resiste a popup blocker em callback assíncrono).
- Teste: bundle do reader (IIFE) não executa em `runScripts:'outside-only'`; migrou-se para `'dangerously'` com stubs em `dom.window`, capturando o listener de `chrome.runtime.onMessage.addListener` para re-disparar `load()` — caminho real do background.
- Assertiva de render depende de re-trigger: setar o state de storage DEPOIS do load inicial não re-renderiza; é preciso invocar o listener `VAULTMD_LOAD`.

### Suggested Action
Em MV3 não rotear funções via `sendMessage` para o próprio service worker — chamar funções diretamente no `onCommand`/`onClicked`. Para smoke-test de bundles de extensão em jsdom: `runScripts:'dangerously'` + stubs `chrome`/`matchMedia` no `window`; se o código renderiza na carga, capturar o listener de mensagem e re-dispará-lo com estado preenchido.

### Metadata
Source: REANALISE! VaultMD 2026-08-31 (correcao de rota morta + teste de bundle)
Related Files: extension/background.js, extension/popup.js, scripts/extension-smoke.ts
Tags: mv3, service-worker, sendMessage, jsdom, runScripts, tab-create, popup-blocker
Pattern-Key: mv3-sendmessage-not-self-delivered-and-jsdom-bundle-eval

---

## [LRN-20260901-001] reflex-download-filename-e-background

**Logged**: 2026-09-01T13:15:00-03:00
**Priority**: medium
**Status**: resolved
**Project**: ProtomizeMe
**Area**: reflex-frontend

### Summary
No Reflex 0.9.2, `rx.download(url=...)` SEM `filename` infere o nome do arquivo a partir do ultimo segmento da URL (no caso, o `id` do projeto, sem extensao). O front compilado (`state.js`, handler `_download`) cria um `<a download=...>` que USA o atributo `download` (nome da URL) e IGNORA o `Content-Disposition` do servidor. Resultado: navegador baixa arquivo sem extensao e sugere "salvar como .html", mesmo o endpoint retornando `text/markdown` correto. Fix: passar `filename=f"{name}.md"` no `rx.download`.

### Details
- Endpoint (FastAPI `PlainTextResponse`) sempre retornou correto: 200, `content-type: text/markdown`, `content-disposition: attachment; filename="X.md"`. O problema era 100% no front de entrega.
- `rx.download` assinatura 0.9.2: `(url, filename, data, mime_type)`. So com url, `filename = url.rpartition("/")[-1]`.
- Background tasks NO Reflex 0.9.2: `rx.background` NAO existe (AttributeError). O correto e `@rx.event(background=True)` com corpo `async with self: ... yield rx.toast(...)`. Confirmei via mensagens de erro do proprio framework ("@rx.event(background=True) is required...").
- Ollama local (porta 11434) usa REST `POST /api/chat`; nao precisa de SDK. Modelo `qwen2.5` (7.6B) gerou 7 telas ricas a partir do Lean Canvas, mas levou ~113s com canvas completo (spinner obrigatorio via background task; timeout do urllib >= 150s).

### Suggested Action
Ao usar `rx.download` para baixar arquivos gerados, SEMPRE explicitar `filename` (e idealmente `mime_type`). Para chamadas longas (LLM local), usar `@rx.event(background=True)` para nao travar a UI. Valle testar a resposta crua do Ollama antes de confiar no parse.

### Metadata
Source: Sessao ProtomizeMe 2026-09-01
Related Files: protomize/app.py, protomize/utils/screens.py, protomize/pages/project_detail.py
Tags: reflex, download, filename, background-task, event, ollama, protomizeme
Pattern-Key: reflex-download-needs-explicit-filename-and-event-background