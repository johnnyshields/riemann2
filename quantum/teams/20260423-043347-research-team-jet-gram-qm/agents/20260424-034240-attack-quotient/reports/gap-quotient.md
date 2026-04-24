# gap-quotient

- **Claim**: Let \(L_r(\lambda):=\operatorname{span}\{\psi(\lambda)\}\subset A_r(\lambda)\). Then the orthogonal projector
  \[
  P_\lambda:=I-|\psi(\lambda)\rangle\langle\psi(\lambda)|
  \]
  restricts to a surjective map \(P_\lambda:A_r(\lambda)\to O_r(\lambda)\) with kernel \(L_r(\lambda)\). Hence it induces a canonical isometric isomorphism
  \[
  \widetilde P_\lambda:
  A_r(\lambda)/L_r(\lambda)\xrightarrow{\ \cong\ } O_r(\lambda),
  \qquad [v]\mapsto P_\lambda v.
  \]
  Equivalently, `O_r` is exactly the Hilbert-space quotient of `A_r` by the state line.
- **Status**: proved
- **Evidence**: The exact orthogonal decomposition \(A_r=\operatorname{span}\{\psi\}\oplus O_r\) is already established in the note. Since every generator of \(O_r\) is horizontal, \(O_r\subset\psi^\perp\), and for any \(v=a\psi+o\in A_r\) with \(o\in O_r\), one has \(P_\lambda v=o\). So \(P_\lambda|_{A_r}\) has kernel \(L_r\) and range \(O_r\). Because the decomposition is orthogonal, the quotient norm agrees exactly with the norm of the projected representative, making \(\widetilde P_\lambda\) an isometry.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:327-335`; `quantum/findings.md:70-74`; `quantum/teams/20260424-034240-attack-quotient/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The exact decomposition \(A_r=\operatorname{span}\{\psi\}\oplus O_r\); the ambient Hilbert-space projector \(P=I-|\psi\rangle\langle\psi|\).
- **Strongest objection**: This is a clean quotient interpretation, but it does not by itself decide whether `A_r` or `O_r` should be preferred in all roles, nor does it upgrade the two-point matrix story.
- **Needed for promotion**: Use it as a short interpretive corollary near the `A_r` / `O_r` discussion, not as a major standalone theorem.
