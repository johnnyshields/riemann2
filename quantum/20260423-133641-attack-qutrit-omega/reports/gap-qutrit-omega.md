# gap-qutrit-omega

- **Claim**: For the real qutrit curve
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2)^T}{\sqrt{1+t^2+t^4}},
  \]
  with identity transport in the real lift, the bilaterally whitened first-horizontal-jet block is explicitly
  \[
  \Omega(u,v)=
  \begin{pmatrix}
  \langle \psi(u),\psi(v)\rangle & \langle \psi(u),e(v)\rangle\\
  \langle e(u),\psi(v)\rangle & \langle e(u),e(v)\rangle
  \end{pmatrix},
  \]
  where \(D(t):=1+t^2+t^4\), \(J(t):=1+4t^2+t^4\),
  \[
  h(t)=\partial_t\psi(t)=\frac{1}{D(t)^{3/2}}
  \begin{pmatrix}
  -t(1+2t^2)\\
  1-t^4\\
  t(2+t^2)
  \end{pmatrix},
  \qquad
  \|h(t)\|^2=\frac{J(t)}{D(t)^2},
  \]
  \[
  e(t):=\frac{h(t)}{\|h(t)\|}=
  \frac{1}{\sqrt{J(t)}}
  \begin{pmatrix}
  -t(1+2t^2)\\
  1-t^4\\
  t(2+t^2)
  \end{pmatrix}.
  \]
  Thus
  \[
  \Omega(u,v)=
  \begin{pmatrix}
  \frac{1+uv+u^2v^2}{\sqrt{D(u)D(v)}} &
  \frac{(u-v)(1+2v^2+2uv+uv^3)}{\sqrt{D(u)D(v)J(v)}}\\[1.2ex]
  \frac{(v-u)(1+2u^2+2uv+u^3v)}{\sqrt{D(u)D(v)J(u)}} &
  \frac{1-u^4-v^4+5uv+4u^3v+4uv^3+5u^3v^3+u^4v^4}{\sqrt{D(u)D(v)J(u)J(v)}}
  \end{pmatrix}.
  \]
  A clean simplification is
  \[
  \det \Omega(u,v)=\frac{1+4uv+u^2v^2}{\sqrt{J(u)J(v)}}=n(u)\cdot n(v),
  \qquad
  n(t)=\frac{(t^2,-2t,1)^T}{\sqrt{J(t)}},
  \]
  so the singular values are \(1\) and
  \[
  \frac{|1+4uv+u^2v^2|}{\sqrt{(1+4u^2+u^4)(1+4v^2+v^4)}}.
  \]
- **Status**: proved
- **Evidence**: Proved: because the family is real and normalized, \(\langle \psi(t),\partial_t\psi(t)\rangle=0\), so the first horizontal jet is exactly \(h(t)=\partial_t\psi(t)\). Proved: differentiating the normalized vector gives the closed form for \(h(t)\), and direct contraction gives \(\|h(t)\|^2=J(t)/D(t)^2\), hence the unit first-jet vector \(e(t)\). Proved: whitening the mixed first-jet block by the endpoint norms turns the \((\psi,h)\) pair into the orthonormal frame \((\psi,e)\), so \(\Omega(u,v)\) is exactly the \(2\times2\) overlap matrix written above. Proved: the determinant simplifies to the normal overlap \(n(u)\cdot n(v)\), which recovers the previously reported second singular value. Conditional: for any scalar-phase transport \(U_{u\leftarrow v}=e^{i\alpha(u,v)}I\), the whole matrix is multiplied by the single phase \(e^{i\alpha(u,v)}\), so the displayed real formula is the identity-transport representative of that phase class. Missing: no transport-independent canonical matrix statement follows from this computation alone.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:37-50`; `quantum/paper/jet_gram_quantum_note.md:107-152`; `quantum/paper/jet_gram_quantum_note.md:178-247`; `quantum/paper/jet_gram_quantum_note.md:300-315`; `quantum/findings.md:85-90`; `quantum/findings.md:115-122`; `quantum/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`; `quantum/20260423-133641-attack-qutrit-omega/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The one-parameter first-horizontal-jet setup from the working note; identity transport or, more generally, the reduced scalar-phase transport class; the fact that for this real normalized family the horizontal jet equals the ordinary derivative; direct algebraic differentiation and inner-product contraction in \(\mathbb R^3\).
- **Strongest objection**: The explicit matrix is proved only in the chosen real lift with identity transport, and only up to a global phase in the scalar-phase transport class. So this closes the benchmark computation, but not the larger question whether the full matrix \(\Omega(u,v)\) is a canonical transport-independent ray-space invariant.
- **Needed for promotion**: One explicit equal-overlap / different-second-singular-value witness pair and an adversarial check that the scalar-phase transport caveat is stated at the same place as the benchmark.
