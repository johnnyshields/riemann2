# gap-canonical-frames

- **Claim**: Let \(S_-,S_+\subset \mathcal H\) be the already-canonical endpoint subspaces in a common ambient Hilbert space, with orthogonal projectors \(\Pi_\pm\), and let
  \[
  K_-:=\Pi_-\Pi_+\Pi_-\big|_{S_-}.
  \]
  If every nonzero eigenvalue \(\lambda_i\in(0,1]\) of \(K_-\) is simple, then the corresponding normalized eigenvectors \(u_i\in S_-\) are canonical up to individual phase/sign. Writing \(\sigma_i:=\sqrt{\lambda_i}\) and
  \[
  v_i:=\sigma_i^{-1}\Pi_+u_i\in S_+,
  \]
  the vectors \(v_i\) are likewise canonical up to the same phase/sign, satisfy
  \[
  \Pi_+u_i=\sigma_i v_i,\qquad \Pi_-v_i=\sigma_i u_i,
  \qquad \langle u_i,v_j\rangle=\sigma_i\delta_{ij},
  \]
  and therefore give a canonical principal frame on the nonzero principal block. In these matched frames the comparison matrix is canonically diagonal:
  \[
  [\langle u_i,v_j\rangle]_{ij}=\operatorname{diag}(\sigma_1,\dots,\sigma_m),
  \]
  unique up to simultaneous phase/sign changes \((u_i,v_i)\mapsto (e^{i\phi_i}u_i,e^{i\phi_i}v_i)\). Thus simple nonzero projector spectrum gives canonical principal vectors and a diagonal representative for the nonzero block; it does not canonically fix bases on any zero-eigenspace or repeated-eigenvalue sector.
- **Status**: proved
- **Evidence**: Proved: the note already establishes that the endpoint ambient osculating subspaces are canonical and that the compression \(K_-\) has spectrum equal to the squared principal-angle cosines. Since \(K_-\) is a finite-rank self-adjoint positive operator on \(S_-\), each simple nonzero eigenvalue has a one-dimensional eigenspace, so its normalized eigenvector is canonical up to phase/sign. For such an eigenvector \(u_i\), \(\Pi_+u_i\neq0\) and \(\|\Pi_+u_i\|^2=\langle u_i,K_-u_i\rangle=\lambda_i\), so \(v_i:=\sigma_i^{-1}\Pi_+u_i\) is well defined and normalized. Then \(\Pi_-v_i=\sigma_i^{-1}K_-u_i=\sigma_i u_i\), and orthogonality across distinct \(i\) follows from spectral orthogonality. Hence the cross-Gram matrix in these paired frames is diagonal with entries \(\sigma_i\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:356-372`; `quantum/findings.md:62-69`; `quantum/teams/20260424-003729-attack-canonical-frames/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The ambient-subspace theorem for the endpoint spaces \(S_\pm\); fixed common ambient Hilbert space; standard spectral theorem for finite-rank positive self-adjoint operators; the identification of \(\operatorname{spec}(K_-)\) with squared principal-angle cosines; the explicit hypothesis that the nonzero spectrum is simple.
- **Strongest objection**: This diagonalization adds no invariant content beyond the principal-angle data; it only canonically chooses eigenvectors when the nonzero spectrum is simple. If any nonzero eigenvalue is repeated, the eigenspace has internal unitary freedom and no canonical principal frame follows.
- **Needed for promotion**: Keep it as a conditional normal-form corollary, not as a stronger general matrix theorem.
