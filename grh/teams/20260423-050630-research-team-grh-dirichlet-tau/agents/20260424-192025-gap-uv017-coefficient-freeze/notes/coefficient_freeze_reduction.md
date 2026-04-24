# UV-017 Coefficient / Freeze Reduction

Date: 2026-04-24

## Fixed harness

Target UV-017 only. UV-016 is used only as the staged source input:
the completed-Hadamard paired theorem fixes the boundary phase by
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t)
=-\frac12\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}
{\Phi_\chi^{\mathrm{pair}}}\!\left(\tfrac12+it\right),
\]
and in the completed normalization
\[
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0,
\qquad
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}=q_\chi^{\mathrm{pair}}.
\]

## Conditional coefficient lemma

Let \(m\in I\) and let the paired corrected local blocks be defined from the
same boundary phase \(\Theta_\chi^{\mathrm{pair}}\) used in the source theorem.
Assume a local holomorphic jet chart for the corrected paired whitened block
\[
\mathcal F_{\chi,m,\sigma}(a,\eta)
\]
near \((a,\eta)=(0,\eta_0)\), where:

- \(a\) is the zeroth value coordinate
  \(q_\chi^{\mathrm{pair}}(m)-B_{\chi}^{\mathrm{pair}}(m)\);
- \(\eta\) consists of the non-value local coordinates: derivative, mixed-jet,
  curvature, background, cutoff/correction, and normalization data;
- the actual paired object has coordinates
  \[
  (a,\eta)=
  (S_\chi^{\mathrm{pair}}(m),\eta_\chi(m));
  \]
- the pure value-channel path is
  \[
  (a,\eta)=(\alpha,\eta_0),
  \]
  so all non-value data are frozen.

Define
\[
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
:=
\partial_a\mathcal F_{\chi,m,\sigma}(0,\eta_0)
\]
and
\[
R_\chi^{\mathrm{pair}}(m,\sigma)
:=
\mathcal F_{\chi,m,\sigma}
\bigl(S_\chi^{\mathrm{pair}}(m),\eta_\chi(m)\bigr)
-\mathcal F_{\chi,m,\sigma}(0,\eta_0)
-S_\chi^{\mathrm{pair}}(m)
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma).
\]
Then
\[
\Delta_\chi^{\mathrm{pair}}(m,\sigma)
=
S_\chi^{\mathrm{pair}}(m)
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
+R_\chi^{\mathrm{pair}}(m,\sigma).
\]
Moreover, along the pure value path,
\[
\left.
\frac{\partial}{\partial\alpha}
\left(
\mathcal F_{\chi,m,\sigma}(\alpha,\eta_0)
-\mathcal F_{\chi,m,\sigma}(0,\eta_0)
-\alpha A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
\right)
\right|_{\alpha=0}=0.
\]
Thus a replacement \(c_\chi(m)S_\chi^{\mathrm{pair}}(m)\) can satisfy the same
pure-value freeze rule only if \(c_\chi(m)=1\), provided
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\ne0\) in the slot being tested.

## Proof sketch

This is the RH local algebra with the coordinate names changed. The source
theorem supplies the scalar \(S_\chi^{\mathrm{pair}}(m)\) in the same phase
normalization as the local block if the local block uses
\(\Theta_\chi^{\mathrm{pair}}\) and \(q_\chi^{\mathrm{pair}}=\Theta'\). The
holomorphic whitening map
\[
(G_-,N,G_+)\mapsto G_-^{-1/2}NG_+^{-1/2}
\]
is linear to first order in the three block variations; it does not introduce a
new scalar once the value parameter \(a\) is chosen. The only possible
renormalization site is therefore the source-to-local coordinate map
\[
S_\chi^{\mathrm{pair}}(m)\mapsto a.
\]
The unit-coordinate hypothesis \(a=S_\chi^{\mathrm{pair}}(m)\) forces unit
coefficient. If instead \(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)+O(S^2)\), then
the coefficient becomes \(c_\chi(m)A_{\mathrm{val},\chi}^{\mathrm{pair}}\).

## Proved / Conditional / Missing

Proved from the current harness:

- the staged source theorem fixes the sign and factor convention for
  \(q_\chi^{\mathrm{pair}}\);
- in completed-Hadamard normalization, the source scalar is \(S=q\);
- the RH draft's pure value derivative freezes non-value data and the matrix
  whitening linearization introduces no new scalar.

Conditional:

- the coefficient lemma above is theorem-ready once a paired unit-coordinate
  local jet chart and holomorphic whitening interface are installed.

Missing:

1. Paired unit-coordinate jet chart: prove the corrected paired same-point and
   mixed blocks are functions of the same phase \(\Theta_\chi^{\mathrm{pair}}\)
   with zeroth coordinate exactly
   \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\), not a rescaled
   coordinate.
2. Paired parameter holomorphy and whitening: prove holomorphy in \(a\) and the
   non-value coordinates, plus same-point positivity/nondegeneracy for the
   inverse square roots.
3. Freeze-rule remainder criterion: state that \(R_\chi^{\mathrm{pair}}\) has
   zero first derivative along the pure value path; derivative, curvature,
   background, multiplicity, and gauge variations may enter \(R\) only through
   non-value directions.
4. Scalar readout boundary: if UV-017 is pushed beyond the matrix-level local
   expansion to a downstream scalar functional, prove that the scalar readout
   adds no extra normalization factor.

Honest verdict: this reduces UV-017 to a precise local normal-form lemma. It
does not prove that the paired Dirichlet construction already has that
unit-coordinate chart.
