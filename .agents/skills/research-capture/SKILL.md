---
name: research-capture
description: Synchronous coordinator append of a single structural / negative / goodie / gap entry to <team-dir>/findings.md, with provenance, then commit.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Capture

Synchronous append of one entry to `<team-dir>/findings.md`. No delegation.
Provenance is mandatory. Use this only for durable briefable knowledge; route
history belongs in `attempts.md`, live missing sub-statements in `uv.md`, and
no-action rationale in `collation.md`.

`$ARGUMENTS` format: `<section> <one-line summary>`, section in
`structural | negative | goodie | gap`. The entry body is provided inline or in
a follow-up message.

Examples:
- `/research-capture negative tangent-separator fails at W=0 inflections`
- `/research-capture goodie reusable quintic normal form at Section 12.3.2`
- `/research-capture gap mixed 4-point factorization still open`

## Protocol

Read current `findings.md`. If the same claim already exists, refine its
`Provenance:` instead of adding a duplicate. Append under the right `##`
heading with `Provenance:` always, plus `Do-not-retry:` for Negative entries.

If the file exceeds 200 lines after this append, run `findings-prune`.

Stage `findings.md` by name and commit `findings: capture <section> - <summary>`.
If the entry came out of a team-dir session, cite the dir in the body.

## Don't

Add entries without provenance. Add a Negative without `Do-not-retry:`. Add
route-history rows or duplicate UV text. Add status annotations inside entries:
presence is the signal, removal is promotion or rejection.
