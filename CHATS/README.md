# CHATS/ — Módulo de Transcrições de Sessão

> **Esta instância pública do repositório vem com esta pasta VAZIA de propósito.**
> Transcrições de sessão contêm diálogo pessoal e íntimo entre o SPA e o SPD,
> e por isso vivem apenas no repositório PRIVADO do sistema.

## O que é

Convenção global (21/08/2026): toda sessão evolving-coder pode gerar uma transcrição fiel em Markdown, arquivada com data, duração e descritor do projeto.

## Como funciona

1. **Export nativo** do OpenCode executado via Python subprocess (preserva UTF-8):

```python
import subprocess, json
EXE = r"C:\Users\<voce>\AppData\Roaming\npm\node_modules\opencode-ai\bin\opencode.exe"
raw = subprocess.run([EXE, "export", "<sessionID>"], capture_output=True, timeout=120).stdout
d = json.loads(raw.decode("utf-8"))
```

⚠️ Nunca use redirect `>` do PowerShell 5.1 para capturar o export — ele corrompe UTF-8 (dupla codificação).

2. **Conversor**: ajuste `SID` e `OUT` em `convert_session.py` e execute com qualquer Python 3.10+. Saída: `YYYY-MM-DD_<slug-da-sessao>_<descritor>.md` com cabeçalho (participantes, sistema, início/fim em BRT, duração), diálogos verbatim (👤 SPA / 🔧 SPD), tool calls como resumo de 1 linha e estatísticas finais.

3. **Sync**: as transcrições geradas na SUA instalação devem ir para o seu repo privado. Este módulo público entrega apenas a ferramenta.

## Estrutura esperada

```
CHATS/
├── README.md            ← este arquivo
├── convert_session.py   ← conversor reutilizável
└── *.md                 ← transcrições (privado; vazio aqui)
```
