---
name: paper-demote
description: Structured reverse-promotion. Remove or weaken a claim currently in a paper main TeX file, reinstate a UV-NNN entry in the team uv.md, and optionally capture a negative finding in one atomic commit. Use when a promoted claim turns out to be wrong or weaker than stated.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Demote

Atomic reverse-promotion: paper edit, UV reinstatement, and optional negative
capture in one commit.

`$ARGUMENTS`:
- `<label-or-region>` - what to demote, resolved by the coordinator.
- `--weaken` - keep a scoped weaker form in the paper; the original strong
  statement becomes the new UV entry.
- `--reason "<text>"` - appears in the commit body and the new UV's explanation.

## Protocol

Before anything, broadcast the correction to every active agent working on the
affected claim with `send_input`.

Edit `<paper>/<main>.tex`. With `--weaken`, replace the stronger statement with
the scoped form and keep the label if still apt; otherwise delete the claim and
proof, then fix every reference to deleted labels. Add a new
`rem:wip-demoted-<slug>` remark pointing at the new UV entry.

Add the new UV-NNN (next available, monotonic) to `<team-dir>/uv.md`. Include
source label, claim, current role / needed-for-promotion, dependency refs if
known, and provenance. Put the original stronger claim in the claim field so
future work can retry.

If the demote produced a reusable "do not retry this route" lesson, capture it
as a Negative finding in the same commit. If it also produced a route outcome,
log that outcome in `attempts.md`; put no-action rationale in `collation.md`.

Compile-check runs via the pre-commit hook.

## Commit

Single atomic commit. Stage `<paper>/<main>.tex`, `<team-dir>/uv.md`, and any
`findings.md` / `attempts.md` / `collation.md` changes by name. Subject
`demote <label-or-UV>: <reason>`. Body: what was removed or weakened, the new
UV-NNN, and any team dir whose adversarial report triggered it.

If teams are still active, `send_input` each a short correction notice so they
do not build on the demoted claim.

## Don't

Demote without a trigger. Reuse an old UV-NNN ID. Split the edit, reinstatement,
and capture across commits. Bypass the compile-check.
