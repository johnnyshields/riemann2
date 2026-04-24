---
name: cycle-status
description: Snapshot of the current research state including active teams, recent team dirs, UV entries with dependencies, ledger health, and open threads from recent lore. Run at session start or mid-session to orient without re-reading everything.
---

# Cycle Status

Single-call orientation. Read-only. No delegation, edits, or commits.

`$ARGUMENTS`: empty → full snapshot; `--paper <name>` → one paper; `--recent <N>` → last N days (default 7); `--uv-only` / `--teams-only` → filter.

## Gather

- **Active teams** via current Codex subagent handles when available; otherwise infer from newest `dispatch.md` / `collation.md` and unclosed agent reports.
- **Recent team dirs** per `<paper>`: paper, team-slug, landed vs expected reports from `dispatch.md`, `collation.md` summary line if present.
- **Current UV ledger** from the most recent team dir's `uv.md`. Flag critical-path entries, orphan labels missing from `<main>.tex`, suspected dependency cycles.
- **`findings.md` size** via line count. Warn ≥180, treat ≥200 as prune work.
- **Ledger health** for the most recent team dir: `attempts.md` exists, uses the markdown route table, has a frontier summary. Flag legacy `attempts.tsv`, top-level `<paper>/findings.md`, `<paper>/unverified.tex`, or parallel ledgers as migration work. Flag report deposits with no `attempts.md` row and no `collation.md` no-action note.
- **Uncaptured agent material** — reports whose claims don't appear in `findings.md` / `uv.md` / `attempts.md` / `collation.md`. Capture-miss surface.
- **Recent lore** — last 5–10 `lore/*.md` by date. If a recent `session-handoff` exists, quote its "Open threads" and "Queued follow-ups".
- **Recent commits** — `git log --oneline -n 15`. Highlight promote / demote / reject / correction / findings / carry-forward subjects.

## Report

Scannable, ≤80 lines, fixed section order:

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

Empty sections: emit "none" — don't suppress the heading. If anything looks action-worthy (`findings.md` at 195, orphan UV, legacy ledger active, missing report capture, unpushed >3, uncaptured material), add a `NEXT ACTIONS` footer with ≤5 bullets.
