---
name: paper-dedupe
description: Remove duplicate content from <paper>/<main>.tex while preserving every unique observation. Tracks provenance in <paper>/cut-for-time.md and fixes cross-references.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

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


