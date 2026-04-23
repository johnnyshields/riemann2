# Zeta Source Proof Plan

Date: 2026-04-24
Focused attack: `tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/`

## Main conclusion

The RH-facing patch unit is now stable:

1. one source-normalization subsection;
2. one compact-interval localized source theorem.

But the theorem endpoint must stay narrower than some of the current surrounding
prose.

## Safe theorem endpoint

The safe theorem endpoint is:

`one normalized compact-interval source identity`

not a broad unqualified global source declaration.

## Practical proof order

1. Fix the quotient `phi(s)=Lambda(2s-1)/Lambda(2s)`.
2. Fix the boundary phase convention and the bridge from `phi'/phi` to `q`.
3. Prove the one-zero contribution in the normalized convention.
4. Prove compact-interval summation / regularization to obtain the localized
   source identity.
5. Immediately after the theorem, state scoped text for:
   - background naming,
   - multiplicity,
   - the `q` / `q_zeta` specialization.

## Scoped warning

Do not let the theorem itself carry more than the compact-interval source
identity safely supports.

In particular, keep the following weaker until normalized in that subsection:

- unqualified `q = B_zeta + S`;
- unqualified `S(m) = q_zeta(m) - B_zeta(m)`;
- exact background aliasing across all three existing background symbols.

## Report refs

- `tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/reports/gap-zeta-source-proof-skeleton-routeA.md`
- `tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/reports/gap-zeta-source-proof-skeleton-routeB.md`
- `tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/reports/verifier-adversarial-zeta-source-proof-skeleton.md`
