# gap-completeness

- **Claim**: For finite-dimensional subspace pairs, the principal-angle/operator package is complete up to ambient unitary equivalence once endpoint and ambient dimensions are included.
- **Status**: proved
- **Evidence**: The canonical operator package `C = Pi_-|_{S_+}`, `K_± = C* C, C C*`, the polar factor `V`, and the principal-angle multiset encode exactly the singular values of `C`. In finite dimension, standard principal-angle / CS decomposition shows that two ordered subspace pairs are ambient-unitarily equivalent iff they have the same endpoint dimensions and the same principal angles with multiplicities; equivalently, iff their canonical cross-contractions have the same singular-value data with the matching dimension data.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:405-448`; `quantum/findings.md:73-91`; `quantum/teams/20260424-030000-attack-operator-package/reports/gap-operator-package.md:3-19`; `quantum/teams/20260424-044343-attack-completeness/notes/coordinator-brief.md:3-10`.
- **Dependencies**: Finite-dimensional principal-angle/CS decomposition; fixed convention on ordered pair and ambient dimension.
- **Strongest objection**: This is a completeness statement for classifying subspace pairs up to unitary equivalence, not a stronger entrywise matrix theorem.
- **Needed for promotion**: A self-contained CS block normal form would make this cleaner for note-level inclusion.
