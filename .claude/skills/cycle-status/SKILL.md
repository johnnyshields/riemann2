---
name: cycle-status
description: Snapshot of the current research state — active teams, recent team dirs, UV entries with status + dependencies, open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

# Cycle Status

Single-call orientation. Read-only. No delegation, no edits, no
commits.

`$ARGUMENTS`: empty → full snapshot; `--paper <name>` → limit to one
paper; `--recent <N>` → limit to last N days (default 7);
`--uv-only` / `--teams-only` → filter.

## Gather

- **Active teams** via `TeamList` (or equivalent) — name, members,
  last message time.
- **Recent team dirs** — for each `<paper>` in the repo, run
  `ls -1t <paper>/teams/ 2>/dev/null | grep -E '^[0-9]{8}-' | head -5`.
  For each dir: paper, team-slug, agent count (landed vs expected
  from `dispatch.md`), `collation.md` summary line if present.
- **Current UV ledger** — read the *most recent* team dir's `uv.md`.
  One line per UV: `UV-NNN <status> "<title>" deps: [...]`. Flag
  critical-path entries (those with `Depends on: None` and cited in
  others' deps — closing them unblocks the most downstream), orphans
  (label absent from `<main>.tex` — run `uv-sync`), suspected cycles
  (run `dep-graph`).
- **Current `findings.md` size** — `wc -l` on the most recent team
  dir's `findings.md`. Warn at ≥180 lines (pending forward-carry
  prune next cycle).
- **Uncaptured agent material** — for the most recent team dir, list
  any `agents/*/report.md` whose claims don't yet appear in
  `findings.md` or `uv.md`. That's the `Capture before shutdown, forward-carry at dispatch` capture miss surface.
- **Recent lore** — last 5–10 `lore/*.md` by date, one-line titles.
  If a recent `session-handoff` exists, quote its "Open threads" and
  "Queued follow-ups" sections verbatim.
- **Recent commits** — `git log --oneline -n 15`. Highlight
  promote / demote / reject / correction / findings / carry-forward
  subjects.

## Report

Scannable block, ≤80 lines, fixed section order:

```
ACTIVE TEAMS
RECENT TEAM DIRS
CURRENT UV LEDGER
CURRENT FINDINGS SIZE
UNCAPTURED AGENT MATERIAL
RECENT LORE
RECENT COMMITS
```

Empty sections: emit "none" — don't suppress the heading.

If anything looks action-worthy (`findings.md` at 195 lines, orphan
UV, team dir with missing reports, unpushed commits > 3, uncaptured
agent material > 0), add a "NEXT ACTIONS" footer (≤5 bullets).
