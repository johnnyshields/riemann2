- Claim

  The cleanest exact missing `variable-x` theorem for UV-001 is the following calibration-level statement.

  **[candidate] Variable-\(x\) microscopic calibration theorem.** Fix a compact interval \(D\subset(0,\infty)\). There exist constants
  \[
  x_*(D)>0,\qquad c_\sigma(D)>0,\qquad C_{\rm cal}(D),C_{\rm rem}(D),C_{\rm cut}(D)>0,
  \]
  such that for every admissible midpoint \(m\), every \(d\in D\), and every
  \[
  0<x\le x_*(D),\qquad \sigma:=x/B_\zeta(m),\qquad |\sigma|\le c_\sigma(D)Q^{-1},
  \]
  the corrected local deformation satisfies
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(x)+R_\zeta(m,\sigma),
  \]
  the calibration functional
  \[
  \Psi_{x,d}(X):=\frac{\langle A_{\val}(x),X\rangle_\F}{\langle A_{\val}(x),M(d)\rangle_\F}
  \]
  is well-defined, and one has uniformly
  \[
  \Psi_{x,d}(A_{\val}(x))\asymp_D \frac{x}{B_\zeta(m)},
  \qquad
  |\Psi_{x,d}(R_\zeta(m,\sigma))|\le C_{\rm rem}(D)\frac{S_2}{Q^3}.
  \]
  If in addition the cutoff is chosen in the admissible regime so that
  \[
  R^3\ge \frac{C_{\rm cut}(D)}{xQ\,S(m)},
  \]
  then
  \[
  \Psi_{x,d}(R_\zeta(m,\sigma))=o\!\left(\frac{x}{B_\zeta(m)}S(m)\right),
  \qquad
  u^2\asymp_D \frac{x}{B_\zeta(m)}S(m).
  \]
  Consequently, if \(u_0(D)\) is the microscopic toy threshold and one sets
  \[
  x(m):=\min\!\left\{x_*(D),\,\frac{u_0(D)^2}{2C_{\rm cal}(D)}\frac{B_\zeta(m)}{S(m)}\right\},
  \]
  then the calibrated toy parameter obeys
  \[
  |u|<u_0(D).
  \]

  This is sharper than the five-item remark at `rem:wip-calibration-small-u`: it isolates the exact missing input as a variable/shrinking-\(x\) extension of the corrected zeta-side calibration package, with the adaptive choice of \(x(m)\) then becoming formal.

- Status

  open

- Evidence

  **Proved.**

  The denominator/pairing side is already uniform for \(0<x\le x_0(D)\). Proposition `prop:pairing` proves
  \[
  |\langle A_{\val}(x),M(d)\rangle_\F|\asymp x/B
  \]
  uniformly on compact \(d\)-ranges for all sufficiently small \(x\), and Proposition `prop:canonical-calibration` then gives
  \[
  \Psi_{x,d}(A_{\val}(x))\asymp x/B.
  \]
  So item (1) of `rem:wip-calibration-small-u` is already closed at the calibration-functional level.

  The normalized remainder estimate is also already \(x\)-independent once the corrected deformation is available in the relevant regime. Corollary `cor:sharpened-calibration-remainder` proves
  \[
  |\Psi_{x,d}(R_\zeta)|\ll_D S_2/Q^3,
  \]
  and the proof uses \(x\) only through the small-\(x\) size of \(A_{\val}(x)\), so there is no visible blow-up as \(x\to 0\) inside the calibration quotient itself.

  **Conditional on a shrinking-\(\sigma\) extension.**

  If the corrected local deformation package remains valid uniformly for
  \[
  x=B_\zeta(m)\sigma,\qquad |\sigma|\le cQ^{-1},
  \]
  rather than only \(|\sigma|\asymp Q^{-1}\), then the same calibration proof gives the displayed variable-\(x\) theorem. Under that extension, the adaptive choice
  \[
  x(m)=\min\!\left\{x_*,\,\frac{u_0^2}{2C_{\rm cal}}\frac{B_\zeta(m)}{S(m)}\right\}
  \]
  immediately forces \(u^2\le u_0(D)^2/2\), hence \(|u|<u_0(D)\).

  **Missing.**

  The draft does not yet state or prove the corrected zeta-side package in that shrinking-\(\sigma\) regime. The hard-coded hypotheses still use the fixed-scaled relation
  \[
  x=B_\zeta(m)\sigma,\qquad |\sigma|\asymp Q^{-1},
  \]
  and several upstream perturbation statements are normalized with a fixed local window length \(L_I\asymp x_0/Q\). That is the real unresolved theorem. The adaptive formula for \(x(m)\) itself is not the gap.

