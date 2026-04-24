# gap-orthopoly-basis

- **Claim**: In the exact unitary/Krylov specialization, the spectral measure \(\mu(B)=\langle\psi_0,E_H(B)\psi_0\rangle\) canonically determines orthonormal polynomial data, hence a canonical orthonormal basis of \(A_r(t)\), and a centered analogue for \(O_r(t)\), up to the finite-rank cutoff. Precisely: let \(p_0,\dots,p_r\) be the orthonormal polynomials in \(L^2(\mu)\) obtained from \(1,\lambda,\dots,\lambda^r\) by Gram-Schmidt with positive leading coefficients, whenever the order-\(r\) Hankel form is nondegenerate. Under the canonical cyclic spectral identification \(W(f(H)\psi_0)=f\), the vectors
  \[
  e_k(t):=e^{-itH}p_k(H)\psi_0,\qquad 0\le k\le r,
  \]
  form a canonical orthonormal basis of \(A_r(t)\). Moreover \(p_k\perp 1\) for \(k\ge1\), so \(e_1(t),\dots,e_r(t)\) give a canonical orthonormal basis of \(O_r(t)\). In this basis, \(H\) has the canonical Jacobi/Lanczos tridiagonal matrix determined by \(\mu\), and the exact two-point compressed propagator matrices become
  \[
  U^{A_r}_{jk}(\Delta)=\int e^{-i\Delta\lambda}p_j(\lambda)\overline{p_k(\lambda)}\,d\mu(\lambda),
  \]
  with the `O_r` package given by the centered block `1 <= j,k <= r`.
- **Status**: proved
- **Evidence**: The exact unitary/Krylov theorem already identifies `A_r(t)` with the transported order-`r` Krylov space and the spectral-moment corollary rewrites the corresponding two-point matrices as moment matrices of `μ`. Orthogonalizing the monomial Krylov list against `μ` with the positive-leading-coefficient convention therefore gives a canonical orthonormal basis realization of the same exact subspace/package. Since degree-`k` orthonormal polynomials with `k>=1` are orthogonal to the constant polynomial, they automatically yield the `O_r` basis by dropping `p_0`.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-359`; `quantum/findings.md:89-124`; `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-38`; `quantum/teams/20260424-005339-attack-spectral-moments/reports/gap-spectral-moments.md:3-20`; `quantum/teams/20260424-042727-attack-orthopoly-basis/notes/coordinator-brief.md:3-15`.
- **Dependencies**: Spectral theorem for the cyclic pair `(H, psi_0)`; nondegeneracy of the moment form up to order `r`; positive-leading-coefficient normalization for orthonormal polynomials.
- **Strongest objection**: This is canonical only inside the exact unitary/Krylov specialization and adds basis structure rather than new invariant content. It does not strengthen the main subspace/operator theorem outside that setting.
- **Needed for promotion**: If later promoted, keep it as a specialized unitary/Lanczos normal form, not as part of the main invariant spine.
