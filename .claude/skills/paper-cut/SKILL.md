---
name: paper-cut
description: Move a passage from <paper>/<main>.tex to <paper>/cut-for-time.md with full provenance (original location, reason, broken refs), then commit.
---

# Paper Cut

Move a passage from `<paper>/<main>.tex` to `<paper>/cut-for-time.md`
with provenance.

Read the passage. Grep for `\ref{...}` / `\eqref{...}` pointing at any
`\label{...}` inside — note each (redirect or record as broken in the
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
