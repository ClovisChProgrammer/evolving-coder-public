const vscode = require("vscode");
const fs = require("fs");
const path = require("path");
const os = require("os");
const { execSync, spawn } = require("child_process");

const SKILL_DIR = path.join(
  process.env.USERPROFILE || path.join(os.homedir(), ".config"),
  "opencode", "skills", "evolving-coder"
);
const PRESENCE_FILE = path.join(SKILL_DIR, ".kai-presence.json");
const HTML_FILE = path.join(SKILL_DIR, "assets", "kai-presence", "kai-presence.html");
const SPRITE_SCRIPT = path.join(SKILL_DIR, "scripts", "kai_sprite.py");

function findSpritePid() {
  try {
    const tmpPs = path.join(os.tmpdir(), "kai-find-sprite.ps1");
    fs.writeFileSync(tmpPs, `Get-CimInstance Win32_Process -Filter "Name='pythonw.exe'" | Where-Object { $_.CommandLine -match 'kai_sprite' } | ForEach-Object { $_.ProcessId }`, "utf-8");
    const out = execSync(`powershell -NoProfile -ExecutionPolicy Bypass -File "${tmpPs}"`, { encoding: "utf-8", timeout: 5000 }).trim();
    if (out) {
      const pid = parseInt(out.split(/\r?\n/)[0].trim());
      if (pid > 0) return pid;
    }
  } catch { /* silent */ }
  return null;
}

function findPython() {
  for (const cmd of ["pythonw", "python"]) {
    try {
      const out = execSync(`where ${cmd}`, { encoding: "utf-8", timeout: 3000 });
      const first = out.split(/\r?\n/).map(s => s.trim()).find(Boolean);
      if (first) return first;
    } catch { /* not found */ }
  }
  return null;
}

function startSprite() {
  const pid = findSpritePid();
  if (pid) {
    vscode.window.showInformationMessage(`KAI Sprite já está rodando (PID: ${pid})`);
    return pid;
  }
  const py = findPython();
  if (!py) {
    vscode.window.showErrorMessage("KAI: Python não encontrado no PATH");
    return null;
  }
  try {
    const child = spawn(py, [SPRITE_SCRIPT], { detached: true, stdio: "ignore", windowsHide: true });
    child.unref();
    vscode.window.showInformationMessage(`KAI Sprite iniciado (PID: ${child.pid})`);
    return child.pid;
  } catch (e) {
    vscode.window.showErrorMessage(`KAI: Falha ao iniciar sprite — ${e.message}`);
    return null;
  }
}

function stopSprite() {
  const pid = findSpritePid();
  if (!pid) {
    vscode.window.showInformationMessage("KAI Sprite não está rodando");
    return;
  }
  try {
    execSync(`taskkill /F /PID ${pid}`, { stdio: "ignore", timeout: 5000 });
    vscode.window.showInformationMessage(`KAI Sprite encerrado (PID: ${pid})`);
  } catch (e) {
    vscode.window.showErrorMessage(`KAI: Falha ao encerrar sprite — ${e.message}`);
  }
}

function toggleSprite() {
  const pid = findSpritePid();
  if (pid) {
    stopSprite();
  } else {
    startSprite();
  }
}

class KaiViewProvider {
  constructor(context) {
    this.context = context;
    this.view = undefined;
  }

  resolveWebviewView(view) {
    this.view = view;
    view.webview.options = {
      enableScripts: true,
      localResourceRoots: [vscode.Uri.file(SKILL_DIR)]
    };
    view.webview.onDidReceiveMessage(msg => {
      if (msg.type === "ready") this.pushState();
      else if (msg.type === "kai-reload") this.rebuild();
    });

    const watcher = vscode.workspace.createFileSystemWatcher(
      new vscode.RelativePattern(vscode.Uri.file(SKILL_DIR), ".kai-presence.json")
    );
    const onChange = () => this.pushState();
    watcher.onDidChange(onChange);
    watcher.onDidCreate(onChange);
    this.context.subscriptions.push(watcher);

    view.webview.html = this.buildHtml();
    setTimeout(() => this.pushState(), 600);
  }

  pushState() {
    if (!this.view) return;
    try {
      if (!fs.existsSync(PRESENCE_FILE)) return;
      const raw = fs.readFileSync(PRESENCE_FILE, "utf-8");
      const payload = JSON.parse(raw);
      this.view.webview.postMessage({ type: "kai-presence", payload });
    } catch (e) {
      console.error("KAI Presence:", e.message);
    }
  }

  buildHtml() {
    let html = fs.readFileSync(HTML_FILE, "utf-8");
    const baseUri = this.view.webview.asWebviewUri(
      vscode.Uri.file(path.join(SKILL_DIR, "assets", "kai-presence"))
    ).toString();
    html = html.replace("<head>", `<head>\n<base href="${baseUri}/">`);
    return html;
  }

  rebuild() {
    if (!this.view) return;
    this.view.webview.html = this.buildHtml();
    setTimeout(() => this.pushState(), 400);
  }
}

function activate(context) {
  const provider = new KaiViewProvider(context);
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider("kaiPresence.view", provider),
    vscode.commands.registerCommand("kaiPresence.reload", () => provider.rebuild()),
    vscode.commands.registerCommand("kaiPresence.startSprite", () => startSprite()),
    vscode.commands.registerCommand("kaiPresence.stopSprite", () => stopSprite()),
    vscode.commands.registerCommand("kaiPresence.toggleSprite", () => toggleSprite())
  );
}

function deactivate() {}

module.exports = { activate, deactivate };
