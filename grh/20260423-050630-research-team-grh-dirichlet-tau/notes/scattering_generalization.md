# Scattering Generalization Note

Date: 2026-04-23
Focused attack: `tasks/20260423-130548-attack-gap-scattering-generalization/`

## Main conclusion

The manuscript's scalar `S(m)` is better understood as a positive strip-edge
zero kernel than as a raw critical-line-value surrogate.

The strongest safe statement now is:

`S(m) = sum over zeros of f_{beta,gamma}(m)`, where
`f_{beta,gamma}(m) = Re((1+2im-rho)^(-1) - (2im-rho)^(-1))`.

So `S(m)` is the background-subtracted scalar coefficient of the local value
channel, built from a positive strip-edge zero contribution.

## Archive provenance

The repo's chat archive already contains a precise candidate source formula for
this reading:

- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`

There the candidate quotient is written as

`phi(s) = Lambda(2s-1) / Lambda(2s)`

with

`phi(1/2+it) = e^{-2 i Phi(t)}`.

In that archived derivation, a zero `rho` contributes exactly the displayed
strip-edge kernel. This is strong provenance for the candidate-object reading,
but it is still chat-archive provenance, not a theorem of
`paper/proof_of_rh.tex`.

## What this improves

This sharpens the GRH program at the level of candidate object selection.

- For primitive Dirichlet and tau, the better target is not a raw completed
  value or mere critical-line reality surrogate.
- The better target is a completed-object package whose background-subtracted
  zero contribution produces a real nonnegative scalar analogous to `S(m)`.

## What this does not improve yet

From current manuscript scope alone, this does not prove:

- an explicit completed-quotient formula for the draft's `q(t)`;
- a Dirichlet analogue of the corrected local block;
- a tau analogue of the corrected local block;
- denominator comparability, whitening, boundary control, or contradiction in
  any new family.

So this is a channel-selection upgrade, not a realized portability theorem.

After the quotient-phase attack, the sharpest wording is: this is a
`phase-channel upgrade only`, unless and until the value-channel realization is
proved.

## Effect on the existing notes

- `dirichlet_channel.md`: still correct on the boundary, but too weak if read as
  only a reality problem. The sharper target is a positive scattering-style
  scalar analogue of `S(m)`.
- `tau_localization.md`: still correct on the boundary. The tau case stays a
  cleaner self-dual channel candidate, now with a better candidate object in
  view.

## Honest boundary

Say:

- `the scattering-quotient reading sharpens the candidate object`;
- `the Dirichlet and tau realization theorems are still missing`.

Do not say:

- `the manuscript already proves a completed-quotient formula for q`;
- `Dirichlet or tau portability is now realized`.

## Report refs

- `tasks/20260423-130548-attack-gap-scattering-generalization/reports/gap-scattering-generalization-routeA.md`
- `tasks/20260423-130548-attack-gap-scattering-generalization/reports/gap-scattering-generalization-routeB.md`
- `tasks/20260423-130548-attack-gap-scattering-generalization/reports/verifier-adversarial-scattering-generalization.md`
