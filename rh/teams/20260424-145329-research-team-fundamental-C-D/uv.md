# UV Ledger

Working forward-carry of the current open UV items relevant to the active queue.

## Active

- **UV-001** — `rem:wip-calibration-small-u`
  Claim: variable-`x` calibration forces the toy parameter into the microscopic regime uniformly.
  Current role: paused downstream pair-like quantitative cleanup.

- **UV-002** — `rem:wip-pairlike-finitecore`
  Claim: either all relevant cores reduce to the pair-like branch, or the general finite-core branch closes via the first nonzero odd jet.
  Current role: top queue item.

- **UV-003** — `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: actual corrected edge-law / local good-patch package on the collision-cancellation chart.
  Current role: support theorem for UV-002.

- **UV-010** — `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: construct the actual corrected order-7 quotient-defect edge package
  `\mathcal H_7^q` for `\overline E_{12}^{(7;1)}` with quotient-line
  trivialization to the midpoint quotient, without assuming diagonal merger.
  Current role: immediate C-FS2/C-FS3 definition target under UV-003; descent
  and merger normalization are downstream, not part of this definition target.

- **UV-022** — `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: define an invariant source-weight-linear input for corrected blocks
  through order 7 and an analytic corrected-whitening cross-effect package with
  exact one-amplitude collapse, then prove its order-7 quotient component is
  collision-vanishing in the UV-010 chart.
  Current role: package-definition subtarget for UV-010; needed before the
  actual two-atom `\mathcal J_2^{(7)}` / `\mathfrak O_7` construction can be
  promoted.

- **UV-023** — `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: prove that the order-7 quotient component of the corrected-whitening
  cross-effect has zero first collision derivative after source-weight
  linearization, either because only the quadratic homogeneous transfer
  `\mathcal T_2` contributes or because all `\mathcal T_{p\ge3}` terms are
  quotient-invisible through order 7.
  Current role: sharp subtarget of UV-022; required before the cross-effect
  package can yield the `\delta^2\mathcal H_7^q` edge law for UV-010.

