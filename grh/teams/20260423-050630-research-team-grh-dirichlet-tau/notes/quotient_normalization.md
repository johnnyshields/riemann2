# Quotient Normalization Note

Date: 2026-04-24
Focused attack: `tasks/20260424-003621-attack-gap-quotient-normalization/`

## Main conclusion

The factor-of-2 is fine. The sign is the actual issue.

With the archived boundary law

`phi(1/2+it) = e^{-2 i Phi(t)}`

and the manuscript convention

`q(t) = Phi'(t)`

the exact bridge is

`(phi'/phi)(1/2+it) = -2 q(t)`

not `+2 q(t)`.

## Safest patch-plan conclusion

The cleanest paper-facing fix is:

- add one source-normalization subsection at the start of `\section{Zeta-side decomposition}`;
- fix the quotient `phi(s)=Lambda(2s-1)/Lambda(2s)`;
- fix the boundary phase convention;
- fix the bridge between `phi'/phi` and `q`;
- then state the source split `q = B_zeta + S` with explicit scope.

If the manuscript wants to keep `q = Phi'` and a positive `q = B_zeta + S`
normalization, then the cleanest convention is to use

`phi(1/2+it) = e^{2 i Phi(t)}`

rather than the archived negative-sign version.

## Scoped warning

Until that source-normalization package is in place, claims around

- `q = B_zeta + S`
- `S(m) = q_zeta(m) - B_zeta(m)`

should be read as manuscript notation, not yet as a fully normalized canonical
source theorem.

## Report refs

- `tasks/20260424-003621-attack-gap-quotient-normalization/reports/gap-quotient-normalization-routeA.md`
- `tasks/20260424-003621-attack-gap-quotient-normalization/reports/gap-quotient-normalization-routeB.md`
- `tasks/20260424-003621-attack-gap-quotient-normalization/reports/verifier-adversarial-quotient-normalization.md`
