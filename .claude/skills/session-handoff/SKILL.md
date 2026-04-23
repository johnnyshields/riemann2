---
name: session-handoff
description: End-of-session writeup producing a lore entry that summarizes team dirs opened, UV movements, findings changes, queued follow-ups, and open threads. Makes cross-session handoff clean so the next session can resume without reconstructing state.
---

# Session Handoff

Structured end-of-session lore entry. Pairs with the auto-push rule so
the next session starts current.

`$ARGUMENTS`: empty → cover since the last handoff; `--since <ref>` →
git ref or ISO date; `--note "<text>"` → free-text addendum.

## Gather

Commits since `<since>` (`git log --since=... --oneline`). Team dirs
opened or touched (`find <paper>/teams/ -maxdepth 1 -type d -newer
<marker>`). UV and findings changes across the team dirs' `uv.md`
and `findings.md`. Paper edits to `<main>.tex` with stats. Active
teams (should be none — close any that survived).

## Write

Path: `lore/<yyyymmdd>-session-handoff.md` (append `-N` if a handoff
already exists today). Structure:

```markdown
# Session Handoff — <yyyymmdd>

Since: <ref>   Commits: N (<first>..<last>)   Pushed: yes / N

## What happened
<one-paragraph theme — not a commit recap>

## Team dirs opened / touched
| Path | Team-slug | Status |

## UV ledger changes
- Added / Promoted / Demoted / Rejected / Refined: one bullet each

## findings.md changes
- Added / Removed

## Paper edits
- <§ref> — one line

## Open threads (for next session)
## Queued follow-ups
## Coordinator notes
```

Don't produce a commit-by-commit recap (git log is that already).
Capture synthesis: themes, decisions, open threads. Never omit "Open
threads" even when nothing is blocked — small continuity notes matter.

## Commit + push

Stage by name, commit `lore: session handoff <yyyymmdd> — <theme>`, and
push any trailing unpushed commits (handoff should always hit the
remote).

## Close teams

If any team is still alive, `SendMessage` each a brief "session ending"
notice and `TeamDelete`. No zombie teams across sessions unless the
user explicitly wants a background watcher.

Finish with a ≤10-line summary to the user covering the handoff theme
and any follow-up needing attention before session end.
