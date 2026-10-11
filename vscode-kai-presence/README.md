# KAI Presence — Extensão VS Code

Presença viva da KAI dentro do VS Code: retrato com aura reativa ao estado real
das sessões opencode (lendo dados / trabalhando / erro / marco / idle).

## Arquitetura

```
opencode → plugins/kai-presence.js → skills/evolving-coder/.kai-presence.json
                                              │ FileSystemWatcher
                                              ▼
        Esta extensão (WebviewView) → kai-presence.html (aura CSS + retrato)
```

## Instalação

### Opção A — empacotar com vsce (recomendado)

```powershell
cd "$env:USERPROFILE\.config\opencode\skills\evolving-coder\vscode-kai-presence"
npx --yes @vscode/vsce package --no-dependencies
```

Gera `kai-presence-0.1.0.vsix`. Instalar no VS Code:

1. Abra a paleta (`Ctrl+Shift+P`) → **Extensions: Install from VSIX...**
2. Selecione o arquivo `.vsix` gerado.

### Opção B — rodar sem instalar (dev)

Abra esta pasta no VS Code e pressione `F5` (Extension Development Host).

## Posicionamento da janela

A view aparece com o ícone de gota na **barra de atividade** (esquerda).
Para deixá-la do lado direito, na sua linha de visão:

- Arraste a view "KAI > Presença" para a **Secondary Side Bar** (`Ctrl+Alt+B`),
  OU arraste a aba para fora e solte para virar **janela flutuante**.

O VS Code memoriza a posição entre sessões.

## Estados

| Estado | Cor | Gatilho |
|--------|-----|---------|
| aguardando | ciano calmo | `session.idle` ou staleness >120s |
| pensando | violeta | partes reasoning/thinking no stream |
| lendo dados | ciano claro | tools read/grep/glob/webfetch/websearch |
| trabalhando | âmbar | tools bash/write/edit/task/skill |
| respondendo | verde-água | partes text no stream |
| erro | vermelho (+shake no sprite) | saída bash com padrão fatal/erro |
| marco | dourado (flash) | clique no sprite (emissor não produz) |
| encerrando | azul-escuro | assinatura "câmbio fechado · sessão encerrada" |

Botão **pausar** congela animações e atualizações (override manual).

## Notas

- Zero rede: watcher de arquivo local + webview local.
- O JSON contém apenas `{state, detail, message, pid, hb, ts}` — nenhum conteúdo sensível.
- `pid` existe para a despedida do sprite; `message` carrega balões transitórios.
