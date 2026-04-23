# gap-matrix-data

- **Claim**: For a canonical pair of ambient subspaces, the strongest exact matrix-level statement is that any natural frame matrix is canonical only up to left/right unitary equivalence. The complete frame-free matrix data is therefore the singular-value list, equivalently the spectrum of the projector compression.
- **Status**: proved
- **Evidence**: If `U_-` and `U_+` are orthonormal frame isometries for the endpoint subspaces, the natural cross matrix is `C = U_-^* U_+`. Changing frames gives `C -> L C R` with unitary `L,R`, so only biunitary-invariant data survives canonically. By SVD, that invariant data is exactly the singular values, equivalently the projector-compression spectra.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:356-380`; `quantum/findings.md:62-79`; `quantum/teams/20260423-192358-attack-matrix-data/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Canonical ambient subspace pair and standard SVD/principal-angle theory.
- **Strongest objection**: This is operator/matrix packaging, not new invariant content.
- **Needed for promotion**: Already subsumed by the projector-spectrum and polar-transport package.
