# GRH / Dirichlet / Tau Synthesis

Date: 2026-04-23
Cycle: `20260423-050630`

## Bottom line

The research team found a real portability template in the current RH draft,
but not a proved extension.

- Safe now: the draft already contains a source-light local package built from a
  real phase, jet normalization, whitening, an odd transverse scalar template,
  and the discrete odd-moment projector.
- Not safe now: claims that the current manuscript already supports Dirichlet,
  GRH, or Ramanujan-\(\tau\) realizations of UV-001, UV-002, or UV-008.
- Best port-back: expose the abstraction boundary earlier. The first explicit
  zeta-side layer begins at `paper/proof_of_rh.tex:271-301`, not at the start
  of the local kernel package.

## Proved From Current Draft

- The material in `paper/proof_of_rh.tex:145-269` is largely phase-level local
  algebra, not zeta-specific source structure.
- The calibration linearization in `paper/proof_of_rh.tex:426-794` has a real
  local algebra core: `A_{\val}`, `\Phi_K(A_{\val})=0`, the small-`x`
  asymptotics, and the nonzero pairing with the toy anomaly are all local.
- The odd transverse scalar template in `paper/proof_of_rh.tex:2212-2322` and
  the `N`-point odd-moment projector in `paper/proof_of_rh.tex:2975-3169` are
  genuinely abstraction-friendly once an odd holomorphic scalar with the right
  boundary control exists.
- The draft itself says the late contradiction is RH-specific and cannot be
  closed from intrinsic local geometry alone. See
  `paper/proof_of_rh.tex:25842-26022`, `26280-26299`, `26369-26551`.

## Conditional On New Input

- Primitive Dirichlet \(L\)-functions look like the cleanest first extension
  target, but only after a completed-\(L\) realization theorem replaces the
  zeta-side source package.
- For complex primitive characters, the likely entry point is a self-dual or
  real-valued critical-line object built from the completed function, not raw
  `L(1/2+it,\chi)`. The verifier flagged this as conditional, not established.
- The Ramanujan \(\tau\) \(L\)-function looks like a good degree-2 test of the
  local package because self-duality is cleaner than in the complex Dirichlet
  case. But portability is still conditional on rebuilding the microscopic
  denominator, boundary, and whitening-scale package.
- The effective high-height story should be rewritten in analytic-conductor
  language if this program is generalized: schematically `Q` becomes
  `\log \mathcal C`.

## Missing Theorems

The verifier consensus was that portability claims become real only after a new
 completed-\(L\) realization package is proved. The missing pieces are:

1. A completed-\(L\) analogue of the corrected local deformation and corrected
   odd holomorphic transverse scalar.
2. A real, sign-compatible calibration amplitude replacing `S(m)` in the actual
   channel used.
3. Microscopic denominator comparability outside zeta.
4. Conductor-uniform zero counting / zero-free input strong enough to replace
   the zeta shell and crude-`S` bounds.
5. A check that the whitening scales and `Q^{-3}` boundary hierarchy survive in
   the new family.
6. In the complex Dirichlet case, a decision on the correct object: rotated
   single channel, paired `\chi,\bar\chi` object, or matrix-valued package.

## Safe Port-Backs To The RH Draft

- Present the opening local kernel / jet / whitening package in neutral phase
  language first, then specialize to zeta.
- Mark `paper/proof_of_rh.tex:271-301` as the first explicitly zeta-side input
  layer.
- Present the `N`-point layer as a universal operator on odd holomorphic germs,
  then state that the paper's actual germ is the zeta realization.
- Move some of the late scoped-negation language earlier: intrinsic geometry is
  exhausted from that scope alone.

## Unsafe Claims

- "The current draft already extends to GRH."
- "Complex Dirichlet characters are almost as clean as the zeta case."
- "Degree 2 only changes constants."
- "UV-001, UV-002, and UV-008 already have Dirichlet or tau analogues in the
  present manuscript."

## Best Next Targets In `grh/`

1. Write a family-agnostic local note that isolates exactly which parts of the
   current draft require only a real phase, a background slope, and an odd
   holomorphic scalar.
2. Write a separate Dirichlet note that defines the candidate completed
   critical-line object and identifies where sign-compatibility of the amplitude
   becomes a real issue.
3. Write a separate tau note that checks whether degree-2 archimedean data
   preserve the same microscopic radius and whitening power counting.

## Report Paths

- `tasks/20260423-050630-attack-gap-grh-dirichlet-tau/reports/gap-closer-finite-core-portability.md`
- `tasks/20260423-050630-attack-gap-grh-dirichlet-tau/reports/gap-closer-effective-portability.md`
- `tasks/20260423-050630-attack-gap-grh-dirichlet-tau/reports/gap-closer-calibration-portability.md`
- `tasks/20260423-050630-attack-fund-grh-dirichlet-tau/reports/explorer-dirichlet-phase.md`
- `tasks/20260423-050630-attack-fund-grh-dirichlet-tau/reports/explorer-tau-degree2.md`
- `tasks/20260423-050630-attack-fund-grh-dirichlet-tau/reports/explorer-portback-abstraction.md`
- `tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md`
- `tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-source-auditor-portability.md`
