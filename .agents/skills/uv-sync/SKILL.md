---
name: uv-sync
description: Reconcile rem:wip-* labels in a paper main TeX file with live UV-NNN entries in a team uv.md. Reports and fixes missing UV entries and orphan UVs. Synchronous coordinator action, no delegation.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# UV Sync

Reconcile the two quarantine anchors. `rem:wip-*` labels in the paper mark
conditional / open / in-progress claims; `UV-NNN` entries in `<team-dir>/uv.md`
ledger the live missing sub-statements. A UV is live by presence; do not add
status annotations.

## Protocol

Enumerate paper labels and UV anchors with `rg`. Build the mapping from each
`rem:wip-<slug>` to the UV entry whose header or `Source in paper:` cites that
slug. Classify:

- **Matched** - one paper label and one UV entry point at each other.
- **Missing UV** - paper label has no matching live UV entry.
- **Orphan UV** - UV entry cites a label absent from the paper.
- **Weak provenance** - UV entry lacks source label, report path, script, lore,
  or other provenance required by AGENTS.md.

## Report

```markdown
## UV Sync - <yyyymmdd-hhmmss>
Labels: N   UV entries: M   Matched: P
Missing UV: Q   Orphan UV: R   Weak provenance: S

### Matched
| rem:wip-<slug> | UV-NNN | Paper line | Provenance |

### Missing UV
| rem:wip-<slug> | Paper line | New UV-NNN | Claim |

### Orphan UV
| UV-NNN | Cited label | Likely cause | Action |
```

## Fix

- **Missing UV**: create UV entries with the next monotonic IDs. Include source
  label, claim, current role / needed-for-promotion, dependency refs if known,
  and provenance.
- **Orphan UV**: if git history or paper context makes the redirect clear,
  update the source label. If the claim was promoted or rejected, process it
  through `Claim lifecycle (git-as-archive)`. Otherwise keep it live and record
  the blocker in `collation.md`.
- **Weak provenance**: add the narrowest concrete source available. If none is
  recoverable, mark the provenance defect in `collation.md` and keep the UV
  quarantined.

Stage changed paths by name. Commit `uv-sync: <counts> - <summary>`. Avoid
`<paper>/<main>.tex` edits unless the sync itself exposes a clear stale label.

## When

After a large paper editing pass; before `research-team` / `research-attack` so
gap-closers get correct entries; periodic hygiene after major proof-state churn.
