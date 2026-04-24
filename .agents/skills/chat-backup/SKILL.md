---
name: chat-backup
description: Write a structured current-session chat/provenance summary to <paper>/teams/<current-team-dir>/chat.md (or a user-supplied dir). Use mid-session or at wrap to capture decisions, user directives, and agent interactions when raw Codex transcripts are unavailable.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Chat Backup

Capture this session's decision trail into the team dir for the cycle that
owns it. Prefer a raw Codex/ChatGPT export when the user supplies one; otherwise
write a structured summary because no stable runtime API exposes raw transcripts.

`$ARGUMENTS`: empty â†’ most-recent team dir in `<paper>/teams/` owned by this
cycle; `<paper>/teams/...` path â†’ that specific dir; `--session` â†’ force a
fresh `<paper>/teams/<ts>-other-chat-backup/`.

## Protocol

Resolve destination. If ambiguous (empty argument + multiple candidate
team dirs), choose the most recent active-looking team dir and record the
rationale in `chat.md`; do not ask for approval. With `--session`, create
`<paper>/teams/$(date +%Y%m%d-%H%M%S)-other-chat-backup/`.

Write a structured summary to `<target-dir>/chat.md`:

```markdown
# Chat Backup â€” <yyyymmdd-hhmmss>

Session cycle: <team-dir slug or "ad-hoc">
Coordinator model: <model name>
Codex thread/export: <path if available, else "not exported">
Committed SHAs this session: <from `git log --since=... --oneline`>

## Major decisions
## Dispatched teams
## Messages of record  (user directives, quoted)
## Findings captured   (research-capture calls)
## Open threads
```

Never overwrite an existing `chat.md` â€” append, or create `chat-N.md`.
Scrub secrets before dumping.

`chat.md` is secondary provenance. Any mathematical or computational claim
still needs an on-disk report, script, UV entry, finding, lore entry, or paper
edit with its own exact refs.

Stage by name, commit `chat-backup: <cycle-slug>`.

## When

End of every meaningful session. After a major cycle completes, before
risky actions (promotion, demotion, structural edits).


