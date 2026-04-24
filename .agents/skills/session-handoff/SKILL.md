---
name: session-handoff
description: End-of-session writeup producing a lore entry that summarizes team dirs opened, UV movements, findings changes, queued follow-ups, and open threads. Makes cross-session handoff clean so the next session can resume without reconstructing state.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Session Handoff

Structured end-of-session lore entry. Pairs with the auto-push rule so
the next session starts current.

`$ARGUMENTS`: empty â†’ cover since the last handoff; `--since <ref>` â†’
git ref or ISO date; `--note "<text>"` â†’ free-text addendum.

## Gather

Commits since `<since>` (`git log --since=... --oneline`). Team dirs
opened or touched (`find <paper>/teams/ -maxdepth 1 -type d -newer
<marker>`). UV and findings changes across the team dirs' `uv.md`
and `findings.md`. Paper edits to `<main>.tex` with stats. Active
teams (should be none â€” close any that survived).

## Write

Path: `lore/<yyyymmdd>-session-handoff.md` (append `-N` if a handoff
already exists today). Structure:

```markdown
# Session Handoff â€” <yyyymmdd>

Since: <ref>   Commits: N (<first>..<last>)   Pushed: yes / N

## What happened
<one-paragraph theme â€” not a commit recap>

## Team dirs opened / touched
| Path | Team-slug | Status |

## UV ledger changes
- Added / Promoted / Demoted / Rejected / Refined: one bullet each

## findings.md changes
- Added / Removed

## Paper edits
- <Â§ref> â€” one line

## Open threads (for next session)
## Queued follow-ups
## Coordinator notes
```

Don't produce a commit-by-commit recap (git log is that already).
Capture synthesis: themes, decisions, open threads. Never omit "Open
threads" even when nothing is blocked â€” small continuity notes matter.

## Commit + push

Stage by name, commit `lore: session handoff <yyyymmdd> â€” <theme>`, and
push any trailing unpushed commits (handoff should always hit the
remote).

## Close teams

If any team is still alive, `send_input` each a brief "session ending"
notice and `close_agent`. No zombie teams across sessions unless the
user explicitly wants a background watcher.

Finish with a â‰¤10-line summary to the user covering the handoff theme
and any follow-up needing attention before session end.


