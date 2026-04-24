---
name: paper-dedupe
description: Remove duplicate content from a paper main TeX file while preserving every unique observation. Tracks provenance in the paper's cut-for-time.md and fixes cross-references.
---

# Paper Dedupe

Remove duplicate content while preserving every unique observation.

Identify the duplicate passage or region. Compare copies and record anything unique in each. Merge unique content into the surviving copy — prefer the one closest to its proof context, most self-contained, best written.

Delete redundant copies. Redirect every `\ref{...}` / `\eqref{...}` pointing at a removed `\label{...}` to the surviving label. Append deleted content to `<paper>/cut-for-time.md` with `paper-cut` provenance. If a removed `rem:wip-*` label was cited by a UV entry, update the UV's `Source in paper:` or record the blocker in `collation.md`.

Commit with a subject listing what was deduped and what was preserved. Stage `<paper>/<main>.tex` and `<paper>/cut-for-time.md` by name.
