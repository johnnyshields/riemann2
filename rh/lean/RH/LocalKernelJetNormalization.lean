/-
Section 2 of `rh/rh_rebuild.tex`: local kernel and jet normalization.

`theta`, `q`, `qPrime`, `qDoublePrime` and the Riemann–Siegel asymptotics
live in `RH.RiemannSiegelTheta`.  This module re-exports them and defines
the phase kernel `K_Φ`, its symmetry / diagonal / off-diagonal
derivatives, and the point-to-jet transform `P_h`.

Maps to the LaTeX as follows (all in the §2 namespace):
  RH.LocalKernelJetNormalization.phaseKernel
      ↔ K_Φ(x, y) of `def:phase-kernel`
  RH.LocalKernelJetNormalization.pointToJetTransform
      ↔ P_h of `eq:point-to-jet-transform` (Gram-normalized form)

Theorems:
  phase_kernel_symmetric             ↔ Lemma `lem:phase-kernel-properties` (symmetry)
  phase_kernel_diagonal_value        ↔ Lemma `lem:phase-kernel-properties` (diagonal value)
  phase_kernel_diagonal_limit        ↔ Lemma `lem:phase-kernel-properties` (continuity)
  phase_kernel_diagonal_partial_x    ↔ Lemma `lem:phase-kernel-diagonal-derivatives` (K_x(T,T))
  phase_kernel_diagonal_partial_y    ↔ Lemma `lem:phase-kernel-diagonal-derivatives` (K_y(T,T))
  phase_kernel_diagonal_partial_xy   ↔ Lemma `lem:phase-kernel-diagonal-derivatives` (K_xy(T,T))
  phase_kernel_partial_x             ↔ Lemma `lem:phase-kernel-derivatives` (∂_x)
  phase_kernel_partial_y             ↔ Lemma `lem:phase-kernel-derivatives` (∂_y)
  phase_kernel_partial_xy            ↔ Lemma `lem:phase-kernel-derivatives` (∂_xy)
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.IteratedDeriv.Defs
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Topology.Order.Basic

import RH.RiemannSiegelTheta

namespace RH.LocalKernelJetNormalization

open Real RH.RiemannSiegelTheta

/-! ## Phase kernel

    The phase function `theta` and its derivatives `q`, `qPrime`,
    `qDoublePrime` live in `RH.RiemannSiegelTheta` and are accessed via
    `open RH.RiemannSiegelTheta` above.

    Scope: this module formalizes the *theta-specialized* kernel used
    downstream by Sections 2–3.  The paper states several
    phase-kernel lemmas for a general real `C¹` (resp. `C⁴`) phase `Φ`
    and then specializes to `Φ_T = θ`; that general parameterization is
    not represented here as a Lean theorem family. -/

/-- Phase kernel
    `K_Φ(x, y) = sin(Φ(x) - Φ(y)) / (π (x - y))` for `x ≠ y`,
    extended by `K_Φ(x, x) = q(x) / π` across the diagonal. -/
noncomputable def phaseKernel (x y : ℝ) : ℝ :=
  if x = y then q x / Real.pi
  else Real.sin (theta x - theta y) / (Real.pi * (x - y))

