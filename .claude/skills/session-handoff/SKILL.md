---
name: session-handoff
description: End-of-session writeup producing a lore entry that summarizes task dirs opened, UV movements, findings changes, queued follow-ups, and open threads. Makes cross-session handoff clean so the next session can resume without reconstructing state.
---

# Session Handoff

Structured end-of-session lore entry. See `CLAUDE.md` §2 (lore role),
§5 (task dirs), §6 (claim lifecycle), §11 (auto-push — trailing commits
get pushed at session end).

## When to run

- End of a working session.
- Before a planned long gap (overnight, over-weekend, travel).
- Before a major model-context switch (if switching between
  Opus/Sonnet/etc. mid-project).
- After a milestone cycle completes (even if session continues — a
  handoff at the milestone is a clean commit boundary).

## Arguments

`$ARGUMENTS` (optional):

- **empty** — full auto-summary covering everything since the last
  handoff.
- `--since <ref>` — start point: a git ref or ISO date. Default is the
  most recent prior `session-handoff` lore entry, or start-of-day if
  none.
- `--note "<text>"` — free-text addendum from the user (something they
  want recorded that isn't captured automatically).

## Protocol

### Step 1: Gather session state

```sh
# Commits this session
git log --since="<since>" --oneline

# Task dirs opened or touched this session
find tasks/ -maxdepth 1 -type d -newer "<since-marker>"

# UV entries changed
git log --since="<since>" -- paper/unverified.tex | head -40

# Findings entries changed
git log --since="<since>" -- paper/findings.md | head -40

# Paper edits
git log --since="<since>" -- paper/proof_of_rh.tex --stat | head -20
```

Also inspect:

- Active teams via `TeamList` (if any survived the session — usually
  none should).
- Pending `unverified.tex` entries whose status changed (open ↔
  heuristic, or newly added, or removed / promoted).
- Any `rem:wip-*` label that moved (renamed or relocated).

### Step 2: Draft the lore entry

Path: `lore/<yyyymmdd>-session-handoff.md` (today's date; if a prior
handoff exists on the same date, append `-N` suffix).

Structure:

```markdown
# Session Handoff — <yyyymmdd>

Since: <git-ref or ISO date>
Commits: <N>  (range `<first>..<last>`)
Pushed: <yes / no — count of commits pushed>

## What happened

<one-paragraph natural-language summary of the session's main
theme — not a commit-by-commit recap>

## Task dirs opened / touched

| Path | Type | Status |
|---|---|---|
| tasks/<ts>-<type>-<slug>/ | attack-gap | closed — promoted UV-003 |
| ... | ... | ... |

## UV ledger changes

- **Added**: UV-NNN (title, one-line why).
- **Promoted**: UV-NNN → §<ref> (landed at commit <SHA>).
- **Demoted**: <paper label> → UV-NNN.
- **Rejected**: UV-NNN (short reason).
- **Refined**: UV-NNN (what changed).

## findings.md changes

- **Added**: Structural / Negative / Goodies / Gap bullets.
- **Removed**: (on promotion or rejection).

## Paper edits

- <§ref> — one-line what changed (add / revise / remove / demote).

## Open threads (for next session)

- <thread 1 with enough context to resume>
- <thread 2>

## Queued follow-ups

- <concrete TODO for next session, with pointer to a task dir or UV if
  applicable>

## Coordinator notes

- <any ambient observation worth preserving — working patterns, model
  quirks observed, adjacent ideas to explore>

<-- end lore entry -->
```

### Step 3: Commit + push

```sh
git add lore/<yyyymmdd>-session-handoff.md
git commit -m "lore: session handoff <yyyymmdd> — <one-line theme>"
```

Per `CLAUDE.md` §11 auto-push rule: push trailing commits now if any
are unpushed. Handoff entries should always hit the remote.

### Step 4: Broadcast (if any team is still active)

If `TeamList` shows active teammates, `SendMessage` each a short
"session ending" notice and gracefully `TeamDelete`. No zombie teams
across sessions.

### Step 5: Report to the user

Short summary (≤ 10 lines) covering the handoff theme and any
queued follow-up that benefits from user attention before the session
ends.

## Anti-patterns

- Do NOT produce a commit-by-commit recap — git log is already that.
  The lore entry captures synthesis: themes, decisions, open threads.
- Do NOT leave active teams running across sessions unless the user
  explicitly wants a background watcher.
- Do NOT omit the "Open threads" section just because nothing is
  blocked — next-session-you will thank you for writing down even small
  continuity notes.
