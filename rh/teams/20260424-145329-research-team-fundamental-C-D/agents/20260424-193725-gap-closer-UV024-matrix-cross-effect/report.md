# Claim

There is a clean **conditional** matrix/fixed-sector cross-effect construction
before \(\Phi_K\):
\[
C_{\mathcal W}(a_1,h_1;a_2,h_2)
=
\mathcal W(B+a_1L_{h_1}+a_2L_{h_2})
-\mathcal W(B+a_1L_{h_1})
-\mathcal W(B+a_2L_{h_2})
+\mathcal W(B),
\]
where \(B=(G_-^{(0)},N^{(0)},G_+^{(0)})\) and \(L_h\) is the source-linear
pre-whitening corrected-block input. If this is the actual two-atom
corrected-whitening cross-effect, then
\[
B_7^{\mathfrak f}(C_{\mathcal W})
:=
\pi_{\mathfrak f}[z^7]C_{\mathcal W}
\]
is the right pre-determinant coefficient map, and
\[
Q_{7,m}^q(C_{\mathcal W})
:=
[B_7^{\mathfrak f}(C_{\mathcal W})]
\in \mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]

The current source does not prove this is the actual UV-024 object, because it
does not define the actual two-atom source-linear \(L_h/X^{[1]}\) before
whitening. It proves matrix analyticity of \(\mathcal W\) and scalar
\(\Phi_K\)-visible transfer, but not the source-defined matrix cross-effect
needed for \(B_7^{\mathfrak f}\).

The non-\((1,1)\) compatibility remains open. A cubic finite-order witness of
type \((1,1,5)\) can be fixed-sector quotient-visible unless a new theorem
proves its \(B_7^{\mathfrak f}\) contribution is
\(\mathbf C A_5^{\mathfrak f}(m)\)-gauge.

# Status

open

# Evidence

Three-bin separation:

- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1458`
  proves corrected finite-\(s\) matrix whitening is holomorphic before scalar
  extraction:
  \[
  \widehat\Omega_\zeta^{\corr}
  =
  G_-^{-1/2}NG_+^{-1/2}.
  \]
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575`
  defines the analytic matrix whitening map \(\mathcal W\), and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799` gives its first-order
  expansion around the baseline matrix triple.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2414`
  gives matrix-level scaling for corrected whitening and explicitly separates
  matrix factors from later scalar normalization.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587`
  defines the scaled corrected-whitening transfer after \(\Phi_K\), with a
  homogeneous expansion and coefficient bounds. This supports analytic
  transfer but does not itself define \(B_7^{\mathfrak f}\), because the
  proposition's output is scalar.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787`
  gives one-pair weighted corrected-block perturbations and shows entries are
  linear in pair kernels modulo terms with at least two such kernels. This
  supports the \(L_h\) candidate, but only at the one-pair bookkeeping level.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7062`
  defines \(\mathfrak f=\operatorname{span}\{I,S\}\), fixed-sector
  \(A_5^{\mathfrak f}\), \(A_7^{\mathfrak f}\), and the quotient target
  \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\).
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-8033`
  closes the one-pair quotient-septic class, but not the actual two-atom
  matrix cross-effect.
- **Conditional from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775`
  assumes the septic quotient defect is already written in a moving quotient
  before using a determinant slot.
- **Conditional from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189`
  gives quadratic factorization only after an actual package satisfies swap,
  one-amplitude collapse, and diagonal merger.
- **Proved source negative:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rules out the naive post-whitening source-summed model; whitened finite-order
  coefficients are even in source weight.
- **Proved source warning:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12230-12255`
  says quotient-only and single-determinant routes are shear-blind. Scalar
  invisibility cannot replace the \(A_5^{\mathfrak f}\)-gauge theorem.
- **Missing:** no inspected source line defines the actual two-atom
  source-linear corrected-block input \(L_h/X^{[1]}\) before whitening.
- **Missing:** no inspected source line defines \(C_{\mathcal W}\) as the
  actual matrix cross-effect of that two-atom package.
- **Missing:** no inspected source line proves
  \(B_7^{\mathfrak f}((1-\Pi_{1,1})C_{\mathcal W})
  \in \mathbf C A_5^{\mathfrak f}(m)\).

I wrote and ran the matrix cross-effect harness:

`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/scripts/matrix_cross_effect_model.py`

Script SHA1: `7b2e7d38ddf5bfbb87de00fd8f7ea69f115160a4`.

Relevant output:

```text
[conditional_matrix_cross_effect_definition]
matrix_cross_effect_before_PhiK = W(B+a1L1+a2L2)-W(B+a1L1)-W(B+a2L2)+W(B)
B7f = pi_f[z^7] matrix_cross_effect
definition_requires_actual_source_linear_Lh = true

[fixed_sector_terms]
A5_midpoint=(2, 5)
B7f_11=(7, 11)
B7f_non11_total=(17, 38)
B7f_non11_det_coordinate=9
B7f_non11_is_A5_gauge=False

[cubic_115_witness]
source_bidegree=(1,2)
finite_grades=(1,1,5)
total_grade=7
witness_B7f=(3, 7)
witness_det_coordinate=1
witness_is_A5_gauge=False

[PhiK_warning]
scalar_hidden_but_quotient_visible=True

