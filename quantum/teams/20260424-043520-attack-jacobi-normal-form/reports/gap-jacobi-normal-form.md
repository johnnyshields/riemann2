# gap-jacobi-normal-form

- **Claim**: Let `(H, psi_0)` be an exact unitary cyclic pair with finite cyclic dimension
  \[
  K_\infty(H,\psi_0):=\operatorname{span}\{\psi_0,H\psi_0,H^2\psi_0,\dots\},\qquad \dim K_\infty(H,\psi_0)=m<\infty,
  \]
  and let `mu` be its spectral measure. Let `p_0,...,p_{m-1}` be the orthonormal polynomials in `L^2(mu)` obtained from `1, λ, ..., λ^{m-1}` by Gram-Schmidt with positive leading coefficients, and let `J` be the corresponding finite Jacobi matrix for multiplication by `λ`. Then the finite-cyclic exact unitary package has a canonical Jacobi normal form:
  \[
  e_k(t):=e^{-itH}p_k(H)\psi_0,
  \qquad 0\le k\le m-1,
  \]
  is a canonical orthonormal basis of `A_{m-1}(t)`, and in this basis
  \[
  H|_{A_{m-1}(t)}\sim J,
  \qquad
  \Pi_{A_{m-1}(t_-) }e^{-i\Delta H}\big|_{A_{m-1}(t_-)}\sim e^{-i\Delta J},
  \qquad \Delta=t_+-t_-.
  \]
  Thus the full ambient finite-cyclic two-point package is exactly the finite Jacobi matrix model together with the canonical matrix function `e^{-i Δ J}`. On the `O` side, the canonical basis is `e_1(t),...,e_{m-1}(t)`, and the exact compressed propagator is the corresponding block/compression of `e^{-i Δ J}`.
- **Status**: proved
- **Evidence**: The exact unitary/Krylov theorem identifies `A_r(t)` with transported Krylov spaces and the spectral-moment theorem identifies the exact propagator/compression matrices with moment kernels of `mu`. Orthogonalizing monomials in `L^2(mu)` therefore gives a canonical orthonormal basis of the full finite cyclic space and its unitary transports. Multiplication by `λ` is exactly the Jacobi matrix in that basis, so functional calculus gives the `e^{-iΔJ}` formula. Since `p_k ⟂ 1` for `k>=1`, dropping `p_0` yields the canonical `O`-basis.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-365`; `quantum/findings.md:89-109`; `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-38`; `quantum/teams/20260424-005339-attack-spectral-moments/reports/gap-spectral-moments.md:3-20`; `quantum/teams/20260424-043520-attack-jacobi-normal-form/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Exact unitary orbit; finite cyclic dimension; spectral theorem; orthogonal-polynomial/Lanczos construction.
- **Strongest objection**: This is a canonical matrix realization only in the finite-cyclic exact unitary specialization. It does not upgrade the general subspace package to a general canonical matrix theorem, and on the `O` side the exact statement is a compression/block of `e^{-iΔJ}`, not an independent smaller Jacobi functional calculus theorem.
- **Needed for promotion**: If included in the note, keep it as a finite-cyclic normal-form corollary under the exact unitary/Krylov specialization.
