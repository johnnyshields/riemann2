# q Notation Note

Date: 2026-04-24
Focused attack: `tasks/20260424-011402-attack-gap-q-notation/`

## Main conclusion

The `q` / `q_zeta` clash is genuinely local in the text, but not local enough
for a one-line repair.

Safe RH-facing fix:

- a small source-normalization subsection at the start of `Zeta-side decomposition`;
- there declare the specialization once;
- then rewrite `S(m)` in terms of that normalized source object.

## Why this matters

The draft uses `q` everywhere for the active phase derivative, but `q_zeta`
appears in the single definition

`S(m) = q_zeta(m) - B_zeta(m)`.

That one switch blocks a clean canonical source theorem unless the source
subsection explicitly identifies the quotient-normalized source with the active
`q` used elsewhere.

## Safe wording

Until that source subsection exists, read

- `q = B_zeta + S`
- `S(m) = q_zeta(m) - B_zeta(m)`

as scoped manuscript notation, not yet as a fully normalized canonical source
package.

## Report refs

- `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeA.md`
- `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeB.md`
- `tasks/20260424-011402-attack-gap-q-notation/reports/verifier-adversarial-q-notation.md`
