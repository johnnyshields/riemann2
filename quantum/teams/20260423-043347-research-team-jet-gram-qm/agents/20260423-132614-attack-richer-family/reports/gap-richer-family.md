# gap-richer-family

- **Claim**: The best next family to attack is the real qutrit polynomial curve
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2)^T}{\sqrt{1+t^2+t^4}},\qquad t\in\mathbb R.
  \]
  It is small, exact, finite-dimensional, and non-homogeneous. For the first-horizontal-jet block with identity/scalar-phase transport, its singular values are not determined by endpoint overlap alone. The conceptual reason is that the overlap sees only the endpoint state lines, while the second singular value sees the relative position of the endpoint tangent planes \(S_t=\mathrm{span}\{\psi(t),\partial_t\psi(t)\}\); in this family those are genuinely independent data.
- **Status**: proved
- **Evidence**: Proved: because the family is real and normalized, \(\langle \psi(t),\partial_t\psi(t)\rangle=0\), so the first horizontal jet is just \(h_t=\partial_t\psi(t)\), with \(\|h_t\|^2=(t^4+4t^2+1)/(1+t^2+t^4)^2>0\). Proved: the endpoint overlap is
  \[
  I(u,v)=\frac{1+uv+u^2v^2}{\sqrt{(1+u^2+u^4)(1+v^2+v^4)}}.
  \]
  Proved: after whitening, the \(2\times2\) block is the overlap matrix between orthonormal endpoint frames \((\psi,e)\), \(e=h/\|h\|\), so its singular values are the principal-angle cosines between the two planes \(S_u,S_v\). Since these are \(2\)-planes in \(\mathbb R^3\), one singular value is always \(1\), and the second is the cosine between the unit normals. With
  \[
  n(t)=\frac{(t^2,-2t,1)^T}{\sqrt{t^4+4t^2+1}},
  \]
  the second singular value is
  \[
  s_2(u,v)=\frac{|1+4uv+u^2v^2|}{\sqrt{(1+4u^2+u^4)(1+4v^2+v^4)}}.
  \]
  Proved: \(s_2\) is not a function of \(I\) alone. A local independence check gives
  \[
  \det \frac{\partial(I,s_2)}{\partial(u,v)}\Big|_{(u,v)=(0,1)}=\frac{1}{\sqrt2}\neq 0,
  \]
  so \(I\) and \(s_2\) are functionally independent near \((0,1)\). Hence there cannot exist any function \(f\) with \(s_2=f(I)\) on this family. Conditional: if one wants the transport phrased as Berry or Pancharatnam rather than identity, this real family should stay inside the same scalar-phase class, so the singular values should be unchanged. Missing: a deposited exact closed form for the full whitened matrix \(\Omega(u,v)\) itself.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:225-247`; `quantum/findings.md:78-82,99-113`; `quantum/teams/20260423-131550-attack-first-jet-singular-values/reports/gap-singular-values.md:3-9`; `quantum/teams/20260423-132614-attack-richer-family/notes/coordinator-brief.md:3-14`.
- **Dependencies**: One-parameter first-horizontal-jet framework from the note; scalar-phase transport class or fixed identity transport; the standard fact that bilateral whitening of the first-jet pair gives the overlap matrix of orthonormal endpoint frames; the principal-angle description of singular values for \(2\)-planes in \(\mathbb R^3\).
- **Strongest objection**: This family is mathematically clean rather than physically famous. Also, the proof above exploits its real \(3\)-dimensional realization, where the second singular value becomes a normal-overlap invariant; a referee may ask for the same conclusion written directly from \(\Omega\), not via plane geometry.
- **Needed for promotion**: Write the direct \(\Omega(u,v)\) formula for this family, add one explicit equal-overlap/different-\(s_2\) witness pair, and run one adversarial check that no hidden transport or reparameterization issue is being smuggled in.
