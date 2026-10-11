# MANUAL — KAI Presence

> Sistema de presença viva da KAI: ela te vê trabalhando, reage ao que acontece
> nas sessões opencode e se comunica por balões. Este é o documento mestre.
> Última revisão: 2026-08-24 (v1.4).
> Idiomas: [English](MANUAL-kai-presence.md) · [Português](MANUAL-kai-presence_pt-BR.md) · [Español](MANUAL-kai-presence_es.md)

---

## Visão Geral

```
┌─────────────────────────────────────────────────────────────┐
│ opencode (processo node)                                    │
│   plugins/kai-presence.js  [EMISSOR v1.4]                   │
│     • hooks tool.execute.before/after + event stream        │
│     • escreve .kai-presence.json (estado+balão+pid)         │
│     • heartbeat 5s (mantém ts fresco)                       │
│     • SPAWN do sprite no boot (auto-start)                  │
└──────────────┬──────────────────────────────────────────────┘
               │ .kai-presence.json (~90 bytes, UTF-8)
       ┌───────┴────────────────┬─────────────────────────┐
       ▼                        ▼                         │
┌──────────────┐   ┌───────────────────────────┐           │
│ SPRITE       │   │ VIEWER VS CODE            │           │
│ scripts/     │   │ vscode-kai-presence/      │           │
│ kai_sprite.py│   │ extension.js (WebviewView)│           │
│ (tkinter,    │   │ → kai-presence.html       │           │
│ poll 500ms)  │   │   (aura + retrato)        │           │
└──────────────┘   └───────────────────────────┘           │
```

Três consumidores independentes do mesmo arquivo de estado. Zero rede.

---

## Componentes

### 1. Emissor — `plugins/kai-presence.js` (v1.4)

**Localização canônica**: `skills/evolving-coder/plugins/kai-presence.js`
**Deploy**: `~/.config/opencode/plugins/kai-presence.js` (registrado em `opencode.json` → `"plugin"`)

| Recurso | Detalhe |
|---------|---------|
| Mapeamento tools | `read/grep/glob/webfetch/websearch` → reading; `write/edit/task/skill/bash` → working |
| Stream parts | `reasoning/thinking` → thinking; `text` → speaking |
| Throttle | 800ms por estado contínuo (writes repetidos suprimidos) |
| Erro | saída bash com padrões `fatal/exception/traceback/...` → estado error force |
| Idle | `session.idle` com debounce 2s, defer se tool em voo, ignore cross-session |
| Shutdown | assinatura final no texto: "câmbio fechado" AND "sessão encerrada" (buffer rolante 400 chars + NFD); sticky — idle não acorda |
| Preservação | init não-destrutivo: estado vivo <120s é preservado (hot-reload seguro) |
| **Balões (novo v1.4)** | `pickBubble()`: mensagem amigável em transição de estado (working/reading/idle/error/shutdown), variantes aleatórias, cooldown 25s (error/shutdown ignoram) |
| **Heartbeat (novo v1.4)** | reescreve o JSON a cada 5s com `ts` fresco e `message:""` (bolhas mostram uma vez só) |
| **Auto-start (novo v1.4)** | `ensureSprite()` no boot: resolve `pythonw`→`python` via `where`, faz spawn detached do sprite (mutex garante instância única) |
| **pid (novo v1.4)** | todo write inclui `pid: process.pid` — base da despedida |

Log: `~/.config/opencode/plugins/kai-presence-debug.log`.

### 2. Sprite Flutuante — `scripts/kai_sprite.py`

Janela tkinter nativa: borderless, topmost, alpha configurável (30–100%),
transparentcolor chroma `#10141c`, animação 4 frames/estado (400ms/frame).

**Estados** (8): idle/calma · pensando · leitura · chave(working) · sorriso(speaking) · fúria(error) · milestone(sorriso dourado) · sono(shutdown).

| Recurso | Detalhe |
|---------|---------|
| Movimento | wander (alvo aleatório 9–16s, 26px/s) ou bob (flutuar no lugar); menu direito alterna |
| Confinamento | soltar sobre uma janela a adota como hospedeira (EnumWindows + DWM cloak check); transiente até re-drag |
| Multi-monitor | EnumDisplayMonitors + rcWork; clamp correto; posição invisível → reset |
| Drag | botão esquerdo; timeout 6s anti-arrasto-preso; duplo clique abre o painel HTML |
| **Caption (fix v1.4)** | reveza a cada 6s entre label do ESTADO ("pensando") e contexto ("em VS Code") — antes o contexto sequestrava o label |
| **Balões (novo v1.4)** | bolha acima do retrato; dedupe (mesmo texto <60s não repete) + gap mínimo 15s; toggle "Balões de atividade" no menu (persistido); greeting/click/error são `force` |
| **Saudação (v1.x)** | boot mostra "Bom dia/Boa tarde/Boa noite/Boa madrugada" conforme hora |
| **Despedida (novo v1.4)** | `check_stale()` valida PID do opencode (`OpenProcess`); PID morto após grace de 10s do boot → bolha "até logo" + som + destroy em ~2.8s |
| Lazy-load (v1.4) | frame 0 de cada estado carrega síncrono; frames de animação enfileirados em background (boot rápido) |
| Persistência | `%LOCALAPPDATA%\KAI\sprite-pos.json`: x, y, size, motion, alpha, bubbles |
| Instância única | mutex `KAI_Sprite_Mutex` — launchers idempotentes |

