# gap-lower-order-Or

- **Claim**: For the real Veronese curve
  \[
  v_n(t)=(1,t,\dots,t^n)^T,\qquad \psi_n(t)=\frac{v_n(t)}{\|v_n(t)\|},
  \]
  and any \(0\le r\le n-1\), the value-channel-free ambient subspace
  \[
  O_r(t)=\operatorname{span}\{j_1(t),\dots,j_r(t)\},
  \qquad j_k=(I-\psi_n\psi_n^T)\partial_t^k\psi_n,
  \]
  has the exact orthogonal-complement description
  \[
  O_r(t)^\perp=\operatorname{span}\{\psi_n(t)\}\oplus A_r(t)^\perp
  =\operatorname{span}\{\psi_n(t)\}\oplus
  \operatorname{Coeff}\!\big((x-t)^{r+1}\mathbb R_{\le n-r-1}[x]\big).
  \]
  Equivalently, a basis of \(O_r(t)^\perp\) is given by
  \[
  \psi_n(t),
  \quad
  \operatorname{Coeff}\big((x-t)^{r+1}\big),
  \quad
  \operatorname{Coeff}\big(x(x-t)^{r+1}\big),
  \ \,\dots,
  \operatorname{Coeff}\big(x^{n-r-1}(x-t)^{r+1}\big).
  \]
  So the lower-order value-channel-free Veronese side is as explicit as the lower-order ambient side at the complement level.
- **Status**: proved
- **Evidence**: Proved: the note and findings now record the exact decomposition
  \(A_r(t)=\operatorname{span}\{\psi_n(t)\}\oplus O_r(t)\), with
  \(\psi_n(t)\perp O_r(t)\). Therefore
  \[
  O_r(t)^\perp=\operatorname{span}\{\psi_n(t)\}\oplus A_r(t)^\perp.
  \]
  The lower-order ambient Veronese theorem gives
  \[
  A_r(t)^\perp=\operatorname{Coeff}\!\big((x-t)^{r+1}\mathbb R_{\le n-r-1}[x]\big).
  \]
  Combining the two gives the stated formula. No further argument is needed.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:327-335`; `quantum/findings.md:70-79,152-156`; `quantum/teams/20260423-195245-attack-lower-order-veronese/reports/gap-lower-order-veronese.md:3-17`; `quantum/teams/20260424-014948-attack-lower-order-Or/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The exact decomposition `A_r = span{psi} ⊕ O_r`; the deposited lower-order ambient Veronese complement theorem.
- **Strongest objection**: This is a clean complement-basis theorem, but still not a closed all-`(n,r)` principal-angle/singular-value formula. So it is best treated as a side corollary rather than a new main theorem.
- **Needed for promotion**: Add it to findings and, if useful, to the note as a brief side corollary after the lower-order ambient statement.
