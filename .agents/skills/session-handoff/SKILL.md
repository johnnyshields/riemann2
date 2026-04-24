---
name: session-handoff
description: End-of-session writeup producing a lore entry that summarizes team dirs opened, UV movements, findings changes, attempts/frontier changes, queued follow-ups, and open threads. Makes cross-session handoff clean.
---

# Session Handoff

Structured end-of-session lore entry. Pairs with auto-push so the next session starts current.

`$ARGUMENTS`: empty → cover since last handoff; `--since <ref>` → git ref or ISO date; `--note "<text>"` → free-text addendum.

## Gather

Commits since `<since>`. Team dirs opened or touched. UV / findings changes across team dirs. Route/frontier changes from `attempts.md`; no-action rationale, verifier queue, one-ahead lane, ledger-gate defects from `collation.md`. Paper edits to `<main>.tex` with stats. Active teams (close unless the user wants them left running).

## Write

Path: `lore/<yyyymmdd>-session-handoff.md` (append `-N` if needed).

```markdown
# Session Handoff - <yyyymmdd>

Since: <ref>   Commits: N (<first>..<last>)   Pushed: yes / N

## What happened
<one-paragraph theme, not a commit recap>

## Team dirs opened / touched
| Path | Team-slug | Status |

## UV ledger changes
- Added / Promoted / Demoted / Rejected / Refined: one bullet each

## findings.md changes
- Added / Removed

## attempts.md / frontier changes
- Keep / Discard / Blocked / Terminal / Crash counts; current best; next lane

## Collation notes
- No-action rationale / verifier queue / one-ahead research lane
- Ledger-gate defects or "clean"

## Paper edits
- <section ref> - one line

## Open threads (for next session)
## Queued follow-ups
## Coordinator notes
```

No commit-by-commit recap. Capture synthesis: themes, decisions, open threads, what should be resumed. Never omit "Open threads".

## Commit + Push

Stage by name, commit `lore: session handoff <yyyymmdd> - <theme>`, push trailing unpushed commits.

## Close Teams

If any team is still alive, `send_input` each a brief session-ending notice and `close_agent`, unless the user wants a background watcher.

Finish with a ≤10-line summary covering the handoff theme and any follow-up needing attention before session end.
