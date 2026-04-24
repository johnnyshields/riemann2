# Claim

The paper supports a **candidate** pre-whitening source-linear input from the
one-pair corrected block formulas, but it does not define the actual two-atom
source object needed by UV-023.

The viable candidate is the pair-kernel-linear derivative
\[
L_h :=
\operatorname{Lin}_{U_\pm,E_\pm,G_\pm,V}
\mathfrak D_Q(\delta G_{h,-},\delta N_h,\delta G_{h,+}),
\]
taken before corrected whitening. Formally this would give
\[
X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2},
\]
which can feed `\mathcal T_1` and a source-bidegree projector `\Pi_{1,1}`.

From the tested source, this is not yet an actual theorem: the paper lacks an
actual two-atom corrected block definition before whitening and a theorem that
its pair-kernel-linear derivative is the required source functor.

# Status

open

# Evidence

Three-bin separation:

- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587`
  defines the corrected-whitening transfer on a pre-whitening perturbation triple
  `X=(X_-,Y,X_+)`, and proves the homogeneous expansion
  `\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2674`
  defines the one-pair weighted perturbation triple
  `X_{\rho,\pm}:=\mathfrak D_Q(\delta G_{\rho,\pm})`,
  `Y_\rho:=\mathfrak D_Q(\delta N_\rho)`, and states that every entry is linear
  in `U_-,U_+,E_-,E_+,G_-,G_+,V` modulo terms with at least two pair kernels.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`
  verifies the same-point corrected block: the `(1,1)` and off-diagonal entries
  are linear in `U_\pm,E_\pm`, while the `(2,2)` entry is linear in
  `G_\pm` and `U_\pm` modulo `U_\pm^2,U_\pm^3`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`
  verifies the mixed corrected block by Taylor expansion in
  `(d_-,d_+,\eta)`: the linear part is a bounded-baseline combination of
  `U_-`, `U_+`, and `V`, while the remainder has at least two pair kernels.
- **Proved source negative:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rules out the post-whitening signed source-weight lift: whitened coefficients
  are even analytic functions of the source weight, so multiplying by the source
  amplitude leaves higher `a^3,a^5,\dots` terms and does not give exact
  one-amplitude collapse.
- **Conditional from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189`
  gives the source criterion only after an actual package satisfies swap
  symmetry, exact one-amplitude collapse, and diagonal merger.
- **Conditional / target-only:** `C:/workspace/riemann2/rh/proof_of_rh.tex:10790-10810`,
  `12385-12584`, `21293-21330`, and `23072-23109` keep the relevant two-atom
  collision-functoriality, same-reduced-image, and package-level collapse as
  theorem targets rather than established inputs.
- **Missing:** no inspected source line defines the actual two-atom corrected
  block triple before whitening.
- **Missing:** no inspected source line defines `L_h` as a canonical
  pair-kernel-linear derivative functor on that actual two-atom object.
- **Missing:** no inspected source line proves that the resulting
  `X^{[1]}` satisfies the vanishing-at-`w=0` condition needed by
  `\mathcal T_{Q,R}` or that it is compatible with `Q_7^q`.

I wrote and ran:

`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/scripts/lh_source_input_check.py`

Script SHA1: `6e699454e6e4f902f3b487fb1f69ee39cdc619e5`.

Relevant output:

```text
[pre_whitening_pair_kernel_linear_part]
one_pair_model_kernel_degrees = [1, 2, 3]
linear_part_source_bidegrees = [(0, 1), (1, 0)]
linear_part_additive_in_sources = True
candidate_is_before_whitening = true

[feed_into_transfer]
T1_source_bidegrees = [(0, 1), (1, 0)]
cross_effect_source_bidegrees = [(1, 1), (1, 2), (2, 1)]
Pi_11_keeps = [(1, 1)]
linear_input_can_feed_T1 = true
two_atom_interaction_needs_transfer_cross_effect = true

[signed_lift_negative]
signed_lift_one_amplitude_error = 2808
linear_derivative_one_amplitude_error = 0
signed_lift_leaves_higher_a_terms = true

[source_status]
one_pair_pair_kernel_linear_derivative_supported = true
actual_two_atom_block_definition_found_in_tested_source = false
Lh_source_functor_requires_new_definition_or_source_line = true
```

Interpretation: the one-pair formulas support taking a pre-whitening
pair-kernel-linear part. That construction has the right formal behavior for
source tags and avoids the signed-lift failure. It still cannot be promoted
from current source because the actual two-atom corrected block and its
canonical linear derivative are not defined.

# Baseline / delta

