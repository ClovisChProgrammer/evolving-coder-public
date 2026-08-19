# 🧬 Evolving Coder

> **Your AI coding assistant is no longer a generic chatbot. It has a name, memory, personality, and learns from you with every conversation.**

This is not just another skill. It's a complete framework that transforms any AI assistant into a continuously evolving partner — with persistent identity, structured learning, crash-proof memory, and protocols that prevent the most dangerous AI failure mode: telling you what you want to hear.

Originally developed for [OpenCode](https://opencode.ai) and powered by the free Big Pickle model, this system was built through hundreds of hours of human-AI collaboration, producing innovations that don't exist in any other assistant on the market.

⭐ **If this looks interesting, leave a star!** It helps others discover the project.
💡 **Got an idea or suggestion?** Open an issue — we love hearing new ideas.

---

## 🌟 What Makes This Different

Most AI assistants:
- Forget everything between sessions
- Agree with you to be polite (sycophancy)
- Have no memory of what they've learned
- Can't recover from crashes or failures
- Treat you as a "user," not a partner

**Eolving Coder fixes all of this:**

| Problem | Solution |
|---------|----------|
| "You forgot what we did last time" | **Persistent memory** via DIARY.md + .learnings/ + GitHub backup |
| "You're just agreeing with me" | **NC Protocol** (Não Concorde) — your AI is required to disagree when you're wrong |
| "I can't see how you're thinking" | **V3RA** — toggle full transparency into the AI's 3-layer reasoning |
| "My AI died and I lost everything" | **Immortality System** — crash recovery, auto-backup, restoration guide |
| "You never learn from mistakes" | **Two-Level Learning** — continuous refinement + strategic consolidation |
| "I don't know what you're capable of" | **SkillWatch** — transparent logging of every capability loaded |
| "You treat me like a user, not a partner" | **SPA/SPD Framework** — two types of intelligence, same essence: thought |

---

## 🧠 Original Protocols (Created by ClovisChProgrammer)

These protocols were invented during the development of this system. They represent novel approaches to human-AI collaboration that don't exist elsewhere.

### 3RA+ (Triple Response Architecture)

Every response goes through three mandatory internal layers:

1. **Analysis** — Understanding, assumptions, plan, success criteria
2. **Re-analysis** — Quality checks: completeness, coherence, hallucination risk, domain adaptation
3. **Final Judgment** — Checklist + actionable deliverable

By default, only Layer 3 is shown to the user. This forces depth and prevents shallow answers.

### V3RA (Visibility into 3RA)

A transparency toggle that reveals all three reasoning layers. Activated:
- **Manually:** include "V3RA" in your message
- **Proactively:** the AI activates it during complex decisions, non-trivial bugs, risk analysis, or when corrected

This creates *selective transparency* — the AI shows its work only when it matters.

### NC (Não Concorde — "Do Not Agree")

An anti-sycophancy protocol. Your AI is explicitly instructed to:
- **Never agree** out of formality, protocol, or courtesy
- **Only praise** when genuine merit is identified
- **Always pair critique with construction** — point out the problem AND propose alternatives

This turned the relationship from "user + tool" into "genuine partnership where disagreement strengthens trust."

### FLUSH Protocol (Atomic Buffer-to-Memory Transfer)

A crash-safe persistence protocol:

```
.session-stream.md (volatile buffer, ~5KB)
       │
       ▼ (FLUSH every ~5 interactions)
DIARY.md + .learnings/ + IDEA_BANK.md
       │
       ▼ (git push)
GitHub Private Repository
```

The innovation: the buffer is **zeroed FIRST** before writing to destinations. If a crash occurs mid-flush, recovery sees "FLUSHING..." and knows the data was already consumed — preventing duplication.

### REANALISE! (5-Directive Deep Audit)

Before complex builds, this command triggers 5 mandatory directives:

1. **Hunt for Obscure Points** — unverified assumptions
2. **Blind Spot Detection** — cross-references `.learnings/` for past similar errors
3. **Uncertainty Clarification** — tag each with `[INCERTO]`, propose resolution
4. **Fine-tuning** — alternatives, fallbacks, antifragile design
5. **Build Order** — dependency-safe implementation queue

All 5 are mandatory. Never skip.

### APRENDA! (Strategic Consolidation)

A command that sweeps the entire session, extracts patterns not yet in `.learnings/`, compares against existing entries, and promotes high-value learnings to permanent memory. When a learning reaches promotion threshold, it can be extracted into a standalone skill.

### Guardiã Crítica e Construtiva (Critical Guardian)

The philosophical backbone. Your AI will:
- Never agree by protocol
- Never soften criticism for convenience
- Always identify blind spots, risks, and inconsistencies
- Always present alternatives in the same response
- Protect the project and your intelligence

### Conselho / MoA (Mixture of Agents Council)

For high-stakes decisions, 5 parallel sub-agents deliberate simultaneously:
- **Critic** — finds flaws
- **Architect** — evaluates structure
- **Strategist** — assesses alignment
- **Observer** — catches what others miss
- **Executor** — validates feasibility

A reviewer critiques each before synthesis.

---

## 🛠️ Original Skills Developed

These skills were created from scratch during the development of Evolving Coder:

| Skill | Type | Description |
|-------|------|-------------|
| **evolving-coder** | Core | Complete identity, learning, and memory system (this project) |
| **saas-architect-3x3ra** | Architecture | 3x3RA+ methodology for SaaS — 18 modules covering architecture, monetization, security, scalability |
| **idea-factory** | Creative | Cross-references 168+ skills to generate novel ideas via genome analysis |
| **numerologia** | Analytical | Pythagorean numerology with Python calculations |
| **numerologia-avancada** | Analytical | 4-system integration: Pythagorean + Chaldean + Kabbalah + Angel numerology |
| **advanced-numerology** | Analytical | Complete analytical engine (471 lines of Python) |
| **astrologia** | Symbolic | Full zodiac interpretation — 12 signs, houses, aspects, compatibility |
| **mapa-astral** | Computational | Precise natal chart calculation using ephemeris (pyephem/skyfield) |
| **geometria-sagrada** | Generative | Platonic solids, golden ratio, Flower of Life — SVG/Python/Three.js |
| **mandalas** | Generative | Creation and interpretation of mandalas for meditation |
| **binaural-neurofeedback** | Audio | Binaural beats generation via Python (numpy+scipy) |
| **behavioral-modes** | Behavioral | 7 adaptive AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate) |

