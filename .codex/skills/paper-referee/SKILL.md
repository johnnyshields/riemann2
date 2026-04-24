---
name: paper-referee
description: Two-phase review loop on <paper>/<main>.tex â€” Phase 1 fixers edit the paper to address known issues, Phase 2 fresh referees re-review. Phase 1 is an explicit edit-capable exception.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Paper Referee

Two phases in one team dir: Phase 1 fixers edit the paper against known
issues; Phase 2 fresh referees re-review without seeing what Phase 1
touched. Phase 1 is the explicit edit-capable exception to the
read-only default. Follows `.codex/references/agents/_autoresearch.md`, CLAUDE.md
`Dispatch` long-lived-agent rules, `Briefing rule`, `Team dirs and agent
self-deposit`, `Capture before shutdown, forward-carry at dispatch`. For Codex, use the inherited model by default; only override the model if the user explicitly asks or the task clearly requires it. Original Claude note: use the original Claude research model for every fixer/referee, always.

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

`Codex subagent delegation when explicitly requested team_name: "paper-referee-fix-<ts>"`. Spawn up to 3
fixers (`Codex agent role: fixer`, the inherited Codex model by default) named for their content area
(e.g. `fixer-local-geometry`, `fixer-finite-s-algebra`,
`fixer-endgame`). Each gets its own `agents/<ts>-fixer-<slug>/`
subdir and the full `.codex/references/agents/_autoresearch.md` metaprompt.

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

`Codex subagent delegation when explicitly requested team_name: "paper-referee-review-<ts>"` (same team dir,
new Codex subagent delegation when explicitly requested). Spawn two referees read-only (`Codex agent role: referee`,
the inherited Codex model by default) with the full `.codex/references/agents/_autoresearch.md` metaprompt:

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


