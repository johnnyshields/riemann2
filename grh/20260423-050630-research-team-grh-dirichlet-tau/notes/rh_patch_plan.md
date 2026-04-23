# RH Patch Plan Note

Date: 2026-04-24
Focused attack: `tasks/20260424-001046-attack-gap-rh-patch-plan/`

## Main conclusion

The highest-value, lowest-risk patch to the main RH draft is:

- add one canonical zeta-source subsection at the start of `\section{Zeta-side decomposition}`;
- use it to justify the manuscript’s `q`, `B_zeta`, `S`, and positive strip-edge kernel representation;
- then clean up later notation and dependency language accordingly.

## Exact cut point

The explicit local/source boundary should be stated at the beginning of

- `paper/proof_of_rh.tex:271-301`

That is where the paper first stops being generic phase geometry and starts
using zeta-specific source data.

## Minimal theorem package needed there

The safest patch is now 2-step:

1. one source-normalization subsection fixing the quotient, boundary phase
   convention, and bridge from `phi'/phi` to `q`;
2. one bundled localized zeta-source theorem covering the single-zero formula,
   compact-interval summation / regularization, explicit background
   identification, and multiplicity.

## Why this patch is high value

- it clarifies the real dependency structure of the draft;
- it justifies the later use of `S(m)` as a positive source scalar;
- it strengthens the paper even if no GRH/ERH work is ever promoted back;
- it does not require redesigning the endgame.

## Report refs

- `tasks/20260424-001046-attack-gap-rh-patch-plan/reports/gap-rh-patch-plan-routeA.md`
- `tasks/20260424-001046-attack-gap-rh-patch-plan/reports/gap-rh-patch-plan-routeB.md`
