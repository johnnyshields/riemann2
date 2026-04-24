---
name: research-team
description: Primary workhorse. Dispatches a coordinator-selected live roster via Codex subagents when delegated teamwork is authorized, with one team dir and per-agent subdirs under paper teams. Uses a one-ahead pattern where researchers keep attacking while verifiers review prior stable deposits.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Team

Adaptive research dispatch via Codex subagents when delegated teamwork is
authorized. The coordinator chooses the live roster from the frontier: gap
closers for concrete UVs, explorers for redirects, verifiers or source auditors
when there is something specific to check. Verification is risk-based and
usually one step behind the research lane. Follow `Dispatch`,
`.agents/references/agents/_autoresearch.md`, `Briefing rule`, `Writing
discipline`, `Team dirs and agent self-deposit`, and `Capture before shutdown,
forward-carry at dispatch`.

`$ARGUMENTS`: empty -> coordinator picks the most useful frontier; topic phrase
-> orient around it; `UV-NNN` -> assign at least one gap-closer to it.

## Preamble

1. Read the most recent team dir's `findings.md`, `uv.md`, current
   `rem:wip-*` labels, last 2-3 lore entries, and recent agent reports.
2. Create `<paper>/teams/<ts>-<team-slug>/`. Copy the prior `findings.md` and
   `uv.md`, prune dead entries, add uncaptured material, initialize a fresh
   `attempts.md`, carry only open next-actions into `dispatch.md` or
   `collation.md`, and commit.
3. Run the AGENTS.md ledger gate: every prior landed report is filed to the
   right ledger or has a `collation.md` no-action note.
4. Pick the initial roster and one-ahead cadence. Write `dispatch.md` with the
   originating commit, roster, verifier queue if any, targets, exact in-scope
   files/lines/reports, protected surfaces, non-goals, fixed-harness criteria,
   ground-truth checks, budgets/timeouts, and the ledger contract.

## Dispatch

When delegated teamwork is authorized, record team name `research-team-<ts>` in
`dispatch.md`. Spawn the coordinator-selected initial roster, not a fixed quota.
Start enough research/exploration lanes to keep work moving; add verifier or
source-auditor lanes when a prior deposit is ready to check or risk demands an
early check. Each agent's slug gets its own `agents/<ts>-<agent-slug>/` subdir.

Keep teammates alive after their first deposit. Treat idle notifications as
availability for the next assignment, not completion. Use `send_input` to reuse
context; spawn fresh agents for new roles, independence checks, blocked
teammates, or stale long-idle teams.

Every briefing gets the full `.agents/references/agents/_autoresearch.md`
metaprompt, the team dir's full `findings.md`, the 9-field report schema,
non-goals, the agent's exact deposit path, self-deposit checklist, and
`Writing discipline`. Synthesize non-goals from context.

Role-specific idioms:

- **Gap-closers** receive their specific UV entry verbatim from `uv.md`;
  include "What is the cleanest target here?", smallest concrete unresolved
  sub-statements, routes A/B/C, and fallback to minimal finite reduction.
- **Explorers** receive no `uv.md` content by default; they return observations
  and candidate findings tagged `[confirmed]`, `[conditional]`, or
  `[candidate]`.
- **Verifiers/source auditors** review specific prior deposits, not the whole
  frontier by default. If no verification target is ready, do not spawn them
  yet. Give only the UV entries and reports needed for the check, then ask for
  the honest verdict and scoped objections.

Every agent is told: `unsupported`, `blocked`, and `no progress` are acceptable
returns.

## Continuing Cycle

1. Verify each returning agent deposited `agents/<agent-slug>/report.md` plus
   cited `scripts/` and `notes/`. Chase missing deposits via `send_input`; log
   unanswered gaps in `collation.md`.
2. Walk each report. Classify by `State ledger separation`: UV candidates to
   `uv.md`, reusable lessons to `findings.md`, route outcomes to `attempts.md`,
   synthesis/no-action notes to `collation.md`, and paper-ready text to
   `paper-updates.md`. Every substantial route gets either an `attempts.md`
   row citing the report or an explicit `collation.md` no-action note. Process
   proof-state changes through `Claim lifecycle (git-as-archive)`, refresh
   frontier summaries, and commit per deposit where possible.
3. Maintain the one-ahead pipeline: queue verifier work for stable claims that
   need checking, but immediately redelegate independent next attacks or
   explorations to the research lane. Wait only when the next move depends on
   the verifier's answer.
4. Respond to each agent with one concrete follow-up, challenge, clarification,
   or next adjacent task. Use `send_input` when context is useful.
5. Write `paper-updates.md` only for paper-ready edits. No direct `<main>.tex`
   edits here; promotion is a separate deliberate step after review.
6. Write a lore entry for major direction changes or team-level decisions.

Do not shut down agents at ordinary cycle boundaries. Keep the delegated Codex
team alive for continuity. Use `close_agent` only at a terminal condition,
explicit user halt, stale long-idle team, or when replacement is clearly better.
