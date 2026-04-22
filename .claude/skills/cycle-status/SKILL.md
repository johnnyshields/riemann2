---
name: cycle-status
description: Snapshot of the current research state — active teams, recent task dirs, UV entries with status + dependencies, open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

# Cycle Status

Single-call orientation. Read-only. No delegation, no edits, no commits.

`$ARGUMENTS`: empty → full snapshot; `--recent <N>` → limit to last N
days (default 7); `--uv-only` / `--tasks-only` → filter.

## Gather

- **Active teams** via `TeamList` (or equivalent) — name, members, last
  message time.
- **Recent task dirs** — `ls -1t tasks/ | grep -E '^[0-9]{8}-' | head -10`.
  For each: type, role, report count (landed vs expected), status from
  `reports/_summary.md` if present.
- **UV ledger** — one line per UV: `UV-NNN <status> "<title>" deps:
  [...]`. Flag critical-path entries (those with `Depends on: None`
  and cited in others' deps — closing them unblocks the most
  downstream), orphans (label absent from paper — run `uv-sync`),
  suspected cycles (run `dep-graph`).
- **`findings.md` size** — warn at ≥180 lines.
- **Recent lore** — last 5–10 `lore/*.md` by date, one-line titles.
  If a recent `session-handoff` exists, quote its "Open threads" and
  "Queued follow-ups" sections verbatim.
- **Recent commits** — `git log --oneline -n 15`. Highlight
  promote / demote / reject / correction / findings subjects.

## Report

Scannable block, ≤80 lines, fixed section order:

```
ACTIVE TEAMS
RECENT TASKS
UV LEDGER
FINDINGS SIZE
RECENT LORE
RECENT COMMITS
```

Empty sections: emit "none" — don't suppress the heading.

If anything looks action-worthy (`findings.md` at 195 lines, orphan
UV, task dir with missing reports, unpushed commits > 3), add a
"NEXT ACTIONS" footer (≤5 bullets).
