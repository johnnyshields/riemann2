---
name: uv-sync
description: Reconcile rem:wip-* labels in paper/proof_of_rh.tex with UV-NNN entries in paper/unverified.tex. Reports missing UV entries (label without UV) and orphan UVs (UV without matching label). Synchronous coordinator action, no delegation.
---

# UV Sync

Integrity check between the two quarantine anchors:

- `rem:wip-*` labels embedded in `paper/proof_of_rh.tex` mark places
  where a claim is acknowledged conditional / open / in-progress.
- `UV-NNN` entries in `paper/unverified.tex` ledger the same items
  with their status, promotion condition, and dependencies.

These should be in 1:1 correspondence. Drift happens: new `rem:wip-*`
gets added to the paper without a UV entry; a UV entry survives after
its `rem:wip-*` was removed or renamed. This skill reconciles.

## Protocol (synchronous, no delegation)

### Step 1: Enumerate both sides

```sh
# All rem:wip-* labels in the paper (with line numbers)
grep -n '\\label{rem:wip-' paper/proof_of_rh.tex \
    | sed -E 's/.*\\label\{(rem:wip-[^}]+)\}.*/\1/' | sort -u

# All UV-NNN entries and their Source-in-paper references
grep -nE '\\item\[UV-[0-9]+\]|Source in paper' paper/unverified.tex
```

### Step 2: Build the mapping

For each `rem:wip-<slug>` label, find the UV entry whose "Source in
paper" line references that exact slug. Record:

- **Matched**: label → UV-NNN (1:1).
- **Missing UV**: label has no matching UV entry in `unverified.tex`.
- **Orphan UV**: UV entry cites a label that no longer appears in
  `proof_of_rh.tex` (renamed, deleted, or cut).

### Step 3: Report

Print a structured report:

```
## UV Sync Report — <yyyymmdd-hhmmss>

### Summary
- Labels in paper: N
- UV entries: M
- Matched: P
- Missing UV (label without entry): Q — each needs a new UV-NNN
- Orphan UV (entry without label): R — each needs to be rejected,
  redirected, or promoted

### Matched (P entries)
| rem:wip-<slug> | UV-NNN | Paper line | Status |
|---|---|---|---|
| rem:wip-foo | UV-003 | 12447 | heuristic |
| ... | ... | ... | ... |

### Missing UV (Q entries)
| rem:wip-<slug> | Paper line | Proposed UV-NNN | Notes |
|---|---|---|---|
| rem:wip-bar | 24167 | UV-010 (next available) | needs entry |
| ... | ... | ... | ... |

### Orphan UV (R entries)
| UV-NNN | Cited label | Likely cause | Suggested action |
|---|---|---|---|
| UV-099 | rem:wip-baz | label renamed | redirect source to <new> |
| ... | ... | ... | ... |
```

### Step 4: Fix, or queue fixes

- **Missing UV** is a real integrity gap: the paper has an unverified
  claim that isn't in the ledger. For each, draft a new UV-NNN entry
  by reading the relevant remark in the paper and proposing Title /
  Status / Claim / Why unverified / Needed for promotion / Depends on.
  If the missing count is small (\(\le 3\)), write them directly. If
  large, report to the user and ask whether to generate draft entries
  for review.
- **Orphan UV** needs triage: label may have been renamed (update
  `Source in paper:`), the claim may have been silently promoted (demote
  or accept), or the label may have been deliberately removed (reject
  the UV). Do not auto-act — surface to the user unless the case is
  obvious from recent git history.

### Step 5: Commit

Stage `paper/unverified.tex` by name and commit:
`uv-sync: <N added / M rejected / K redirected> — <one-line summary>`.

No `paper/proof_of_rh.tex` edits from this skill — only `unverified.tex`
may change, and only in clear cases.

## When to run

- After a large editing pass on `proof_of_rh.tex` (added / removed
  remarks).
- Before starting a `research-team` or `research-attack` cycle, so the
  gap-closer gets a correct UV entry.
- Periodically (e.g., once per week or every 20 paper commits) as
  preventive hygiene.
