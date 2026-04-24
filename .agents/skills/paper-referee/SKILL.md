---
name: paper-referee
description: Two-phase review loop on a paper main TeX file. Phase 1 fixers edit scoped known issues, Phase 2 fresh referees re-review. Phase 1 is an explicit edit-capable exception.
---

# Paper Referee

Two phases in one team dir: Phase 1 fixers edit the paper against known issues; Phase 2 fresh referees re-review without seeing what Phase 1 touched. Phase 1 is the explicit edit-capable exception. See `Dispatch`, `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: empty → fix against latest referee feedback in `lore/`; file path → target that; `--no-referee` → skip Phase 2; `--referee-only` → skip Phase 1; specific issues listed → fix only those.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`, recent referee reports in `lore/`, the paper region at issue.
2. Create `<paper>/teams/<ts>-referee-<slug>/`. Copy prior `findings.md` / `uv.md`, initialize `attempts.md`, prune, add uncaptured material.
3. Write `dispatch.md` with target region, issues, phases, protected surfaces, fixed-harness criteria, ledger contract.

## Phase 1: Fix

Record team name `paper-referee-fix-<ts>` in `dispatch.md`. Spawn the smallest set of scoped fixers needed. Each gets `agents/<ts>-fixer-<slug>/`, `_autoresearch.md`, current `findings.md`, specific UV entries for their region, issue list, self-deposit checklist, non-goals.

**Edit-capable exception.** Fixers may edit `<paper>/<main>.tex` within their scoped region. They still don't edit team ledgers; they surface findings in their reports and the team lead captures.

Keep fixers alive while edits and capture are reviewed. `send_input` for follow-up fixes or narrowed objections. Commit edits with compile-check. Process fixer reports through `Ledger separation` and `Claim lifecycle`; every scoped fix gets an `attempts.md` row or `collation.md` no-action note.

## Phase 2: Re-review (unless `--no-referee`)

Record team name `paper-referee-review-<ts>` in `dispatch.md`, same team dir. Spawn fresh independent read-only referees for the needed angles; full pass uses math and general referees. Don't tell them which issues Phase 1 addressed. Both receive only UV entries in their assigned region, prior referee reports in `lore/`, and the post-fix paper region.

Each returns a verdict in `accept | minor | major | reject`.

## Continuing Cycle

Process Phase 2 reports through `Ledger separation` and `Claim lifecycle`: new issues → `uv.md`, lessons → `findings.md`, verdicts → `attempts.md`, demotions for killed claims, synthesis → `collation.md`. Every verdict row cites the referee report.

Keep fixers/referees alive for follow-up objections, narrowed repairs, adjacent passes. `send_input` to continue dialogue. `close_agent` only at terminal condition, halt, stale team, or clear better replacement. Commit logical units naming the team dir.
