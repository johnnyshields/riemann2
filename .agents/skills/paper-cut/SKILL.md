---
name: paper-cut
description: Move a passage from a paper main TeX file to that paper's cut-for-time.md with full provenance, then commit.
---

# Paper Cut

Move a passage from `<paper>/<main>.tex` to `<paper>/cut-for-time.md` with provenance.

Read the passage. Search for references pointing at labels inside it. Record each redirect or broken reference in the provenance block. Remove the passage and fix surrounding transitions.

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

If the passage contained a `rem:wip-*` label cited by a UV entry, update that UV's `Source in paper:` to the new home, or record the blocker in `collation.md` while keeping the UV live.

Commit paper edit + `cut-for-time.md` update together, staging by name. Subject: `cut: <one-line of what moved>`.
