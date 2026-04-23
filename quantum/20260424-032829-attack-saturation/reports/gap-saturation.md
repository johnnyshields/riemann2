# gap-saturation

- **Claim**: Let
  \[
  K_\infty(H,\psi_0):=\operatorname{span}\{\psi_0,H\psi_0,H^2\psi_0,\dots\},
  \qquad \dim K_\infty(H,\psi_0)=m<\infty,
  \]
  and let \(\psi(t)=e^{-itH}\psi_0\) be an exact unitary orbit. Define
  \[
  A_r(t)=\operatorname{span}\{\psi(t),\partial_t\psi(t),\dots,\partial_t^r\psi(t)\},
  \qquad
  O_r(t)=\operatorname{span}\{j_1(t),\dots,j_r(t)\}.
  \]
  Then for every \(r\ge m-1\),
  \[
  A_r(t)=e^{-itH}K_\infty(H,\psi_0),
  \qquad
  O_r(t)=e^{-itH}\bigl(K_\infty(H,\psi_0)\cap \psi_0^\perp\bigr).
  \]
  Hence the exact two-point subspace invariants stabilize at order \(m-1\): for any endpoints \(t_\pm\) and every \(r\ge m-1\), the principal-angle cosines, projector-compression spectra, and compressed-propagator singular values for the pair \((A_r(t_-),A_r(t_+))\) are independent of \(r\) and equal those for \(r=m-1\); likewise for \((O_r(t_-),O_r(t_+))\).
- **Status**: proved
- **Evidence**: Proved: \(A_r(t)=e^{-itH}K_r\) and \(O_r(t)=e^{-itH}L_r\), where \(K_r=\operatorname{span}\{\psi_0,H\psi_0,\dots,H^r\psi_0\}\) and \(L_r=K_r\cap\psi_0^\perp\). If \(\dim K_\infty=m<\infty\), then \(K_r=K_\infty\) for all \(r\ge m-1\). Since \(A_r=\operatorname{span}\{\psi\}\oplus O_r\), one gets \(L_r=K_\infty\cap\psi_0^\perp\) for all \(r\ge m-1\). Therefore the endpoint subspaces themselves stabilize, and so do all their exact two-point subspace/principal-angle/projector-spectrum invariants.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-347`; `quantum/findings.md:87-99`; `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-40`; `quantum/teams/20260424-021540-attack-rank-growth/reports/gap-rank-growth.md:3-39`; `quantum/teams/20260424-002612-attack-propagator-subspaces/reports/gap-propagator-subspaces.md:3-46`; `quantum/20260424-032829-attack-saturation/notes/coordinator-brief.md:3-10`.
- **Dependencies**: Exact unitary orbit hypothesis; finite cyclic dimension \(m<\infty\); the proved identifications of \(A_r\) and \(O_r\) with transported Krylov/compressed-Krylov spaces.
- **Strongest objection**: This is exact but specialized. It is only a finite-cyclic corollary of the exact unitary/Krylov picture, not a new invariant theorem.
- **Needed for promotion**: Include as a short corollary in the unitary/Krylov subsection, explicitly marked as finite-cyclic and subspace-level.
