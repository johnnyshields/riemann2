**Claim**

The cleanest exact boundary is:

- **Minimal local admissibility / exact slot meaning** consists only of the hypotheses needed to make the paired manuscript-style objects well-defined: a compact-interval paired source decomposition with unified `B_\chi^{\pair}` and exact `S_\chi^{\pair}`, a symmetric local normal form for the paired window, microscopic holomorphy/removable-singularity control for the corrected same-point and mixed blocks, positive same-point blocks so inverse-square-root whitening exists holomorphically, and the resulting first-order paired value-channel derivative `A_{\val,\chi}^{\pair}`.
- **Quantitative corrected-whitening transport** begins only when one asks for theorem-level input that transports real-line control into the microscopic disk with explicit size preservation: denominator comparability, omitted-smooth holomorphy proved from that comparability, holomorphic corrected whitening proved uniformly on the disk, preserved post-`\Phi_K` transfer scale, and the resulting bounds on `R_\chi^{\pair}` / boundary odd coefficients.

So the paired slot theorem should be read as `source + slot + minimal local admissibility`, while denominator comparability and transfer-scale preservation belong to a later quantitative transport theorem.

**Status**

conditional

**Evidence**

Proved from the supplied notes/manuscript interface:

- `paired_slot_hypotheses.md` states that source alone is insufficient and isolates the minimal extra package as: symmetric local normal form, corrected-whitening admissibility sufficient to define the corrected paired whitened block, and a first-order paired value-channel derivative, with downstream items listed separately as remainder dominance, quantitative corrected-whitening transport, odd/transverse realization, and boundary estimates.
- In the manuscript, the exact local decomposition
  `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`
  is an analytic-whitening statement, so some local admissibility is part of exact object definition rather than later estimation.
- The manuscript also separates this definitional layer from the later transfer layer: denominator comparability, perturbative block transfer, preserved `Q^{-3}` transverse scale, sharpened remainder estimates, and boundary control are proved strictly after the corrected local deformation has already been defined.
- `corrected_whitening_transport.md` explicitly says corrected-whitening transport is only a partial intermediate bundle, and lists as its safe bundle: denominator comparability plus omitted-smooth holomorphy, holomorphic corrected whitening with positive same-point blocks, and preserved post-`\Phi_K` transfer scale. That is already a quantitative transport package, not merely object definition.
- `denominator_theorem.md` narrows denominator comparability further: it is a necessary subtheorem inside corrected-whitening transport whose role is to carry real-line omitted-zero control into the microscopic disk and support corrected-whitening admissibility. This makes it upstream support for transport, not the clean hypothesis boundary for exact slot meaning.

Conditional on paired-family lift:

- The paired analogue should inherit the same boundary if one can formulate the paired corrected local deformation and its background expansion in the manuscript interface. Then the paired exact theorem would end at
  `\Delta_\chi^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_\chi^{\pair}`,
  with no smallness claim on `R_\chi^{\pair}`.
- Under that lift, the only corrected-whitening content imported into the paired slot theorem is the admissibility fragment needed for definability: microscopic holomorphy/removable poles, positive same-point blocks, and holomorphic inverse-square-root whitening.

Missing / not yet proved by the supplied material:

- A paired-family theorem showing that the compact-interval paired source scalar `S_\chi^{\pair}(m)` is exactly the coefficient of the first paired value-channel derivative in the corrected whitened local deformation.
- A clean paired proof that the admissibility fragment can be assumed or proved independently of the stronger denominator-comparability / preserved-scale transport estimates.
- A paired quantitative transport theorem proving the analogue of the manuscript's preserved post-`\Phi_K` transfer scale and the consequent remainder/boundary estimates.

**Exact refs**

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-18,25-40`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:6-27`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`
- `paper/proof_of_rh.tex:1497-1622` (`Corrected local deformation decomposition with fixed core`)
- `paper/proof_of_rh.tex:856-903` (`Microscopic denominator comparability and omitted-smooth holomorphy`)
- `paper/proof_of_rh.tex:1392-1458` (`Corrected finite-s holomorphic whitening`)
- `paper/proof_of_rh.tex:1693-1754` (`Whitened mixed-block transfer with preserved Q^{-3} scale`)
- `paper/proof_of_rh.tex:2050-2210` (`Sharpened calibration remainder estimate`)
- `paper/proof_of_rh.tex:2223-2321` (`Boundary estimate`, `Odd microscopic expansion`)

**Dependencies**

- The notes' interpretation of the paired slot theorem interface.
- The manuscript's corrected local deformation / whitening framework as the model for what counts as exact slot meaning.
- A future paired-family construction matching the manuscript interface.

**Strongest objection**

The weakest point is whether `microscopic holomorphy + positive same-point blocks + inverse-square-root whitening` can really be treated as a purely minimal admissibility fragment in the paired family, rather than as the first part of the quantitative transport theorem. In the manuscript those properties are ultimately *proved* through denominator comparability and perturbative control, so the paired theorem may still need a family-level analytic package larger than the notes' high-level split suggests.

**Needed for promotion**

- State a paired theorem in exact manuscript-interface form, explicitly defining `q_\chi^{\pair}`, `B_\chi^{\pair}`, `S_\chi^{\pair}`, the corrected paired local deformation, and `A_{\val,\chi}^{\pair}`.
- Prove that the paired exact coefficient identity uses only the admissibility fragment above and does not yet require denominator comparability or preserved-scale transfer estimates.
- Separately state the paired quantitative corrected-whitening transport theorem with denominator comparability, omitted-smooth holomorphy, preserved transfer scale, and the remainder/boundary consequences.
- Honest verdict: the boundary is conceptually clean, but only conditional until the paired family is shown to realize the manuscript interface with that exact split.
