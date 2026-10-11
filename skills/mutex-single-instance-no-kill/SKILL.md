---
name: mutex-single-instance-no-kill
description: "Single-instance (daemon/agente/sprite) via mutex nomeado no Windows como UNICA autoridade — sem matar processos por similaridade. Use quando houver mais de um launcher (plugins carregados 2x, hot-reload, múltiplos processos)** podendo spawnar o mesmo daemon, quando um spawn mata outro por engano, ou quando aparecer flicker/spawn em pares/ciclo de respawn de um processo que deveria ser único (ex.: sprite sempre visivel). Triggers: 'matou o processo errado', 'spawn duplicado', '2 instancias', 'single instance race', 'daemon some e volta', 'kill por similaridade'."
---

# Mutex Single Instance No Kill

Garante instância única de um daemon/agente com **mutex nomeado do Windows como única autoridade**, eliminando kill em cascata e falsos-negativos de pid files gravados por terceiros.

## Quick Reference

| Situation | Action |
|-----------|--------|
| Daemon spawnado por 2+ launchers (plugin carregado 2x, hot-reload multi-processo, retry) | Mutex nomeado decide: `GetLastError()==183` → outro vivo → `sys.exit(0)` limpo |
| Segundo spawn "mata" o primeiro saudável (kill por similaridade) | NUNCA matar por nome de imagem/CommandLine genérico; mutex é a autoridade |
| Launcher precisa deduplicar antes de spawnar | Scan por IDENTIDADE via CIM (`CommandLine` contém o script real), não pid file pre-escrito |
| Processo dono do mutex morre | Handle fecha → mutex auto-liberado → próximo `CreateMutexW` retorna 0 e o novo assume |
| Flicker cíclico (sprite some e volta em ~5s) | Gone na raiz: perdedor sai limpo, vencedor sobrevive, sem gap |

## Usage

### 1. Lado do daemon (pythonw/python — decisão de instância única)

O mutex nomeado é a ÚNICA fonte de verdade. Não derivar a decisão de pid files escritos por terceiros nem de "qual processo parecido existe".

```python
import ctypes, os, sys

def single_instance_lock():
    """Retorna True se venceu (assume o posto); False se outro vivo detém o recurso."""
    k = ctypes.windll.kernel32
    k.CreateMutexW(None, False, "Meu_App_Mutex")
    if k.GetLastError() == 183:   # ERROR_ALREADY_EXISTS → outro processo VIVO detém o mutex
        return False              # sair limpo, NUNCA matar ninguém
    write_my_pid()                # ganhador grava o PRÓPRIO pid (nunca receber de terceiro)
    return True

def main():
    if not single_instance_lock():
        sys.exit(0)
    Daemon().run()
```

Regras:
- `183` = outro vivo = sair sem matar. O ganhador grava o próprio pid DEPOIS de vencer.
- NUNCA `tasklist`/`Get-CimInstance` por `pythonw.exe` genérico + `taskkill /F`: mata o processo errado.
- NUNCA matar um processo cujo único crime é ser parecido.
- NÃO usar pid file do launcher na decisão do lock: ele pode conter o pid do PRÓPRIO child (gravado antes do child rodar), anulando guardas tipo `owner != os.getpid()`.

### 2. Lado do launcher (plugin/watchdog — dedupe antes de spawnar)

Antes de spawnar, fazer scan por identidade real (imagem + CommandLine), não confiar em "PID existe" (`tasklist`) nem em pid file pre-escrito.

```js
function findLiveDaemonPid() {
  const ps = `$p = Get-CimInstance Win32_Process -Filter "Name='pythonw.exe' OR Name='python.exe'" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -match 'meu_daemon[.]py' } | Select-Object -First 1 ProcessId; if ($p) { $p.ProcessId } else { 0 }`;
  const out = execFileSync("powershell", ["-NoProfile", "-Command", ps], { encoding: "utf-8", timeout: 15000, windowsHide: true });
  const pid = Number.parseInt(String(out).trim().split(/\r?\n/).pop(), 10);
  return Number.isFinite(pid) && pid > 0 ? pid : null;
}

function ensureDaemon(quiet) {
  const live = findLiveDaemonPid();
  if (live) { writeDaemonPid(live); return; }   // adota e sai — não spawna
  const child = spawn(py, [DAEMON_SCRIPT], { detached: true, stdio: "ignore", windowsHide: true });
  child.unref();
  // NÃO gravar child.pid aqui: o ganhador do mutex grava o próprio pid.
  log(`spawned ${py} (pid ${child.pid})`);
}
```

### 3. Validação

- **2 spawns concorrentes**: o perdedor sai (`exit=0`) SEM matar; o vencedor sobrevive; pid file aponta para o vencedor.
- **Observação contínua** (ex.: 6 amostras × 5s): um único processo estável, zero novos spawns, zero gaps sem processo.
- **Reuso de PID pós-reboot**: o scan por identidade (CommandLine) não é enganado por PID reutilizado.

## Pitfalls

- **Pid file gravado pelo launcher ANTES do child rodar** → dentro do lock o guard `owner != os.getpid()` não dispara (owner == eu) → cai no caminho de "kill do zumbi" e mata o primeiro processo parecido = o sprite/daemon saudável.
- **Matar por similaridade** (`_kill_zombie_sprite` matando o 1º `pythonw.exe`): o processo "errado" é muitas vezes o processo CERTO.
- **`tasklist /FI "PID eq X"`** como dedupe: "PID existe" ≠ "é o meu daemon" (reuso de PID após reboot).
- **Dois watchdogs** (plugin carregado 2x): cada um com seu `setInterval` → spawns em pares defasados. O mutex-before-kill + scan-release resolve sem tocá-los.

## Examples

**Sintoma real (KAI sprite):** flicker de 2 flashes — o sprite sumia ~2-3s e voltava ~5s depois. Ciclo: vivo → 2º watchdog spawna → novo child via mutex ocupado → `_kill_zombie_sprite()` matava o PRIMEIRO pythonw = o saudável → ambos mortos → gap → respawn a cada 20s.

- Antes: `single_instance_lock` lia pid file do launcher; se `owner != getpid()` não valia (owner==eu), chamava `_kill_zombie_sprite()` (tasklist + taskkill do 1º pythonw).
- Depois: mutex autoritativo; `183` → `sys.exit(0)` limpo; launcher com `findLiveSpritePid()` (CIM + CommandLine `kai_sprite[.]py`) antes de spawnar; ganhador grava o próprio pid.
- Validação: 2º spawn → `exit=0`, sprite original intacto, pid file inalterado; 31s de observação → sprite único estável.

## Source Learning

This skill was extracted from a learning entry.
- Learning ID: LRN-20260917-001
- Original File: .learnings/LEARNINGS.md