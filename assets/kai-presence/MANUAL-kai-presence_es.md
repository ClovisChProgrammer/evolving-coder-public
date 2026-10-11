# MANUAL — KAI Presence

> Sistema de presencia viva de KAI: te ve trabajar, reacciona a lo que ocurre
> en las sesiones opencode y se comunica mediante globos. Este es el documento
> maestro. Última revisión: 2026-08-24 (v1.4).
> Idiomas: [English](MANUAL-kai-presence.md) · [Português](MANUAL-kai-presence_pt-BR.md) · [Español](MANUAL-kai-presence_es.md)

---

## Visión General

```
┌─────────────────────────────────────────────────────────────┐
│ opencode (proceso node)                                     │
│   plugins/kai-presence.js  [EMISOR v1.4]                    │
│     • hooks tool.execute.before/after + event stream        │
│     • escribe .kai-presence.json (estado+globo+pid)         │
│     • heartbeat 5s (mantiene ts fresco)                     │
│     • SPAWN del sprite en el boot (auto-inicio)             │
└──────────────┬──────────────────────────────────────────────┘
               │ .kai-presence.json (~90 bytes, UTF-8)
       ┌───────┴────────────────┬─────────────────────────┐
       ▼                        ▼                         │
┌──────────────┐   ┌───────────────────────────┐           │
│ SPRITE       │   │ VISOR VS CODE             │           │
│ scripts/     │   │ vscode-kai-presence/      │           │
│ kai_sprite.py│   │ extension.js (WebviewView)│           │
│ (tkinter,    │   │ → kai-presence.html       │           │
│ poll 500ms)  │   │   (aura + retrato)        │           │
└──────────────┘   └───────────────────────────┘           │
```

Tres consumidores independientes del mismo archivo de estado. Cero red.

---

## Componentes

### 1. Emisor — `plugins/kai-presence.js` (v1.4)

**Ubicación canónica**: `skills/evolving-coder/plugins/kai-presence.js`
**Deploy**: `~/.config/opencode/plugins/kai-presence.js` (registrado en `opencode.json` → `"plugin"`)

| Característica | Detalle |
|----------------|---------|
| Mapeo de tools | `read/grep/glob/webfetch/websearch` → reading; `write/edit/task/skill/bash` → working |
| Stream parts | `reasoning/thinking` → thinking; `text` → speaking |
| Throttle | 800ms por estado continuo (writes repetidos suprimidos) |
| Error | salida bash con patrones `fatal/exception/traceback/...` → estado error forzado |
| Idle | `session.idle` con debounce 2s, diferido si hay tool en vuelo, ignora cross-session |
| Shutdown | firma final en el texto: "câmbio fechado" AND "sessão encerrada" (buffer rodante 400 chars + NFD); sticky — idle no la despierta |
| Preservación | init no destructivo: estado vivo <120s se preserva (hot-reload seguro) |
| **Globos (nuevo v1.4)** | `pickBubble()`: mensaje amistoso en transiciones de estado (working/reading/idle/error/shutdown), variantes aleatorias, cooldown 25s (error/shutdown lo ignoran) |
| **Heartbeat (nuevo v1.4)** | reescribe el JSON cada 5s con `ts` fresco y `message:""` (los globos se muestran una sola vez) |
| **Auto-inicio (nuevo v1.4)** | `ensureSprite()` en el boot: resuelve `pythonw`→`python` vía `where`, lanza el sprite detached (el mutex garantiza instancia única) |
| **pid (nuevo v1.4)** | todo write incluye `pid: process.pid` — base de la despedida |

Log: `~/.config/opencode/plugins/kai-presence-debug.log`.

### 2. Sprite Flotante — `scripts/kai_sprite.py`

Ventana tkinter nativa: borderless, topmost, alpha configurable (30–100%),
transparentcolor chroma `#10141c`, animación 4 frames/estado (400ms/frame).

**Estados** (8): idle/calmado · pensando · lectura · llave(working) · sonrisa(speaking) · furia(error) · milestone(sonrisa dorada) · sueño(shutdown).

