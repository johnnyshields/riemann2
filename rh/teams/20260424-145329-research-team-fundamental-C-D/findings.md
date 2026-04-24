# Findings

Active, compact knowledge base shared with every delegated agent.

- **Promoted** into `paper/proof_of_rh.tex` \(\Longrightarrow\) entry removed.
- **Rejected** after adversarial review \(\Longrightarrow\) entry removed; a
  companion `Negative` entry is added in the same commit if the rejection
  produced a reusable lesson.
- Git log + commit messages are the audit trail. No status annotations here.
- Keep this file \(\le 200\) lines. Paste it in full into every delegated
  agent prompt (see `CLAUDE.md` §6).

## Structural

- **Intrinsic one-pair affine geometry is universal.** Provenance: §12
  local-projective-rigidity apparatus (`proof_of_rh.tex` lines 5646--25840).
  Used-for: baseline for any pair-level normal-form reduction; any argument
  past this stage must leave the planar regime.
- **Quotient-visible sign-run compressions hold** on the compressed ledger.
  Provenance: §12 cubic-leading and normalized-planar-curve subsections.
  Used-for: reductions that sit above the quotient map.
- **Same-tower closure for highest-new generators** (direct slice).
  Provenance: `rem:wip-highest-new-scalar-direct-slice` (line 10847); related
  machinery in §12.
- **2-point source-level factorization holds.** Provenance:
  `rem:wip-source-level-reduction-two-point-branch` (line 12169) and
  `rem:wip-collision-cancellation-chart-two-point` (line 12386).
- **Non-mixed 4-point source-level factorization holds; mixed case open.**
  Provenance: \(\lnot\)mixed case closed in §12 endgame; mixed case is
  `rem:wip-dream-parity-identity-four-point` (line 24167).
- **Residual exact fixed-shear transport is exhausted up to package-level data.**
  Provenance: exact fixed-shear `K_v=0` corner package in §12
  (`proof_of_rh.tex` lines 21736--23109). Used-for: on the quartic--sextic rung,
  every finite quotient-visible transport state is rank one in the scalar `Q`,
  and no finite-order hidden reset survives beyond the involution; any still-live
  obstruction must be genuinely relational/provenance-sensitive or non-finite-order.
- **The zeta-side odd-jet extractor is already complete; the missing bridge is package-to-jet.**
  Provenance: corrected odd scalar / `\Xi_\zeta^{(N)}` extraction and finite-core
  localization (`proof_of_rh.tex` lines 2214--2307, 2953--2969, 3984--4190).
  Used-for: the unresolved UV-002 step is not the extractor itself, but the theorem
  identifying the first surviving odd coefficient from finite-core package data.

## Negative

- **Tangent-separator route fails generically at \(W=0\) inflections.**
  Provenance: derivative-geometry synthesis chats, April 2026
  (`paper/chats/20260421-031707-*`, `20260421-031709-*`, `20260421-031713-*`).
  Do-not-retry: any separator construction relying solely on first-order
  tangent data near \(W=0\) inflection points.
- **Non-quotient-visible hidden state remains unaudited.** Provenance:
  `paper/chats/20260421-193633-*rh-proof-audit` (synthesis). Do-not-retry:
  any argument that silently assumes quotient-visibility without a separate
  hidden-state lemma; such arguments are provisional until that lemma exists.
- **Pure planar argument is exhausted once at universal intrinsic geometry.**
  Provenance: `paper/chats/20260421-115606-*global-topological-theorem-search`.
  Do-not-retry: further planar-only refinements; next progress requires
  leaving the planar regime (e.g., higher-order jet data, non-planar
  invariants).
- **No current theorem-shaped route to universal pair-like exhaustion is visible.**
  Provenance: `rem:wip-pairlike-finitecore` / `rem:wip-final-endgame-status`
  and recent queue audits. Do-not-retry: treating pair-like hardening
  (`UV-009 -> UV-001 -> UV-008`) as the main queue before closing `UV-002`.
