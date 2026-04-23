# gap-lower-order-veronese

- **Claim**: For the real Veronese curve
  \[
  v_n(t)=(1,t,\dots,t^n)^T\in\mathbb R^{n+1},
  \]
  the ambient order-\(r\) osculating space for any \(0\le r\le n-1\),
  \[
  A_r(t):=\operatorname{span}\{v_n(t),v_n'(t),\dots,v_n^{(r)}(t)\},
  \]
  admits a clean exact complement description. Identifying a vector \(c=(c_0,\dots,c_n)^T\) with the polynomial \(p_c(x)=\sum_{k=0}^n c_k x^k\), one has
  \[
  c\in A_r(t)^\perp
  \quad\Longleftrightarrow\quad
  p_c^{(j)}(t)=0\ \text{for }0\le j\le r
  \quad\Longleftrightarrow\quad
  (x-t)^{r+1}\mid p_c(x).
  \]
  Hence
  \[
  A_r(t)^\perp
  =
  \operatorname{Coeff}\!\big((x-t)^{r+1}\mathbb R_{\le n-r-1}[x]\big),
  \]
  a subspace of dimension \(n-r\). An explicit basis is given by the coefficient vectors of
  \[
  (x-t)^{r+1},\ x(x-t)^{r+1},\ \dots,\ x^{n-r-1}(x-t)^{r+1}.
  \]
  Equivalently, for the normalized curve \(\psi_n(t)=v_n(t)/\|v_n(t)\|\), the ambient osculating space
  \[
  \operatorname{span}\{\psi_n(t),\partial_t\psi_n(t),\dots,\partial_t^r\psi_n(t)\}
  \]
  has the same orthogonal complement.
- **Status**: proved
- **Evidence**: Proved: \(\partial_t^j v_n(t)\) has \(k\)-th coordinate \(k(k-1)\cdots(k-j+1)t^{k-j}\), so for \(c\leftrightarrow p_c\),
  \[
  c\cdot v_n^{(j)}(t)=p_c^{(j)}(t).
  \]
  Therefore \(c\perp A_r(t)\) iff \(p_c^{(j)}(t)=0\) for \(0\le j\le r\), i.e. iff \(p_c\) has a root of multiplicity at least \(r+1\) at \(t\), equivalently \(p_c(x)=(x-t)^{r+1}q(x)\) with \(\deg q\le n-r-1\). This gives the explicit basis above and shows \(\dim A_r(t)^\perp=n-r\). Proved: replacing \(v_n\) by \(\psi_n=\|v_n\|^{-1}v_n\) does not change the osculating span, because \((\psi_n,\partial_t\psi_n,\dots,\partial_t^r\psi_n)\) is obtained from \((v_n,v_n',\dots,v_n^{(r)})\) by an invertible lower-triangular same-point change of basis. Conditional: this gives an exact ambient-subspace/complement theorem in the fixed Euclidean ambient space \(\mathbb R^{n+1}\). Missing: no deposited argument gives a comparably simple closed-form diagonalization of the lower-order cross-complement Gram matrices, so the clean theorem is the complement-basis description itself, not a full lower-order principal-angle formula.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:318-336`; `quantum/paper/jet_gram_quantum_note.md:574-590`; `quantum/findings.md:54-60`; `quantum/teams/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md:9-18`; `quantum/teams/20260423-195245-attack-lower-order-veronese/notes/coordinator-brief.md:5-14`.
- **Dependencies**: Elementary polynomial/jet duality; the fact that \(c\cdot v_n^{(j)}(t)=p_c^{(j)}(t)\); multiplicity-\((r+1)\) roots are exactly divisibility by \((x-t)^{r+1}\); invertible lower-triangular change from normalized derivatives to raw polynomial derivatives; fixed common ambient inner product on coefficient space.
- **Strongest objection**: The clean statement is about the annihilator/complement basis, not about a closed two-point spectral formula. For \(r=n-1\) the complement is \(1\)-dimensional and collapses to the single normal \((x-t)^n\), which is why the earlier theorem becomes especially sharp. For general \(r<n-1\), the complement has dimension \(n-r\), and the present record does not show that the associated two-point complement Gram matrix has a comparably simple canonical singular-value formula.
- **Needed for promotion**: Promote only the lower-order ambient complement theorem in the form
  \[
  A_r(t)^\perp=\operatorname{Coeff}\!\big((x-t)^{r+1}\mathbb R_{\le n-r-1}[x]\big),
  \]
  with the explicit monomial basis above and the explicit caveat that no equally clean all-\((n,r)\) principal-angle/singular-value formula is currently proved for \(r<n-1\).
