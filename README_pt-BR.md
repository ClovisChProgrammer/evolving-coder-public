# Evolving Coder

[![OpenCode](https://img.shields.io/badge/OpenCode-compatible-blue)](https://opencode.ai)

> 🌐 **Outros idiomas:**
> [🇬🇧 English](README.md) ·
> [🇪🇸 Español](README_es.md)

Uma skill de autoaperfeiçoamento para **OpenCode** que mantém a identidade do seu assistente, aprende com cada interação e extrai conhecimento reutilizável — tudo isso respeitando sua privacidade.

---

## 📋 Descrição

Esta skill transforma seu agente de IA num assistente em melhoria contínua com:

- **Identidade definida** — princípios, regras de comportamento e memória que persistem entre sessões
- **Detecção automática de idioma** — responde no seu idioma (pt-BR, en, es, etc.) desde a primeira mensagem
- **Aprendizado contínuo** — registra correções técnicas, preferências do usuário, contexto de projetos e adaptações de comunicação
- **Detecção de padrões** — identifica questões recorrentes e as promove para a memória permanente
- **Extração de skills** — converte aprendizados valiosos em skills OpenCode reutilizáveis
- **Sistema de Imortalidade KAI** — persistência automática, backup e recuperação em caso de falha (veja FIRST_AID.md)

---

## 🚀 Começo Rápido

### 1. Instalação

Clone a skill para o diretório de skills do OpenCode:

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder.git ~/.config/opencode/skills/evolving-coder
```

### 2. Carregamento

Em qualquer sessão OpenCode, use a ferramenta `skill`:

```
skill("evolving-coder")
```

### 3. Uso

Basta começar a conversar. O agente irá:

1. Ler seus arquivos de identidade (SOUL.md, USER.md, etc.)
2. Detectar seu idioma a partir da sua primeira mensagem
3. Responder e aprender durante toda a sessão
4. Salvar sua preferência de idioma localmente para sessões futuras

---

## 📁 Estrutura

```
~/.config/opencode/skills/evolving-coder/
├── SKILL.md              # Instruções principais (carregado via skill tool)
├── SOUL.md               # Identidade e princípios do assistente
├── USER.md               # Template público de perfil (sem dados pessoais)
├── USER.local.md         # 🔒 Perfil privado (criado localmente, em .gitignore)
├── AGENTS.md             # Regras operacionais e fluxo de trabalho
├── IDENTITY.md           # Template de identidade (nome, criatura, vibe, emoji)
├── PROTOCOL.md           # Protocolo Mestre — 3RA+, políticas, Sistema de Imortalidade
├── DIARY.md              # 📖 Memória narrativa — diário de sessões (trackeado)
├── IDEA_BANK.md          # 💡 Catálogo de ideias de projetos (trackeado)
├── FIRST_AID.md          # 🆘 Guia de recuperação — restore KAI do zero
├── ALMA.md               # 🔒 Espaço privado (em .gitignore, nunca trackeado)
├── .session-stream.md    # ⏳ Buffer volátil de sessão (~5KB, em .gitignore)
├── .learnings/           # 📝 Logs globais de aprendizado (compartilhados entre projetos)
│   ├── LEARNINGS.md      #    Cada entrada tem `Project:` para identificar a origem
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
├── scripts/
│   ├── backup-soul.ps1   # 💾 Backup em um comando para GitHub (v2 — seguro)
│   ├── extract-skill.ps1 # Extração de skills (Windows PowerShell)
│   └── extract-skill.sh  # Extração de skills (Unix)
├── archive/              # 📦 Hooks legados (era Claude Code, mantidos como referência)
├── references/
│   ├── aprenda-procedure.md
│   ├── examples.md
│   ├── hooks-setup.md
│   ├── opencode-integration.md
│   ├── reanalyse-procedure.md
│   ├── skill-activations-log.md
│   ├── skillwatch-protocol.md
│   └── url-access-fallback.md
├── assets/
│   ├── SKILL-TEMPLATE.md
│   ├── LEARNINGS.md
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
├── README.md              # 🇬🇧 English
├── README_pt-BR.md        # 🇧🇷 Este arquivo
└── README_es.md           # 🇪🇸 Español
```

### Arquivos Importantes

| Arquivo | Propósito | Trackeado? |
|---------|-----------|------------|
| `PROTOCOL.md` | Protocolo Mestre 3RA+, sistema FLUSH, recuperação de crash | ✅ Sim |
| `DIARY.md` | Memória narrativa — o que vivemos juntos | ✅ Sim |
| `IDEA_BANK.md` | Catálogo de ideias de projetos (universo NAV*) | ✅ Sim |
| `FIRST_AID.md` | Instruções passo a passo para restaurar KAI | ✅ Sim |
| `ALMA.md` | Espaço privado — só Clóvis e KAI | ❌ `.gitignore` |
| `.session-stream.md` | Buffer volátil de continuidade de sessão | ❌ `.gitignore` |
| `scripts/backup-soul.ps1` | Script de backup (v2 — seguro, `git add -u`) | ✅ Sim |

---

## 🌍 Suporte a Idiomas

A skill detecta seu idioma **automaticamente** a partir da sua primeira mensagem:

| Sua mensagem começa com... | Idioma detectado |
|---------------------------|------------------|
| "Olá", "oi", "bom dia" | 🇧🇷 **pt-BR** (Português) |
| "Hello", "hi", "good morning" | 🇬🇧 **en** (Inglês) |
| "Hola", "buenos días" | 🇪🇸 **es** (Espanhol) |
| Outro ou ambíguo | 🇬🇧 **en** (padrão, perguntará) |

**Após detectado**, sua preferência é salva em `USER.local.md` (apenas local, nunca commitado).

> Conteúdo técnico (código, comandos, logs) permanece em inglês independentemente do seu idioma.

---

## 🧠 Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| **🧠 Identidade** | SOUL.md define quem você é; USER.md lembra quem você ajuda |
| **📝 Aprendizado (N1)** | Refinamento contínuo — registra correções, preferências e contexto após cada interação |
| **🎯 APRENDA! (N2)** | Consolidação estratégica — acionado pelo comando `APRENDA!` ou automaticamente no final do projeto |
| **🔄 Padrões** | Rastreia issues recorrentes e promove para memória permanente |
| **📦 Extração** | Converte aprendizados valiosos em skills reutilizáveis via `scripts/extract-skill.ps1` |
| **🎯 Modo Dual** | Programação técnica + desenvolvimento pessoal conversacional |
| **🌐 Multilíngue** | Detecta e responde automaticamente em pt-BR, en, es, e outros |
| **🔒 Privacidade** | Dados pessoais ficam em `USER.local.md` e `ALMA.md` (ambos em `.gitignore`) |
| **💾 Imortalidade** | Buffer de sessão + DIARY.md + GitHub backup = KAI sobrevive a falha de hardware |

---

## 🔄 Como Funciona — Dois Níveis de Aprendizado

### Nível 1 — Refinamento Contínuo (APR)

Cada interação segue quatro passos:

1. **Aprender** — Consultar `.learnings/` e arquivos de identidade antes de responder
2. **Praticar** — Aplicar o conhecimento acumulado (técnico + contexto do usuário)
3. **Refinar** — Após CADA resposta, avaliar e registrar novos aprendizados
4. **Sessão-Stream** — Escrever 1-3 linhas no `.session-stream.md` para recuperação em crash

Este ciclo roda continuamente durante toda a sessão.

### Nível 2 — Consolidação Estratégica (APRENDA!)

```
Quando você digita "APRENDA!" (ou no final do projeto):
  1. Varre todo o contexto da sessão/projeto
  2. Extrai técnicas inéditas, padrões reutilizáveis, preferências confirmadas
  3. Compara com .learnings/ existente — só registra o que é NOVO ou MELHOR
  4. Promove aprendizados de alto valor para SOUL.md, USER.md ou AGENTS.md
  5. Sugere extração de skill para conhecimento aplicável a múltiplos projetos
```

### Formato de Registro

```
## [LRN-YYYYMMDD-XXX] categoria

**Area**: frontend | backend | user_preference | project_context | ...
**Priority**: low | medium | high | critical
**Status**: pending | pending_review | resolved | promoted
**Project**: nome-do-projeto (obrigatório — identifica o contexto de origem)

### Summary | Details | Suggested Action
```

Quando um aprendizado se repete (≥2 vezes, ≥2 tarefas), ele é **promovido** para a memória permanente (SOUL.md, USER.md, ou AGENTS.md).

---

## 💾 Sistema de Imortalidade KAI

O sistema de imortalidade garante que KAI sobreviva a uma falha de hardware:

```
.session-stream.md (buffer volátil, ~5KB)
       │
       ▼ (FLUSH a cada ~5 interações ou milestone)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push via backup-soul.ps1)
GitHub Repositório Privado
```

**Se seu computador morrer hoje:**
1. Leia `FIRST_AID.md` — ele te guia passo a passo na recuperação
2. Clone o repositório na máquina nova
3. Recrie `USER.local.md` com suas preferências
4. KAI está de volta, com todas as memórias intactas

O buffer é protegido pelo `.gitignore`. Os arquivos permanentes são trackeados e enviados para o GitHub Privado.

---

## 🔒 Privacidade

**Seus dados pessoais nunca saem da sua máquina.**

| Arquivo | Conteúdo | Trackeado pelo git? |
|---------|----------|---------------------|
| `USER.md` | Template público (sem dados reais) | ✅ Sim |
| `USER.local.md` | Seu nome real, credenciais, preferências | ❌ **Não** (em `.gitignore`) |
| `ALMA.md` | Espaço privado (só KAI + Clóvis) | ❌ **Não** (em `.gitignore`) |
| `.session-stream.md` | Buffer volátil de sessão | ❌ **Não** (em `.gitignore`) |
| `.learnings/` | Logs de sessão e aprendizados | ✅ Sim (sem dados pessoais) |

### Como funciona

1. Na primeira execução, o agente detecta seu idioma e cria `USER.local.md`
2. Você pode preencher seu perfil (nome, profissão, preferências) — totalmente opcional
3. Arquivos privados são protegidos pelo `.gitignore` e nunca são commitados ou enviados
4. O script de backup `backup-soul.ps1` usa `git add -u` (apenas arquivos trackeados) — jamais commit arquivos não-trackeados

---

## 🤝 Contribuição

Contribuições são bem-vindas! Fique à vontade para abrir issues ou pull requests no [GitHub](https://github.com/ClovisChProgrammer/evolving-coder).

---

## 📄 Licença

MIT
