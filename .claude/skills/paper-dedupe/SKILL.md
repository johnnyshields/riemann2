---
name: paper-dedupe
description: Remove duplicate content from paper/proof_of_rh.tex while preserving every unique observation. Tracks provenance in paper/cut-for-time.md and fixes cross-references.
---

# Paper De-dupe

Remove duplicate content from `paper/proof_of_rh.tex` while preserving
ALL unique meaning, findings, and observations.

## Principles

1. **No meaning lost.** If a duplicated passage contains ANY unique
   observation, phrasing, or insight not present in the surviving copy,
   merge that content into the surviving copy before deleting.
2. **Keep the best version.** Prefer the copy that is (a) closest to its
   proof context, (b) most self-contained, (c) best written.
3. **Track provenance.** Append removed content to
   `paper/cut-for-time.md` with the standard provenance format (see
   `paper-cut`).
4. **Check references.** Before deleting, grep for `\ref{...}` /
   `\eqref{...}` pointing at any `\label{...}` inside the condemned
   copies. Redirect references to the surviving copy.

## Steps

1. **Identify the duplicate.** User specifies what's duplicated and
   where.
2. **Read ALL copies.** Diff them mentally; record unique content in
   each.
3. **Merge unique content** into the surviving copy.
4. **Delete the redundant copies.**
5. **Fix references.** Redirect all `\ref{...}` / `\eqref{...}` that
   pointed at removed labels.
6. **Append deleted content to `paper/cut-for-time.md`** with provenance.
7. **UV sync.** If any `rem:wip-*` label inside the removed copies is
   cited by a UV-NNN entry in `unverified.tex`, update that UV's
   `Source in paper:` to the surviving location.
8. **Commit** with a message listing what was de-duped and what was
   preserved. Stage `paper/proof_of_rh.tex` and `paper/cut-for-time.md`
   by name.
