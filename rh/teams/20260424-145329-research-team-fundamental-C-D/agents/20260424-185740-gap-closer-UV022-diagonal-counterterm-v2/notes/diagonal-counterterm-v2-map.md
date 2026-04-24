# UV-022 diagonal counterterm v2 map

## Source bins

- Proved: `rh/proof_of_rh.tex:2415-2553` supplies an analytic corrected-whitening transfer
  \(\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)\) with coefficient bounds.
- Proved: `rh/proof_of_rh.tex:11888-11932` gives the formal source criterion:
  if an actual finite-order package has swap symmetry, exact one-amplitude
  collapse, and diagonal merger, then its interaction remainder has an
  \(a_1a_2(h_1-h_2)^2\) factor.
- Proved: `rh/proof_of_rh.tex:12447-12469` gives the collision-chart edge
  template: an actual defect that is analytic, swap-even in
  \((\omega,\delta)\), and zero at \((\omega,\delta)=(0,0)\) has a
  \(\delta^2\mathcal H(m,\kappa,\delta^2)\) form.
- Conditional/missing: `rh/proof_of_rh.tex:12163-12189` states that neither
  the finite-order source-level merger route nor the quotient-diagonal route is
  proved. The remaining input is verification of the actual corrected two-atom
  package identities.
- Missing: no line defines the source-weight-linear two-atom input
  \(X^{[1]}\), no line defines a source-honest diagonal counterterm for the
  order-7 quotient component, and no line proves that the order-7 quotient
  output of the corrected-whitening cross-effect sees only the quadratic
  homogeneous transfer \(\mathcal T_2\).

## Harness conclusion

Subtracting the diagonal self cross-effect is harmless for a quadratic transfer:
the remaining interaction is \(\delta^2\)-divisible. The same operation fails
for cubic and higher analytic transfer terms. It still has one-amplitude
collapse, atom-swap symmetry, and zero diagonal value, but a first-order
\(\delta\) term remains, even after the leading cancellation substitution
\(a_2=-a_1\).

Thus the diagonal-counterterm route needs one of the following source inputs:

1. The order-7 quotient component is purely quadratic in the
   source-weight-linear input, so higher \(\mathcal T_{p\ge3}\) pieces are
   quotient-invisible through order 7.
2. A same-reduced-image germ or collision-functoriality theorem kills the first
   collision derivative of the renormalized order-7 quotient component.
3. A source-honest diagonal counterterm is defined before quotient extraction
   and is proved to produce an analytic swap-even UV-010-chart defect that
   vanishes at \((\omega,\delta)=(0,0)\).
