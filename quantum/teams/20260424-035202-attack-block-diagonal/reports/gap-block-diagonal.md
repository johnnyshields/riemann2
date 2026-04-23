# gap-block-diagonal

- **Claim**: Let \(L_\pm:=\operatorname{span}\{\psi_\pm\}\), \(A_\pm:=A_r(\lambda_\pm)\), and \(O_\pm:=O_r(\lambda_\pm)\). Since
  \[
  A_\pm=L_\pm\oplus O_\pm
  \quad\text{orthogonally},
  \qquad
  O_\pm^\perp=L_\pm\oplus A_\pm^\perp,
  \]
  the complement comparison for \(O_r\) between the two endpoints has an adapted block form
  \[
  C_{O^\perp}=
  \begin{pmatrix}
  \langle \psi_-,\psi_+\rangle & \langle \psi_-,A_+^\perp\rangle\\
  \langle A_-^\perp,\psi_+\rangle & C_{A^\perp}
  \end{pmatrix}.
  \]
  Therefore the strongest exact criterion for the split
  \[
  O_-^\perp \leftrightarrow O_+^\perp
  \quad=\quad
  \text{value-channel line comparison } \oplus \text{ }A_-^\perp\leftrightarrow A_+^\perp
  \]
  is exactly
  \[
  \psi_-\perp A_+^\perp
  \quad\text{and}\quad
  \psi_+\perp A_-^\perp,
  \]
  equivalently
  \[
  L_-\subset A_+
  \quad\text{and}\quad
  L_+\subset A_-.
  \]
  In that and only that case, every orthonormal-basis comparison of \(O_r^\perp\) adapted to \(L_\pm\oplus A_\pm^\perp\) is block diagonal, with a `1x1` value-line block \(\langle\psi_-,\psi_+\rangle\) and the \(A_r^\perp\) comparison block.
- **Status**: proved
- **Evidence**: The exact orthogonal decomposition \(A_r=L_r\oplus O_r\) is already established, hence \(O_r^\perp=L_r\oplus A_r^\perp\). With orthonormal bases adapted to these sums, the comparison matrix has the displayed block form, so splitting is equivalent to vanishing of the off-diagonal blocks. Those vanish exactly when \(\psi_-\perp A_+^\perp\) and \(\psi_+\perp A_-^\perp\), i.e. exactly when \(L_-\subset A_+\) and \(L_+\subset A_-\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:327-346`; `quantum/findings.md:116-124`; `quantum/teams/20260424-034240-attack-quotient/reports/gap-quotient.md:3-18`; `quantum/teams/20260424-035202-attack-block-diagonal/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Orthogonal decomposition \(A_r=L_r\oplus O_r\); complement identity \(O_r^\perp=L_r\oplus A_r^\perp\); elementary Hilbert-space fact \(x\perp A^\perp\iff x\in A\).
- **Strongest objection**: This is a clean complement-level criterion, but it is specialized and does not by itself advance the main invariant package beyond the already-safe quotient relation and benchmark complement formulas.
- **Needed for promotion**: If ever used, keep it as a benchmark/complement corollary rather than a main theorem.
