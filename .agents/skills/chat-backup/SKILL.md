---
name: chat-backup
description: Write a structured current-session chat/provenance summary to a paper team directory chat.md or a user-supplied directory. Use mid-session or at wrap to capture decisions, user directives, and agent interactions when raw Codex transcripts are unavailable.
---

# Chat Backup

Capture this session's decision trail into the team dir for the cycle that owns it. Prefer a raw Codex/ChatGPT export when supplied; otherwise write a structured summary because raw transcripts aren't stable across runtimes.

`$ARGUMENTS`: empty → most recent active-looking team dir; `<paper>/teams/...` path → that dir; `--session` → fresh ad-hoc session team dir.

## Protocol

Resolve destination. If ambiguous, pick the most recent active-looking team dir and record the rationale in `chat.md`; don't ask. With `--session`, create `<paper>/teams/<ts>-other-chat-backup/` with standard stubs (`findings.md`, `uv.md`, `attempts.md`, `dispatch.md`, `collation.md`, `agents/`).

Write to `<target-dir>/chat.md`:

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

Never overwrite an existing `chat.md`; append or create `chat-N.md`. Scrub secrets first.

`chat.md` is secondary provenance. Math/computational claims still need an on-disk report, script, UV entry, finding, lore entry, or paper edit with exact refs.

Stage by name and commit `chat-backup: <cycle-slug>`.

## When

End of meaningful sessions. After major cycles, before risky actions (promote/demote/structural).
