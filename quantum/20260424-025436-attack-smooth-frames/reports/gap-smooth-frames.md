# gap-smooth-frames

- **Claim**: Let \(I\subset\mathbb R\) be an interval and \(t\mapsto (S_-(t),S_+(t))\) a \(C^k\) path of finite-dimensional subspace pairs in a fixed Hilbert space, with \(C^k\) orthogonal projectors \(\Pi_\pm(t)\). Define the canonical compression
  \[
  K_-(t):=\Pi_-(t)\Pi_+(t)\Pi_-(t)\big|_{S_-(t)}.
  \]
  Fix \(t_0\in I\). If, on some neighborhood \(J\ni t_0\), the relevant nonzero eigenvalues \(\lambda_i(t)\in(0,1]\) of \(K_-(t)\) remain simple and separated from the rest of the spectrum, then after shrinking to \(J\) if needed there exist \(C^k\) local branches of canonical principal vectors \(u_i(t)\in S_-(t)\), unique up to a constant phase/sign on each branch, such that with \(\sigma_i(t)=\sqrt{\lambda_i(t)}\) and
  \[
  v_i(t):=\sigma_i(t)^{-1}\Pi_+(t)u_i(t)\in S_+(t),
  \]
  the vectors \(v_i(t)\) are also \(C^k\), and for all \(t\in J\),
  \[
  \Pi_+(t)u_i(t)=\sigma_i(t)v_i(t),\qquad
  \Pi_-(t)v_i(t)=\sigma_i(t)u_i(t),\qquad
  \langle u_i(t),v_j(t)\rangle=\sigma_i(t)\delta_{ij}.
  \]
  Thus the static simple-spectrum principal-frame corollary upgrades to a local smooth pathwise theorem on the simple nonzero spectral locus. On a whole interval, the same holds globally for each eigenvalue branch that stays nonzero and simple; the only ambiguity is branchwise constant phase/sign, while degeneracy or collision with \(0\) is the sharp obstruction.
- **Status**: heuristic
- **Evidence**: The static simple-spectrum corollary already gives canonical principal vectors at each fixed \(t\). The remaining ingredient is standard smooth perturbation theory for isolated simple eigenvalues of the self-adjoint family \(K_-(t)\). Under that input, the eigenprojections and normalized eigenvector branches are \(C^k\), and the formulas above follow exactly as in the static case. This is a plausible local smooth refinement, but it has not yet been folded into the main note because the supporting perturbation-theory assumptions and phase/sign bookkeeping have not been written there explicitly.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:397-423`; `quantum/findings.md:77-91`; `quantum/20260424-003729-attack-canonical-frames/reports/gap-canonical-frames.md:3-26`; `quantum/20260424-023315-attack-degenerate-nogo/reports/gap-degenerate-nogo.md:3-15`; `quantum/20260424-025436-attack-smooth-frames/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The static simple-spectrum principal-frame theorem; smooth dependence of the projector pair \(\Pi_\pm(t)\); standard smooth spectral perturbation theory for isolated simple eigenvalues.
- **Strongest objection**: This is not yet note-ready because the smooth-perturbation input and global sign/phase issues are not explicitly packaged in the current note. It adds no new invariant content beyond the static theorem.
- **Needed for promotion**: If ever promoted, it should be added only as a local regularity corollary, with the perturbation-theory hypothesis stated explicitly and with clear wording about phase/sign ambiguity and failure at eigenvalue collisions.
