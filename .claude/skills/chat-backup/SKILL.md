---
name: chat-backup
description: Dump the current conversation transcript to tasks/<current-task-dir>/chat.md (or a user-supplied dir). Use mid-session or at wrap to capture the provenance of decisions and agent interactions.
---

# Chat Backup

Captures this session's transcript into the task dir for the cycle that
owns it. The per-task-dir provenance story (`CLAUDE.md` §5) includes a
`chat.md` file; this skill is how it gets written.

## Arguments

`$ARGUMENTS`:

- **empty** — backup to the most-recently-created task dir in `tasks/`
  (default: the one the current coordinator cycle is writing into).
- **task-dir path** (e.g. `tasks/20260423-020000-attack-gap-uv002/`) —
  backup to that specific dir.
- **`--session`** — force a fresh session-level backup at
  `tasks/<ts>-other-chat-backup/chat.md` instead of targeting an
  existing task dir. Useful for ad-hoc sessions not tied to a cycle.

## Protocol

### Step 1: Resolve the destination

- If `$ARGUMENTS` is a path: use it; verify the dir exists. If not,
  error rather than silently creating.
- If `$ARGUMENTS` is empty: find the most recent `tasks/*/` by mtime
  that doesn't already have a `chat.md`, or the one explicitly owned
  by this coordinator cycle. If ambiguous, surface a short list via
  `AskUserQuestion` (this IS a major decision — choosing the wrong dir
  loses provenance).
- If `--session`: create `tasks/$(date +%Y%m%d-%H%M%S)-other-chat-backup/`.

### Step 2: Dump the transcript

There is no runtime API exposed for "dump the current conversation" in
Claude Code. The practical implementation:

1. The coordinator writes a structured summary of the session into
   `<target-dir>/chat.md`. Structure:

   ```markdown
   # Chat Backup — <yyyymmdd-hhmmss>

   Session cycle: <task-dir slug or "ad-hoc">
   Coordinator model: <model name>
   Committed SHAs this session: <list from `git log --since=<session-start>
     --oneline`>

   ## Major decisions
   <one bullet per real decision made in the session>

   ## Dispatched teams
   <one entry per TeamCreate with the team_name and teammates>

   ## Messages of record
   <user directives that shaped the session, quoted verbatim>

   ## Findings captured
   <list of research-capture calls this session, if any>

   ## Open threads
   <anything left incomplete for a future session>
   ```

2. If the runtime exposes a raw transcript (e.g. via an
   `Export`-style mechanism available in future versions), prefer
   that — attach the raw file at `<target-dir>/chat-raw.md` and keep
   the structured summary alongside. As of this writing, no such API is
   exposed, so the structured summary is the full backup.

3. If the user previously opted into a different backup mechanism
   (e.g. an OS-level session log at a known path), the coordinator
   should reference that in `chat.md` instead of re-dumping.

### Step 3: Stage and commit

```sh
git add <target-dir>/chat.md
git commit -m "chat-backup: <session-cycle-slug>"
```

## When to run

- **End of session**: always, unless the session produced no meaningful
  decisions. A session without a chat backup lost provenance.
- **Mid-session**: after a major cycle completes (e.g. after
  `research-team` finishes). Captures the decisions of that cycle
  before context compaction risks losing details.
- **Before risky actions**: prior to a promotion / demotion / big
  structural edit, so the decision trail is preserved even if the
  action itself goes wrong.

## Anti-patterns

- Do NOT back up routine exchanges or tool-use-only turns. The summary
  should focus on decisions and directives, not mechanical steps.
- Do NOT overwrite an existing `chat.md` in a task dir. Append, or
  create a `chat-N.md` sibling.
- Do NOT commit user messages that contain secrets, credentials, or
  personal data. Scrub before dumping.
