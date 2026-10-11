# MANUAL — KAI Presence

> A living presence system for KAI: she watches you work, reacts in real time
> to what happens in opencode sessions, and talks to you through speech bubbles.
> This is the master document. Last revision: 2026-08-24 (v1.4).
> Languages: [English](MANUAL-kai-presence.md) · [Português](MANUAL-kai-presence_pt-BR.md) · [Español](MANUAL-kai-presence_es.md)

---

## Overview

```
┌─────────────────────────────────────────────────────────────┐
│ opencode (node process)                                     │
│   plugins/kai-presence.js  [EMITTER v1.4]                   │
│     • tool.execute.before/after hooks + event stream        │
│     • writes .kai-presence.json (state + bubble + pid)      │
│     • 5s heartbeat (keeps ts fresh)                         │
│     • SPAWNS the sprite on boot (auto-start)                │
└──────────────┬──────────────────────────────────────────────┘
               │ .kai-presence.json (~90 bytes, UTF-8)
       ┌───────┴────────────────┬─────────────────────────┐
       ▼                        ▼                         │
┌──────────────┐   ┌───────────────────────────┐           │
│ SPRITE       │   │ VS CODE VIEWER            │           │
│ scripts/     │   │ vscode-kai-presence/      │           │
│ kai_sprite.py│   │ extension.js (WebviewView)│           │
│ (tkinter,    │   │ → kai-presence.html       │           │
│ poll 500ms)  │   │   (aura + portrait)       │           │
└──────────────┘   └───────────────────────────┘           │
```

Three independent consumers of the same state file. Zero network.

---

## Components

### 1. Emitter — `plugins/kai-presence.js` (v1.4)

**Canonical location**: `skills/evolving-coder/plugins/kai-presence.js`
**Deploy target**: `~/.config/opencode/plugins/kai-presence.js` (registered in `opencode.json` → `"plugin"`)

| Feature | Detail |
|---------|--------|
| Tool mapping | `read/grep/glob/webfetch/websearch` → reading; `write/edit/task/skill/bash` → working |
| Stream parts | `reasoning/thinking` → thinking; `text` → speaking |
| Throttle | 800ms per continuous state (repeated writes suppressed) |
| Error | bash output matching `fatal/exception/traceback/...` → forced error state |
| Idle | `session.idle` with 2s debounce, deferred while a tool is in flight, cross-session ignored |
| Shutdown | final-signature detection in text: "câmbio fechado" AND "sessão encerrada" (400-char rolling buffer + NFD normalization); sticky — idle won't wake it |
| Preservation | non-destructive init: live state <120s is preserved (hot-reload safe) |
| **Bubbles (new in v1.4)** | `pickBubble()`: friendly message on state transitions (working/reading/idle/error/shutdown), random variants, 25s cooldown (error/shutdown bypass it) |
| **Heartbeat (new in v1.4)** | rewrites the JSON every 5s with a fresh `ts` and `message:""` (bubbles display once only) |
| **Auto-start (new in v1.4)** | `ensureSprite()` on boot: resolves `pythonw`→`python` via `where`, spawns the sprite detached (mutex guarantees single instance) |
| **pid (new in v1.4)** | every write includes `pid: process.pid` — the farewell mechanism's foundation |

Log: `~/.config/opencode/plugins/kai-presence-debug.log`.

### 2. Floating Sprite — `scripts/kai_sprite.py`

Native tkinter window: borderless, topmost, adjustable alpha (30–100%),
transparentcolor chroma key `#10141c`, 4-frame animation per state (400ms/frame).

**States** (8): idle/calm · thinking · reading · wrench(working) · smile(speaking) · fury(error) · milestone(golden smile) · sleep(shutdown).