| Característica | Detalle |
|----------------|---------|
| Movimiento | wander (objetivo aleatorio 9–16s a 26px/s) o bob (flotar en el sitio); menú derecho alterna |
| Confinamiento | soltar sobre una ventana la adopta como anfitriona (EnumWindows + DWM cloak check); transitorio hasta el próximo drag |
| Multi-monitor | EnumDisplayMonitors + rcWork; clamp correcto; posición invisible → reset |
| Drag | botón izquierdo; timeout 6s anti-arrastre-atascado; doble clic abre el panel HTML |
| **Caption (fix v1.4)** | alterna cada 6s entre label del ESTADO ("pensando") y contexto ("en VS Code") — antes el contexto secuestraba el label |
| **Globos (nuevo v1.4)** | globo sobre el retrato; dedupe (mismo texto <60s no repite) + gap mínimo 15s; toggle "Balões de atividade" en el menú (persistido); greeting/click/error son `force` |
| **Saludo (v1.x)** | el boot muestra "Bom dia/Boa tarde/Boa noite/Boa madrugada" según la hora |
| **Despedida (nuevo v1.4)** | `check_stale()` valida el PID del opencode (`OpenProcess`); PID muerto tras la gracia de 10s del boot → globo de despedida + sonido + destroy en ~2.8s |
| Lazy-load (v1.4) | frame 0 de cada estado carga síncrono; frames de animación en cola en background (boot rápido) |
| Persistencia | `%LOCALAPPDATA%\KAI\sprite-pos.json`: x, y, size, motion, alpha, bubbles |
| Instancia única | mutex `KAI_Sprite_Mutex` — launchers idempotentes |

Errores de runtime: `%LOCALAPPDATA%\KAI\sprite-error.log` (solo 1ª ocurrencia).

### 3. Visor VS Code — `vscode-kai-presence/`

Extensión local (publisher `kai-local`, v0.1.0): WebviewView en la activity bar
(icono de gota). FileSystemWatcher sobre `.kai-presence.json` → pushState.
Botón ↻ recarga el HTML; comando de paleta "KAI: Recarregar Presença".
Detalles de instalación → `vscode-kai-presence/README.md`.

El HTML (`assets/kai-presence/kai-presence.html`) tiene negative-cache de assets
con TTL 15s + cache-busting por load (lección 2026-08-23: un webview longevo
nunca adoptaría un asset creado después).

---

## Ciclo de Vida (desde v1.4)

1. Abres opencode (terminal de VS Code o standalone)
2. El plugin carga → preserva estado vivo si existe → heartbeat activo → **lanza el sprite**
3. El trabajo fluye: estados y globos reaccionan en tiempo real
4. Cierras opencode → heartbeat cesa → el sprite detecta PID muerto → **se despide y sale**
5. Abrir de nuevo → KAI vuelve

> Legado: la Run key `KAISprite` (HKCU, inicio de Windows) existió desde 23/08.
> Redundante con el auto-inicio por sesión — se recomienda eliminarla (el sprite
> solo tiene sentido con opencode vivo).

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

| Campo | Quién escribe | Consumo |
|-------|---------------|---------|
| state | emitter | todos (sprite/visor/demo HTML) |
| detail | emitter | visor (leyenda) |
| message | emitter (transiciones) / heartbeat la limpia | sprite (globo), 1 visualización |
| pid | emitter | sprite (despedida) |
| hb | heartbeat | diagnóstico |
| ts | siempre | stale-watchdog (>120s → idle) |

---

## Deploy & Paridad

```powershell
# tras editar el plugin en el repo:
Copy-Item plugins\kai-presence.js "$env:USERPROFILE\.config\opencode\plugins\" -Force
```

El `healthcheck.ps1` compara MD5 repo vs deploy → WARNING si divergen.
El sprite corre DIRECTO del repo (sin copia deploy). La extensión VS Code se
instala vía VSIX (ver su propio README).

## QA Rápido

```powershell
node --check plugins\kai-presence.js          # sintaxis emisor
python -m py_compile scripts\kai_sprite.py    # sintaxis sprite
# smoke boot (6s vivo, sin sprite-error.log = verde):
$p = Start-Process pythonw -ArgumentList "scripts\kai_sprite.py" -PassThru; Start-Sleep 6; $p.HasExited; Stop-Process $p.Id
```

La prueba fin-a-fin del ciclo completo exige reiniciar opencode (spawn en boot).
Regeneración de sprites: `make-sprites.py` (tarjetas) + `generate_anim_frames.py`
(frames de animación); QA de keying: `qa-expressoes.ps1`.

## Troubleshooting

| Síntoma | Causa probable | Acción |
|---------|----------------|--------|
| El sprite no aparece con opencode | plugin sin deploy / python fuera del PATH | healthcheck (paridad); `where pythonw` |
| Dos KAI en pantalla | imposible por mutex; si ocurre, proceso zombi antiguo | matar pythonw viejo |
| Globo no desaparece / repite | versión antigua del sprite (pre-v1.4) | confirmar deploy + restart |
| KAI desapareció sola | despedida: opencode cerró/crasheó | esperado — reabre opencode |
| Label atascado en un estado | emisor muerto (heartbeat paró >120s) → idle automático | revisar log del plugin |
| Foto errada en un estado (visor) | cache negativo pre-TTL | reload del webview (↻) |
