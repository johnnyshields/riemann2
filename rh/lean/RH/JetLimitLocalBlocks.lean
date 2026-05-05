/-
Section 3 of `rh/rh_rebuild.tex`: jet-limit local blocks.

Lean module for the §3 jet-limit local blocks.  The analytic/Taylor
inputs are exposed as explicit axioms; the algebraic matrix identities
are stated as Lean theorems.

Maps to the LaTeX as follows:
  RH.JetLimitLocalBlocks.samePointBlock
      ↔ A_h(T) of Lemma `lem:same-point-jet-limit`
  RH.JetLimitLocalBlocks.crossBlock
      ↔ C_h(T₁, T₂) of Lemma `lem:cross-block-jet-limit`
  RH.JetLimitLocalBlocks.J
      ↔ J(T) of `eq:same-point-J`
  RH.JetLimitLocalBlocks.N12
      ↔ N_{12}(T₁, T₂) of `eq:cross-N12`
  RH.JetLimitLocalBlocks.D_J
      ↔ D_J(T) of `eq:same-point-gram-determinant`

Theorems:
  same_point_jet_limit               ↔ Lemma `lem:same-point-jet-limit`
  cross_block_jet_limit              ↔ Lemma `lem:cross-block-jet-limit`
  J_trace, J_det                     ↔ Lemma `lem:algebraic-same-point-gram-criterion`
  algebraic_gram_criterion           ↔ Lemma `lem:algebraic-same-point-gram-criterion`
  same_point_gram_positivity         ↔ Lemma `lem:same-point-gram-positivity`
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Topology.Instances.Matrix
import Mathlib.Topology.Order.Basic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Analysis.Real.Pi.Bounds

import RH.LocalKernelJetNormalization
import RH.RiemannSiegelTheta

namespace RH.JetLimitLocalBlocks

open Real Matrix RH.LocalKernelJetNormalization RH.RiemannSiegelTheta

/-! ## Block matrices -/

/-- Same-point block `A_h(T)` of K_Φ at the pair `(T - h, T + h)`,
    with row/column order `(T - h, T + h)`. -/
noncomputable def samePointBlock (T h : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![phaseKernel (T - h) (T - h), phaseKernel (T - h) (T + h);
     phaseKernel (T + h) (T - h), phaseKernel (T + h) (T + h)]

/-- Cross-block `C_h(T₁, T₂)` of K_Φ between the pairs
    `(T₁ - h, T₁ + h)` and `(T₂ - h, T₂ + h)`,
    with row order `(T₁ - h, T₁ + h)` and column order
    `(T₂ - h, T₂ + h)`. -/
noncomputable def crossBlock (T₁ T₂ h : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![phaseKernel (T₁ - h) (T₂ - h), phaseKernel (T₁ - h) (T₂ + h);
     phaseKernel (T₁ + h) (T₂ - h), phaseKernel (T₁ + h) (T₂ + h)]

/-! ## Limit matrices -/

/-- Same-point Gram block `J(T)` of `eq:same-point-J`. -/
noncomputable def J (T : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  (1 / Real.pi) • !![2 * q T,           qPrime T / 2;
                     qPrime T / 2,      (qDoublePrime T + 2 * (q T)^3) / 12]

/-- Cross-block limit `N₁₂(T₁, T₂)` of `eq:cross-N12`. -/
noncomputable def N12 (T₁ T₂ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  let s    := T₁ - T₂
  let Δ    := theta T₁ - theta T₂
  let q₁   := q T₁
  let q₂   := q T₂
  !![(2 * Real.sin Δ) / s,
     (Real.sin Δ - q₂ * s * Real.cos Δ) / s^2;
     (q₁ * s * Real.cos Δ - Real.sin Δ) / s^2,
     ((q₁ + q₂) * s * Real.cos Δ +
      (q₁ * q₂ * s^2 - 2) * Real.sin Δ) / (2 * s^3)]

/-! ## O(h²) rate statements (axiomatic Taylor inputs)

    The paper proves `P_h A_h(T) P_h^⊤ = J(T) + O(h²)` and the
    corresponding cross-block bound entrywise.  The plain `Tendsto`
    versions follow by squeeze; the explicit `O(h²)` form is required
    by downstream finite-scale comparisons.

    **Decomposition for future closure.**  Each rate axiom decomposes
    into per-entry bounds on the 2 × 2 matrix `P_h A_h(T) P_h^⊤ − J(T)`.
    Using the symmetry-induced parity of the entries (each is an *even*
    function of `h`), the order-1 Taylor coefficient at `h = 0` vanishes,
    and the residual is `O(h²)`.  Concretely:

    * Entry `(1, 2) = (q(T+h) − q(T−h)) / (4πh) − q'(T)/(2π)`.  This
      reduces to `|q(T+h) − q(T−h) − 2 q'(T) h| ≤ M h³`, which follows
      from `taylor_mean_remainder_lagrange_iteratedDeriv` for `q` at `T`
      with `n = 2` (using `q ∈ C^3`, derived from `theta_smooth`) and a
      uniform bound on `iteratedDeriv 3 q` over `[T − 1, T + 1]`.
    * Entry `(1, 1) = (q(T−h) + q(T+h))/(2π) + sin(θ(T+h) − θ(T−h)) /
      (2πh) − 2q(T)/π`.  This involves a Taylor expansion of `sin ∘ ε`
      where `ε(h) := θ(T+h) − θ(T−h)`, giving a third-order bound on
      `sin(ε(h))/h − 2q(T) − (q''(T) − 4q(T)³)/3 · h²` via
      `Real.sin_bound` plus order-3 Taylor of `θ`.
    * Entry `(2, 2) = (q(T−h) + q(T+h))/(8πh²) − sin(...)/(8πh³) −
      (q''(T) + 2q(T)³)/(12π)`.  The leading and `h¹/h⁰` terms cancel
      after the Taylor expansions, leaving the `O(h²)` residual.

    For the cross block (`T₁ ≠ T₂`), the entries involve `θ(T_i ± h)`
    differences across the fixed separation `s = T₁ − T₂` and the
    expansions are smooth (no `1/h^k` blowups for `h ≤ |s|/3`); the
    bound is again `M h²` with `M` depending on `1/|s|`.

    **Build-out cost.**  Each per-entry bound is roughly `~200 Lean
    lines` (Lagrange remainder setup + compact-interval sup-norm bound
    + algebraic combination), giving `~600−800 lines` per rate axiom
    plus shared infrastructure for q/theta Taylor remainders.  Both
    rate axioms together would be `~1500−2000 lines`. -/

/-- Helper: phaseKernel values at `(T ± h, T ± h)` for `h > 0`. -/
private lemma phaseKernel_vals_at_pm (T h : ℝ) (h_pos : 0 < h) :
    phaseKernel (T - h) (T - h) = q (T - h) / Real.pi ∧
    phaseKernel (T + h) (T + h) = q (T + h) / Real.pi ∧
    phaseKernel (T - h) (T + h) =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) ∧
    phaseKernel (T + h) (T - h) =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) := by
  have hh_ne : h ≠ 0 := ne_of_gt h_pos
  have h_neq_h : (T - h) ≠ (T + h) := by intro heq; linarith
  have h_pK_aa : phaseKernel (T - h) (T - h) = q (T - h) / Real.pi := by
    unfold phaseKernel; simp
  have h_pK_bb : phaseKernel (T + h) (T + h) = q (T + h) / Real.pi := by
    unfold phaseKernel; simp
  have h_pK_ab : phaseKernel (T - h) (T + h) =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) := by
    unfold phaseKernel
    rw [if_neg h_neq_h]
    have hsub : T - h - (T + h) = -(2 * h) := by ring
    rw [hsub]
    rw [show Real.pi * -(2 * h) = -(Real.pi * (2 * h)) from by ring]
    have h_sin : Real.sin (theta (T - h) - theta (T + h)) =
                 -Real.sin (theta (T + h) - theta (T - h)) := by
      rw [show theta (T - h) - theta (T + h) = -(theta (T + h) - theta (T - h)) from by ring,
          Real.sin_neg]
    rw [h_sin]
    field_simp
  have h_pK_ba : phaseKernel (T + h) (T - h) =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) := by
    rw [phase_kernel_symmetric]; exact h_pK_ab
  exact ⟨h_pK_aa, h_pK_bb, h_pK_ab, h_pK_ba⟩

/-- The bare 2×2 matrix `M_p(h) = !![1, 1; -1/(2h), 1/(2h)]` with the
    `1/√2` factor of `pointToJetTransform` stripped. -/
private noncomputable def jetMatrixBare (h : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1, 1; -1/(2*h), 1/(2*h)]

/-- `pointToJetTransform h = (1/√2) • jetMatrixBare h`. -/
private lemma pointToJetTransform_eq (h : ℝ) :
    pointToJetTransform h = (1 / Real.sqrt 2) • jetMatrixBare h := rfl

/-- The smul-factor of `pointToJetTransform` extracted: `P_h X P_h^⊤ =
    (1/2) • (M_p(h) * X * M_p(h)^⊤)`. -/
private lemma pointToJetTransform_mul_eq (h : ℝ) (X : Matrix (Fin 2) (Fin 2) ℝ) :
    pointToJetTransform h * X * (pointToJetTransform h).transpose =
    (1/2 : ℝ) • (jetMatrixBare h * X * (jetMatrixBare h).transpose) := by
  rw [pointToJetTransform_eq]
  rw [Matrix.transpose_smul]
  rw [Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  congr 1
  rw [show (1 / Real.sqrt 2 : ℝ) * (1 / Real.sqrt 2) = 1 / (Real.sqrt 2 * Real.sqrt 2) from by
    ring]
  rw [Real.mul_self_sqrt (by norm_num : (0:ℝ) ≤ 2)]

/-- Pointwise values of `samePointBlock T h` for `h > 0`. -/
private lemma samePointBlock_apply (T h : ℝ) (h_pos : 0 < h) :
    samePointBlock T h 0 0 = q (T - h) / Real.pi ∧
    samePointBlock T h 0 1 =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) ∧
    samePointBlock T h 1 0 =
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) ∧
    samePointBlock T h 1 1 = q (T + h) / Real.pi := by
  have ⟨h_pK_aa, h_pK_bb, h_pK_ab, h_pK_ba⟩ := phaseKernel_vals_at_pm T h h_pos
  refine ⟨?_, ?_, ?_, ?_⟩
  all_goals (unfold samePointBlock; simp [h_pK_aa, h_pK_bb, h_pK_ab, h_pK_ba])

/-- Pointwise values of `jetMatrixBare h` (the bare 2×2 part). -/
private lemma jetMatrixBare_apply (h : ℝ) :
    jetMatrixBare h 0 0 = 1 ∧
    jetMatrixBare h 0 1 = 1 ∧
    jetMatrixBare h 1 0 = -1 / (2 * h) ∧
    jetMatrixBare h 1 1 = 1 / (2 * h) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [jetMatrixBare]

/-- Matrix entry `(0, 0)` of `P_h A_h(T) P_h^⊤`. -/
private lemma jet_matrix_apply_00 (T h : ℝ) (h_pos : 0 < h) :
    (pointToJetTransform h * samePointBlock T h *
      (pointToJetTransform h).transpose) 0 0 =
    (q (T - h) + q (T + h)) / (2 * Real.pi) +
    Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) := by
  have ⟨h_A_00, h_A_01, h_A_10, h_A_11⟩ := samePointBlock_apply T h h_pos
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := ne_of_gt h_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01, h_A_00, h_A_01, h_A_10, h_A_11]
  field_simp
  ring

/-- Matrix entry `(0, 1)` of `P_h A_h(T) P_h^⊤`. -/
private lemma jet_matrix_apply_01 (T h : ℝ) (h_pos : 0 < h) :
    (pointToJetTransform h * samePointBlock T h *
      (pointToJetTransform h).transpose) 0 1 =
    (q (T + h) - q (T - h)) / (4 * Real.pi * h) := by
  have ⟨h_A_00, h_A_01, h_A_10, h_A_11⟩ := samePointBlock_apply T h h_pos
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := ne_of_gt h_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01, h_M_10, h_M_11, h_A_00, h_A_01, h_A_10, h_A_11]
  field_simp
  ring

/-- Matrix entry `(1, 0)` of `P_h A_h(T) P_h^⊤`. -/
private lemma jet_matrix_apply_10 (T h : ℝ) (h_pos : 0 < h) :
    (pointToJetTransform h * samePointBlock T h *
      (pointToJetTransform h).transpose) 1 0 =
    (q (T + h) - q (T - h)) / (4 * Real.pi * h) := by
  have ⟨h_A_00, h_A_01, h_A_10, h_A_11⟩ := samePointBlock_apply T h h_pos
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := ne_of_gt h_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01, h_M_10, h_M_11, h_A_00, h_A_01, h_A_10, h_A_11]
  field_simp
  ring

/-- Matrix entry `(1, 1)` of `P_h A_h(T) P_h^⊤`. -/
private lemma jet_matrix_apply_11 (T h : ℝ) (h_pos : 0 < h) :
    (pointToJetTransform h * samePointBlock T h *
      (pointToJetTransform h).transpose) 1 1 =
    (q (T - h) + q (T + h)) / (8 * Real.pi * h^2) -
    Real.sin (theta (T + h) - theta (T - h)) / (8 * Real.pi * h^3) := by
  have ⟨h_A_00, h_A_01, h_A_10, h_A_11⟩ := samePointBlock_apply T h h_pos
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := ne_of_gt h_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_10, h_M_11, h_A_00, h_A_01, h_A_10, h_A_11]
  field_simp
  ring

/-- `J(T)` entry values. -/
private lemma J_apply (T : ℝ) :
    J T 0 0 = 2 * q T / Real.pi ∧
    J T 0 1 = qPrime T / (2 * Real.pi) ∧
    J T 1 0 = qPrime T / (2 * Real.pi) ∧
    J T 1 1 = (qDoublePrime T + 2 * (q T)^3) / (12 * Real.pi) := by
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    (unfold J; simp [Matrix.smul_apply, smul_eq_mul]; field_simp)

/-- Bound on entry `(0, 1)` of `P_h A_h(T) P_h^⊤ − J(T)` is `O(h²)`. -/
private lemma rate_bound_01 (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) 0 1| ≤ M * h^2 := by
  obtain ⟨K_q, hK_q_nn, hK_q⟩ := q_taylor_remainder_2 T
  obtain ⟨_, hJ_01, _, _⟩ := J_apply T
  refine ⟨K_q / (2 * Real.pi), by positivity, ?_⟩
  intro h h_pos h_le
  rw [Matrix.sub_apply, jet_matrix_apply_01 T h h_pos, hJ_01]
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hh_ne : h ≠ 0 := h_pos.ne'
  have h_pos_abs : |h| ≤ 1 := by rw [abs_of_pos h_pos]; exact h_le
  have h_neg_abs : |(-h)| ≤ 1 := by rw [abs_neg]; exact h_pos_abs
  have h_taylor_p := hK_q h h_pos_abs
  have h_taylor_m := hK_q (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_m
  have habs_h : |h|^3 = h^3 := by rw [abs_of_pos h_pos]
  have habs_neg_h : |(-h)|^3 = h^3 := by rw [abs_neg, abs_of_pos h_pos]
  rw [habs_h] at h_taylor_p
  rw [habs_neg_h] at h_taylor_m
  -- Key bound: |q(T+h) - q(T-h) - 2 qPrime T h| ≤ 2 K_q h^3.
  have h_abs_diff : |q (T + h) - q (T - h) - 2 * qPrime T * h| ≤ 2 * K_q * h^3 := by
    have heq : q (T + h) - q (T - h) - 2 * qPrime T * h =
        (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2)) -
        (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2)) := by ring
    rw [heq]
    have htri := abs_sub
      (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2))
      (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2))
    linarith
  -- |(q(T+h) - q(T-h))/(4πh) - qPrime T/(2π)| = |(q(T+h) - q(T-h) - 2 qPrime T h)/(4πh)|
  have h_eq : (q (T + h) - q (T - h)) / (4 * Real.pi * h) - qPrime T / (2 * Real.pi) =
      (q (T + h) - q (T - h) - 2 * qPrime T * h) / (4 * Real.pi * h) := by
    field_simp
    ring
  rw [h_eq]
  rw [abs_div]
  rw [abs_of_pos (by positivity : 0 < 4 * Real.pi * h)]
  rw [div_le_iff₀ (by positivity : 0 < 4 * Real.pi * h)]
  calc |q (T + h) - q (T - h) - 2 * qPrime T * h|
      ≤ 2 * K_q * h^3 := h_abs_diff
    _ = K_q / (2 * Real.pi) * h^2 * (4 * Real.pi * h) := by
        field_simp
        ring

set_option maxHeartbeats 1200000 in
/-- Bound on entry `(0, 0)` of `P_h A_h(T) P_h^⊤ − J(T)` is `O(h²)`. -/
private lemma rate_bound_00 (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) 0 0| ≤ M * h^2 := by
  obtain ⟨K_q, hK_q_nn, hK_q⟩ := q_taylor_remainder_2 T
  obtain ⟨K_θ, hK_θ_nn, hK_θ⟩ := theta_taylor_remainder_3 T
  obtain ⟨hJ_00, _, _, _⟩ := J_apply T
  -- Constants.
  set C_ε : ℝ := 2 * |q T| + |qDoublePrime T| / 3 + 2 * K_θ with hC_ε_def
  have hC_ε_nn : 0 ≤ C_ε := by
    have h1 : 0 ≤ |q T| := abs_nonneg _
    have h2 : 0 ≤ |qDoublePrime T| := abs_nonneg _
    rw [hC_ε_def]; linarith
  set M_sin : ℝ := C_ε^3/6 + C_ε^5/120 + C_ε^6/720 with hM_sin_def
  have hM_sin_nn : 0 ≤ M_sin := by
    have h3 : 0 ≤ C_ε^3 := pow_nonneg hC_ε_nn 3
    have h5 : 0 ≤ C_ε^5 := pow_nonneg hC_ε_nn 5
    have h6 : 0 ≤ C_ε^6 := pow_nonneg hC_ε_nn 6
    rw [hM_sin_def]; positivity
  set M_first : ℝ := (|qDoublePrime T| + 2 * K_q) / (2 * Real.pi) with hM_first_def
  set M_second : ℝ := (M_sin + |qDoublePrime T|/3 + 2 * K_θ) / (2 * Real.pi)
    with hM_second_def
  refine ⟨M_first + M_second, ?_, ?_⟩
  · have hπ_pos : 0 < Real.pi := Real.pi_pos
    have h1 : 0 ≤ M_first := by
      rw [hM_first_def]
      have : 0 ≤ |qDoublePrime T| + 2 * K_q := by linarith [abs_nonneg (qDoublePrime T)]
      positivity
    have h2 : 0 ≤ M_second := by
      rw [hM_second_def]
      have : 0 ≤ M_sin + |qDoublePrime T|/3 + 2 * K_θ := by
        have : 0 ≤ |qDoublePrime T| := abs_nonneg _
        linarith
      positivity
    linarith
  intro h h_pos h_le
  rw [Matrix.sub_apply, jet_matrix_apply_00 T h h_pos, hJ_00]
  have hh_ne : h ≠ 0 := h_pos.ne'
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hπ_ne : Real.pi ≠ 0 := hπ_pos.ne'
  have h_pos_abs : |h| ≤ 1 := by rw [abs_of_pos h_pos]; exact h_le
  have h_neg_abs : |(-h)| ≤ 1 := by rw [abs_neg]; exact h_pos_abs
  have habs_h : |h|^3 = h^3 := by rw [abs_of_pos h_pos]
  have habs_neg_h : |(-h)|^3 = h^3 := by rw [abs_neg, abs_of_pos h_pos]
  have habs_h4 : |h|^4 = h^4 := by rw [abs_of_pos h_pos]
  have habs_neg_h4 : |(-h)|^4 = h^4 := by rw [abs_neg, abs_of_pos h_pos]
  -- Decompose the entry into two parts.
  have h_decomp : (q (T - h) + q (T + h)) / (2 * Real.pi) +
      Real.sin (theta (T + h) - theta (T - h)) / (2 * Real.pi * h) -
      2 * q T / Real.pi =
      (q (T - h) + q (T + h) - 2 * q T) / (2 * Real.pi) +
      (Real.sin (theta (T + h) - theta (T - h)) - 2 * q T * h) /
        (2 * Real.pi * h) := by
    field_simp
    ring
  rw [h_decomp]
  set ε : ℝ := theta (T + h) - theta (T - h) with hε_def
  -- Bound first term: |q(T-h) + q(T+h) - 2 q T - qDoublePrime T h^2| ≤ 2 K_q h^3.
  have h_taylor_q_p := hK_q h h_pos_abs
  have h_taylor_q_m := hK_q (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_q_m
  rw [habs_h] at h_taylor_q_p
  rw [habs_neg_h] at h_taylor_q_m
  have h_q_sym : |q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2| ≤
      2 * K_q * h^3 := by
    have heq : q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2 =
      (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2)) +
      (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2)) := by ring
    rw [heq]
    have htri := abs_add_le
      (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2))
      (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2))
    linarith
  have h_q_sum : |q (T + h) + q (T - h) - 2 * q T| ≤
      |qDoublePrime T| * h^2 + 2 * K_q * h^3 := by
    have heq : q (T + h) + q (T - h) - 2 * q T =
        qDoublePrime T * h^2 + (q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2) := by
      ring
    rw [heq]
    have htri := abs_add_le (qDoublePrime T * h^2)
      (q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2)
    have h_abs1 : |qDoublePrime T * h^2| = |qDoublePrime T| * h^2 := by
      rw [abs_mul]
      congr 1
      rw [abs_of_pos (by positivity : 0 < h^2)]
    linarith
  have h_first_bd : |(q (T - h) + q (T + h) - 2 * q T) / (2 * Real.pi)| ≤
      M_first * h^2 := by
    rw [abs_div]
    rw [abs_of_pos (by positivity : 0 < 2 * Real.pi)]
    rw [div_le_iff₀ (by positivity : 0 < 2 * Real.pi)]
    have hreord : q (T - h) + q (T + h) - 2 * q T = q (T + h) + q (T - h) - 2 * q T := by ring
    rw [hreord]
    -- |q sum - 2 q T| ≤ |qDoublePrime T| h^2 + 2 K_q h^3 ≤ (|qDoublePrime T| + 2 K_q) h^2.
    have h3_le_h2 : h^3 ≤ h^2 := by
      have : h^3 = h^2 * h := by ring
      rw [this]
      have : h^2 * h ≤ h^2 * 1 := mul_le_mul_of_nonneg_left h_le (by positivity)
      linarith
    have step1 : |qDoublePrime T| * h^2 + 2 * K_q * h^3 ≤
        (|qDoublePrime T| + 2 * K_q) * h^2 := by
      have : 2 * K_q * h^3 ≤ 2 * K_q * h^2 := by
        have : 2 * K_q * h^3 = 2 * K_q * h^2 * h := by ring
        rw [this]
        nlinarith
      linarith
    calc |q (T + h) + q (T - h) - 2 * q T|
        ≤ |qDoublePrime T| * h^2 + 2 * K_q * h^3 := h_q_sum
      _ ≤ (|qDoublePrime T| + 2 * K_q) * h^2 := step1
      _ = M_first * h^2 * (2 * Real.pi) := by
          rw [hM_first_def]; field_simp
  -- Bound on |ε|: |ε| ≤ C_ε h.
  have h_taylor_θ_p := hK_θ h h_pos_abs
  have h_taylor_θ_m := hK_θ (-h) h_neg_abs
  rw [h_T_m] at h_taylor_θ_m
  rw [habs_h4] at h_taylor_θ_p
  rw [habs_neg_h4] at h_taylor_θ_m
  -- |ε - 2 qT h - qDoublePrime T h^3/3| ≤ 2 K_θ h^4.
  have h_ε_sub : |ε - 2 * q T * h - qDoublePrime T * h^3 / 3| ≤ 2 * K_θ * h^4 := by
    have heq : ε - 2 * q T * h - qDoublePrime T * h^3 / 3 =
        (theta (T + h) -
          (theta T + q T * h + qPrime T * h^2/2 + qDoublePrime T * h^3/6)) -
        (theta (T - h) -
          (theta T + q T * (-h) + qPrime T * (-h)^2/2 + qDoublePrime T * (-h)^3/6)) := by
      simp [hε_def]; ring
    rw [heq]
    have htri := abs_sub
      (theta (T + h) -
        (theta T + q T * h + qPrime T * h^2/2 + qDoublePrime T * h^3/6))
      (theta (T - h) -
        (theta T + q T * (-h) + qPrime T * (-h)^2/2 + qDoublePrime T * (-h)^3/6))
    linarith
  have h_ε_2qT : |ε - 2 * q T * h| ≤ (|qDoublePrime T|/3 + 2 * K_θ) * h^3 := by
    have heq : ε - 2 * q T * h =
        qDoublePrime T * h^3/3 + (ε - 2 * q T * h - qDoublePrime T * h^3/3) := by ring
    rw [heq]
    have htri := abs_add_le (qDoublePrime T * h^3/3)
      (ε - 2 * q T * h - qDoublePrime T * h^3/3)
    have h_abs1 : |qDoublePrime T * h^3 / 3| = |qDoublePrime T| * h^3 / 3 := by
      rw [show qDoublePrime T * h^3 / 3 = (qDoublePrime T * h^3) / 3 from rfl]
      rw [abs_div, abs_mul, abs_of_pos (by positivity : 0 < h^3)]
      have : |(3 : ℝ)| = 3 := by norm_num
      rw [this]
    have h4_le_h3 : h^4 ≤ h^3 := by
      have : h^4 = h^3 * h := by ring
      rw [this]
      have : h^3 * h ≤ h^3 * 1 := mul_le_mul_of_nonneg_left h_le (by positivity)
      linarith
    have h_step : |qDoublePrime T| * h^3 / 3 + 2 * K_θ * h^4 ≤
        (|qDoublePrime T|/3 + 2 * K_θ) * h^3 := by
      have : 2 * K_θ * h^4 ≤ 2 * K_θ * h^3 := by nlinarith
      have heq2 : (|qDoublePrime T|/3 + 2 * K_θ) * h^3 =
          |qDoublePrime T| * h^3 / 3 + 2 * K_θ * h^3 := by ring
      linarith
    linarith
  have h_ε_bd : |ε| ≤ C_ε * h := by
    have heq : ε = 2 * q T * h + (ε - 2 * q T * h) := by ring
    rw [heq]
    have htri := abs_add_le (2 * q T * h) (ε - 2 * q T * h)
    have h_abs1 : |2 * q T * h| = 2 * |q T| * h := by
      rw [abs_mul, abs_mul]
      rw [show |(2 : ℝ)| = 2 from by norm_num]
      rw [abs_of_pos h_pos]
    rw [hC_ε_def]
    have h3_le_h : h^3 ≤ h := by
      have heq3 : h^3 = h * h^2 := by ring
      rw [heq3]
      have : h * h^2 ≤ h * 1 :=
        mul_le_mul_of_nonneg_left (by nlinarith) (le_of_lt h_pos)
      linarith
    have h_d : (|qDoublePrime T|/3 + 2 * K_θ) * h^3 ≤
        (|qDoublePrime T|/3 + 2 * K_θ) * h := by
      have : 0 ≤ |qDoublePrime T|/3 + 2 * K_θ := by
        have : 0 ≤ |qDoublePrime T| := abs_nonneg _
        linarith
      nlinarith
    linarith
  -- |sin(ε) - ε| ≤ M_sin h^3.
  have h_sin_sub : |Real.sin ε - ε| ≤ M_sin * h^3 := by
    have h_sin5 := sin_taylor_remainder_5 ε
    -- |sin ε - (ε - ε^3/6 + ε^5/120)| ≤ |ε|^6/720
    have h_decomp_sin : Real.sin ε - ε =
        (Real.sin ε - (ε - ε^3/6 + ε^5/120)) - ε^3/6 + ε^5/120 := by ring
    have habs1 := abs_sub (Real.sin ε - (ε - ε^3/6 + ε^5/120) - ε^3/6) (ε^5/120)
    have habs2 := abs_sub (Real.sin ε - (ε - ε^3/6 + ε^5/120)) (ε^3/6)
    have h_abs_e3 : |ε^3 / 6| = |ε|^3 / 6 := by
      rw [abs_div, abs_pow]
      rw [show |(6 : ℝ)| = 6 from by norm_num]
    have h_abs_e5 : |ε^5 / 120| = |ε|^5 / 120 := by
      rw [abs_div, abs_pow]
      rw [show |(120 : ℝ)| = 120 from by norm_num]
    have h_abs_e6 : |ε|^6 = |ε|^6 := rfl
    have h_e_sub : |Real.sin ε - ε| ≤ |ε|^6/720 + |ε|^3/6 + |ε|^5/120 := by
      rw [h_decomp_sin]
      have h1 : |Real.sin ε - (ε - ε^3/6 + ε^5/120) - ε^3/6 + ε^5/120| ≤
          |Real.sin ε - (ε - ε^3/6 + ε^5/120) - ε^3/6| + |ε^5/120| := by
        have := abs_add_le (Real.sin ε - (ε - ε^3/6 + ε^5/120) - ε^3/6) (ε^5/120)
        linarith
      have h2 : |Real.sin ε - (ε - ε^3/6 + ε^5/120) - ε^3/6| ≤
          |Real.sin ε - (ε - ε^3/6 + ε^5/120)| + |ε^3/6| := by
        have := abs_sub (Real.sin ε - (ε - ε^3/6 + ε^5/120)) (ε^3/6)
        linarith
      rw [h_abs_e3, h_abs_e5] at *
      linarith
    -- |ε|^k ≤ C_ε^k h^k for k = 3, 5, 6.
    have h_e_pow : ∀ k : ℕ, |ε|^k ≤ C_ε^k * h^k := by
      intro k
      have hε_nn : 0 ≤ |ε| := abs_nonneg _
      have h_h_nn : 0 ≤ h := le_of_lt h_pos
      have h_Ce_h : C_ε * h ≥ 0 := mul_nonneg hC_ε_nn h_h_nn
      have h_pow_le : |ε|^k ≤ (C_ε * h)^k := by
        apply pow_le_pow_left₀ hε_nn h_ε_bd
      rw [mul_pow] at h_pow_le
      exact h_pow_le
    have h_e3 := h_e_pow 3
    have h_e5 := h_e_pow 5
    have h_e6 := h_e_pow 6
    -- For h ∈ (0, 1]: h^k ≤ h^3 for k ≥ 3.
    have h_h_nn : 0 ≤ h := le_of_lt h_pos
    have h_h3_nn : 0 ≤ h^3 := pow_nonneg h_h_nn 3
    have h_h2_le : h^2 ≤ 1 := by
      have : h * h ≤ 1 * 1 := mul_le_mul h_le h_le h_h_nn zero_le_one
      have heq : h^2 = h * h := by ring
      rw [heq]; linarith
    have h_h3_le : h^3 ≤ 1 := by
      have h32 : h^3 = h * h^2 := by ring
      rw [h32]
      have : h * h^2 ≤ 1 * 1 :=
        mul_le_mul h_le h_h2_le (by positivity) zero_le_one
      linarith
    have h5_le_h3 : h^5 ≤ h^3 := by
      have heq : h^5 = h^3 * h^2 := by ring
      rw [heq]
      have : h^3 * h^2 ≤ h^3 * 1 :=
        mul_le_mul_of_nonneg_left h_h2_le h_h3_nn
      linarith
    have h6_le_h3 : h^6 ≤ h^3 := by
      have heq : h^6 = h^3 * h^3 := by ring
      rw [heq]
      have : h^3 * h^3 ≤ h^3 * 1 :=
        mul_le_mul_of_nonneg_left h_h3_le h_h3_nn
      linarith
    -- Combine.
    have hC5_nn : 0 ≤ C_ε^5 := pow_nonneg hC_ε_nn 5
    have hC6_nn : 0 ≤ C_ε^6 := pow_nonneg hC_ε_nn 6
    have h_target : |ε|^6/720 + |ε|^3/6 + |ε|^5/120 ≤
        (C_ε^3/6 + C_ε^5/120 + C_ε^6/720) * h^3 := by
      have h_e3' : |ε|^3/6 ≤ C_ε^3 * h^3 / 6 := by linarith
      have h_C5h5_le : C_ε^5 * h^5 ≤ C_ε^5 * h^3 :=
        mul_le_mul_of_nonneg_left h5_le_h3 hC5_nn
      have h_e5' : |ε|^5/120 ≤ C_ε^5 * h^3 / 120 := by linarith
      have h_C6h6_le : C_ε^6 * h^6 ≤ C_ε^6 * h^3 :=
        mul_le_mul_of_nonneg_left h6_le_h3 hC6_nn
      have h_e6' : |ε|^6/720 ≤ C_ε^6 * h^3 / 720 := by linarith
      have h_combine : C_ε^3 * h^3 / 6 + C_ε^5 * h^3 / 120 + C_ε^6 * h^3 / 720 =
          (C_ε^3/6 + C_ε^5/120 + C_ε^6/720) * h^3 := by ring
      linarith
    rw [hM_sin_def]
    linarith
  -- |sin(ε) - 2 q T h| ≤ (M_sin + |qDoublePrime T|/3 + 2 K_θ) * h^3.
  have h_sin_2qT : |Real.sin ε - 2 * q T * h| ≤
      (M_sin + |qDoublePrime T|/3 + 2 * K_θ) * h^3 := by
    have heq : Real.sin ε - 2 * q T * h = (Real.sin ε - ε) + (ε - 2 * q T * h) := by ring
    rw [heq]
    have := abs_add_le (Real.sin ε - ε) (ε - 2 * q T * h)
    have h1 := h_sin_sub
    have h2 := h_ε_2qT
    linarith
  -- Bound second term.
  have h_second_bd :
      |(Real.sin (theta (T + h) - theta (T - h)) - 2 * q T * h) /
        (2 * Real.pi * h)| ≤ M_second * h^2 := by
    rw [show theta (T + h) - theta (T - h) = ε from rfl]
    rw [abs_div, abs_of_pos (by positivity : 0 < 2 * Real.pi * h)]
    rw [div_le_iff₀ (by positivity : 0 < 2 * Real.pi * h)]
    calc |Real.sin ε - 2 * q T * h|
        ≤ (M_sin + |qDoublePrime T|/3 + 2 * K_θ) * h^3 := h_sin_2qT
      _ = M_second * h^2 * (2 * Real.pi * h) := by
          rw [hM_second_def]; field_simp
  -- Triangle inequality: total ≤ M_first h^2 + M_second h^2.
  have h_total :=
    abs_add_le ((q (T - h) + q (T + h) - 2 * q T) / (2 * Real.pi))
      ((Real.sin (theta (T + h) - theta (T - h)) - 2 * q T * h) /
        (2 * Real.pi * h))
  calc |(q (T - h) + q (T + h) - 2 * q T) / (2 * Real.pi) +
        (Real.sin (theta (T + h) - theta (T - h)) - 2 * q T * h) /
          (2 * Real.pi * h)|
      ≤ |(q (T - h) + q (T + h) - 2 * q T) / (2 * Real.pi)| +
        |(Real.sin (theta (T + h) - theta (T - h)) - 2 * q T * h) /
          (2 * Real.pi * h)| := h_total
    _ ≤ M_first * h^2 + M_second * h^2 := by linarith
    _ = (M_first + M_second) * h^2 := by ring