- **UV-024** -- `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: define the pre-determinant fixed-sector order-7 coefficient
  `B_7^{\mathfrak f}(C)` for the actual source-linear corrected-whitening
  cross-effect before `\Phi_K` / determinant scalarization, define
  `Q_{7,m}^q(C)=[B_7^{\mathfrak f}(C)]` in
  `\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)`, and prove
  `B_7^{\mathfrak f}((1-\Pi_{1,1})C)\in
  \mathbf C A_5^{\mathfrak f}(m)`, equivalently
  `Q_7^q((1-\Pi_{1,1})C)=0`.
  Current role: coefficient-map subtarget of UV-023; needed before the
  quotient-invisibility theorem can be promoted.

- **UV-026** -- `rem:wip-parity-projective-factorization-collision-blow-up`
  Claim: for the actual source-linear corrected-whitening matrix cross-effect,
  every non-`(1,1)` cubic finite-order source term `T` of type `(1,1,5)`
  satisfies `B_7^{\mathfrak f}(T)\in\mathbf C A_5^{\mathfrak f}(m)`.
  Current role: narrowed cubic gauge subtarget for UV-024; needed before the
  full non-`(1,1)` quotient-invisibility theorem can be promoted.
  Shared table subtarget: prove a finite normalized source-table theorem in
  ordinary `z`, before `\Phi_K`, with source tags retained and
  `M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})`; the theorem
  must display order-`<=7` tables for `G_\pm^{(0)}`, `N_0`,
  `\delta G_{i,\pm}^{\lin,[1/5]}`, and `M_i^{[1/5]}`, then derive the
  first/second/third Frechet inverse-square-root tables from `S^2=G` and
  `BS=I`.  The source theorem must state the raw-vs-`\mathfrak D_Q` convention
  for same-point Frechet inputs and prove the mixed-block removable-singularity
  expansion before coefficient extraction.
  Immediate source-jet subtarget: define the actual finite-grade split
  `r_i=r_i^{[1]}+r_i^{[5]}+\cdots` in this normalization and supply the 42
  scalar midpoint derivatives consumed by the Stage 1 generator:
  `q_0^{(k)}(m)` for `0<=k<=9` and
  `(r_i^{[a]})^{(k)}(m)` for `i=1,2`, `a in {1,5}`, `2<=k<=9`.  Current source
  supports the ungraded one-pair formula `r_\rho^{(k)}(m)=f_{\beta,\gamma}^{(k)}(m)`
  for `k>=2`, but still lacks a scalar grade-projection theorem defining
  `Gr_1 r_i`, `Gr_5 r_i`, its compatibility with affine removal, and whether
  grade `5` means the `q^{(5)}/X_3`, `q^{(7)}/X_5`, or another mixed-block slice.
  Do not import `\eta_2/X_1`, `q^{(5)}/X_3`, or `q^{(7)}/X_5` matrix witnesses
  as scalar grades without that source theorem.  The `q^{(5)}/X_3` convention is
  rejected for `M_i^{[5]}` if grade means finite mixed order; the only
  source-compatible candidate then is `q^{(7)}/X_5`, still unpromoted.
  Baseline subtarget: prove a `q_0`-jet theorem giving exact
  `q_0^{(k)}(m)`, `0<=k<=9`, or reducing them to named baseline objects in the
  same ordinary-`z`, pre-`\Phi_K` normalization; scale estimates are not tables.
  Candidate projection subtarget: if finite grade means lowest pre-whitening
  ordinary-`z` matrix order, prove `Gr_a r = r^{(a+2)}(m)(t-m)^{a+2}/(a+2)!`
  for `a in {1,5}`, and separately handle/exclude the grade-0 `r^{(2)}(m)`
  sector by exclusion, gauge, source-class identification, or expanded
  determinant inventory.  The pure homogeneous candidate fails for `L_1YR_1`:
  exact mixed-block parity makes odd scalar pieces `r^{(3)}` and `r^{(7)}` first
  appear in mixed orders `2` and `6`, so `[z^5]M^{[5]}=0` for the `r^{(7)}`
  candidate.  The full source-linear mixed input has transpose parity
  `M(-z)=M(z)^T`; through order `7`, `[z^5]M` is off-diagonal antisymmetric and
  source-supported only by even derivatives `r^{(2)},r^{(4)},r^{(6)}`.  Hence
  `M_i^{[5]}` is a conditional placeholder until a theorem states whether `[5]`
  is a source-grade label whose mixed series may start away from `z^5`, an
  actual ordinary-`z` order-5 projection, or a parity-corrected non-homogeneous
  source projection.  The scalar-grade shortcut that moves
  `r^{(2)},r^{(4)},r^{(6)}` into grade `5` is rejected from current bookkeeping:
  those pieces naturally occupy grades `0,2,4` and have same-point shadows in
  those orders.  A surviving convention must either define `M_i^{[5]}` as a
  mixed matrix order-5 projection, or prove a no-double-counting
  parity-corrected source projection compatible with the seven-family inventory.
  Under the clean homogeneous scalar grade convention
  `Gr_a r=r^{(a+2)}(m)(t-m)^{a+2}/(a+2)!`, the `L_1YR_1` middle input is absent
  at `B_7`; the source/adversarial verifier confirms this as a scoped absence
  theorem, not a determinant identity.  Under the same convention,
  `L_2YR_0`/`L_0YR_2` are also verified absent: the allowed second-Frechet
  placements start at ordinary order `8`, and holomorphic Frechet coefficients
  cannot lower order.  If a future theorem instead defines `M^{[5]}` as
  matrix-output order `5`, reopen all `Y`-slot gates.  The active homogeneous
  cubic gates are now the non-`Y` families `L_2N_0R_1`/`L_1N_0R_2` and
  `L_3N_0R_0`/`L_0N_0R_3`.  For `L_2N_0R_1`/`L_1N_0R_2`, order counting does
  not close the gate: `N_0[0]` is available and the two homogeneous placements
  land exactly at order `7` (`2+0+5` and `6+0+1`).  The missing theorem is now
  only the leading-coefficient fixed-sector test using `[z^2]`/`[z^6]`
  second-Frechet outputs, `N_0[0]`, and `[z^1]`/`[z^5]` first-Frechet outputs,
  plus mirrors.
  Gate subtargets: compute determinant identities against
  `A_5^{\mathfrak f}(m)` for all seven classified cubic families:
  `L_1YR_1`; `L_3N_0R_0` and `L_0N_0R_3`; `L_2YR_0` and `L_0YR_2`;
  `L_2N_0R_1` and `L_1N_0R_2`.

- **UV-004** — `rem:wip-explicit-pointwise-bridge-good-patch-detector`
  Claim: the local detector either sees the same-tower source `r=q^{(7)}` or the explicit pointwise package is invisible.
  Current role: bridge/diagnostic theorem beneath the package theorem.

- **UV-005** — `rem:wip-inverse-branch-gap-endgame-fixed-shear`
  Claim: strict-overlap transport endgame on the three-run lane.
  Current role: paused unless needed as support.

- **UV-006** — `rem:wip-same-parity-compression-affine-lane`
  Claim: residual affine lane compresses to same-parity / middle-limited triples.
  Current role: support/diagnostic, not queue head.

- **UV-007** — `rem:wip-final-endgame-status`
  Claim: current endgame status theorem.
  Current role: depends on UV-002.

- **UV-008** — `rem:wip-high-height-only`
  Claim: effective high-height theorem plus low-height bridge to full RH.
  Current role: paused downstream pair-like/effective queue.

- **UV-009** — `rem:wip-toy-microscopic-expansion`
  Claim: quantitative toy microscopic expansion with explicit remainder.
  Current role: paused downstream pair-like/effective queue.