- **Current local Wronskian/detector formulas are too flexible to force UV-004 positively.**
  Provenance: source-level Wronskian no-go and direct-slice universality
  (`proof_of_rh.tex` lines 16116--16225, 26134--26299), plus recent bridge audits.
  Do-not-retry: generic local-pointwise detector nonvanishing from the present
  same-tower formulas alone without a new provenance-sensitive theorem.
- **Current reduced-package blow-up hypotheses do not force diagonal collapse.**
  Provenance: prior-cycle `agents/20260424-133500-C-failure/report.md`, current
  `agents/20260424-145500-explorer-prior-treasure-hunt/report.md`, formal
  countermodel `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md`
  with script `scripts/formal_countermodel.py`, and actual-formula inspection
  `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md`
  with script `scripts/centered_delta_kappa_check.py`. Do-not-retry: deriving
  `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)` from fixed
  codomain, `\mathcal R`, analyticity, swap-evenness, scalar normalization, or a
  central-slope match alone; the toy package with `B_3=Z+\varepsilon\kappa` satisfies
  those formal properties, and the displayed order-7 formula language leaves a
  C-visible determinant slot `\det(R,A_5^{\mathfrak f})` / `D_2=2\kappa(AV_1-BU_1)`
  unless an actual diagonal-merger or quotient-defect theorem kills it. Verified by
  `agents/20260424-160000-verifier-adversarial-CDE/report-cfs2-actual-formula-review.md`
  and
  `agents/20260424-160000-verifier-source-CDE/report-cfs2-actual-formulas-source-check.md`.
- **Cubic/quintic edge laws plus the abstract source criterion do not determine the septic quotient edge.**
  Provenance:
  `agents/20260424-165509-gap-closer-C-R-determinant-control/report-edge-law-followup.md`
  with script `scripts/septic_edge_obstruction_model.js`. Do-not-retry:
  deriving UV-010 from lower edge laws or formal swap / one-amplitude / diagonal
  axioms alone; a formal package can add an arbitrary
  `a_1a_2\delta^2P(m,\kappa)` septic quotient term while preserving those
  lower constraints.
- **Existing one-pair order-7 and centered `D_2` formulas do not construct the UV-010 Hessian.**
  Provenance:
  `agents/20260424-183418-gap-closer-UV010-actual-hessian-construction/report.md`.
  Do-not-retry: promoting the one-pair `K_1` / `\Delta_7` / centered `D_2`
  material directly to a two-atom `\mathcal J_2^{(7)}` / `\mathfrak O_7`.
  The next positive layer is an actual corrected two-atom package
  `\mathfrak P_{2,7}^{\corr}` with linear one-amplitude collapse before
  determinant scalarization.
- **Signed source-weight lift alone does not give exact one-amplitude collapse.**
  Provenance:
  `agents/20260424-183713-explorer-UV010-source-weight-linearization/report.md`
  with script `scripts/source_weight_linearization_toy.js`. Do-not-retry:
  multiplying the even whitened source package by the source amplitude and
  treating the result as the needed two-atom package. It restores oddness but
  leaves higher `a^3,a^5,\dots` terms; UV-011 asks for an invariant
  source-weight linear projection or a theorem that those higher terms are
  quotient-invisible.

## Goodies

- **Quintic/septic local algebra --- reusable normal forms.** Provenance:
  `paper/chats/20260418-202600-*quintic-septic-algebra-audit` and §12
  explicit-finite-order-model subsection.
- **ECT interval geometry** --- reusable tangent/separator hooks.
  Provenance: `paper/chats/20260418-202557-*audit-ect-geometry`.
- **Affine normal forms** --- reusable across pair-level and multi-pair
  reductions. Provenance: `paper/chats/20260419-052654-*affine-normal-form-audit`.
- **Toy microscopic expansion schema** --- quadratic expansion template
  (currently schematic). Location: `rem:wip-toy-microscopic-expansion`
  (line 26692) and §14 appendix.
