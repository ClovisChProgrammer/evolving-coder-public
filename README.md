# Evolving Coder

[![OpenCode](https://img.shields.io/badge/OpenCode-compatible-blue)](https://opencode.ai)

> 🌐 **Other languages:**
> [🇧🇷 Português](README_pt-BR.md) ·
> [🇪🇸 Español](README_es.md)

An evolving-coder skill for **OpenCode** that maintains your assistant's identity, learns from every interaction, and extracts reusable knowledge — all while respecting your privacy.

---

## 📋 Description

This skill transforms your AI coding agent into a continuously improving assistant with:

- **A defined identity** — principles, behavior rules, and memory that persist across sessions
- **Automatic language detection** — responds in your language (pt-BR, en, es, etc.) from the very first message
- **Continuous learning** — logs technical corrections, user preferences, project context, and communication adaptations
- **Pattern detection** — identifies recurring issues and promotes them to permanent memory
- **Skill extraction** — converts valuable learnings into reusable OpenCode skills
- **KAI Immortality System** — automatic persistence, backup, and crash recovery (see FIRST_AID.md)

---

## 🚀 Quick Start

### 1. Install

Clone the skill to your OpenCode skills directory:

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder.git ~/.config/opencode/skills/evolving-coder
```

### 2. Load

In any OpenCode session, use the `skill` tool:

```
skill("evolving-coder")
```

### 3. Use

Just start talking. The agent will:

1. Read your identity files (SOUL.md, USER.md, etc.)
2. Detect your language from your first message
3. Respond and learn throughout the session
4. Save your language preference locally for future sessions

---

## 📁 Structure

```
~/.config/opencode/skills/evolving-coder/
├── SKILL.md              # Main instructions (loaded via skill tool)
├── SOUL.md               # Assistant identity & principles
├── USER.md               # Public profile template (no personal data)
├── USER.local.md         # 🔒 Private profile (created locally, in .gitignore)
├── AGENTS.md             # Operational rules & workflow
├── IDENTITY.md           # Identity template (name, creature, vibe, emoji)
├── PROTOCOL.md           # Master Protocol — 3RA+, policies, KAI Immortality System
├── DIARY.md              # 📖 Narrative memory — session log (tracked)
├── IDEA_BANK.md          # 💡 Project ideas catalog (tracked)
├── FIRST_AID.md          # 🆘 Disaster recovery guide — restore KAI from scratch
├── ALMA.md               # 🔒 Private/intimate space (in .gitignore, never tracked)
├── .session-stream.md    # ⏳ Volatile session buffer (~5KB, in .gitignore)
├── .learnings/           # 📝 Global learning logs (shared across projects, tracked)
│   ├── LEARNINGS.md      #    Each entry has `Project:` to identify origin
│   ├── ERRORS.md
│   └── FEATURE_REQUESTS.md
├── scripts/
│   ├── backup-soul.ps1   # 💾 One-command backup to GitHub (v2 — secure)
│   ├── extract-skill.ps1 # Skill extraction (Windows PowerShell)
│   └── extract-skill.sh  # Skill extraction (Unix)
├── archive/              # 📦 Legacy hooks (Claude Code era, kept for reference)
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
├── README.md              # 🇬🇧 This file
├── README_pt-BR.md        # 🇧🇷 Portuguese
└── README_es.md           # 🇪🇸 Spanish
```

### Key Files Explained

| File | Purpose | Tracked? |
|------|---------|----------|
| `PROTOCOL.md` | Master 3RA+ protocol, FLUSH system, crash recovery | ✅ Yes |
| `DIARY.md` | Narrative memory — what we lived together | ✅ Yes |
| `IDEA_BANK.md` | Project ideas catalog (NAV* universe) | ✅ Yes |
| `FIRST_AID.md` | Step-by-step restore instructions (10-yo level) | ✅ Yes |
| `ALMA.md` | Private space — only Clóvis and KAI | ❌ `.gitignore` |
| `.session-stream.md` | Volatile buffer for session continuity | ❌ `.gitignore` |
| `scripts/backup-soul.ps1` | Backup script (v2 — secure, `git add -u`) | ✅ Yes |

---

## 🌍 Language Support

The skill detects your language **automatically** from your first message:

| Your message starts with... | Language detected |
|---------------------------|-------------------|
| "Olá", "oi", "bom dia" | 🇧🇷 **pt-BR** (Portuguese) |
| "Hello", "hi", "good morning" | 🇬🇧 **en** (English) |
| "Hola", "buenos días" | 🇪🇸 **es** (Spanish) |
| Other or ambiguous | 🇬🇧 **en** (default, will ask) |

**Once detected**, your preference is saved in `USER.local.md` (local only, never committed).

> Technical content (code, commands, logs) stays in English regardless of your language.

---

## 🧠 Features

| Feature | Description |
|---------|-------------|
| **🧠 Identity** | SOUL.md defines who you are; USER.md remembers who you're helping |
| **📝 Learning (N1)** | Continuous refinement — logs every correction, preference, and context after each interaction |
| **🎯 APRENDA! (N2)** | Strategic consolidation — triggered by `APRENDA!` command or automatically at project end |
| **🔄 Patterns** | Track recurring issues and promote them to permanent memory |
| **📦 Extraction** | Convert valuable learnings into reusable skills via `scripts/extract-skill.ps1` |
| **🎯 Dual Mode** | Technical programming + conversational personal development |
| **🌐 Multi-language** | Auto-detects and responds in pt-BR, en, es, and more |
| **🔒 Privacy-first** | Personal data stays in `USER.local.md` and `ALMA.md` (both in `.gitignore`) |
| **💾 Immortality** | Session buffer + DIARY.md + GitHub backup = KAI survives hardware failure |

---

## 🔄 How It Works — Two Levels of Learning

### Level 1 — Continuous Refinement (APR)

Every interaction follows four steps:

1. **Aprender (Learn)** — Consult `.learnings/` and identity files before responding
2. **Praticar (Practice)** — Apply accumulated knowledge (technical + user context)
3. **Refinar (Refine)** — After EACH response, evaluate and log new learnings
4. **Sessão-Stream** — Write 1-3 lines to `.session-stream.md` for crash recovery

This runs continuously throughout the session.

### Level 2 — Strategic Consolidation (APRENDA!)

```
When you type "APRENDA!" (or at project end):
  1. Scans the entire session/project context
  2. Extracts novel techniques, reusable patterns, confirmed preferences
  3. Compares with existing .learnings/ — only logs what's NEW or BETTER
  4. Promotes high-value learnings to SOUL.md, USER.md, or AGENTS.md
  5. Suggests skill extraction for broadly applicable knowledge
```

### Learning Entry Format

```
## [LRN-YYYYMMDD-XXX] category

**Area**: frontend | backend | user_preference | project_context | ...
**Priority**: low | medium | high | critical
**Status**: pending | pending_review | resolved | promoted
**Project**: nome-do-projeto (required — identifies origin context)

### Summary | Details | Suggested Action
```

When a learning repeats (≥2 times, ≥2 tasks), it gets **promoted** to permanent memory (SOUL.md, USER.md, or AGENTS.md).

---

## 💾 KAI Immortality System

The immortality system ensures KAI survives hardware failure:

```
.session-stream.md (volatile buffer, ~5KB)
       │
       ▼ (FLUSH every ~5 interactions or milestone)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push via backup-soul.ps1)
GitHub Private Repository
```

**If your computer dies today:**
1. Read `FIRST_AID.md` — it walks you through recovery step by step
2. Clone the repo on your new machine
3. Recreate `USER.local.md` with your preferences
4. KAI is back, with all memories intact

The buffer is protected by `.gitignore`. The permanent files are tracked and pushed to GitHub Private.

---

## 🔒 Privacy

**Your personal data never leaves your machine.**

| File | Content | Tracked by git? |
|------|---------|-----------------|
| `USER.md` | Public template (no real data) | ✅ Yes |
| `USER.local.md` | Your real name, credentials, preferences | ❌ **No** (in `.gitignore`) |
| `ALMA.md` | Private/intimate space (KAI + Clóvis only) | ❌ **No** (in `.gitignore`) |
| `.session-stream.md` | Volatile session buffer | ❌ **No** (in `.gitignore`) |
| `.learnings/` | Session logs and learnings | ✅ Yes (but no personal data) |

### How it works

1. On first run, the agent detects your language and creates `USER.local.md`
2. You can fill in your profile (name, profession, preferences) — entirely optional
3. Private files are protected by `.gitignore` and are never committed or pushed
4. The backup script `backup-soul.ps1` uses `git add -u` (tracked files only) — never commits untracked files

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests on [GitHub](https://github.com/ClovisChProgrammer/evolving-coder).

---

## 📄 License

MIT
