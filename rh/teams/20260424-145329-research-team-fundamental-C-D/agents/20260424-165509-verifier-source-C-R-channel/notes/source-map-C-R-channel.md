# Source map: C R-determinant channel

Role: verifier-source-C-R-channel.

Owned path:
`rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-source-C-R-channel/`.

## Read state

- `CLAUDE.md`
- `.agents/agents/_autoresearch.md`
- Current `findings.md` in full.
- `uv.md` entries `UV-002`, `UV-003`, `UV-004` only.
- `dispatch.md` at `Resume dispatch 20260424-165509`.
- `collation.md` from `Verified frontier after six-report review` onward.
- Prior source reports:
  - `agents/20260424-160000-verifier-source-CDE/report-cfs23-countermodel-source-check.md`
  - `agents/20260424-160000-verifier-source-CDE/report-cfs2-actual-formulas-source-check.md`
- Paper slices:
  - `rh/proof_of_rh.tex:6976-7003`, `7004-7191`, `7540-7974`,
    `11368-11450`, `11587-11775`, `11888-12189`, `12192-12255`,
    `12385-12584`, `22470-22530`, `23070-23108`, `23120-23160`,
    `23294-23409`.
- Sibling resume deposits were checked for fresh target state. At read time,
  `20260424-165509-verifier-adversarial-C-R-channel/report.md` existed and
  `20260424-165509-gap-closer-C-R-determinant-control/` contained only
  `scripts/determinant_slot_linear_algebra.py`, with no report yet.

## Proved / source-supported

- Fixed-sector basis is `\mathfrak f=\operatorname{span}\{I,S\}` and
  `\mathfrak a=\operatorname{span}\{D,J\}` with explicit matrices at
  `rh/proof_of_rh.tex:6976-7002`.
- One-pair package:
  `A_5^{\mathfrak f}=u_5I+v_5S`,
  `A_7^{\mathfrak f}=u_7I+v_7S`,
  `\Delta_7=u_7v_5-u_5v_7`; raw septic representative is noncanonical modulo
  `\mathbf C A_5^{\mathfrak f}`. Refs:
  `rh/proof_of_rh.tex:7004-7062`, `7065-7191`.
- Quotient-septic closure and direct \(q^{(7)}\) slice are paper-supported for
  the one-pair canonical quotient-level data. Refs:
  `rh/proof_of_rh.tex:7540-7974`, with the status warning at
  `rh/proof_of_rh.tex:10780-10810`.
- `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` and scalar-rescaling invariance are
  proved for one-pair data. Refs: `rh/proof_of_rh.tex:11368-11450`.
- The defect-thickened theorem exposes a C-visible scalar slot
  `\det(R,A_{5,1}^{\mathfrak f})`, where `R` is any representative of
  `-a_1^{-1}\overline E_{12}^{(7;1)}`. The proof proves independence from raw
  representative changes `R -> R+\xi A_{5,1}^{\mathfrak f}` only. Refs:
  `rh/proof_of_rh.tex:11587-11775`, especially `11625-11669`,
  `11705-11745`, `11768-11774`.
- Collision-cancellation variables
  `m=(h_1+h_2)/2`, `\delta=h_2-h_1`, `\omega=(\lambda-1)/(\lambda+1)`, and
  `\kappa=2\omega/\delta` are paper-supported as a WIP reduction. Refs:
  `rh/proof_of_rh.tex:12385-12511`.
- The centered Taylor package displays
  `\widehat U_1=2\kappa A`, `\widehat V_1=2\kappa B`, and
  `D_2=\widehat U_1V_1-U_1\widehat V_1`, hence
  `D_2=2\kappa(AV_1-BU_1)` in bracket shorthand. Refs:
  `rh/proof_of_rh.tex:23294-23409`.

## Conditional

- The minimal finite-order source criterion proves quadratic two-point
  factorization if an analytic two-atom package `\mathfrak P_2` satisfies swap
  symmetry, one-amplitude collapse, and diagonal merger. It does not construct
  the actual corrected package. Refs: `rh/proof_of_rh.tex:11888-12189`.
- The conditional quadratic defect estimate assumes an actual corrected
  finite-order package through order 7 in
  `\mathbf C\oplus\mathfrak f\oplus(\mathfrak f/\mathbf C A_5^{\mathfrak f})`.
  Refs: `rh/proof_of_rh.tex:11994-12040`.
- The weaker quotient-diagonal exclusion assumes an actual corrected two-atom
  quotient map plus continuity, diagonal collapse, and precompactness. Refs:
  `rh/proof_of_rh.tex:12042-12166`.
- The involutive-branch package collapse assumes state-locality and the natural
  merger law. Refs: `rh/proof_of_rh.tex:22472-22505`.
- The residual exact fixed-shear reduction assumes swap invariance and
  coincident-atom vanishing for the actual corrected cubic and quintic defects.
  Refs: `rh/proof_of_rh.tex:23072-23108`.

## Missing / not source-supported

- Exact-string search found no paper definition of the actual corrected
  fixed-codomain triple
  `\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`.
  The paper has generic or conditional `\mathfrak P_2` criteria, not this
  constructed corrected object.
- The corrected reduced-package fiber is not defined as a paper object. The
  current phrase remains cycle shorthand unless tied to an explicit equivalence
  relation or to `\mathcal R\circ\mathfrak P_2^{\corr}` on the exceptional
  divisor.
- The representative independence at `rh/proof_of_rh.tex:11768-11774` does not
  prove determinant independence from the quotient-defect class, slope, or
  provenance. It only kills raw additions parallel to `A_5^{\mathfrak f}`.
- The paper does not compute `R` on the exceptional divisor for the actual
  corrected two-atom package.
- No identity in the checked centered package forces `AV_1-BU_1=0`.
- Same reduced image germ and collision-functoriality are named as theorem
  targets, not proved closure theorems. Refs: `rh/proof_of_rh.tex:10780-10810`,
  `12513-12584`.

## Drift flags

- Basis drift: the fixed-sector source uses `(I,S,D,J)` with
  `J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}` at `6976-7002`; later scalar
  extraction uses `(I,D,S,K)` with
  `K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}` at `23123-23155`, so `K=-J`.
  Future C/D text must announce the switch.
- `\kappa` is overloaded. In the collision chart it is the blow-up slope
  `2\omega/\delta` (`12463`). In one-pair K1 formulas it appears as a local
  coefficient `\kappa(h)` (`7563`, `7617`). In the centered package it appears
  as the coefficient multiplying `\widehat U_1`, `\widehat V_1` (`23345-23365`).
  These should not be silently identified.
- `R` is overloaded: `R\in\mathfrak f` at `11625-11638` is a quotient-defect
  representative, while `R(z)` at `23127` is a raw one-pair corrected germ.
- `D_2` in `23294-23409` is a scalar Taylor coefficient, not the matrix `D` in
  the fixed-sector basis.

## Audit verdict

The source map supports the same scoped negative as the prior reports and the
fresh adversarial deposit: the current draft proves one-pair quotient/determinant
invariance and exposes a representative-independent scalar slot
`\det(R,A_5^{\mathfrak f})`, but it does not construct the actual corrected
two-atom fixed triple, define corrected reduced-package fibers, compute/control
`R` on the exceptional divisor, or prove a diagonal-merger/collision-functoriality
theorem that kills independent slope/provenance dependence.
