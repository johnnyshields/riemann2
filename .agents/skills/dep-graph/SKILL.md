---
name: dep-graph
description: Validate the UV dependency graph in <team-dir>/uv.md. Detects cycles, orphans, broken references, and identifies critical-path UV entries that unblock the most downstream work. Reports only â€” no auto-edits.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Dep Graph

Validate the `Depends on:` graph in `<team-dir>/uv.md`. Read-only
coordinator action; reports only.

## Protocol

Parse each UV-NNN into (title, status, depends_on, source_label,
source_line). A malformed `Depends on:` (prose instead of UV IDs) is a
reportable defect â€” flag and stop until fixed.

Build the graph (nodes = UV IDs, edge `U â†’ V` if V is in U's
`Depends on`). Check:

- **Cycles** â€” DFS; any cycle is a hard error. Report each cycle
  ordered.
- **Orphan dependencies** â€” `U` cites `V` but `V` doesn't exist in the
  ledger.
- **Dead-end dependencies** â€” `U` cites a `rejected` V, silently
  blocking `U`.
- **Label cross-check** â€” `source_label` missing from `<paper>/<main>.tex`
  flags a `uv-sync` follow-up (not this skill's job to fix).

For critical-path ranking, compute per UV: **in-degree** (how many
entries depend on it) and **reachable-from-open** (count of `open` /
`heuristic` entries transitively depending on it). Rank by
reachable-from-open descending.

## Report

```
## Dep-Graph â€” <yyyymmdd-hhmmss>
Entries: N   Malformed: 0

Structural defects:
- Cycles: 0 (or list)
- Orphan deps: 0 (or list)
- Dead-end deps on rejected: 0 (or list)

Critical path (by reachable-from-open):
| UV | Status | In-deg | Reach | Title |

Leaves (depends_on = []): attackable independently
Root blockers: UV closing would cascade the most
Cross-check for uv-sync: labels missing from paper
```

Archive as `lore/<yyyymmdd>-dep-graph.md` and commit when the result changes
the active agenda; otherwise print the report and exit.

## Don't

Auto-edit `<team-dir>/uv.md` â€” fixes go through `uv-sync` or
`paper-demote`. Infer deps from prose â€” only trust the explicit
`Depends on:` field. Rank by raw in-degree (reachable-from-open is the
right signal).


