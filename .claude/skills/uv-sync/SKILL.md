---
name: uv-sync
description: Reconcile rem:wip-* labels in <paper>/<main>.tex with UV-NNN entries in <team-dir>/uv.md. Reports missing UV entries (label without UV) and orphan UVs (UV without matching label). Synchronous coordinator action, no delegation.
---

# UV Sync

Reconcile the two quarantine anchors. `rem:wip-*` labels in the paper
mark conditional / open / in-progress claims; `UV-NNN` entries in
`<team-dir>/uv.md` ledger them with status, promotion condition, deps.
They should be 1:1. Drift happens.

## Protocol

Enumerate:

```sh
grep -n '\\label{rem:wip-' <paper>/<main>.tex
grep -nE '\\item\[UV-[0-9]+\]|Source in paper' <team-dir>/uv.md
```

Build the mapping: for each `rem:wip-<slug>`, find the UV whose
`Source in paper:` cites that slug. Classify:

- **Matched** — 1:1.
- **Missing UV** — label has no matching entry.
- **Orphan UV** — entry cites a label absent from the paper.

## Report

```
## UV Sync — <yyyymmdd-hhmmss>
Labels: N   UV entries: M   Matched: P
Missing UV (need entry): Q
Orphan UV (need redirect/reject/promote): R

### Matched
| rem:wip-<slug> | UV-NNN | Line | Status |

### Missing UV
| rem:wip-<slug> | Line | Proposed UV-NNN | Notes |

### Orphan UV
| UV-NNN | Cited label | Likely cause | Suggested action |
```

## Fix (clear cases only)

- **Missing UV**: if ≤3, draft new entries directly — read the paper
  remark and propose Title / Status / Claim / Why / Needed / Depends on.
  If more, surface to the user for batch review.
- **Orphan UV**: surface. Label renames are usually a `Source in paper:`
  redirect; silent promotions or deletions need coordinator judgment.
  Don't auto-act without clear git-history evidence.

Stage `<team-dir>/uv.md` by name. Commit
`uv-sync: <counts> — <summary>`. No `<paper>/<main>.tex` edits.

## When

After a large paper editing pass; before `research-team` /
`research-attack` so gap-closers get correct entries; periodic hygiene
(weekly or every ~20 paper commits).