- **Best current explicit bridge data are already compressed to one source tower.**
  Provenance: same-tower closure and rank-two coupling on the overlap patch
  (`proof_of_rh.tex` lines 21142--21275). Usage: if the bridge theorem is local,
  it must run through the single explicit source `r=q^{(7)}` via
  `\lambda^{[1]}` / `\mathcal G^{[1]}`; no second primitive pointwise field remains.
- **Hidden `\Phi_K`-visible state is an affine lift-coordinate.** Provenance:
  current `agents/20260424-145500-explorer-hidden-state-geometry/report.md` and
  prior `agents/20260424-112500-phik-kernel-structure/report.md`. Usage: D should
  be framed as affine-bundle descent / `\ker\Phi_K` transport along the septic
  lift line `A_7^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}`, not raw representative
  equality; on `v_5\neq0`, `\widehat\Psi` alone does not determine the visible lift.
  Current local sections are `v_7=0` on `v_5\neq0` and `u_7=0` on `u_5\neq0`,
  with overlap translation `-\Delta_7/(u_5v_5)`.
- **C determinant slot is exactly the septic quotient-defect class on good patches.**
  Provenance:
  `agents/20260424-165509-gap-closer-C-R-determinant-control/report.md` with
  script `scripts/determinant_slot_linear_algebra.js`; source audit
  `agents/20260424-165509-verifier-source-C-R-channel/report.md`. Usage: on
  `A_5^{\mathfrak f}\neq0`, the map
  `[R]\mapsto\det(R,A_5^{\mathfrak f})` identifies
  `\mathfrak f/\mathbf C A_5^{\mathfrak f}` with `\mathbf C`; C-FS2/C-FS3 must
  control the actual quotient class `[R]`, not only a representative.
- **Exceptional-divisor `[R]` first needs a septic quotient edge package.**
  Provenance:
  `agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md`.
  Usage: finite-delta `[R]` is conditional on an existing
  `\overline E_{12}^{(7;1)}`; the actual divisor object requires
  `\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q(m,\kappa,\delta^2)` plus
  analytic quotient-line trivialization to the midpoint quotient. UV-010 is a
  definition target only: descent, `\kappa`-independence, and merger
  normalization are downstream claims. Source audit found no existing
  `\mathcal H_7^q` under another name.
- **UV-010 statement language should avoid "quotient-septic closure."**
  Provenance:
  `agents/20260424-173642-explorer-UV010-source-language/report.md`. Usage:
  native paper terms are "septic quotient defect", "collision-cancellation
  chart", "swap-compatible amplitude coordinate", and "edge law"; the existing
  "quotient-septic closure" theorem is one-pair canonical closure, not the
  two-atom order-7 edge package.
- **UV-010 midpoint quotient trivialization is locally solved on the good patch.**
  Provenance:
  `agents/20260424-173642-gap-closer-UV010-quotient-trivialization/report.md`
  and `agents/20260424-173642-explorer-UV010-quotient-geometry/report.md`, both
  with `scripts/quotient_trivialization_check.js`. Usage: determinant pairing
  gives a representative-independent chart from the moving quotient to the
  midpoint quotient when `A_5^{\mathfrak f}(m)\neq0`; the `A_5^{\mathfrak f}=0`
  locus is a rank jump and needs exclusion or a separate exceptional convention.