/-- Bound on entry `(1, 0)` is the same as `(0, 1)` by symmetry. -/
private lemma rate_bound_10 (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) 1 0| ≤ M * h^2 := by
  obtain ⟨M, hM_nn, hM⟩ := rate_bound_01 T
  refine ⟨M, hM_nn, ?_⟩
  intro h h_pos h_le
  obtain ⟨_, hJ_01, hJ_10, _⟩ := J_apply T
  have h_diff_eq : (pointToJetTransform h * samePointBlock T h *
        (pointToJetTransform h).transpose - J T) 1 0 =
      (pointToJetTransform h * samePointBlock T h *
        (pointToJetTransform h).transpose - J T) 0 1 := by
    rw [Matrix.sub_apply, Matrix.sub_apply,
        jet_matrix_apply_10 T h h_pos, jet_matrix_apply_01 T h h_pos,
        hJ_01, hJ_10]
  rw [h_diff_eq]
  exact hM h h_pos h_le

/-- Helper: q sum residual for use in rate_bound_11.  -/
private lemma q_sum_residual_bound (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2| ≤ K * h^4 := by
  obtain ⟨K_q3, hK_q3_nn, hK_q3⟩ := q_taylor_remainder_3 T
  refine ⟨2 * K_q3, by positivity, ?_⟩
  intro h h_pos h_le
  have h_pos_abs : |h| ≤ 1 := by rw [abs_of_pos h_pos]; exact h_le
  have h_neg_abs : |(-h)| ≤ 1 := by rw [abs_neg]; exact h_pos_abs
  have h_T_m : T + (-h) = T - h := by ring
  have habs_h4 : |h|^4 = h^4 := by rw [abs_of_pos h_pos]
  have habs_neg_h4 : |(-h)|^4 = h^4 := by rw [abs_neg, abs_of_pos h_pos]
  have h_q_p := hK_q3 h h_pos_abs
  have h_q_m := hK_q3 (-h) h_neg_abs
  rw [h_T_m] at h_q_m
  rw [habs_h4] at h_q_p
  rw [habs_neg_h4] at h_q_m
  have heq : q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2 =
    (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2 +
      iteratedDeriv 3 q T * h^3 / 6)) +
    (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2 +
      iteratedDeriv 3 q T * (-h)^3 / 6)) := by ring
  rw [heq]
  have htri := abs_add_le
    (q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2/2 +
      iteratedDeriv 3 q T * h^3 / 6))
    (q (T - h) - (q T + qPrime T * (-h) + qDoublePrime T * (-h)^2/2 +
      iteratedDeriv 3 q T * (-h)^3 / 6))
  linarith

/-- Helper: ε := θ(T+h) - θ(T-h) residual for use in rate_bound_11. -/
private lemma epsilon_residual_bound (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(theta (T + h) - theta (T - h)) - 2 * q T * h - qDoublePrime T * h^3 / 3 -
        iteratedDeriv 5 theta T * h^5 / 60| ≤ K * h^6 := by
  obtain ⟨K_θ5, hK_θ5_nn, hK_θ5⟩ := theta_taylor_remainder_5 T
  refine ⟨2 * K_θ5, by positivity, ?_⟩
  intro h h_pos h_le
  have h_pos_abs : |h| ≤ 1 := by rw [abs_of_pos h_pos]; exact h_le
  have h_neg_abs : |(-h)| ≤ 1 := by rw [abs_neg]; exact h_pos_abs
  have h_T_m : T + (-h) = T - h := by ring
  have habs_h6 : |h|^6 = h^6 := by rw [abs_of_pos h_pos]
  have habs_neg_h6 : |(-h)|^6 = h^6 := by rw [abs_neg, abs_of_pos h_pos]
  have h_θ_p := hK_θ5 h h_pos_abs
  have h_θ_m := hK_θ5 (-h) h_neg_abs
  rw [h_T_m] at h_θ_m
  rw [habs_h6] at h_θ_p
  rw [habs_neg_h6] at h_θ_m
  have heq : theta (T + h) - theta (T - h) - 2 * q T * h -
        qDoublePrime T * h^3 / 3 - iteratedDeriv 5 theta T * h^5 / 60 =
    (theta (T + h) - (theta T + q T * h + qPrime T * h^2/2 +
      qDoublePrime T * h^3/6 + iteratedDeriv 4 theta T * h^4/24 +
      iteratedDeriv 5 theta T * h^5/120)) -
    (theta (T - h) - (theta T + q T * (-h) + qPrime T * (-h)^2/2 +
      qDoublePrime T * (-h)^3/6 + iteratedDeriv 4 theta T * (-h)^4/24 +
      iteratedDeriv 5 theta T * (-h)^5/120)) := by ring
  rw [heq]
  have htri : |(theta (T + h) - (theta T + q T * h + qPrime T * h^2/2 +
        qDoublePrime T * h^3/6 + iteratedDeriv 4 theta T * h^4/24 +
        iteratedDeriv 5 theta T * h^5/120)) -
      (theta (T - h) - (theta T + q T * (-h) + qPrime T * (-h)^2/2 +
        qDoublePrime T * (-h)^3/6 + iteratedDeriv 4 theta T * (-h)^4/24 +
        iteratedDeriv 5 theta T * (-h)^5/120))| ≤
      |theta (T + h) - (theta T + q T * h + qPrime T * h^2/2 +
        qDoublePrime T * h^3/6 + iteratedDeriv 4 theta T * h^4/24 +
        iteratedDeriv 5 theta T * h^5/120)| +
      |theta (T - h) - (theta T + q T * (-h) + qPrime T * (-h)^2/2 +
        qDoublePrime T * (-h)^3/6 + iteratedDeriv 4 theta T * (-h)^4/24 +
        iteratedDeriv 5 theta T * (-h)^5/120)| := by
    have heq2 : ∀ a b : ℝ, a - b = a + (-b) := fun _ _ => by ring
    rw [heq2]
    have habs_neg : ∀ x : ℝ, |(-x)| = |x| := abs_neg
    have := abs_add_le
      (theta (T + h) - (theta T + q T * h + qPrime T * h^2/2 +
        qDoublePrime T * h^3/6 + iteratedDeriv 4 theta T * h^4/24 +
        iteratedDeriv 5 theta T * h^5/120))
      (-(theta (T - h) - (theta T + q T * (-h) + qPrime T * (-h)^2/2 +
        qDoublePrime T * (-h)^3/6 + iteratedDeriv 4 theta T * (-h)^4/24 +
        iteratedDeriv 5 theta T * (-h)^5/120)))
    rw [habs_neg] at this
    exact this
  linarith

/-- |ε| ≤ C h on the unit interval, where ε := θ(T+h) - θ(T-h). -/
private lemma epsilon_abs_bound (T : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |theta (T + h) - theta (T - h)| ≤ C * h := by
  obtain ⟨K_ε, hK_ε_nn, hK_ε⟩ := epsilon_residual_bound T
  set C : ℝ := 2 * |q T| + |qDoublePrime T|/3 + |iteratedDeriv 5 theta T|/60 + K_ε
    with hC_def
  have hC_nn : 0 ≤ C := by
    have := abs_nonneg (q T); have := abs_nonneg (qDoublePrime T)
    have := abs_nonneg (iteratedDeriv 5 theta T)
    rw [hC_def]; linarith
  refine ⟨C, hC_nn, ?_⟩
  intro h h_pos h_le
  have h_h_nn : 0 ≤ h := le_of_lt h_pos
  have h_h2_le_1 : h^2 ≤ 1 := by nlinarith
  have h_h3_le_h : h^3 ≤ h := by
    have heq : h^3 = h * h^2 := by ring
    rw [heq]
    have := mul_le_mul_of_nonneg_left h_h2_le_1 h_h_nn
    linarith
  have h_h5_le_h : h^5 ≤ h := by
    have heq : h^5 = h * h^4 := by ring
    rw [heq]
    have h_h4_le_1 : h^4 ≤ 1 := by nlinarith
    have := mul_le_mul_of_nonneg_left h_h4_le_1 h_h_nn
    linarith
  have h_h6_le_h : h^6 ≤ h := by
    have heq : h^6 = h * h^5 := by ring
    rw [heq]
    have h_h5_le_1 : h^5 ≤ 1 := by nlinarith
    have := mul_le_mul_of_nonneg_left h_h5_le_1 h_h_nn
    linarith
  have hε_res := hK_ε h h_pos h_le
  have heq : theta (T + h) - theta (T - h) =
      (theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
        iteratedDeriv 5 theta T * h^5/60) +
      (2 * q T * h + qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60) := by
    ring
  rw [heq]
  have htri := abs_add_le
    (theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
      iteratedDeriv 5 theta T * h^5/60)
    (2 * q T * h + qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60)
  -- Spart parses as ((2 qT h) + qD h^3/3) + d_5 h^5/60 (left-assoc).
  -- |Spart| ≤ |(2 qT h) + qD h^3/3| + |d_5 h^5/60| ≤ |2 qT h| + |qD h^3/3| + |d_5 h^5/60|.
  have h_tri2 := abs_add_le (2 * q T * h + qDoublePrime T * h^3/3)
    (iteratedDeriv 5 theta T * h^5/60)
  have h_tri3 := abs_add_le (2 * q T * h) (qDoublePrime T * h^3/3)
  have h_abs_2qTh : |2 * q T * h| = 2 * |q T| * h := by
    rw [abs_mul, abs_mul]
    rw [show |(2:ℝ)| = 2 from by norm_num, abs_of_pos h_pos]
  have h_abs_qDh3 : |qDoublePrime T * h^3 / 3| = |qDoublePrime T| * h^3 / 3 := by
    rw [show qDoublePrime T * h^3 / 3 = qDoublePrime T * h^3 * (1/3) from by ring]
    rw [abs_mul, abs_mul]
    rw [abs_of_pos (by positivity : (0:ℝ) < h^3)]
    rw [show |(1/3 : ℝ)| = 1/3 from abs_of_pos (by norm_num)]
    ring
  have h_abs_d5h5 : |iteratedDeriv 5 theta T * h^5 / 60| =
      |iteratedDeriv 5 theta T| * h^5 / 60 := by
    rw [show iteratedDeriv 5 theta T * h^5 / 60 =
        iteratedDeriv 5 theta T * h^5 * (1/60) from by ring]
    rw [abs_mul, abs_mul]
    rw [abs_of_pos (by positivity : (0:ℝ) < h^5)]
    rw [show |(1/60 : ℝ)| = 1/60 from abs_of_pos (by norm_num)]
    ring
  -- bounds for the polynomial pieces
  have b_qD : |qDoublePrime T| * h^3 ≤ |qDoublePrime T| * h := by
    have := abs_nonneg (qDoublePrime T)
    nlinarith
  have b_d5 : |iteratedDeriv 5 theta T| * h^5 ≤ |iteratedDeriv 5 theta T| * h := by
    have := abs_nonneg (iteratedDeriv 5 theta T)
    nlinarith
  have b_Kε : K_ε * h^6 ≤ K_ε * h := by nlinarith
  rw [hC_def]
  -- Set up shorthand.
  set R : ℝ := theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
    iteratedDeriv 5 theta T * h^5/60
  set Spart : ℝ := 2 * q T * h + qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60
  -- htri form: |R + S| ≤ |R| + |S|.
  -- Derivative bounds.
  have h_qD_h3_le_h : |qDoublePrime T| * h^3 ≤ |qDoublePrime T| * h := b_qD
  have h_d5_h5_le_h : |iteratedDeriv 5 theta T| * h^5 ≤
      |iteratedDeriv 5 theta T| * h := b_d5
  -- Chain step by step:
  calc |R + Spart|
      ≤ |R| + |Spart| := htri
    _ ≤ K_ε * h^6 + |Spart| := by linarith
    _ ≤ K_ε * h^6 + (|2 * q T * h + qDoublePrime T * h^3/3| +
        |iteratedDeriv 5 theta T * h^5/60|) := by linarith
    _ ≤ K_ε * h^6 + (|2 * q T * h| + |qDoublePrime T * h^3/3| +
        |iteratedDeriv 5 theta T * h^5/60|) := by linarith
    _ = K_ε * h^6 + (2 * |q T| * h + |qDoublePrime T| * h^3 / 3 +
        |iteratedDeriv 5 theta T| * h^5 / 60) := by
          rw [h_abs_2qTh, h_abs_qDh3, h_abs_d5h5]
    _ ≤ K_ε * h + (2 * |q T| * h + |qDoublePrime T| / 3 * h +
        |iteratedDeriv 5 theta T| / 60 * h) := by linarith
    _ = (2 * |q T| + |qDoublePrime T|/3 + |iteratedDeriv 5 theta T|/60 + K_ε) * h := by
          ring

/-- |ε - 2 qT h| ≤ D h^3 on the unit interval. -/
private lemma epsilon_minus_2qTh_bound (T : ℝ) :
    ∃ D : ℝ, 0 ≤ D ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |theta (T + h) - theta (T - h) - 2 * q T * h| ≤ D * h^3 := by
  obtain ⟨K_ε, hK_ε_nn, hK_ε⟩ := epsilon_residual_bound T
  set D : ℝ := |qDoublePrime T|/3 + |iteratedDeriv 5 theta T|/60 + K_ε with hD_def
  have hD_nn : 0 ≤ D := by
    have := abs_nonneg (qDoublePrime T)
    have := abs_nonneg (iteratedDeriv 5 theta T)
    rw [hD_def]; linarith
  refine ⟨D, hD_nn, ?_⟩
  intro h h_pos h_le
  have h_h_nn : 0 ≤ h := le_of_lt h_pos
  have h_h2_le_1 : h^2 ≤ 1 := by nlinarith
  have h_h3_nn : 0 ≤ h^3 := by positivity
  have h_h5_le_h3 : h^5 ≤ h^3 := by
    have heq : h^5 = h^3 * h^2 := by ring
    rw [heq]
    nlinarith
  have h_h6_le_h3 : h^6 ≤ h^3 := by
    have heq : h^6 = h^3 * h^3 := by ring
    rw [heq]
    have h_h3_le_1 : h^3 ≤ 1 := by nlinarith
    nlinarith
  have hε_res := hK_ε h h_pos h_le
  have heq : theta (T + h) - theta (T - h) - 2 * q T * h =
      (theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
        iteratedDeriv 5 theta T * h^5/60) +
      (qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60) := by ring
  rw [heq]
  have htri := abs_add_le
    (theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
      iteratedDeriv 5 theta T * h^5/60)
    (qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60)
  have h_tri2 := abs_add_le (qDoublePrime T * h^3/3) (iteratedDeriv 5 theta T * h^5/60)
  have h_abs_qDh3 : |qDoublePrime T * h^3 / 3| = |qDoublePrime T| * h^3 / 3 := by
    rw [show qDoublePrime T * h^3 / 3 = qDoublePrime T * h^3 * (1/3) from by ring]
    rw [abs_mul, abs_mul, abs_of_pos (pow_pos h_pos 3)]
    rw [show |(1/3 : ℝ)| = 1/3 from abs_of_pos (by norm_num)]
    ring
  have h_abs_d5h5 : |iteratedDeriv 5 theta T * h^5 / 60| =
      |iteratedDeriv 5 theta T| * h^5 / 60 := by
    rw [show iteratedDeriv 5 theta T * h^5 / 60 =
        iteratedDeriv 5 theta T * h^5 * (1/60) from by ring]
    rw [abs_mul, abs_mul, abs_of_pos (pow_pos h_pos 5)]
    rw [show |(1/60 : ℝ)| = 1/60 from abs_of_pos (by norm_num)]
    ring
  rw [hD_def]
  calc |(theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
        iteratedDeriv 5 theta T * h^5/60) +
      (qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60)|
      ≤ |theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
          iteratedDeriv 5 theta T * h^5/60| +
        |qDoublePrime T * h^3/3 + iteratedDeriv 5 theta T * h^5/60| := htri
    _ ≤ K_ε * h^6 + (|qDoublePrime T * h^3/3| + |iteratedDeriv 5 theta T * h^5/60|) := by
        linarith
    _ = K_ε * h^6 + (|qDoublePrime T| * h^3 / 3 + |iteratedDeriv 5 theta T| * h^5 / 60) := by
        rw [h_abs_qDh3, h_abs_d5h5]
    _ ≤ K_ε * h^3 + (|qDoublePrime T| * h^3 / 3 + |iteratedDeriv 5 theta T| * h^3 / 60) := by
        have hKε : 0 ≤ K_ε := hK_ε_nn
        have h_qD_nn : 0 ≤ |qDoublePrime T| := abs_nonneg _
        have h_d5_nn : 0 ≤ |iteratedDeriv 5 theta T| := abs_nonneg _
        nlinarith
    _ = (|qDoublePrime T|/3 + |iteratedDeriv 5 theta T|/60 + K_ε) * h^3 := by ring

/-- |ε^3 - 8 qT^3 h^3| ≤ E h^5 on the unit interval. -/
private lemma epsilon_cube_residual_bound (T : ℝ) :
    ∃ E : ℝ, 0 ≤ E ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(theta (T + h) - theta (T - h))^3 - 8 * (q T)^3 * h^3| ≤ E * h^5 := by
  obtain ⟨D, hD_nn, hD⟩ := epsilon_minus_2qTh_bound T
  set E : ℝ := 12 * |q T|^2 * D + 6 * |q T| * D^2 + D^3 with hE_def
  have hE_nn : 0 ≤ E := by
    have h1 : 0 ≤ |q T|^2 := by positivity
    have h2 : 0 ≤ |q T| := abs_nonneg _
    have h3 : 0 ≤ D^2 := by positivity
    have h4 : 0 ≤ D^3 := by positivity
    rw [hE_def]
    positivity
  refine ⟨E, hE_nn, ?_⟩
  intro h h_pos h_le
  have h_h_nn : 0 ≤ h := le_of_lt h_pos
  have h_h2_nn : 0 ≤ h^2 := by positivity
  have h_h2_le_1 : h^2 ≤ 1 := by nlinarith
  have h_h7_le_h5 : h^7 ≤ h^5 := by
    have : h^7 = h^5 * h^2 := by ring
    rw [this]; nlinarith [pow_nonneg h_h_nn 5]
  have h_h9_le_h5 : h^9 ≤ h^5 := by
    have : h^9 = h^5 * h^4 := by ring
    rw [this]
    have h_h4_le_1 : h^4 ≤ 1 := by nlinarith
    nlinarith [pow_nonneg h_h_nn 5]
  -- δ := theta(T+h) - theta(T-h) - 2 qT h.
  set δ : ℝ := theta (T + h) - theta (T - h) - 2 * q T * h with hδ_def
  -- |δ| ≤ D h^3.
  have hδ_bd : |δ| ≤ D * h^3 := hD h h_pos h_le
  have hδ_sq_bd : |δ|^2 ≤ D^2 * h^6 := by
    have h_δ_nn : 0 ≤ |δ| := abs_nonneg _
    have h_D_h3_nn : 0 ≤ D * h^3 := by positivity
    have h_sq : |δ|^2 ≤ (D * h^3)^2 := by nlinarith
    have heq : (D * h^3)^2 = D^2 * h^6 := by ring
    linarith
  have hδ_cube_bd : |δ|^3 ≤ D^3 * h^9 := by
    have h_δ_nn : 0 ≤ |δ| := abs_nonneg _
    have h_D_h3_nn : 0 ≤ D * h^3 := by positivity
    have h_cube : |δ|^3 ≤ (D * h^3)^3 := by
      have := pow_le_pow_left₀ h_δ_nn hδ_bd 3
      exact this
    have heq : (D * h^3)^3 = D^3 * h^9 := by ring
    linarith
  -- (theta(T+h) - theta(T-h))^3 - 8 qT^3 h^3 = 12 qT^2 h^2 δ + 6 qT h δ^2 + δ^3.
  have heq : (theta (T + h) - theta (T - h))^3 - 8 * (q T)^3 * h^3 =
      12 * (q T)^2 * h^2 * δ + 6 * q T * h * δ^2 + δ^3 := by
    rw [hδ_def]; ring
  rw [heq]
  -- Use triangle and absolute value lemmas.
  have h_qT_sq_eq : |q T|^2 = (q T)^2 := sq_abs (q T)
  have h_term1_abs : |12 * (q T)^2 * h^2 * δ| ≤ 12 * |q T|^2 * h^2 * |δ| := by
    rw [show 12 * (q T)^2 * h^2 * δ = 12 * h^2 * ((q T)^2 * δ) from by ring]
    rw [abs_mul, abs_mul, abs_of_pos (by norm_num : (0:ℝ) < 12),
        abs_of_pos (pow_pos h_pos 2)]
    rw [show |(q T)^2 * δ| = (q T)^2 * |δ| from by rw [abs_mul]; rw [abs_of_nonneg (sq_nonneg _)]]
    rw [← h_qT_sq_eq]
    linarith
  have h_term2_abs : |6 * q T * h * δ^2| ≤ 6 * |q T| * h * |δ|^2 := by
    have habs : |6 * q T * h * δ^2| = 6 * |q T| * h * |δ|^2 := by
      rw [abs_mul, abs_mul, abs_mul, abs_of_pos (by norm_num : (0:ℝ) < 6),
          abs_of_pos h_pos]
      have : |δ^2| = |δ|^2 := abs_pow δ 2
      rw [this]
    linarith
  have h_term3_abs : |δ^3| = |δ|^3 := abs_pow δ 3
  -- Combine.
  have htri := abs_add_le (12 * (q T)^2 * h^2 * δ + 6 * q T * h * δ^2) (δ^3)
  have htri2 := abs_add_le (12 * (q T)^2 * h^2 * δ) (6 * q T * h * δ^2)
  have h_qT2_h2_nn : 0 ≤ |q T|^2 * h^2 := by positivity
  have h_qT_h_nn : 0 ≤ |q T| * h := by
    have := abs_nonneg (q T); have := le_of_lt h_pos; positivity
  -- 12 |qT|^2 h^2 |δ| ≤ 12 |qT|^2 h^2 * D h^3 = 12 |qT|^2 D h^5.
  have h_t1 : 12 * |q T|^2 * h^2 * |δ| ≤ 12 * |q T|^2 * D * h^5 := by
    have : 12 * |q T|^2 * h^2 * |δ| ≤ 12 * |q T|^2 * h^2 * (D * h^3) := by
      have h_h2_nn' : 0 ≤ 12 * |q T|^2 * h^2 := by positivity
      nlinarith
    have heq2 : 12 * |q T|^2 * h^2 * (D * h^3) = 12 * |q T|^2 * D * h^5 := by ring
    linarith
  -- 6 |qT| h |δ|^2 ≤ 6 |qT| h * D^2 h^6 = 6 |qT| D^2 h^7 ≤ 6 |qT| D^2 h^5.
  have h_t2 : 6 * |q T| * h * |δ|^2 ≤ 6 * |q T| * D^2 * h^5 := by
    have step1 : 6 * |q T| * h * |δ|^2 ≤ 6 * |q T| * h * (D^2 * h^6) := by
      have h_qT_h_nn' : 0 ≤ 6 * |q T| * h := by positivity
      nlinarith
    have heq2 : 6 * |q T| * h * (D^2 * h^6) = 6 * |q T| * D^2 * h^7 := by ring
    have h_h7 : 6 * |q T| * D^2 * h^7 ≤ 6 * |q T| * D^2 * h^5 := by
      have : 0 ≤ 6 * |q T| * D^2 := by
        have := abs_nonneg (q T); have := sq_nonneg D; positivity
      nlinarith
    linarith
  -- |δ|^3 ≤ D^3 h^9 ≤ D^3 h^5.
  have h_t3 : |δ|^3 ≤ D^3 * h^5 := by
    have h_h9_le : D^3 * h^9 ≤ D^3 * h^5 := by
      have : 0 ≤ D^3 := by positivity
      nlinarith
    linarith
  -- Combine.
  rw [hE_def]
  calc |12 * (q T)^2 * h^2 * δ + 6 * q T * h * δ^2 + δ^3|
      ≤ |12 * (q T)^2 * h^2 * δ + 6 * q T * h * δ^2| + |δ^3| := htri
    _ ≤ |12 * (q T)^2 * h^2 * δ| + |6 * q T * h * δ^2| + |δ^3| := by linarith
    _ ≤ 12 * |q T|^2 * h^2 * |δ| + 6 * |q T| * h * |δ|^2 + |δ|^3 := by
        rw [h_term3_abs] at *
        linarith
    _ ≤ 12 * |q T|^2 * D * h^5 + 6 * |q T| * D^2 * h^5 + D^3 * h^5 := by linarith
    _ = (12 * |q T|^2 * D + 6 * |q T| * D^2 + D^3) * h^5 := by ring

/-- |ε^5| ≤ C^5 h^5 on the unit interval (raw `ε^5` upper bound). -/
private lemma epsilon_pow_5_bound (T : ℝ) :
    ∃ F : ℝ, 0 ≤ F ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(theta (T + h) - theta (T - h))^5| ≤ F * h^5 := by
  obtain ⟨C, hC_nn, hC⟩ := epsilon_abs_bound T
  refine ⟨C^5, by positivity, ?_⟩
  intro h h_pos h_le
  have h_h_nn : 0 ≤ h := le_of_lt h_pos
  have h_C_h_nn : 0 ≤ C * h := mul_nonneg hC_nn h_h_nn
  have h_eps_pow_5 : |theta (T + h) - theta (T - h)|^5 ≤ (C * h)^5 := by
    have := hC h h_pos h_le
    have h_eps_nn : 0 ≤ |theta (T + h) - theta (T - h)| := abs_nonneg _
    exact pow_le_pow_left₀ h_eps_nn this 5
  have h_abs_pow : |(theta (T + h) - theta (T - h))^5| =
      |theta (T + h) - theta (T - h)|^5 := abs_pow _ 5
  have heq : (C * h)^5 = C^5 * h^5 := by ring
  linarith [h_abs_pow ▸ h_eps_pow_5, heq]

set_option maxHeartbeats 4000000 in
/-- Bound on entry `(1, 1)` of `P_h A_h(T) P_h^⊤ − J(T)` is `O(h²)`. -/
theorem rate_bound_11 (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) 1 1| ≤ M * h^2 := by
  obtain ⟨K_q, hK_q_nn, hK_q⟩ := q_sum_residual_bound T
  obtain ⟨K_ε, hK_ε_nn, hK_ε⟩ := epsilon_residual_bound T
  obtain ⟨C, hC_nn, hC⟩ := epsilon_abs_bound T
  obtain ⟨E, hE_nn, hE⟩ := epsilon_cube_residual_bound T
  obtain ⟨F, hF_nn, hF⟩ := epsilon_pow_5_bound T
  obtain ⟨_, _, _, hJ_11⟩ := J_apply T
  set M_total : ℝ :=
    |iteratedDeriv 5 theta T|/20 + 3 * K_ε + E/2 + F/40 + C^6/240 + 3 * K_q
    with hM_total_def
  set M_11 : ℝ := M_total / (24 * Real.pi) with hM_11_def
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hM_total_nn : 0 ≤ M_total := by
    have := abs_nonneg (iteratedDeriv 5 theta T)
    rw [hM_total_def]; positivity
  refine ⟨M_11, by rw [hM_11_def]; positivity, ?_⟩
  intro h h_pos h_le
  have hh_ne : h ≠ 0 := h_pos.ne'
  have hh_nn : 0 ≤ h := le_of_lt h_pos
  have hπ_ne : Real.pi ≠ 0 := hπ_pos.ne'
  have h_h_le_1 := h_le
  have h_h2_le_1 : h^2 ≤ 1 := by nlinarith
  have h_h_pow_nn : ∀ k : ℕ, 0 ≤ h^k := fun k => pow_nonneg hh_nn k
  have h_h6_le_h5 : h^6 ≤ h^5 := by
    have : h^6 = h^5 * h := by ring
    rw [this]
    have := mul_le_mul_of_nonneg_left h_le (h_h_pow_nn 5)
    linarith
  -- Compute the entry.
  rw [Matrix.sub_apply, jet_matrix_apply_11 T h h_pos, hJ_11]
  set ε : ℝ := theta (T + h) - theta (T - h) with hε_def
  set d_5 : ℝ := iteratedDeriv 5 theta T with hd_5_def
  -- Reformulate as numerator/(24πh^3).
  rw [show (q (T - h) + q (T + h)) / (8 * Real.pi * h^2) -
      Real.sin (theta (T + h) - theta (T - h)) / (8 * Real.pi * h^3) -
      (qDoublePrime T + 2 * (q T)^3) / (12 * Real.pi) =
      (3 * h * (q (T - h) + q (T + h)) - 3 * Real.sin ε -
        2 * (qDoublePrime T + 2 * (q T)^3) * h^3) / (24 * Real.pi * h^3) from by
    rw [show ε = theta (T + h) - theta (T - h) from rfl]
    field_simp
    ring]
  rw [abs_div, abs_of_pos (by positivity : 0 < 24 * Real.pi * h^3),
      div_le_iff₀ (by positivity : 0 < 24 * Real.pi * h^3)]
  -- Goal: |numerator| ≤ M_11 * h^2 * (24 π h^3) = M_total h^5.
  -- Key algebraic identity (verified by hand earlier).
  have h_alg : 3 * h * (q (T - h) + q (T + h)) - 3 * Real.sin ε -
      2 * (qDoublePrime T + 2 * (q T)^3) * h^3 =
    -d_5 * h^5/20 +
      -3 * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60) +
    (ε^3 - 8 * (q T)^3 * h^3)/2 + -ε^5/40 +
      -3 * (Real.sin ε - (ε - ε^3/6 + ε^5/120)) +
    3 * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2) := by
    rw [hd_5_def]
    ring
  rw [h_alg]
  -- Bounds on the six terms.
  have h_q_sum := hK_q h h_pos h_le
  have h_ε_res := hK_ε h h_pos h_le
  have h_ε_abs := hC h h_pos h_le
  have h_eps_cube := hE h h_pos h_le
  have h_eps_pow_5 := hF h h_pos h_le
  have h_sin5 := sin_taylor_remainder_5 ε
  -- |d_5 h^5/20| = |d_5| h^5/20.
  have h_term1 : |(-d_5) * h^5/20| ≤ |iteratedDeriv 5 theta T| / 20 * h^5 := by
    rw [show (-d_5) * h^5/20 = (-d_5) * h^5 * (1/20) from by ring]
    rw [abs_mul, abs_mul, abs_of_pos (pow_pos h_pos 5)]
    rw [show |(1/20:ℝ)| = 1/20 from abs_of_pos (by norm_num)]
    rw [abs_neg]
    rw [hd_5_def]
    have : |iteratedDeriv 5 theta T| * h^5 * (1/20) = |iteratedDeriv 5 theta T| / 20 * h^5 := by
      ring
    linarith [le_refl (|iteratedDeriv 5 theta T| * h^5 * (1/20))]
  -- |3 R_ε| ≤ 3 K_ε h^6 ≤ 3 K_ε h^5.
  have h_term2 : |(-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 -
      d_5 * h^5/60)| ≤ 3 * K_ε * h^5 := by
    rw [hd_5_def, hε_def] at *
    rw [abs_mul, abs_neg, show |(3:ℝ)| = 3 from by norm_num]
    have hres : |theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
        iteratedDeriv 5 theta T * h^5/60| ≤ K_ε * h^6 := h_ε_res
    have : 3 * |theta (T + h) - theta (T - h) - 2 * q T * h - qDoublePrime T * h^3/3 -
        iteratedDeriv 5 theta T * h^5/60| ≤ 3 * (K_ε * h^6) := by linarith
    have h6le5 : 3 * (K_ε * h^6) ≤ 3 * K_ε * h^5 := by
      have h6 : K_ε * h^6 ≤ K_ε * h^5 := by nlinarith [hK_ε_nn]
      linarith
    linarith
  -- |(ε^3 - 8 qT^3 h^3)/2| ≤ E h^5/2.
  have h_term3 : |(ε^3 - 8 * (q T)^3 * h^3)/2| ≤ E/2 * h^5 := by
    rw [show (ε^3 - 8 * (q T)^3 * h^3) / 2 = (ε^3 - 8 * (q T)^3 * h^3) * (1/2) from by ring]
    rw [abs_mul, show |(1/2:ℝ)| = 1/2 from abs_of_pos (by norm_num)]
    have heq : ε^3 = (theta (T + h) - theta (T - h))^3 := by rw [hε_def]
    have h_cube_bd : |(theta (T + h) - theta (T - h))^3 - 8 * (q T)^3 * h^3| ≤ E * h^5 :=
      h_eps_cube
    rw [heq]
    nlinarith
  -- |ε^5/40| ≤ F h^5/40.
  have h_term4 : |(-ε^5)/40| ≤ F/40 * h^5 := by
    rw [show (-ε^5)/40 = (-ε^5) * (1/40) from by ring]
    rw [abs_mul, show |(1/40:ℝ)| = 1/40 from abs_of_pos (by norm_num)]
    rw [abs_neg]
    have heq : ε^5 = (theta (T + h) - theta (T - h))^5 := by rw [hε_def]
    rw [heq]
    have hbd : |(theta (T + h) - theta (T - h))^5| ≤ F * h^5 := h_eps_pow_5
    nlinarith
  -- |3 S_sin| ≤ 3 |ε|^6/720 ≤ C^6 h^6/240 ≤ C^6 h^5/240.
  have h_term5 : |(-3) * (Real.sin ε - (ε - ε^3/6 + ε^5/120))| ≤ C^6/240 * h^5 := by
    rw [abs_mul, abs_neg, show |(3:ℝ)| = 3 from by norm_num]
    have h_sin_bd : |Real.sin ε - (ε - ε^3/6 + ε^5/120)| ≤ |ε|^6/720 := h_sin5
    have h_eps_pow6_bd : |ε|^6 ≤ C^6 * h^6 := by
      have h_eps_le : |ε| ≤ C * h := by rw [hε_def]; exact h_ε_abs
      have h_eps_nn : 0 ≤ |ε| := abs_nonneg _
      have h_pow := pow_le_pow_left₀ h_eps_nn h_eps_le 6
      have hCh : (C * h)^6 = C^6 * h^6 := by ring
      linarith
    have h_eps_pow6_h5 : C^6 * h^6 ≤ C^6 * h^5 := by
      have hC6_nn : 0 ≤ C^6 := pow_nonneg hC_nn 6
      nlinarith
    -- Combine: 3 |sin - poly| ≤ 3 * (|ε|^6/720) ≤ 3 * (C^6 h^6/720) = C^6 h^6/240 ≤ C^6 h^5/240.
    have h_step1 : 3 * |Real.sin ε - (ε - ε^3/6 + ε^5/120)| ≤ 3 * |ε|^6/720 := by
      linarith
    have h_step2 : 3 * |ε|^6 ≤ 3 * (C^6 * h^6) := by
      have := abs_nonneg ε
      nlinarith
    have h_step3 : 3 * (C^6 * h^6)/720 ≤ C^6/240 * h^5 := by
      have heq : 3 * (C^6 * h^6)/720 = C^6 * h^6 / 240 := by ring
      have hC6_nn : 0 ≤ C^6 := pow_nonneg hC_nn 6
      have h6le5 : C^6 * h^6 ≤ C^6 * h^5 := by nlinarith
      have : C^6 * h^6 / 240 ≤ C^6 * h^5 / 240 := by linarith
      have heq2 : C^6 * h^5 / 240 = C^6/240 * h^5 := by ring
      linarith
    linarith
  -- |3 h R_q| ≤ 3 K_q h^5 (R_q has |R_q| ≤ K_q h^4).
  have h_term6 : |3 * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2)| ≤
      3 * K_q * h^5 := by
    rw [show (3:ℝ) * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2) =
        3 * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2) from rfl]
    rw [abs_mul, abs_mul, show |(3:ℝ)| = 3 from by norm_num, abs_of_pos h_pos]
    have hres : |q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2| ≤ K_q * h^4 := h_q_sum
    have hreord : q (T + h) + q (T - h) - 2 * q T - qDoublePrime T * h^2 =
        q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2 := by ring
    rw [hreord] at hres
    have : 3 * h * |q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2| ≤
        3 * h * (K_q * h^4) := by
      have : 0 ≤ 3 * h := by positivity
      nlinarith
    have heq : 3 * h * (K_q * h^4) = 3 * K_q * h^5 := by ring
    linarith
  -- Combine all terms.
  have htri := abs_add_le
    ((-d_5) * h^5/20 +
     ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60)) +
     ((ε^3 - 8 * (q T)^3 * h^3)/2) +
     ((-ε^5)/40) +
     ((-3) * (Real.sin ε - (ε - ε^3/6 + ε^5/120))))
    (3 * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2))
  -- Repeated triangle:
  have htri2 := abs_add_le
    ((-d_5) * h^5/20 +
     ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60)) +
     ((ε^3 - 8 * (q T)^3 * h^3)/2) +
     ((-ε^5)/40))
    ((-3) * (Real.sin ε - (ε - ε^3/6 + ε^5/120)))
  have htri3 := abs_add_le
    ((-d_5) * h^5/20 +
     ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60)) +
     ((ε^3 - 8 * (q T)^3 * h^3)/2))
    ((-ε^5)/40)
  have htri4 := abs_add_le
    ((-d_5) * h^5/20 +
     ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60)))
    ((ε^3 - 8 * (q T)^3 * h^3)/2)
  have htri5 := abs_add_le
    ((-d_5) * h^5/20)
    ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60))
  rw [hM_11_def]
  rw [hM_total_def]
  -- The big inequality.
  have h_full : |((-d_5) * h^5/20 +
      ((-3) * (ε - 2 * q T * h - qDoublePrime T * h^3/3 - d_5 * h^5/60)) +
      ((ε^3 - 8 * (q T)^3 * h^3)/2) +
      ((-ε^5)/40) +
      ((-3) * (Real.sin ε - (ε - ε^3/6 + ε^5/120)))) +
      3 * h * (q (T - h) + q (T + h) - 2 * q T - qDoublePrime T * h^2)| ≤
      (|iteratedDeriv 5 theta T|/20 + 3 * K_ε + E/2 + F/40 + C^6/240 + 3 * K_q) * h^5 := by
    linarith
  -- Goal RHS: M_total / (24 π) * h^2 * (24 π h^3) = M_total * h^5.
  have h_rhs : (|iteratedDeriv 5 theta T| / 20 + 3 * K_ε + E / 2 + F / 40 + C ^ 6 / 240 +
      3 * K_q) /
        (24 * Real.pi) * h^2 * (24 * Real.pi * h^3) =
      (|iteratedDeriv 5 theta T| / 20 + 3 * K_ε + E / 2 + F / 40 + C ^ 6 / 240 +
      3 * K_q) * h ^ 5 := by
    field_simp
  rw [h_rhs]
  linarith [h_full]

