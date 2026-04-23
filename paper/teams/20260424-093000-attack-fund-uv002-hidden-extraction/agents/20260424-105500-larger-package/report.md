# Report

## Claim

If equal reduced-`\widehat\Psi` fibers are not sufficient, the smallest larger reduced package state suggested by the current draft is
\[
\bigl(\widehat\Psi,[\delta c:\delta v_5:\delta u_5:\delta\lambda]\bigr),
\qquad
\lambda:=\frac{\Delta_7}{v_5},
\]
that is: the amplitude-invariant strengthened datum `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` together with the projectivized hidden `\lambda`-shear / defect direction. On affine charts this is equivalently `\widehat\Psi` plus the limiting shear triple `(\eta_*,\xi_*,\gamma_*)` from
\[
\delta(c)=\eta\,\delta(\lambda),\qquad
\delta(v_5)=\xi\,\delta(\lambda),\qquad
\delta(u_5)=\gamma\,\delta(\lambda).
\]
This is the smallest draft-native enlargement that plausibly controls the first surviving odd jet, because `\widehat\Psi` is already identified as the minimal projective extraction datum, while the only explicit extra reduced state later introduced is exactly this projective hidden-shear class.

## Status

heuristic

## Evidence

- The draft already says the downstream extraction datum is `\widehat\Psi`, not a smaller pair-level object; so any enlargement should start from `\widehat\Psi`, not replace it.
- The exact strengthened two-pair coincidence theorem shows that vanishing of the cubic/quintic/septic interaction package forces equality of `\widehat\Psi`, so equal `\widehat\Psi` fibers are the current package-level quotient.
- The draft then identifies the next residual mixed information not as a new primitive field, but as the projective moving `\lambda`-shear defect direction `[\delta c:\delta v_5:\delta u_5:\delta\lambda]`; it explicitly says downstream reduction should be formulated in terms of this projective class rather than an exact frozen transport law.
- On the zeta side, `H_m=\Phi_K(\widehat\Omega_\zeta^{\corr})`, and `\Phi_K` kills the pure value channel. The whitening-parity lemmas show diagonal and off-diagonal inputs first couple bilinearly, so a hidden off-diagonal shear class can affect the first `\Phi_K`-visible odd term only through such mixed data. This is consistent with enlarging `\widehat\Psi` by one projectivized hidden class, not by introducing a second primitive generator.
- The same draft also isolates the direct `q^{(7)}` slice as the highest-new source tower. That points toward one extra relational/provenance class attached to the existing package, rather than a larger zoo of package coordinates.

## Exact refs

- `paper/proof_of_rh.tex:567-598` (`\Phi_K(A_{\val})=0`)
- `paper/proof_of_rh.tex:1518-1565` (corrected whitened block and `H_{m,R}` packaged through `\Phi_K`)
- `paper/proof_of_rh.tex:2214-2307` (`H_m` and odd-jet expansion)
- `paper/proof_of_rh.tex:6353-6385` (whitening parity at diagonal base)
- `paper/proof_of_rh.tex:7576-7584,7655-7668` (direct `q^{(7)}` diagonal slice mixed with off-diagonal shear slice)
- `paper/proof_of_rh.tex:11368-11409` (definition of `\widehat\Psi`)
- `paper/proof_of_rh.tex:11445-11449` (`\widehat\Psi` is the natural scalar-invariant datum for multi-pair coincidence)
- `paper/proof_of_rh.tex:11476-11584` (exact strengthened two-pair coincidence implies equality of `\widehat\Psi`)
- `paper/proof_of_rh.tex:12257-12383` (projective compactness and projective hidden `\lambda`-shear defect direction)
- `paper/proof_of_rh.tex:12586-12609` (`\widehat\Psi` as extraction datum in the two-stage reformulation)

## Dependencies

- A package-side theorem upgrading reduced-`\widehat\Psi` coincidence to coincidence of the projective hidden-shear class.
- A package-to-jet theorem showing the first surviving odd jet of `H_m` is constant on fibers of `\bigl(\widehat\Psi,[\delta c:\delta v_5:\delta u_5:\delta\lambda]\bigr)`.
- The existing zeta-side extractor (`H_m`, `c_{2r+1}`, `\Xi_\zeta^{(N)}`), already in place once the package-to-jet factorization exists.

## Strongest objection

The draft does not yet prove that the projective `\lambda`-shear class is actually sufficient for `H_m`; it is introduced as the correct reduction object for the mixed two-point branch, not yet as a hidden-state classifier for the corrected finite-core package. So this is the sharpest plausible larger state suggested by the current draft, not a closed theorem.

## Needed for promotion

1. State the enlarged reduced package functor explicitly on the actual corrected two-atom / finite-core package.
2. Prove that equal values of this enlarged state force agreement of the corrected block modulo `\ker\Phi_K` through the first surviving odd order.
3. Deduce that the first nonzero odd jet of `H_m`, equivalently the first nonzero `\Xi_{\zeta,\le H}^{(N)}`, factors through this enlarged state.

Honest verdict: the draft does suggest a smallest next package state beyond reduced `\widehat\Psi`, and it is the projectivized hidden `\lambda`-shear / defect class. I do not see draft evidence for any smaller enlargement that still remembers the live hidden directions.
