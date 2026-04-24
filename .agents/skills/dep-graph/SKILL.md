---
name: dep-graph
description: Validate the UV dependency graph in a team directory uv.md. Detects cycles, orphans, broken references, missing explicit deps, and critical-path UV entries. Reports only; no auto-edits.
---

# Dep Graph

Validate dependency structure in `<team-dir>/uv.md`. Read-only; reports only. A UV is live by presence. Don't infer hard dependencies from prose unless an explicit `Depends on:` field or clear `depends on UV-NNN` phrase exists; report soft references separately.

## Protocol

Parse each UV-NNN into: title/source label, claim, explicit deps, soft UV refs, current role / needed-for-promotion, provenance. A malformed `Depends on:` field is a defect.

Build the graph from explicit deps only. Check:

- **Cycles** — hard error.
- **Orphan deps** — a UV cites a missing UV.
- **Missing explicit deps** — soft UV refs but no explicit deps.
- **Weak provenance** — no paper label, report path, script, lore, or other concrete source.
- **Label cross-check** — source label missing from `<paper>/<main>.tex`; run `uv-sync` for fixes.

For critical-path ranking, compute in-degree and reachable downstream count over explicit deps. If many deps are missing, mark ranking provisional.

## Report

```markdown
## Dep Graph - <yyyymmdd-hhmmss>
Entries: N   Explicit deps: E   Soft refs: S   Malformed: M

Structural defects:
- Cycles:
- Orphan deps:
- Missing explicit deps:
- Weak provenance:
- Labels needing uv-sync:

Critical path, provisional if needed:
| UV | In-degree | Reach | Source label | Current role |

Leaves: attackable independently
Root blockers: closing these would cascade most
```

Archive as `lore/<yyyymmdd>-dep-graph.md` and commit when the result changes the active agenda; otherwise print and exit.

## Don't

Auto-edit `<team-dir>/uv.md` — fixes go through `uv-sync`, `paper-demote`, or coordinator capture. Treat `attempts.md` route history as proof state. Rank by raw in-degree when reachable count is available.
