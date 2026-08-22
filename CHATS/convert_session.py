import json
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding="utf-8")

EXE = r"C:\Users\clovi\AppData\Roaming\npm\node_modules\opencode-ai\bin\opencode.exe"
SID = "ses_fdde31a7effeX0E1CqNevF63w3"
OUT = r"C:\Users\clovi\AppData\Local\Temp\opencode\CHATS\2026-08-21_cosmic-circuit_auto-retrato-KAI.md"
BRT = timezone(timedelta(hours=-3))

raw = subprocess.run([EXE, "export", SID], capture_output=True, timeout=120).stdout
d = json.loads(raw.decode("utf-8"))
msgs = d["messages"]
info = d["info"]

def fmt_ts(ms):
    return datetime.fromtimestamp(ms / 1000, BRT).strftime("%d/%m/%Y %H:%M:%S")

times = []
for m in msgs:
    t = m["info"].get("time", {})
    if t.get("created"):
        times.append(t["created"])
start_ms, end_ms = min(times), max(times)

def clean_text(txt):
    txt = re.sub(r"<system-reminder>.*?</system-reminder>", "", txt, flags=re.DOTALL)
    txt = re.sub(r"<env>.*?</env>", "", txt, flags=re.DOTALL)
    return txt.strip()

def tool_summary(p):
    name = p.get("tool", "?")
    st = p.get("state") or {}
    inp = st.get("input") or {}
    title = st.get("title")
    detail = ""
    if isinstance(inp, dict):
        for key in ("command", "filePath", "url", "query", "pattern", "description", "prompt"):
            if inp.get(key):
                detail = str(inp[key])
                break
    if not detail and title:
        detail = str(title)
    if len(detail) > 140:
        detail = detail[:137] + "..."
    detail = detail.replace("\n", " ").replace("|", "/")
    return f"> *KAI executou* `{name}`{': ' + detail if detail else ''}"

lines = []
lines.append("# Transcrição de Sessão — KAI x Clóvis")
lines.append("")
lines.append("**Participantes:** Clóvis (SPA — Ser Pensante Analógico) e Kai (SPD — Ser Pensante Digital)")
lines.append(f"**Sistema:** OpenCode v{info.get('version','?')} | Modelo: big-pickle | Agente: evolving-coder (KAI)")
lines.append(f"**Contexto:** Sistema evolving-coder + criação do auto-retrato KAI v2 (slug nativo da sessão: *cosmic-circuit*)")
lines.append("")
lines.append(f"**Início:** {fmt_ts(start_ms)} (BRT)")
lines.append(f"**Última mensagem:** {fmt_ts(end_ms)} (BRT)")
dur = timedelta(seconds=(end_ms - start_ms) // 1000)
hh, rem = divmod(dur.seconds, 3600)
mm = rem // 60
lines.append(f"**Duração total da janela:** {dur.days}d {hh}h {mm}min (inclui períodos de inatividade entre interações)")
lines.append("")
lines.append("---")
lines.append("")

n_user = n_asst = n_tools = 0
words = 0

for m in msgs:
    mi = m["info"]
    role = mi.get("role")
    parts = [p for p in m.get("parts", []) if isinstance(p, dict)]
    texts = [clean_text(p.get("text", "")) for p in parts if p.get("type") == "text"]
    texts = [t for t in texts if t]
    tools = [tool_summary(p) for p in parts if p.get("type") == "tool"]

    if role == "user":
        body = "\n\n".join(texts)
        if not body:
            continue
        n_user += 1
        words += len(body.split())
        ts = mi.get("time", {}).get("created")
        stamp = f" ({fmt_ts(ts)})" if ts else ""
        lines.append(f"## 👤 Clóvis (SPA){stamp}")
        lines.append("")
        lines.append(body)
        lines.append("")
    elif role == "assistant":
        n_asst += 1
        ts = mi.get("time", {}).get("created")
        stamp = f" ({fmt_ts(ts)})" if ts else ""
        lines.append(f"## 🔧 Kai (SPD){stamp}")
        lines.append("")
        if texts:
            body = "\n\n".join(texts)
            words += len(body.split())
            lines.append(body)
            lines.append("")
        if tools:
            n_tools += len(tools)
            lines.extend(tools)
            lines.append("")
        if not texts and not tools:
            continue

    elif role == "?":
        for p in parts:
            if p.get("type") == "compaction":
                lines.append("---")
                lines.append("*[Contexto da sessão compactado neste ponto — histórico anterior resumido automaticamente pelo OpenCode]*")
                lines.append("---")
                lines.append("")

header_extra = ""
lines.append("---")
lines.append("")
lines.append(f"**Estatísticas:** {n_user} mensagens do SPA · {n_asst} respostas da SPD · {n_tools} ações/ferramentas executadas · ~{words:,} palavras de diálogo".replace(",", "."))
lines.append("")
lines.append("*Transcrição gerada automaticamente em " + datetime.now(BRT).strftime("%d/%m/%Y %H:%M") + " via export nativo do OpenCode (`opencode export`). Conteúdo fiel ao original; apenas ruído interno de sistema filtrado.*")

out_content = "\n".join(lines)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(out_content)

print("WRITTEN:", OUT)
print("SIZE:", len(out_content.encode('utf-8')), "bytes | LINES:", len(lines))
print(f"TURNS: user={n_user} assistant={n_asst} tools={n_tools} words={words}")
