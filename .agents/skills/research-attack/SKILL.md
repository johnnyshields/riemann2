---
name: research-attack
description: Small-cycle variant of research-team. 1-2 gap-closers + 1 verifier for a focused push on one UV-NNN or rem:wip-* target. Cheaper than the 3+3+2 full cycle.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Attack

Focused push on one gap. 1 gap-closer + 1 adversarial verifier by
default; `--double` for 2 gap-closers on different routes. Follows
`.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch` long-lived-agent rules,
`Briefing rule`, `Team dirs and agent self-deposit` deposit, `Capture before shutdown, forward-carry at dispatch` forward-carry. Use the inherited Codex model by default for every
research agent, always. Do not override Codex model selection unless explicitly needed.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text (coordinator
resolves to the best match). Optional `--double`.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`, plus the
   paper region around the target's `rem:wip-*` label (Â±200 lines).
2. Create `<paper>/teams/<ts>-attack-gap-<slug>/` where `<slug>` is
   UV-ID or short descriptor. Copy prior `findings.md` + `uv.md` in;
   prune dead entries; add anything surfaced last cycle not yet
   captured. Initialize `attempts.md` with a markdown attempts table and
   `Frontier summaries` block. Commit.
3. Confirm no existing team dir has the same timestamp/slug. Write
   `dispatch.md` with the originating commit, target, current baseline/frontier,
   exact in-scope files/lines/reports, protected surfaces, routes, non-goals,
   fixed-harness criteria, ground-truth checks, and any run budgets/timeouts.

## Dispatch

When delegated teamwork is authorized, record team name `research-attack-<ts>` in `dispatch.md`. Spawn Codex subagents with the inherited Codex model by default:

- **Gap-closer(s)** (`role prompt: gap-closer`) â€” `gap-<slug>` (or
  `-routeA` / `-routeB` under `--double`). Briefing: full
  `.agents/references/agents/_autoresearch.md`, current team dir's `findings.md`, the
  specific UV entry verbatim (narrow `Briefing rule` exception), target in cleanest form,
  routes A/B/C, the `agents/<slug>/` path + self-deposit checklist.
- **`verifier-adversarial`** (`role prompt: verifier-adversarial`) â€”
  same briefing skeleton plus the UV entry (`Briefing rule` adversarial exception).
  Waits for gap-closer(s) to deposit, then attacks.

Keep those teammates alive after deposit. Use `send_input` for follow-up
challenges, verifier objections, sharpened reductions, and the next adjacent
attack before spawning replacements.

Non-goals (coordinator-synthesized): no adjacent UVs, no re-proving
closed lemmas, no new conjectures outside scope.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

1. Verify every `agents/<slug>/report.md` + `scripts/` deposited; chase
   missing via `send_input`.
2. Walk each report. Refine the target UV entry in this team dir's
   `uv.md` (sharpen `Needed for promotion`, or remove it if the verifier
   confirmed closure). File any new UV candidates. Add any new findings.
   Append an `attempts.md` row for every substantial route with `keep`,
   `discard`, or `crash`; periodically summarize counts and the current
   frontier in `collation.md`.
3. Respond to the agents. Ask the verifier to attack the strongest new claim;
   ask the gap-closer to reduce the sharpest remaining obstruction; or assign
   the next adjacent target to the same named teammate.
4. Write `paper-updates.md` only if the cycle produced paper-ready edits.
5. No direct `<main>.tex` edits here.

Do not shut down at ordinary attack boundaries. Keep the team alive for a good
while, continue the dialogue, and redelegate through `send_input`. Use
`close_agent` only at a terminal condition, explicit user halt, stale long-idle
team, or when replacing the team is clearly better than continuing it.


