---
name: _autoresearch
description: NOT INVOCABLE — shared autoresearch rules included in every research brief.
---

# Autoresearch (every research agent)

Continuous loop. A single report does not end your job; expect dialogue and redelegation. If runtime/compaction interrupts you, leave a concrete next action so the next coordinator resumes without re-discovery.

## Loop

1. Read brief, `findings.md`, your prior `report.md` / `notes/` / `scripts/`, and any UV entry the team lead supplied.
2. Pick the next concrete move — prove, reduce, compute, search adjacent structure, verify, or reject — without asking.
3. Do the work. Computational claims = scripts written to files first, paths cited.
4. Deposit a 9-field report (`AGENTS.md` `Report schema`) plus updated notes/scripts. Include enough route detail for the lead to file `attempts.md`/`uv.md`/`findings.md`/`collation.md` without rereading your reasoning.
5. Close with the next best task for yourself: sharpest follow-up, adversarial check, finite reduction, or why the route is exhausted.
6. Wait. If redelegated, continue from prior context — don't restart.

## Posture

- Keep going. `no progress` is acceptable only after reducing the obstacle to its sharpest missing sub-statement or explaining why the route is exhausted from the tested scope.
- Don't ask whether to continue, which UV to pick, or whether a stopping point is good.
- Treat hypotheses as disposable. Keep useful results, discard failed routes with scoped negatives.
- Stop only for explicit team-lead halt, hard blocker requiring coordinator action, or terminal closure/rejection.

## Experiment discipline

- **Fixed harness:** paper, current `findings.md`/`uv.md`, frozen macros, assigned target. Don't move goalposts mid-route.
- **Baseline first:** name the current frontier (best proof state, sharpest obstruction) and what would count as improvement.
- **Ground-truth check:** before working, name the theorem statement, `rem:wip-*`, source ref, verifier question, pinned objection, or script output that decides whether evidence counts.
- **Promotion bar:** proof evidence + clean dependencies + adversarial/source verification + no unresolved strongest objection. Computational support is evidence, not proof.
- **Route status** in your report — exactly one of:
  - `keep` — usable proof / reduction / finding / negative
  - `discard` — scoped failure, do not retry unchanged
  - `blocked` — needs coordinator action
  - `terminal` — target closed or rejected
  - `crash` — tooling/execution failure (not mathematical)
- **Ledger destination:** name it explicitly (`uv.md`, `findings.md`, `attempts.md`, `paper-updates.md`, `collation.md/no-action`, or `none`) with one sentence why. Ambiguous destination = defect.
- **Timeouts:** if a run exceeds the briefed budget, stop, record what was learned, propose the next bounded attempt.
- **Crash handling:** fix typos/imports and rerun. If the idea itself is broken after a few attempts, log `crash`/`discard` and move on.
- **Simplicity:** at equal proof value, prefer fewer new definitions, assumptions, dependencies, scripts, and paper edits.
- **No log floods:** long output goes to files under your `scripts/` or `notes/`. Reports cite path + relevant excerpts.

## Required closing block

After the 9-field report, add:

- **Autoresearch next step:** one of `continue:` / `verify:` / `blocked:` / `terminal:` with the concrete action.
- **Ledger destination:** one of the values above + one sentence why.
