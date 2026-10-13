# GRILLING MANUAL (grill-me / grilling) — EN

> Author: Matt Pocock (mattpocock/skills) · License: MIT · Adapted for opencode/KAI
> Last updated: 2026-10-13

## 1. Purpose

The `grill-me` and `grilling` skills **stress-test and sharpen a plan, idea, or decision** before committing to implementation. Instead of jumping straight to code, the agent asks structured questions in rounds until ambiguity is removed and there is shared understanding.

- `grill-me`: thin invocation wrapper (say "grill this idea").
- `grilling`: primitive (design tree, rounds, frontier).

## 2. When to use

Use when:
- You have a vague idea ("I want to build X", "refactor Y") with missing details
- An important decision has trade-offs
- You want to validate scope before spending time/tokens
- Alternatives need to be clarified
- Goals, users, constraints need alignment

Do not use when:
- Trivial tasks (1 file, few lines)
- A clear, approved spec/PRD already exists

## 3. Key concepts

| Concept | Explanation |
|---|---|
| **Design Tree** | Decision tree: each decision branches into others that depend on it. |
| **Rounds** | The agent asks the **entire frontier** in one round, numbers each question, and gives a recommended answer. Wait for answers before next round. |
| **Frontier** | Questions whose **prerequisites are already settled**. Questions depending on an unanswered question remain for a later round. |
| **Recommended answer** | Each question includes `➡️ <recommended answer>`. Questions are worded so that answering **"yes"** accepts the recommended answer. |
| **Facts vs Decisions** | **Facts**: agent finds them (filesystem, grep/glob, reads, sub-agent). **Decisions**: belong to the user — never guess. |

## 4. Invocation (opencode)

With skills installed in `~/.config/opencode/skills/`, just say:

```text
grill this idea: I want a CLI to extract build metrics
```

Or:
```text
use the grilling skill on this idea
```

`grill-me` triggers `grilling` automatically.

## 5. Round format

Each round looks like:

```text
❓ **Q1** - **<question title>**: <body, paragraphs, optional choices>

➡️ <recommended answer>

---

❓ **Q2** - **<question title>**: ...

➡️ <recommended answer>
```

## 6. Workflow

1. **Initial mapping** – build minimal decision tree.
2. **Round 1 (initial frontier)** – ask all questions whose dependencies are satisfied.
3. **You answer** – `yes` (accept recommendation), `no` (with reason), or freeform per question.
4. **Recompute** – update tree, expand frontier with newly unblocked questions.
5. **Next rounds** – repeat until **frontier is empty**.
6. **Closure** – agent confirms shared understanding. **Do not implement before this confirmation**.

## 7. Practical rules

- **Never guess facts.** If it needs filesystem/code inspection, use tools/sub-agent — do not ask user.
- **Ask for decisions, not facts.** "What should the command name be?" → decision (user). "Does package.json exist?" → agent checks.
- **Recommended answer is intentional.** If it matches your intent, `yes` is enough.
- **One round at a time.** Answer all questions in that round or state what's pending.
- **No premature action.** Only proceed to implementation after explicit shared-understanding confirmation.

## 8. Quick examples

**Vague idea**
> `grill this idea: app to remember reading`

Covers: purpose, audience, MVP vs full, platform (web/CLI/app), local vs remote data.

**Refactor**
> `grill this idea: extract module X without breaking public API`

Covers: stable contracts, existing tests, risks, strict scope.

## 9. vs brainstorming

| Aspect | `brainstorming` (existing) | `grilling` (new) |
|---|---|---|
| Focus | General Socratic + pre-impl gate | **Design tree + rounds + frontier** (systematic) |
| Output | Min 3 questions + clarification | Multiple questions grouped by dependencies, per-item recommendation |
| Facts | May ask user | Strong: "facts = your job; decisions = user" |
| Iteration | Often 1–2 exchanges | Iterative rounds until frontier empty |

## 10. Tips

- Short answers: `yes`, `no — prefer CLI`, `Q1 yes, Q2 no because...`
- State changes explicitly if you change mind mid-rounds.
- Paste full answers if ready; numbering by Q# is fine.

## 11. Operational notes (opencode)

- Installed at `~/.config/opencode/skills/grill-me/`, `~/.config/opencode/skills/grilling/`
- Frontmatter adapted to opencode format (removed `disable-model-invocation`)
- Natural invocation via human language.

## 12. References

- [mattpocock/skills – grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
- [mattpocock/skills – grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)
- Local: `~/.config/opencode/skills/grilling/SKILL.md`