/-- Same-point jet-limit with explicit `O(h²)` rate.  Entrywise:
    for `h ∈ (0, 1]` and each entry `(i, j)` of `Fin 2 × Fin 2`,
        `|((P_h A_h(T) P_h^⊤) − J(T)) i j| ≤ M h²`.

    Proved by combining `rate_bound_00`, `rate_bound_01`, `rate_bound_10`,
    `rate_bound_11` with `M := max(M_00, M_01, M_10, M_11)`. -/
theorem same_point_jet_limit_rate (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      ∀ i j : Fin 2,
        |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) i j| ≤ M * h^2 := by
  obtain ⟨M_00, hM_00_nn, hM_00⟩ := rate_bound_00 T
  obtain ⟨M_01, hM_01_nn, hM_01⟩ := rate_bound_01 T
  obtain ⟨M_10, hM_10_nn, hM_10⟩ := rate_bound_10 T
  obtain ⟨M_11, hM_11_nn, hM_11⟩ := rate_bound_11 T
  refine ⟨max M_00 (max M_01 (max M_10 M_11)), ?_, ?_⟩
  · exact le_max_of_le_left hM_00_nn
  intro h h_pos h_le i j
  have h_h2_nn : 0 ≤ h^2 := by positivity
  fin_cases i <;> fin_cases j
  · calc |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) 0 0|
        ≤ M_00 * h^2 := hM_00 h h_pos h_le
      _ ≤ max M_00 (max M_01 (max M_10 M_11)) * h^2 :=
          mul_le_mul_of_nonneg_right (le_max_left _ _) h_h2_nn
  · calc |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) 0 1|
        ≤ M_01 * h^2 := hM_01 h h_pos h_le
      _ ≤ max M_00 (max M_01 (max M_10 M_11)) * h^2 :=
          mul_le_mul_of_nonneg_right
            (le_trans (le_max_left _ _) (le_max_right _ _)) h_h2_nn
  · calc |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) 1 0|
        ≤ M_10 * h^2 := hM_10 h h_pos h_le
      _ ≤ max M_00 (max M_01 (max M_10 M_11)) * h^2 :=
          mul_le_mul_of_nonneg_right
            (le_trans (le_max_left _ _)
              (le_trans (le_max_right _ _) (le_max_right _ _))) h_h2_nn
  · calc |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) 1 1|
        ≤ M_11 * h^2 := hM_11 h h_pos h_le
      _ ≤ max M_00 (max M_01 (max M_10 M_11)) * h^2 :=
          mul_le_mul_of_nonneg_right
            (le_trans (le_max_right _ _)
              (le_trans (le_max_right _ _) (le_max_right _ _))) h_h2_nn

/-! ### Cross-block helpers -/

/-- For `h ∈ (0, |s|/3]` with `s = T₁ - T₂ ≠ 0`, all of `s`, `s + 2h`,
    `s - 2h` are nonzero and bounded below by `|s|/3`. -/
private lemma cross_denominators_nonzero (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    (T₁ - T₂) ≠ 0 ∧
    (T₁ - T₂ + 2 * h) ≠ 0 ∧
    (T₁ - T₂ - 2 * h) ≠ 0 := by
  set s := T₁ - T₂ with hs_def
  have hs_ne : s ≠ 0 := sub_ne_zero.mpr hT
  have hs_abs_pos : 0 < |s| := abs_pos.mpr hs_ne
  have hs_abs_pos_3 : 0 < |s| / 3 := by linarith
  have h_2h_lt : 2 * h ≤ 2 * (|s| / 3) := by linarith
  have h_2h_lt_abs : 2 * h < |s| := by
    have : 2 * (|s| / 3) < |s| := by linarith
    linarith
  refine ⟨hs_ne, ?_, ?_⟩
  · -- s + 2h ≠ 0
    intro heq
    have : 2 * h = -s := by linarith
    rcases lt_or_gt_of_ne hs_ne with hslt | hsgt
    · have hs_abs : |s| = -s := abs_of_neg hslt
      rw [hs_abs] at h_2h_lt_abs
      linarith
    · have hs_abs : |s| = s := abs_of_pos hsgt
      rw [hs_abs] at h_2h_lt_abs
      linarith
  · -- s - 2h ≠ 0
    intro heq
    have : 2 * h = s := by linarith
    rcases lt_or_gt_of_ne hs_ne with hslt | hsgt
    · have hs_abs : |s| = -s := abs_of_neg hslt
      rw [hs_abs] at h_2h_lt_abs
      linarith
    · have hs_abs : |s| = s := abs_of_pos hsgt
      rw [hs_abs] at h_2h_lt_abs
      linarith

/-- phaseKernel values at the 4 cross-block evaluation points,
    for `h ∈ (0, |s|/3]`. -/
private lemma phaseKernel_cross_vals (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    phaseKernel (T₁ - h) (T₂ - h) =
      Real.sin (theta (T₁ - h) - theta (T₂ - h)) /
        (Real.pi * (T₁ - T₂)) ∧
    phaseKernel (T₁ - h) (T₂ + h) =
      Real.sin (theta (T₁ - h) - theta (T₂ + h)) /
        (Real.pi * (T₁ - T₂ - 2 * h)) ∧
    phaseKernel (T₁ + h) (T₂ - h) =
      Real.sin (theta (T₁ + h) - theta (T₂ - h)) /
        (Real.pi * (T₁ - T₂ + 2 * h)) ∧
    phaseKernel (T₁ + h) (T₂ + h) =
      Real.sin (theta (T₁ + h) - theta (T₂ + h)) /
        (Real.pi * (T₁ - T₂)) := by
  obtain ⟨hs_ne, hsp_ne, hsm_ne⟩ := cross_denominators_nonzero T₁ T₂ h hT h_pos h_le
  have h_aa_ne : T₁ - h ≠ T₂ - h := by intro heq; apply hs_ne; linarith
  have h_ab_ne : T₁ - h ≠ T₂ + h := by intro heq; apply hsm_ne; linarith
  have h_ba_ne : T₁ + h ≠ T₂ - h := by intro heq; apply hsp_ne; linarith
  have h_bb_ne : T₁ + h ≠ T₂ + h := by intro heq; apply hs_ne; linarith
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold phaseKernel
    rw [if_neg h_aa_ne]
    congr 2; ring
  · unfold phaseKernel
    rw [if_neg h_ab_ne]
    congr 2; ring
  · unfold phaseKernel
    rw [if_neg h_ba_ne]
    congr 2; ring
  · unfold phaseKernel
    rw [if_neg h_bb_ne]
    congr 2; ring

/-- Pointwise values of `crossBlock T₁ T₂ h` for `h ∈ (0, |s|/3]`. -/
private lemma crossBlock_apply (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    crossBlock T₁ T₂ h 0 0 =
      Real.sin (theta (T₁ - h) - theta (T₂ - h)) / (Real.pi * (T₁ - T₂)) ∧
    crossBlock T₁ T₂ h 0 1 =
      Real.sin (theta (T₁ - h) - theta (T₂ + h)) /
        (Real.pi * (T₁ - T₂ - 2 * h)) ∧
    crossBlock T₁ T₂ h 1 0 =
      Real.sin (theta (T₁ + h) - theta (T₂ - h)) /
        (Real.pi * (T₁ - T₂ + 2 * h)) ∧
    crossBlock T₁ T₂ h 1 1 =
      Real.sin (theta (T₁ + h) - theta (T₂ + h)) / (Real.pi * (T₁ - T₂)) := by
  have ⟨h_pK_00, h_pK_01, h_pK_10, h_pK_11⟩ :=
    phaseKernel_cross_vals T₁ T₂ h hT h_pos h_le
  refine ⟨?_, ?_, ?_, ?_⟩
  all_goals (unfold crossBlock; simp [h_pK_00, h_pK_01, h_pK_10, h_pK_11])

/-- Matrix entry `(0, 0)` of `P_h · C(T₁, T₂; h) · P_h^⊤`. -/
private lemma jet_cross_matrix_apply_00 (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 0 =
    (crossBlock T₁ T₂ h 0 0 + crossBlock T₁ T₂ h 0 1 +
     crossBlock T₁ T₂ h 1 0 + crossBlock T₁ T₂ h 1 1) / 2 := by
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01]
  ring

/-- Matrix entry `(0, 1)` of `P_h · C(T₁, T₂; h) · P_h^⊤`. -/
private lemma jet_cross_matrix_apply_01 (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 1 =
    (-crossBlock T₁ T₂ h 0 0 + crossBlock T₁ T₂ h 0 1 -
     crossBlock T₁ T₂ h 1 0 + crossBlock T₁ T₂ h 1 1) / (4 * h) := by
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := h_pos.ne'
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01, h_M_10, h_M_11]
  field_simp
  ring

/-- Matrix entry `(1, 0)` of `P_h · C(T₁, T₂; h) · P_h^⊤`. -/
private lemma jet_cross_matrix_apply_10 (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 1 0 =
    (-crossBlock T₁ T₂ h 0 0 - crossBlock T₁ T₂ h 0 1 +
     crossBlock T₁ T₂ h 1 0 + crossBlock T₁ T₂ h 1 1) / (4 * h) := by
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := h_pos.ne'
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_00, h_M_01, h_M_10, h_M_11]
  field_simp
  ring

/-- Matrix entry `(1, 1)` of `P_h · C(T₁, T₂; h) · P_h^⊤`. -/
private lemma jet_cross_matrix_apply_11 (T₁ T₂ h : ℝ) (hT : T₁ ≠ T₂)
    (h_pos : 0 < h) (h_le : h ≤ |T₁ - T₂| / 3) :
    (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 1 1 =
    (crossBlock T₁ T₂ h 0 0 - crossBlock T₁ T₂ h 0 1 -
     crossBlock T₁ T₂ h 1 0 + crossBlock T₁ T₂ h 1 1) / (8 * h^2) := by
  have ⟨h_M_00, h_M_01, h_M_10, h_M_11⟩ := jetMatrixBare_apply h
  have hh_ne : h ≠ 0 := h_pos.ne'
  rw [pointToJetTransform_mul_eq]
  rw [Matrix.smul_apply, smul_eq_mul]
  rw [Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.mul_apply, Matrix.mul_apply, Fin.sum_univ_two, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.transpose_apply]
  rw [h_M_10, h_M_11]
  field_simp
  ring

/-- Linear absolute bound on `θ` differences: there is `M ≥ 0` such that
    for `|h| ≤ R`, `|θ(T+h) - θT| ≤ M · |h|`. -/
private lemma theta_lin_abs_bound (T R : ℝ) (hR : 0 < R) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) - theta T| ≤ M * |h| := by
  obtain ⟨K, hK_nn, hK⟩ := theta_taylor_remainder_1_on T R hR
  refine ⟨|q T| + K * R, by positivity, ?_⟩
  intro h hh
  have h_split : theta (T + h) - theta T =
      (theta (T + h) - (theta T + q T * h)) + (q T * h) := by ring
  have h_abs_sq : |h|^2 = h^2 := sq_abs h
  have h_abs_nn : 0 ≤ |h| := abs_nonneg h
  have h_abs_le_R : |h| ≤ R := hh
  calc |theta (T + h) - theta T|
      = |(theta (T + h) - (theta T + q T * h)) + (q T * h)| := by rw [← h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h)| + |q T * h| := abs_add_le _ _
    _ ≤ K * h^2 + |q T| * |h| := by
        rw [abs_mul]; linarith [hK h hh]
    _ = K * (|h| * |h|) + |q T| * |h| := by rw [show h^2 = |h| * |h| from by
          rw [show |h| * |h| = |h|^2 from (sq |h|).symm, h_abs_sq]]
    _ ≤ K * (R * |h|) + |q T| * |h| := by
        have : K * (|h| * |h|) ≤ K * (R * |h|) :=
          mul_le_mul_of_nonneg_left
            (by nlinarith) hK_nn
        linarith
    _ = (|q T| + K * R) * |h| := by ring

/-- Symmetric-sum bound for `θ`: `|θ(T+h) + θ(T-h) - 2 θ T| ≤ 2 K h²`. -/
private lemma theta_sym_sum_bound (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) + theta (T - h) - 2 * theta T| ≤ K * h^2 := by
  obtain ⟨K₀, hK₀_nn, hK₀⟩ := theta_taylor_remainder_1_on T R hR
  refine ⟨2 * K₀, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  have h_taylor_p := hK₀ h hh
  have h_taylor_m := hK₀ (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_m
  have h_neg_sq : (-h)^2 = h^2 := by ring
  rw [h_neg_sq] at h_taylor_m
  have h_split : theta (T + h) + theta (T - h) - 2 * theta T =
      (theta (T + h) - (theta T + q T * h)) +
      (theta (T - h) - (theta T + q T * (-h))) := by ring
  calc |theta (T + h) + theta (T - h) - 2 * theta T|
      = |(theta (T + h) - (theta T + q T * h)) +
         (theta (T - h) - (theta T + q T * (-h)))| := by rw [h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h)| +
        |theta (T - h) - (theta T + q T * (-h))| := abs_add_le _ _
    _ ≤ K₀ * h^2 + K₀ * h^2 := by linarith
    _ = 2 * K₀ * h^2 := by ring

/-- Anti-symmetric difference bound for `θ` at order 3:
    `|θ(T+h) − θ(T−h) − 2 q T h| ≤ 2 K |h|³` (cubic remainder). -/
private lemma theta_anti_sym_diff_bound_3 (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) - theta (T - h) - 2 * q T * h| ≤ K * |h|^3 := by
  obtain ⟨K_2, hK_2_nn, hK_2⟩ := theta_taylor_remainder_2_on T R hR
  refine ⟨2 * K_2, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  have h_taylor_p := hK_2 h hh
  have h_taylor_m := hK_2 (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_m
  have h_neg_sq : (-h)^2 = h^2 := by ring
  rw [h_neg_sq] at h_taylor_m
  have h_neg_abs_3 : |(-h)|^3 = |h|^3 := by rw [abs_neg]
  rw [h_neg_abs_3] at h_taylor_m
  have h_split : theta (T + h) - theta (T - h) - 2 * q T * h =
      (theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)) -
      (theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2)) := by ring
  calc |theta (T + h) - theta (T - h) - 2 * q T * h|
      = |(theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)) -
         (theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2))| := by rw [h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)| +
        |theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2)| := abs_sub _ _
    _ ≤ K_2 * |h|^3 + K_2 * |h|^3 := by linarith
    _ = 2 * K_2 * |h|^3 := by ring

/-- Anti-symmetric difference bound for `θ`:
    `|θ(T+h) − θ(T−h) − 2 q T h| ≤ 2 K h²`. -/
private lemma theta_anti_sym_diff_bound (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) - theta (T - h) - 2 * q T * h| ≤ K * h^2 := by
  obtain ⟨K₀, hK₀_nn, hK₀⟩ := theta_taylor_remainder_1_on T R hR
  refine ⟨2 * K₀, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  have h_taylor_p := hK₀ h hh
  have h_taylor_m := hK₀ (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_m
  have h_neg_sq : (-h)^2 = h^2 := by ring
  rw [h_neg_sq] at h_taylor_m
  have h_split : theta (T + h) - theta (T - h) - 2 * q T * h =
      (theta (T + h) - (theta T + q T * h)) -
      (theta (T - h) - (theta T + q T * (-h))) := by ring
  calc |theta (T + h) - theta (T - h) - 2 * q T * h|
      = |(theta (T + h) - (theta T + q T * h)) -
         (theta (T - h) - (theta T + q T * (-h)))| := by rw [h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h)| +
        |theta (T - h) - (theta T + q T * (-h))| := abs_sub _ _
    _ ≤ K₀ * h^2 + K₀ * h^2 := by linarith
    _ = 2 * K₀ * h^2 := by ring

/-- Pointwise values of `(1/π) • N12 T₁ T₂`. -/
private lemma N12_smul_apply (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ((1 / Real.pi) • N12 T₁ T₂) 0 0 =
      2 * Real.sin (theta T₁ - theta T₂) /
        (Real.pi * (T₁ - T₂)) ∧
    ((1 / Real.pi) • N12 T₁ T₂) 0 1 =
      (Real.sin (theta T₁ - theta T₂) -
        q T₂ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂)) /
        (Real.pi * (T₁ - T₂)^2) ∧
    ((1 / Real.pi) • N12 T₁ T₂) 1 0 =
      (q T₁ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) -
        Real.sin (theta T₁ - theta T₂)) /
        (Real.pi * (T₁ - T₂)^2) ∧
    ((1 / Real.pi) • N12 T₁ T₂) 1 1 =
      ((q T₁ + q T₂) * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) +
        (q T₁ * q T₂ * (T₁ - T₂)^2 - 2) *
          Real.sin (theta T₁ - theta T₂)) /
        (2 * Real.pi * (T₁ - T₂)^3) := by
  have hs_ne : T₁ - T₂ ≠ 0 := sub_ne_zero.mpr hT
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  refine ⟨?_, ?_, ?_, ?_⟩
  all_goals (unfold N12; simp [Matrix.smul_apply, smul_eq_mul]; field_simp)

/-- Sum-of-sines bound for the cross block: for the symmetric pair
    `(α, δ)` and `(β, γ)`,
    `|sin α + sin δ − 2 sin Δ| ≤ M h²` and `|sin β + sin γ − 2 sin Δ| ≤ M h²`. -/
private lemma cross_sin_pair_sym_bound (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, |h| ≤ R →
      |Real.sin (theta (T₁ - h) - theta (T₂ - h)) +
       Real.sin (theta (T₁ + h) - theta (T₂ + h)) -
       2 * Real.sin (theta T₁ - theta T₂)| ≤ M * h^2 ∧
      |Real.sin (theta (T₁ - h) - theta (T₂ + h)) +
       Real.sin (theta (T₁ + h) - theta (T₂ - h)) -
       2 * Real.sin (theta T₁ - theta T₂)| ≤ M * h^2 := by
  obtain ⟨M_lin_1, hM_lin_1_nn, hM_lin_1⟩ := theta_lin_abs_bound T₁ R hR
  obtain ⟨M_lin_2, hM_lin_2_nn, hM_lin_2⟩ := theta_lin_abs_bound T₂ R hR
  obtain ⟨K_sym_1, hK_sym_1_nn, hK_sym_1⟩ := theta_sym_sum_bound T₁ R hR
  obtain ⟨K_sym_2, hK_sym_2_nn, hK_sym_2⟩ := theta_sym_sum_bound T₂ R hR
  refine ⟨(M_lin_1 + M_lin_2)^2 + (K_sym_1 + K_sym_2), by positivity, ?_⟩
  intro h hh
  set Δ := theta T₁ - theta T₂ with hΔ_def
  set α := theta (T₁ - h) - theta (T₂ - h) with hα_def
  set β := theta (T₁ - h) - theta (T₂ + h) with hβ_def
  set γ := theta (T₁ + h) - theta (T₂ - h) with hγ_def
  set δ := theta (T₁ + h) - theta (T₂ + h) with hδ_def
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  -- Linear bounds on θ(T_i ± h) - θ T_i.
  have h_θT₁_p : |theta (T₁ + h) - theta T₁| ≤ M_lin_1 * |h| := hM_lin_1 h hh
  have h_θT₁_m : |theta (T₁ - h) - theta T₁| ≤ M_lin_1 * |h| := by
    have := hM_lin_1 (-h) h_neg_abs
    rw [show T₁ + (-h) = T₁ - h from by ring, abs_neg] at this
    exact this
  have h_θT₂_p : |theta (T₂ + h) - theta T₂| ≤ M_lin_2 * |h| := hM_lin_2 h hh
  have h_θT₂_m : |theta (T₂ - h) - theta T₂| ≤ M_lin_2 * |h| := by
    have := hM_lin_2 (-h) h_neg_abs
    rw [show T₂ + (-h) = T₂ - h from by ring, abs_neg] at this
    exact this
  -- Bounds on |α - Δ|, |β - Δ|, |γ - Δ|, |δ - Δ| ≤ (M_lin_1 + M_lin_2)|h|.
  have h_lin : (M_lin_1 + M_lin_2) * |h| ≥ 0 := by positivity
  have h_α_Δ : |α - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := by
    have h_split : α - Δ =
        (theta (T₁ - h) - theta T₁) - (theta (T₂ - h) - theta T₂) := by
      simp [hα_def, hΔ_def]; ring
    calc |α - Δ|
        = |(theta (T₁ - h) - theta T₁) - (theta (T₂ - h) - theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ - h) - theta T₁| + |theta (T₂ - h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = (M_lin_1 + M_lin_2) * |h| := by ring
  have h_δ_Δ : |δ - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := by
    have h_split : δ - Δ =
        (theta (T₁ + h) - theta T₁) - (theta (T₂ + h) - theta T₂) := by
      simp [hδ_def, hΔ_def]; ring
    calc |δ - Δ|
        = |(theta (T₁ + h) - theta T₁) - (theta (T₂ + h) - theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta T₁| + |theta (T₂ + h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = (M_lin_1 + M_lin_2) * |h| := by ring
  have h_β_Δ : |β - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := by
    have h_split : β - Δ =
        (theta (T₁ - h) - theta T₁) - (theta (T₂ + h) - theta T₂) := by
      simp [hβ_def, hΔ_def]; ring
    calc |β - Δ|
        = |(theta (T₁ - h) - theta T₁) - (theta (T₂ + h) - theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ - h) - theta T₁| + |theta (T₂ + h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = (M_lin_1 + M_lin_2) * |h| := by ring
  have h_γ_Δ : |γ - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := by
    have h_split : γ - Δ =
        (theta (T₁ + h) - theta T₁) - (theta (T₂ - h) - theta T₂) := by
      simp [hγ_def, hΔ_def]; ring
    calc |γ - Δ|
        = |(theta (T₁ + h) - theta T₁) - (theta (T₂ - h) - theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta T₁| + |theta (T₂ - h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = (M_lin_1 + M_lin_2) * |h| := by ring
  -- |α + δ - 2Δ| = |sym₁ - sym₂| ≤ K_sym_1 h² + K_sym_2 h².
  have h_sym_sum : |α + δ - 2 * Δ| ≤ (K_sym_1 + K_sym_2) * h^2 := by
    have h_split : α + δ - 2 * Δ =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂) := by
      simp [hα_def, hδ_def, hΔ_def]; ring
    calc |α + δ - 2 * Δ|
        = |(theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
           (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂| := abs_sub _ _
      _ ≤ K_sym_1 * h^2 + K_sym_2 * h^2 := by
          have h1 := hK_sym_1 h hh
          have h2 := hK_sym_2 h hh
          linarith
      _ = (K_sym_1 + K_sym_2) * h^2 := by ring
  have h_β_γ_sym : |β + γ - 2 * Δ| ≤ (K_sym_1 + K_sym_2) * h^2 := by
    have h_split : β + γ - 2 * Δ =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂) := by
      simp [hβ_def, hγ_def, hΔ_def]; ring
    calc |β + γ - 2 * Δ|
        = |(theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
           (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂)| := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂| := abs_sub _ _
      _ ≤ K_sym_1 * h^2 + K_sym_2 * h^2 := by
          have h1 := hK_sym_1 h hh
          have h2 := hK_sym_2 h hh
          linarith
      _ = (K_sym_1 + K_sym_2) * h^2 := by ring
  -- Now bound each sin pair:
  have h_sin_α : |Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)| ≤ (α - Δ)^2 / 2 := by
    have hh := sin_taylor_at_quad Δ (α - Δ)
    have h_eq : Δ + (α - Δ) = α := by ring
    rw [h_eq] at hh
    have h_sub_eq :
        Real.sin α - (Real.sin Δ + Real.cos Δ * (α - Δ)) =
        Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ) := by ring
    rw [h_sub_eq] at hh
    exact hh
  have h_sin_δ : |Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ)| ≤ (δ - Δ)^2 / 2 := by
    have hh := sin_taylor_at_quad Δ (δ - Δ)
    have h_eq : Δ + (δ - Δ) = δ := by ring
    rw [h_eq] at hh
    have h_sub_eq :
        Real.sin δ - (Real.sin Δ + Real.cos Δ * (δ - Δ)) =
        Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ) := by ring
    rw [h_sub_eq] at hh
    exact hh
  have h_sin_β : |Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)| ≤ (β - Δ)^2 / 2 := by
    have hh := sin_taylor_at_quad Δ (β - Δ)
    have h_eq : Δ + (β - Δ) = β := by ring
    rw [h_eq] at hh
    have h_sub_eq :
        Real.sin β - (Real.sin Δ + Real.cos Δ * (β - Δ)) =
        Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ) := by ring
    rw [h_sub_eq] at hh
    exact hh
  have h_sin_γ : |Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ)| ≤ (γ - Δ)^2 / 2 := by
    have hh := sin_taylor_at_quad Δ (γ - Δ)
    have h_eq : Δ + (γ - Δ) = γ := by ring
    rw [h_eq] at hh
    have h_sub_eq :
        Real.sin γ - (Real.sin Δ + Real.cos Δ * (γ - Δ)) =
        Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ) := by ring
    rw [h_sub_eq] at hh
    exact hh
  have h_cos_le : |Real.cos Δ| ≤ 1 := Real.abs_cos_le_one Δ
  -- Pair (α, δ): bound |sin α + sin δ - 2 sin Δ|.
  have h_α_δ : |Real.sin α + Real.sin δ - 2 * Real.sin Δ| ≤
      ((M_lin_1 + M_lin_2)^2 + (K_sym_1 + K_sym_2)) * h^2 := by
    have h_combined : Real.sin α + Real.sin δ - 2 * Real.sin Δ =
        (Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)) +
        (Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ)) +
        Real.cos Δ * (α + δ - 2 * Δ) := by ring
    have h_α_Δ_sq : (α - Δ)^2 ≤ (M_lin_1 + M_lin_2)^2 * h^2 := by
      have h_abs_le : |α - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := h_α_Δ
      have h_sq_eq : |α - Δ|^2 = (α - Δ)^2 := sq_abs _
      have h_h_sq : |h|^2 = h^2 := sq_abs h
      have h_lin_nn : 0 ≤ M_lin_1 + M_lin_2 := by linarith
      calc (α - Δ)^2 = |α - Δ|^2 := h_sq_eq.symm
        _ ≤ ((M_lin_1 + M_lin_2) * |h|)^2 := by
            apply pow_le_pow_left₀ (abs_nonneg _) h_abs_le
        _ = (M_lin_1 + M_lin_2)^2 * |h|^2 := by ring
        _ = (M_lin_1 + M_lin_2)^2 * h^2 := by rw [h_h_sq]
    have h_δ_Δ_sq : (δ - Δ)^2 ≤ (M_lin_1 + M_lin_2)^2 * h^2 := by
      have h_abs_le : |δ - Δ| ≤ (M_lin_1 + M_lin_2) * |h| := h_δ_Δ
      have h_sq_eq : |δ - Δ|^2 = (δ - Δ)^2 := sq_abs _
      have h_h_sq : |h|^2 = h^2 := sq_abs h
      have h_lin_nn : 0 ≤ M_lin_1 + M_lin_2 := by linarith
      calc (δ - Δ)^2 = |δ - Δ|^2 := h_sq_eq.symm
        _ ≤ ((M_lin_1 + M_lin_2) * |h|)^2 := by
            apply pow_le_pow_left₀ (abs_nonneg _) h_abs_le
        _ = (M_lin_1 + M_lin_2)^2 * |h|^2 := by ring
        _ = (M_lin_1 + M_lin_2)^2 * h^2 := by rw [h_h_sq]
    have h_h_sq_nn : 0 ≤ h^2 := sq_nonneg h
    have h_tri1 : |(Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)) +
            (Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ))| ≤
        |Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)| +
        |Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ)| := abs_add_le _ _
    have h_α_δ_2Δ_nn : 0 ≤ |α + δ - 2 * Δ| := abs_nonneg _
    have h_cos_mul : |Real.cos Δ * (α + δ - 2 * Δ)| ≤ (K_sym_1 + K_sym_2) * h^2 := by
      rw [abs_mul]
      calc |Real.cos Δ| * |α + δ - 2 * Δ|
          ≤ 1 * |α + δ - 2 * Δ| :=
            mul_le_mul_of_nonneg_right h_cos_le h_α_δ_2Δ_nn
        _ ≤ 1 * ((K_sym_1 + K_sym_2) * h^2) :=
            mul_le_mul_of_nonneg_left h_sym_sum (by norm_num)
        _ = (K_sym_1 + K_sym_2) * h^2 := by ring
    calc |Real.sin α + Real.sin δ - 2 * Real.sin Δ|
        = |(Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)) +
           (Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ)) +
           Real.cos Δ * (α + δ - 2 * Δ)| := by rw [h_combined]
      _ ≤ |(Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)) +
            (Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ))| +
          |Real.cos Δ * (α + δ - 2 * Δ)| := abs_add_le _ _
      _ ≤ (|Real.sin α - Real.sin Δ - Real.cos Δ * (α - Δ)| +
           |Real.sin δ - Real.sin Δ - Real.cos Δ * (δ - Δ)|) +
          |Real.cos Δ * (α + δ - 2 * Δ)| := by linarith
      _ ≤ ((α - Δ)^2 / 2 + (δ - Δ)^2 / 2) +
          (K_sym_1 + K_sym_2) * h^2 := by linarith
      _ ≤ ((M_lin_1 + M_lin_2)^2 * h^2 / 2 + (M_lin_1 + M_lin_2)^2 * h^2 / 2) +
          (K_sym_1 + K_sym_2) * h^2 := by linarith
      _ = ((M_lin_1 + M_lin_2)^2 + (K_sym_1 + K_sym_2)) * h^2 := by ring
  -- Pair (β, γ): same constants.
  have h_β_γ : |Real.sin β + Real.sin γ - 2 * Real.sin Δ| ≤
      ((M_lin_1 + M_lin_2)^2 + (K_sym_1 + K_sym_2)) * h^2 := by
    have h_combined : Real.sin β + Real.sin γ - 2 * Real.sin Δ =
        (Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)) +
        (Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ)) +
        Real.cos Δ * (β + γ - 2 * Δ) := by ring
    have h_β_Δ_sq : (β - Δ)^2 ≤ (M_lin_1 + M_lin_2)^2 * h^2 := by
      have h_sq_eq : |β - Δ|^2 = (β - Δ)^2 := sq_abs _
      have h_h_sq : |h|^2 = h^2 := sq_abs h
      calc (β - Δ)^2 = |β - Δ|^2 := h_sq_eq.symm
        _ ≤ ((M_lin_1 + M_lin_2) * |h|)^2 := by
            apply pow_le_pow_left₀ (abs_nonneg _) h_β_Δ
        _ = (M_lin_1 + M_lin_2)^2 * |h|^2 := by ring
        _ = (M_lin_1 + M_lin_2)^2 * h^2 := by rw [h_h_sq]
    have h_γ_Δ_sq : (γ - Δ)^2 ≤ (M_lin_1 + M_lin_2)^2 * h^2 := by
      have h_sq_eq : |γ - Δ|^2 = (γ - Δ)^2 := sq_abs _
      have h_h_sq : |h|^2 = h^2 := sq_abs h
      calc (γ - Δ)^2 = |γ - Δ|^2 := h_sq_eq.symm
        _ ≤ ((M_lin_1 + M_lin_2) * |h|)^2 := by
            apply pow_le_pow_left₀ (abs_nonneg _) h_γ_Δ
        _ = (M_lin_1 + M_lin_2)^2 * |h|^2 := by ring
        _ = (M_lin_1 + M_lin_2)^2 * h^2 := by rw [h_h_sq]
    have h_tri2 : |(Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)) +
            (Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ))| ≤
        |Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)| +
        |Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ)| := abs_add_le _ _
    have h_β_γ_2Δ_nn : 0 ≤ |β + γ - 2 * Δ| := abs_nonneg _
    have h_cos_mul2 : |Real.cos Δ * (β + γ - 2 * Δ)| ≤ (K_sym_1 + K_sym_2) * h^2 := by
      rw [abs_mul]
      calc |Real.cos Δ| * |β + γ - 2 * Δ|
          ≤ 1 * |β + γ - 2 * Δ| :=
            mul_le_mul_of_nonneg_right h_cos_le h_β_γ_2Δ_nn
        _ ≤ 1 * ((K_sym_1 + K_sym_2) * h^2) :=
            mul_le_mul_of_nonneg_left h_β_γ_sym (by norm_num)
        _ = (K_sym_1 + K_sym_2) * h^2 := by ring
    calc |Real.sin β + Real.sin γ - 2 * Real.sin Δ|
        = |(Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)) +
           (Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ)) +
           Real.cos Δ * (β + γ - 2 * Δ)| := by rw [h_combined]
      _ ≤ |(Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)) +
            (Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ))| +
          |Real.cos Δ * (β + γ - 2 * Δ)| := abs_add_le _ _
      _ ≤ (|Real.sin β - Real.sin Δ - Real.cos Δ * (β - Δ)| +
           |Real.sin γ - Real.sin Δ - Real.cos Δ * (γ - Δ)|) +
          |Real.cos Δ * (β + γ - 2 * Δ)| := by linarith
      _ ≤ ((β - Δ)^2 / 2 + (γ - Δ)^2 / 2) +
          (K_sym_1 + K_sym_2) * h^2 := by linarith
      _ ≤ ((M_lin_1 + M_lin_2)^2 * h^2 / 2 + (M_lin_1 + M_lin_2)^2 * h^2 / 2) +
          (K_sym_1 + K_sym_2) * h^2 := by linarith
      _ = ((M_lin_1 + M_lin_2)^2 + (K_sym_1 + K_sym_2)) * h^2 := by ring
  exact ⟨h_α_δ, h_β_γ⟩

