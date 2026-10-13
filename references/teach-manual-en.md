# TEACH MANUAL — EN

> Author: Matt Pocock (mattpocock/skills) · License: MIT · Adapted for opencode/KAI
> Last updated: 2026-10-13

## 1. Purpose

The `teach` skill provides **structured, stateful** teaching across multiple sessions. Instead of a one-off answer, it creates a **teaching workspace** in the current directory with HTML lessons, learning records, resources, and a mission.

## 2. When to use

Use when:
- You want to learn from scratch or go deeper (QA/Playwright, regex, bash, architecture, etc.)
- You want a track with exercises/review
- You need persistence between sessions
- You prefer short lessons with a tangible win

Do not use when:
- You need a single, quick answer
- Pure lookup ("how to do X?")

## 3. Key concepts

| Concept | Explanation |
|---|---|
| **Stateful** | State lives in the directory where you invoked `teach`. |
| **MISSION.md** | Real reason to learn. Drives every lesson choice. |
| **Zone of Proximal Development (ZPD)** | "Challenged just enough" — not too easy, not overwhelming. |
| **Lessons (`./lessons/*.html`)** | Self-contained, short, clean (Tufte style). Each delivers 1 win. |
| **Learning records (`./learning-records/*.md`)** | Lightweight ADRs: non-obvious insights, corrections, direction changes. |
| **Reference (`./reference/*.html`)** | Compact cheat sheets/glossaries/algorithms. |
| **Assets (`./assets/*`)** | Reusable components (CSS, quiz, simulator). Reuse by default. |
| **RESOURCES.md** | Trusted sources (official docs > random blogs). |
| **NOTES.md** | Agent notes about your prefs/pace. |

## 4. Invocation

From target directory (e.g. `C:\Users\clovi\learn\qa-playwright`):

```text
teach me QA with Playwright from scratch
```

Or:
```text
use the teach skill: I want to learn bash for automation
```

## 5. Created structure

```text
<cwd>/
├── MISSION.md
├── RESOURCES.md
├── NOTES.md
├── assets/
├── lessons/          # 0001-name.html, 0002-name.html,...
├── learning-records/ # 0001-insight.md,...
└── reference/
```

Format files live at `~/.config/opencode/skills/teach/*-FORMAT.md`.

## 6. Initial flow

1. **Mission** – if missing, agent asks why, practical goal, timeline, prior knowledge.
2. **ZPD** – read existing learning-records or start minimal.
3. **Resources** – curate high-trust sources.
4. **First lesson** – short, practical, mission-aligned. Opens HTML.
5. **Iterate** – after each lesson: update learning-record, propose next "just enough" step.

## 7. Pedagogic principles

| Principle | Application |
|---|---|
| **Short > long** | Small lessons. Protect working memory. |
| **Practice over heavy theory** | Teach only what's needed to do something useful now. |
| **Desirable difficulty** | Active recall (unclued quiz), spacing on review. Don't overdo. |
| **Careful interleaving** | Mix related topics only in practical exercises. |
| **Source fidelity** | Cite trusted sources. Prefer official docs. |
| **Reuse-first** | Check `assets/` before creating CSS/quiz. Extract reusable component if general. |
| **Beautiful but functional** | Clean HTML, readable (Tufte-inspired). Clarity > decoration. |
| **Mission-grounded** | Every lesson must serve the stated mission. |

## 8. Good practices

- **1 win per lesson.** e.g. "run 1 Playwright test in headless".
- **Self-contained HTML.** Minimal CSS/JS or via `assets/`.
- **Internal links.** Cross-link lesson↔reference↔lesson.
- **Final reminder.** Each lesson reminds: "Ask the agent if anything is unclear".
- **Explicit learning.** After session, write to `learning-records/000X-*.md`.
- **Dynamic ZPD.** Easy → harder; stuck → easier.
- **Don't trust parametric only.** Research when unsure.

## 9. Examples

**Playwright from scratch (pragmatic)**
```text
teach me Playwright focused on 3 simple E2E tests for a form
```

**Bash for automation**
```text
teach me bash focused on small automation scripts for my workflow
```

**Regex applied to logs**
```text
teach me regex with exercises applied to log parsing
```

## 10. Fit with your QA/Playwright course

Perfect to consolidate:
- `MISSION.md` = "why" (practice/certification)
- `lessons/` = incremental track
- `learning-records/` = weak spots map
- `reference/playwright-cheatsheet.html` = grows with you

## 11. Operational notes (opencode)

- Installed at `~/.config/opencode/skills/teach/`
- Includes `SKILL.md` + 4 `*-FORMAT.md` + `LICENSE`
- Frontmatter adapted to opencode
- Natural language invocation
- Creates structure only in current directory

## 12. References

- [mattpocock/skills – teach](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach)
- Local: `~/.config/opencode/skills/teach/SKILL.md`, `MISSION-FORMAT.md`, `LEARNING-RECORD-FORMAT.md`, `RESOURCES-FORMAT.md`, `GLOSSARY-FORMAT.md`