---
name: cycle-status
description: Snapshot of the current research state â€” active teams, recent team dirs, UV entries with status + dependencies, open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Cycle Status

Single-call orientation. Read-only. No delegation, no edits, no
commits.

`$ARGUMENTS`: empty â†’ full snapshot; `--paper <name>` â†’ limit to one
paper; `--recent <N>` â†’ limit to last N days (default 7);
`--uv-only` / `--teams-only` â†’ filter.

## Gather

- **Active teams** via current Codex subagent handles when available;
  otherwise infer live work from the newest `dispatch.md` / `collation.md`
  and unclosed agent reports.
- **Recent team dirs** â€” for each `<paper>` in the repo, run
  `ls -1t <paper>/teams/ 2>/dev/null | grep -E '^[0-9]{8}-' | head -5`.
  For each dir: paper, team-slug, agent count (landed vs expected
  from `dispatch.md`), `collation.md` summary line if present.
- **Current UV ledger** â€” read the *most recent* team dir's `uv.md`.
  One line per UV: `UV-NNN <status> "<title>" deps: [...]`. Flag
  critical-path entries (those with `Depends on: None` and cited in
  others' deps â€” closing them unblocks the most downstream), orphans
  (label absent from `<main>.tex` â€” run `uv-sync`), suspected cycles
  (run `dep-graph`).
- **Current `findings.md` size** â€” `wc -l` on the most recent team
  dir's `findings.md`. Warn at â‰¥180 lines (pending forward-carry
  prune next cycle).
- **Uncaptured agent material** â€” for the most recent team dir, list
  any `agents/*/report.md` whose claims don't yet appear in
  `findings.md` or `uv.md`. That's the `Capture before shutdown, forward-carry at dispatch` capture miss surface.
- **Recent lore** â€” last 5â€“10 `lore/*.md` by date, one-line titles.
  If a recent `session-handoff` exists, quote its "Open threads" and
  "Queued follow-ups" sections verbatim.
- **Recent commits** â€” `git log --oneline -n 15`. Highlight
  promote / demote / reject / correction / findings / carry-forward
  subjects.

## Report

Scannable block, â‰¤80 lines, fixed section order:

```
ACTIVE TEAMS
RECENT TEAM DIRS
CURRENT UV LEDGER
CURRENT FINDINGS SIZE
UNCAPTURED AGENT MATERIAL
RECENT LORE
RECENT COMMITS
```

Empty sections: emit "none" â€” don't suppress the heading.

If anything looks action-worthy (`findings.md` at 195 lines, orphan
UV, team dir with missing reports, unpushed commits > 3, uncaptured
agent material > 0), add a "NEXT ACTIONS" footer (â‰¤5 bullets).