/-- Cubic-remainder linear approximation for the cross block:
    sin pairs are linear in h with O(h³) residual.

    `|sin δ − sin α − 2(q T₁ − q T₂) cos Δ · h| ≤ M |h|³`
    `|sin β − sin γ + 2(q T₁ + q T₂) cos Δ · h| ≤ M |h|³`
-/
private lemma cross_sin_pair_anti_lin_bound (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, |h| ≤ R →
      |Real.sin (theta (T₁ + h) - theta (T₂ + h)) -
       Real.sin (theta (T₁ - h) - theta (T₂ - h)) -
       2 * (q T₁ - q T₂) * Real.cos (theta T₁ - theta T₂) * h| ≤ M * |h|^3 ∧
      |Real.sin (theta (T₁ - h) - theta (T₂ + h)) -
       Real.sin (theta (T₁ + h) - theta (T₂ - h)) +
       2 * (q T₁ + q T₂) * Real.cos (theta T₁ - theta T₂) * h| ≤ M * |h|^3 := by
  obtain ⟨M_lin_1, hM_lin_1_nn, hM_lin_1⟩ := theta_lin_abs_bound T₁ R hR
  obtain ⟨M_lin_2, hM_lin_2_nn, hM_lin_2⟩ := theta_lin_abs_bound T₂ R hR
  obtain ⟨K_sym_1, hK_sym_1_nn, hK_sym_1⟩ := theta_sym_sum_bound T₁ R hR
  obtain ⟨K_sym_2, hK_sym_2_nn, hK_sym_2⟩ := theta_sym_sum_bound T₂ R hR
  obtain ⟨K_anti_1, hK_anti_1_nn, hK_anti_1⟩ := theta_anti_sym_diff_bound_3 T₁ R hR
  obtain ⟨K_anti_2, hK_anti_2_nn, hK_anti_2⟩ := theta_anti_sym_diff_bound_3 T₂ R hR
  set M_lin := M_lin_1 + M_lin_2 with hM_lin_def
  set K_sym := K_sym_1 + K_sym_2 with hK_sym_def
  set K_anti := K_anti_1 + K_anti_2 with hK_anti_def
  refine ⟨M_lin^3 / 3 + K_anti + K_sym * M_lin, by positivity, ?_⟩
  intro h hh
  set Δ := theta T₁ - theta T₂ with hΔ_def
  set α := theta (T₁ - h) - theta (T₂ - h) with hα_def
  set β := theta (T₁ - h) - theta (T₂ + h) with hβ_def
  set γ := theta (T₁ + h) - theta (T₂ - h) with hγ_def
  set δ := theta (T₁ + h) - theta (T₂ + h) with hδ_def
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  -- Linear bounds.
  have h_θT₁_p : |theta (T₁ + h) - theta T₁| ≤ M_lin_1 * |h| := hM_lin_1 h hh
  have h_θT₁_m : |theta (T₁ - h) - theta T₁| ≤ M_lin_1 * |h| := by
    have := hM_lin_1 (-h) h_neg_abs
    rw [show T₁ + (-h) = T₁ - h from by ring, abs_neg] at this
    exact this
  have h_θT₂_p : |theta (T₂ + h) - theta T₂| ≤ M_lin_2 * |h| := hM_lin_2 h hh
  have h_θT₂_m : |theta (T₂ - h) - theta T₂| ≤ M_lin_2 * |h| := by
    have := hM_lin_2 (-h) h_neg_abs
    rw [show T₂ + (-h) = T₂ - h from by ring, abs_neg] at this
    exact this
  -- |α - Δ|, |β - Δ|, |γ - Δ|, |δ - Δ| ≤ M_lin |h|
  have h_α_Δ : |α - Δ| ≤ M_lin * |h| := by
    have h_split : α - Δ =
        (theta (T₁ - h) - theta T₁) - (theta (T₂ - h) - theta T₂) := by
      simp [hα_def, hΔ_def]; ring
    calc |α - Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ - h) - theta T₁| + |theta (T₂ - h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = M_lin * |h| := by rw [hM_lin_def]; ring
  have h_β_Δ : |β - Δ| ≤ M_lin * |h| := by
    have h_split : β - Δ =
        (theta (T₁ - h) - theta T₁) - (theta (T₂ + h) - theta T₂) := by
      simp [hβ_def, hΔ_def]; ring
    calc |β - Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ - h) - theta T₁| + |theta (T₂ + h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = M_lin * |h| := by rw [hM_lin_def]; ring
  have h_γ_Δ : |γ - Δ| ≤ M_lin * |h| := by
    have h_split : γ - Δ =
        (theta (T₁ + h) - theta T₁) - (theta (T₂ - h) - theta T₂) := by
      simp [hγ_def, hΔ_def]; ring
    calc |γ - Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta T₁| + |theta (T₂ - h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = M_lin * |h| := by rw [hM_lin_def]; ring
  have h_δ_Δ : |δ - Δ| ≤ M_lin * |h| := by
    have h_split : δ - Δ =
        (theta (T₁ + h) - theta T₁) - (theta (T₂ + h) - theta T₂) := by
      simp [hδ_def, hΔ_def]; ring
    calc |δ - Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta T₁| + |theta (T₂ + h) - theta T₂| := abs_sub _ _
      _ ≤ M_lin_1 * |h| + M_lin_2 * |h| := by linarith
      _ = M_lin * |h| := by rw [hM_lin_def]; ring
  -- |α + δ - 2Δ|, |β + γ - 2Δ| ≤ K_sym h².
  have h_sym_αδ : |α + δ - 2 * Δ| ≤ K_sym * h^2 := by
    have h_split : α + δ - 2 * Δ =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂) := by
      simp [hα_def, hδ_def, hΔ_def]; ring
    calc |α + δ - 2 * Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂| := abs_sub _ _
      _ ≤ K_sym_1 * h^2 + K_sym_2 * h^2 := by linarith [hK_sym_1 h hh, hK_sym_2 h hh]
      _ = K_sym * h^2 := by rw [hK_sym_def]; ring
  have h_sym_βγ : |β + γ - 2 * Δ| ≤ K_sym * h^2 := by
    have h_split : β + γ - 2 * Δ =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂) := by
      simp [hβ_def, hγ_def, hΔ_def]; ring
    calc |β + γ - 2 * Δ| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂| := abs_sub _ _
      _ ≤ K_sym_1 * h^2 + K_sym_2 * h^2 := by linarith [hK_sym_1 h hh, hK_sym_2 h hh]
      _ = K_sym * h^2 := by rw [hK_sym_def]; ring
  -- |δ - α - 2(q₁-q₂)h| ≤ K_anti |h|³
  have h_δα_lin : |δ - α - 2 * (q T₁ - q T₂) * h| ≤ K_anti * |h|^3 := by
    have h_split : δ - α - 2 * (q T₁ - q T₂) * h =
        (theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h) -
        (theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h) := by
      simp [hα_def, hδ_def]; ring
    calc |δ - α - 2 * (q T₁ - q T₂) * h| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h| +
          |theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h| := abs_sub _ _
      _ ≤ K_anti_1 * |h|^3 + K_anti_2 * |h|^3 := by
          linarith [hK_anti_1 h hh, hK_anti_2 h hh]
      _ = K_anti * |h|^3 := by rw [hK_anti_def]; ring
  -- |γ - β - 2(q₁+q₂)h| ≤ K_anti |h|³ (i.e., |β - γ + 2(q₁+q₂)h| ≤ K_anti |h|³)
  have h_βγ_lin : |γ - β - 2 * (q T₁ + q T₂) * h| ≤ K_anti * |h|^3 := by
    have h_split : γ - β - 2 * (q T₁ + q T₂) * h =
        (theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h) +
        (theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h) := by
      simp [hβ_def, hγ_def]; ring
    calc |γ - β - 2 * (q T₁ + q T₂) * h| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h| +
          |theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h| := abs_add_le _ _
      _ ≤ K_anti_1 * |h|^3 + K_anti_2 * |h|^3 := by
          linarith [hK_anti_1 h hh, hK_anti_2 h hh]
      _ = K_anti * |h|^3 := by rw [hK_anti_def]; ring
  -- Sin Taylor at cubic at sin α, β, γ, δ relative to Δ.
  have h_sin_α_cub : |Real.sin α - (Real.sin Δ + Real.cos Δ * (α - Δ) -
      Real.sin Δ * (α - Δ)^2 / 2)| ≤ |α - Δ|^3 / 6 := by
    have hh_cub := sin_taylor_at_cubic Δ (α - Δ)
    have h_eq : Δ + (α - Δ) = α := by ring
    rw [h_eq] at hh_cub
    exact hh_cub
  have h_sin_β_cub : |Real.sin β - (Real.sin Δ + Real.cos Δ * (β - Δ) -
      Real.sin Δ * (β - Δ)^2 / 2)| ≤ |β - Δ|^3 / 6 := by
    have hh_cub := sin_taylor_at_cubic Δ (β - Δ)
    have h_eq : Δ + (β - Δ) = β := by ring
    rw [h_eq] at hh_cub
    exact hh_cub
  have h_sin_γ_cub : |Real.sin γ - (Real.sin Δ + Real.cos Δ * (γ - Δ) -
      Real.sin Δ * (γ - Δ)^2 / 2)| ≤ |γ - Δ|^3 / 6 := by
    have hh_cub := sin_taylor_at_cubic Δ (γ - Δ)
    have h_eq : Δ + (γ - Δ) = γ := by ring
    rw [h_eq] at hh_cub
    exact hh_cub
  have h_sin_δ_cub : |Real.sin δ - (Real.sin Δ + Real.cos Δ * (δ - Δ) -
      Real.sin Δ * (δ - Δ)^2 / 2)| ≤ |δ - Δ|^3 / 6 := by
    have hh_cub := sin_taylor_at_cubic Δ (δ - Δ)
    have h_eq : Δ + (δ - Δ) = δ := by ring
    rw [h_eq] at hh_cub
    exact hh_cub
  have h_cos_le : |Real.cos Δ| ≤ 1 := Real.abs_cos_le_one Δ
  have h_sin_le : |Real.sin Δ| ≤ 1 := Real.abs_sin_le_one Δ
  -- Bounds on |α-Δ|³, etc.
  have h_M_lin_nn : 0 ≤ M_lin := by rw [hM_lin_def]; linarith
  have h_M_lin_h_nn : 0 ≤ M_lin * |h| := by positivity
  have h_α_Δ_cube : |α - Δ|^3 ≤ M_lin^3 * |h|^3 := by
    calc |α - Δ|^3 ≤ (M_lin * |h|)^3 :=
          pow_le_pow_left₀ (abs_nonneg _) h_α_Δ 3
      _ = M_lin^3 * |h|^3 := by ring
  have h_β_Δ_cube : |β - Δ|^3 ≤ M_lin^3 * |h|^3 := by
    calc |β - Δ|^3 ≤ (M_lin * |h|)^3 :=
          pow_le_pow_left₀ (abs_nonneg _) h_β_Δ 3
      _ = M_lin^3 * |h|^3 := by ring
  have h_γ_Δ_cube : |γ - Δ|^3 ≤ M_lin^3 * |h|^3 := by
    calc |γ - Δ|^3 ≤ (M_lin * |h|)^3 :=
          pow_le_pow_left₀ (abs_nonneg _) h_γ_Δ 3
      _ = M_lin^3 * |h|^3 := by ring
  have h_δ_Δ_cube : |δ - Δ|^3 ≤ M_lin^3 * |h|^3 := by
    calc |δ - Δ|^3 ≤ (M_lin * |h|)^3 :=
          pow_le_pow_left₀ (abs_nonneg _) h_δ_Δ 3
      _ = M_lin^3 * |h|^3 := by ring
  -- (δ-Δ)² - (α-Δ)² = (δ+α-2Δ)(δ-α). Bound using sym_sum × lin.
  have h_sq_diff_αδ : (δ - Δ)^2 - (α - Δ)^2 = (δ + α - 2 * Δ) * (δ - α) := by ring
  have h_sq_diff_βγ : (β - Δ)^2 - (γ - Δ)^2 = (β + γ - 2 * Δ) * (β - γ) := by ring
  have h_δ_α : |δ - α| ≤ 2 * M_lin * |h| := by
    have h_split : δ - α = (δ - Δ) - (α - Δ) := by ring
    calc |δ - α| = _ := by rw [h_split]
      _ ≤ |δ - Δ| + |α - Δ| := abs_sub _ _
      _ ≤ M_lin * |h| + M_lin * |h| := by linarith
      _ = 2 * M_lin * |h| := by ring
  have h_β_γ : |β - γ| ≤ 2 * M_lin * |h| := by
    have h_split : β - γ = (β - Δ) - (γ - Δ) := by ring
    calc |β - γ| = _ := by rw [h_split]
      _ ≤ |β - Δ| + |γ - Δ| := abs_sub _ _
      _ ≤ M_lin * |h| + M_lin * |h| := by linarith
      _ = 2 * M_lin * |h| := by ring
  have h_h_sq_eq : |h|^2 = h^2 := sq_abs h
  have h_h_cube_eq : |h|^3 = |h|^2 * |h| := by rw [show |h|^3 = |h| * |h|^2 from by ring]; ring
  -- Bound |sin Δ ((δ-Δ)² - (α-Δ)²) / 2| ≤ K_sym M_lin |h|³.
  have h_sin_Δ_sq_diff_αδ : |Real.sin Δ * ((δ - Δ)^2 - (α - Δ)^2) / 2| ≤
      K_sym * M_lin * |h|^3 := by
    rw [h_sq_diff_αδ]
    rw [show Real.sin Δ * ((δ + α - 2 * Δ) * (δ - α)) / 2 =
        Real.sin Δ * (δ + α - 2 * Δ) * (δ - α) / 2 from by ring]
    rw [abs_div, abs_mul, abs_mul]
    rw [show |(2 : ℝ)| = 2 from by norm_num]
    rw [div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    have h_h_nn : 0 ≤ |h| := abs_nonneg h
    have h_α_δ_sym_eq : δ + α - 2 * Δ = α + δ - 2 * Δ := by ring
    have h_sym_αδ' : |δ + α - 2 * Δ| ≤ K_sym * h^2 := by
      rw [h_α_δ_sym_eq]; exact h_sym_αδ
    have h_α_δ_sym_nn : 0 ≤ |δ + α - 2 * Δ| := abs_nonneg _
    calc |Real.sin Δ| * |δ + α - 2 * Δ| * |δ - α|
        ≤ 1 * (K_sym * h^2) * (2 * M_lin * |h|) := by
          have step1 : |Real.sin Δ| * |δ + α - 2 * Δ| ≤ 1 * |δ + α - 2 * Δ| :=
            mul_le_mul_of_nonneg_right h_sin_le h_α_δ_sym_nn
          have step2 : 1 * |δ + α - 2 * Δ| ≤ 1 * (K_sym * h^2) :=
            mul_le_mul_of_nonneg_left h_sym_αδ' (by norm_num)
          have step3 : 1 * (K_sym * h^2) * |δ - α| ≤
              1 * (K_sym * h^2) * (2 * M_lin * |h|) :=
            mul_le_mul_of_nonneg_left h_δ_α (by positivity)
          have h_lhs_le : |Real.sin Δ| * |δ + α - 2 * Δ| * |δ - α| ≤
              1 * (K_sym * h^2) * |δ - α| := by
            apply mul_le_mul_of_nonneg_right (le_trans step1 step2)
            exact abs_nonneg _
          linarith
      _ = K_sym * M_lin * |h|^3 * 2 := by
          rw [show |h|^3 = h^2 * |h| from by rw [h_h_cube_eq, h_h_sq_eq]]; ring
  have h_sin_Δ_sq_diff_βγ : |Real.sin Δ * ((β - Δ)^2 - (γ - Δ)^2) / 2| ≤
      K_sym * M_lin * |h|^3 := by
    rw [h_sq_diff_βγ]
    rw [show Real.sin Δ * ((β + γ - 2 * Δ) * (β - γ)) / 2 =
        Real.sin Δ * (β + γ - 2 * Δ) * (β - γ) / 2 from by ring]
    rw [abs_div, abs_mul, abs_mul]
    rw [show |(2 : ℝ)| = 2 from by norm_num]
    rw [div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    have h_β_γ_sym_nn : 0 ≤ |β + γ - 2 * Δ| := abs_nonneg _
    calc |Real.sin Δ| * |β + γ - 2 * Δ| * |β - γ|
        ≤ 1 * (K_sym * h^2) * (2 * M_lin * |h|) := by
          have step1 : |Real.sin Δ| * |β + γ - 2 * Δ| ≤ 1 * |β + γ - 2 * Δ| :=
            mul_le_mul_of_nonneg_right h_sin_le h_β_γ_sym_nn
          have step2 : 1 * |β + γ - 2 * Δ| ≤ 1 * (K_sym * h^2) :=
            mul_le_mul_of_nonneg_left h_sym_βγ (by norm_num)
          have step3 : 1 * (K_sym * h^2) * |β - γ| ≤
              1 * (K_sym * h^2) * (2 * M_lin * |h|) :=
            mul_le_mul_of_nonneg_left h_β_γ (by positivity)
          have h_lhs_le : |Real.sin Δ| * |β + γ - 2 * Δ| * |β - γ| ≤
              1 * (K_sym * h^2) * |β - γ| := by
            apply mul_le_mul_of_nonneg_right (le_trans step1 step2)
            exact abs_nonneg _
          linarith
      _ = K_sym * M_lin * |h|^3 * 2 := by
          rw [show |h|^3 = h^2 * |h| from by rw [h_h_cube_eq, h_h_sq_eq]]; ring
  -- Bound |cos Δ (δ - α) - 2(q₁-q₂) cos Δ h| ≤ K_anti |h|³.
  have h_cos_δα : |Real.cos Δ * (δ - α) - 2 * (q T₁ - q T₂) * Real.cos Δ * h| ≤
      K_anti * |h|^3 := by
    have h_eq : Real.cos Δ * (δ - α) - 2 * (q T₁ - q T₂) * Real.cos Δ * h =
        Real.cos Δ * (δ - α - 2 * (q T₁ - q T₂) * h) := by ring
    rw [h_eq, abs_mul]
    have h_anti_nn : 0 ≤ |δ - α - 2 * (q T₁ - q T₂) * h| := abs_nonneg _
    calc |Real.cos Δ| * |δ - α - 2 * (q T₁ - q T₂) * h|
        ≤ 1 * |δ - α - 2 * (q T₁ - q T₂) * h| :=
          mul_le_mul_of_nonneg_right h_cos_le h_anti_nn
      _ ≤ 1 * (K_anti * |h|^3) :=
          mul_le_mul_of_nonneg_left h_δα_lin (by norm_num)
      _ = K_anti * |h|^3 := by ring
  have h_cos_γβ : |Real.cos Δ * (γ - β) - 2 * (q T₁ + q T₂) * Real.cos Δ * h| ≤
      K_anti * |h|^3 := by
    have h_eq : Real.cos Δ * (γ - β) - 2 * (q T₁ + q T₂) * Real.cos Δ * h =
        Real.cos Δ * (γ - β - 2 * (q T₁ + q T₂) * h) := by ring
    rw [h_eq, abs_mul]
    have h_anti_nn : 0 ≤ |γ - β - 2 * (q T₁ + q T₂) * h| := abs_nonneg _
    calc |Real.cos Δ| * |γ - β - 2 * (q T₁ + q T₂) * h|
        ≤ 1 * |γ - β - 2 * (q T₁ + q T₂) * h| :=
          mul_le_mul_of_nonneg_right h_cos_le h_anti_nn
      _ ≤ 1 * (K_anti * |h|^3) :=
          mul_le_mul_of_nonneg_left h_βγ_lin (by norm_num)
      _ = K_anti * |h|^3 := by ring
  -- Main bound 1: |sin δ - sin α - 2(q₁-q₂) cos Δ h| ≤ M h³
  have h_main_αδ : |Real.sin δ - Real.sin α -
      2 * (q T₁ - q T₂) * Real.cos Δ * h| ≤
      (M_lin^3 / 3 + K_anti + K_sym * M_lin) * |h|^3 := by
    have h_combined :
        Real.sin δ - Real.sin α - 2 * (q T₁ - q T₂) * Real.cos Δ * h =
        (Real.sin δ - (Real.sin Δ + Real.cos Δ * (δ - Δ) -
          Real.sin Δ * (δ - Δ)^2 / 2)) -
        (Real.sin α - (Real.sin Δ + Real.cos Δ * (α - Δ) -
          Real.sin Δ * (α - Δ)^2 / 2)) +
        (Real.cos Δ * (δ - α) - 2 * (q T₁ - q T₂) * Real.cos Δ * h) -
        Real.sin Δ * ((δ - Δ)^2 - (α - Δ)^2) / 2 := by ring
    -- Use triangle: |R_δ - R_α + S - C| ≤ |R_δ| + |R_α| + |S| + |C|
    set Rδ := Real.sin δ - (Real.sin Δ + Real.cos Δ * (δ - Δ) -
                  Real.sin Δ * (δ - Δ)^2 / 2) with hRδ_def
    set Rα := Real.sin α - (Real.sin Δ + Real.cos Δ * (α - Δ) -
                  Real.sin Δ * (α - Δ)^2 / 2) with hRα_def
    set S := Real.cos Δ * (δ - α) - 2 * (q T₁ - q T₂) * Real.cos Δ * h with hS_def
    set C := Real.sin Δ * ((δ - Δ)^2 - (α - Δ)^2) / 2 with hC_def
    have h_tri : |Rδ - Rα + S - C| ≤ |Rδ| + |Rα| + |S| + |C| := by
      have h1 : |Rδ - Rα + S - C| ≤ |Rδ - Rα + S| + |C| := abs_sub _ _
      have h2 : |Rδ - Rα + S| ≤ |Rδ - Rα| + |S| := abs_add_le _ _
      have h3 : |Rδ - Rα| ≤ |Rδ| + |Rα| := abs_sub _ _
      linarith
    calc |Real.sin δ - Real.sin α - 2 * (q T₁ - q T₂) * Real.cos Δ * h|
        = |Rδ - Rα + S - C| := by rw [h_combined]
      _ ≤ |Rδ| + |Rα| + |S| + |C| := h_tri
      _ ≤ |δ - Δ|^3 / 6 + |α - Δ|^3 / 6 +
          K_anti * |h|^3 + K_sym * M_lin * |h|^3 := by
          linarith [h_sin_δ_cub, h_sin_α_cub, h_cos_δα, h_sin_Δ_sq_diff_αδ]
      _ ≤ M_lin^3 * |h|^3 / 6 + M_lin^3 * |h|^3 / 6 +
          K_anti * |h|^3 + K_sym * M_lin * |h|^3 := by linarith
      _ = (M_lin^3 / 3 + K_anti + K_sym * M_lin) * |h|^3 := by ring
  -- Main bound 2: |sin β - sin γ + 2(q₁+q₂) cos Δ h| ≤ M h³
  have h_main_βγ : |Real.sin β - Real.sin γ +
      2 * (q T₁ + q T₂) * Real.cos Δ * h| ≤
      (M_lin^3 / 3 + K_anti + K_sym * M_lin) * |h|^3 := by
    -- sin β - sin γ + ... = -(sin γ - sin β - 2(q₁+q₂) cos Δ h) and the analysis
    -- mirrors the αδ pair using h_cos_γβ for the (γ-β) part.
    have h_combined :
        Real.sin β - Real.sin γ + 2 * (q T₁ + q T₂) * Real.cos Δ * h =
        (Real.sin β - (Real.sin Δ + Real.cos Δ * (β - Δ) -
          Real.sin Δ * (β - Δ)^2 / 2)) -
        (Real.sin γ - (Real.sin Δ + Real.cos Δ * (γ - Δ) -
          Real.sin Δ * (γ - Δ)^2 / 2)) -
        (Real.cos Δ * (γ - β) - 2 * (q T₁ + q T₂) * Real.cos Δ * h) -
        Real.sin Δ * ((β - Δ)^2 - (γ - Δ)^2) / 2 := by ring
    -- Use triangle: |R_β - R_γ - S - C| ≤ |R_β| + |R_γ| + |S| + |C|
    set Rβ := Real.sin β - (Real.sin Δ + Real.cos Δ * (β - Δ) -
                  Real.sin Δ * (β - Δ)^2 / 2) with hRβ_def
    set Rγ := Real.sin γ - (Real.sin Δ + Real.cos Δ * (γ - Δ) -
                  Real.sin Δ * (γ - Δ)^2 / 2) with hRγ_def
    set S := Real.cos Δ * (γ - β) - 2 * (q T₁ + q T₂) * Real.cos Δ * h with hS_def
    set C := Real.sin Δ * ((β - Δ)^2 - (γ - Δ)^2) / 2 with hC_def
    have h_tri : |Rβ - Rγ - S - C| ≤ |Rβ| + |Rγ| + |S| + |C| := by
      have h1 : |Rβ - Rγ - S - C| ≤ |Rβ - Rγ - S| + |C| := abs_sub _ _
      have h2 : |Rβ - Rγ - S| ≤ |Rβ - Rγ| + |S| := abs_sub _ _
      have h3 : |Rβ - Rγ| ≤ |Rβ| + |Rγ| := abs_sub _ _
      linarith
    calc |Real.sin β - Real.sin γ + 2 * (q T₁ + q T₂) * Real.cos Δ * h|
        = |Rβ - Rγ - S - C| := by rw [h_combined]
      _ ≤ |Rβ| + |Rγ| + |S| + |C| := h_tri
      _ ≤ |β - Δ|^3 / 6 + |γ - Δ|^3 / 6 +
          K_anti * |h|^3 + K_sym * M_lin * |h|^3 := by
          linarith [h_sin_β_cub, h_sin_γ_cub, h_cos_γβ, h_sin_Δ_sq_diff_βγ]
      _ ≤ M_lin^3 * |h|^3 / 6 + M_lin^3 * |h|^3 / 6 +
          K_anti * |h|^3 + K_sym * M_lin * |h|^3 := by linarith
      _ = (M_lin^3 / 3 + K_anti + K_sym * M_lin) * |h|^3 := by ring
  exact ⟨h_main_αδ, h_main_βγ⟩

/-- Anti-difference of sines bound for the cross block:
    `|sin β − sin γ| ≤ M · |h|` (linear in `h`). -/
private lemma cross_sin_pair_anti_bound (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, |h| ≤ R →
      |Real.sin (theta (T₁ - h) - theta (T₂ + h)) -
       Real.sin (theta (T₁ + h) - theta (T₂ - h))| ≤ M * |h| := by
  obtain ⟨K_anti_1, hK_anti_1_nn, hK_anti_1⟩ := theta_anti_sym_diff_bound T₁ R hR
  obtain ⟨K_anti_2, hK_anti_2_nn, hK_anti_2⟩ := theta_anti_sym_diff_bound T₂ R hR
  refine ⟨(K_anti_1 + K_anti_2) * R + 2 * (|q T₁| + |q T₂|), by positivity, ?_⟩
  intro h hh
  set β := theta (T₁ - h) - theta (T₂ + h) with hβ_def
  set γ := theta (T₁ + h) - theta (T₂ - h) with hγ_def
  -- |sin β - sin γ| ≤ |β - γ|
  have h_lipschitz : |Real.sin β - Real.sin γ| ≤ |β - γ| :=
    Real.abs_sin_sub_sin_le β γ
  -- |β - γ| ≤ |θ(T₁+h) - θ(T₁-h)| + |θ(T₂+h) - θ(T₂-h)|
  have h_β_minus_γ : β - γ = -(theta (T₁ + h) - theta (T₁ - h)) -
      (theta (T₂ + h) - theta (T₂ - h)) := by simp [hβ_def, hγ_def]; ring
  -- Bounds on each of |θ(T+h) - θ(T-h)|.
  have h_T₁_diff : |theta (T₁ + h) - theta (T₁ - h)| ≤
      K_anti_1 * h^2 + 2 * |q T₁| * |h| := by
    have h_aux : theta (T₁ + h) - theta (T₁ - h) =
        (theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h) + 2 * q T₁ * h := by ring
    calc |theta (T₁ + h) - theta (T₁ - h)|
        = |(theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h) + 2 * q T₁ * h| := by
          rw [← h_aux]
      _ ≤ |theta (T₁ + h) - theta (T₁ - h) - 2 * q T₁ * h| + |2 * q T₁ * h| := abs_add_le _ _
      _ ≤ K_anti_1 * h^2 + 2 * |q T₁| * |h| := by
          have := hK_anti_1 h hh
          have h_abs : |2 * q T₁ * h| = 2 * |q T₁| * |h| := by
            rw [abs_mul, abs_mul, abs_of_pos (by norm_num : (2:ℝ) > 0)]
          linarith
  have h_T₂_diff : |theta (T₂ + h) - theta (T₂ - h)| ≤
      K_anti_2 * h^2 + 2 * |q T₂| * |h| := by
    have h_aux : theta (T₂ + h) - theta (T₂ - h) =
        (theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h) + 2 * q T₂ * h := by ring
    calc |theta (T₂ + h) - theta (T₂ - h)|
        = |(theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h) + 2 * q T₂ * h| := by
          rw [← h_aux]
      _ ≤ |theta (T₂ + h) - theta (T₂ - h) - 2 * q T₂ * h| + |2 * q T₂ * h| := abs_add_le _ _
      _ ≤ K_anti_2 * h^2 + 2 * |q T₂| * |h| := by
          have := hK_anti_2 h hh
          have h_abs : |2 * q T₂ * h| = 2 * |q T₂| * |h| := by
            rw [abs_mul, abs_mul, abs_of_pos (by norm_num : (2:ℝ) > 0)]
          linarith
  -- Combine and convert h² ≤ R · |h|
  have h_h_abs_nn : 0 ≤ |h| := abs_nonneg h
  have h_h_sq_le_R_abs : h^2 ≤ R * |h| := by
    have h_eq : h^2 = |h| * |h| := by rw [show |h| * |h| = |h|^2 from (sq |h|).symm, sq_abs]
    rw [h_eq]
    exact mul_le_mul_of_nonneg_right hh h_h_abs_nn
  calc |Real.sin β - Real.sin γ|
      ≤ |β - γ| := h_lipschitz
    _ = |-(theta (T₁ + h) - theta (T₁ - h)) - (theta (T₂ + h) - theta (T₂ - h))| := by
        rw [h_β_minus_γ]
    _ ≤ |-(theta (T₁ + h) - theta (T₁ - h))| + |theta (T₂ + h) - theta (T₂ - h)| :=
        abs_sub _ _
    _ = |theta (T₁ + h) - theta (T₁ - h)| + |theta (T₂ + h) - theta (T₂ - h)| := by
        rw [abs_neg]
    _ ≤ (K_anti_1 * h^2 + 2 * |q T₁| * |h|) + (K_anti_2 * h^2 + 2 * |q T₂| * |h|) := by linarith
    _ = (K_anti_1 + K_anti_2) * h^2 + 2 * (|q T₁| + |q T₂|) * |h| := by ring
    _ ≤ (K_anti_1 + K_anti_2) * (R * |h|) + 2 * (|q T₁| + |q T₂|) * |h| := by
        have h_ge : 0 ≤ K_anti_1 + K_anti_2 := by linarith
        have : (K_anti_1 + K_anti_2) * h^2 ≤ (K_anti_1 + K_anti_2) * (R * |h|) :=
          mul_le_mul_of_nonneg_left h_h_sq_le_R_abs h_ge
        linarith
    _ = ((K_anti_1 + K_anti_2) * R + 2 * (|q T₁| + |q T₂|)) * |h| := by ring

/-- Lower bound on `s² - 4h²` for `h ∈ (0, |s|/3]`. -/
private lemma cross_denom_sq_lower (s h : ℝ) (hs_ne : s ≠ 0)
    (h_pos : 0 < h) (h_le : h ≤ |s| / 3) :
    5 * s^2 / 9 ≤ s^2 - 4 * h^2 ∧ 0 < s^2 - 4 * h^2 := by
  have hs_abs_pos : 0 < |s| := abs_pos.mpr hs_ne
  have hs_sq_pos : 0 < s^2 := by
    have : s^2 = |s|^2 := (sq_abs s).symm
    rw [this]; positivity
  have h_h_nn : 0 ≤ h := h_pos.le
  have h_h_sq_le : h^2 ≤ s^2 / 9 := by
    have h_lhs : h * h ≤ (|s| / 3) * (|s| / 3) :=
      mul_le_mul h_le h_le h_h_nn (by linarith)
    have h_rhs_eq : (|s| / 3) * (|s| / 3) = |s|^2 / 9 := by ring
    have h_abs_sq : |s|^2 = s^2 := sq_abs s
    have h_h_sq : h * h = h^2 := (sq h).symm
    linarith [h_lhs, h_rhs_eq, h_abs_sq, h_h_sq]
  refine ⟨?_, ?_⟩
  · linarith
  · linarith

set_option maxHeartbeats 1200000 in
/-- Bound on entry `(0, 0)` of `P_h C_h(T₁, T₂) P_h^⊤ − (1/π) N₁₂(T₁, T₂)`
    for `h ∈ (0, |s|/3]`. -/
private lemma cross_rate_bound_00 (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ |T₁ - T₂| / 3 →
      |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 0| ≤ M * h^2 := by
  set s : ℝ := T₁ - T₂ with hs_def
  set R : ℝ := |s| / 3 with hR_def
  have hs_ne : s ≠ 0 := sub_ne_zero.mpr hT
  have hs_abs_pos : 0 < |s| := abs_pos.mpr hs_ne
  have hR_pos : 0 < R := by show 0 < |s| / 3; linarith
  have hs_sq_pos : 0 < s^2 := by have : s^2 = |s|^2 := (sq_abs s).symm; rw [this]; positivity
  have hs_cube_pos : 0 < |s|^3 := by positivity
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  obtain ⟨M_a, hM_a_nn, hM_a⟩ := cross_sin_pair_sym_bound T₁ T₂ R hR_pos
  obtain ⟨M_b, hM_b_nn, hM_b⟩ := cross_sin_pair_anti_bound T₁ T₂ R hR_pos
  set M : ℝ := (18 * s^2 * M_a + 18 * |s| * M_b + 72) / (10 * Real.pi * |s|^3) with hM_def
  have hM_nn : 0 ≤ M := by
    apply div_nonneg
    · have h_term1_nn : 0 ≤ 18 * s^2 * M_a := by positivity
      have h_term2_nn : 0 ≤ 18 * |s| * M_b := by positivity
      linarith
    · positivity
  refine ⟨M, hM_nn, ?_⟩
  intro h h_pos h_le
  have h_le_R : h ≤ R := by show h ≤ |s| / 3; exact h_le
  have h_abs_le : |h| ≤ R := by rw [abs_of_pos h_pos]; exact h_le_R
  obtain ⟨h_pK_00, h_pK_01, h_pK_10, h_pK_11⟩ :=
    crossBlock_apply T₁ T₂ h hT h_pos h_le
  obtain ⟨h_N_00, h_N_01, h_N_10, h_N_11⟩ := N12_smul_apply T₁ T₂ hT
  -- Apply (P · C · P^T)(0,0) = (a+b+c+d)/2
  have h_jet_00 : (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 0 =
      (Real.sin (theta (T₁ - h) - theta (T₂ - h)) / (Real.pi * s) +
       Real.sin (theta (T₁ - h) - theta (T₂ + h)) / (Real.pi * (s - 2 * h)) +
       Real.sin (theta (T₁ + h) - theta (T₂ - h)) / (Real.pi * (s + 2 * h)) +
       Real.sin (theta (T₁ + h) - theta (T₂ + h)) / (Real.pi * s)) / 2 := by
    rw [jet_cross_matrix_apply_00 T₁ T₂ h hT h_pos h_le]
    rw [h_pK_00, h_pK_01, h_pK_10, h_pK_11]
  -- The target.
  have h_n_00 : ((1 / Real.pi) • N12 T₁ T₂) 0 0 =
      2 * Real.sin (theta T₁ - theta T₂) / (Real.pi * s) := h_N_00
  -- Algebraic constants/sin values.
  set Δ := theta T₁ - theta T₂ with hΔ_def
  set α := theta (T₁ - h) - theta (T₂ - h) with hα_def
  set β := theta (T₁ - h) - theta (T₂ + h) with hβ_def
  set γ := theta (T₁ + h) - theta (T₂ - h) with hγ_def
  set δ := theta (T₁ + h) - theta (T₂ + h) with hδ_def
  -- Get the sin pair sym/anti bounds.
  obtain ⟨h_sym_αδ, h_sym_βγ⟩ := hM_a h h_abs_le
  have h_anti_βγ := hM_b h h_abs_le
  rw [show |h| = h from abs_of_pos h_pos] at h_anti_βγ
  -- Denominator bounds.
  obtain ⟨h_denom_lower, h_denom_pos⟩ := cross_denom_sq_lower s h hs_ne h_pos h_le
  -- Useful: |s² - 4h²| ≤ s²
  have h_denom_upper : s^2 - 4 * h^2 ≤ s^2 := by nlinarith [sq_nonneg h]
  have h_denom_abs : |s^2 - 4 * h^2| = s^2 - 4 * h^2 := abs_of_pos h_denom_pos
  have hs_2h_ne : s + 2 * h ≠ 0 := by
    have : (s - 2 * h) * (s + 2 * h) = s^2 - 4 * h^2 := by ring
    intro heq
    have : s^2 - 4 * h^2 = 0 := by rw [← this, heq]; ring
    linarith
  have hs_2h_neg_ne : s - 2 * h ≠ 0 := by
    intro heq
    have : (s - 2 * h) * (s + 2 * h) = s^2 - 4 * h^2 := by ring
    have : s^2 - 4 * h^2 = 0 := by rw [← this, heq]; ring
    linarith
  -- Compute the difference.
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  have h_denom_sq_ne : s^2 - 4 * h^2 ≠ 0 := h_denom_pos.ne'
  -- Algebraic identity.
  have h_identity :
      (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 0 =
      ((s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
       s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ) +
       2 * s * h * (Real.sin β - Real.sin γ) +
       8 * h^2 * Real.sin Δ) /
       (2 * Real.pi * s * (s^2 - 4 * h^2)) := by
    rw [Matrix.sub_apply, h_jet_00, h_n_00]
    have h_denom_prod_eq : s^2 - 4 * h^2 = (s - 2 * h) * (s + 2 * h) := by ring
    rw [h_denom_prod_eq]
    field_simp
    ring
  rw [h_identity]
  rw [abs_div]
  -- Bound the absolute value of the denominator.
  have h_denom_full_pos : 0 < 2 * Real.pi * s * (s^2 - 4 * h^2) ∨
                         2 * Real.pi * s * (s^2 - 4 * h^2) < 0 := by
    rcases lt_or_gt_of_ne hs_ne with hslt | hsgt
    · right
      have h_neg : 2 * Real.pi * s < 0 := by
        have : 2 * Real.pi > 0 := by positivity
        nlinarith
      nlinarith
    · left
      have h_pos2 : 2 * Real.pi * s > 0 := by positivity
      nlinarith
  have h_denom_abs_full : |2 * Real.pi * s * (s^2 - 4 * h^2)| =
      2 * Real.pi * |s| * (s^2 - 4 * h^2) := by
    rw [show 2 * Real.pi * s * (s^2 - 4 * h^2) =
        (2 * Real.pi) * s * (s^2 - 4 * h^2) from by ring]
    rw [abs_mul, abs_mul]
    rw [abs_of_pos (by positivity : 0 < 2 * Real.pi)]
    rw [abs_of_pos h_denom_pos]
  rw [h_denom_abs_full]
  -- Bound numerator.
  have h_num_bound :
      |(s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
       s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ) +
       2 * s * h * (Real.sin β - Real.sin γ) +
       8 * h^2 * Real.sin Δ| ≤
      (2 * s^2 * M_a + 2 * |s| * M_b + 8) * h^2 := by
    have h_t1 : |(s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ)| ≤
        s^2 * M_a * h^2 := by
      rw [abs_mul]
      rw [h_denom_abs]
      calc (s^2 - 4 * h^2) * |Real.sin α + Real.sin δ - 2 * Real.sin Δ|
          ≤ s^2 * |Real.sin α + Real.sin δ - 2 * Real.sin Δ| := by
            apply mul_le_mul_of_nonneg_right h_denom_upper (abs_nonneg _)
        _ ≤ s^2 * (M_a * h^2) := by
            apply mul_le_mul_of_nonneg_left h_sym_αδ (le_of_lt hs_sq_pos)
        _ = s^2 * M_a * h^2 := by ring
    have h_t2 : |s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ)| ≤
        s^2 * M_a * h^2 := by
      rw [abs_mul]
      have h_s2_abs : |s^2| = s^2 := abs_of_pos hs_sq_pos
      rw [h_s2_abs]
      calc s^2 * |Real.sin β + Real.sin γ - 2 * Real.sin Δ|
          ≤ s^2 * (M_a * h^2) := mul_le_mul_of_nonneg_left h_sym_βγ (le_of_lt hs_sq_pos)
        _ = s^2 * M_a * h^2 := by ring
    have h_t3 : |2 * s * h * (Real.sin β - Real.sin γ)| ≤
        2 * |s| * M_b * h^2 := by
      rw [abs_mul, abs_mul, abs_mul]
      rw [show |(2 : ℝ)| = 2 from by norm_num, abs_of_pos h_pos]
      calc 2 * |s| * h * |Real.sin β - Real.sin γ|
          ≤ 2 * |s| * h * (M_b * h) := by
            apply mul_le_mul_of_nonneg_left h_anti_βγ (by positivity)
        _ = 2 * |s| * M_b * h^2 := by ring
    have h_t4 : |8 * h^2 * Real.sin Δ| ≤ 8 * h^2 := by
      rw [abs_mul, abs_mul]
      rw [show |(8 : ℝ)| = 8 from by norm_num]
      have h_h_sq_abs : |h^2| = h^2 := abs_of_nonneg (sq_nonneg h)
      rw [h_h_sq_abs]
      calc 8 * h^2 * |Real.sin Δ|
          ≤ 8 * h^2 * 1 := by
            apply mul_le_mul_of_nonneg_left (Real.abs_sin_le_one Δ) (by positivity)
        _ = 8 * h^2 := by ring
    calc |(s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
         s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ) +
         2 * s * h * (Real.sin β - Real.sin γ) +
         8 * h^2 * Real.sin Δ|
        ≤ |(s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ)| +
          |s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ)| +
          |2 * s * h * (Real.sin β - Real.sin γ)| +
          |8 * h^2 * Real.sin Δ| := by
          have h₁ := abs_add_le
            ((s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
             s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ) +
             2 * s * h * (Real.sin β - Real.sin γ))
            (8 * h^2 * Real.sin Δ)
          have h₂ := abs_add_le
            ((s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
             s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ))
            (2 * s * h * (Real.sin β - Real.sin γ))
          have h₃ := abs_add_le
            ((s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ))
            (s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ))
          linarith
      _ ≤ s^2 * M_a * h^2 + s^2 * M_a * h^2 + 2 * |s| * M_b * h^2 + 8 * h^2 := by linarith
      _ = (2 * s^2 * M_a + 2 * |s| * M_b + 8) * h^2 := by ring
  -- Final calculation.
  rw [div_le_iff₀ (by positivity : 0 < 2 * Real.pi * |s| * (s^2 - 4 * h^2))]
  calc |(s^2 - 4 * h^2) * (Real.sin α + Real.sin δ - 2 * Real.sin Δ) +
        s^2 * (Real.sin β + Real.sin γ - 2 * Real.sin Δ) +
        2 * s * h * (Real.sin β - Real.sin γ) +
        8 * h^2 * Real.sin Δ|
      ≤ (2 * s^2 * M_a + 2 * |s| * M_b + 8) * h^2 := h_num_bound
    _ ≤ M * h^2 * (2 * Real.pi * |s| * (s^2 - 4 * h^2)) := by
        -- M * (2π|s|·(s²-4h²)) ≥ M · 2π|s| · 5s²/9 = 10π|s|³ M / 9 needed ≥ (2s²M_a + 2|s|M_b + 8)
        -- Recall M = (18 s² M_a + 18 |s| M_b + 72) / (10 π |s|³).
        -- Then 10π|s|³ M / 9 = (10π|s|³)/9 · (18s²M_a + 18|s|M_b + 72)/(10π|s|³)
        --                   = (18s²M_a + 18|s|M_b + 72)/9
        --                   = 2 s² M_a + 2|s| M_b + 8.
        have h_h_sq_nn : 0 ≤ h^2 := sq_nonneg h
        have hM_eq : M * (2 * Real.pi * |s| * (s^2 - 4 * h^2)) =
            (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (s^2 - 4 * h^2) /
              (5 * |s|^2) := by
          show ((18 * s^2 * M_a + 18 * |s| * M_b + 72) /
                (10 * Real.pi * |s|^3)) * (2 * Real.pi * |s| * (s^2 - 4 * h^2)) = _
          rw [show |s|^3 = |s| * |s|^2 from by ring]
          field_simp
          ring
        have hM_factor :
            M * h^2 * (2 * Real.pi * |s| * (s^2 - 4 * h^2)) =
            M * (2 * Real.pi * |s| * (s^2 - 4 * h^2)) * h^2 := by ring
        rw [hM_factor, hM_eq]
        -- Need: (2s² M_a + 2|s| M_b + 8) ≤ (18s²M_a + 18|s|M_b + 72)(s²-4h²)/(5|s|²)
        have h_step1 :
            (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (s^2 - 4 * h^2) ≥
            (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (5 * s^2 / 9) := by
          have h_factor_nn : 0 ≤ 18 * s^2 * M_a + 18 * |s| * M_b + 72 := by positivity
          exact mul_le_mul_of_nonneg_left h_denom_lower h_factor_nn
        have h_step2 :
            (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (5 * s^2 / 9) / (5 * |s|^2) =
            (2 * s^2 * M_a + 2 * |s| * M_b + 8) := by
          have h_abs_sq : |s|^2 = s^2 := sq_abs s
          rw [h_abs_sq]
          field_simp
          ring
        have h_step3 :
            (2 * s^2 * M_a + 2 * |s| * M_b + 8) ≤
            (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (s^2 - 4 * h^2) / (5 * |s|^2) := by
          rw [show (2 * s^2 * M_a + 2 * |s| * M_b + 8) =
              (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (5 * s^2 / 9) / (5 * |s|^2) from h_step2.symm]
          have h_5s2_pos : 0 ≤ 5 * |s|^2 := by
            have : |s|^2 = s^2 := sq_abs s
            rw [this]; linarith
          exact div_le_div_of_nonneg_right h_step1 h_5s2_pos
        calc (2 * s^2 * M_a + 2 * |s| * M_b + 8) * h^2
            ≤ (18 * s^2 * M_a + 18 * |s| * M_b + 72) * (s^2 - 4 * h^2) / (5 * |s|^2) * h^2 := by
              exact mul_le_mul_of_nonneg_right h_step3 h_h_sq_nn

/-- Symmetric difference bound for theta at order 3:
    `|θ(T+h) + θ(T-h) - 2θT - qPrime T h²| ≤ 2 K |h|⁴`.
    Used for precise h² leading-term tracking in cross_rate_bound_11. -/
private lemma theta_sym_sum_bound_h2 (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) + theta (T - h) - 2 * theta T - qPrime T * h^2| ≤
        K * |h|^4 := by
  obtain ⟨K_3, hK_3_nn, hK_3⟩ := theta_taylor_remainder_3_on T R hR
  refine ⟨2 * K_3, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  have h_taylor_p := hK_3 h hh
  have h_taylor_m := hK_3 (-h) h_neg_abs
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_taylor_m
  have h_neg_sq : (-h)^2 = h^2 := by ring
  have h_neg_cube : (-h)^3 = -(h^3) := by ring
  rw [h_neg_sq, h_neg_cube] at h_taylor_m
  have h_neg_abs_4 : |(-h)|^4 = |h|^4 := by rw [abs_neg]
  rw [h_neg_abs_4] at h_taylor_m
  have h_split : theta (T + h) + theta (T - h) - 2 * theta T - qPrime T * h^2 =
      (theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
        qDoublePrime T * h^3 / 6)) +
      (theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2 +
        qDoublePrime T * (-(h^3)) / 6)) := by ring
  calc |theta (T + h) + theta (T - h) - 2 * theta T - qPrime T * h^2|
      = |(theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
            qDoublePrime T * h^3 / 6)) +
         (theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2 +
            qDoublePrime T * (-(h^3)) / 6))| := by rw [h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
            qDoublePrime T * h^3 / 6)| +
        |theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2 +
            qDoublePrime T * (-(h^3)) / 6)| := abs_add_le _ _
    _ ≤ K_3 * |h|^4 + K_3 * |h|^4 := by linarith
    _ = 2 * K_3 * |h|^4 := by ring

/-- Cross-block precise sym sum bound at h² leading order:
    `|(α + δ - 2Δ) - (qPrime T₁ - qPrime T₂) h²| ≤ K |h|⁴`
    and same for `(β + γ - 2Δ)`.  Critical for `cross_rate_bound_11`. -/
private lemma cross_theta_sym_sum_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |(theta (T₁ - h) - theta (T₂ - h)) +
       (theta (T₁ + h) - theta (T₂ + h)) -
       2 * (theta T₁ - theta T₂) -
       (qPrime T₁ - qPrime T₂) * h^2| ≤ K * |h|^4 ∧
      |(theta (T₁ - h) - theta (T₂ + h)) +
       (theta (T₁ + h) - theta (T₂ - h)) -
       2 * (theta T₁ - theta T₂) -
       (qPrime T₁ - qPrime T₂) * h^2| ≤ K * |h|^4 := by
  obtain ⟨K_1, hK_1_nn, hK_1⟩ := theta_sym_sum_bound_h2 T₁ R hR
  obtain ⟨K_2, hK_2_nn, hK_2⟩ := theta_sym_sum_bound_h2 T₂ R hR
  refine ⟨K_1 + K_2, by positivity, ?_⟩
  intro h hh
  have h1 := hK_1 h hh
  have h2 := hK_2 h hh
  refine ⟨?_, ?_⟩
  · -- α + δ - 2Δ = (θ(T₁-h) - θ(T₂-h)) + (θ(T₁+h) - θ(T₂+h)) - 2(θT₁ - θT₂)
    -- = (θ(T₁+h) + θ(T₁-h) - 2θT₁) - (θ(T₂+h) + θ(T₂-h) - 2θT₂)
    have h_split :
        (theta (T₁ - h) - theta (T₂ - h)) + (theta (T₁ + h) - theta (T₂ + h)) -
          2 * (theta T₁ - theta T₂) - (qPrime T₁ - qPrime T₂) * h^2 =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁ - qPrime T₁ * h^2) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂ - qPrime T₂ * h^2) := by
      ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁ - qPrime T₁ * h^2| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂ - qPrime T₂ * h^2| := abs_sub _ _
      _ ≤ K_1 * |h|^4 + K_2 * |h|^4 := by linarith
      _ = (K_1 + K_2) * |h|^4 := by ring
  · -- β + γ - 2Δ has the same form: same algebraic simplification.
    have h_split :
        (theta (T₁ - h) - theta (T₂ + h)) + (theta (T₁ + h) - theta (T₂ - h)) -
          2 * (theta T₁ - theta T₂) - (qPrime T₁ - qPrime T₂) * h^2 =
        (theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁ - qPrime T₁ * h^2) -
        (theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂ - qPrime T₂ * h^2) := by
      ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) + theta (T₁ - h) - 2 * theta T₁ - qPrime T₁ * h^2| +
          |theta (T₂ + h) + theta (T₂ - h) - 2 * theta T₂ - qPrime T₂ * h^2| := abs_sub _ _
      _ ≤ K_1 * |h|^4 + K_2 * |h|^4 := by linarith
      _ = (K_1 + K_2) * |h|^4 := by ring

/-- Cross-block angle precise linear approximation:
    `|(α - Δ) + (q T₁ - q T₂) h| ≤ K h²` (residual after subtracting linear h leading).
    Similarly for β, γ, δ.  Foundation for `cross_rate_bound_11`. -/
private lemma cross_angle_lin_bound_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |(theta (T₁ - h) - theta (T₂ - h)) - (theta T₁ - theta T₂) +
        (q T₁ - q T₂) * h| ≤ K * h^2 ∧
      |(theta (T₁ + h) - theta (T₂ + h)) - (theta T₁ - theta T₂) -
        (q T₁ - q T₂) * h| ≤ K * h^2 ∧
      |(theta (T₁ - h) - theta (T₂ + h)) - (theta T₁ - theta T₂) +
        (q T₁ + q T₂) * h| ≤ K * h^2 ∧
      |(theta (T₁ + h) - theta (T₂ - h)) - (theta T₁ - theta T₂) -
        (q T₁ + q T₂) * h| ≤ K * h^2 := by
  obtain ⟨K_1, hK_1_nn, hK_1⟩ := theta_taylor_remainder_1_on T₁ R hR
  obtain ⟨K_2, hK_2_nn, hK_2⟩ := theta_taylor_remainder_1_on T₂ R hR
  refine ⟨K_1 + K_2, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  -- For each T, theta(T+h) - θT - qT·h is bounded by K·h².
  have hR_T₁_p : |theta (T₁ + h) - (theta T₁ + q T₁ * h)| ≤ K_1 * h^2 := hK_1 h hh
  have hR_T₁_m_orig : |theta (T₁ + (-h)) - (theta T₁ + q T₁ * (-h))| ≤ K_1 * (-h)^2 :=
    hK_1 (-h) h_neg_abs
  have h_neg_sq : (-h)^2 = h^2 := by ring
  have hR_T₁_m : |theta (T₁ - h) - (theta T₁ + q T₁ * (-h))| ≤ K_1 * h^2 := by
    have : theta (T₁ + (-h)) = theta (T₁ - h) := by ring_nf
    rw [this, h_neg_sq] at hR_T₁_m_orig
    exact hR_T₁_m_orig
  have hR_T₂_p : |theta (T₂ + h) - (theta T₂ + q T₂ * h)| ≤ K_2 * h^2 := hK_2 h hh
  have hR_T₂_m_orig : |theta (T₂ + (-h)) - (theta T₂ + q T₂ * (-h))| ≤ K_2 * (-h)^2 :=
    hK_2 (-h) h_neg_abs
  have hR_T₂_m : |theta (T₂ - h) - (theta T₂ + q T₂ * (-h))| ≤ K_2 * h^2 := by
    have : theta (T₂ + (-h)) = theta (T₂ - h) := by ring_nf
    rw [this, h_neg_sq] at hR_T₂_m_orig
    exact hR_T₂_m_orig
  refine ⟨?_, ?_, ?_, ?_⟩
  · -- α: (θ(T₁-h) - θT₁ + qT₁ h) - (θ(T₂-h) - θT₂ + qT₂ h)
    have h_split :
        (theta (T₁ - h) - theta (T₂ - h)) - (theta T₁ - theta T₂) +
          (q T₁ - q T₂) * h =
        (theta (T₁ - h) - (theta T₁ + q T₁ * (-h))) -
        (theta (T₂ - h) - (theta T₂ + q T₂ * (-h))) := by ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ - h) - (theta T₁ + q T₁ * (-h))| +
          |theta (T₂ - h) - (theta T₂ + q T₂ * (-h))| := abs_sub _ _
      _ ≤ K_1 * h^2 + K_2 * h^2 := by linarith
      _ = (K_1 + K_2) * h^2 := by ring
  · -- δ: (θ(T₁+h) - θT₁ - qT₁ h) - (θ(T₂+h) - θT₂ - qT₂ h)
    have h_split :
        (theta (T₁ + h) - theta (T₂ + h)) - (theta T₁ - theta T₂) -
          (q T₁ - q T₂) * h =
        (theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
        (theta (T₂ + h) - (theta T₂ + q T₂ * h)) := by ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - (theta T₁ + q T₁ * h)| +
          |theta (T₂ + h) - (theta T₂ + q T₂ * h)| := abs_sub _ _
      _ ≤ K_1 * h^2 + K_2 * h^2 := by linarith
      _ = (K_1 + K_2) * h^2 := by ring
  · -- β: (θ(T₁-h) - θT₁ + qT₁ h) - (θ(T₂+h) - θT₂ - qT₂ h)
    have h_split :
        (theta (T₁ - h) - theta (T₂ + h)) - (theta T₁ - theta T₂) +
          (q T₁ + q T₂) * h =
        (theta (T₁ - h) - (theta T₁ + q T₁ * (-h))) -
        (theta (T₂ + h) - (theta T₂ + q T₂ * h)) := by ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ - h) - (theta T₁ + q T₁ * (-h))| +
          |theta (T₂ + h) - (theta T₂ + q T₂ * h)| := abs_sub _ _
      _ ≤ K_1 * h^2 + K_2 * h^2 := by linarith
      _ = (K_1 + K_2) * h^2 := by ring
  · -- γ: (θ(T₁+h) - θT₁ - qT₁ h) - (θ(T₂-h) - θT₂ + qT₂ h)
    have h_split :
        (theta (T₁ + h) - theta (T₂ - h)) - (theta T₁ - theta T₂) -
          (q T₁ + q T₂) * h =
        (theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
        (theta (T₂ - h) - (theta T₂ + q T₂ * (-h))) := by ring
    calc |_| = _ := by rw [h_split]
      _ ≤ |theta (T₁ + h) - (theta T₁ + q T₁ * h)| +
          |theta (T₂ - h) - (theta T₂ + q T₂ * (-h))| := abs_sub _ _
      _ ≤ K_1 * h^2 + K_2 * h^2 := by linarith
      _ = (K_1 + K_2) * h^2 := by ring

/-- Anti-sym diff bound at order 3 with cubic-remainder bound:
    `|R_T(h) - R_T(-h)| ≤ 2 K_2 |h|³` where R_T is the order-1 theta
    Taylor residual, using theta_taylor_remainder_2_on. -/
private lemma theta_R1_anti_diff_h3 (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |(theta (T + h) - (theta T + q T * h)) -
       (theta (T - h) - (theta T + q T * (-h)))| ≤ K * |h|^3 := by
  obtain ⟨K_2, hK_2_nn, hK_2⟩ := theta_taylor_remainder_2_on T R hR
  refine ⟨2 * K_2, by positivity, ?_⟩
  intro h hh
  have h_neg_abs : |(-h)| ≤ R := by rw [abs_neg]; exact hh
  have h_p := hK_2 h hh
  have h_m := hK_2 (-h) h_neg_abs
  -- Goal: |R_T(h) - R_T(-h)| ≤ 2 K_2 |h|³
  -- where R_T(h) = θ(T+h) - θT - qT h.
  -- The order-2 Taylor: θ(T+h) - (θT + qT h + qPrime T h²/2) = R'(h) where |R'(h)| ≤ K_2 |h|³.
  -- So R_T(h) = qPrime T h²/2 + R'(h).
  -- R_T(h) - R_T(-h) = qPrime T h²/2 + R'(h) - qPrime T (-h)²/2 - R'(-h)
  --                  = qPrime T h²/2 - qPrime T h²/2 + R'(h) - R'(-h)
  --                  = R'(h) - R'(-h)
  -- Bounded by 2 K_2 |h|³.
  have h_T_m : T + (-h) = T - h := by ring
  rw [h_T_m] at h_m
  have h_neg_sq : (-h)^2 = h^2 := by ring
  rw [h_neg_sq] at h_m
  have h_neg_abs_3 : |(-h)|^3 = |h|^3 := by rw [abs_neg]
  rw [h_neg_abs_3] at h_m
  have h_split :
      (theta (T + h) - (theta T + q T * h)) -
      (theta (T - h) - (theta T + q T * (-h))) =
      (theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)) -
      (theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2)) := by ring
  calc |_| = _ := by rw [h_split]
    _ ≤ |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)| +
        |theta (T - h) - (theta T + q T * (-h) + qPrime T * h^2 / 2)| := abs_sub _ _
    _ ≤ K_2 * |h|^3 + K_2 * |h|^3 := by linarith
    _ = 2 * K_2 * |h|^3 := by ring

