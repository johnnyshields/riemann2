- Claim

  The cleanest theorem-facing corrected-whitening transport bundle suggested by the current draft is a three-layer package, not a single automatic odd-package transport theorem.

  Proved layer: a corrected-whitening admissibility theorem. On the microscopic disk \(|s|<\rho_0/Q\), denominator comparability transfers the real-line omitted-zero shell bounds to the complex disk, hence the omitted smooth part \(g_{\sm}(t_\pm)\) and the derivatives needed in the corrected finite-\(s\) blocks are holomorphic there; from this, together with the same-point perturbation bound and baseline spectral gap, the corrected same-point blocks stay positive definite and the corrected whitened block \(\widehat\Omega_\zeta^{\corr}(s;m)\) is holomorphic.

  Conditional layer: a corrected local-deformation transport theorem. After fixing the anomaly core \(\mathcal C\), the full corrected deformation should be packaged as
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
  \]
  with all auxiliary-near, far-tail, jet-correction, and estimation terms internal to the same corrected cutoff-dependent scalar. This is the right structural theorem, but as a transport statement it is only safe conditional on a family-level theorem identifying the corrected value channel and proving that the decomposition is the genuine first-order/value-channel split rather than only a formal remainder definition.

  Missing layer: a family-specific odd transverse realization-and-boundary theorem. What transports from the current draft is only the statement that once a corrected odd holomorphic transverse scalar is realized and bounded on \(|s|=\rho_0/Q\), the odd expansion, Cauchy coefficient bounds, and \(N\)-point projector/cancellation machinery follow. Existence of that realized odd scalar, its post-correction symmetry mechanism, and the boundary estimate are not automatic from the corrected-whitening admissibility layer alone.

  The safe bundled conclusion is therefore: denominator comparability is a necessary subtheorem inside corrected-whitening transport; corrected whitening then transports the matrix object and preserves the transverse \(Q^{-3}\) gain after \(\Phi_K\) kills the value channel; the odd scalar theorem remains a separate family theorem target.

- Status

  heuristic

- Evidence

  Proved in the current draft:
  Proposition \(\ref{prop:denominator-comparability}\) proves the denominator lower/upper comparison and uses it to extend the omitted smooth part and the required \(t\)-derivatives holomorphically to \(|s|<\rho_0/Q\). Proposition \(\ref{prop:corrected-whitening}\) then uses that holomorphy, the removable-pole argument in the corrected mixed block, the same-point perturbation bound, and the baseline spectral gap to conclude holomorphic corrected whitening.

  Conditional on the draft's structural identifications:
  Proposition \(\ref{prop:corrected-local-decomposition}\) and Proposition \(\ref{prop:cutoff-compatibility}\) package the corrected object so that auxiliary, tail, jet, and estimation terms are internal to the corrected scalar. This is exactly the right theorem shape for transport. But the proof of the decomposition identifies \(R_\zeta\) by definition after expanding around \(S(m)=0\); it does not, in the cited region alone, supply an independent family-level theorem that the corrected value-channel derivative and its internal remainder decomposition persist in a portable way.

  Proved for preserved transverse gain once the corrected blocks are in hand:
  Proposition \(\ref{prop:whitened-mixed-transfer}\) shows that after first-order Fr\'echet expansion of whitening, the three linear transfer pieces and the quadratic error satisfy
  \[
  \Phi_K(\mathcal T_-),\ \Phi_K(\mathcal T_{\mix}),\ \Phi_K(\mathcal T_+)\ll S_2/Q^3,
  \qquad
  \Phi_K(\mathcal E_2)\ll S_2^2/Q^3,
  \]
  hence the corrected-minus-baseline whitened block keeps the same transverse \(Q^{-3}\) scale.

  Missing from local scope alone:
  In the odd-channel section, the boundary estimate and odd microscopic expansion use the internal decomposition plus the preserved \(Q^{-3}\) gain, but the broader transport lesson from the GRH notes is narrower: the odd/projector algebra transports only after a family supplies a realized corrected odd holomorphic transverse scalar and its microscopic boundary control. The notes explicitly warn against saying that the odd package transports automatically from source theorem plus positive \(S\).

- Exact refs

  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`

  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`

  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:6-49`

  `paper/proof_of_rh.tex:856-946` (`prop:denominator-comparability`)

  `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)

  `paper/proof_of_rh.tex:1497-1683` (`prop:corrected-local-decomposition`, `prop:cutoff-compatibility`)

  `paper/proof_of_rh.tex:1693-1886` and continuation (`prop:whitened-mixed-transfer`)

  `paper/proof_of_rh.tex:567-572` (`cor:PhiK-Aval-zero`)

  `paper/proof_of_rh.tex:2214-2322` (`eq:Hm-def`, `prop:boundary-estimate`, `prop:odd-expansion`)

- Dependencies

  Theorem \(\ref{thm:tail-curvature}\) for the smallness input \(S_2=o(Q)\) and the corrected-regime size comparison used at the boundary stage.

  Proposition \(\ref{prop:block-perturbation}\) and Proposition \(\ref{prop:cross-block-perturbation}\) for the same-point and mixed-block remainder sizes entering holomorphic whitening and the preserved \(Q^{-3}\) transfer.

  Corollary \(\ref{cor:PhiK-Aval-zero}\) for annihilation of the leading value channel.

  A separate family theorem realizing the corrected odd holomorphic transverse scalar and proving its boundary control.

- Strongest objection

  The draft currently encourages an over-tight packaging: the admissibility layer and the preserved \(\Phi_K\)-gain layer are genuinely theorem-shaped, but the jump from those layers to a transported odd scalar theorem is not justified from local corrected-whitening scope alone. In particular, the cited proof of \(\Delta_\zeta=S A_{\val}+R_\zeta\) defines \(R_\zeta\) after a formal expansion around \(S(m)=0\), and the boundary estimate then imports the corrected-regime comparison \(S_2\ll L(m)S(m)^2\). That is enough to motivate the theorem bundle, but not enough to say that odd transverse realization and boundary control transport automatically across families.

- Needed for promotion

  Prove a family-level corrected local-deformation theorem in which the value-channel derivative \(A_{\val}\) is identified intrinsically from the fixed core and the remainder \(R_\zeta\) is shown to be the genuine internal non-leading part, not only a formal definition.

  Prove the family analogue of the corrected same-point and mixed-block perturbation estimates with the same anisotropic entry scales needed for the Fr\'echet whitening expansion and the \(\Phi_K\)-level \(Q^{-3}\) gain.

  Prove the separate corrected odd transverse realization-and-boundary theorem: construct the realized odd holomorphic scalar in the chosen family/channel, prove the symmetry mechanism that makes it odd after correction/whitening, and prove the boundary estimate on \(|s|=\rho_0/Q\).
