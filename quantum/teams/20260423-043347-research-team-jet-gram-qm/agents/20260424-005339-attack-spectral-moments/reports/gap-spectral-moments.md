# gap-spectral-moments

- **Claim**: Let `mu(B)=<psi_0, E_H(B) psi_0>` be the spectral measure of `(H, psi_0)` and write
  \[
  m_n(\Delta):=\int \lambda^n e^{-i\Delta\lambda}\,d\mu(\lambda).
  \]
  Then for exact unitary orbits, the ambient/Krylov package `A_r` gives an exact truncated Hankel moment matrix:
  \[
  N^{A_r}_{jk}(\Delta)=m_{j+k}(\Delta)
  \]
  in the monomial Krylov list `H^j psi_0`. The value-channel-free side `O_r` gives the corresponding centered-polynomial moment package:
  \[
  N^{O_r}_{jk}(\Delta)=\int (\lambda^j-m_j(0))(\lambda^k-m_k(0))e^{-i\Delta\lambda}\,d\mu(\lambda).
  \]
- **Status**: proved
- **Evidence**: This is a direct spectral-theorem rewrite of the exact unitary/Krylov identities: `A_r` is the transported monomial Krylov space, while `O_r` is the transported centered-polynomial / compressed Krylov space. The two-point compressed propagator matrices are therefore the corresponding twisted moment matrices.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-359`; `quantum/findings.md:80-95`; `quantum/teams/20260424-005339-attack-spectral-moments/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Spectral theorem for `H`, exact unitary/Krylov package.
- **Strongest objection**: This is a basis-dependent realization, not new invariant content.
- **Needed for promotion**: Keep as a short corollary if ever used; otherwise archive-only is fine.
