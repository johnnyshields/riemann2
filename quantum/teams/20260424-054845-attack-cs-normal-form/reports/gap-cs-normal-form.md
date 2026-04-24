# gap-cs-normal-form

- **Claim**: Let \(S_-,S_+\subset \mathcal H\) be finite-dimensional subspaces of a finite-dimensional Hilbert space. Then there is an orthogonal decomposition
  \[
  \mathcal H = H_{00}\oplus\Bigl(\bigoplus_{j=1}^{\ell} H_{\theta_j}\Bigr)\oplus H_{10}\oplus H_{01}\oplus H_\perp,
  \]
  where:
  \[
  H_{00}=S_-\cap S_+,
  \qquad
  H_{10}=S_-\cap S_+^\perp,
  \qquad
  H_{01}=S_-^\perp\cap S_+,
  \qquad
  H_\perp=(S_-+S_+)^\perp,
  \]
  each \(H_{\theta_j}\) is a 2-plane carrying one principal angle \(\theta_j\in(0,\pi/2)\), and in suitable orthonormal bases \(e_j,f_j\) of \(H_{\theta_j}\)
  \[
  S_-\cap H_{\theta_j}=\operatorname{span}\{e_j\},
  \qquad
  S_+\cap H_{\theta_j}=\operatorname{span}\{\cos\theta_j\,e_j+\sin\theta_j\,f_j\}.
  \]
  Thus the ordered pair \((S_-,S_+)\) is classified up to ambient unitary equivalence by the dimensions
  \(
  \dim H_{00},\dim H_{10},\dim H_{01},\dim H_\perp
  \)
  together with the multiset \(\{\theta_j\}\). Equivalently, it is classified by
  \(
  \dim \mathcal H,\dim S_-,\dim S_+
  \)
  together with the principal-angle multiset (with multiplicities).

  In particular, the canonical principal-angle / operator package already in the note is complete for classifying finite-dimensional subspace pairs up to ambient unitary equivalence.
- **Status**: proved
- **Evidence**: Proved: the canonical cross-contraction \(C=\Pi_-|_{S_+}\) has singular values \(\cos\theta_j\). Choose orthonormal singular-vector pairs \((u_j,v_j)\) for the nonzero singular values, so \(Cv_j=\cos\theta_j u_j\) and \(\Pi_-v_j=\cos\theta_j u_j\). Then
  \[
  w_j:=\frac{v_j-\cos\theta_j u_j}{\sin\theta_j}
  \]
  is well defined and unit, orthogonal to \(u_j\), and the span of \(u_j,w_j\) is the 2-plane block \(H_{\theta_j}\). The zero-angle sector is exactly \(S_-\cap S_+\), the right-angle sectors are \(S_-\cap S_+^\perp\) and \(S_-^\perp\cap S_+\), and the remaining orthogonal complement is \((S_-+S_+)^\perp\). This yields the CS block form. The converse is immediate: a unitary that matches these blocks and angles matches the subspace pair. Since the note’s canonical operator package is exactly the principal-angle package in operator form, it is complete at this classification level.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:397-430`; `quantum/findings.md:73-91`; `quantum/teams/20260424-030000-attack-operator-package/reports/gap-operator-package.md:3-19`; `quantum/teams/20260424-044343-attack-completeness/reports/gap-completeness.md:3-17`; `quantum/teams/20260424-054845-attack-cs-normal-form/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Finite-dimensional principal-angle theory; the canonical operator package \((C,K_\pm,V)\); standard singular-vector construction on the nonzero principal blocks.
- **Strongest objection**: This is a finite-dimensional classification theorem for subspace pairs, not a stronger entrywise matrix theorem. It does not recover canonical bases inside repeated principal blocks; it only classifies the pair up to unitary equivalence.
- **Needed for promotion**: A short finite-dimensional corollary in the note is justified: the principal-angle/operator package is complete for classifying finite-dimensional subspace pairs up to ambient unitary equivalence.
