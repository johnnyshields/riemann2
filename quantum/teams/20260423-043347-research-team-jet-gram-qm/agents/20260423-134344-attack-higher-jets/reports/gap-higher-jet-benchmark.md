# gap-higher-jet-benchmark

- **Claim**: The best next benchmark is the real normalized quartit cubic curve
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}},\qquad t\in\mathbb R.
  \]
  It is the smallest exact finite-dimensional one-parameter family that can show the second-jet phenomenon the brief asks for: raw second-jet matrices fail under reparameterization by upper-triangular mixing, while the second osculating subspace survives and still carries nontrivial two-point information.
- **Status**: proved
- **Evidence**: Proved: the general obstruction is already established in `quantum/`: higher jets mix lower jets under gauge change and reparameterization, and whitening is not invariant under those non-orthogonal triangular changes, while the honest repaired object is the osculating jet subspace and its principal-angle data. Proved: for the proposed family it is enough to work with the unnormalized polynomial lift \(v(t)=(1,t,t^2,t^3)^T\), because normalization multiplies by a scalar and therefore only changes \((v,v',v'')\) by a lower-triangular same-point change of basis, which preserves the span. Proved:
  \[
  v'(t)=(0,1,2t,3t^2)^T,\qquad v''(t)=(0,0,2,6t)^T,
  \]
  so \(\{v,v',v''\}\) is linearly independent for all \(t\), hence the second osculating space is a genuine \(3\)-plane in \(\mathbb R^4\). Proved: its orthogonal normal is
  \[
  n(t)=(-t^3,\,3t^2,\,-3t,\,1)^T,
  \]
  since \(n(t)\cdot v(t)=n(t)\cdot v'(t)=n(t)\cdot v''(t)=0\). Thus the endpoint second-osculating \(3\)-planes vary nontrivially with \(t\). Proved: under a reparameterization \(t=\phi(s)\),
  \[
  \partial_s\psi=\phi'\,\partial_t\psi,\qquad
  P\partial_s^2\psi=\phi'^2\,P\partial_t^2\psi+\phi''\,\partial_t\psi,
  \]
  so the ordered second-jet frame changes by a non-orthogonal upper-triangular law. Therefore a raw second-jet Gram/mixed/whitened matrix is presentation-dependent. Proved: the subspace
  \[
  \mathcal O_2(t)=\mathrm{span}\{\psi(t),\partial_t\psi(t),P\partial_t^2\psi(t)\}
  \]
  is unchanged by that triangular mixing, so the second osculating space survives reparameterization. Conditional: with fixed identity/scalar-phase transport, the singular values for the endpoint \(3\)-planes should be \(1,1,\frac{|(1+uv)^3|}{\sqrt{(1+9u^2+9u^4+u^6)(1+9v^2+9v^4+v^6)}}\), because they reduce to the principal angles between codimension-\(1\) planes with normals \(n(u),n(v)\). Missing: a deposited exact closed form for the full bilaterally whitened \(3\times3\) second-jet block for this family, and an explicit witness pair showing that the surviving nontrivial singular value is not determined by endpoint overlap alone.
- **Exact refs**: `quantum/teams/20260423-043347-research-team-jet-gram-qm/reports/gap-closer-gauge.md:3-9`; `quantum/teams/20260423-134344-attack-higher-jets/notes/coordinator-brief.md:3-16`; `quantum/findings.md:95-125`; `quantum/teams/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`.
- **Dependencies**: The proved higher-jet triangular-mixing statement; the osculating-subspace repair from the gauge report; elementary exact linear algebra for the polynomial lift \(v(t)=(1,t,t^2,t^3)^T\); fixed transport if one wants a two-point singular-value statement rather than only same-point/subspace survival.
- **Strongest objection**: The full higher-jet covariantization is still not canonically settled, so the benchmark proves matrix failure versus subspace survival most cleanly at the level of reparameterization and osculating spaces, not yet as a transport-independent canonical quantum invariant.
- **Needed for promotion**: Compute the exact second-jet whitened block for this quartit curve under identity or scalar-phase transport; verify the singular-value formula directly from that block; exhibit one equal-overlap/different-subspace-angle endpoint pair; then state the benchmark theorem explicitly as “second-jet matrix failure, second-osculating-subspace survival” for this family.
