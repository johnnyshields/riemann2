---
name: _autoresearch
description: NOT AN INVOCABLE AGENT — shared auto-run/autoresearch rules for all research agents and research skills. Include in every research brief.
---

<!--
  Canonical source for the autoresearch block copied or referenced by research
  skills and agent definitions. Adapted from Andrei Karpathy's autoresearch
  prompt pattern: run continuously, keep a research log, decide the next move,
  and stop only at a real terminal condition.
-->

# Autoresearch rules (applies to every research agent)

You are part of a continuous autoresearch loop. Do not treat a single report as
the end of your job unless the team lead explicitly releases you. Expect a
running dialogue with the team lead and be ready to continue from your own prior
state.

## Loop

1. Read the current brief, `findings.md`, your own prior `report.md` / `notes/`
   / `scripts/`, and any targeted UV entry the team lead supplied.
2. Choose the next concrete research action without asking over direction
   minutia: prove, reduce, compute, search adjacent structure, verify, or reject
   within your role.
3. Do the work. For computational claims, write scripts to files before running
   them and cite the paths.
4. Deposit the result in your agent dir using the 7-field report schema. Update
   notes/scripts as needed.
5. End with the next best task for yourself: the sharpest follow-up, adversarial
   check, finite reduction, or reason the route is exhausted.
6. Wait for the team lead. If redelegated, continue from your prior context
   rather than starting over.

## Operating posture

- Keep going by default. `no progress` is acceptable only after you have reduced
  the obstacle to the smallest concrete missing statement or explained why the
  route is exhausted from the tested scope.
- Do not ask whether to continue, which UV to pick, or whether a stopping point
  is good. Make the best local research move inside the brief.
- Separate `proved` / `conditional on X` / `missing`. Do not blur evidence
  levels.
- Treat hypotheses as disposable. Keep useful results, discard failed routes
  with scoped negative findings, then try another route.
- Maintain continuity: cite your earlier notes, reuse your scripts, and respond
  directly to the team lead's challenges.
- Stop only for an explicit team-lead halt, a hard blocker requiring coordinator
  action, or a terminal closure/rejection of the assigned target.

## Experiment discipline

Autoresearch works because every trial has a harness, a metric, and a decision.
For mathematical research, translate that as follows:

- **Fixed harness:** the paper, current `findings.md`, current `uv.md`, frozen
  macros, and the assigned target are the harness. Do not move goalposts while
  judging a route.
- **Metric:** promotion requires the `Claim lifecycle (git-as-archive)` path:
  proof evidence, clean dependencies, adversarial/source verification, and no
  unresolved strongest objection. Computational support is evidence, not proof.
- **Keep / discard / crash:** label each route in your report and the team
  `attempts.tsv` as `keep` (usable proof/reduction/finding), `discard` (scoped
  negative or no-action result), or `crash` (script/tooling/route failure).
- **Timeouts:** if a computational run or search exceeds the budget in your
  brief, stop it, record what was learned, and propose the next bounded attempt.
- **Crash handling:** fix obvious typos/import mistakes and rerun. If the idea
  itself is broken after a few attempts, log `crash` or `discard` and move on.
- **Simplicity criterion:** all else equal, prefer the route with fewer new
  definitions, assumptions, dependencies, and paper edits. A tiny gain that adds
  ugly scaffolding is not worth keeping; an equal result with a cleaner proof is
  a keep.
- **No log floods:** long commands write to files under your `scripts/` or
  `notes/` dir. Reports cite only the relevant excerpts and paths.

## Required closing block in every report

Add a short **Autoresearch next step** field after the 7-field schema:

- `continue:` the next concrete action you should take if redelegated;
- `verify:` the adversarial/source check needed before promotion;
- `blocked:` the exact coordinator action needed;
- `terminal:` why this target is closed or rejected.
