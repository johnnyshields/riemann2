---
name: research-attack
description: Small-cycle variant of research-team for a focused push on one UV-NNN or rem:wip-* target. Starts with one or two gap-closers and adds lagging verification only when a stable claim is ready or risk demands it.
---

# Research Attack

Focused push on one gap. Start with one gap-closer; `--double` for two independent routes. Add a verifier only when a stable claim is ready, the target is high-risk, or promotion is being considered. See `Dispatch`, `Briefing`, `Team dirs`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text resolved to the best match. Optional `--double`.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md` plus the paper region around the target's `rem:wip-*` label.
2. Create `<paper>/teams/<ts>-attack-gap-<slug>/`. Copy prior `findings.md` / `uv.md`, prune, add uncaptured material, initialize fresh `attempts.md`, carry target-relevant open next-actions to `dispatch.md` or `collation.md`. Commit.
3. Run the ledger gate for the target.
4. Write `dispatch.md` with originating commit, target, current baseline/frontier, exact in-scope files/lines/reports, protected surfaces, routes, verifier queue, non-goals, fixed-harness criteria, ground-truth checks, budgets, ledger contract.

## Dispatch

Record team name `research-attack-<ts>` in `dispatch.md`. Roster:

- **Gap-closer(s)** (`role: gap-closer`) → `gap-<slug>` or `gap-<slug>-routeA` / `-routeB` under `--double`. Brief with `_autoresearch.md`, full `findings.md`, the UV entry verbatim, clean target, routes A/B/C, exact deposit path, self-deposit checklist.
- **Verifier / source auditor** (`role: verifier-adversarial` or `verifier-source`) → spawn only when there's a concrete prior deposit to attack or source-check. Give the specific UV entry and report path needed — not the whole ledger.

Keep teammates alive after deposit. Use `send_input` for follow-up challenges, verifier objections, sharpened reductions, next adjacent attack — before spawning replacements.

Non-goals are coordinator-synthesized: no adjacent UVs, no re-proving closed lemmas, no new conjectures outside scope.

## Continuing Cycle

1. Verify every `report.md` plus cited `scripts/` / `notes/` exists; chase missing.
2. Walk each report per `Ledger separation`: refine or file UVs, append only reusable lessons to `findings.md`, log routes in `attempts.md` with report provenance, put synthesis/no-action in `collation.md`.
3. One-ahead: send independent next attacks to gap-closers while any verifier checks the previous stable claim. Wait only when the next attack depends on that check.
4. `paper-updates.md` for paper-ready edits only. No direct `<main>.tex` edits.

Don't shut down at attack boundaries. Keep the team alive. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
