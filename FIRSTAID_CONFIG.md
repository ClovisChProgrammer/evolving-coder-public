# FIRSTAID_CONFIG — Recuperação do OpenCode

> **Uso**: se o OpenCode parar de iniciar com erro de configuração,
> copie o conteúdo de `FIRSTAID_CONFIG.json` para `opencode.json`.

---

## Como usar

### Opção 1 — Renomear (mais rápido)

```powershell
cd ~/.config/opencode
Copy-Item -Force opencode.json opencode.json.bak
Copy-Item -Force skills/evolving-coder/FIRSTAID_CONFIG.json opencode.json
```

### Opção 2 — Copiar manualmente

1. Abra `FIRSTAID_CONFIG.json` no bloco de notas
2. Copie tudo (Ctrl+A, Ctrl+C)
3. Abra `opencode.json` no bloco de notas
4. Cole (Ctrl+V)
5. Salve (Ctrl+S)

---

## Erro conhecido: "Expected PermissionActionConfig"

**Mensagem**:
```
Expected PermissionActionConfig | object | undefined, got [...array...]
```

**Causa**: o campo `permission` estava no formato array:
```json
"permission": [
  {"permission":"edit","pattern":"...","action":"allow"}
]
```

**Formato correto** (objeto com tipos de ferramenta como chaves):
```json
"permission": {
  "edit": "allow",
  "bash": "ask",
  "read": {
    "C:\\Users\\clovi\\.config\\*": "allow"
  }
}
```

**Valores válidos para PermissionActionConfig**: `"ask"`, `"allow"`, `"deny"`

**Tipos de ferramenta suportados**: `read`, `edit`, `glob`, `grep`, `list`, `bash`, `task`, `external_directory`, `todowrite`, `question`, `webfetch`, `websearch`, `lsp`, `doom_loop`, `skill`

---

## Diagnóstico rápido

Se o OpenCode não inicia:

1. **Erro de JSON**: `opencode.json` tem vírgula faltando ou extra
   - Verifique em jsonlint.com
2. **Erro de permission**: copie do FIRSTAID_CONFIG.json (este arquivo)
3. **Erro de plugin**: verifique se `plugins/evolving-coder.js` existe
4. **Erro de model**: verifique se o Ollama está rodando (`ollama list`)

---

## Estado funcional (24/07/2026)

- Plugin: `evolving-coder.js` (injeta SKILL.md 7.2KB via system prompt)
- Model: `ollama/rnj-1` via localhost:11434
- Instructions: `evolving-coder.md`
- Sem campo `permission` (defaults do OpenCode)

---

**Arquivo original**: `~/.config/opencode/opencode.json`
**Backup**: `~/.config/opencode/opencode.json.bak` (criado ao restaurar)