/-- Cross-block squared-angle sum precise h² bound for αδ pair:
    `|((α-Δ)² + (δ-Δ)²) - 2(q T₁ - q T₂)² h²| ≤ K h⁴`. -/
private lemma cross_angle_sq_sum_αδ_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      let α := theta (T₁ - h) - theta (T₂ - h)
      let δ := theta (T₁ + h) - theta (T₂ + h)
      let Δ := theta T₁ - theta T₂
      |(α - Δ)^2 + (δ - Δ)^2 - 2 * (q T₁ - q T₂)^2 * h^2| ≤ K * h^4 := by
  obtain ⟨K_lin, hK_lin_nn, hK_lin⟩ := cross_angle_lin_bound_h2 T₁ T₂ R hR
  obtain ⟨K_anti_T₁, hK_anti_T₁_nn, hK_anti_T₁⟩ := theta_R1_anti_diff_h3 T₁ R hR
  obtain ⟨K_anti_T₂, hK_anti_T₂_nn, hK_anti_T₂⟩ := theta_R1_anti_diff_h3 T₂ R hR
  refine ⟨2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) + 2 * K_lin^2,
    by positivity, ?_⟩
  intro h hh
  simp only
  -- Define r_α := α - Δ + (q₁-q₂) h, r_δ := δ - Δ - (q₁-q₂) h.
  -- (α-Δ)² + (δ-Δ)² - 2(q₁-q₂)² h² = 2(q₁-q₂) h (r_δ - r_α) + r_α² + r_δ²
  set α := theta (T₁ - h) - theta (T₂ - h)
  set δ := theta (T₁ + h) - theta (T₂ + h)
  set Δ := theta T₁ - theta T₂
  set r_α := α - Δ + (q T₁ - q T₂) * h with hr_α_def
  set r_δ := δ - Δ - (q T₁ - q T₂) * h with hr_δ_def
  obtain ⟨h_α_lin, h_δ_lin, _, _⟩ := hK_lin h hh
  -- |r_α| ≤ K_lin h²
  have h_r_α_b : |r_α| ≤ K_lin * h^2 := h_α_lin
  -- |r_δ| ≤ K_lin h²
  have h_r_δ_b : |r_δ| ≤ K_lin * h^2 := by
    show |δ - Δ - (q T₁ - q T₂) * h| ≤ _
    exact h_δ_lin
  -- |r_δ - r_α| bound: from theta_R1_anti_diff_h3 for T₁ and T₂.
  have h_R1_T₁ := hK_anti_T₁ h hh
  have h_R1_T₂ := hK_anti_T₂ h hh
  -- r_α = R_T₁(-h) - R_T₂(-h) where R_T(h) = θ(T+h) - θT - qT h.
  -- r_δ = R_T₁(h) - R_T₂(h).
  -- r_δ - r_α = (R_T₁(h) - R_T₁(-h)) - (R_T₂(h) - R_T₂(-h)).
  have h_r_diff : |r_δ - r_α| ≤ (K_anti_T₁ + K_anti_T₂) * |h|^3 := by
    have h_split : r_δ - r_α =
        ((theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
         (theta (T₁ - h) - (theta T₁ + q T₁ * (-h)))) -
        ((theta (T₂ + h) - (theta T₂ + q T₂ * h)) -
         (theta (T₂ - h) - (theta T₂ + q T₂ * (-h)))) := by
      simp [hr_α_def, hr_δ_def]; ring
    calc |r_δ - r_α| = _ := by rw [h_split]
      _ ≤ |(theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
            (theta (T₁ - h) - (theta T₁ + q T₁ * (-h)))| +
          |(theta (T₂ + h) - (theta T₂ + q T₂ * h)) -
            (theta (T₂ - h) - (theta T₂ + q T₂ * (-h)))| := abs_sub _ _
      _ ≤ K_anti_T₁ * |h|^3 + K_anti_T₂ * |h|^3 := by linarith
      _ = (K_anti_T₁ + K_anti_T₂) * |h|^3 := by ring
  -- Now combine.
  have h_id : (α - Δ)^2 + (δ - Δ)^2 - 2 * (q T₁ - q T₂)^2 * h^2 =
      2 * (q T₁ - q T₂) * h * (r_δ - r_α) + r_α^2 + r_δ^2 := by
    rw [hr_α_def, hr_δ_def]; ring
  rw [h_id]
  -- Bound each piece.
  have h_h_abs : |h|^2 = h^2 := sq_abs h
  have h_h_pow_4 : |h|^4 = h^4 := by
    rw [show (4 : ℕ) = 2 + 2 from rfl, pow_add, h_h_abs]
    ring
  have h_h_pow_3 : |h|^3 = |h| * h^2 := by
    rw [show (3 : ℕ) = 1 + 2 from rfl, pow_add, h_h_abs]; ring
  have h_h_abs_le_R : |h| ≤ R := hh
  -- |2(q₁-q₂) h (r_δ - r_α)| ≤ 2|q₁-q₂||h| · (K_anti_T₁ + K_anti_T₂) |h|³
  --                       = 2|q₁-q₂| (K_anti_T₁ + K_anti_T₂) |h|⁴
  have h_b1 : |2 * (q T₁ - q T₂) * h * (r_δ - r_α)| ≤
      2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
    rw [show 2 * (q T₁ - q T₂) * h * (r_δ - r_α) =
        2 * (q T₁ - q T₂) * (h * (r_δ - r_α)) from by ring]
    rw [abs_mul, abs_mul, abs_mul]
    rw [show |(2:ℝ)| = 2 from by norm_num]
    have h_step1 : |h| * |r_δ - r_α| ≤ |h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3) :=
      mul_le_mul_of_nonneg_left h_r_diff (abs_nonneg _)
    have h_simpl : |h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3) =
        (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
      rw [show |h|^4 = |h| * |h|^3 from by ring]; ring
    calc 2 * |q T₁ - q T₂| * (|h| * |r_δ - r_α|)
        ≤ 2 * |q T₁ - q T₂| * (|h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3)) := by
          apply mul_le_mul_of_nonneg_left h_step1 (by positivity)
      _ = 2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
          rw [h_simpl]; ring
  -- |r_α²| ≤ K_lin² h⁴.
  have h_b2 : |r_α^2| ≤ K_lin^2 * h^4 := by
    rw [show r_α^2 = r_α * r_α from sq r_α]
    rw [abs_mul]
    have : |r_α| * |r_α| ≤ (K_lin * h^2) * (K_lin * h^2) :=
      mul_le_mul h_r_α_b h_r_α_b (abs_nonneg _) (by positivity)
    linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
  -- |r_δ²| ≤ K_lin² h⁴.
  have h_b3 : |r_δ^2| ≤ K_lin^2 * h^4 := by
    rw [show r_δ^2 = r_δ * r_δ from sq r_δ]
    rw [abs_mul]
    have : |r_δ| * |r_δ| ≤ (K_lin * h^2) * (K_lin * h^2) :=
      mul_le_mul h_r_δ_b h_r_δ_b (abs_nonneg _) (by positivity)
    linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
  -- Combine via triangle inequality.
  have h_tri : |2 * (q T₁ - q T₂) * h * (r_δ - r_α) + r_α^2 + r_δ^2| ≤
      |2 * (q T₁ - q T₂) * h * (r_δ - r_α)| + |r_α^2| + |r_δ^2| := by
    have h₁ := abs_add_le (2 * (q T₁ - q T₂) * h * (r_δ - r_α) + r_α^2) (r_δ^2)
    have h₂ := abs_add_le (2 * (q T₁ - q T₂) * h * (r_δ - r_α)) (r_α^2)
    linarith
  calc |2 * (q T₁ - q T₂) * h * (r_δ - r_α) + r_α^2 + r_δ^2|
      ≤ |2 * (q T₁ - q T₂) * h * (r_δ - r_α)| + |r_α^2| + |r_δ^2| := h_tri
    _ ≤ 2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 +
        K_lin^2 * h^4 + K_lin^2 * h^4 := by linarith
    _ = 2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) * h^4 +
        2 * K_lin^2 * h^4 := by rw [h_h_pow_4]; ring
    _ = (2 * |q T₁ - q T₂| * (K_anti_T₁ + K_anti_T₂) + 2 * K_lin^2) * h^4 := by ring

