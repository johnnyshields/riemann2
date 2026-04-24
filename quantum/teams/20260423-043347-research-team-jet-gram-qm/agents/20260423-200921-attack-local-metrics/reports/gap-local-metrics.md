# gap-local-metrics

- **Claim**: Let \(x\mapsto S(x)\) be a \(C^1\) family of finite-dimensional subspaces of a fixed Hilbert space with locally constant rank, and let \(\Pi(x)\) be the orthogonal projector onto \(S(x)\). Then
  \[
  g^{\Pi}_{ab}(x):=\frac12\operatorname{Tr}\big((\partial_a\Pi)(\partial_b\Pi)\big)
  \]
  is an exact, basis-free, positive-semidefinite local tensor on the parameter manifold. It depends only on the subspace map \(S(\cdot)\), not on a chosen frame, and is the pullback of the canonical Grassmannian metric. For the canonical ambient subspace family \(A_r(x)\), this gives a clean exact local metric whenever \(\dim A_r\) is locally constant; likewise for \(O_r(x)\) when \(\dim O_r\) is locally constant. In the rank-one case \(A_0(x)=\mathrm{span}\{\psi(x)\}\), one has
  \[
  g^{\Pi}_{ab}=\Re\langle \partial_a\psi|(I-|\psi\rangle\langle\psi|)|\partial_b\psi\rangle=\Re Q_{ab},
  \]
  so \(r=0\) recovers exactly the Fubini-Study metric, i.e. the real part of the pure-state QGT.
- **Status**: proved
- **Evidence**: For any local orthonormal frame \(\Psi(x)\) of \(S(x)\), \(\Pi=\Psi\Psi^*\), and projector calculus gives \(\frac12\operatorname{Tr}((d\Pi)^2)=\operatorname{Tr}(d\Psi^*(I-\Pi)d\Psi)\), so the tensor is frame-independent and nonnegative. In the rank-one case \(\Pi=|\psi\rangle\langle\psi|\), direct differentiation gives \(\frac12\operatorname{Tr}((\partial_a\Pi)(\partial_b\Pi))=\Re Q_{ab}\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:55-80`; `quantum/findings.md:27-34`; `quantum/teams/20260423-200921-attack-local-metrics/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Fixed ambient Hilbert space; `C^1` constant-rank subspace family; orthogonal-projector calculus.
- **Strongest objection**: This is an exact local metric theorem, but it adds no new finite-separation invariant content beyond the existing principal-angle/projector package.
- **Needed for promotion**: If included, keep it as a short local Grassmannian corollary.
