---
name: chat-backup
description: Dump the current conversation transcript to <paper>/teams/<current-team-dir>/chat.md (or a user-supplied dir). Use mid-session or at wrap to capture the provenance of decisions and agent interactions.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Chat Backup

Capture this session's transcript into the team dir for the cycle that
owns it. Structured summary (no runtime API exposes raw transcripts).

`$ARGUMENTS`: empty â†’ most-recent team dir in `<paper>/teams/` owned by this
cycle; `<paper>/teams/...` path â†’ that specific dir; `--session` â†’ force a
fresh `<paper>/teams/<ts>-other-chat-backup/`.

## Protocol

Resolve destination. If ambiguous (empty argument + multiple candidate
team dirs), this is worth asking about â€” choosing the wrong dir loses
provenance. With `--session`, create
`<paper>/teams/$(date +%Y%m%d-%H%M%S)-other-chat-backup/`.

Write a structured summary to `<target-dir>/chat.md`:

```markdown
# Chat Backup â€” <yyyymmdd-hhmmss>

Session cycle: <team-dir slug or "ad-hoc">
Coordinator model: <model name>
Committed SHAs this session: <from `git log --since=... --oneline`>

## Major decisions
## Dispatched teams
## Messages of record  (user directives, quoted)
## Findings captured   (research-capture calls)
## Open threads
```

Never overwrite an existing `chat.md` â€” append, or create `chat-N.md`.
Scrub secrets before dumping.

Stage by name, commit `chat-backup: <cycle-slug>`.

## When

End of every meaningful session. After a major cycle completes, before
risky actions (promotion, demotion, structural edits).