[conclusion]
conditional_B7f_definition_is_valid_once_matrix_C_exists = true
current_source_proves_actual_matrix_C_exists = false
non11_source_bidegrees_A5_gauge_generically = false
cubic_115_witness_survives_quotient_generically = true
promotion_needs_source_theorem_not_scalar_check = true
```

Interpretation: once the matrix cross-effect exists, \(B_7^{\mathfrak f}\) is a
straight coefficient map. The compatibility theorem is not automatic. A
generic non-\((1,1)\) fixed-sector coefficient, including a cubic
\((1,1,5)\) witness, is not \(A_5^{\mathfrak f}\)-gauge.

# Baseline / delta

Baseline: UV-023/Q7q work isolated \(Q_{7,m}^q(C)=[B_7^{\mathfrak f}(C)]\) as
the right quotient target and left UV-024 to construct
\(B_7^{\mathfrak f}(C)\) before \(\Phi_K\). The \(L_h\) pass identified the
pre-whitening pair-kernel-linear derivative as the best source input
candidate, but not a current-source theorem.

Delta: this pass constructs the matrix cross-effect and coefficient map
conditionally from the analytic matrix whitening map. It also rejects the
promotion shortcut "scalar-hidden implies quotient-gauge": a term can be hidden
by a scalar functional and still have nonzero determinant against
\(A_5^{\mathfrak f}\). The remaining gap is now exact: identify the conditional
matrix cross-effect with the actual two-atom corrected package and prove the
non-\((1,1)\) fixed-sector order-7 coefficient is \(A_5^{\mathfrak f}\)-gauge.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-2048` - matrix whitening,
  analytic expansion, and first-order matrix transfer before \(\Phi_K\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - matrix scaling and
  scalar corrected-whitening transfer.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` - one-pair weighted
  corrected-block input and pair-kernel-linear bookkeeping.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7062` - fixed-sector target
  \(\mathfrak f\), \(A_5^{\mathfrak f}\), \(A_7^{\mathfrak f}\), and quotient
  class.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-8033` - one-pair
  quotient-septic closure and raw representative caveat.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` - finite-delta
  theorem assumes the moving quotient defect before determinant bookkeeping.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12255` - conditional source
  criterion, even-amplitude obstruction, and shear-blind determinant warning.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-gap-closer-UV023-Q7q-extractor/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-191517-verifier-adversarial-UV023-projection/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190928-gap-closer-UV023-bidegree-projection/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/notes/matrix-cross-effect-map.md`.
- Own script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/scripts/matrix_cross_effect_model.py`.

# Dependencies

- A source-defined actual two-atom corrected-block input \(L_h/X^{[1]}\) before
  whitening.
- Proof that the conditional matrix cross-effect \(C_{\mathcal W}\) is the
  actual corrected-whitening cross-effect of that two-atom package.
- A source-bidegree projector \(\Pi_{1,1}\) acting on \(C_{\mathcal W}\) before
  coefficient extraction.
- Constant-rank good patch \(A_5^{\mathfrak f}(m)\neq0\), or a separate
  exceptional convention.
- A theorem that every non-\((1,1)\) contribution to
  \(\pi_{\mathfrak f}[z^7]C_{\mathcal W}\) is proportional to
  \(A_5^{\mathfrak f}(m)\).

# Strongest objection

The conditional matrix cross-effect is formally standard and uses only the
paper's analytic matrix whitening map. The weak point is provenance: the source
does not define the actual two-atom source-linear block triple, and the scalar
transfer proposition applies \(\Phi_K\) before the coefficient extraction
needed here. Therefore this is a valid definition template, not a closure of
UV-024 from current source.

# Needed for promotion

1. Define the actual two-atom source-linear corrected-block input
   \(L_h/X^{[1]}\) before whitening.
2. Define \(C_{\mathcal W}\) from that input and prove it is the actual
   corrected-whitening cross-effect, not merely a formal Banach-space
   cross-effect.
3. Define
   \(B_7^{\mathfrak f}(C_{\mathcal W})=\pi_{\mathfrak f}[z^7]C_{\mathcal W}\)
   in the collision-chart variable used by UV-010.
4. Prove
   \(B_7^{\mathfrak f}((1-\Pi_{1,1})C_{\mathcal W})
   \in\mathbf C A_5^{\mathfrak f}(m)\).
5. Test the proof against cubic \((1,1,5)\) witnesses, and require gauge
   proportionality to \(A_5^{\mathfrak f}(m)\), not scalar invisibility under
   \(\Phi_K\).

# Autoresearch next step

continue: attack the provenance step. Write a source-level definition of the
actual two-atom corrected-block triple before whitening and show its
pair-kernel-linear part is the \(L_h\) input used in this conditional matrix
cross-effect.

verify: source verifier should check whether the matrix coefficient
\(\pi_{\mathfrak f}[z^7]\) uses the same \(z\)/collision variable as the
one-pair \(A_7^{\mathfrak f}\) package. Adversarial verifier should test any
claimed compatibility with a cubic \((1,1,5)\) fixed-sector vector and demand
\(A_5^{\mathfrak f}\)-gauge, not determinant or \(\Phi_K\) hiding.

blocked: no process blocker. Mathematical blocker is the missing actual
two-atom source-linear block definition and the missing non-\((1,1)\)
\(A_5^{\mathfrak f}\)-gauge theorem.

terminal: terminal for promoting UV-024 from scalar \(\Phi_K\)-transfer or
determinant scalarization alone. Not terminal for the conditional matrix
cross-effect route once the actual source-linear block is defined.

Honest verdict: UV-024 remains open. The matrix cross-effect and
\(B_7^{\mathfrak f}\) coefficient map are well-defined conditionally, but
current source does not yet supply the actual two-atom input or the
quotient-gauge theorem needed for promotion.
