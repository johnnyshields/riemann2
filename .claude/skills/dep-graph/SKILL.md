---
name: dep-graph
description: Validate the UV dependency graph in paper/unverified.tex. Detects cycles, orphans, broken references, and identifies critical-path UV entries that unblock the most downstream work. Reports only — no auto-edits.
---

# Dep Graph

Structural validator for the `Depends on:` fields in
`paper/unverified.tex`. The fields make the UV dependency graph
explicit (`CLAUDE.md` §6 / the UV schema); this skill checks that
the graph is well-formed and flags the highest-leverage nodes.

## When to run

- After `uv-sync` reports any change.
- Before starting a `research-team` / `research-attack` cycle, so the
  coordinator picks gap-closers with awareness of blocking chains.
- Periodically (e.g., once per week) as hygiene.
- Invoked by `cycle-status` when it detects possible cycles.

## Protocol (synchronous, read-only)

### Step 1: Parse

Parse `paper/unverified.tex` into a list of records:

```
UV-NNN:
  title: "..."
  status: open | heuristic | computational | blocked | rejected | promoted
  depends_on: [UV-XXX, UV-YYY] or []
  source_label: rem:wip-...
  source_line: N
```

Every `Depends on:` entry must be parseable. Malformed entries
(e.g. `Depends on: See UV-002`, prose instead of UV IDs) are a
**reportable defect** — flag and stop validation until the entry is
fixed.

### Step 2: Build the graph

Nodes: UV-NNN IDs.
Edges: `U -> V` if `V` appears in `U`'s `Depends on:` list.

### Step 3: Validate

#### 3a. Cycle detection

Run a standard DFS cycle-finding pass. Any cycle is a **hard error**:
no research can close a cycle of mutual dependencies; one of the
edges is wrong. Report each cycle as an ordered list of UV IDs and
surface to the user.

#### 3b. Orphan detection (dangling dependencies)

For every UV ID cited in some `Depends on:`, verify that UV ID exists
in the ledger. Missing targets are a defect: they reference a UV that
was rejected or never created. Report each as
`UV-AAA depends on UV-BBB (not found)`.

#### 3c. Dead-end detection

UV entries with `status: rejected` that still appear in others'
`Depends on:` lists — these are silently blocking downstream work that
thinks they're live. Report as `UV-AAA depends on rejected UV-BBB —
update UV-AAA`.

#### 3d. Contradiction with the paper

Cross-check `source_label` against the paper. If the `rem:wip-*` label
no longer exists in `proof_of_rh.tex`, flag for `uv-sync` (out of
scope for this skill, but mention it in the report).

### Step 4: Critical-path analysis

For each UV, compute:

- **In-degree**: how many other UV entries depend on it. High
  in-degree → closing this unblocks many downstream.
- **Reachable-from-open**: the number of `status: open` or `heuristic`
  entries that transitively depend on this UV.

Rank UVs by `reachable-from-open` descending. The top 3 are the
**critical-path entries** — closing them produces the biggest unblock.

### Step 5: Report

Output format:

```
## Dep-Graph Validation — <yyyymmdd-hhmmss>

### Parse
- Entries: N
- Malformed Depends-on lines: 0  (or list)

### Structural defects
- Cycles: 0  (or list each cycle)
- Orphan dependencies: 0  (or list each UV-AAA → UV-BBB)
- Dead-end dependencies (on rejected UVs): 0  (or list)

### Critical path (by reachable-from-open)
| Rank | UV   | Status | In-deg | Reachable-from-open | Title |
|------|------|--------|--------|---------------------|-------|
| 1    | UV-002 | open  | 2      | 3                   | Pair-like vs finite-core |
| 2    | ...    | ...   | ...    | ...                 | ...   |

### Leaves
(UVs with depends_on = [] — candidate starting points for a
research cycle, since they can be attacked independently)
- UV-001: Calibration small-u (status: open)
- UV-003: Parity/projective factorization (status: heuristic)
- ...

### Root blockers
(UVs whose closure would cascade the most)
- UV-002 closes 3 downstream (UV-007, ...)

### Cross-check notes (for uv-sync, not this skill)
- UV-004 cites rem:wip-... which is absent from proof_of_rh.tex
- ...
```

### Step 6: Commit (only if report is generated for record)

This skill is primarily for on-demand inspection. If the user wants
the report archived, save as `lore/<yyyymmdd>-dep-graph.md` and
commit:

```
dep-graph: snapshot <yyyymmdd> — <N UVs, M defects>
```

Otherwise, print-and-exit is fine.

## Anti-patterns

- Do NOT auto-edit `unverified.tex`. Fixes are the coordinator's call
  (and structural issues should probably route through `uv-sync` or
  `paper-demote`).
- Do NOT infer dependencies from prose — only trust the explicit
  `Depends on:` field. If the field is missing, flag and stop.
- Do NOT rank by raw in-degree alone — reachable-from-open is the
  better signal for where to attack next.