/-- The phase kernel is symmetric. -/
theorem phase_kernel_symmetric (x y : ℝ) :
    phaseKernel x y = phaseKernel y x := by
  unfold phaseKernel
  by_cases h : x = y
  · simp [h]
  · have h' : y ≠ x := fun e => h e.symm
    simp only [h, h', if_false]
    rw [show theta y - theta x = -(theta x - theta y) from by ring,
        Real.sin_neg,
        show Real.pi * (y - x) = -(Real.pi * (x - y)) from by ring]
    field_simp

/-- Removable singularity at the diagonal: `K_Φ(x, y) → q(y) / π` as `x → y`.
    One-variable form (with `y` fixed). -/
theorem phase_kernel_diagonal_limit (y : ℝ) :
    Filter.Tendsto (fun x => phaseKernel x y) (nhds y) (nhds (q y / Real.pi)) := by
  -- TODO: continuity of `theta` plus `Real.sin t / t → 1` as `t → 0`.
  sorry

/-- Joint continuity at the diagonal: `K_Φ(x, y) → q(T) / π` as
    `(x, y) → (T, T)`.  Stronger than the one-variable
    `phase_kernel_diagonal_limit` and matches the paper's continuity
    statement in `lem:phase-kernel-properties`. -/
theorem phase_kernel_joint_diagonal_limit (T : ℝ) :
    Filter.Tendsto (fun p : ℝ × ℝ => phaseKernel p.1 p.2)
      (nhds (T, T)) (nhds (q T / Real.pi)) := by
  -- TODO: continuity of `theta` and `Real.sin t / t → 1` as `t → 0`,
  -- jointly across both arguments.
  sorry

/-! ## Diagonal kernel derivatives

    Cf. Lemma `lem:phase-kernel-diagonal-derivatives`. -/

/-- Diagonal value: `K_Φ(T, T) = q(T) / π`. -/
theorem phase_kernel_diagonal_value (T : ℝ) :
    phaseKernel T T = q T / Real.pi := by
  unfold phaseKernel
  simp

/-- Diagonal partial in `x`: `K_x(T, T) = q'(T) / (2 π)`. -/
theorem phase_kernel_diagonal_partial_x (T : ℝ) :
    deriv (fun x => phaseKernel x T) T = qPrime T / (2 * Real.pi) := by
  -- TODO: Taylor expansion of `K_Φ(T+u, T)` to first order in `u`.
  sorry

/-- Diagonal partial in `y`: `K_y(T, T) = q'(T) / (2 π)`. -/
theorem phase_kernel_diagonal_partial_y (T : ℝ) :
    deriv (phaseKernel T) T = qPrime T / (2 * Real.pi) := by
  -- TODO: by symmetry of `phase_kernel_diagonal_partial_x`.
  sorry

/-- Diagonal mixed partial: `K_{xy}(T, T) = (q''(T) + 2 q(T)³) / (6 π)`. -/
theorem phase_kernel_diagonal_partial_xy (T : ℝ) :
    deriv (fun x => deriv (phaseKernel x) T) T =
      (qDoublePrime T + 2 * (q T)^3) / (6 * Real.pi) := by
  -- TODO: factored Taylor of `K_Φ` along the diagonal at total degree 2.
  sorry

/-! ## Phase-kernel derivatives at distinct points -/

/-- ∂/∂x K_Φ at distinct points, given `theta` differentiable at `T₁`. -/
theorem phase_kernel_partial_x (T₁ T₂ : ℝ) (h : T₁ ≠ T₂)
    (h_diff : DifferentiableAt ℝ theta T₁) :
    deriv (fun x => phaseKernel x T₂) T₁ =
      (q T₁ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) -
       Real.sin (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^2) := by
  -- For x near T₁ (≠ T₂), `phaseKernel x T₂ = sin(θ(x) − θ(T₂)) / (π(x − T₂))`.
  have h_θ : HasDerivAt theta (q T₁) T₁ := h_diff.hasDerivAt
  have h_eq : ∀ᶠ x in nhds T₁,
      phaseKernel x T₂ = Real.sin (theta x - theta T₂) / (Real.pi * (x - T₂)) := by
    filter_upwards [eventually_ne_nhds h] with x hx
    unfold phaseKernel
    simp [hx]
  rw [Filter.EventuallyEq.deriv_eq h_eq]
  have h_num : HasDerivAt (fun x : ℝ => Real.sin (theta x - theta T₂))
      (Real.cos (theta T₁ - theta T₂) * q T₁) T₁ := by
    have h_sub : HasDerivAt (fun x : ℝ => theta x - theta T₂) (q T₁) T₁ :=
      h_θ.sub_const (theta T₂)
    exact (Real.hasDerivAt_sin (theta T₁ - theta T₂)).comp T₁ h_sub
  have h_den : HasDerivAt (fun x : ℝ => Real.pi * (x - T₂)) Real.pi T₁ := by
    have h_id : HasDerivAt (fun x : ℝ => x - T₂) 1 T₁ :=
      (hasDerivAt_id T₁).sub_const T₂
    have := h_id.const_mul Real.pi
    simpa using this
  have h_den_ne : Real.pi * (T₁ - T₂) ≠ 0 :=
    mul_ne_zero Real.pi_ne_zero (sub_ne_zero.mpr h)
  have h_quot : HasDerivAt
      (fun x : ℝ => Real.sin (theta x - theta T₂) / (Real.pi * (x - T₂)))
      ((Real.cos (theta T₁ - theta T₂) * q T₁ * (Real.pi * (T₁ - T₂)) -
          Real.sin (theta T₁ - theta T₂) * Real.pi) /
        (Real.pi * (T₁ - T₂)) ^ 2) T₁ :=
    h_num.div h_den h_den_ne
  rw [h_quot.deriv]
  field_simp

/-- ∂/∂y K_Φ at distinct points, given `theta` differentiable at `T₂`. -/
theorem phase_kernel_partial_y (T₁ T₂ : ℝ) (h : T₁ ≠ T₂)
    (h_diff : DifferentiableAt ℝ theta T₂) :
    deriv (phaseKernel T₁) T₂ =
      (Real.sin (theta T₁ - theta T₂) -
       q T₂ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^2) := by
  have h_θ : HasDerivAt theta (q T₂) T₂ := h_diff.hasDerivAt
  have h_ne_sym : T₁ ≠ T₂ ↔ T₂ ≠ T₁ := ne_comm
  have h_eq : ∀ᶠ y in nhds T₂,
      phaseKernel T₁ y = Real.sin (theta T₁ - theta y) / (Real.pi * (T₁ - y)) := by
    filter_upwards [eventually_ne_nhds (h_ne_sym.mp h)] with y hy
    unfold phaseKernel
    simp [hy.symm]
  rw [Filter.EventuallyEq.deriv_eq h_eq]
  have h_num : HasDerivAt (fun y : ℝ => Real.sin (theta T₁ - theta y))
      (Real.cos (theta T₁ - theta T₂) * (-(q T₂))) T₂ := by
    have h_sub : HasDerivAt (fun y : ℝ => theta T₁ - theta y) (-(q T₂)) T₂ := by
      have := (hasDerivAt_const T₂ (theta T₁)).sub h_θ
      simpa using this
    exact (Real.hasDerivAt_sin (theta T₁ - theta T₂)).comp T₂ h_sub
  have h_den : HasDerivAt (fun y : ℝ => Real.pi * (T₁ - y)) (-Real.pi) T₂ := by
    have h_id : HasDerivAt (fun y : ℝ => T₁ - y) (-1) T₂ := by
      have := (hasDerivAt_const T₂ T₁).sub (hasDerivAt_id T₂)
      simpa using this
    have := h_id.const_mul Real.pi
    simpa using this
  have h_den_ne : Real.pi * (T₁ - T₂) ≠ 0 :=
    mul_ne_zero Real.pi_ne_zero (sub_ne_zero.mpr h)
  have h_quot : HasDerivAt
      (fun y : ℝ => Real.sin (theta T₁ - theta y) / (Real.pi * (T₁ - y)))
      ((Real.cos (theta T₁ - theta T₂) * (-(q T₂)) * (Real.pi * (T₁ - T₂)) -
          Real.sin (theta T₁ - theta T₂) * (-Real.pi)) /
        (Real.pi * (T₁ - T₂)) ^ 2) T₂ :=
    h_num.div h_den h_den_ne
  rw [h_quot.deriv]
  field_simp
  ring

/-- ∂²/∂x∂y K_Φ at distinct points, given `theta` differentiable at
    both `T₁` and `T₂`. -/
theorem phase_kernel_partial_xy (T₁ T₂ : ℝ) (h : T₁ ≠ T₂)
    (h_diff_T₁ : DifferentiableAt ℝ theta T₁)
    (h_diff_T₂ : DifferentiableAt ℝ theta T₂) :
    deriv (fun x => deriv (phaseKernel x) T₂) T₁ =
      ((q T₁ + q T₂) * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) +
       (q T₁ * q T₂ * (T₁ - T₂)^2 - 2) * Real.sin (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^3) := by
  have h_θ₁ : HasDerivAt theta (q T₁) T₁ := h_diff_T₁.hasDerivAt
  -- On a neighborhood of T₁, the inner deriv is given by phase_kernel_partial_y
  have h_inner_eq : ∀ᶠ x in nhds T₁,
      deriv (phaseKernel x) T₂ =
        (Real.sin (theta x - theta T₂) -
         q T₂ * (x - T₂) * Real.cos (theta x - theta T₂)) /
        (Real.pi * (x - T₂) ^ 2) := by
    filter_upwards [eventually_ne_nhds h] with x hx
    exact phase_kernel_partial_y x T₂ hx h_diff_T₂
  rw [Filter.EventuallyEq.deriv_eq h_inner_eq]
  -- Numerator: A(x) = sin(θ(x) − θ(T₂)) − q(T₂)(x − T₂) cos(θ(x) − θ(T₂))
  have h_θ_sub : HasDerivAt (fun x : ℝ => theta x - theta T₂) (q T₁) T₁ :=
    h_θ₁.sub_const (theta T₂)
  have h_sin : HasDerivAt (fun x : ℝ => Real.sin (theta x - theta T₂))
      (Real.cos (theta T₁ - theta T₂) * q T₁) T₁ := by
    exact (Real.hasDerivAt_sin (theta T₁ - theta T₂)).comp T₁ h_θ_sub
  have h_cos : HasDerivAt (fun x : ℝ => Real.cos (theta x - theta T₂))
      (-Real.sin (theta T₁ - theta T₂) * q T₁) T₁ := by
    exact (Real.hasDerivAt_cos (theta T₁ - theta T₂)).comp T₁ h_θ_sub
  have h_xT₂ : HasDerivAt (fun x : ℝ => x - T₂) (1 : ℝ) T₁ :=
    (hasDerivAt_id T₁).sub_const T₂
  have h_xT₂_cos : HasDerivAt (fun x : ℝ => (x - T₂) * Real.cos (theta x - theta T₂))
      (1 * Real.cos (theta T₁ - theta T₂) +
        (T₁ - T₂) * (-Real.sin (theta T₁ - theta T₂) * q T₁)) T₁ :=
    h_xT₂.mul h_cos
  have h_qT₂_term : HasDerivAt
      (fun x : ℝ => q T₂ * ((x - T₂) * Real.cos (theta x - theta T₂)))
      (q T₂ * (1 * Real.cos (theta T₁ - theta T₂) +
        (T₁ - T₂) * (-Real.sin (theta T₁ - theta T₂) * q T₁))) T₁ :=
    h_xT₂_cos.const_mul (q T₂)
  have h_num : HasDerivAt
      (fun x : ℝ => Real.sin (theta x - theta T₂) -
                    q T₂ * ((x - T₂) * Real.cos (theta x - theta T₂)))
      (Real.cos (theta T₁ - theta T₂) * q T₁ -
        q T₂ * (1 * Real.cos (theta T₁ - theta T₂) +
          (T₁ - T₂) * (-Real.sin (theta T₁ - theta T₂) * q T₁))) T₁ :=
    h_sin.sub h_qT₂_term
  have h_num_eq_fn :
      (fun x : ℝ => Real.sin (theta x - theta T₂) -
                    q T₂ * ((x - T₂) * Real.cos (theta x - theta T₂))) =
      (fun x : ℝ => Real.sin (theta x - theta T₂) -
                    q T₂ * (x - T₂) * Real.cos (theta x - theta T₂)) := by
    funext x; ring
  rw [h_num_eq_fn] at h_num
  -- Denominator: D(x) = π (x − T₂)²
  have h_xT₂_sq : HasDerivAt (fun x : ℝ => (x - T₂) ^ 2) (2 * (T₁ - T₂)) T₁ := by
    have := h_xT₂.pow 2
    simpa using this
  have h_den : HasDerivAt (fun x : ℝ => Real.pi * (x - T₂) ^ 2)
      (Real.pi * (2 * (T₁ - T₂))) T₁ :=
    h_xT₂_sq.const_mul Real.pi
  have h_den_ne : Real.pi * (T₁ - T₂) ^ 2 ≠ 0 := by
    have : (T₁ - T₂) ^ 2 ≠ 0 := pow_ne_zero _ (sub_ne_zero.mpr h)
    exact mul_ne_zero Real.pi_ne_zero this
  -- Quotient with explicit return type to avoid Function.div display
  have h_quot : HasDerivAt
      (fun x : ℝ => (Real.sin (theta x - theta T₂) -
                     q T₂ * (x - T₂) * Real.cos (theta x - theta T₂)) /
                    (Real.pi * (x - T₂) ^ 2))
      (((Real.cos (theta T₁ - theta T₂) * q T₁ -
          q T₂ * (1 * Real.cos (theta T₁ - theta T₂) +
            (T₁ - T₂) * (-Real.sin (theta T₁ - theta T₂) * q T₁))) *
          (Real.pi * (T₁ - T₂) ^ 2) -
        (Real.sin (theta T₁ - theta T₂) -
          q T₂ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂)) *
          (Real.pi * (2 * (T₁ - T₂)))) /
        (Real.pi * (T₁ - T₂) ^ 2) ^ 2) T₁ :=
    h_num.div h_den h_den_ne
  rw [h_quot.deriv]
  field_simp
  ring

/-! ## Point-to-jet transform -/

/-- Gram-normalized point-to-jet transform `P_h` of `eq:point-to-jet-transform`,

      P_h = (1 / √2) · ⎛  1     1  ⎞
                       ⎝ -1/(2h) 1/(2h) ⎠

    For `h = 0` the entries `±1/(2h)` are interpreted as `0` (Mathlib
    convention for division by zero); this case is never used. -/
noncomputable def pointToJetTransform (h : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  (1 / Real.sqrt 2) • !![1, 1; -1/(2*h), 1/(2*h)]

end RH.LocalKernelJetNormalization