/-- Cross-block squared-angle sum precise h² bound for βγ pair:
    `|((β-Δ)² + (γ-Δ)²) - 2(q T₁ + q T₂)² h²| ≤ K h⁴`.
    Mirrors `cross_angle_sq_sum_αδ_h2` with sign on q₂ flipped. -/
private lemma cross_angle_sq_sum_βγ_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      let β := theta (T₁ - h) - theta (T₂ + h)
      let γ := theta (T₁ + h) - theta (T₂ - h)
      let Δ := theta T₁ - theta T₂
      |(β - Δ)^2 + (γ - Δ)^2 - 2 * (q T₁ + q T₂)^2 * h^2| ≤ K * h^4 := by
  obtain ⟨K_lin, hK_lin_nn, hK_lin⟩ := cross_angle_lin_bound_h2 T₁ T₂ R hR
  obtain ⟨K_anti_T₁, hK_anti_T₁_nn, hK_anti_T₁⟩ := theta_R1_anti_diff_h3 T₁ R hR
  obtain ⟨K_anti_T₂, hK_anti_T₂_nn, hK_anti_T₂⟩ := theta_R1_anti_diff_h3 T₂ R hR
  refine ⟨2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) + 2 * K_lin^2,
    by positivity, ?_⟩
  intro h hh
  simp only
  set β := theta (T₁ - h) - theta (T₂ + h)
  set γ := theta (T₁ + h) - theta (T₂ - h)
  set Δ := theta T₁ - theta T₂
  set r_β := β - Δ + (q T₁ + q T₂) * h with hr_β_def
  set r_γ := γ - Δ - (q T₁ + q T₂) * h with hr_γ_def
  obtain ⟨_, _, h_β_lin, h_γ_lin⟩ := hK_lin h hh
  have h_r_β_b : |r_β| ≤ K_lin * h^2 := h_β_lin
  have h_r_γ_b : |r_γ| ≤ K_lin * h^2 := by
    show |γ - Δ - (q T₁ + q T₂) * h| ≤ _
    exact h_γ_lin
  have h_R1_T₁ := hK_anti_T₁ h hh
  have h_R1_T₂ := hK_anti_T₂ h hh
  -- For β: β = θ(T₁-h) - θ(T₂+h).
  -- r_β = β - Δ + (q₁+q₂) h
  --     = (θ(T₁-h) - θT₁ + q₁ h) + (θ T₂ - θ(T₂+h) + q₂ h)
  --     = R_T₁(-h) - R_T₂(h)·(-1)... let me think.
  -- R_T(h) := θ(T+h) - θT - qT h. Then R_T(-h) = θ(T-h) - θT + qT h.
  -- β - Δ = (θ(T₁-h) - θT₁) - (θ(T₂+h) - θT₂) = (-q₁ h + R_T₁(-h)) - (q₂ h + R_T₂(h)) = -q₁ h - q₂ h + R_T₁(-h) - R_T₂(h)
  -- So β - Δ + (q₁+q₂) h = R_T₁(-h) - R_T₂(h).
  -- For γ: γ = θ(T₁+h) - θ(T₂-h).
  -- γ - Δ = (q₁ h + R_T₁(h)) - (-q₂ h + R_T₂(-h)) = (q₁+q₂) h + R_T₁(h) - R_T₂(-h).
  -- γ - Δ - (q₁+q₂) h = R_T₁(h) - R_T₂(-h).
  -- r_γ - r_β = (R_T₁(h) - R_T₂(-h)) - (R_T₁(-h) - R_T₂(h)) = (R_T₁(h) - R_T₁(-h)) + (R_T₂(h) - R_T₂(-h)).
  have h_r_diff : |r_γ - r_β| ≤ (K_anti_T₁ + K_anti_T₂) * |h|^3 := by
    have h_split : r_γ - r_β =
        ((theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
         (theta (T₁ - h) - (theta T₁ + q T₁ * (-h)))) +
        ((theta (T₂ + h) - (theta T₂ + q T₂ * h)) -
         (theta (T₂ - h) - (theta T₂ + q T₂ * (-h)))) := by
      simp [hr_β_def, hr_γ_def]; ring
    calc |r_γ - r_β| = _ := by rw [h_split]
      _ ≤ |(theta (T₁ + h) - (theta T₁ + q T₁ * h)) -
            (theta (T₁ - h) - (theta T₁ + q T₁ * (-h)))| +
          |(theta (T₂ + h) - (theta T₂ + q T₂ * h)) -
            (theta (T₂ - h) - (theta T₂ + q T₂ * (-h)))| := abs_add_le _ _
      _ ≤ K_anti_T₁ * |h|^3 + K_anti_T₂ * |h|^3 := by linarith
      _ = (K_anti_T₁ + K_anti_T₂) * |h|^3 := by ring
  have h_id : (β - Δ)^2 + (γ - Δ)^2 - 2 * (q T₁ + q T₂)^2 * h^2 =
      2 * (q T₁ + q T₂) * h * (r_γ - r_β) + r_β^2 + r_γ^2 := by
    rw [hr_β_def, hr_γ_def]; ring
  rw [h_id]
  have h_h_abs : |h|^2 = h^2 := sq_abs h
  have h_h_pow_4 : |h|^4 = h^4 := by
    rw [show (4 : ℕ) = 2 + 2 from rfl, pow_add, h_h_abs]; ring
  have h_b1 : |2 * (q T₁ + q T₂) * h * (r_γ - r_β)| ≤
      2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
    rw [show 2 * (q T₁ + q T₂) * h * (r_γ - r_β) =
        2 * (q T₁ + q T₂) * (h * (r_γ - r_β)) from by ring]
    rw [abs_mul, abs_mul, abs_mul]
    rw [show |(2:ℝ)| = 2 from by norm_num]
    have h_step1 : |h| * |r_γ - r_β| ≤ |h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3) :=
      mul_le_mul_of_nonneg_left h_r_diff (abs_nonneg _)
    have h_simpl : |h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3) =
        (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
      rw [show |h|^4 = |h| * |h|^3 from by ring]; ring
    calc 2 * |q T₁ + q T₂| * (|h| * |r_γ - r_β|)
        ≤ 2 * |q T₁ + q T₂| * (|h| * ((K_anti_T₁ + K_anti_T₂) * |h|^3)) := by
          apply mul_le_mul_of_nonneg_left h_step1 (by positivity)
      _ = 2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 := by
          rw [h_simpl]; ring
  have h_b2 : |r_β^2| ≤ K_lin^2 * h^4 := by
    rw [show r_β^2 = r_β * r_β from sq r_β]
    rw [abs_mul]
    have : |r_β| * |r_β| ≤ (K_lin * h^2) * (K_lin * h^2) :=
      mul_le_mul h_r_β_b h_r_β_b (abs_nonneg _) (by positivity)
    linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
  have h_b3 : |r_γ^2| ≤ K_lin^2 * h^4 := by
    rw [show r_γ^2 = r_γ * r_γ from sq r_γ]
    rw [abs_mul]
    have : |r_γ| * |r_γ| ≤ (K_lin * h^2) * (K_lin * h^2) :=
      mul_le_mul h_r_γ_b h_r_γ_b (abs_nonneg _) (by positivity)
    linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
  have h_tri : |2 * (q T₁ + q T₂) * h * (r_γ - r_β) + r_β^2 + r_γ^2| ≤
      |2 * (q T₁ + q T₂) * h * (r_γ - r_β)| + |r_β^2| + |r_γ^2| := by
    have h₁ := abs_add_le (2 * (q T₁ + q T₂) * h * (r_γ - r_β) + r_β^2) (r_γ^2)
    have h₂ := abs_add_le (2 * (q T₁ + q T₂) * h * (r_γ - r_β)) (r_β^2)
    linarith
  calc |2 * (q T₁ + q T₂) * h * (r_γ - r_β) + r_β^2 + r_γ^2|
      ≤ |2 * (q T₁ + q T₂) * h * (r_γ - r_β)| + |r_β^2| + |r_γ^2| := h_tri
    _ ≤ 2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) * |h|^4 +
        K_lin^2 * h^4 + K_lin^2 * h^4 := by linarith
    _ = 2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) * h^4 +
        2 * K_lin^2 * h^4 := by rw [h_h_pow_4]; ring
    _ = (2 * |q T₁ + q T₂| * (K_anti_T₁ + K_anti_T₂) + 2 * K_lin^2) * h^4 := by ring

/-- Cross-block angle cubed-sum bound for αδ pair: `|(α-Δ)³ + (δ-Δ)³| ≤ K h⁴`.
    The h³ contribution from the linear part cancels by parity, leaving an
    O(h⁴) leading term.  Combines `cross_angle_lin_bound_h2`. -/
private lemma cross_angle_cube_sum_αδ_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      let α := theta (T₁ - h) - theta (T₂ - h)
      let δ := theta (T₁ + h) - theta (T₂ + h)
      let Δ := theta T₁ - theta T₂
      |(α - Δ)^3 + (δ - Δ)^3| ≤ K * h^4 := by
  obtain ⟨K_lin, hK_lin_nn, hK_lin⟩ := cross_angle_lin_bound_h2 T₁ T₂ R hR
  refine ⟨6 * (q T₁ - q T₂)^2 * K_lin + 6 * |q T₁ - q T₂| * K_lin^2 * R +
           2 * K_lin^3 * R^2, by positivity, ?_⟩
  intro h hh
  simp only
  set α := theta (T₁ - h) - theta (T₂ - h) with hα_def
  set δ := theta (T₁ + h) - theta (T₂ + h) with hδ_def
  set Δ := theta T₁ - theta T₂ with hΔ_def
  set r_α := α - Δ + (q T₁ - q T₂) * h with hr_α_def
  set r_δ := δ - Δ - (q T₁ - q T₂) * h with hr_δ_def
  obtain ⟨h_α_lin, h_δ_lin, _, _⟩ := hK_lin h hh
  have h_r_α_b : |r_α| ≤ K_lin * h^2 := h_α_lin
  have h_r_δ_b : |r_δ| ≤ K_lin * h^2 := by
    show |δ - Δ - (q T₁ - q T₂) * h| ≤ _
    exact h_δ_lin
  have h_id : (α - Δ)^3 + (δ - Δ)^3 =
      3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ) +
      3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2) +
      (r_α^3 + r_δ^3) := by
    rw [hr_α_def, hr_δ_def]; ring
  rw [h_id]
  have h_h_pow_4_nn : 0 ≤ h^4 := by positivity
  have h_h_sq_le_R_sq : h^2 ≤ R^2 := by
    rw [show h^2 = |h|^2 from (sq_abs h).symm,
        show R^2 = R * R from sq R, show |h|^2 = |h| * |h| from sq |h|]
    exact mul_le_mul hh hh (abs_nonneg _) hR.le
  -- Bound 1: |3 ((q₁-q₂) h)² (r_α + r_δ)| ≤ 6 (q₁-q₂)² K_lin h⁴
  have h_b1 : |3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ)| ≤
      6 * (q T₁ - q T₂)^2 * K_lin * h^4 := by
    rw [show 3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ) =
        (3 * (q T₁ - q T₂)^2 * h^2) * (r_α + r_δ) from by ring]
    rw [abs_mul]
    rw [show |3 * (q T₁ - q T₂)^2 * h^2| = 3 * (q T₁ - q T₂)^2 * h^2 from
        abs_of_nonneg (by positivity)]
    have h_sum_b : |r_α + r_δ| ≤ 2 * K_lin * h^2 := by
      calc |r_α + r_δ| ≤ |r_α| + |r_δ| := abs_add_le _ _
        _ ≤ K_lin * h^2 + K_lin * h^2 := by linarith
        _ = 2 * K_lin * h^2 := by ring
    calc 3 * (q T₁ - q T₂)^2 * h^2 * |r_α + r_δ|
        ≤ 3 * (q T₁ - q T₂)^2 * h^2 * (2 * K_lin * h^2) := by
          apply mul_le_mul_of_nonneg_left h_sum_b (by positivity)
      _ = 6 * (q T₁ - q T₂)^2 * K_lin * h^4 := by ring
  -- Bound 2: |3 ((q₁-q₂) h) (r_δ² - r_α²)| ≤ 6 |q₁-q₂| K_lin² R h⁴
  have h_b2 : |3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2)| ≤
      6 * |q T₁ - q T₂| * K_lin^2 * R * h^4 := by
    rw [abs_mul, abs_mul]
    rw [show |(3:ℝ)| = 3 from by norm_num]
    rw [show |(q T₁ - q T₂) * h| = |q T₁ - q T₂| * |h| from abs_mul _ _]
    have h_α_sq_b : |r_α^2| ≤ K_lin^2 * h^4 := by
      rw [show r_α^2 = r_α * r_α from sq r_α, abs_mul]
      have := mul_le_mul h_r_α_b h_r_α_b (abs_nonneg _) (by positivity)
      linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
    have h_δ_sq_b : |r_δ^2| ≤ K_lin^2 * h^4 := by
      rw [show r_δ^2 = r_δ * r_δ from sq r_δ, abs_mul]
      have := mul_le_mul h_r_δ_b h_r_δ_b (abs_nonneg _) (by positivity)
      linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
    have h_diff_b : |r_δ^2 - r_α^2| ≤ 2 * K_lin^2 * h^4 := by
      calc |r_δ^2 - r_α^2| ≤ |r_δ^2| + |r_α^2| := abs_sub _ _
        _ ≤ K_lin^2 * h^4 + K_lin^2 * h^4 := by linarith
        _ = 2 * K_lin^2 * h^4 := by ring
    calc 3 * (|q T₁ - q T₂| * |h|) * |r_δ^2 - r_α^2|
        ≤ 3 * (|q T₁ - q T₂| * |h|) * (2 * K_lin^2 * h^4) := by
          apply mul_le_mul_of_nonneg_left h_diff_b (by positivity)
      _ = 6 * |q T₁ - q T₂| * K_lin^2 * (|h| * h^4) := by ring
      _ ≤ 6 * |q T₁ - q T₂| * K_lin^2 * (R * h^4) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          exact mul_le_mul_of_nonneg_right hh h_h_pow_4_nn
      _ = 6 * |q T₁ - q T₂| * K_lin^2 * R * h^4 := by ring
  -- Bound 3: |r_α³ + r_δ³| ≤ 2 K_lin³ R² h⁴
  have h_b3 : |r_α^3 + r_δ^3| ≤ 2 * K_lin^3 * R^2 * h^4 := by
    have h_α_cube : |r_α^3| ≤ K_lin^3 * h^6 := by
      have h_α_sq_b' : |r_α|^2 ≤ K_lin^2 * h^4 := by
        rw [show |r_α|^2 = |r_α| * |r_α| from sq _]
        have := mul_le_mul h_r_α_b h_r_α_b (abs_nonneg _) (by positivity)
        linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
      rw [show r_α^3 = r_α * (r_α * r_α) from by ring, abs_mul]
      rw [show |r_α * r_α| = |r_α|^2 from by rw [abs_mul, sq]]
      have := mul_le_mul h_r_α_b h_α_sq_b' (sq_nonneg _) (by positivity)
      linarith [show K_lin * h^2 * (K_lin^2 * h^4) = K_lin^3 * h^6 from by ring]
    have h_δ_cube : |r_δ^3| ≤ K_lin^3 * h^6 := by
      have h_δ_sq_b' : |r_δ|^2 ≤ K_lin^2 * h^4 := by
        rw [show |r_δ|^2 = |r_δ| * |r_δ| from sq _]
        have := mul_le_mul h_r_δ_b h_r_δ_b (abs_nonneg _) (by positivity)
        linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
      rw [show r_δ^3 = r_δ * (r_δ * r_δ) from by ring, abs_mul]
      rw [show |r_δ * r_δ| = |r_δ|^2 from by rw [abs_mul, sq]]
      have := mul_le_mul h_r_δ_b h_δ_sq_b' (sq_nonneg _) (by positivity)
      linarith [show K_lin * h^2 * (K_lin^2 * h^4) = K_lin^3 * h^6 from by ring]
    calc |r_α^3 + r_δ^3| ≤ |r_α^3| + |r_δ^3| := abs_add_le _ _
      _ ≤ K_lin^3 * h^6 + K_lin^3 * h^6 := by linarith
      _ = 2 * K_lin^3 * (h^4 * h^2) := by ring
      _ ≤ 2 * K_lin^3 * (h^4 * R^2) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          exact mul_le_mul_of_nonneg_left h_h_sq_le_R_sq h_h_pow_4_nn
      _ = 2 * K_lin^3 * R^2 * h^4 := by ring
  -- Combine via triangle inequality
  calc |3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ) +
        3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2) +
        (r_α^3 + r_δ^3)|
      ≤ |3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ) +
         3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2)| + |r_α^3 + r_δ^3| :=
        abs_add_le _ _
    _ ≤ |3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ)| +
        |3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2)| + |r_α^3 + r_δ^3| := by
        have := abs_add_le (3 * ((q T₁ - q T₂) * h)^2 * (r_α + r_δ))
                            (3 * ((q T₁ - q T₂) * h) * (r_δ^2 - r_α^2))
        linarith
    _ ≤ 6 * (q T₁ - q T₂)^2 * K_lin * h^4 +
        6 * |q T₁ - q T₂| * K_lin^2 * R * h^4 +
        2 * K_lin^3 * R^2 * h^4 := by linarith
    _ = (6 * (q T₁ - q T₂)^2 * K_lin + 6 * |q T₁ - q T₂| * K_lin^2 * R +
         2 * K_lin^3 * R^2) * h^4 := by ring

/-- Cross-block angle cubed-sum bound for βγ pair: `|(β-Δ)³ + (γ-Δ)³| ≤ K h⁴`.
    Mirrors `cross_angle_cube_sum_αδ_h2` with `q T₁ + q T₂` in place of
    `q T₁ - q T₂`. -/
private lemma cross_angle_cube_sum_βγ_h2 (T₁ T₂ R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      let β := theta (T₁ - h) - theta (T₂ + h)
      let γ := theta (T₁ + h) - theta (T₂ - h)
      let Δ := theta T₁ - theta T₂
      |(β - Δ)^3 + (γ - Δ)^3| ≤ K * h^4 := by
  obtain ⟨K_lin, hK_lin_nn, hK_lin⟩ := cross_angle_lin_bound_h2 T₁ T₂ R hR
  refine ⟨6 * (q T₁ + q T₂)^2 * K_lin + 6 * |q T₁ + q T₂| * K_lin^2 * R +
           2 * K_lin^3 * R^2, by positivity, ?_⟩
  intro h hh
  simp only
  set β := theta (T₁ - h) - theta (T₂ + h) with hβ_def
  set γ := theta (T₁ + h) - theta (T₂ - h) with hγ_def
  set Δ := theta T₁ - theta T₂ with hΔ_def
  set r_β := β - Δ + (q T₁ + q T₂) * h with hr_β_def
  set r_γ := γ - Δ - (q T₁ + q T₂) * h with hr_γ_def
  obtain ⟨_, _, h_β_lin, h_γ_lin⟩ := hK_lin h hh
  have h_r_β_b : |r_β| ≤ K_lin * h^2 := h_β_lin
  have h_r_γ_b : |r_γ| ≤ K_lin * h^2 := by
    show |γ - Δ - (q T₁ + q T₂) * h| ≤ _
    exact h_γ_lin
  have h_id : (β - Δ)^3 + (γ - Δ)^3 =
      3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ) +
      3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2) +
      (r_β^3 + r_γ^3) := by
    rw [hr_β_def, hr_γ_def]; ring
  rw [h_id]
  have h_h_pow_4_nn : 0 ≤ h^4 := by positivity
  have h_h_sq_le_R_sq : h^2 ≤ R^2 := by
    rw [show h^2 = |h|^2 from (sq_abs h).symm,
        show R^2 = R * R from sq R, show |h|^2 = |h| * |h| from sq |h|]
    exact mul_le_mul hh hh (abs_nonneg _) hR.le
  -- Bound 1: |3 ((q₁+q₂) h)² (r_β + r_γ)| ≤ 6 (q₁+q₂)² K_lin h⁴
  have h_b1 : |3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ)| ≤
      6 * (q T₁ + q T₂)^2 * K_lin * h^4 := by
    rw [show 3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ) =
        (3 * (q T₁ + q T₂)^2 * h^2) * (r_β + r_γ) from by ring]
    rw [abs_mul]
    rw [show |3 * (q T₁ + q T₂)^2 * h^2| = 3 * (q T₁ + q T₂)^2 * h^2 from
        abs_of_nonneg (by positivity)]
    have h_sum_b : |r_β + r_γ| ≤ 2 * K_lin * h^2 := by
      calc |r_β + r_γ| ≤ |r_β| + |r_γ| := abs_add_le _ _
        _ ≤ K_lin * h^2 + K_lin * h^2 := by linarith
        _ = 2 * K_lin * h^2 := by ring
    calc 3 * (q T₁ + q T₂)^2 * h^2 * |r_β + r_γ|
        ≤ 3 * (q T₁ + q T₂)^2 * h^2 * (2 * K_lin * h^2) := by
          apply mul_le_mul_of_nonneg_left h_sum_b (by positivity)
      _ = 6 * (q T₁ + q T₂)^2 * K_lin * h^4 := by ring
  -- Bound 2: |3 ((q₁+q₂) h) (r_γ² - r_β²)| ≤ 6 |q₁+q₂| K_lin² R h⁴
  have h_b2 : |3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2)| ≤
      6 * |q T₁ + q T₂| * K_lin^2 * R * h^4 := by
    rw [abs_mul, abs_mul]
    rw [show |(3:ℝ)| = 3 from by norm_num]
    rw [show |(q T₁ + q T₂) * h| = |q T₁ + q T₂| * |h| from abs_mul _ _]
    have h_β_sq_b : |r_β^2| ≤ K_lin^2 * h^4 := by
      rw [show r_β^2 = r_β * r_β from sq r_β, abs_mul]
      have := mul_le_mul h_r_β_b h_r_β_b (abs_nonneg _) (by positivity)
      linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
    have h_γ_sq_b : |r_γ^2| ≤ K_lin^2 * h^4 := by
      rw [show r_γ^2 = r_γ * r_γ from sq r_γ, abs_mul]
      have := mul_le_mul h_r_γ_b h_r_γ_b (abs_nonneg _) (by positivity)
      linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
    have h_diff_b : |r_γ^2 - r_β^2| ≤ 2 * K_lin^2 * h^4 := by
      calc |r_γ^2 - r_β^2| ≤ |r_γ^2| + |r_β^2| := abs_sub _ _
        _ ≤ K_lin^2 * h^4 + K_lin^2 * h^4 := by linarith
        _ = 2 * K_lin^2 * h^4 := by ring
    calc 3 * (|q T₁ + q T₂| * |h|) * |r_γ^2 - r_β^2|
        ≤ 3 * (|q T₁ + q T₂| * |h|) * (2 * K_lin^2 * h^4) := by
          apply mul_le_mul_of_nonneg_left h_diff_b (by positivity)
      _ = 6 * |q T₁ + q T₂| * K_lin^2 * (|h| * h^4) := by ring
      _ ≤ 6 * |q T₁ + q T₂| * K_lin^2 * (R * h^4) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          exact mul_le_mul_of_nonneg_right hh h_h_pow_4_nn
      _ = 6 * |q T₁ + q T₂| * K_lin^2 * R * h^4 := by ring
  -- Bound 3: |r_β³ + r_γ³| ≤ 2 K_lin³ R² h⁴
  have h_b3 : |r_β^3 + r_γ^3| ≤ 2 * K_lin^3 * R^2 * h^4 := by
    have h_β_cube : |r_β^3| ≤ K_lin^3 * h^6 := by
      have h_β_sq_b' : |r_β|^2 ≤ K_lin^2 * h^4 := by
        rw [show |r_β|^2 = |r_β| * |r_β| from sq _]
        have := mul_le_mul h_r_β_b h_r_β_b (abs_nonneg _) (by positivity)
        linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
      rw [show r_β^3 = r_β * (r_β * r_β) from by ring, abs_mul]
      rw [show |r_β * r_β| = |r_β|^2 from by rw [abs_mul, sq]]
      have := mul_le_mul h_r_β_b h_β_sq_b' (sq_nonneg _) (by positivity)
      linarith [show K_lin * h^2 * (K_lin^2 * h^4) = K_lin^3 * h^6 from by ring]
    have h_γ_cube : |r_γ^3| ≤ K_lin^3 * h^6 := by
      have h_γ_sq_b' : |r_γ|^2 ≤ K_lin^2 * h^4 := by
        rw [show |r_γ|^2 = |r_γ| * |r_γ| from sq _]
        have := mul_le_mul h_r_γ_b h_r_γ_b (abs_nonneg _) (by positivity)
        linarith [show (K_lin * h^2) * (K_lin * h^2) = K_lin^2 * h^4 from by ring]
      rw [show r_γ^3 = r_γ * (r_γ * r_γ) from by ring, abs_mul]
      rw [show |r_γ * r_γ| = |r_γ|^2 from by rw [abs_mul, sq]]
      have := mul_le_mul h_r_γ_b h_γ_sq_b' (sq_nonneg _) (by positivity)
      linarith [show K_lin * h^2 * (K_lin^2 * h^4) = K_lin^3 * h^6 from by ring]
    calc |r_β^3 + r_γ^3| ≤ |r_β^3| + |r_γ^3| := abs_add_le _ _
      _ ≤ K_lin^3 * h^6 + K_lin^3 * h^6 := by linarith
      _ = 2 * K_lin^3 * (h^4 * h^2) := by ring
      _ ≤ 2 * K_lin^3 * (h^4 * R^2) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          exact mul_le_mul_of_nonneg_left h_h_sq_le_R_sq h_h_pow_4_nn
      _ = 2 * K_lin^3 * R^2 * h^4 := by ring
  -- Combine via triangle inequality
  calc |3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ) +
        3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2) +
        (r_β^3 + r_γ^3)|
      ≤ |3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ) +
         3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2)| + |r_β^3 + r_γ^3| :=
        abs_add_le _ _
    _ ≤ |3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ)| +
        |3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2)| + |r_β^3 + r_γ^3| := by
        have := abs_add_le (3 * ((q T₁ + q T₂) * h)^2 * (r_β + r_γ))
                            (3 * ((q T₁ + q T₂) * h) * (r_γ^2 - r_β^2))
        linarith
    _ ≤ 6 * (q T₁ + q T₂)^2 * K_lin * h^4 +
        6 * |q T₁ + q T₂| * K_lin^2 * R * h^4 +
        2 * K_lin^3 * R^2 * h^4 := by linarith
    _ = (6 * (q T₁ + q T₂)^2 * K_lin + 6 * |q T₁ + q T₂| * K_lin^2 * R +
         2 * K_lin^3 * R^2) * h^4 := by ring

