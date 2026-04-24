# gap-smooth-polar

- **Claim**: Let \(I\subset \mathbb R\) be an interval and \(t\mapsto (S_-(t),S_+(t))\) a \(C^\infty\) path of canonical endpoint subspace pairs in a fixed ambient Hilbert space \(\mathcal H\), with orthogonal projectors \(\Pi_\pm(t)\). Define the ambient canonical cross-contraction
  \[
  C(t):=\Pi_-(t)\Pi_+(t),
  \]
  equivalently \(C(t)=\Pi_-(t)|_{S_+(t)}:S_+(t)\to S_-(t)\). If \(\operatorname{rank} C(t)\) is constant on a neighborhood of \(t_0\), then the polar partial isometry \(V(t)\) in
  \[
  C(t)=V(t)\,|C(t)|
  \]
  is locally as smooth as the projector path. Equivalently, on any constant-rank locus the canonical operator-level transport given by the polar factor is locally smooth. A convenient formula is
  \[
  V(t)=C(t)\,|C(t)|^\dagger
      =C(t)\,(C(t)^*C(t))^{\dagger 1/2},
  \]
  with \(\dagger\) the Moore-Penrose inverse.
- **Status**: heuristic
- **Evidence**: The static operator package already gives the canonical cross-contraction \(C\), the positive factors \(K_\pm\), and the polar factor \(V\). If \(t\mapsto \Pi_\pm(t)\) is smooth, then so are \(C(t)\), \(K_\pm(t)\). On a constant-rank locus, the kernel dimension of \(C(t)\) is constant, so the support projection of \(|C(t)|\) should vary smoothly, and standard functional calculus on the positive invertible part then yields smooth \((C(t)^*C(t))^{\dagger 1/2}\), hence smooth \(V(t)\). This is the operator-level analogue of the simpler pathwise smoothness one expects on isolated simple principal-value branches, but it does not require simplicity, only constant rank. The result is still kept out of the main note because the smooth dependence argument has not yet been packaged there explicitly.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:387-445`; `quantum/findings.md:73-91`; `quantum/teams/20260424-020810-attack-polar-transport/reports/gap-polar-transport.md:3-24`; `quantum/teams/20260424-030928-attack-smooth-polar/notes/coordinator-brief.md:3-10`.
- **Dependencies**: Smooth ambient projector path \(t\mapsto \Pi_\pm(t)\); constant rank of the cross-contraction; standard smooth dependence of polar factors / pseudoinverses on constant-rank families.
- **Strongest objection**: This is not yet note-ready because the smooth perturbation input has not been made explicit there. It adds pathwise regularity, not new invariant content.
- **Needed for promotion**: Write the smooth-dependence argument explicitly enough to cite, and keep it as a local regularity corollary rather than a new invariant theorem.
