---
name: paper-referee
description: Two-phase review loop on <paper>/<main>.tex â€” Phase 1 fixers edit the paper to address known issues, Phase 2 fresh referees re-review. Phase 1 is an explicit edit-capable exception.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Referee

Two phases in one team dir: Phase 1 fixers edit the paper against known
issues; Phase 2 fresh referees re-review without seeing what Phase 1
touched. Phase 1 is the explicit edit-capable exception to the
read-only default. Follows `.agents/references/agents/_autoresearch.md`, AGENTS.md
`Dispatch` long-lived-agent rules, `Briefing rule`, `Team dirs and agent
self-deposit`, and `Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default.

`$ARGUMENTS`: empty â†’ fix against latest referee feedback in `lore/`;
file path â†’ target that; `--no-referee` â†’ skip Phase 2;
`--referee-only` â†’ skip Phase 1; specific issues listed â†’ fix only
those.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`, recent
   referee reports in `lore/`, and the paper region at issue.
2. Create `<paper>/teams/<ts>-referee-<slug>/`. Copy prior
   `findings.md` + `uv.md` in; prune; add any uncaptured material.
3. Write `dispatch.md` describing target region, issues, phases.

## Phase 1 (fix)

When delegated teamwork is authorized, record team name `paper-referee-fix-<ts>` in `dispatch.md`. Spawn up to 3
fixers (`role prompt: fixer`, inherited Codex model) named for their content area
(e.g. `fixer-local-geometry`, `fixer-finite-s-algebra`,
`fixer-endgame`). Each gets its own `agents/<ts>-fixer-<slug>/`
subdir and the full `.agents/references/agents/_autoresearch.md` metaprompt.

Briefing per fixer: the current team dir's `findings.md`, the specific
UV entries for their region (narrow `Briefing rule` exception), the issue list,
the self-deposit checklist. Non-goals: no rewrite beyond assigned
issues; no new lemmas without a UV entry.

**Edit-capable exception.** Fixers may edit `<paper>/<main>.tex`
within their scoped region. They still do **not** edit the team dir's
`findings.md` / `uv.md` / `paper-updates.md` â€” surface new findings in
their reports, the team lead handles capture (`Capture before shutdown, forward-carry at dispatch`).

Keep the fix team alive while paper edits and report capture are reviewed; use
`send_input` for follow-up fixes or narrowed objections. Commit paper edits
(pre-commit compile-check applies). Process fixer reports through `Claim lifecycle (git-as-archive)` capture. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when Phase 2 needs fresh independence.

## Phase 2 (re-review, unless `--no-referee`)

When delegated teamwork is authorized, record team name `paper-referee-review-<ts>` in `dispatch.md` (same team dir,
new Codex subagents). Spawn two referees read-only (`role prompt: referee`,
inherited Codex model) with the full `.agents/references/agents/_autoresearch.md` metaprompt:

- **`referee-math`** â€” pure-math standard: proofs, hypotheses,
  circularity, citations.
- **`referee-general`** â€” clarity, accessibility, flow, overclaim.

Briefing: the paper region post-fix (do NOT tell them which issues
Phase 1 addressed â€” that biases them toward rubber-stamping). Both
receive specific UV entries that land in their region (adversarial `Briefing rule`
exception). Both read prior referee reports in `lore/` and track which
old issues remain.

Each returns a verdict âˆˆ `accept | minor | major | reject`.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

Process Phase 2 reports through `Claim lifecycle (git-as-archive)`. Update `uv.md` with new issues,
demote any claim that a referee killed, file new UVs where they
sharpened a gap. Summarize verdicts in `collation.md`.

Keep fixers/referees alive for follow-up objections, narrowed repairs, and
adjacent referee passes while their context is fresh. Use `send_input` to
continue the dialogue. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when replacement is clearly better. Commit
logical units naming the team dir.