/-- Pure algebraic identity used to combine the four phaseKernel entries
    into a single fraction.  Treats `a, b, c, d, s, h` as abstract real
    numbers, sidestepping function-argument normalization issues. -/
private lemma cross_neg_pos_combine_alg (s h a b c d : ℝ)
    (hs_ne : s ≠ 0) (hsm_ne : s - 2 * h ≠ 0) (hsp_ne : s + 2 * h ≠ 0) :
    -(a / s) + b / (s - 2 * h) - c / (s + 2 * h) + d / s =
    ((s^2 - 4 * h^2) * (d - a) + s^2 * (b - c) + 2 * s * h * (b + c)) /
    (s * (s^2 - 4 * h^2)) := by
  have h_eq : s^2 - 4 * h^2 = (s - 2 * h) * (s + 2 * h) := by ring
  rw [h_eq]
  field_simp
  ring

set_option maxHeartbeats 4000000 in
/-- Bound on entry `(0, 1)` of `P_h C_h(T₁, T₂) P_h^⊤ − (1/π) N₁₂(T₁, T₂)`
    for `h ∈ (0, |s|/3]`. -/
private lemma cross_rate_bound_01 (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ |T₁ - T₂| / 3 →
      |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1| ≤ M * h^2 := by
  set R : ℝ := |T₁ - T₂| / 3 with hR_def
  have hs_ne : T₁ - T₂ ≠ 0 := sub_ne_zero.mpr hT
  have hs_abs_pos : 0 < |T₁ - T₂| := abs_pos.mpr hs_ne
  have hR_pos : 0 < R := by show 0 < |T₁ - T₂| / 3; linarith
  obtain ⟨M_sym, hM_sym_nn, hM_sym⟩ := cross_sin_pair_sym_bound T₁ T₂ R hR_pos
  obtain ⟨M_a, hM_a_nn, hM_a⟩ := cross_sin_pair_anti_lin_bound T₁ T₂ R hR_pos
  -- M_01 constant: bound on |D| = O(h²).
  -- Decomposition gives 3 pieces E₁, E₂, E₃ each O(h³) before /(4h):
  --   |E₁/(4h)| ≤ M_a/(2π|s|) · h²
  --   |E₂/(4h)| ≤ M_sym/(2π s²) · h²
  --   |E₃/(4h)| bound: depends on |sin β + sin γ| linear in h (= M_b lin) plus const.
  -- For a coarse bound, use cross_sin_pair_anti_bound for |sin β - sin γ| ≤ M_b h.
  obtain ⟨M_b, hM_b_nn, hM_b⟩ := cross_sin_pair_anti_bound T₁ T₂ R hR_pos
  -- Set the final M to be a sufficient bound.
  set M_01 : ℝ :=
      M_a / (2 * Real.pi * |T₁ - T₂|) +
      M_sym / (2 * Real.pi * (T₁ - T₂)^2) +
      9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) with hM_01_def
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  have hs_sq_pos : 0 < (T₁ - T₂)^2 := by positivity
  have hs_4_pos : 0 < (T₁ - T₂)^4 := by positivity
  have hM_01_nn : 0 ≤ M_01 := by
    show 0 ≤ M_a / (2 * Real.pi * |T₁ - T₂|) +
        M_sym / (2 * Real.pi * (T₁ - T₂)^2) +
        9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4)
    have h1 : 0 ≤ M_a / (2 * Real.pi * |T₁ - T₂|) := by positivity
    have h2 : 0 ≤ M_sym / (2 * Real.pi * (T₁ - T₂)^2) := by positivity
    have h3 : 0 ≤ 9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) := by
      apply div_nonneg
      · have : 0 ≤ M_b * |T₁ - T₂| + 4 := by positivity
        linarith
      · positivity
    linarith
  refine ⟨M_01, hM_01_nn, ?_⟩
  intro h h_pos h_le
  have h_abs_le : |h| ≤ R := by rw [abs_of_pos h_pos]; exact h_le
  obtain ⟨h_pK_00, h_pK_01, h_pK_10, h_pK_11⟩ :=
    crossBlock_apply T₁ T₂ h hT h_pos h_le
  obtain ⟨_, h_N_01, _, _⟩ := N12_smul_apply T₁ T₂ hT
  obtain ⟨_, h_sym_βγ⟩ := hM_sym h h_abs_le
  obtain ⟨h_anti_αδ, h_anti_βγ⟩ := hM_a h h_abs_le
  have h_anti_diff_βγ := hM_b h h_abs_le
  obtain ⟨h_denom_lower, h_denom_pos⟩ :=
    cross_denom_sq_lower (T₁ - T₂) h hs_ne h_pos h_le
  obtain ⟨_, hsp_ne, hsm_ne⟩ := cross_denominators_nonzero T₁ T₂ h hT h_pos h_le
  have h_h_abs_eq : |h| = h := abs_of_pos h_pos
  -- Sin abbreviations.
  set α_sin := Real.sin (theta (T₁ - h) - theta (T₂ - h)) with hα_sin_def
  set β_sin := Real.sin (theta (T₁ - h) - theta (T₂ + h)) with hβ_sin_def
  set γ_sin := Real.sin (theta (T₁ + h) - theta (T₂ - h)) with hγ_sin_def
  set δ_sin := Real.sin (theta (T₁ + h) - theta (T₂ + h)) with hδ_sin_def
  set Δ_sin := Real.sin (theta T₁ - theta T₂) with hΔ_sin_def
  set Δ_cos := Real.cos (theta T₁ - theta T₂) with hΔ_cos_def
  -- Step 1: jet entry = (-α_sin/(πs) + β_sin/(π(s-2h)) - γ_sin/(π(s+2h)) + δ_sin/(πs)) / (4h).
  have h_jet_01 : (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 1 =
      (-(α_sin / (Real.pi * (T₁ - T₂))) +
       β_sin / (Real.pi * (T₁ - T₂ - 2 * h)) -
       γ_sin / (Real.pi * (T₁ - T₂ + 2 * h)) +
       δ_sin / (Real.pi * (T₁ - T₂))) / (4 * h) := by
    rw [jet_cross_matrix_apply_01 T₁ T₂ h hT h_pos h_le]
    rw [h_pK_00, h_pK_01, h_pK_10, h_pK_11]
  -- Apply cross_neg_pos_combine_alg with s = π·(T₁-T₂), the abstract values
  -- Actually our denoms have an extra π factor. Let me rewrite into pure form.
  -- Note: -(α_sin / (π·s)) = -(α_sin/π) / s. So if we set a := α_sin/π, etc.,
  -- this matches the cross_neg_pos_combine_alg form.
  set a := α_sin / Real.pi with ha_def
  set b := β_sin / Real.pi with hb_def
  set c := γ_sin / Real.pi with hc_def
  set d := δ_sin / Real.pi with hd_def
  have h_jet_01_v2 : (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 1 =
      (-(a / (T₁ - T₂)) +
       b / ((T₁ - T₂) - 2 * h) -
       c / ((T₁ - T₂) + 2 * h) +
       d / (T₁ - T₂)) / (4 * h) := by
    rw [h_jet_01]
    show (-(α_sin / (Real.pi * (T₁ - T₂))) +
         β_sin / (Real.pi * (T₁ - T₂ - 2 * h)) -
         γ_sin / (Real.pi * (T₁ - T₂ + 2 * h)) +
         δ_sin / (Real.pi * (T₁ - T₂))) / (4 * h) = _
    rw [ha_def, hb_def, hc_def, hd_def]
    have hπ_ne' : Real.pi ≠ 0 := hπ_ne
    field_simp
  -- Apply cross_neg_pos_combine_alg.
  have h_combine := cross_neg_pos_combine_alg (T₁ - T₂) h a b c d
      hs_ne hsm_ne hsp_ne
  rw [h_combine] at h_jet_01_v2
  -- Now h_jet_01_v2 has the combined form: (numerator) / (s(s²-4h²)) / (4h).
  -- Define explicit sin-num form.
  set num_combined : ℝ :=
    ((T₁ - T₂)^2 - 4 * h^2) * (d - a) +
    (T₁ - T₂)^2 * (b - c) +
    2 * (T₁ - T₂) * h * (b + c)
  have h_jet_01_v3 : (pointToJetTransform h * crossBlock T₁ T₂ h *
      (pointToJetTransform h).transpose) 0 1 =
      num_combined / ((T₁ - T₂) * ((T₁ - T₂)^2 - 4 * h^2)) / (4 * h) :=
    h_jet_01_v2
  -- Compute D = jet - n12_value.
  have h_n_01 : ((1 / Real.pi) • N12 T₁ T₂) 0 1 =
      (Δ_sin - q T₂ * (T₁ - T₂) * Δ_cos) /
        (Real.pi * (T₁ - T₂)^2) := h_N_01
  -- Multiply both sides of h_jet_01_v3 by (T₁ - T₂) · π and show:
  -- num_combined = ((T₁-T₂)²-4h²)(d-a) + (T₁-T₂)²(b-c) + 2(T₁-T₂)h(b+c)
  --             = ((T₁-T₂)² - 4h²)·(δ_sin - α_sin)/π + (T₁-T₂)²·(β_sin - γ_sin)/π +
  --                + 2(T₁-T₂)·h·(β_sin + γ_sin)/π
  -- All divided by π.
  -- Express num_combined explicitly in sin form.
  have h_num_combined_expand : num_combined =
      (((T₁ - T₂)^2 - 4 * h^2) * (δ_sin - α_sin) +
       (T₁ - T₂)^2 * (β_sin - γ_sin) +
       2 * (T₁ - T₂) * h * (β_sin + γ_sin)) / Real.pi := by
    show num_combined = _
    rw [show num_combined = ((T₁ - T₂)^2 - 4 * h^2) * (d - a) +
        (T₁ - T₂)^2 * (b - c) +
        2 * (T₁ - T₂) * h * (b + c) from rfl]
    rw [ha_def, hb_def, hc_def, hd_def]
    field_simp
  rw [h_num_combined_expand] at h_jet_01_v3
  -- Key step: bound D = jet_01_value - n12_value using algebraic decomposition.
  -- Define the residual functions.
  set R_αδ := δ_sin - α_sin - 2 * (q T₁ - q T₂) * Δ_cos * h with hR_αδ_def
  set R_βγ := β_sin - γ_sin + 2 * (q T₁ + q T₂) * Δ_cos * h with hR_βγ_def
  set R_sym := β_sin + γ_sin - 2 * Δ_sin with hR_sym_def
  have h_h_pow_eq : |h|^3 = h^3 := by rw [h_h_abs_eq]
  have hR_αδ_b : |R_αδ| ≤ M_a * h^3 := by
    have := h_anti_αδ
    rw [h_h_pow_eq] at this
    exact this
  have hR_βγ_b : |R_βγ| ≤ M_a * h^3 := by
    have := h_anti_βγ
    rw [h_h_pow_eq] at this
    exact this
  have hR_sym_b : |R_sym| ≤ M_sym * h^2 := h_sym_βγ
  -- Key identity using residuals (derived purely algebraically):
  -- jet_01 - (1/π)N12_01 = E₁ + E₂ + E₃ where:
  --   E₁ = (R_αδ + R_βγ) / (4h π (T₁-T₂))
  --   E₂ = R_sym / (2 π (T₁-T₂)²)   -- note: 2h R_sym / (4h π s²) = R_sym/(2π s²)
  --   E₃ = h(β_sin(T₁-T₂+2h) - γ_sin(T₁-T₂-2h)) / (π (T₁-T₂)² ((T₁-T₂)²-4h²))
  set E₁ := (R_αδ + R_βγ) / (4 * h * Real.pi * (T₁ - T₂))
  set E₂ := R_sym / (2 * Real.pi * (T₁ - T₂)^2)
  set E₃ := h * (β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h)) /
      (Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2))
  -- Final bound: each |E_i| ≤ M_i h².  Use triangle.
  have h_h2_nn : 0 ≤ h^2 := sq_nonneg h
  have h_h_nn : 0 ≤ h := h_pos.le
  -- Bound |E₁|: |R_αδ + R_βγ| ≤ |R_αδ| + |R_βγ| ≤ 2 M_a h³.
  -- |E₁| = |R_αδ + R_βγ| / (4 h π |T₁-T₂|) ≤ 2 M_a h³ / (4 h π |T₁-T₂|) = M_a h² / (2 π |T₁-T₂|).
  have h_E1_bound : |E₁| ≤ M_a / (2 * Real.pi * |T₁ - T₂|) * h^2 := by
    show |(R_αδ + R_βγ) / (4 * h * Real.pi * (T₁ - T₂))| ≤ _
    rw [abs_div]
    rw [show |4 * h * Real.pi * (T₁ - T₂)| =
        4 * h * Real.pi * |T₁ - T₂| from by
      rw [show 4 * h * Real.pi * (T₁ - T₂) =
          (4 * h * Real.pi) * (T₁ - T₂) from by ring]
      rw [abs_mul]
      rw [show |4 * h * Real.pi| = 4 * h * Real.pi from
          abs_of_pos (by positivity)]]
    rw [div_le_iff₀ (by positivity : (0:ℝ) < 4 * h * Real.pi * |T₁ - T₂|)]
    have h_R_sum : |R_αδ + R_βγ| ≤ 2 * M_a * h^3 := by
      calc |R_αδ + R_βγ| ≤ |R_αδ| + |R_βγ| := abs_add_le _ _
        _ ≤ M_a * h^3 + M_a * h^3 := by linarith
        _ = 2 * M_a * h^3 := by ring
    have h_eq : 2 * M_a * h^3 =
        M_a / (2 * Real.pi * |T₁ - T₂|) * h^2 * (4 * h * Real.pi * |T₁ - T₂|) := by
      have hπ_ne_local : Real.pi ≠ 0 := Real.pi_ne_zero
      have hs_abs_ne : |T₁ - T₂| ≠ 0 := hs_abs_pos.ne'
      field_simp
      ring
    linarith [h_R_sum, h_eq]
  -- Bound |E₂|: |R_sym| ≤ M_sym h². So |E₂| ≤ M_sym h² / (2 π s²).
  have h_E2_bound : |E₂| ≤ M_sym / (2 * Real.pi * (T₁ - T₂)^2) * h^2 := by
    show |R_sym / (2 * Real.pi * (T₁ - T₂)^2)| ≤ _
    rw [abs_div]
    rw [show |2 * Real.pi * (T₁ - T₂)^2| = 2 * Real.pi * (T₁ - T₂)^2 from
        abs_of_pos (by positivity)]
    rw [div_le_iff₀ (by positivity : (0:ℝ) < 2 * Real.pi * (T₁ - T₂)^2)]
    calc |R_sym| ≤ M_sym * h^2 := hR_sym_b
      _ = M_sym / (2 * Real.pi * (T₁ - T₂)^2) * h^2 * (2 * Real.pi * (T₁ - T₂)^2) := by
          field_simp
  -- Bound |E₃|. The numerator: h · (β_sin(s+2h) - γ_sin(s-2h)).
  -- Let X = β_sin(s+2h) - γ_sin(s-2h) = s(β_sin - γ_sin) + 2h(β_sin + γ_sin)
  -- |s(β_sin - γ_sin)| ≤ |s| · M_b h
  -- |2h(β_sin + γ_sin)| ≤ 2h · 2 = 4h (using |sin| ≤ 1)
  -- |X| ≤ M_b |s| h + 4h
  -- |h · X| ≤ M_b |s| h² + 4 h²
  -- Denom: π s² (s²-4h²) ≥ π s² · 5s²/9 = 5π s⁴/9.
  -- |E₃| ≤ (M_b |s| h² + 4 h²) / (5π s⁴/9) = 9(M_b |s| + 4) h² / (5π s⁴)
  have h_E3_bound : |E₃| ≤ 9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) * h^2 := by
    show |h * (β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h)) /
         (Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2))| ≤ _
    rw [abs_div]
    have h_denom_pos_full :
        0 < Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) := by positivity
    rw [abs_of_pos h_denom_pos_full]
    rw [div_le_iff₀ h_denom_pos_full]
    -- |h · X| ≤ h · (|s| · M_b h + 4h) = M_b |s| h² + 4 h²
    have h_X_bound : |β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h)| ≤
        M_b * |T₁ - T₂| * h + 4 * h := by
      have h_X_eq : β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h) =
          (T₁ - T₂) * (β_sin - γ_sin) + 2 * h * (β_sin + γ_sin) := by ring
      rw [h_X_eq]
      have h_step1 : |(T₁ - T₂) * (β_sin - γ_sin) + 2 * h * (β_sin + γ_sin)| ≤
          |(T₁ - T₂) * (β_sin - γ_sin)| + |2 * h * (β_sin + γ_sin)| := abs_add_le _ _
      have h_step2 : |(T₁ - T₂) * (β_sin - γ_sin)| ≤ |T₁ - T₂| * (M_b * h) := by
        rw [abs_mul]
        have h_anti_h : |β_sin - γ_sin| ≤ M_b * h := by
          rw [← h_h_abs_eq]; exact h_anti_diff_βγ
        exact mul_le_mul_of_nonneg_left h_anti_h (abs_nonneg _)
      have h_sin_sum : |β_sin + γ_sin| ≤ 2 := by
        have hβ : |β_sin| ≤ 1 := Real.abs_sin_le_one _
        have hγ : |γ_sin| ≤ 1 := Real.abs_sin_le_one _
        have h_tri := abs_add_le β_sin γ_sin
        linarith
      have h_step3 : |2 * h * (β_sin + γ_sin)| ≤ 2 * h * 2 := by
        rw [abs_mul, abs_mul, abs_of_pos h_pos,
            show |(2:ℝ)| = 2 from by norm_num]
        exact mul_le_mul_of_nonneg_left h_sin_sum (by positivity)
      have h_combined : |(T₁ - T₂) * (β_sin - γ_sin) + 2 * h * (β_sin + γ_sin)| ≤
          M_b * |T₁ - T₂| * h + 4 * h := by
        have h_sum : |T₁ - T₂| * (M_b * h) + 2 * h * 2 = M_b * |T₁ - T₂| * h + 4 * h := by ring
        linarith [h_step1, h_step2, h_step3, h_sum]
      exact h_combined
    have h_h_X_bound : |h * (β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h))| ≤
        h * (M_b * |T₁ - T₂| * h + 4 * h) := by
      rw [abs_mul, abs_of_pos h_pos]
      exact mul_le_mul_of_nonneg_left h_X_bound h_h_nn
    -- Now use h_denom_lower (s²-4h² ≥ 5s²/9).
    -- Goal: |h · X| ≤ M_h2 · π s²(s²-4h²) where M_h2 = 9(M_b|s|+4)/(5π s⁴) · h²
    have h_target : 9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) * h^2 *
        (Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2)) ≥
        h * (M_b * |T₁ - T₂| * h + 4 * h) := by
      -- Goal: h * (M_b * |T₁-T₂| * h + 4 * h) ≤ (M_01_3) * h² * π s²(s²-4h²)
      -- where M_01_3 = 9(M_b|s|+4)/(5πs⁴).
      -- LHS = (M_b|s|+4) h²
      -- RHS = (9(M_b|s|+4)/(5πs⁴)) · h² · πs²(s²-4h²)
      --     = (9(M_b|s|+4) · s² · (s²-4h²) / (5 s⁴)) · h²
      --     ≥ (9(M_b|s|+4) · s² · 5s²/9 / (5 s⁴)) · h² (using s²-4h² ≥ 5s²/9)
      --     = (M_b|s|+4) · h²
      have h_h2_pos : 0 ≤ h^2 := sq_nonneg h
      have h_factor_nn : 0 ≤ M_b * |T₁ - T₂| + 4 := by positivity
      have h_5s4_pos : 0 < 5 * (T₁ - T₂)^4 := by positivity
      have h_lhs_eq : h * (M_b * |T₁ - T₂| * h + 4 * h) = (M_b * |T₁ - T₂| + 4) * h^2 := by ring
      have h_rhs_eq :
          9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) * h^2 *
            (Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2)) =
          9 * (M_b * |T₁ - T₂| + 4) * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) /
            (5 * (T₁ - T₂)^4) * h^2 := by
        have h_pi_ne : Real.pi ≠ 0 := Real.pi_ne_zero
        have h_s2_ne : (T₁ - T₂)^2 ≠ 0 := by positivity
        have h_s4_ne : (T₁ - T₂)^4 ≠ 0 := by positivity
        field_simp
      rw [h_lhs_eq, h_rhs_eq]
      -- Goal: (M_b|s|+4) h² ≤ 9(M_b|s|+4) s² (s²-4h²)/(5 s⁴) · h²
      -- Divide out h²: need (M_b|s|+4) ≤ 9(M_b|s|+4) s² (s²-4h²)/(5 s⁴)
      -- i.e., 5 s⁴ ≤ 9 s² (s²-4h²) (using M_b|s|+4 ≥ 0)
      -- i.e., 5 s² ≤ 9 (s²-4h²) (dividing by s²)
      -- which follows from s²-4h² ≥ 5s²/9
      have h_inner_ineq : 5 * (T₁ - T₂)^4 ≤
          9 * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) := by
        have h_step1 : 9 * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) ≥
            9 * (T₁ - T₂)^2 * (5 * (T₁ - T₂)^2 / 9) :=
          mul_le_mul_of_nonneg_left h_denom_lower (by positivity)
        have h_step2 : 9 * (T₁ - T₂)^2 * (5 * (T₁ - T₂)^2 / 9) = 5 * (T₁ - T₂)^4 := by ring
        linarith
      have h_div_le : (M_b * |T₁ - T₂| + 4) ≤
          9 * (M_b * |T₁ - T₂| + 4) * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) /
            (5 * (T₁ - T₂)^4) := by
        rw [le_div_iff₀ h_5s4_pos]
        have step1 :
            (M_b * |T₁ - T₂| + 4) * (5 * (T₁ - T₂)^4) ≤
            (M_b * |T₁ - T₂| + 4) *
              (9 * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2)) :=
          mul_le_mul_of_nonneg_left h_inner_ineq h_factor_nn
        linarith
      have h_target_inner :
          (M_b * |T₁ - T₂| + 4) * h^2 ≤
          9 * (M_b * |T₁ - T₂| + 4) * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2) /
            (5 * (T₁ - T₂)^4) * h^2 :=
        mul_le_mul_of_nonneg_right h_div_le h_h2_pos
      linarith [h_target_inner]
    linarith [h_h_X_bound, h_target]
  -- Now use h_jet_01_v3 and h_n_01 to express D = E₁ + E₂ + E₃.
  -- D = jet_value - n12_value
  -- jet_value = ((s²-4h²)(δ_sin-α_sin) + s²(β_sin-γ_sin) + 2sh(β_sin+γ_sin)) / (π s(s²-4h²) · 4h)
  -- n12_value = (Δ_sin - q T₂ s Δ_cos) / (π s²)
  -- We claim: D = E₁ + E₂ + E₃.
  have h_D_decomp :
      (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1 = E₁ + E₂ + E₃ := by
    rw [Matrix.sub_apply, h_jet_01_v3, h_n_01]
    -- Goal: (((s²-4h²)(δ_sin-α_sin) + s²(β_sin-γ_sin) + 2sh(β_sin+γ_sin))/π / (s(s²-4h²))) / (4h)
    --       - (Δ_sin - q T₂ s Δ_cos)/(π s²) = E₁ + E₂ + E₃
    show _ = E₁ + E₂ + E₃
    rw [show E₁ = (R_αδ + R_βγ) / (4 * h * Real.pi * (T₁ - T₂)) from rfl]
    rw [show E₂ = R_sym / (2 * Real.pi * (T₁ - T₂)^2) from rfl]
    rw [show E₃ = h * (β_sin * ((T₁ - T₂) + 2 * h) - γ_sin * ((T₁ - T₂) - 2 * h)) /
        (Real.pi * (T₁ - T₂)^2 * ((T₁ - T₂)^2 - 4 * h^2)) from rfl]
    rw [hR_αδ_def, hR_βγ_def, hR_sym_def, hΔ_sin_def, hΔ_cos_def]
    field_simp
    ring
  rw [h_D_decomp]
  -- Now bound |E₁ + E₂ + E₃| ≤ |E₁| + |E₂| + |E₃| and use the bounds.
  have h_tri₁ : |E₁ + E₂ + E₃| ≤ |E₁ + E₂| + |E₃| := abs_add_le _ _
  have h_tri₂ : |E₁ + E₂| ≤ |E₁| + |E₂| := abs_add_le _ _
  calc |E₁ + E₂ + E₃|
      ≤ |E₁ + E₂| + |E₃| := h_tri₁
    _ ≤ (|E₁| + |E₂|) + |E₃| := by linarith
    _ ≤ M_a / (2 * Real.pi * |T₁ - T₂|) * h^2 +
        M_sym / (2 * Real.pi * (T₁ - T₂)^2) * h^2 +
        9 * (M_b * |T₁ - T₂| + 4) / (5 * Real.pi * (T₁ - T₂)^4) * h^2 := by
        linarith [h_E1_bound, h_E2_bound, h_E3_bound]
    _ = M_01 * h^2 := by rw [hM_01_def]; ring

/-- Bound on entry `(1, 0)` of `P_h C_h(T₁, T₂) P_h^⊤ − (1/π) N₁₂(T₁, T₂)`
    for `h ∈ (0, |s|/3]`.  Derived from `cross_rate_bound_01` via the
    identity `D₁₀ = 2 F − D₀₁` where `F = (sin δ − sin α − 2(q₁−q₂) cos Δ · h) /
    (4hπs)` is the "α/δ residual" piece. -/
private lemma cross_rate_bound_10 (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ |T₁ - T₂| / 3 →
      |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 1 0| ≤ M * h^2 := by
  set R : ℝ := |T₁ - T₂| / 3 with hR_def
  have hs_ne : T₁ - T₂ ≠ 0 := sub_ne_zero.mpr hT
  have hs_abs_pos : 0 < |T₁ - T₂| := abs_pos.mpr hs_ne
  have hR_pos : 0 < R := by show 0 < |T₁ - T₂| / 3; linarith
  obtain ⟨M_01, hM_01_nn, hM_01⟩ := cross_rate_bound_01 T₁ T₂ hT
  obtain ⟨M_a, hM_a_nn, hM_a⟩ := cross_sin_pair_anti_lin_bound T₁ T₂ R hR_pos
  -- M_10 = M_a/(2π|s|) + M_01.
  set M_10 : ℝ := M_a / (2 * Real.pi * |T₁ - T₂|) + M_01 with hM_10_def
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  have hM_10_nn : 0 ≤ M_10 := by
    show 0 ≤ M_a / (2 * Real.pi * |T₁ - T₂|) + M_01
    have h1 : 0 ≤ M_a / (2 * Real.pi * |T₁ - T₂|) := by positivity
    linarith
  refine ⟨M_10, hM_10_nn, ?_⟩
  intro h h_pos h_le
  have h_abs_le : |h| ≤ R := by rw [abs_of_pos h_pos]; exact h_le
  obtain ⟨h_pK_00, h_pK_01, h_pK_10, h_pK_11⟩ :=
    crossBlock_apply T₁ T₂ h hT h_pos h_le
  obtain ⟨_, h_N_01, h_N_10, _⟩ := N12_smul_apply T₁ T₂ hT
  obtain ⟨h_anti_αδ, _⟩ := hM_a h h_abs_le
  obtain ⟨_, hsp_ne, hsm_ne⟩ := cross_denominators_nonzero T₁ T₂ h hT h_pos h_le
  have h_h_abs_eq : |h| = h := abs_of_pos h_pos
  have h_h_pow_eq : |h|^3 = h^3 := by rw [h_h_abs_eq]
  -- F = R_αδ/(4hπs).
  set α_sin := Real.sin (theta (T₁ - h) - theta (T₂ - h))
  set δ_sin := Real.sin (theta (T₁ + h) - theta (T₂ + h))
  set Δ_cos := Real.cos (theta T₁ - theta T₂)
  set R_αδ := δ_sin - α_sin - 2 * (q T₁ - q T₂) * Δ_cos * h with hR_αδ_def
  have hR_αδ_b : |R_αδ| ≤ M_a * h^3 := by
    have := h_anti_αδ
    rw [h_h_pow_eq] at this
    exact this
  set F := R_αδ / (4 * h * Real.pi * (T₁ - T₂)) with hF_def
  -- |F| ≤ M_a/(4π|s|) · h².
  have h_F_bound : |F| ≤ M_a / (4 * Real.pi * |T₁ - T₂|) * h^2 := by
    show |R_αδ / (4 * h * Real.pi * (T₁ - T₂))| ≤ _
    rw [abs_div]
    have h_denom_eq : |4 * h * Real.pi * (T₁ - T₂)| =
        4 * h * Real.pi * |T₁ - T₂| := by
      rw [show 4 * h * Real.pi * (T₁ - T₂) =
          (4 * h * Real.pi) * (T₁ - T₂) from by ring]
      rw [abs_mul]
      rw [show |4 * h * Real.pi| = 4 * h * Real.pi from
          abs_of_pos (by positivity)]
    rw [h_denom_eq]
    rw [div_le_iff₀ (by positivity : (0:ℝ) < 4 * h * Real.pi * |T₁ - T₂|)]
    have h_eq : M_a * h^3 =
        M_a / (4 * Real.pi * |T₁ - T₂|) * h^2 * (4 * h * Real.pi * |T₁ - T₂|) := by
      have hπ_ne_local : Real.pi ≠ 0 := Real.pi_ne_zero
      have hs_abs_ne : |T₁ - T₂| ≠ 0 := hs_abs_pos.ne'
      field_simp
    linarith [hR_αδ_b, h_eq]
  -- Identity: D_(1,0) = 2F - D_(0,1).
  -- D_(0,1) = jet_01 - n12_01, D_(1,0) = jet_10 - n12_10.
  -- jet_10 + jet_01 = (sin δ - sin α)/(2hπs).
  -- n12_10 + n12_01 = (q₁-q₂) cos Δ/(πs).
  -- 2F = (sin δ - sin α - 2(q₁-q₂) cos Δ h)/(2hπs) = (sin δ - sin α)/(2hπs) - (q₁-q₂) cos Δ/(πs)
  --    = (jet_10 + jet_01) - (n12_10 + n12_01)
  --    = (jet_10 - n12_10) + (jet_01 - n12_01) = D_(1,0) + D_(0,1)
  -- Hence D_(1,0) = 2F - D_(0,1).
  have h_D_id :
      (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 1 0 =
      2 * F -
      (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1 := by
    rw [Matrix.sub_apply, Matrix.sub_apply]
    rw [jet_cross_matrix_apply_10 T₁ T₂ h hT h_pos h_le]
    rw [jet_cross_matrix_apply_01 T₁ T₂ h hT h_pos h_le]
    rw [h_pK_00, h_pK_01, h_pK_10, h_pK_11]
    rw [h_N_01, h_N_10]
    rw [hF_def, hR_αδ_def]
    field_simp
    ring
  rw [h_D_id]
  have h_D_01 := hM_01 h h_pos h_le
  have h_tri : |2 * F - (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1| ≤
      |2 * F| + |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1| := abs_sub _ _
  have h_2F_bound : |2 * F| = 2 * |F| := by
    rw [abs_mul, show |(2:ℝ)| = 2 from by norm_num]
  calc |2 * F - (pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1|
      ≤ |2 * F| + |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1| := h_tri
    _ = 2 * |F| + |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) 0 1| := by rw [h_2F_bound]
    _ ≤ 2 * (M_a / (4 * Real.pi * |T₁ - T₂|) * h^2) + M_01 * h^2 := by linarith
    _ = M_10 * h^2 := by rw [hM_10_def]; ring

/-- Cross-block jet-limit with explicit `O(h²)` rate.  Entrywise: for
    fixed separation `s = T₁ − T₂ ≠ 0`, there is `M(|s|⁻¹) ≥ 0` such
    that for `h ∈ (0, |s|/3]`,
        `|((P_h C_h(T₁,T₂) P_h^⊤) − (1/π) N₁₂(T₁,T₂)) i j| ≤ M h²`. -/
axiom cross_block_jet_limit_rate (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ |T₁ - T₂| / 3 →
      ∀ i j : Fin 2,
        |(pointToJetTransform h * crossBlock T₁ T₂ h *
            (pointToJetTransform h).transpose -
          (1 / Real.pi) • N12 T₁ T₂) i j| ≤ M * h^2

/-! ## Jet-limit theorems (derived from the rate axioms by squeeze) -/

/-- Helper: `M * h^2 → 0` as `h → 0⁺`. -/
private lemma mul_sq_tendsto_zero (M : ℝ) :
    Filter.Tendsto (fun h : ℝ => M * h^2) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
  have h₀ : Filter.Tendsto (fun h : ℝ => M * h^2) (nhds 0) (nhds 0) := by
    have hcont : Continuous (fun h : ℝ => M * h^2) :=
      continuous_const.mul (continuous_id.pow 2)
    have h_at0 : (M * (0 : ℝ)^2) = 0 := by ring
    have := hcont.tendsto 0
    rw [h_at0] at this
    exact this
  exact h₀.mono_left nhdsWithin_le_nhds

/-- Same-point jet-limit:
    `P_h * A_h(T) * P_h^⊤ → J(T)` as `h → 0⁺`.
    Cf. Lemma `lem:same-point-jet-limit`.
    Derived from `same_point_jet_limit_rate` by entrywise squeeze. -/
theorem same_point_jet_limit (T : ℝ) :
    Filter.Tendsto
      (fun h => let P := pointToJetTransform h
                P * samePointBlock T h * P.transpose)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds (J T)) := by
  obtain ⟨M, _, hM⟩ := same_point_jet_limit_rate T
  refine tendsto_pi_nhds.mpr fun i => tendsto_pi_nhds.mpr fun j => ?_
  have h_filter : ∀ᶠ h in nhdsWithin (0 : ℝ) (Set.Ioi 0),
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) i j| ≤ M * h^2 := by
    filter_upwards [Ioo_mem_nhdsGT (zero_lt_one : (0:ℝ) < 1)] with h hh
    exact hM h hh.1 (le_of_lt hh.2) i j
  have h_bound_to_zero := mul_sq_tendsto_zero M
  have h_target_const : Filter.Tendsto (fun _ : ℝ => J T i j)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0)) (nhds (J T i j)) :=
    tendsto_const_nhds
  have h_lower : Filter.Tendsto (fun h : ℝ => J T i j - M * h^2)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0)) (nhds (J T i j)) := by
    have := h_target_const.sub h_bound_to_zero
    simpa using this
  have h_upper : Filter.Tendsto (fun h : ℝ => J T i j + M * h^2)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0)) (nhds (J T i j)) := by
    have := h_target_const.add h_bound_to_zero
    simpa using this
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le' h_lower h_upper
  · filter_upwards [h_filter] with h hh
    have habs := abs_le.mp hh
    simp only [Matrix.sub_apply] at habs
    linarith [habs.1]
  · filter_upwards [h_filter] with h hh
    have habs := abs_le.mp hh
    simp only [Matrix.sub_apply] at habs
    linarith [habs.2]

