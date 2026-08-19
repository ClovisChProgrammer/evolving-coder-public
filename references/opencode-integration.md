# OpenCode Integration

How the evolving-coder skill works within OpenCode.

## Skill Loading

Skills in OpenCode are loaded on-demand via the `skill` tool. When you invoke `skill("evolving-coder")`:

1. The content of `SKILL.md` is injected into the current session context
2. The agent then reads the supporting files (SOUL.md, USER.md, etc.) from the skill directory
3. The agent reads existing `.learnings/` entries from the current project's working directory

## File Locations

**Skill directory** (global, shared across projects):
```
~/.config/opencode/skills/evolving-coder/
├── SKILL.md
├── SOUL.md
├── USER.md
├── AGENTS.md
├── IDENTITY.md
└── ...
```

**.learnings/** (per project, created where you work):
```
<project-root>/.learnings/
├── LEARNINGS.md
├── ERRORS.md
└── FEATURE_REQUESTS.md
```

OpenCode searches for skills in multiple locations (including `~/.config/opencode/skills/`), so any OpenCode instance can find this skill.

## Auto-Loading Plugin

For automatic loading (skill activates at session start without `skill()` command):

**Plugin file:** `~/.config/opencode/plugins/evolving-coder.js`

```javascript
import { readFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SKILL_DIR = join(__dirname, "..", "skills", "evolving-coder");

export const server = (ctx) => ({
  hooks: {
    "experimental.chat.system.transform": async (systemPrompt) => {
      const skillPaths = [
        join(SKILL_DIR, "SKILL.md"),
        join(SKILL_DIR, "SOUL.md"),
        join(SKILL_DIR, "AGENTS.md"),
      ];
      const chunks = [systemPrompt];
      for (const p of skillPaths) {
        try {
          chunks.push(`\n<!-- ${p.split("/").pop()} -->\n${readFileSync(p, "utf-8")}`);
        } catch { /* skip */ }
      }
      return chunks.join("\n\n");
    },
  },
});
```

**Config:** Add to `~/.config/opencode/opencode.json`:

```json
{
  "plugin": ["./plugins/evolving-coder.js"],
  ...
}
```

## Troubleshooting

### Skill not loading
1. Verify SKILL.md is in `~/.config/opencode/skills/evolving-coder/`
2. Check frontmatter has `name: evolving-coder`
3. Try `skill("evolving-coder")` explicitly

### Files not found
1. The skill directory is at `~/.config/opencode/skills/evolving-coder/`
2. Use the Read tool with the full path to verify files exist
3. If missing, the init script will create .learnings/ files automatically
