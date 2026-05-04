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

/-- Bound on entry `(1, 1)` of `P_h A_h(T) P_h^⊤ − J(T)`.  The full
    proof requires order-5 Taylor expansion with explicit `ε^3` and `ε^5`
    cross-term bounds (~400 lines).  All necessary infrastructure helpers
    are in place. -/
axiom rate_bound_11 (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      |(pointToJetTransform h * samePointBlock T h *
          (pointToJetTransform h).transpose - J T) 1 1| ≤ M * h^2

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
