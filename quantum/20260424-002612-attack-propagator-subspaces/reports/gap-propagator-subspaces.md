# gap-propagator-subspaces

- **Claim**: For an exact unitary orbit \(U_t=e^{-itH}\), the strongest exact finite-separation two-point formula is subspace-level and is given by the propagator compressed to the initial invariant space. Write \(\Delta=t_+-t_-\).

  For the ambient/Krylov case,
  \[
  K_r:=\operatorname{span}\{\psi_0,H\psi_0,\dots,H^r\psi_0\},\qquad
  A_r(t)=U_t K_r.
  \]
  Then the principal-angle cosines between \(A_r(t_-)\) and \(A_r(t_+)\) are exactly the singular values of
  \[
  C^{A}_r(\Delta):=\Pi_{K_r}e^{-i\Delta H}\big|_{K_r}:K_r\to K_r,
  \]
  and the squared cosines are exactly the spectrum of
  \[
  K^{A}_r(\Delta):=C^{A}_r(\Delta)\,C^{A}_r(\Delta)^*
  =\Pi_{K_r}e^{-i\Delta H}\Pi_{K_r}e^{i\Delta H}\big|_{K_r}.
  \]

  For the value-channel-removed / compressed-Krylov case,
  \[
  L_r:=K_r\cap\psi_0^\perp
      =\operatorname{span}\{P_0H\psi_0,\dots,P_0H^r\psi_0\},\qquad
  O_r(t)=U_t L_r.
  \]
  Then the principal-angle cosines between \(O_r(t_-)\) and \(O_r(t_+)\) are exactly the singular values of
  \[
  C^{O}_r(\Delta):=\Pi_{L_r}e^{-i\Delta H}\big|_{L_r}:L_r\to L_r,
  \]
  and the squared cosines are exactly the spectrum of
  \[
  K^{O}_r(\Delta):=C^{O}_r(\Delta)\,C^{O}_r(\Delta)^*
  =\Pi_{L_r}e^{-i\Delta H}\Pi_{L_r}e^{i\Delta H}\big|_{L_r}.
  \]

  Equivalently, if \(\Pi_\pm^{A}\) are the orthogonal projectors onto \(A_r(t_\pm)\), and \(\Pi_\pm^{O}\) onto \(O_r(t_\pm)\), then
  \[
  U_{t_-}^*(\Pi_-^{A}\Pi_+^{A}\Pi_-^{A})U_{t_-}=K_r^{A}(\Delta),\qquad
  U_{t_-}^*(\Pi_-^{O}\Pi_+^{O}\Pi_-^{O})U_{t_-}=K_r^{O}(\Delta).
  \]
- **Status**: proved
- **Evidence**: Proved: \(A_r(t)=U_tK_r\) and \(O_r(t)=U_tL_r\) exactly, from the unitary/Krylov identities already established. Hence the two endpoint pairs are \((U_{t_-}K_r,U_{t_+}K_r)\) and \((U_{t_-}L_r,U_{t_+}L_r)\). Principal angles are invariant under common unitary conjugation, so they equal the principal angles between \(K_r\) and \(e^{-i\Delta H}K_r\) in the \(A_r\) case, and between \(L_r\) and \(e^{-i\Delta H}L_r\) in the \(O_r\) case. For any finite-dimensional subspace \(S\), the principal-angle cosines between \(S\) and \(US\) are the singular values of the compressed operator \(\Pi_S U|_S\), and the squared cosines are the eigenvalues of \(\Pi_SU\Pi_SU^*|_S\). Applying this with \(S=K_r\) or \(S=L_r\) gives the formulas above.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:294-358`; `quantum/paper/jet_gram_quantum_note.md:368-389`; `quantum/findings.md:84-99`; `quantum/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-41`; `quantum/20260424-002612-attack-propagator-subspaces/notes/coordinator-brief.md:3-14`.
- **Dependencies**: Self-adjoint \(H\) with unitary flow \(U_t=e^{-itH}\); \(\psi_0\) in the domain of \(H^k\) up to order \(r\); the exact identifications \(A_r(t)=U_tK_r\) and \(O_r(t)=U_tL_r\); the standard principal-angle fact that for subspaces \(S,T\), the cosines are the singular values of \(\Pi_SU|_S\) in the unitary-orbit case.
- **Strongest objection**: This is exact only at the subspace/singular-value/projector-spectrum level. It does not produce a canonical entrywise matrix beyond basis-dependent realizations, and for \(O_r\) it does not collapse to the ordinary Krylov propagator of the compressed pair except in special invariant cases.
- **Needed for promotion**: Keep it as a short corollary after the unitary/Krylov remark, not as a new pillar.
