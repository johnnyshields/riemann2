---
name: research-capture
description: Synchronous coordinator append of a single structural / negative / goodie / gap entry to <team-dir>/findings.md, with provenance, then commit.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Research Capture

Synchronous append of one entry to `<team-dir>/findings.md`. No delegation.
Provenance is mandatory.

`$ARGUMENTS` format: `<section> <one-line summary>`, section \(\in\)
`structural | negative | goodie | gap`. The entry body is provided
inline or in a follow-up message.

Examples:
- `/research-capture negative tangent-separator fails at W=0 inflections`
- `/research-capture goodie reusable quintic normal form at Section 12.3.2`
- `/research-capture gap mixed 4-point factorization still open`
- `/research-capture structural same-tower closure proved in `Git workflow`.2`

## Protocol

Read current `findings.md`. If the same claim already exists, refine its
`Provenance:` instead of adding a duplicate. Append under the right `##`
heading with `Provenance:` always, plus `Do-not-retry:` for Negative
entries.

If the file exceeds 200 lines after this append, run `findings-prune`.

Stage `findings.md` by name and commit
`findings: capture <section> â€” <summary>`. If the entry came out of a
team-dir session, cite the dir in the body.

## Don't

Add entries without provenance. Add a Negative without `Do-not-retry:`.
Add status annotations inside entries â€” presence is the signal, removal
is promotion or rejection.


