---
name: paper-cut
description: Move a passage from <paper>/<main>.tex to <paper>/cut-for-time.md with full provenance (original location, reason, broken refs), then commit.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Paper Cut

Move a passage from `<paper>/<main>.tex` to `<paper>/cut-for-time.md`
with provenance.

Read the passage. Grep for `\ref{...}` / `\eqref{...}` pointing at any
`\label{...}` inside â€” note each (redirect or record as broken in the
provenance block). Remove the passage from the paper; fix surrounding
transitions.

Append to `<paper>/cut-for-time.md`:

```markdown
---

## From: [Section name] ([context])

**Cut date:** YYYY-MM-DD
**Original location:** <paper>/<main>.tex, [line range or label]
**Reason:** [brief reason]
**Broken refs:** [list, if any]

\`\`\`latex
[exact LaTeX cut]
\`\`\`
```

If the passage contained a `rem:wip-*` label cited by a UV entry, update
that UV's `Source in paper:` to the new home, or mark it `blocked` with
an explanation.

Commit paper edit + `cut-for-time.md` update together, stage by name.
Subject: `cut: <one-line of what moved>`.


