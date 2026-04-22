---
name: cycle-status
description: Snapshot of the current research state — active teams, recent task dirs, UV entries with status + dependencies, open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

# Cycle Status

Single-call orientation. No delegation, no edits, no commits. Prints a
structured snapshot that the coordinator (or the user) can scan in a
few seconds to resume or handoff.

## When to run

- At session start to orient.
- Mid-session after context switch to re-anchor.
- Before a `session-handoff` to make sure nothing is being forgotten.
- Whenever a recent chat segment left the state unclear.

## Arguments

`$ARGUMENTS` (optional):

- **empty** — full snapshot.
- `--recent <N>` — limit task-dir and lore history to the last N days
  (default 7).
- `--uv-only` — just the UV ledger snapshot with dependency edges.
- `--tasks-only` — just the task-dir overview.

## Protocol (synchronous, read-only)

### Step 1: Active teams

```sh
# Runtime-specific. Typical:
```

List any teams currently alive (via `TeamList` or the equivalent).
For each: name, members, last message time, lead agent.

### Step 2: Recent task dirs

```sh
ls -1t tasks/ | grep -E '^[0-9]{8}-' | head -10
```

For each, read `reports/_summary.md` if present, else list
`reports/*.md` count and approximate conclusion (open / closed /
mixed). Output a compact table:

| Task dir | Type | Role | Reports | Status |
|---|---|---|---|---|
| 20260423-180000-attack-gap-mixed-4-point | attack-gap | gap-close | 1/1 | closed (UV-002 refined) |
| ... | ... | ... | ... | ... |

### Step 3: UV ledger snapshot

Parse `paper/unverified.tex`. For each UV-NNN, emit:

```
UV-NNN  <status>  "<one-line title>"  deps: [UV-XXX, UV-YYY]
```

Highlight:

- **Critical-path items**: any UV whose `Depends on:` is `None` AND
  which is cited in at least one other UV's `Depends on:` — these
  unblock the most downstream work.
- **Orphan items**: if their cited `rem:wip-*` no longer appears in the
  paper (flag to run `uv-sync`).
- **Cycles in the dependency graph**: flag to run `dep-graph`.

### Step 4: findings.md size and composition

```sh
wc -l paper/findings.md
```

Report size, and counts per section (Structural / Negative / Goodies /
Recurring-open-gaps). Warn at ≥180 lines (pruning-due threshold per
`findings-prune`).

### Step 5: Recent lore

List the last 5–10 `lore/*.md` entries by date with one-line titles.
Highlight the most recent `session-handoff` entry (if any) and quote
its "Open threads" / "Queued follow-ups" sections verbatim.

### Step 6: Recent commits

```sh
git log --oneline -n 15
```

Highlight promote / demote / reject / correction / findings subjects.

### Step 7: Report

Print the above as a single scannable block, ordered:

```
ACTIVE TEAMS   (§1)
RECENT TASKS   (§2)
UV LEDGER      (§3)
FINDINGS SIZE  (§4)
RECENT LORE    (§5)
RECENT COMMITS (§6)
```

Under 80 lines of output. If any section is empty, emit "none" — do
not suppress the heading.

### Step 8: Coordinator summary (optional)

If the snapshot reveals something action-worthy (findings.md at 195
lines, an orphan UV, a task dir with missing reports, an unpushed
commit count > 3), append a "NEXT ACTIONS" footer of ≤ 5 bullets.

## Anti-patterns

- Do NOT edit anything from this skill — read-only is the contract.
- Do NOT delegate — this is synchronous coordinator observation.
- Do NOT produce narrative prose — the output is a scan-friendly
  dashboard, not an essay.
