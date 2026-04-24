---
name: research-resume
description: Continue research-team from an existing <paper>/teams/<ts>-<slug>/ directory. Same adaptive roster, one-ahead verification pattern, briefing, capture, and provenance rules as research-team; the only difference is that it reuses the existing team dir and creates only new agent subdirs.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Resume

Resume is `research-team` run in an existing team dir. Same adaptive roster,
one-ahead verifier queue, briefing, capture, long-lived-agent behavior,
autoresearch loop, and promotion discipline. The only difference: do not create
a sibling team dir. Reuse the supplied team dir and create fresh
`agents/<resume-ts>-<agent-slug>/` subdirs.

`$ARGUMENTS`: existing `<paper>/teams/<ts>-<slug>/` path; optional focus text
such as `UV-NNN`, `rem:wip-*`, or a route name. If no focus is given, choose the
most blocking frontier from the existing dir without asking for approval.

## Preamble

1. Resolve the existing team dir. It must be the working team snapshot for this
   cycle. Do not create a new team dir.
2. Read `findings.md`, `uv.md`, `attempts.md` if present, `dispatch.md`,
   `collation.md`, `paper-updates.md` if present, current `rem:wip-*` labels,
   last 2-3 relevant lore entries, and every `agents/*/report.md`.
3. Capture useful material stranded only in reports before dispatch: update
   `findings.md`, `uv.md`, `attempts.md`, or `collation.md`.
4. Initialize missing stubs only inside the existing team dir.
5. Append `## Resume dispatch <timestamp>` to `dispatch.md` with the current
   commit, roster, verifier queue if any, targets, exact in-scope
   files/lines/reports, protected surfaces, non-goals, fixed-harness criteria,
   ground-truth checks, and budgets/timeouts. Commit the resume checkpoint by
   named paths.

## Dispatch

When delegated teamwork is authorized, record team name
`research-resume-<existing-ts-or-slug>-<resume-ts>` in `dispatch.md`. Use the
same dispatch rules as `research-team`: spawn the coordinator-selected live
roster, keep research/exploration lanes moving, and add verifier/source-auditor
lanes when a stable prior deposit is ready to check or risk demands it. Each
fresh teammate gets a new work dir:

`<existing-team-dir>/agents/<resume-ts>-<agent-slug>/`

Never reuse an old agent dir. Keep all existing team files authoritative.

Every briefing matches `research-team`: full autoresearch metaprompt, full
`findings.md`, 9-field report schema, non-goals, exact deposit path,
self-deposit checklist, `Writing discipline`, and role-specific UV/report
exceptions.

Do not ask for approval. Pick the roster and targets from the recovered
frontier, then proceed.

## Continuing Cycle

Same as `research-team`, but all capture stays in the existing team dir.

1. Verify each returning agent deposited `report.md` plus cited `scripts/` and
   `notes/`. Chase missing deposits via `send_input`; record unanswered gaps in
   `collation.md`.
2. Walk each report. Process through `Claim lifecycle (git-as-archive)`,
   update `attempts.md`, refresh `Frontier summaries`, and commit logical units
   by named paths.
3. Maintain the one-ahead pipeline: queue verification for stable claims that
   need checking while independent research/exploration teammates continue the
   next attack. Wait only when the next move depends on the verifier's answer.
4. Respond to each agent with a concrete follow-up, adversarial challenge, or
   next adjacent task. Use `send_input` when that teammate's context is useful.
5. Write `paper-updates.md` only for paper-ready edits. No direct `<main>.tex`
   edits here.

Do not shut down agents at ordinary cycle boundaries. Keep the resumed team
alive for continuity. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when replacement is clearly better.
