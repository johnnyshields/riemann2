---
name: research-attack
description: Default focused-attack pattern. 1-3 researchers in attack mode on bounded technical lanes for one UV-NNN or rem:wip-* target; verifier spawned lazily after a candidate exists, or via cross-audit redelegation.
---

# Research Attack

Tight focused push on one gap. Coordinator owns theorem statement and ledger/paper integration directly. Subagents take bounded technical lanes that can fail cleanly. See `Dispatch`, `Briefing`, `Team dirs`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text resolved to the best match. Optional `--double` to run two independent attack lanes; `--triple` for three.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md` plus the paper region around the target's `rem:wip-*`.
2. Create `<paper>/teams/<ts>-attack-gap-<slug>/`. Copy prior `findings.md` / `uv.md`, prune, add uncaptured material, initialize fresh `attempts.md`, carry target-relevant open next-actions to `dispatch.md` or `collation.md`. Commit.
3. Run the ledger gate for the target.
4. Write `dispatch.md` with originating commit, target, current baseline/frontier, exact in-scope files/lines/reports, protected surfaces, routes, non-goals, fixed-harness criteria, ground-truth checks, budgets, ledger contract.

## Dispatch

Record team name `research-attack-<ts>` in `dispatch.md`. Roster (default 1; `--double` = 2; `--triple` = 3):

- **Researcher in `attack` mode** → slug `attack-<lane>` (e.g. `attack-routeA`, `attack-routeB`, or `attack-coefficient-list`). Brief with `_autoresearch.md`, full `findings.md`, the UV entry verbatim, the *bounded* sub-problem for this lane, routes A/B/C, deposit path, self-deposit checklist.

Coordinator handles theorem formulation and ledger/paper integration — don't delegate the synthesis to a subagent.

**No pre-spawned verifier.** Verification lands one of two ways once a concrete candidate exists:

- **Cross-audit (default):** redelegate one of the existing attackers in `verify` mode to a sibling's deposit. They've been close to the problem and can spot routine errors fast.
- **Fresh verify:** spawn a new researcher in `verify` mode only when independence matters — the existing pool is too entangled with the route, or promotion is being considered.

Keep teammates alive after deposit. `send_input` to push back, sharpen a reduction, request the next lane.

Non-goals are coordinator-synthesized: no adjacent UVs, no re-proving closed lemmas, no new conjectures outside scope.

## Continuing Cycle

1. Verify every `report.md` plus cited `scripts/` / `notes/`; chase missing.
2. Walk each report per `Ledger separation`: refine or file UVs, append reusable lessons to `findings.md`, log routes in `attempts.md` with report provenance, put synthesis/no-action in `collation.md`.
3. Once a deposit looks promising, redelegate a sibling in `verify` mode (cross-audit) — or do the adversarial pass yourself if scope is small. Spawn a fresh verifier only when independence is the point.
4. `paper-updates.md` for paper-ready edits only. Direct `<main>.tex` edits stay coordinator-owned and gated by `Claim lifecycle`.

Don't shut down at attack boundaries. Keep the team alive. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
