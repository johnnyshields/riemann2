# gap-rank-growth

- **Claim**: Let
  \[
  K_\infty(H,\psi_0):=\mathrm{span}\{\psi_0,H\psi_0,H^2\psi_0,\dots\},
  \qquad \dim K_\infty(H,\psi_0)=m<\infty.
  \]
  For the exact unitary orbit \(\psi(t)=e^{-itH}\psi_0\), with
  \[
  A_r(t)=\mathrm{span}\{\psi(t),\partial_t\psi(t),\dots,\partial_t^r\psi(t)\},
  \qquad
  O_r(t)=\mathrm{span}\{j_1(t),\dots,j_r(t)\},
  \]
  the exact rank-growth formulas are
  \[
  \dim A_r(t)=\min(r+1,m),
  \qquad
  \dim O_r(t)=\min(r,m-1)=\min(r+1,m)-1.
  \]
  Equivalently,
  \[
  \dim A_r=
  \begin{cases}
  r+1,&0\le r\le m-1,\\
  m,&r\ge m,
  \end{cases}
  \qquad
  \dim O_r=
  \begin{cases}
  r,&0\le r\le m-1,\\
  m-1,&r\ge m.
  \end{cases}
  \]
- **Status**: proved
- **Evidence**: Proved: \(A_r(t)=e^{-itH}K_r\), where \(K_r=\mathrm{span}\{\psi_0,H\psi_0,\dots,H^r\psi_0\}\), so \(\dim A_r(t)=\dim K_r\). If \(\dim K_\infty=m<\infty\), then the first \(m\) Krylov vectors are independent; otherwise a first linear relation at order \(n<m\) would force all later powers into the same span and contradict \(\dim K_\infty=m\). Hence \(\dim K_r=\min(r+1,m)\). Since \(A_r=\mathrm{span}\{\psi\}\oplus O_r\), one gets \(\dim O_r=\dim A_r-1\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-347`; `quantum/findings.md:87-99`; `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-38`; `quantum/teams/20260424-021540-attack-rank-growth/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Exact unitary/Krylov identification; finite cyclic dimension hypothesis.
- **Strongest objection**: This is a useful finite-dimensional corollary, but not a new invariant theorem.
- **Needed for promotion**: At most a short remark in the unitary/Krylov subsection.
