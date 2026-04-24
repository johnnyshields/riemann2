---
name: research-attack
description: Small-cycle variant of research-team for a focused push on one UV-NNN or rem:wip-* target. Starts with one or two gap-closers and adds lagging verification only when a stable claim is ready or risk demands it.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Attack

Focused push on one gap. Start with one gap-closer by default; use `--double`
for two independent routes. Add an adversarial verifier or source auditor only
when a stable claim is ready to check, the target is high-risk, or promotion is
being considered. Follow `.agents/references/agents/_autoresearch.md`,
AGENTS.md `Dispatch`, `Briefing rule`, `Team dirs and agent self-deposit`, and
`Capture before shutdown, forward-carry at dispatch`.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text resolved to the best
match. Optional `--double`.

## Preamble

1. Read the most recent team dir's `findings.md` and `uv.md`, plus the paper
   region around the target's `rem:wip-*` label.
2. Create `<paper>/teams/<ts>-attack-gap-<slug>/`. Copy prior `findings.md` and
   `uv.md`, prune dead entries, add uncaptured material, initialize a fresh
   `attempts.md`, carry only target-relevant open next-actions into
   `dispatch.md` or `collation.md`, and commit.
3. Write `dispatch.md` with the originating commit, target, current
   baseline/frontier, exact in-scope files/lines/reports, protected surfaces,
   routes, verifier queue if any, non-goals, fixed-harness criteria,
   ground-truth checks, and budgets/timeouts.

## Dispatch

When delegated teamwork is authorized, record team name `research-attack-<ts>`
in `dispatch.md`. Spawn the coordinator-selected small roster with the inherited
Codex model:

- **Gap-closer(s)** (`role prompt: gap-closer`) -> `gap-<slug>` or
  `gap-<slug>-routeA` / `gap-<slug>-routeB` under `--double`. Brief with the
  autoresearch metaprompt, full `findings.md`, the specific UV entry verbatim,
  clean target, routes A/B/C, exact deposit path, and self-deposit checklist.
- **Verifier/source auditor** (`role prompt: verifier-adversarial` or
  `verifier-source`) -> spawn only when there is a concrete prior deposit to
  attack or source-check. Give the specific UV entry and report path needed for
  that check, not the whole ledger.

Keep teammates alive after deposit. Use `send_input` for follow-up challenges,
verifier objections, sharpened reductions, and the next adjacent attack before
spawning replacements.

Non-goals are coordinator-synthesized: no adjacent UVs, no re-proving closed
lemmas, no new conjectures outside scope.

## Continuing Cycle

1. Verify every `agents/<slug>/report.md` plus cited `scripts/` and `notes/`
   exists; chase missing deposits via `send_input`.
2. Walk each report. Classify by `State ledger separation`: refine or file UVs,
   append only reusable lessons to `findings.md`, log route outcomes in
   `attempts.md`, and put synthesis/no-action rationale in `collation.md`.
3. Maintain one-ahead flow: send independent next attacks to gap-closers while
   any verifier checks the previous stable claim. Wait only when the next attack
   depends on that check.
4. Write `paper-updates.md` only for paper-ready edits. No direct `<main>.tex`
   edits here.

Do not shut down at ordinary attack boundaries. Keep the team alive for
continuity. Use `close_agent` only at a terminal condition, explicit user halt,
stale long-idle team, or when replacement is clearly better.
