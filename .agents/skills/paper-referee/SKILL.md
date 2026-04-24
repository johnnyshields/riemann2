---
name: paper-referee
description: Two-phase review loop on <paper>/<main>.tex: Phase 1 fixers edit scoped known issues, Phase 2 fresh referees re-review. Phase 1 is an explicit edit-capable exception.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Referee

Two phases in one team dir: Phase 1 fixers edit the paper against known issues;
Phase 2 fresh referees re-review without seeing what Phase 1 touched. Phase 1
is the explicit edit-capable exception to the read-only default. Follow
`.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch`,
`Briefing rule`, `Team dirs and agent self-deposit`, `State ledger separation`,
and `Capture before shutdown, forward-carry at dispatch`.

`$ARGUMENTS`: empty -> fix against latest referee feedback in `lore/`; file
path -> target that; `--no-referee` -> skip Phase 2; `--referee-only` -> skip
Phase 1; specific issues listed -> fix only those.

## Preamble

1. Read the most recent team dir's `findings.md` and `uv.md`, recent referee
   reports in `lore/`, and the paper region at issue.
2. Create `<paper>/teams/<ts>-referee-<slug>/`. Copy prior `findings.md` and
   `uv.md`, initialize `attempts.md`, prune, and add uncaptured material.
3. Write `dispatch.md` describing target region, issues, phases, protected
   surfaces, and fixed-harness criteria.

## Phase 1: Fix

When delegated teamwork is authorized, record team name `paper-referee-fix-<ts>`
in `dispatch.md`. Spawn the smallest set of scoped fixers needed for the issue
list. Each gets `agents/<ts>-fixer-<slug>/`, the autoresearch metaprompt,
current `findings.md`, specific UV entries for their region, issue list,
self-deposit checklist, and non-goals.

**Edit-capable exception.** Fixers may edit `<paper>/<main>.tex` within their
scoped region. They still do not edit team ledgers; they surface new findings in
their reports, and the team lead captures them.

Keep fixers alive while paper edits and report capture are reviewed. Use
`send_input` for follow-up fixes or narrowed objections. Commit paper edits
with compile-check. Process fixer reports through `State ledger separation` and
`Claim lifecycle (git-as-archive)`.

## Phase 2: Re-review, unless `--no-referee`

When delegated teamwork is authorized, record team name
`paper-referee-review-<ts>` in `dispatch.md` using the same team dir. Spawn
fresh, independent read-only referees for the needed angles; a full pass uses
math and general referees. Do not tell them which issues Phase 1 addressed.
Both receive only UV entries in their assigned region, prior referee reports in
`lore/`, and the post-fix paper region.

Each returns a verdict in `accept | minor | major | reject`.

## Continuing Cycle

Process Phase 2 reports through `State ledger separation` and `Claim lifecycle
(git-as-archive)`: new issues to `uv.md`, durable lessons to `findings.md`,
route/verdict outcomes to `attempts.md`, demotions for killed claims, and
synthesis to `collation.md`.

Keep fixers/referees alive for follow-up objections, narrowed repairs, and
adjacent referee passes while their context is fresh. Use `send_input` to
continue the dialogue. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when replacement is clearly better. Commit
logical units naming the team dir.
