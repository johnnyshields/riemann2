# Paper De-dupe

Remove duplicate content from the paper while preserving ALL unique meaning, findings, and observations.

## Principles

1. **No meaning lost.** If a duplicated passage contains ANY unique observation, phrasing, or insight not present in the surviving copy, merge that content into the surviving copy before deleting.
2. **Keep the best version.** When choosing which copy to keep, prefer the one that is (a) closest to its proof context, (b) most self-contained, (c) best written.
3. **Track provenance.** Add removed content to `paper/paper15-c-cut-for-time.md` with the standard provenance format.
4. **Check references.** Before deleting, verify no `\ref{}` points to the deleted `\label{}`. If references exist, redirect them to the surviving copy.

## Steps

1. **Identify the duplicate.** The user specifies what's duplicated and where.
2. **Read ALL copies** of the duplicated content. Diff them mentally — note any unique content in each.
3. **Merge unique content** into the copy that will survive.
4. **Delete the redundant copies.**
5. **Check for broken `\ref{}`/`\label{}` references.** Fix any that point to deleted labels.
6. **Add deleted content to cut-for-time doc** with provenance.
7. **Commit** with a message listing what was de-duped and what was preserved.
