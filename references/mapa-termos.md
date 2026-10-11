# Mapa de Termos — Tradução de Conceitos Externos

> Glossário de tradução para termos/slash-commands citados em conversas. Serve para o assistente
> não alucinar significado, não confundir ferramentas e saber o que já existe nativamente no opencode.
> **NÃO é protocolo** — é conhecimento de referência.

## Tabela-Resumo

| Termo | O que é (tradução) | Origem | Status |
|-------|--------------------|--------|--------|
| **Red Team** | Exercício de segurança: simular adversário real contra o sistema (origem militar → cibersegurança). Em IA: testar limites de modelos (jailbreak, viés, guardrails) | Conceito consolidado (militar → MITRE ATT&CK) | ✅ confirmado |
| **ELI5** | "Explain Like I'm 5": explicar para criança de 5 anos, zero jargão, analogias do cotidiano | Padrão de prompt consolidado | ✅ confirmado |
| **Like 10** | Variação de "Explain Like I'm 10": mesma família ELI5, nível pré-adolescente (acima do ELI5) | Convenção informal | ✅ esclarecido por Clóvis |
| **/code-review --fix** | Claude Code: revisa o diff e APLICA os achados no working tree como mudanças unstaged (nunca commita) | Claude Code (era `/simplify` até v2.1.147; `--fix` desde v2.1.152+, mai/2026) | ✅ confirmado via docs |
| **/connect** | opencode: adicionar provider de LLM + API key no TUI | **opencode nativo** | ✅ confirmado via docs |
| **/init** | opencode: setup guiado para criar/atualizar `AGENTS.md`. (No Claude Code gera `CLAUDE.md` — DIVERGÊNCIA) | opencode nativo / Claude Code | ✅ confirmado via docs |
| **/undo** | opencode: remove última mensagem + respostas + mudanças de arquivo (usa Git). No Claude Code: `/rewind` | **opencode nativo** / Claude Code | ✅ confirmado via docs |
| **/redo** | opencode: refaz mensagem desfeita pelo `/undo` (restaura arquivos). Requer repo Git | **opencode nativo** | ✅ confirmado via docs |

---

## Red Team

### O que é
Simulação de um atacante/adversário real contra um sistema, com o objetivo de encontrar
vulnerabilidades antes que exploradores reais o façam. Origem militar (estratégia de simular o
inimigo); adotado pela cibersegurança formalizado no MITRE ATT&CK.

### Em IA
Red-teaming de modelos = testar jailbreaks, viés, vazamento de contexto, evasão de guardrails,
alucinações perigosas. Prática padronizada da indústria (ex.: testes adversários antes de release).

### Mapeamento no nosso mundo
Já temos: skill `red-team-tactics` (MITRE ATT&CK), `red-team-verifier-patrick-munro`
(verificação adversária de conteúdo legal) e scanners estáticos CodeQL/Semgrep.

## ELI5

### O que é
"Explain Like I'm 5" — explicar um conceito no nível de uma criança de 5 anos: analogias do
cotidiano, zero jargão, frases curtas.

### Família da "escada de profundidade"
ELI5 é o degrau mais baixo de uma escala (ELI5 → adolescente → faculdade → profissional). Padrão
relacionado: Feynman Technique (4 camadas: criança → entusiasta → expert → destilação de 1 frase).

### Mapeamento no nosso mundo
Não temos protocolo próprio de "explicação em camadas". Se Clóvis quiser, vira candidato a skill
(explicação em N níveis ajustáveis).

## Like 10

### O que é
Variação informal de "Explain Like I'm 10" — mesmo espírito do ELI5, porém no nível de um
pré-adolescente (~10 anos): permite um pouco mais de vocabulário e abstração que o ELI5, mas
ainda longe do técnico.

### Nota NC
Não é comando/ferramenta estabelecida; é convenção informal de prompt. Confirmado por Clóvis.

## /code-review --fix

### O que é
Comando do **Claude Code** (v2.1.152+, mai/2026). Revisa o diff (commits à frente do upstream +
mudanças unstaged) e **aplica os achados diretamente no working tree como alterações unstaged** —
nunca commita. Fluxo de 2 passos: identifica → edita.

### Detalhes
- Alvos: número de PR, branch, caminho, ref range.
- Flags: `--comment` (publica inline comments no PR), `--post`.
- Níveis de esforço de busca: low/medium/high/ultra.
- História: antes chamava `/simplify` (aplicava fixes por padrão). `/code-review --fix` substituiu.
- Verificação: usar `git diff` / `git add -p` — o usuário revisa antes de commitar.

### Mapeamento no nosso mundo
Temos equivalente parcial (REVALORE/REFATORE, differential-review), mas sem o "aplicar fixes no
working tree" como comando de 1 passo do Claude Code. Documentar apenas — não implementar por ora.

## /connect

### O que é
Comando **nativo do opencode** (o nosso próprio TUI). Abre seletor para adicionar um provider de
LLM e inserir a API key. Equivalente CLI: `opencode auth login`. Para trocar de modelo depois, `/models`.

### Armadilha de tradução
Em outras ferramentas "/connect" pode significar outra coisa (ex.: conexão remota). No opencode,
é adição de provider. **Não confundir.**

## /init

### O que é
Setup guiado para criar/atualizar o arquivo de regras do projeto.

### DIVERGÊNCIA CRÍTICA
- **opencode**: `/init` gera/atualiza **`AGENTS.md`**.
- **Claude Code**: `/init` gera **`CLAUDE.md`**.
Traduzir com atenção — no nosso ecossistema o alvo é `AGENTS.md`.

## /undo

### O que é
Remove a última mensagem da conversa, todas as respostas subsequentes e as mudanças de arquivo.
**Requer repo Git** (usa Git internamente para reverter). Keybind: `ctrl+x u`.

### Sinônimos
- opencode: `/undo` nativo.
- Claude Code: `/rewind` (aliases `/checkpoint`, `/undo`).

## /redo

### O que é
Refaz um `/undo`. Só disponível após usar `/undo`; restaura também as mudanças de arquivo.
**Requer repo Git.** Keybind: `ctrl+x r`.

### Correção NC registrada
Inicialmente suspeitei que `/redo` não existia no opencode — **errado**. É nativo (docs do TUI
opencode, verificado 2026-09-05). O que não existe é `/redo` como comando de topo no Claude Code.

---

## Proveniência

| Fonte | Data |
|-------|------|
| Docs do opencode TUI (https://opencode.ai/docs/tui/) — comandos `/connect`, `/init`, `/undo`, `/redo` | 2026-09-05 |
| Docs do Claude Code — `/code-review --fix`, `/rewind`, `/init` | 2026-09-05 |
| Clóvis (esclarecimento manual) — "Like 10" | 2026-09-05 |
| Websearch — Red Team/ELI5/escada de profundidade (Feynman) | 2026-09-05 |

## NC Dicionário

- Tudo na tabela-resumo está **confirmado** (docs ou esclarecimento do usuário). Nada de "suspeito sem confirmar".
- Se um termo novo aparecer sem origem conhecida: **perguntar** antes de afirmar o significado (postura NC).