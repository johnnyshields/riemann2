# gap-quartit-witness

- **Claim**: For the quartit cubic curve
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}},
  \]
  there is an explicit witness pair with equal endpoint overlap but different nontrivial second-osculating singular value. One such choice is
  \[
  (u,v)=(0,1),\qquad (u',v')=\left(\frac12,\alpha\right),
  \]
  where \(\alpha\) is the positive real root
  \[
  81x^6-16x^5+37x^4-128x^3-107x^2-256x-171=0,
  \]
  numerically \(\alpha\approx 1.5842613016400051\).
- **Status**: proved
- **Evidence**: Proved: the second osculating \(3\)-plane is the codimension-\(1\) hyperplane orthogonal to
  \[
  n(t)=(-t^3,3t^2,-3t,1)^T,
  \]
  so for endpoints \(u,v\) the principal-angle singular values are \(1,1,s_3(u,v)\), with
  \[
  s_3(u,v)=\frac{|1+9uv+9u^2v^2+u^3v^3|}{\sqrt{(1+9u^2+9u^4+u^6)(1+9v^2+9v^4+v^6)}}.
  \]
  The endpoint overlap is
  \[
  I(u,v)=\frac{1+uv+u^2v^2+u^3v^3}{\sqrt{(1+u^2+u^4+u^6)(1+v^2+v^4+v^6)}}.
  \]
  Proved: for \((u,v)=(0,1)\), \(I(0,1)=1/2\) and \(s_3(0,1)=1/(2\sqrt5)\). Proved: for \((u',v')=(1/2,\alpha)\), the defining polynomial for \(\alpha\) is exactly the cleared-denominator equation \(I(1/2,\alpha)=1/2\), so the overlaps agree. Proved: if \(s_3(1/2,\alpha)=1/(2\sqrt5)\), then \(\alpha\) would also satisfy
  \[
  45x^6-48x^5+201x^4-640x^3-519x^2-768x-207=0.
  \]
  These two polynomials are coprime, so this is impossible. Hence the nontrivial singular values differ. Numerically,
  \[
  s_3\!\left(\frac12,\alpha\right)\approx 0.3000986560411918.
  \]
  Conditional: this is an exact witness for the endpoint second-osculating subspaces, hence for identity transport; in the reduced scalar-phase transport class the singular values are unchanged. Missing: a deposited closed form for the full \(3\times3\) whitened second-jet block.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:249-299`; `quantum/findings.md:98-102,103-133`; `quantum/teams/20260423-134344-attack-higher-jets/reports/gap-higher-jet-benchmark.md:3-30`; `quantum/teams/20260423-135052-attack-quartit-osculating/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The higher-jet triangular-mixing / osculating-subspace repair already established in `quantum/`; the exact quartit normal vector \(n(t)\); the codimension-\(1\) principal-angle formula for \(3\)-planes in \(\mathbb R^4\); fixed identity transport or the reduced scalar-phase transport class.
- **Strongest objection**: This closes the witness problem at the subspace/singular-value level, not at the level of a transport-independent canonical second-jet matrix. A referee could still ask for the full whitened \(3\times3\) block written explicitly and matched directly to the same singular values.
- **Needed for promotion**: Add the explicit formulas for \(I(u,v)\) and \(s_3(u,v)\) to the note, record the witness pair \((0,1)\) and \((1/2,\alpha)\), and, if desired, append the coprime-polynomial check as the exact reason the singular values differ.
