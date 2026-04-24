---
name: cycle-status
description: Snapshot of the current research state including active teams, recent team dirs, UV entries with dependencies, ledger health, and open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Cycle Status

Single-call orientation. Read-only. No delegation, no edits, no commits.

`$ARGUMENTS`: empty -> full snapshot; `--paper <name>` -> limit to one paper;
`--recent <N>` -> limit to last N days (default 7); `--uv-only` /
`--teams-only` -> filter.

## Gather

- **Active teams** via current Codex subagent handles when available; otherwise
  infer live work from newest `dispatch.md` / `collation.md` and unclosed agent
  reports.
- **Recent team dirs** for each `<paper>` in the repo. For each dir: paper,
  team-slug, landed vs expected agent reports from `dispatch.md`, and
  `collation.md` summary line if present.
- **Current UV ledger** from the most recent team dir's `uv.md`. Flag
  critical-path entries, orphan labels missing from `<main>.tex`, and suspected
  dependency cycles.
- **Current `findings.md` size** via line count. Warn at >=180 lines and treat
  >=200 as prune work.
- **Ledger health** for the most recent team dir: `attempts.md` exists, uses the
  markdown route table, and has a short frontier summary. Flag legacy
  `attempts.tsv`, top-level `<paper>/findings.md`, `<paper>/unverified.tex`, or
  parallel ledgers as migration work, not authoritative state. Also flag report
  deposits with no `attempts.md` row and no `collation.md` no-action note.
- **Uncaptured agent material**: reports whose claims do not appear in
  `findings.md`, `uv.md`, `attempts.md`, or `collation.md`. This is the capture
  miss surface.
- **Recent lore**: last 5-10 `lore/*.md` by date. If a recent
  `session-handoff` exists, quote its "Open threads" and "Queued follow-ups".
- **Recent commits**: `git log --oneline -n 15`. Highlight promote, demote,
  reject, correction, findings, and carry-forward subjects.

## Report

Scannable block, <=80 lines, fixed section order:

```text
ACTIVE TEAMS
RECENT TEAM DIRS
CURRENT UV LEDGER
CURRENT FINDINGS SIZE
LEDGER HEALTH
UNCAPTURED AGENT MATERIAL
RECENT LORE
RECENT COMMITS
```

Empty sections: emit "none"; do not suppress the heading. If anything looks
action-worthy (`findings.md` at 195 lines, orphan UV, legacy ledger still
active, missing report-route capture, unpushed commits > 3, uncaptured
material), add a `NEXT ACTIONS` footer with at most 5 bullets.
