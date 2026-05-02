/-
Section 3 of `rh/rh_rebuild.tex`: jet-limit local blocks.

Spec-level Lean module.  Builds on §2.  Proofs are deferred via `sorry`.

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

/-! ## Jet-limit theorems -/

/-- Same-point jet-limit:
    `P_h * A_h(T) * P_h^⊤ → J(T)` as `h → 0⁺`.
    Cf. Lemma `lem:same-point-jet-limit`. -/
theorem same_point_jet_limit (T : ℝ) :
    Filter.Tendsto
      (fun h => let P := pointToJetTransform h
                P * samePointBlock T h * P.transpose)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds (J T)) := by
  sorry

/-- Cross-block jet-limit:
    `P_h * C_h(T₁, T₂) * P_h^⊤ → (1/π) · N₁₂(T₁, T₂)` as `h → 0⁺`,
    for `T₁ ≠ T₂`.
    Cf. Lemma `lem:cross-block-jet-limit`. -/
theorem cross_block_jet_limit (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    Filter.Tendsto
      (fun h => let P := pointToJetTransform h
                P * crossBlock T₁ T₂ h * P.transpose)
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds ((1 / Real.pi) • N12 T₁ T₂)) := by
  sorry

/-! ## O(h²) rate statements

    The paper proves `P_h A_h(T) P_h^⊤ = J(T) + O(h²)` and the
    corresponding cross-block bound entrywise.  The `Tendsto` versions
    above lose this rate; the explicit `O(h²)` form is required by
    downstream finite-scale comparisons. -/

/-- Same-point jet-limit with explicit `O(h²)` rate.  Entrywise:
    there is `M ≥ 0` such that for `h ∈ (0, 1]` and each entry `(i, j)`
    of `Fin 2 × Fin 2`,
        `|((P_h A_h(T) P_h^⊤) − J(T)) i j| ≤ M h²`. -/
theorem same_point_jet_limit_rate (T : ℝ) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ 1 →
      ∀ i j : Fin 2,
        |(pointToJetTransform h * samePointBlock T h *
            (pointToJetTransform h).transpose - J T) i j| ≤ M * h^2 := by
  -- TODO: 5th-order Taylor of θ around T, applied to the four-sample
  -- conjugation; the explicit constant M depends on a local C^5 bound
  -- for θ near T.
  sorry

/-- Cross-block jet-limit with explicit `O(h²)` rate.  Entrywise: for
    fixed separation `s = T₁ − T₂ ≠ 0`, there is `M(|s|⁻¹) ≥ 0` such
    that for `h ∈ (0, |s|/3]`,
        `|((P_h C_h(T₁,T₂) P_h^⊤) − (1/π) N₁₂(T₁,T₂)) i j| ≤ M h²`. -/
theorem cross_block_jet_limit_rate (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ h : ℝ, 0 < h → h ≤ |T₁ - T₂| / 3 →
      ∀ i j : Fin 2,
        |(pointToJetTransform h * crossBlock T₁ T₂ h *
            (pointToJetTransform h).transpose -
          (1 / Real.pi) • N12 T₁ T₂) i j| ≤ M * h^2 := by
  -- TODO: 5th-order Taylor with parity weights `(1, σ₂, σ₁, σ₁σ₂)`
  -- across the four samples; constant depends on `|s|⁻¹` and a local
  -- C^5 bound for θ near `T₁` and `T₂`.
  sorry

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
  obtain ⟨T₁, C₁, hT₁_pos, hC₁_nn, hq_lb⟩ := phase_derivative_lower_bound
  obtain ⟨T₂, C₂, hT₂_pos, hC₂_nn, hasymp⟩ := theta_derivative_asymptotics
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
    have h_qbd := hq_lb T hT_T₁ T (by linarith) (by linarith)
    linarith
  -- (2) |qPrime T| ≤ 1 and |qDoublePrime T| ≤ 1
  obtain ⟨_, hqp_bd, hqpp_bd⟩ := hasymp T hT_T₂ T (by linarith) (by linarith)
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

/-- Uniform spectral floor for `J(T)`: at sufficiently large `T`,
    `xᵀ J(T) x ≥ xᵀ x` for every `x : Fin 2 → ℝ`.

    Equivalent to `λ_min(J(T)) ≥ 1` for real symmetric 2×2.  Matches
    the paper's whitening-relevant floor in
    Lemma `lem:same-point-gram-positivity` after raising the
    lower-height cutoff. -/
theorem same_point_gram_uniform_floor :
    ∃ T₀ : ℝ, 0 < T₀ ∧
      ∀ T : ℝ, T₀ ≤ T →
      ∀ x : Fin 2 → ℝ,
        x ⬝ᵥ ((J T) *ᵥ x) ≥ x ⬝ᵥ x := by
  -- TODO: strengthen `analytic_bounds_eventual` to a regime where
  --   `λ_min(J(T)) = (2 q(T) / π) (1 + o(1)) ≥ 1`,
  -- and translate via the SOS identity used in `algebraic_gram_criterion`.
  sorry

end RH.JetLimitLocalBlocks
