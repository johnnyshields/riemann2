---
name: dep-graph
description: Validate the UV dependency graph in <team-dir>/uv.md. Detects cycles, orphans, broken references, missing explicit deps, and critical-path UV entries. Reports only; no auto-edits.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Dep Graph

Validate dependency structure in `<team-dir>/uv.md`. Read-only coordinator
action; reports only. A UV is live by presence. Do not infer hard dependencies
from prose unless an explicit `Depends on:` field or clear `depends on UV-NNN`
phrase exists; report soft references separately.

## Protocol

Parse each UV-NNN into: title/source label, claim, explicit deps, soft UV refs,
current role / needed-for-promotion, and provenance. A malformed explicit
`Depends on:` field is a reportable defect.

Build the graph from explicit deps only. Check:

- **Cycles** - any cycle is a hard error.
- **Orphan dependencies** - a UV cites a missing UV.
- **Missing explicit deps** - the entry has soft UV refs but no explicit deps.
- **Weak provenance** - the entry lacks paper label, report path, script, lore,
  or other concrete source.
- **Label cross-check** - source label missing from `<paper>/<main>.tex`; run
  `uv-sync` for fixes.

For critical-path ranking, compute in-degree and reachable downstream count over
explicit deps. If many deps are missing, report ranking as provisional.

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

Archive as `lore/<yyyymmdd>-dep-graph.md` and commit when the result changes
the active agenda; otherwise print the report and exit.

## Don't

Do not auto-edit `<team-dir>/uv.md`; fixes go through `uv-sync`,
`paper-demote`, or coordinator capture. Do not treat route history in
`attempts.md` as proof state. Do not rank by raw in-degree when reachable
downstream count is available.