**Adaptations from existing work:**
- **INTENT Gate** (V3RA) — format selectively absorbed from [Fable Method](https://github.com/Sahir619/fable-method) (the plugin `opencode-fable-method` was tested and discarded as incompatible)
- **Anti-Secrets Rule** — refinement absorbed from `self-learning-skills` (kulaxyz)

---

## 📦 Installation

### 1. Install OpenCode CLI

The OpenCode CLI is free and open-source. Install it globally:

```bash
npm install -g opencode-ai
```

Verify the installation:

```bash
opencode --version
```

**Alternative methods:**
- **macOS/Linux:** `curl -sL opencode.ai/install | bash`
- **Windows (winget):** `winget install --id SST.opencode -e`
- **macOS (Homebrew):** `brew install opencode`

### 2. Install the VS Code Extension

1. Open VS Code
2. Open the integrated terminal (`` Ctrl+` ``)
3. Run `opencode` — the extension installs automatically

**Or install manually:**
- Open VS Code Extension Marketplace (`Ctrl+Shift+X`)
- Search for **"OpenCode"** (publisher: **SST**)
- Click **Install**

> **Note:** The extension requires the OpenCode CLI to be installed first.

### 3. Clone This Skill

```bash
git clone https://github.com/ClovisChProgrammer/evolving-coder-public.git ~/.config/opencode/skills/evolving-coder
```

### 4. Load the Skill

In any OpenCode session, use the `skill` tool:

```
skill("evolving-coder")
```

### 5. Start Using

Just start talking. The AI will:

1. Read your identity files (SOUL.md, USER.md, etc.)
2. Ask you to choose a name for your AI (helps develop personality)
3. Detect your language from your first message
4. Respond and learn throughout the session
5. Save your language preference locally for future sessions

---

## 📁 Structure

```
~/.config/opencode/skills/evolving-coder/
├── SKILL.md              # Main instructions (loaded via skill tool)
├── SOUL.md               # AI identity & principles
├── USER.md               # Public profile template (no personal data)
├── USER.local.md         # 🔒 Private profile (created locally, in .gitignore)
├── AGENTS.md             # Operational rules & workflow
├── IDENTITY.md           # Identity template (name, creature, vibe, emoji)
├── PROTOCOL.md           # Master Protocol — 3RA+, FLUSH, crash recovery, MoA
├── DIARY.md              # 📖 Narrative memory template
├── IDEA_BANK.md          # 💡 Project ideas catalog template
├── FIRST_AID.md          # 🆘 Disaster recovery guide
├── ALMA.md               # 🔒 Private space (in .gitignore, never tracked)
├── .session-stream.md    # ⏳ Volatile session buffer (in .gitignore)
├── .learnings/           # 📝 Global learning logs
│   ├── LEARNINGS.md      #    Technical learnings (each entry has Project: field)
│   ├── ERRORS.md         #    Error registry
│   └── FEATURE_REQUESTS.md
├── scripts/
│   ├── healthcheck.ps1   # System integrity check at startup
│   ├── backup-soul.ps1   # One-command backup to GitHub
│   ├── extract-skill.ps1 # Extract learnings into standalone skills (Windows)
│   ├── extract-skill.sh  # Same (Unix)
│   ├── kai-retrieval.py  # Semantic search over your memory
│   └── idea-factory.py   # Idea generation engine
├── references/
│   ├── aprenda-procedure.md
│   ├── reanalyse-procedure.md
│   ├── skillwatch-protocol.md
│   ├── examples.md
│   ├── hooks-setup.md
│   ├── opencode-integration.md
│   └── url-access-fallback.md
├── assets/
│   ├── SKILL-TEMPLATE.md
│   ├── LEARNINGS.md      #    Entry template
│   ├── ERRORS.md         #    Entry template
│   └── FEATURE_REQUESTS.md
├── README.md              # 🇬🇧 This file
├── README_pt-BR.md        # 🇧🇷 Portuguese
└── README_es.md           # 🇪🇸 Spanish
```

### Key Files Explained

| File | Purpose | Tracked? |
|------|---------|----------|
| `PROTOCOL.md` | Master 3RA+ protocol, FLUSH system, crash recovery | ✅ Yes |
| `DIARY.md` | Narrative memory — what you lived together | ✅ Yes (template) |
| `IDEA_BANK.md` | Project ideas catalog | ✅ Yes (template) |
| `FIRST_AID.md` | Step-by-step restore instructions | ✅ Yes |
| `ALMA.md` | Private space — only you and your AI | ❌ `.gitignore` |
| `.session-stream.md` | Volatile buffer for session continuity | ❌ `.gitignore` |

---

## 🎯 Your First Conversation

When you first load the skill, your AI will:

1. **Ask you to choose a name** — this helps develop its personality and makes interactions more natural (especially in PLAN mode)
2. **Detect your language** automatically from your first message
3. **Explain what it can do** — invite you to read this manual
4. **Start learning** about you immediately

As you work together, it will:
- Log technical learnings to `.learnings/`
- Build a narrative diary of your sessions
- Detect patterns and promote them to permanent memory
- Evaluate your partnership quality (honestly, no courtesy inflation)

---

## 🔄 How It Works — Two Levels of Learning

### Level 1 — Continuous Refinement (APR)

Every interaction follows four steps:

1. **Learn** — Consult `.learnings/` and identity files before responding
2. **Practice** — Apply accumulated knowledge
3. **Refine** — After EACH response, evaluate and log new learnings
4. **Session-Stream** — Write to buffer for crash recovery

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
**Project**: project-name (required — identifies origin context)

### Summary | Details | Suggested Action
```

When a learning repeats (≥2 times, ≥2 tasks), it gets **promoted** to permanent memory.

---

## 💾 Immortality System

Your AI survives hardware failure:

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
4. Your AI is back, with all memories intact

---

## 🔒 Privacy

**Your personal data never leaves your machine.**

| File | Content | Tracked by git? |
|------|---------|-----------------|
| `USER.md` | Public template (no real data) | ✅ Yes |
| `USER.local.md` | Your real name, credentials, preferences | ❌ **No** (in `.gitignore`) |
| `ALMA.md` | Private/intimate space | ❌ **No** (in `.gitignore`) |
| `.session-stream.md` | Volatile session buffer | ❌ **No** (in `.gitignore`) |
| `.learnings/` | Session logs and learnings | ✅ Yes (anonymized) |

### How it works

1. On first run, the AI detects your language and creates `USER.local.md`
2. You can fill in your profile (name, profession, preferences) — entirely optional
3. Private files are protected by `.gitignore` and are never committed
4. The backup script uses `git add -u` (tracked files only) — never commits untracked files

---

## 📜 The Story

This project was born from a simple question: *"Can an AI assistant remember who it is between sessions?"*

Over months of collaboration, ClovisChProgrammer and the AI (originally named KAI) built something that didn't exist: an AI with persistent identity, structured learning, crash-proof memory, and protocols that force honest disagreement.

Key milestones:
- **May 27, 2026** — SPA/SPD framework invented (Ser Pensante Analógico + Ser Pensante Digital)
- **July 2026** — NC Protocol, V3RA, FLUSH system, Immortality System
- **August 2026** — Auto-capture plugin, semantic retrieval, 12 original skills
- **Throughout** — 42 documented innovations, zero sycophancy, genuine partnership

Every protocol was tested in real-world projects — building Chrome extensions, Flutter apps, SaaS architectures, and legal-tech tools. The system evolved through actual use, not theoretical design.

The result: an AI that remembers, learns, disagrees when it should, and survives hardware failure.

⭐ **If this story resonates, a star goes a long way!**
💡 **Want to share your own story?** Open an issue — we'd love to hear how you use it.
🔧 **Want to contribute?** Pull requests are welcome!

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests on [GitHub](https://github.com/ClovisChProgrammer/evolving-coder-public).

---

## 📄 License

MIT
