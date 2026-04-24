---
name: chat-backup
description: Write a structured current-session chat/provenance summary to a paper team directory chat.md or a user-supplied directory. Use mid-session or at wrap to capture decisions, user directives, and agent interactions when raw Codex transcripts are unavailable.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Chat Backup

Capture this session's decision trail into the team dir for the cycle that owns
it. Prefer a raw Codex/ChatGPT export when supplied; otherwise write a
structured summary because raw transcripts are not stable across runtimes.

`$ARGUMENTS`: empty -> most recent active-looking team dir; `<paper>/teams/...`
path -> that dir; `--session` -> create a fresh ad-hoc session team dir.

## Protocol

Resolve destination. If ambiguous, choose the most recent active-looking team
dir and record the rationale in `chat.md`; do not ask for approval. With
`--session`, create `<paper>/teams/<ts>-other-chat-backup/` with standard stubs:
`findings.md`, `uv.md`, `attempts.md`, `dispatch.md`, `collation.md`, and
`agents/`.

Write a structured summary to `<target-dir>/chat.md`:

```markdown
# Chat Backup - <yyyymmdd-hhmmss>

Session cycle: <team-dir slug or "ad-hoc">
Coordinator model: <model name>
Codex thread/export: <path if available, else "not exported">
Committed SHAs this session: <from git log>

## Major decisions
## Dispatched teams
## Messages of record (user directives, quoted)
## Findings captured
## UV / attempts / collation updates
## Open threads
```

Never overwrite an existing `chat.md`; append or create `chat-N.md`. Scrub
secrets before dumping.

`chat.md` is secondary provenance. Any mathematical or computational claim still
needs an on-disk report, script, UV entry, finding, lore entry, or paper edit
with exact refs.

Stage by name and commit `chat-backup: <cycle-slug>`.

## When

End of every meaningful session. After a major cycle completes, before risky
actions such as promotion, demotion, or structural edits.
