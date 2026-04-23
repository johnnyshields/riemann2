# gap-complement-relation

- **Claim**: The exact complement-level relation is
  \[
  O_r(\lambda)^\perp=\operatorname{span}\{\psi(\lambda)\}\oplus A_r(\lambda)^\perp,
  \qquad
  A_r(\lambda)^\perp=O_r(\lambda)^\perp\cap \psi(\lambda)^\perp.
  \]
  So the exact `A_r` two-point data is the principal-angle data of the codimension-one complement summands inside `O_r^\perp`, while `O_r` can be finer because its complement still contains the extra value-channel line.
- **Status**: proved
- **Evidence**: This follows directly from the exact orthogonal decomposition `A_r = span{psi} ⊕ O_r`. Taking orthogonal complements gives the displayed formulas. This is the abstract reason the quartit benchmark can have `O_2` finer than `A_2`.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:327-348`; `quantum/findings.md:116-124`; `quantum/teams/20260424-022538-attack-complement-relation/notes/coordinator-brief.md:3-12`.
- **Dependencies**: The exact decomposition `A_r = span{psi} ⊕ O_r`.
- **Strongest objection**: This is a conceptual complement theorem, not by itself a closed two-point spectral formula.
- **Needed for promotion**: Use only as a supporting corollary; the main note does not need a full standalone statement unless the narrative calls for it.