- Exact refs

  `paper/proof_of_rh.tex:661-737` (`prop:pairing`)

  `paper/proof_of_rh.tex:739-794` (`prop:canonical-calibration`)

  `paper/proof_of_rh.tex:948-1003` (`prop:block-perturbation`, fixed-scaled `L_I\asymp x_0/Q` input)

  `paper/proof_of_rh.tex:1497-1566` (`prop:corrected-local-decomposition`)

  `paper/proof_of_rh.tex:2050-2209` (`cor:sharpened-calibration-remainder`)

  `paper/proof_of_rh.tex:5300-5473` (`prop:toy-n-point-direct`, requires `|u|<u_0(D)`)

  `paper/proof_of_rh.tex:5500-5598` (`rem:wip-calibration-small-u`)

  `paper/unverified.tex:43-64` (UV-001)

  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-18` (after exact scalar-slot identification, remainder dominance is the next bottleneck for the calibrated value-channel subchain, but variable-`x` uniformity remains separate)

- Dependencies

  UV-009 remains a dependency for the toy-side microscopic threshold \(u_0(D)\) and the uniform \(u^4\)-error package.

  The source-level scalar slot is treated as given, per assignment.

  The theorem above also depends on a shrinking-\(\sigma\) version of the corrected whitening/transfer package, not just on the already-written pairing algebra.

- Strongest objection

  The statement packages several layers under one label. The calibration quotient itself behaves well as \(x\to 0\), but the draft has not shown that the upstream corrected local deformation, perturbation bounds, and admissible cutoff regime survive uniformly when \(x=B_\zeta(m)\sigma\) is allowed to shrink below the present \(|\sigma|\asymp Q^{-1}\) scale. From the current text alone, one cannot promote the full variable-\(x\) theorem just by citing `cor:sharpened-calibration-remainder`; the missing work is earlier in the zeta-side analytic packaging.

- Needed for promotion

  Reduce UV-001 to the following smallest explicit missing sub-statements.

  1. Prove a shrinking-\(\sigma\) version of the corrected local deformation package: for \(x=B_\zeta(m)\sigma\) with \(|\sigma|\le cQ^{-1}\), the decomposition
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(x)+R_\zeta(m,\sigma)
  \]
  and all whitening/transfer estimates used in `cor:sharpened-calibration-remainder` remain uniform.

  2. Prove the cutoff-compatibility statement in that same variable-\(x\) regime: the requirement
  \[
  R^3\gg \frac{1}{xQ\,S(m)}
  \]
  can still be met inside the admissible cutoff class when \(x=x(m)\) shrinks.

  3. Record the resulting calibration corollary with an explicit constant \(C_{\rm cal}(D)\) so that the adaptive choice
  \[
  x(m)=\min\!\left\{x_*,\,\frac{u_0(D)^2}{2C_{\rm cal}(D)}\frac{B_\zeta(m)}{S(m)}\right\}
  \]
  formally implies \(|u|<u_0(D)\).

  Honest verdict: UV-001 is not blocked by the denominator pairing or by the calibrated quotient itself. The clean missing theorem is a shrinking-\(\sigma\), variable-\(x\) extension of the corrected zeta-side calibration package, plus cutoff compatibility. Once that is proved, the adaptive `x(m)` choice is routine.