| Feature | Detail |
|---------|--------|
| Motion | wander (random target every 9–16s at 26px/s) or bob (float in place); right-click menu switches |
| Host confinement | dropping onto a window adopts it as host (EnumWindows + DWM cloak check); transient until next drag |
| Multi-monitor | EnumDisplayMonitors + rcWork; correct clamping; invisible saved position → reset |
| Drag | left button; 6s stuck-drag timeout; double-click opens the HTML panel |
| **Caption (fixed v1.4)** | alternates every 6s between the STATE label ("thinking") and context ("in VS Code") — context used to hijack the label permanently |
| **Bubbles (new in v1.4)** | bubble above the portrait; dedupe (same text within 60s never repeats) + 15s minimum gap; "Activity bubbles" toggle in the menu (persisted); greeting/click/error are `force` |
| **Greeting (v1.x)** | boot shows "Good morning/afternoon/evening" based on the hour |
| **Farewell (new in v1.4)** | `check_stale()` validates the opencode PID (`OpenProcess`); dead PID after the 10s boot grace → "goodbye" bubble + sound + destroy in ~2.8s |
| Lazy loading (v1.4) | frame 0 of each state loads synchronously; animation frames queue in the background (fast boot) |
| Persistence | `%LOCALAPPDATA%\KAI\sprite-pos.json`: x, y, size, motion, alpha, bubbles |
| Single instance | `KAI_Sprite_Mutex` mutex — idempotent launchers |

Runtime errors: `%LOCALAPPDATA%\KAI\sprite-error.log` (first occurrence only).

### 3. VS Code Viewer — `vscode-kai-presence/`

Local extension (publisher `kai-local`, v0.1.0): WebviewView in the activity
bar (droplet icon). FileSystemWatcher on `.kai-presence.json` → pushState.
↻ button reloads the HTML; palette command "KAI: Recarregar Presença".
Install details → `vscode-kai-presence/README.md`.

The HTML (`assets/kai-presence/kai-presence.html`) has asset negative-cache
with a 15s TTL + cache-busting per load (lesson from 2026-08-23: a long-lived
webview would never adopt assets created after load).

---

## Lifecycle (since v1.4)

1. You open opencode (VS Code terminal or standalone)
2. Plugin loads → preserves live state if any → heartbeat starts → **spawns the sprite**
3. Work flows: states and bubbles react in real time
4. You close opencode → heartbeat stops → sprite detects the dead PID → **says goodbye and exits**
5. Open again → KAI returns

> Legacy: the `KAISprite` Run key (HKCU, Windows logon) existed since 08/23.
> Redundant with per-session auto-start — removal is recommended (the sprite
> only makes sense while opencode lives).

---

## `.kai-presence.json` Schema

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

| Field | Written by | Consumed by |
|-------|-----------|-------------|
| state | emitter | all (sprite/viewer/HTML demo) |
| detail | emitter | viewer (caption) |
| message | emitter (transitions) / heartbeat clears it | sprite (bubble), one display |
| pid | emitter | sprite (farewell) |
| hb | heartbeat | diagnostics |
| ts | always | stale-watchdog (>120s → idle) |

---

## Deploy & Parity

```powershell
# after editing the plugin in the repo:
Copy-Item plugins\kai-presence.js "$env:USERPROFILE\.config\opencode\plugins\" -Force
```

`healthcheck.ps1` compares repo vs deploy MD5 → WARNING if they diverge.
The sprite runs STRAIGHT from the repo (no deployed copy). The VS Code
extension installs via VSIX (see its own README).

## Quick QA

```powershell
node --check plugins\kai-presence.js          # emitter syntax
python -m py_compile scripts\kai_sprite.py    # sprite syntax
# smoke boot (alive for 6s, no sprite-error.log = green):
$p = Start-Process pythonw -ArgumentList "scripts\kai_sprite.py" -PassThru; Start-Sleep 6; $p.HasExited; Stop-Process $p.Id
```

Full end-to-end cycle testing requires restarting opencode (spawn happens on boot).
Sprite regeneration: `make-sprites.py` (cards) + `generate_anim_frames.py`
(animation frames); keying QA: `qa-expressoes.ps1`.

## Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Sprite doesn't appear with opencode | plugin not deployed / python not on PATH | healthcheck (parity); `where pythonw` |
| Two KAIs on screen | impossible due to mutex; if seen, an old zombie process | kill the old pythonw |
| Bubble won't dismiss / repeats | pre-v1.4 sprite version | confirm deploy + restart |
| KAI vanished by herself | farewell: opencode closed/crashed | expected — reopen opencode |
| Label stuck on one state | dead emitter (heartbeat stopped >120s) → auto idle | check plugin log |
| Wrong face for a state (viewer) | negative cache from before TTL era | webview reload (↻) |
