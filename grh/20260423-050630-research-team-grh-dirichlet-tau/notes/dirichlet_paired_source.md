# Dirichlet Paired-Source Note

Date: 2026-04-23
Focused attack: `tasks/20260423-141819-attack-gap-dirichlet-paired-source/`

## Main conclusion

The paired `((chi, bar chi))` route remains the top non-zeta target only with
explicit scope:

- `from current scope alone`;
- and only for `first non-zeta exact-source realization`.

The recent quotient/universal-kernel results strengthen the single-channel route
upstairs, but not enough to displace the paired route at the exact local `S(m)`
slot level.

## Strongest safe theorem candidate

The current best theorem target is:

`exact paired-scalar source theorem with full bookkeeping and exact local-slot
identification`.

In words: construct a contragredient-symmetrized paired strip-edge scalar whose
background-subtracted part is the exact coefficient occupying the manuscript's
`S(m)` slot in the local value channel.

The clean theorem-facing paired object is now:

`Phi_chi^pair(s) = Xi_chi(2s-1) / Xi_chi(2s)`

with

`Xi_chi(s) = Lambda(s,chi) Lambda(s,bar chi)`.

That is cleaner than speaking only about the raw product, because it mirrors the
zeta strip-edge quotient form directly.

The later paired-quotient-properties attack sharpened this further:

- at the boundary-phase level, `Phi_chi^pair` is cleaner than the single-channel
  quotient because the residual root number disappears;
- conditional on an exact paired-source theorem, the one-zero strip-edge kernel
  and its positivity are automatic upstairs;
- positivity of the manuscript's paired `S(m)` slot becomes automatic only if
  that theorem also provides exact local-slot identification.

The later paired-quotient-normalization attack clarifies the front-end sign/factor convention:

- factor `2` is fine here too;
- safest theorem-facing choice, if an explicit phase is introduced, is to mirror
  the repaired zeta-side convention and write
  `Phi_chi^pair(1/2+it)=e^{2 i Theta_chi^pair(t)}` with
  `q_chi^pair=(Theta_chi^pair)'`.

The later paired `q`-normalization attack stabilizes that further:

- this front-end sign/factor issue no longer needs to remain open in the notes;
- but it is still only a source-normalized interface convention, not yet a
  theorem-closing canonical normalization.

The paired-background attack sharpened the source side one step further:

- the clean theorem-facing decomposition should use one unified
  `B_chi^pair` containing conductor/scaling, gamma-derivative, and any
  trivial-zero or pole corrections;
- pairing removes the residual root-number/front-end asymmetry, but not the
  need for exact source-to-slot background identification on compact intervals.

## What pairing fixes

- scalar reality / sign safety at the front end;
- a more conservative route to the exact `S(m)` slot than the current
  single-channel Dirichlet path.
- cleaner boundary-phase packaging than the single-channel quotient.
- a cleaner front-end background story once one passes to a unified
  `B_chi^pair`.

## What pairing does not fix

- the theorem-sized source gap;
- local-slot identification by itself;
- denominator comparability;
- corrected whitening;
- odd/transverse realization;
- boundary control.

## Scoped warning

Do not say:

- `pairing is already canonically realized`;
- `pairing materially shrinks the remaining theorem burden`.

Safe replacement:

- `pairing is still the conservative exact-source target from current scope
  alone`.
- `the clean paired theorem-facing object is the strip-edge quotient built from
  Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)`.

## Report refs

- `tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeA.md`
- `tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeB.md`
- `tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/verifier-adversarial-dirichlet-paired-source.md`
- `tasks/20260423-143207-attack-gap-paired-object-candidate/reports/gap-paired-object-routeA.md`
- `tasks/20260423-143207-attack-gap-paired-object-candidate/reports/gap-paired-object-routeB.md`
- `tasks/20260423-143207-attack-gap-paired-object-candidate/reports/verifier-adversarial-paired-object-candidate.md`
- `tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md`
- `tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeB.md`
- `tasks/20260423-184608-attack-gap-paired-background/reports/gap-paired-background-routeA.md`
- `tasks/20260423-184608-attack-gap-paired-background/reports/gap-paired-background-routeB.md`
