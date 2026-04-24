# Paired Slot Hypotheses Note

Date: 2026-04-24

## Main conclusion

The exact paired slot theorem is not well-posed from the upstairs source theorem
alone.

It already needs a small local analytic admissibility package.

## Minimal hypothesis stack

1. compact-interval paired source theorem with unified `B_chi^pair` and exact
   `S_chi^pair`;
2. symmetric local normal form for the paired local deformation;
3. corrected-whitening admissibility sufficient to define the corrected paired
   whitened block:
   - microscopic holomorphy,
   - same-point positivity/nondegeneracy,
   - well-defined inverse-square-root whitening;
4. first-order paired value-channel derivative `A_val,chi^pair` in that
   corrected local object.

Only with those in place does the exact identity

`Delta_chi^pair = S_chi^pair A_val,chi^pair + R_chi^pair`

become a well-posed theorem.

The later admissibility-boundary attack sharpened the split:

- denominator comparability itself should not appear as a co-equal theorem
  endpoint of the paired slot theorem;
- but its definability residue must already be imported into the theorem through
  microscopic holomorphy / same-point positivity-nondegeneracy / holomorphic whitening
  admissibility.

The later positivity attack sharpened this one step further:

- same-point positivity/nondegeneracy should not stay hidden inside a generic
  `minimal admissibility` phrase;
- it does not seem to come from denominator holomorphy alone in the manuscript;
- safest wording is to name it explicitly as its own local hypothesis line for
  holomorphic whitening.

The later spectral-gap attack sharpened the boundary again:

- safest theorem-facing wording is an explicit local clause
  `same-point positivity/nondegeneracy for holomorphic whitening`;
- denominator comparability supports holomorphy, but positivity appears to need
  a separate spectral-gap stability step.

The later paired-gap-source attack sharpened this once more:

- the baseline same-point gap should remain a separate explicit family-local
  whitening hypothesis for now;
- folding that gap into the compact source package would overstate what the
  current notes support.

## What remains downstream

- remainder dominance;
- quantitative corrected-whitening transport;
- odd/transverse realization;
- boundary estimates.

## Safe wording

`the paired slot theorem is source-plus-slot plus minimal local admissibility, not source alone.`

More sharply:

`denominator comparability stays partial at slot stage: not a theorem endpoint,
but a source of the minimal holomorphy residue; same-point
positivity/nondegeneracy should still be named explicitly as a local whitening
hypothesis.`

## Report refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-021955-paired-slot-theorem-routeA/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-021955-paired-slot-theorem-routeB/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-024215-paired-admissibility-boundary-routeA/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-024215-paired-admissibility-boundary-routeB/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeA/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeB/report.md`
