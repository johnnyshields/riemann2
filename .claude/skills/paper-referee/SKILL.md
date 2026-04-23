---
name: paper-referee
description: Two-phase review loop on <paper>/<main>.tex — Phase 1 fixers edit the paper to address known issues, Phase 2 fresh referees re-review. Phase 1 is an explicit edit-capable exception.
---

# Paper Referee

Two-phase: Phase 1 fixers edit the paper against known issues, Phase 2
fresh referees re-review. Phase 1 is an explicit edit-capable exception
to the read-only default.

`$ARGUMENTS`: empty → fix against latest referee feedback in `lore/`;
file path → target that; `--no-referee` → skip Phase 2;
`--referee-only` → skip Phase 1; specific issues listed → fix only those.

## Preamble

Read `findings.md`, recent referee reports in `lore/`, and the paper
region at issue. Create two team dirs sharing one timestamp:
`<paper>/teams/<ts>-attack-gap-referee-<slug>/` (Phase 1) and
`<paper>/teams/<ts>-verify-referee-<slug>/` (Phase 2). Announce paths.

## Phase 1

`TeamCreate team_name: "paper-referee-fix-<ts>"`. Spawn up to 3 fixers
named for their content area (e.g. `fixer-local-geometry`,
`fixer-finite-s-algebra`, `fixer-endgame`). Standard briefing plus the
specific UV entries their issues touch (narrow exception only, not the
whole ledger) and their assigned issues.

**Edit-capable exception**: fixers may edit `proof_of_rh.tex`; may NOT
edit `unverified.tex` or `findings.md` — surface new findings in their
reports for coordinator review. Non-goals: no rewrite beyond assigned
issues; no new lemmas without a UV entry.

Shut down and `TeamDelete` when Phase 1 completes.

## Phase 2 (unless `--no-referee`)

`TeamCreate team_name: "paper-referee-review-<ts>"`. Spawn two referees
read-only:

- **`referee-math`** — pure-math standard: proofs, hypotheses,
  circularity, citations.
- **`referee-general`** — clarity, accessibility, flow, overclaims.

Both return verdict \(\in\) `accept | minor | major | reject`. Both
receive full `unverified.tex` (referees are adversarial verifiers —
narrow exception). Both read all prior referee reports in `lore/` and
track which old issues are now addressed.

## Post-cycle

Commit Phase 1 paper edits (pre-commit compile-check applies). Commit
Phase 2 reports. Summarize verdicts to the user.