Erros de runtime: `%LOCALAPPDATA%\KAI\sprite-error.log` (1ª ocorrência apenas).

### 3. Viewer VS Code — `vscode-kai-presence/`

Extensão local (publisher `kai-local`, v0.1.0): WebviewView na activity bar
(ícone de gota). FileSystemWatcher no `.kai-presence.json` → pushState.
Botão ↻ recarrega o HTML; comando de paleta "KAI: Recarregar Presença".
Detalhes de instalação → `vscode-kai-presence/README.md`.

O HTML (`assets/kai-presence/kai-presence.html`) tem negative-cache de assets
com TTL 15s + cache-busting por load (lição 2026-08-23: webview longevo nunca
adotaria asset criado depois).

---

## Ciclo de Vida (desde v1.4)

1. Você abre opencode (terminal do VS Code ou standalone)
2. Plugin carrega → preserva estado vivo se houver → heartbeat liga → **spawna o sprite**
3. Trabalho flui: estados e balões reagem em tempo real
4. Você fecha o opencode → heartbeat cessa → sprite detecta PID morto → **se despede e sai**
5. Abrir de novo → KAI volta

> Legado: Run key `KAISprite` (HKCU, logon do Windows) existia desde 23/08.
> Redundante com o auto-start por sessão — remover é recomendado (o sprite só
> faz sentido com opencode vivo).

---

## Schema `.kai-presence.json`

```json
{
  "state": "working",
  "detail": "bash",
  "message": "mãos à obra! 🔧",
  "pid": 12345,
  "hb": true,
  "ts": "2026-08-24T18:00:00.000Z"
}
```

| Campo | Quem escreve | Consumo |
|-------|--------------|---------|
| state | emitter | todos (sprite/viewer/demo HTML) |
| detail | emitter | viewer (legenda) |
| message | emitter (transições) / heartbeat limpa | sprite (balha), 1 exibição |
| pid | emitter | sprite (despedida) |
| hb | heartbeat | diagnóstico |
| ts | sempre | stale-watchdog (>120s → idle) |

---

## Deploy & Paridade

```powershell
# após editar o plugin no repo:
Copy-Item plugins\kai-presence.js "$env:USERPROFILE\.config\opencode\plugins\" -Force
```

O `healthcheck.ps1` compara MD5 repo vs deploy → WARNING se divergirem.
O sprite roda DIRETO do repo (sem cópia deploy). A extensão VS Code instala-se
via VSIX (ver README próprio).

## QA Rápido

```powershell
node --check plugins\kai-presence.js          # sintaxe emissor
python -m py_compile scripts\kai_sprite.py    # sintaxe sprite
# smoke boot (6s vivo, sem sprite-error.log = verde):
$p = Start-Process pythonw -ArgumentList "scripts\kai_sprite.py" -PassThru; Start-Sleep 6; $p.HasExited; Stop-Process $p.Id
```

Teste fim-a-fim do ciclo completo exige reiniciar o opencode (spawn no boot).
Regeneração de sprites: `make-sprites.py` (cartões) + `generate_anim_frames.py`
(frames de animação); QA de keying: `qa-expressoes.ps1`.

## Troubleshooting

| Sintoma | Causa provável | Ação |
|---------|----------------|------|
| Sprite não aparece com o opencode | plugin não deployado / python fora do PATH | healthcheck (paridade); `where pythonw` |
| Duas KAI na tela | impossível por mutex; se vir, processo zumbi antigo | matar pythonw antigo |
| Bolha não some / repete | versão antiga do sprite (pré-v1.4) | confirmar deploy + restart |
| KAI sumiu sozinha | despedida: opencode fechou/crashou | esperado — reabra o opencode |
| Label preso num estado | emissor morto (heartbeat parou >120s) → idle automático | verificar log do plugin |
| Foto errada num estado (viewer) | cache negativo pré-TTL | reload do webview (↻) |
