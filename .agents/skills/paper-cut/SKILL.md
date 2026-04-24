---
name: paper-cut
description: Move a passage from a paper main TeX file to that paper's cut-for-time.md with full provenance, then commit.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Cut

Move a passage from `<paper>/<main>.tex` to `<paper>/cut-for-time.md` with
provenance.

Read the passage. Search for references pointing at labels inside it. Record
each redirect or broken reference in the provenance block. Remove the passage
from the paper and fix surrounding transitions.

Append to `<paper>/cut-for-time.md`:

````markdown
---

## From: [Section name] ([context])

**Cut date:** YYYY-MM-DD
**Original location:** <paper>/<main>.tex, [line range or label]
**Reason:** [brief reason]
**Broken refs:** [list, if any]

```latex
[exact LaTeX cut]
```
````

If the passage contained a `rem:wip-*` label cited by a UV entry, update that
UV's `Source in paper:` to the new home, or record the blocker in
`collation.md` while keeping the UV live.

Commit paper edit plus `cut-for-time.md` update together, staging by name.
Subject: `cut: <one-line of what moved>`.
