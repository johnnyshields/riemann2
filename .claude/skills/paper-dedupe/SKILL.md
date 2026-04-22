---
name: paper-dedupe
description: Remove duplicate content from paper/proof_of_rh.tex while preserving every unique observation. Tracks provenance in paper/cut-for-time.md and fixes cross-references.
---

# Paper De-dupe

Remove duplicates while preserving every unique observation.

Identify the duplicate (user-specified). Diff the copies mentally;
record anything unique in each. Merge unique content into the copy
that will survive — prefer the one closest to its proof context, most
self-contained, and best written.

Delete the redundant copies. Redirect every `\ref{...}` / `\eqref{...}`
that pointed at a removed `\label{...}` to the surviving label. Append
the deleted content to `paper/cut-for-time.md` with standard provenance
(see `paper-cut`). If any removed `rem:wip-*` label was cited by a UV
entry, update the UV's `Source in paper:` to the surviving location.

Commit with a subject listing what was de-duped and what was preserved.
Stage `paper/proof_of_rh.tex` and `paper/cut-for-time.md` by name.
