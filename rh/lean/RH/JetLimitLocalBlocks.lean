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

namespace RH.JetLimitLocalBlocks

open Real Matrix RH.LocalKernelJetNormalization

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

/-- Same-point Gram positivity: at sufficiently large `T`, `J(T) ≻ 0`,
    with eigenvalue lower bound `λ_min(J(T)) ≥ (2 q(T) / π) (1 + o(1))`.

    Combines `algebraic_gram_criterion` with the Riemann–Siegel
    asymptotics from §2 (`phase_derivative_lower_bound`,
    `theta_derivative_asymptotics`). -/
theorem same_point_gram_positivity :
    ∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T → (J T).PosDef := by
  sorry

end RH.JetLimitLocalBlocks
