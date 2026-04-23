# gap-quartit-representative

- **Claim**: For the quartit cubic benchmark, one can choose an orthonormal basis of the common intersection and complete it to orthonormal bases of the endpoint second-osculating spaces so that the resulting `3x3` comparison matrix is exactly `diag(1,1,sigma_3)`. This gives an explicit representative of the canonical second-order subspace data.
- **Status**: proved
- **Evidence**: The quartit second-osculating spaces are codimension-one `3`-planes in `R^4`; choosing two orthonormal vectors in their intersection and the normalized complement vectors gives an orthonormal-frame representative whose cross-Gram is diagonal with entries `(1,1,sigma_3)`.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:416-482`; `quantum/findings.md:128-135`; `quantum/teams/20260423-135757-attack-quartit-representative/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The quartit principal-angle theorem and explicit normal-vector formula.
- **Strongest objection**: It adds no invariant content beyond the principal-angle data.
- **Needed for promotion**: Use only as an explicit representative, not as a stronger matrix theorem.
