---
name: paper-dedupe
description: Remove duplicate content from a paper main TeX file while preserving every unique observation. Tracks provenance in the paper's cut-for-time.md and fixes cross-references.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Dedupe

Remove duplicate content while preserving every unique observation.

Identify the duplicate passage or region. Compare the copies and record anything
unique in each. Merge unique content into the copy that should survive,
preferring the one closest to its proof context, most self-contained, and best
written.

Delete redundant copies. Redirect every `\ref{...}` / `\eqref{...}` pointing at
a removed `\label{...}` to the surviving label. Append deleted content to
`<paper>/cut-for-time.md` with `paper-cut` provenance. If any removed
`rem:wip-*` label was cited by a UV entry, update the UV's `Source in paper:` to
the surviving location or record the blocker in `collation.md`.

Commit with a subject listing what was deduped and what was preserved. Stage
`<paper>/<main>.tex` and `<paper>/cut-for-time.md` by name.