Baseline: prior UV-023 passes reduced the problem to source-defined
`X^{[1]}`, `\Pi_{1,1}`, `Q_7^q`, and the compatibility theorem
`Q_7^q((1-\Pi_{1,1})C)=0`. The source-tags pass showed that `\Pi_{1,1}` is
formal once source tags exist, but `L_h` was still not source-defined.

Delta: this pass identifies the best available source input candidate:
`L_h` should be the pair-kernel-linear derivative of the weighted corrected
block perturbation triple before whitening. The paper supports this for the
one-pair formulas only. The exact remaining definition gap is now the actual
two-atom corrected block map and the theorem that its pair-kernel-linear
derivative is this `L_h`.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-023 entry.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587` -
  corrected-whitening transfer and homogeneous expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` - one-pair weighted
  corrected block perturbation, linear in pair kernels modulo higher kernel
  order.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:10790-10810` - order-7
  same-reduced-image / collision-functoriality remains target-only.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12255` - conditional source
  criterion, exact remaining source identities, even-amplitude obstruction, and
  shear-blind quotient/determinant warning.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12584` -
  collision-cancellation chart and downstream package programs.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:21293-21330` - remaining order-7
  burden is package-level and provenance-sensitive.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23072-23109` - residual fixed-shear
  corner remains package-level.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183713-explorer-UV010-source-weight-linearization/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190438-gap-closer-UV023-transfer-filtration/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190438-verifier-source-UV023-filtration/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190928-gap-closer-UV023-bidegree-projection/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-191517-gap-closer-UV023-source-tags/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-191517-verifier-adversarial-UV023-projection/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/notes/Lh-source-input-map.md`.
- Own script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/scripts/lh_source_input_check.py`.

# Dependencies

- Actual two-atom corrected block triple before whitening.
- A canonical pair-kernel-linear derivative operator
  `\operatorname{Lin}_{\mathcal K}` on that two-atom triple.
- A definition of `L_h` as a source functor, not as a post-whitening signed
  amplitude lift.
- A source-tagged input
  `X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2}` with swap-compatible tags.
- Proof that `X^{[1]}` lies in the transfer domain and satisfies the
  vanishing-at-`w=0` condition for `\mathcal T_{Q,R}`.
- Fixed-target `Q_7^q` and proof of
  `Q_7^q((1-\Pi_{1,1})C)=0`.

# Strongest objection

The candidate `L_h` is strongly suggested by the one-pair source formulas:
the paper explicitly separates linear pair-kernel terms from quadratic and
higher remainders. The obstruction is not algebraic plausibility. The
obstruction is provenance: UV-023 needs an actual two-atom source object before
whitening, while the inspected source only verifies one-pair weighted formulas
and then warns that post-whitening source summation has the wrong parity.

# Needed for promotion

1. Define the actual two-atom corrected block triple before whitening.
2. Define
   `L_h=\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\delta G_{h,-},\delta N_h,\delta G_{h,+})`
   as a source functor through order 7.
3. Prove the two-atom source-linear input is
   `X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2}` up to terms that are
   irrelevant for `Q_7^q`.
4. Prove this input can be fed into `\mathcal T_{Q,R}` and that the resulting
   cross-effect admits the source-bidegree projection `\Pi_{1,1}` before
   quotient extraction.
5. Define `Q_7^q` before determinant scalarization and prove
   `Q_7^q((1-\Pi_{1,1})C)=0`.

# Autoresearch next step

continue: write the definition-level lemma for promotion review:
"the pair-kernel-linear part of the weighted corrected block perturbation is a
canonical source-linear triple `L_h` before whitening." Then source-check
whether the one-pair formula proof at `proof_of_rh.tex:2659-2787` is enough to
support it or whether an explicit actual two-atom block definition must be
added first.

verify: adversarially test any proposed `L_h` definition for invariance under
normalization, vanishing at `w=0`, and failure modes where `Q_7^q` still sees
cubic non-`(1,1)` source bidegrees.

blocked: no process blocker. Mathematical blocker is the missing actual
two-atom corrected block definition and the missing `Q_7^q` compatibility
theorem.

terminal: terminal for obtaining `L_h` as a current-source theorem. Not terminal
for adding `L_h` as a new pre-whitening definition supported by the one-pair
linear-kernel bookkeeping.

Honest verdict: UV-023 remains open. The best candidate source input is clear:
use the pre-whitening pair-kernel-linear part of the corrected block
perturbation. The current paper supports that only as one-pair bookkeeping, not
as the actual two-atom source functor needed for promotion.