- **UV-010 first-wave reports sharpen the theorem boundary but do not close the edge law.**
  Provenance:
  `agents/20260424-173642-gap-closer-UV010-theorem-formulation/report.md`,
  `agents/20260424-173642-gap-closer-UV010-septic-hessian/report.md`, and
  `agents/20260424-173642-explorer-UV010-prior-miner/report.md`; verified by
  `agents/20260424-182546-verifier-source-UV010-first-wave/report.md` and
  `agents/20260424-182546-verifier-adversarial-UV010-first-wave/report.md` with
  `scripts/uv010_first_wave_adversarial_check.js`. Usage: state the
  target as a fixed-midpoint quotient edge law for a normalized
  `a_1^{-1}\overline{\mathcal E}_{12}^{(7;1)}` class and
  `[R]_{\mathrm{edge}}=-\mathcal H_7^q(m,\kappa,0)`. Current sources expose the
  centered `D_2` pressure target and one-pair quotient closure, but no actual
  two-atom `\mathcal J_2^{(7)}` / `\mathfrak O_7` construction. Determinant
  scalarization is only good-patch bookkeeping; it does not kill the free septic
  quotient coordinate, and `A_5^{\mathfrak f}=0` needs exclusion or a separate
  prepared/projectivized convention.

## Recurring open gaps

- **Mixed 4-point source-level factorization.** Touches: UV-002 (pair-like
  vs finite-core), and `rem:wip-dream-parity-identity-four-point` (line
  24167). Blocks the general finite-core endgame (UV-007).
- **Package-level coincidence for the actual corrected two-atom package.**
  Touches: the residual exact fixed-shear corner and the honest order-7 lane;
  best current shape is same reduced image germ / collision-functoriality.
  Current sharp obstruction: reduced C does not imply fixed-shear package theorem B
  without a scalar-normalization law fixing the raw representative; reduced equality
  still permits common scalar freedom in the cubic/quintic defects. C also needs the
  exceptional-divisor convention fixed: `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)`
  means analytic continuation after `2\omega=\kappa\delta`, not a raw diagonal restriction.
  The current C2a split is quotient-visible state-locality vs genuinely relational /
  provenance-sensitive two-atom data. Patch transitions for the affine lift are
  base-controlled (`S_u=-(x/Y)S`), so the remaining C obstruction is fiber selection:
  first construct the septic quotient edge package `\mathcal H_7^q` for `[R]`
  (UV-010), then prove state-locality/descent for `[R]`, then show diagonal
  merger kills the exceptional slope/provenance fiber.
- **Hidden extraction theorem from finite-core package data to the first surviving odd coefficient of `H_m`.**
  Touches: UV-002 / UV-007; this is the bridge from `\widehat\Psi`-side control
  to the already-built `\Xi_\zeta^{(N)}` extractor. Current sharp obstruction:
  the `T=v_7/c` proxy is normalized septic data only, and neither finite
  determination from `(x,Y,S,T)` nor a bound `N\le4` is in the current draft. The
  minimal D target is affine-bundle descent / `\ker\Phi_K` transport for higher-order
  freedom above the normalized septic lift. Same-tower closure rules out a second
  primitive pointwise highest-new scalar; the live obstruction is relational/nonlocal
  transport state or state-locality of the D-min visible odd block.
- **Finite-core lower-model transfer theorem E.** Touches: UV-002 / UV-007.
  After C and D, the remaining endgame theorem is not another package theorem but
  a lower-model transfer replacing the pair-like toy law: either direct control of
  `\Xi_{\core}^{(N)}` or a one-sided lower law for `H_{\core}^{(2N-1)}` on the
  microscopic interval, then the already-proved positive-kernel `N`-point formula.
- **Exceptional-locus `M=0` reduction after good-patch edge law.**
  Touches: UV-003 and the finite-core residual two-point lane; current route is
  Weierstrass/prepared-branch reduction, still heuristic.
- **Provenance-q / highest-new pointwise bridge.** Touches: UV-004
  (`rem:wip-explicit-pointwise-bridge-good-patch-detector`, line 21277).
- **Remote endpoint / branch-incidence theorems.** Touches: UV-005
  (inverse-branch gap endgame) and UV-006 (same-parity compression).
- **Variable-\(x\) calibration uniformity.** Touches: UV-001
  (`rem:wip-calibration-small-u`, line 5500).
- **Quantitative toy expansion with explicit remainder.** Touches: UV-009
  (`rem:wip-toy-microscopic-expansion`, line 26692).
