---
name: research-attack
description: Small-cycle variant of research-team. 1-2 gap-closers + 1 verifier for a focused push on one UV-NNN or rem:wip-* target. Cheaper than the 3+3+2 full cycle.
---

# Research Attack

Focused push on one gap. 1 gap-closer + 1 adversarial verifier by
default; `--double` for 2 gap-closers on different routes. Follows
CLAUDE.md §5 briefing, §6 deposit, §8a forward-carry.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text (coordinator
resolves to the best match). Optional `--double`.

## Preamble (forward-carry first — §8a)

1. Read the most recent team dir's `findings.md` and `uv.md`, plus the
   paper region around the target's `rem:wip-*` label (±200 lines).
2. Create `<paper>/teams/<ts>-attack-gap-<slug>/` where `<slug>` is
   UV-ID or short descriptor. Copy prior `findings.md` + `uv.md` in;
   prune dead entries; add anything surfaced last cycle not yet
   captured. Commit.
3. Write `dispatch.md` with target, routes, non-goals.

## Dispatch

`TeamCreate team_name: "research-attack-<ts>"`. Spawn:

- **Gap-closer(s)** (`subagent_type: gap-closer`) — `gap-<slug>` (or
  `-routeA` / `-routeB` under `--double`). Briefing: current team dir's
  `findings.md`, the specific UV entry verbatim (narrow §5 exception),
  target in cleanest form, routes A/B/C, the `agents/<slug>/` path +
  self-deposit checklist.
- **`verifier-adversarial`** (`subagent_type: verifier-adversarial`) —
  same briefing skeleton plus the UV entry (§5 adversarial exception).
  Waits for gap-closer(s) to deposit, then attacks.

Non-goals (coordinator-synthesized): no adjacent UVs, no re-proving
closed lemmas, no new conjectures outside scope.

## Post-cycle (capture before shutdown — §8a)

1. Verify every `agents/<slug>/report.md` + `scripts/` deposited; chase
   missing via `SendMessage`.
2. Walk each report. Refine the target UV entry in this team dir's
   `uv.md` (sharpen `Needed for promotion`, or remove it if the
   verifier confirmed closure). File any new UV candidates. Add any
   new findings.
3. Write `paper-updates.md` only if the cycle produced paper-ready
   edits.
4. No direct `<main>.tex` edits here.

Shut down, `TeamDelete`, commit with the team dir named and UV-NNN in
the subject.
