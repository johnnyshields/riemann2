# gap-commutator-metric

- **Claim**: Let \(S(t)=U_tS(0)\) with \(U_t=e^{-itH}\), and let \(\Pi_t\) be the orthogonal projector onto \(S(t)\). Then the exact local projector metric
  \[
  g_S(t):=\frac12\,\mathrm{Tr}\bigl(\dot\Pi_t^{\,2}\bigr)=\frac12\|\dot\Pi_t\|_{HS}^2
  \]
  has the exact commutator form
  \[
  \dot\Pi_t=-i[H,\Pi_t],
  \qquad
  g_S(t)=\frac12\|[H,\Pi_t]\|_{HS}^2.
  \]
  Writing the off-subspace leakage block as
  \[
  L_t:=(I-\Pi_t)H\Pi_t,
  \]
  one has the exact identities
  \[
  [H,\Pi_t]=L_t-L_t^\ast,
  \qquad
  g_S(t)=\|L_t\|_{HS}^2
  =\mathrm{Tr}\bigl(\Pi_t H(I-\Pi_t)H\Pi_t\bigr).
  \]
  So the local subspace speed is exactly the Hilbert-Schmidt size of the Hamiltonian block that leaks \(S(t)\) into \(S(t)^\perp\).
- **Status**: proved
- **Evidence**: Proved: \(\Pi_t=U_t\Pi_0U_t^\ast\), so differentiating gives
  \[
  \dot\Pi_t=(-iH)U_t\Pi_0U_t^\ast+U_t\Pi_0(iH)U_t^\ast=-i[H,\Pi_t].
  \]
  Hence \(g_S(t)=\frac12\|[H,\Pi_t]\|_{HS}^2\). In block form relative to
  \(S(t)\oplus S(t)^\perp\),
  \[
  [H,\Pi_t]=\begin{pmatrix}0&-L_t^\ast\\ L_t&0\end{pmatrix},
  \]
  so \(\frac12\|[H,\Pi_t]\|_{HS}^2=\|L_t\|_{HS}^2\), giving the leakage formula.
  For rank one, \(\Pi_t=|\psi(t)\rangle\langle\psi(t)|\), this reduces to
  \[
  g_S(t)=\langle \psi(t),H(I-\Pi_t)H\psi(t)\rangle
  =\langle H^2\rangle_{\psi(t)}-\langle H\rangle_{\psi(t)}^2,
  \]
  i.e. the usual Fubini-Study / pure-state QGT metric along the unitary orbit.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:55-80`; `quantum/paper/jet_gram_quantum_note.md:343-347`; `quantum/paper/jet_gram_quantum_note.md:356-372`; `quantum/findings.md:27-34`; `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-38`; `quantum/teams/20260424-001425-attack-commutator-metric/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Finite-rank orthogonal projector \(\Pi_t\) onto the moving subspace \(S(t)\); unitary orbit \(S(t)=U_tS(0)\) with \(U_t=e^{-itH}\); self-adjoint \(H\); differentiability of \(t\mapsto \Pi_t\).
- **Strongest objection**: This is an infinitesimal reformulation of standard projector dynamics, not a new two-point invariant and not a stronger theorem than the existing subspace/principal-angle framework.
- **Needed for promotion**: If included in the note, keep it as a short corollary immediately after the projector/subspace discussion.
