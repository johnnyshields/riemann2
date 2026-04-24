---
name: paper-dedupe
description: Remove duplicate content from <paper>/<main>.tex while preserving every unique observation. Tracks provenance in <paper>/cut-for-time.md and fixes cross-references.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Paper De-dupe

Remove duplicates while preserving every unique observation.

Identify the duplicate (user-specified). Diff the copies mentally;
record anything unique in each. Merge unique content into the copy
that will survive â€” prefer the one closest to its proof context, most
self-contained, and best written.

Delete the redundant copies. Redirect every `\ref{...}` / `\eqref{...}`
that pointed at a removed `\label{...}` to the surviving label. Append
the deleted content to `<paper>/cut-for-time.md` with standard provenance
(see `paper-cut`). If any removed `rem:wip-*` label was cited by a UV
entry, update the UV's `Source in paper:` to the surviving location.

Commit with a subject listing what was de-duped and what was preserved.
Stage `<paper>/<main>.tex` and `<paper>/cut-for-time.md` by name.


