# Findings

Active, compact knowledge base shared with every delegated agent.

- **Promoted** into `paper/proof_of_rh.tex` \(\Longrightarrow\) entry removed.
- **Rejected** after adversarial review \(\Longrightarrow\) entry removed; a
  companion `Negative` entry is added in the same commit if the rejection
  produced a reusable lesson.
- Git log + commit messages are the audit trail. No status annotations here.
- Keep this file \(\le 200\) lines. Paste it in full into every delegated
  agent prompt (see `AGENTS.md` `Briefing rule`).

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
- **Reduced-package blow-up hypotheses do not force diagonal collapse.**
  Provenance: prior/current C reports plus CFS2/CFS23 scripts and source/adversarial
  reviews under `agents/20260424-160000-*`. Do-not-retry: deriving
  `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)` from fixed
  codomain, `\mathcal R`, analyticity, swap-evenness, scalar normalization, or
  central-slope alone; formal/actual checks leave a C-visible determinant slot
  until an actual diagonal-merger or quotient-defect theorem kills it.
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
  leaves higher `a^3,a^5,\dots` terms; UV-022 asks for an invariant
  source-weight linear projection or a theorem that those higher terms are
  quotient-invisible.

## Goodies

- **Archived reusable background:** quintic/septic normal forms, ECT interval geometry, affine normal forms, and the toy microscopic expansion remain in the April chat audits and `rem:wip-toy-microscopic-expansion`.
- **Best explicit bridge data are compressed to one source tower.** Provenance: same-tower closure and rank-two coupling (`proof_of_rh.tex` lines 21142--21275). Usage: a local bridge must run through `r=q^{(7)}` via `\lambda^{[1]}` / `\mathcal G^{[1]}`; no second primitive pointwise field remains.
- **Hidden `\Phi_K`-visible state is an affine lift-coordinate.** Provenance: `agents/20260424-145500-explorer-hidden-state-geometry/report.md` and `agents/20260424-112500-phik-kernel-structure/report.md`. Usage: frame D as affine-bundle descent / `\ker\Phi_K` transport along `A_7^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}`.
- **C determinant slot is the septic quotient-defect class on good patches.** Provenance: `agents/20260424-165509-gap-closer-C-R-determinant-control/report.md` and `agents/20260424-165509-verifier-source-C-R-channel/report.md`. Usage: on `A_5^{\mathfrak f}\neq0`, `[R]\mapsto\det(R,A_5^{\mathfrak f})` charts the quotient with `\mathbf C`; control the quotient class, not a representative.
- **Exceptional-divisor `[R]` first needs a septic quotient edge package.** Provenance: `agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md`. Usage: finite-delta `[R]` needs `\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q` plus midpoint quotient trivialization; descent, `\kappa`-independence, and merger are downstream.
- **UV-010 statement language:** use "septic quotient defect", "collision-cancellation chart", "swap-compatible amplitude coordinate", "edge law", and midpoint quotient after analytic trivialization. Provenance: `agents/20260424-173642-explorer-UV010-source-language/report.md`.
- **UV-010 midpoint quotient trivialization is locally solved on the good patch.** Provenance: `agents/20260424-173642-gap-closer-UV010-quotient-trivialization/report.md` and `agents/20260424-173642-explorer-UV010-quotient-geometry/report.md`. The `A_5^{\mathfrak f}=0` locus remains a rank jump needing exclusion or a separate convention.
- **UV-010 first-wave boundary:** state the target as a normalized fixed-midpoint quotient edge law with `[R]_{\mathrm{edge}}=-\mathcal H_7^q(m,\kappa,0)`. Current sources expose centered `D_2` and one-pair quotient closure, but no actual two-atom `\mathcal J_2^{(7)}` / `\mathfrak O_7`; determinant scalarization is good-patch bookkeeping.
- **UV-022 whitening-side candidate is the first homogeneous transfer `\mathcal T_1`.** Provenance: `agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`. Missing input: source-weight-linear actual two-atom block perturbation `X^{[1]}` and proof that its order-7 quotient output is the UV-010 edge package.
- **UV-023/UV-026 source-bidegree quotient package is missing from current source.** Provenance: UV-023/UV-026 reports in `agents/20260424-190438-*` through `agents/20260425-002114-*`. Usage: `(1,1)` projection, tagged `L_h`, and `[B_7^{\mathfrak f}(C)]\in\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)` are the right package layer; the guarded source block is canonical.
- **UV-026 coefficient frontier:** seven cubic families and a verified Stage 1 generator exist, but promotion still needs ordinary-`z` tagged tables, explicit `\mathfrak D_Q`, removable mixed-block expansions, baseline `q_0^{(0..9)}(m)` jets, scalar `Gr_1/Gr_5`, grade-0 handling, and determinant gates. Ungraded `f_{\beta,\gamma}` source jets are available; `q^{(5)}/X_3` is rejected for `M^{[5]}` if grade means finite mixed order.
- **UV-026 mixed-input parity:** `M(-z)=M(z)^T`; diagonal entries are even, and `[z^5]M` lives only in the off-diagonal antisymmetric channel from even source derivatives `r^{(2)},r^{(4)},r^{(6)}`. Provenance: `agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md` through `agents/20260425-005100-*`. Under the clean homogeneous scalar grade `Gr_a r=r^{(a+2)}`, `L_1YR_1` is verified absent at `B_7`, and `L_2YR_0`/`L_0YR_2` are order-absent pending verifier; nonzero alternatives require a separate matrix-order or no-double-counting theorem.

## Recurring open gaps

- **Mixed 4-point source-level factorization.** Touches UV-002 and `rem:wip-dream-parity-identity-four-point` (line 24167); blocks the general finite-core endgame.
- **Actual corrected two-atom package coincidence.** Construct `\mathcal H_7^q` / `[R]` (UV-010), prove state-locality/descent, then prove diagonal merger kills slope/provenance data.
- **Hidden extraction theorem.** Convert finite-core package data to the first surviving odd coefficient of `H_m`; `T=v_7/c` and finite determination from `(x,Y,S,T)` are not yet enough.
- **Finite-core lower-model transfer theorem E.** Control `\Xi_{\core}^{(N)}` or a one-sided lower law for `H_{\core}^{(2N-1)}`, then use the positive-kernel `N`-point formula.
- **Exceptional-locus `M=0` reduction.** After good-patch edge law, use Weierstrass/prepared-branch reduction or a separate exceptional convention.
- **Provenance-q / highest-new pointwise bridge.** Touches UV-004 (`rem:wip-explicit-pointwise-bridge-good-patch-detector`, line 21277).
- **Remote endpoint / branch-incidence theorems.** Touches UV-005 and UV-006.
- **Variable-\(x\) calibration uniformity.** Touches UV-001 (`rem:wip-calibration-small-u`, line 5500).
- **Quantitative toy expansion with explicit remainder.** Touches UV-009 (`rem:wip-toy-microscopic-expansion`, line 26692).
