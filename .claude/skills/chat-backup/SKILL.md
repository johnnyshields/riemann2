---
name: chat-backup
description: Dump the current conversation transcript to <paper>/teams/<current-team-dir>/chat.md (or a user-supplied dir). Use mid-session or at wrap to capture the provenance of decisions and agent interactions.
---

# Chat Backup

Capture this session's transcript into the team dir for the cycle that
owns it. Structured summary (no runtime API exposes raw transcripts).

`$ARGUMENTS`: empty → most-recent team dir in `<paper>/teams/` owned by this
cycle; `<paper>/teams/...` path → that specific dir; `--session` → force a
fresh `<paper>/teams/<ts>-other-chat-backup/`.

## Protocol

Resolve destination. If ambiguous (empty argument + multiple candidate
team dirs), this is worth asking about — choosing the wrong dir loses
provenance. With `--session`, create
`<paper>/teams/$(date +%Y%m%d-%H%M%S)-other-chat-backup/`.

Write a structured summary to `<target-dir>/chat.md`:

```markdown
# Chat Backup — <yyyymmdd-hhmmss>

Session cycle: <team-dir slug or "ad-hoc">
Coordinator model: <model name>
Committed SHAs this session: <from `git log --since=... --oneline`>

## Major decisions
## Dispatched teams
## Messages of record  (user directives, quoted)
## Findings captured   (research-capture calls)
## Open threads
```

Never overwrite an existing `chat.md` — append, or create `chat-N.md`.
Scrub secrets before dumping.

Stage by name, commit `chat-backup: <cycle-slug>`.

## When

End of every meaningful session. After a major cycle completes, before
risky actions (promotion, demotion, structural edits).
