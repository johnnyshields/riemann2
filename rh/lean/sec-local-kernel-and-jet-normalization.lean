/-
Section 2 of `rh/rh_rebuild.tex`: local kernel and jet normalization.

Spec-level Lean module.  Definitions are concrete; lemma proofs are
deferred via `sorry` to be filled in against Mathlib's analysis API.

Maps to the LaTeX as follows:
  RH.LocalKernelJetNormalization.theta
      ↔ Riemann–Siegel θ(t) (Remark `rem:phase-chart-identification`)
  RH.LocalKernelJetNormalization.q, qPrime, qDoublePrime
      ↔ q = θ', q' = θ'', q'' = θ'''
  RH.LocalKernelJetNormalization.phaseKernel
      ↔ K_Φ(x, y) of `def:phase-kernel`
  RH.LocalKernelJetNormalization.pointToJetTransform
      ↔ P_h of `eq:point-to-jet-transform` (Gram-normalized form)

Theorems:
  phase_derivative_lower_bound       ↔ Lemma `lem:phase-derivative-lower-bound`
  q_prime_asymptotic                 ↔ Lemma `lem:phase-derivative-upper-bounds` (q')
  q_double_prime_asymptotic          ↔ Lemma `lem:phase-derivative-upper-bounds` (q'')
  phase_kernel_symmetric             ↔ Lemma `lem:phase-kernel-properties` (i)
  phase_kernel_diagonal_limit        ↔ Lemma `lem:phase-kernel-properties` (iii)
  phase_kernel_partial_x             ↔ Lemma `lem:phase-kernel-derivatives` (∂_x)
  phase_kernel_partial_y             ↔ Lemma `lem:phase-kernel-derivatives` (∂_y)
  phase_kernel_partial_xy            ↔ Lemma `lem:phase-kernel-derivatives` (∂_xy)
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.IteratedDeriv.Defs
import Mathlib.Data.Matrix.Notation
import Mathlib.Topology.Order.Basic

namespace RH.LocalKernelJetNormalization

open Real

/-! ## Phase function and its derivatives -/

/-- The Riemann–Siegel theta function on real arguments,
    `θ(t) = arg Γ(1/4 + it/2) - (t/2) log π`.

    Treated as a primitive at this stage; can be unfolded to its
    `Complex.Gamma` definition once that connection is proved. -/
noncomputable def theta : ℝ → ℝ := sorry

/-- First derivative of the phase, `q := θ'`. -/
noncomputable def q (t : ℝ) : ℝ := deriv theta t

/-- Second derivative of the phase, `q' := θ''`. -/
noncomputable def qPrime (t : ℝ) : ℝ := deriv (deriv theta) t

/-- Third derivative of the phase, `q'' := θ'''`. -/
noncomputable def qDoublePrime (t : ℝ) : ℝ := deriv (deriv (deriv theta)) t

/-! ## Riemann–Siegel asymptotics -/

/-- Phase-derivative lower bound (P2):
    on retained packets at sufficiently large `T`,
    `q(t) ≥ (1/2) log(T/(4π)) - C/T²`.

    Proof outline: termwise differentiation of the Riemann–Siegel
    asymptotic `θ(t) = (t/2) log(t/(2π)) - t/2 - π/8 + 1/(48t) + O(t⁻³)`
    gives `q(t) = (1/2) log(t/(2π)) - 1/(48 t²) + O(t⁻⁴)`, then bound
    `t ≥ T/2` on the window. -/
theorem phase_derivative_lower_bound :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T → ∀ t : ℝ, T - 1 ≤ t → t ≤ T + 1 →
    q t ≥ (1/2) * Real.log (T / (4 * Real.pi)) - C / T^2 := by
  sorry

/-- Asymptotic for `q'(T) = θ''(T) = 1/(2T) + O(T⁻³)`. -/
theorem q_prime_asymptotic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T →
    |qPrime T - 1 / (2 * T)| ≤ C / T^3 := by
  sorry

/-- Asymptotic for `q''(T) = θ'''(T) = -1/(2T²) + O(T⁻⁴)`. -/
theorem q_double_prime_asymptotic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T →
    |qDoublePrime T - (-1) / (2 * T^2)| ≤ C / T^4 := by
  sorry

/-! ## Phase kernel -/

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

/-- Removable singularity at the diagonal: `K_Φ(x, y) → q(y) / π` as `x → y`. -/
theorem phase_kernel_diagonal_limit (y : ℝ) :
    Filter.Tendsto (fun x => phaseKernel x y) (nhds y) (nhds (q y / Real.pi)) := by
  sorry

/-! ## Phase-kernel derivatives at distinct points -/

/-- ∂/∂x K_Φ at distinct points. -/
theorem phase_kernel_partial_x (T₁ T₂ : ℝ) (h : T₁ ≠ T₂) :
    deriv (fun x => phaseKernel x T₂) T₁ =
      (q T₁ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) -
       Real.sin (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^2) := by
  sorry

/-- ∂/∂y K_Φ at distinct points. -/
theorem phase_kernel_partial_y (T₁ T₂ : ℝ) (h : T₁ ≠ T₂) :
    deriv (phaseKernel T₁) T₂ =
      (Real.sin (theta T₁ - theta T₂) -
       q T₂ * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^2) := by
  sorry

/-- ∂²/∂x∂y K_Φ at distinct points. -/
theorem phase_kernel_partial_xy (T₁ T₂ : ℝ) (h : T₁ ≠ T₂) :
    deriv (fun x => deriv (phaseKernel x) T₂) T₁ =
      ((q T₁ + q T₂) * (T₁ - T₂) * Real.cos (theta T₁ - theta T₂) +
       (q T₁ * q T₂ * (T₁ - T₂)^2 - 2) * Real.sin (theta T₁ - theta T₂))
      / (Real.pi * (T₁ - T₂)^3) := by
  sorry

/-! ## Point-to-jet transform -/

/-- Gram-normalized point-to-jet transform `P_h` of `eq:point-to-jet-transform`,

      P_h = (1 / √2) · ⎛  1     1  ⎞
                       ⎝ -1/(2h) 1/(2h) ⎠

    For `h = 0` the entries `±1/(2h)` are interpreted as `0` (Mathlib
    convention for division by zero); this case is never used. -/
noncomputable def pointToJetTransform (h : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  (1 / Real.sqrt 2) • !![1, 1; -1/(2*h), 1/(2*h)]

end RH.LocalKernelJetNormalization