/-- Cross-block jet-limit:
    `P_h * C_h(T₁, T₂) * P_h^⊤ → (1/π) · N₁₂(T₁, T₂)` as `h → 0⁺`,
    for `T₁ ≠ T₂`.
    Cf. Lemma `lem:cross-block-jet-limit`.
    Derived from `cross_block_jet_limit_rate` by entrywise squeeze. -/
theorem cross_block_jet_limit (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    Filter.Tendsto
      (fun h => let P := pointToJetTransform h
                P * crossBlock T₁ T₂ h * P.transpose)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds ((1 / Real.pi) • N12 T₁ T₂)) := by
  obtain ⟨M, _, hM⟩ := cross_block_jet_limit_rate T₁ T₂ hT
  have h_pos : (0 : ℝ) < |T₁ - T₂| / 3 := by
    have : |T₁ - T₂| > 0 := abs_pos.mpr (sub_ne_zero.mpr hT)
    linarith
  refine tendsto_pi_nhds.mpr fun i => tendsto_pi_nhds.mpr fun j => ?_
  have h_filter : ∀ᶠ h in nhdsWithin (0 : ℝ) (Set.Ioi 0),
      |(pointToJetTransform h * crossBlock T₁ T₂ h *
          (pointToJetTransform h).transpose -
        (1 / Real.pi) • N12 T₁ T₂) i j| ≤ M * h^2 := by
    filter_upwards [Ioo_mem_nhdsGT h_pos] with h hh
    exact hM h hh.1 (le_of_lt hh.2) i j
  have h_bound_to_zero := mul_sq_tendsto_zero M
  have h_target_const : Filter.Tendsto (fun _ : ℝ => ((1 / Real.pi) • N12 T₁ T₂) i j)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0))
      (nhds (((1 / Real.pi) • N12 T₁ T₂) i j)) :=
    tendsto_const_nhds
  have h_lower : Filter.Tendsto (fun h : ℝ => ((1 / Real.pi) • N12 T₁ T₂) i j - M * h^2)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0))
      (nhds (((1 / Real.pi) • N12 T₁ T₂) i j)) := by
    have := h_target_const.sub h_bound_to_zero
    simpa using this
  have h_upper : Filter.Tendsto (fun h : ℝ => ((1 / Real.pi) • N12 T₁ T₂) i j + M * h^2)
      (nhdsWithin (0 : ℝ) (Set.Ioi 0))
      (nhds (((1 / Real.pi) • N12 T₁ T₂) i j)) := by
    have := h_target_const.add h_bound_to_zero
    simpa using this
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le' h_lower h_upper
  · filter_upwards [h_filter] with h hh
    have habs := abs_le.mp hh
    simp only [Matrix.sub_apply] at habs
    linarith [habs.1]
  · filter_upwards [h_filter] with h hh
    have habs := abs_le.mp hh
    simp only [Matrix.sub_apply] at habs
    linarith [habs.2]

/-! ## Same-point Gram positivity -/

/-- Same-point Gram determinant `D_J(T) = 4 q⁴ + 2 q q'' - 3 (q')²`. -/
noncomputable def D_J (T : ℝ) : ℝ :=
  4 * (q T)^4 + 2 * q T * qDoublePrime T - 3 * (qPrime T)^2

/-- Trace identity for `J(T)`. -/
theorem J_trace (T : ℝ) :
    (J T).trace = (2 * (q T)^3 + 24 * q T + qDoublePrime T) / (12 * Real.pi) := by
  have hπ : (Real.pi : ℝ) ≠ 0 := Real.pi_ne_zero
  simp only [J, Matrix.trace_smul, Matrix.trace_fin_two_of, smul_eq_mul]
  field_simp
  ring

/-- Determinant identity for `J(T)`. -/
theorem J_det (T : ℝ) :
    (J T).det = D_J T / (12 * Real.pi^2) := by
  have hπ : (Real.pi : ℝ) ≠ 0 := Real.pi_ne_zero
  simp only [J, Matrix.det_smul, Matrix.det_fin_two_of, Fintype.card_fin, D_J]
  field_simp
  ring

/-- Algebraic Gram criterion: `J(T) ≻ 0` iff `q(T) > 0` and `D_J(T) > 0`.

    Forward direction: probe `J(T)` against `e₁ = (1, 0)` (giving
    `2 q(T) / π > 0`) and `(q'(T), -4 q(T))` (giving
    `2 q(T) D_J(T) / (3 π) > 0`).

    Reverse direction: the sum-of-squares identity
        `24 q(T) π · (xᵀ J(T) x) = 3 (4 q(T) x₀ + q'(T) x₁)² + D_J(T) x₁²`
    (valid when `q(T) > 0`) shows the right-hand side vanishes only at
    `x = 0`. -/
theorem algebraic_gram_criterion (T : ℝ) :
    (J T).PosDef ↔ 0 < q T ∧ 0 < D_J T := by
  have hπpos : (0:ℝ) < Real.pi := Real.pi_pos
  have hπne : (Real.pi : ℝ) ≠ 0 := ne_of_gt hπpos
  -- Closed-form quadratic form `xᵀ J(T) x`
  have hQF : ∀ x : Fin 2 → ℝ,
      x ⬝ᵥ (J T *ᵥ x) =
        (2 * q T * (x 0)^2 + qPrime T * x 0 * x 1 +
         ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2) / Real.pi := by
    intro x
    simp only [J, dotProduct, mulVec, Fin.sum_univ_two,
               Matrix.smul_apply, smul_eq_mul,
               Matrix.cons_val_zero, Matrix.cons_val_one,
               Matrix.of_apply]
    field_simp
    ring
  -- Specialized values at the two probe vectors
  have hQF_e1 :
      (![1, 0] : Fin 2 → ℝ) ⬝ᵥ (J T *ᵥ ![1, 0]) = 2 * q T / Real.pi := by
    rw [hQF]
    simp
  have hQF_e2 :
      (![qPrime T, -4 * q T] : Fin 2 → ℝ) ⬝ᵥ
          (J T *ᵥ ![qPrime T, -4 * q T]) =
        2 * q T * D_J T / (3 * Real.pi) := by
    rw [hQF]
    unfold D_J
    simp
    field_simp
    ring
  -- Star is the identity on `Fin 2 → ℝ`
  have hstar : ∀ x : Fin 2 → ℝ, (star x : Fin 2 → ℝ) = x := by
    intro x; funext i; exact star_trivial _
  -- `J(T)` is real symmetric, hence Hermitian
  have hHerm : (J T).IsHermitian := by
    show (J T)ᴴ = J T
    funext i j
    fin_cases i <;> fin_cases j <;>
      simp [J, Matrix.conjTranspose_apply, Matrix.smul_apply,
            Matrix.cons_val_zero, Matrix.cons_val_one]
  refine ⟨fun hP => ?_, fun ⟨hQ, hD⟩ => ?_⟩
  · -- Forward direction
    rw [Matrix.posDef_iff_dotProduct_mulVec] at hP
    obtain ⟨_, hPos⟩ := hP
    -- Step 1: `q T > 0` from probing with `(1, 0)`
    have he1 : (![1, 0] : Fin 2 → ℝ) ≠ 0 := by
      intro h
      have h0 := congr_fun h 0
      simp at h0
    have h1 := hPos he1
    rw [hstar, hQF_e1] at h1
    -- h1 : 0 < 2 * q T / Real.pi
    have hQ : 0 < q T := by
      have h_2q : 0 < 2 * q T := by
        have heq : 2 * q T = (2 * q T / Real.pi) * Real.pi := by field_simp
        rw [heq]; exact mul_pos h1 hπpos
      linarith
    refine ⟨hQ, ?_⟩
    -- Step 2: `D_J T > 0` from probing with `(qPrime T, -4 q T)`
    have hQne : q T ≠ 0 := ne_of_gt hQ
    have he2 : (![qPrime T, -4 * q T] : Fin 2 → ℝ) ≠ 0 := by
      intro h
      have h1' := congr_fun h 1
      simp at h1'
      exact hQne (by linarith)
    have h2 := hPos he2
    rw [hstar, hQF_e2] at h2
    -- h2 : 0 < 2 * q T * D_J T / (3 * Real.pi)
    have h_pos_factor : 0 < 2 * q T / (3 * Real.pi) := by positivity
    have heq : 2 * q T * D_J T / (3 * Real.pi) =
               (2 * q T / (3 * Real.pi)) * D_J T := by ring
    rw [heq] at h2
    exact (mul_pos_iff_of_pos_left h_pos_factor).mp h2
  · -- Reverse direction
    have hQne : q T ≠ 0 := ne_of_gt hQ
    rw [Matrix.posDef_iff_dotProduct_mulVec]
    refine ⟨hHerm, ?_⟩
    intro x hx
    rw [hstar, hQF]
    -- Sum-of-squares identity
    have hSOS :
        (2 * q T * (x 0)^2 + qPrime T * x 0 * x 1 +
         ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2) / Real.pi =
        (3 * (4 * q T * x 0 + qPrime T * x 1)^2 + D_J T * (x 1)^2) /
          (24 * q T * Real.pi) := by
      unfold D_J
      field_simp
      ring
    rw [hSOS]
    have h_den : 0 < 24 * q T * Real.pi := by positivity
    apply div_pos _ h_den
    by_cases hx1 : x 1 = 0
    · -- `x 1 = 0` forces `x 0 ≠ 0`
      have hx0 : x 0 ≠ 0 := by
        intro h0
        apply hx
        funext i
        fin_cases i
        · simp [h0]
        · simp [hx1]
      have h_inner : 4 * q T * x 0 + qPrime T * x 1 = 4 * q T * x 0 := by
        rw [hx1]; ring
      rw [h_inner, hx1]
      have h_sq_pos : 0 < (4 * q T * x 0)^2 := by positivity
      nlinarith
    · -- `x 1 ≠ 0`: `D_J T * (x 1)^2 > 0`
      have h_x1sq : 0 < (x 1)^2 := by positivity
      have h_term1 : 0 ≤ 3 * (4 * q T * x 0 + qPrime T * x 1)^2 := by positivity
      have h_term2 : 0 < D_J T * (x 1)^2 := mul_pos hD h_x1sq
      linarith

/-- Algebraic lower bound for `D_J(T)`.  If `q(T) ≥ 2`, `|q'(T)| ≤ 1`,
    and `|q''(T)| ≤ 1`, then `D_J(T) ≥ 57 > 0`.

    Reduction: `4 q⁴ + 2 q q'' - 3 (q')² ≥ 4 q⁴ - 2 q - 3`, and the
    identity `(q-2)(4q³+8q²+16q+30) = 4q⁴ - 2q - 60` shows
    `4 q⁴ - 2 q ≥ 60` for `q ≥ 2`. -/
private lemma D_J_lower_bound (T : ℝ) (hQ : 2 ≤ q T)
    (hQp : |qPrime T| ≤ 1) (hQpp : |qDoublePrime T| ≤ 1) :
    0 < D_J T := by
  unfold D_J
  have hqp_sq : (qPrime T)^2 ≤ 1 := by
    have h := sq_abs (qPrime T)
    nlinarith [hQp, abs_nonneg (qPrime T)]
  have hqpp_lb : -1 ≤ qDoublePrime T := neg_le_of_abs_le hQpp
  have h_q_pos : 0 < q T := by linarith
  have h_factor :
      (q T - 2) * (4 * (q T)^3 + 8 * (q T)^2 + 16 * q T + 30) =
        4 * (q T)^4 - 2 * q T - 60 := by ring
  have h_factor_nn :
      0 ≤ (q T - 2) * (4 * (q T)^3 + 8 * (q T)^2 + 16 * q T + 30) := by
    apply mul_nonneg
    · linarith
    · positivity
  nlinarith [h_factor, h_factor_nn, hqp_sq, hqpp_lb, h_q_pos, hQ]

/-- For sufficiently large `T`, the chart derivatives satisfy
    `q(T) ≥ 2`, `|q'(T)| ≤ 1`, and `|q''(T)| ≤ 1`.

    Chains the Riemann–Siegel asymptotics from §2: the lower bound
    `q(T) ≥ (1/2) log(T/(4π)) - C₁/T²` of
    `phase_derivative_lower_bound` exceeds `2` once
    `log(T/(4π)) ≥ 6` and `C₁/T² ≤ 1`; the bounds
    `|q'(T) - 1/(2T)| ≤ C₂/T³` and `|q''(T) + 1/(2T²)| ≤ C₂/T⁴`
    of `theta_derivative_asymptotics` force `|q'(T)| ≤ 1` and
    `|q''(T)| ≤ 1` once `T ≥ 1 + 2 C₂`. -/
private lemma analytic_bounds_eventual :
    ∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T →
      2 ≤ q T ∧ |qPrime T| ≤ 1 ∧ |qDoublePrime T| ≤ 1 := by
  obtain ⟨T₁, C₁, hT₁_pos, hC₁_nn, hq_lb⟩ := phase_derivative_lower_bound_dyadic
  obtain ⟨T₂, C₂, hT₂_pos, hC₂_nn, hasymp⟩ := theta_derivative_asymptotics_dyadic
  have h_4π_pos : (0 : ℝ) < 4 * Real.pi := by positivity
  set Tlog : ℝ := 4 * Real.pi * Real.exp 6 with hTlog
  set Tcoef : ℝ := 1 + C₁ + 2 * C₂ with hTcoef
  refine ⟨max (max T₁ T₂) (max Tlog Tcoef), ?_, ?_⟩
  · have h1 : 0 < max T₁ T₂ := lt_max_of_lt_left hT₁_pos
    exact lt_max_of_lt_left h1
  intro T hT
  have hT_T₁ : T₁ ≤ T :=
    le_trans (le_max_left _ _) (le_trans (le_max_left _ _) hT)
  have hT_T₂ : T₂ ≤ T :=
    le_trans (le_max_right _ _) (le_trans (le_max_left _ _) hT)
  have hT_log : Tlog ≤ T :=
    le_trans (le_max_left _ _) (le_trans (le_max_right _ _) hT)
  have hT_coef : Tcoef ≤ T :=
    le_trans (le_max_right _ _) (le_trans (le_max_right _ _) hT)
  have h_exp_pos : (0 : ℝ) < Real.exp 6 := Real.exp_pos 6
  have hT_pos : 0 < T := by
    have : 0 < Tlog := by rw [hTlog]; positivity
    linarith
  have hT_ge_one : 1 ≤ T := by
    rw [hTcoef] at hT_coef
    linarith
  have hT_sq_pos : 0 < T^2 := by positivity
  have hT_cube_pos : 0 < T^3 := by positivity
  have hT_four_pos : 0 < T^4 := by positivity
  -- (1) q T ≥ 2
  have h_q_ge_2 : 2 ≤ q T := by
    have h_T_ratio : Real.exp 6 ≤ T / (4 * Real.pi) := by
      rw [le_div_iff₀ h_4π_pos]
      have : 4 * Real.pi * Real.exp 6 ≤ T := by rw [← hTlog]; exact hT_log
      linarith
    have h_log_T : 6 ≤ Real.log (T / (4 * Real.pi)) := by
      calc 6 = Real.log (Real.exp 6) := (Real.log_exp 6).symm
        _ ≤ Real.log (T / (4 * Real.pi)) := Real.log_le_log h_exp_pos h_T_ratio
    have h_C₁_small : C₁ / T^2 ≤ 1 := by
      have h_T_sq : C₁ ≤ T^2 := by
        rw [hTcoef] at hT_coef
        nlinarith [hT_ge_one, hC₁_nn, hC₂_nn]
      rw [div_le_one hT_sq_pos]; exact h_T_sq
    have h_qbd := hq_lb T T hT_T₁ (by linarith) (by linarith)
    linarith
  -- (2) |qPrime T| ≤ 1 and |qDoublePrime T| ≤ 1
  obtain ⟨_, hqp_bd, hqpp_bd⟩ := hasymp T T hT_T₂ (by linarith) (by linarith)
  have h_C₂_T_cube : C₂ / T^3 ≤ 1/2 := by
    -- T³ ≥ T ≥ 1 + 2 C₂ ≥ 2 C₂
    have hT3_ge : 2 * C₂ ≤ T^3 := by
      have h_T_ge_2C₂ : 2 * C₂ ≤ T := by rw [hTcoef] at hT_coef; linarith
      have h_T3_ge_T : T ≤ T^3 := by nlinarith [hT_ge_one]
      linarith
    rw [div_le_iff₀ hT_cube_pos]; linarith
  have h_C₂_T_four : C₂ / T^4 ≤ 1/2 := by
    have hT4_ge : 2 * C₂ ≤ T^4 := by
      have h_T_ge_2C₂ : 2 * C₂ ≤ T := by rw [hTcoef] at hT_coef; linarith
      have h_T4_ge_T : T ≤ T^4 := by nlinarith [hT_ge_one]
      linarith
    rw [div_le_iff₀ hT_four_pos]; linarith
  have h_1_2T_le : 1 / (2 * T) ≤ 1/2 := by
    have h2T : 0 < 2 * T := by linarith
    rw [div_le_div_iff₀ h2T (by norm_num : (0:ℝ) < 2)]
    nlinarith
  have h_1_2T2_le : 1 / (2 * T^2) ≤ 1/2 := by
    have h2T2 : 0 < 2 * T^2 := by positivity
    rw [div_le_div_iff₀ h2T2 (by norm_num : (0:ℝ) < 2)]
    nlinarith [hT_ge_one]
  have h_1_2T_pos : 0 ≤ 1 / (2 * T) := by positivity
  have h_qp_le : |qPrime T| ≤ 1 := by
    rw [abs_le]
    obtain ⟨h_lo, h_hi⟩ := abs_le.mp hqp_bd
    refine ⟨?_, ?_⟩
    · linarith
    · linarith
  have h_qpp_le : |qDoublePrime T| ≤ 1 := by
    rw [abs_le]
    obtain ⟨h_lo, h_hi⟩ := abs_le.mp hqpp_bd
    have h_pos : 0 ≤ 1 / (2 * T^2) := by positivity
    have h_neg : (-1 : ℝ) / (2 * T^2) = -(1 / (2 * T^2)) := by ring
    rw [h_neg] at h_lo h_hi
    refine ⟨?_, ?_⟩
    · linarith
    · linarith
  exact ⟨h_q_ge_2, h_qp_le, h_qpp_le⟩

/-- Eventual same-point Gram positive-definiteness: at sufficiently
    large `T`, `J(T) ≻ 0`.

    Chains `analytic_bounds_eventual` (q ≥ 2 ∧ |q'| ≤ 1 ∧ |q''| ≤ 1
    eventually), `D_J_lower_bound` (gives `D_J > 0` from those bounds),
    and `algebraic_gram_criterion` (gives `PosDef ↔ q > 0 ∧ D_J > 0`).

    This is the eventual-PosDef package; for the spectral floor used
    in whitening, see `same_point_gram_uniform_floor`. -/
theorem same_point_gram_posdef_eventual :
    ∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T → (J T).PosDef := by
  obtain ⟨T₀, hT₀_pos, hbounds⟩ := analytic_bounds_eventual
  refine ⟨T₀, hT₀_pos, ?_⟩
  intro T hT
  obtain ⟨hQ, hQp, hQpp⟩ := hbounds T hT
  have h_q_pos : 0 < q T := by linarith
  have h_DJ_pos : 0 < D_J T := D_J_lower_bound T hQ hQp hQpp
  exact (algebraic_gram_criterion T).mpr ⟨h_q_pos, h_DJ_pos⟩

/-- Backwards-compatible alias for `same_point_gram_posdef_eventual`. -/
theorem same_point_gram_positivity :
    ∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T → (J T).PosDef :=
  same_point_gram_posdef_eventual

/-- Algebraic spectral floor: under `q(T) ≥ 5`, `|q'(T)| ≤ 1`, and
    `|q''(T)| ≤ 1`, the quadratic form `xᵀ J(T) x` dominates `xᵀ x`.

    Proof via the SOS identity (purely algebraic, valid for `2q − π > 0`):
        `144 (2q − π) · π · (xᵀ J x − xᵀ x) =
            (12 (2q − π) x₀ + 6 q' x₁)²
            + (12 (2q − π) (q'' + 2q³ − 12π) − 36 q'²) · x₁²`.
    For `q ≥ 5`, both summands are nonneg (`12(2q−π) ≥ 72`,
    `q'' + 2q³ − 12π ≥ 201`, `36 q'² ≤ 36 ≪ 72·201`). -/
private lemma J_floor_quadform (T : ℝ) (hQ : 5 ≤ q T)
    (hQp : |qPrime T| ≤ 1) (hQpp : |qDoublePrime T| ≤ 1) :
    ∀ x : Fin 2 → ℝ, x ⬝ᵥ ((J T) *ᵥ x) ≥ x ⬝ᵥ x := by
  intro x
  have hπpos : (0:ℝ) < Real.pi := Real.pi_pos
  have hπne : (Real.pi : ℝ) ≠ 0 := ne_of_gt hπpos
  have hπ_lt_4 : Real.pi < 4 := Real.pi_lt_four
  have h_q_pos : 0 < q T := by linarith
  have h_qp_sq : (qPrime T)^2 ≤ 1 := by
    have := sq_abs (qPrime T)
    nlinarith [hQp, abs_nonneg (qPrime T)]
  have h_qpp_lb : -1 ≤ qDoublePrime T := neg_le_of_abs_le hQpp
  have h_2q_minus_π : 6 ≤ 2 * q T - Real.pi := by linarith
  have h_q_sq : 25 ≤ (q T)^2 := by nlinarith [hQ]
  have h_q_cube : 125 ≤ (q T)^3 := by
    have : (q T)^3 = q T * (q T)^2 := by ring
    rw [this]; nlinarith [hQ, h_q_sq, h_q_pos]
  have h_inner_lb : 201 ≤ qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi := by
    have h12π : 12 * Real.pi ≤ 48 := by linarith
    linarith
  -- Closed-form quadratic form
  have hQF :
      x ⬝ᵥ ((J T) *ᵥ x) =
      (2 * q T * (x 0)^2 + qPrime T * x 0 * x 1 +
       ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2) / Real.pi := by
    simp only [J, dotProduct, mulVec, Fin.sum_univ_two,
               Matrix.smul_apply, smul_eq_mul,
               Matrix.cons_val_zero, Matrix.cons_val_one,
               Matrix.of_apply]
    field_simp
    ring
  have hQ_xx : x ⬝ᵥ x = (x 0)^2 + (x 1)^2 := by
    simp [dotProduct, Fin.sum_univ_two, sq]
  rw [ge_iff_le, hQF, hQ_xx, le_div_iff₀ hπpos]
  -- Goal: π · (x₀² + x₁²) ≤ 2q x₀² + q' x₀ x₁ + ((q'' + 2q³)/12) x₁²
  -- Multiply by 12 · 12(2q−π) > 0 and use the SOS identity.
  have h_a_pos : 0 < 12 * (2 * q T - Real.pi) := by linarith
  -- The SOS identity (proved by ring)
  have h_SOS :
      12 * (12 * (2 * q T - Real.pi)) *
        ((2 * q T) * (x 0)^2 + qPrime T * x 0 * x 1 +
         ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2 -
         Real.pi * ((x 0)^2 + (x 1)^2)) =
      (12 * (2 * q T - Real.pi) * x 0 + 6 * qPrime T * x 1)^2 +
      (12 * (2 * q T - Real.pi) *
        (qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi) -
        36 * (qPrime T)^2) * (x 1)^2 := by
    field_simp
    ring
  -- Both summands of the SOS RHS are non-negative
  have h_sq_nn : 0 ≤ (12 * (2 * q T - Real.pi) * x 0 + 6 * qPrime T * x 1)^2 :=
    sq_nonneg _
  have h_disc_nn :
      0 ≤ 12 * (2 * q T - Real.pi) *
            (qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi) -
          36 * (qPrime T)^2 := by
    have h1 : 72 ≤ 12 * (2 * q T - Real.pi) := by linarith
    have h2 : (12 * (2 * q T - Real.pi)) *
              (qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi) ≥ 72 * 201 := by
      have : 0 ≤ qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi := by linarith
      nlinarith [h1, h_inner_lb]
    have h3 : 36 * (qPrime T)^2 ≤ 36 := by linarith [h_qp_sq]
    linarith
  have h_disc_term_nn :
      0 ≤ (12 * (2 * q T - Real.pi) *
            (qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi) -
           36 * (qPrime T)^2) * (x 1)^2 :=
    mul_nonneg h_disc_nn (sq_nonneg _)
  have h_RHS_nn :
      0 ≤ (12 * (2 * q T - Real.pi) * x 0 + 6 * qPrime T * x 1)^2 +
          (12 * (2 * q T - Real.pi) *
            (qDoublePrime T + 2 * (q T)^3 - 12 * Real.pi) -
            36 * (qPrime T)^2) * (x 1)^2 := by linarith
  -- Combine: LHS = RHS ≥ 0; LHS = 144(2q-π) · (E - π · ‖x‖²)
  have h_LHS_nn :
      0 ≤ 12 * (12 * (2 * q T - Real.pi)) *
            ((2 * q T) * (x 0)^2 + qPrime T * x 0 * x 1 +
             ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2 -
             Real.pi * ((x 0)^2 + (x 1)^2)) := h_SOS ▸ h_RHS_nn
  have h_factor_pos : 0 < 12 * (12 * (2 * q T - Real.pi)) := by positivity
  -- Divide by the positive factor
  have h_E_nn :
      0 ≤ (2 * q T) * (x 0)^2 + qPrime T * x 0 * x 1 +
          ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2 -
          Real.pi * ((x 0)^2 + (x 1)^2) := by
    by_contra h
    have h_neg : (2 * q T) * (x 0)^2 + qPrime T * x 0 * x 1 +
                 ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2 -
                 Real.pi * ((x 0)^2 + (x 1)^2) < 0 := lt_of_not_ge h
    have : 12 * (12 * (2 * q T - Real.pi)) *
              ((2 * q T) * (x 0)^2 + qPrime T * x 0 * x 1 +
               ((qDoublePrime T + 2 * (q T)^3) / 12) * (x 1)^2 -
               Real.pi * ((x 0)^2 + (x 1)^2)) < 0 :=
      mul_neg_of_pos_of_neg h_factor_pos h_neg
    linarith
  linarith

/-- Uniform spectral floor for `J(T)`: at sufficiently large `T`,
    `xᵀ J(T) x ≥ xᵀ x` for every `x : Fin 2 → ℝ`.

    Combines `J_floor_quadform` (algebraic SOS, given `q ≥ 5`,
    `|q'| ≤ 1`, `|q''| ≤ 1`) with the §2 asymptotics — at threshold
    `T ≥ 4π exp(12)`, the bound `q(T) ≥ 5` follows from
    `phase_derivative_lower_bound_dyadic`, and `|q'|, |q''| ≤ 1` follow
    from `theta_derivative_asymptotics_dyadic`. -/
theorem same_point_gram_uniform_floor :
    ∃ T₀ : ℝ, 0 < T₀ ∧
      ∀ T : ℝ, T₀ ≤ T →
      ∀ x : Fin 2 → ℝ,
        x ⬝ᵥ ((J T) *ᵥ x) ≥ x ⬝ᵥ x := by
  obtain ⟨T₁, C₁, hT₁_pos, hC₁_nn, hq_lb⟩ := phase_derivative_lower_bound_dyadic
  obtain ⟨T₂, C₂, hT₂_pos, hC₂_nn, hasymp⟩ := theta_derivative_asymptotics_dyadic
  have h_4π_pos : (0 : ℝ) < 4 * Real.pi := by positivity
  set Tlog : ℝ := 4 * Real.pi * Real.exp 12 with hTlog
  set Tcoef : ℝ := 1 + C₁ + 2 * C₂ with hTcoef
  refine ⟨max (max T₁ T₂) (max Tlog Tcoef), ?_, ?_⟩
  · have h1 : 0 < max T₁ T₂ := lt_max_of_lt_left hT₁_pos
    exact lt_max_of_lt_left h1
  intro T hT x
  have hT_T₁ : T₁ ≤ T :=
    le_trans (le_max_left _ _) (le_trans (le_max_left _ _) hT)
  have hT_T₂ : T₂ ≤ T :=
    le_trans (le_max_right _ _) (le_trans (le_max_left _ _) hT)
  have hT_log : Tlog ≤ T :=
    le_trans (le_max_left _ _) (le_trans (le_max_right _ _) hT)
  have hT_coef : Tcoef ≤ T :=
    le_trans (le_max_right _ _) (le_trans (le_max_right _ _) hT)
  have h_exp_pos : (0 : ℝ) < Real.exp 12 := Real.exp_pos 12
  have hT_pos : 0 < T := by
    have : 0 < Tlog := by rw [hTlog]; positivity
    linarith
  have hT_ge_one : 1 ≤ T := by rw [hTcoef] at hT_coef; linarith
  have hT_sq_pos : 0 < T^2 := by positivity
  have hT_cube_pos : 0 < T^3 := by positivity
  have hT_four_pos : 0 < T^4 := by positivity
  -- q T ≥ 5
  have h_q_ge_5 : 5 ≤ q T := by
    have h_T_ratio : Real.exp 12 ≤ T / (4 * Real.pi) := by
      rw [le_div_iff₀ h_4π_pos]
      have : 4 * Real.pi * Real.exp 12 ≤ T := by rw [← hTlog]; exact hT_log
      linarith
    have h_log_T : 12 ≤ Real.log (T / (4 * Real.pi)) := by
      calc 12 = Real.log (Real.exp 12) := (Real.log_exp 12).symm
        _ ≤ Real.log (T / (4 * Real.pi)) := Real.log_le_log h_exp_pos h_T_ratio
    have h_C₁_small : C₁ / T^2 ≤ 1 := by
      have h_T_sq : C₁ ≤ T^2 := by
        rw [hTcoef] at hT_coef
        nlinarith [hT_ge_one, hC₁_nn, hC₂_nn]
      rw [div_le_one hT_sq_pos]; exact h_T_sq
    have h_qbd := hq_lb T T hT_T₁ (by linarith) (by linarith)
    linarith
  -- |q'| ≤ 1, |q''| ≤ 1
  obtain ⟨_, hqp_bd, hqpp_bd⟩ := hasymp T T hT_T₂ (by linarith) (by linarith)
  have h_C₂_T_cube : C₂ / T^3 ≤ 1/2 := by
    have hT3_ge : 2 * C₂ ≤ T^3 := by
      have h_T_ge_2C₂ : 2 * C₂ ≤ T := by rw [hTcoef] at hT_coef; linarith
      have h_T3_ge_T : T ≤ T^3 := by nlinarith [hT_ge_one]
      linarith
    rw [div_le_iff₀ hT_cube_pos]; linarith
  have h_C₂_T_four : C₂ / T^4 ≤ 1/2 := by
    have hT4_ge : 2 * C₂ ≤ T^4 := by
      have h_T_ge_2C₂ : 2 * C₂ ≤ T := by rw [hTcoef] at hT_coef; linarith
      have h_T4_ge_T : T ≤ T^4 := by nlinarith [hT_ge_one]
      linarith
    rw [div_le_iff₀ hT_four_pos]; linarith
  have h_1_2T_le : 1 / (2 * T) ≤ 1/2 := by
    have h2T : 0 < 2 * T := by linarith
    rw [div_le_div_iff₀ h2T (by norm_num : (0:ℝ) < 2)]
    nlinarith
  have h_1_2T2_le : 1 / (2 * T^2) ≤ 1/2 := by
    have h2T2 : 0 < 2 * T^2 := by positivity
    rw [div_le_div_iff₀ h2T2 (by norm_num : (0:ℝ) < 2)]
    nlinarith [hT_ge_one]
  have h_1_2T_pos : 0 ≤ 1 / (2 * T) := by positivity
  have h_qp_le : |qPrime T| ≤ 1 := by
    rw [abs_le]
    obtain ⟨h_lo, h_hi⟩ := abs_le.mp hqp_bd
    refine ⟨by linarith, by linarith⟩
  have h_qpp_le : |qDoublePrime T| ≤ 1 := by
    rw [abs_le]
    obtain ⟨h_lo, h_hi⟩ := abs_le.mp hqpp_bd
    have h_pos : 0 ≤ 1 / (2 * T^2) := by positivity
    have h_neg : (-1 : ℝ) / (2 * T^2) = -(1 / (2 * T^2)) := by ring
    rw [h_neg] at h_lo h_hi
    refine ⟨by linarith, by linarith⟩
  exact J_floor_quadform T h_q_ge_5 h_qp_le h_qpp_le x

end RH.JetLimitLocalBlocks
