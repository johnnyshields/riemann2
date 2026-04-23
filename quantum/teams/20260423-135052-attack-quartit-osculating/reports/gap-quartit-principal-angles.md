# gap-quartit-principal-angles

- **Claim**: For the real quartit cubic curve
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}},
  \]
  the honest second-order two-point invariant is the principal-angle data of the second osculating \(3\)-planes
  \[
  \mathcal O_2(t)=\operatorname{span}\{\psi(t),\partial_t\psi(t),P\partial_t^2\psi(t)\}.
  \]
  These planes are exactly
  \[
  \mathcal O_2(t)=\operatorname{span}\{v(t),v'(t),v''(t)\}=n(t)^\perp,
  \qquad v(t)=(1,t,t^2,t^3)^T,
  \]
  with normal
  \[
  n(t)=(-t^3,\,3t^2,\,-3t,\,1)^T.
  \]
  Hence for endpoints \(u,v\), the singular values of any bilaterally whitened second-osculating cross-Gram block built from bases of \(\mathcal O_2(u)\) and \(\mathcal O_2(v)\) are
  \[
  \sigma_1=\sigma_2=1,\qquad
  \sigma_3=
  \frac{|1+9uv+9u^2v^2+u^3v^3|}
  {\sqrt{(1+9u^2+9u^4+u^6)(1+9v^2+9v^4+v^6)}}.
  \]
  Equivalently, the principal angles are \(\theta_1=\theta_2=0\) and \(\theta_3=\arccos \sigma_3\).
- **Status**: proved
- **Evidence**: Proved: normalization does not change the second osculating plane, because \(\psi=s^{-1/2}v\) with \(s(t)=1+t^2+t^4+t^6\), so \((\psi,\psi',\psi'')\) is obtained from \((v,v',v'')\) by an invertible lower-triangular same-point change of basis, and replacing \(\psi''\) by \(P\psi''\) only removes the \(\psi\)-component. Proved:
  \[
  v'(t)=(0,1,2t,3t^2)^T,\qquad v''(t)=(0,0,2,6t)^T,
  \]
  and \(n(t)\cdot v(t)=n(t)\cdot v'(t)=n(t)\cdot v''(t)=0\), so \(\mathcal O_2(t)=n(t)^\perp\). Proved: two \(3\)-planes in \(\mathbb R^4\) have principal cosines equal to the singular values of any whitened cross-Gram representative, and for codimension-\(1\) planes these are \(1,1,\) and the cosine of the angle between unit normals. Here
  \[
  n(u)\cdot n(v)=1+9uv+9u^2v^2+u^3v^3,
  \qquad
  \|n(t)\|^2=1+9t^2+9t^4+t^6,
  \]
  which gives the displayed exact \(\sigma_3\). Conditional: this is the correct singular-value output for the second-order quantum benchmark under fixed identity/scalar-phase transport, i.e. when one compares the endpoint osculating subspaces inside the common ambient \(\mathbb R^4\). Missing: a transport-independent canonical higher-jet matrix statement.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:283-299`; `quantum/findings.md:98-133`; `quantum/teams/20260423-134344-attack-higher-jets/reports/gap-higher-jet-benchmark.md:3-30`; `quantum/teams/20260423-135052-attack-quartit-osculating/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Elementary linear algebra for principal angles of codimension-\(1\) subspaces; the already-established higher-jet principle that raw second-jet matrices are presentation-dependent but the osculating subspace survives triangular jet mixing; fixed ambient identification of endpoint subspaces via identity/scalar-phase transport.
- **Strongest objection**: This gives the exact second-osculating singular values only at the subspace level. It does not rescue a canonical higher-jet matrix invariant, and it is not transport-independent beyond the fixed identity/scalar-phase setting.
- **Needed for promotion**: Write down one explicit \(3\times3\) whitened second-jet representative whose singular values reduce to \((1,1,\sigma_3)\); decide whether the algebraic witness is sufficient or whether a simpler rational witness is still desired; state the benchmark theorem narrowly as “second-jet matrices fail, second-osculating principal-angle data survives.”
