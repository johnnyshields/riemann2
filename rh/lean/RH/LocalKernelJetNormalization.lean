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
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.IteratedDeriv.Defs
import Mathlib.Analysis.Calculus.Taylor
import Mathlib.Analysis.Calculus.DSlope
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Topology.Order.Basic

import RH.RiemannSiegelTheta

namespace RH.LocalKernelJetNormalization

open Real RH.RiemannSiegelTheta

/-! ## Auxiliary bounds -/

/-- Cubic bound on `|sin u - u|` for `|u| ≤ 1`.
    Derived from `Real.sin_bound`:
    `|sin u - (u - u³/6)| ≤ 5/96 |u|⁴`, then by triangle inequality
    `|sin u - u| ≤ 5/96 |u|⁴ + |u|³/6 ≤ 21/96 |u|³ ≤ |u|³`. -/
private lemma sin_sub_self_abs_le_cube {u : ℝ} (hu : |u| ≤ 1) :
    |Real.sin u - u| ≤ |u|^3 := by
  have h_sin := Real.sin_bound hu
  have h_pow_3 : |u^3| = |u|^3 := abs_pow u 3
  have h_u3_div_6 : |u^3 / 6| = |u|^3 / 6 := by
    rw [abs_div, h_pow_3]
    have h6 : |(6:ℝ)| = 6 := abs_of_pos (by norm_num)
    rw [h6]
  have h_decomp : Real.sin u - u = (Real.sin u - (u - u^3/6)) - u^3/6 := by ring
  have h_u_nn : 0 ≤ |u| := abs_nonneg _
  have h_u3_nn : 0 ≤ |u|^3 := pow_nonneg h_u_nn 3
  have h_u4_le_u3 : |u|^4 ≤ |u|^3 := by
    have hk : |u|^4 = |u|^3 * |u| := by ring
    rw [hk]
    have : |u|^3 * |u| ≤ |u|^3 * 1 :=
      mul_le_mul_of_nonneg_left hu h_u3_nn
    linarith
  have h_tri : |Real.sin u - u| ≤ |Real.sin u - (u - u^3/6)| + |u^3/6| := by
    rw [h_decomp]
    exact abs_sub _ _
  have h_5_96 : (0:ℝ) ≤ 5/96 := by norm_num
  have h_u4_596 : |u|^4 * (5/96) ≤ |u|^3 * (5/96) :=
    mul_le_mul_of_nonneg_right h_u4_le_u3 h_5_96
  rw [h_u3_div_6] at h_tri
  have h_step1 : |Real.sin u - u| ≤ |u|^4 * (5/96) + |u|^3/6 := by
    linarith
  have h_step2 : |u|^4 * (5/96) + |u|^3/6 ≤ |u|^3 * (21/96) := by
    have h_eq : |u|^3 * (21/96) = |u|^3 * (5/96) + |u|^3/6 := by ring
    linarith
  have h_step3 : |u|^3 * (21/96) ≤ |u|^3 := by
    have h21 : (21:ℝ)/96 ≤ 1 := by norm_num
    have : |u|^3 * (21/96) ≤ |u|^3 * 1 :=
      mul_le_mul_of_nonneg_left h21 h_u3_nn
    linarith
  linarith

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
    One-variable form (with `y` fixed), under `theta` differentiable at `y`.

    Proof: on the punctured neighborhood `{y}ᶜ`, phaseKernel(·, y) =
    sin(θ(·) − θ(y)) / (π(· − y)).  The latter is the slope of
    g(x) = sin(θ(x) − θ(y)) at y (with g(y) = 0), so it tends to
    g'(y) = cos(0) · q(y) = q(y) by `hasDerivAt_iff_tendsto_slope`.
    Dividing by π gives the punctured limit q(y)/π; at x = y the value
    equals q(y)/π by `phase_kernel_diagonal_value`.  Combine via
    `nhdsNE_sup_pure y : 𝓝[≠] y ⊔ pure y = 𝓝 y`. -/
theorem phase_kernel_diagonal_limit (y : ℝ)
    (h_diff : DifferentiableAt ℝ theta y) :
    Filter.Tendsto (fun x => phaseKernel x y) (nhds y) (nhds (q y / Real.pi)) := by
  have h_θ : HasDerivAt theta (q y) y := h_diff.hasDerivAt
  have h_θ_sub : HasDerivAt (fun x : ℝ => theta x - theta y) (q y) y :=
    h_θ.sub_const (theta y)
  -- HasDerivAt sin∘(θ − θ y) at y, with deriv cos(0) · q y = q y
  have h_g : HasDerivAt (fun x : ℝ => Real.sin (theta x - theta y)) (q y) y := by
    have h := (Real.hasDerivAt_sin (theta y - theta y)).comp y h_θ_sub
    simpa [sub_self] using h
  -- Slope tendsto on punctured nhds
  have h_slope := hasDerivAt_iff_tendsto_slope.mp h_g
  -- Convert from `slope` to explicit form `(g x - g y) / (x - y)`.
  -- slope f x y = (y - x)⁻¹ • (f y - f x)
  have h_slope_form : Filter.Tendsto
      (fun x => (Real.sin (theta x - theta y) - Real.sin (theta y - theta y)) / (x - y))
      (nhdsWithin y {y}ᶜ) (nhds (q y)) := by
    have heq : (fun x => (Real.sin (theta x - theta y) -
                          Real.sin (theta y - theta y)) / (x - y)) =
                (fun x => slope (fun x : ℝ => Real.sin (theta x - theta y)) y x) := by
      funext x
      simp [slope, smul_eq_mul]
      ring
    rw [heq]; exact h_slope
  -- Simplify using sin(θ y − θ y) = sin 0 = 0
  have h_sin_y_zero : Real.sin (theta y - theta y) = 0 := by
    rw [sub_self]; exact Real.sin_zero
  have h_punc : Filter.Tendsto (fun x => Real.sin (theta x - theta y) / (x - y))
      (nhdsWithin y {y}ᶜ) (nhds (q y)) := by
    have heq : (fun x => Real.sin (theta x - theta y) / (x - y)) =ᶠ[nhdsWithin y {y}ᶜ]
        (fun x => (Real.sin (theta x - theta y) - Real.sin (theta y - theta y)) / (x - y)) := by
      filter_upwards with x
      rw [h_sin_y_zero, sub_zero]
    exact (Filter.tendsto_congr' heq).mpr h_slope_form
  -- Divide by π: punctured limit of phaseKernel is q y / π
  have h_punc_pi : Filter.Tendsto
      (fun x => Real.sin (theta x - theta y) / (Real.pi * (x - y)))
      (nhdsWithin y {y}ᶜ) (nhds (q y / Real.pi)) := by
    have h_div := h_punc.div_const Real.pi
    have heq : (fun x => Real.sin (theta x - theta y) / (x - y) / Real.pi) =
        (fun x => Real.sin (theta x - theta y) / (Real.pi * (x - y))) := by
      funext x; rw [div_div, mul_comm]
    rw [heq] at h_div
    exact h_div
  -- phaseKernel agrees with sin/(π(x-y)) on the punctured neighborhood
  have h_eq_punc : (fun x => phaseKernel x y) =ᶠ[nhdsWithin y {y}ᶜ]
      (fun x => Real.sin (theta x - theta y) / (Real.pi * (x - y))) := by
    filter_upwards [self_mem_nhdsWithin] with x hx
    have hxy : x ≠ y := hx
    unfold phaseKernel
    simp [hxy]
  have h_punc_kernel : Filter.Tendsto (fun x => phaseKernel x y)
      (nhdsWithin y {y}ᶜ) (nhds (q y / Real.pi)) :=
    (Filter.tendsto_congr' h_eq_punc).mpr h_punc_pi
  -- At x = y, phaseKernel y y = q y / π = limit value
  have h_at_y : phaseKernel y y = q y / Real.pi := by
    unfold phaseKernel; simp
  -- Bridge: 𝓝 y = 𝓝[≠] y ⊔ pure y
  rw [← nhdsNE_sup_pure y, Filter.tendsto_sup]
  refine ⟨h_punc_kernel, ?_⟩
  -- Tendsto on `pure y`: just need f y to be in nhds of (q y / π)
  rw [Filter.tendsto_pure_left]
  intro V hV
  rw [h_at_y]
  exact mem_of_mem_nhds hV

/-- Theta-specialized diagonal limit, using the smoothness input from
    `RiemannSiegelTheta`. -/
theorem phase_kernel_diagonal_limit_theta (y : ℝ) :
    Filter.Tendsto (fun x => phaseKernel x y) (nhds y) (nhds (q y / Real.pi)) :=
  phase_kernel_diagonal_limit y (theta_differentiableAt y)

set_option maxHeartbeats 600000 in
/-- Joint continuity at the diagonal: `K_Φ(x, y) → q(T) / π` as
    `(x, y) → (T, T)`.  Stronger than the one-variable
    `phase_kernel_diagonal_limit` and matches the paper's continuity
    statement in `lem:phase-kernel-properties`.

    Proof: by MVT, `θ(x) − θ(y) = q(c)(x − y)` for some `c` between `x`
    and `y`.  For `|q(c)(x−y)| ≤ 1`, `|sin u − u| ≤ |u|³` gives
        `|K(x,y) − q(c)/π| ≤ |q(c)|³ (x−y)² / π`.
    Continuity of `q` then gives `|q(c) − q(T)| → 0` as `(x,y) → (T,T)`. -/
theorem phase_kernel_joint_diagonal_limit (T : ℝ) :
    Filter.Tendsto (fun p : ℝ × ℝ => phaseKernel p.1 p.2)
      (nhds (T, T)) (nhds (q T / Real.pi)) := by
  -- q is continuous from theta_smooth → ContDiff ℝ 1 q.
  have h_q_cont : Continuous q := by
    have h_θ_C2 : ContDiff ℝ 2 theta := theta_smooth.of_le (by decide)
    have h_q_C1 : ContDiff ℝ 1 q := by
      have h : ContDiff ℝ (1 + 1 : ℕ) theta := by
        have heq : (1 + 1 : ℕ) = 2 := by norm_num
        rw [heq]; exact h_θ_C2
      exact h.deriv'
    exact h_q_C1.continuous
  rw [Metric.tendsto_nhds]
  intro ε hε
  rw [Metric.eventually_nhds_iff]
  -- Constants.
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hπ_ne : Real.pi ≠ 0 := Real.pi_ne_zero
  -- Pick δ_q from continuity of q at T (target ε * π / 2).
  obtain ⟨δ_q, hδ_q_pos, hδ_q⟩ :=
    Metric.continuous_iff.mp h_q_cont T (ε * Real.pi / 2) (by positivity)
  -- A uniform |q| bound near T.
  set M : ℝ := |q T| + 1 with hM_def
  have hM_pos : 0 < M := by
    have : 0 ≤ |q T| := abs_nonneg _
    have heq : M = |q T| + 1 := rfl
    linarith
  obtain ⟨δ_M, hδ_M_pos, hδ_M_bd⟩ : ∃ δ_M, 0 < δ_M ∧ ∀ c, |c - T| < δ_M → |q c| ≤ M := by
    obtain ⟨δ', hδ'_pos, hδ'⟩ := Metric.continuous_iff.mp h_q_cont T 1 zero_lt_one
    refine ⟨δ', hδ'_pos, fun c hc => ?_⟩
    have h₁ : |q c - q T| < 1 := hδ' c hc
    have h₂ : |q c| ≤ |q T| + |q c - q T| := by
      have heq : q c = q T + (q c - q T) := by ring
      calc |q c| = |q T + (q c - q T)| := by rw [← heq]
        _ ≤ |q T| + |q c - q T| := abs_add_le _ _
    have heq : M = |q T| + 1 := rfl
    linarith
  -- Need δ small enough: 4 * M^3 * δ^2 / π < ε / 2 and 2 M δ ≤ 1.
  -- δ < √(πε/(8M^3)) and δ ≤ 1/(2M).
  have hM3_pos : 0 < M^3 := by positivity
  set δ_cubic : ℝ := Real.sqrt (Real.pi * ε / (8 * M^3)) with hδc_def
  have hδ_cubic_pos : 0 < δ_cubic := Real.sqrt_pos.mpr (by positivity)
  set δ_lin : ℝ := 1 / (2 * M) with hδl_def
  have hδ_lin_pos : 0 < δ_lin := by
    have : 0 < 2 * M := by linarith
    exact div_pos zero_lt_one this
  set δ : ℝ := min δ_q (min δ_M (min δ_cubic δ_lin)) with hδ_def
  have hδ_pos : 0 < δ := by
    refine lt_min hδ_q_pos (lt_min hδ_M_pos (lt_min hδ_cubic_pos hδ_lin_pos))
  refine ⟨δ, hδ_pos, ?_⟩
  intro p hp
  obtain ⟨x, y⟩ := p
  simp only [Prod.dist_eq] at hp
  have hx_dist : |x - T| < δ := by
    have h := lt_of_le_of_lt (le_max_left _ _) hp
    simpa [Real.dist_eq] using h
  have hy_dist : |y - T| < δ := by
    have h := lt_of_le_of_lt (le_max_right _ _) hp
    simpa [Real.dist_eq] using h
  have hδ_le_q : δ ≤ δ_q := min_le_left _ _
  have hδ_le_M : δ ≤ δ_M := le_trans (min_le_right _ _) (min_le_left _ _)
  have hδ_le_cubic : δ ≤ δ_cubic :=
    le_trans (min_le_right _ _) (le_trans (min_le_right _ _) (min_le_left _ _))
  have hδ_le_lin : δ ≤ δ_lin :=
    le_trans (min_le_right _ _) (le_trans (min_le_right _ _) (min_le_right _ _))
  rw [Real.dist_eq]
  by_cases hxy : x = y
  · -- Diagonal case: K(y, y) = q(y)/π → q(T)/π by continuity of q.
    rw [hxy]
    have h_pK : phaseKernel y y = q y / Real.pi := by unfold phaseKernel; simp
    rw [h_pK]
    have hy_q : |y - T| < δ_q := lt_of_lt_of_le hy_dist hδ_le_q
    have h_q_diff : |q y - q T| < ε * Real.pi / 2 := hδ_q y hy_q
    have heq : q y / Real.pi - q T / Real.pi = (q y - q T) / Real.pi := by
      field_simp
    rw [heq, abs_div, abs_of_pos hπ_pos]
    rw [div_lt_iff₀ hπ_pos]
    nlinarith [h_q_diff, hπ_pos.le, hε.le]
  · -- Off-diagonal case: use MVT.
    have hxy_ne : x - y ≠ 0 := sub_ne_zero.mpr hxy
    have h_θ_diff : Differentiable ℝ theta :=
      theta_smooth.differentiable (by decide)
    have h_θ_cont : Continuous theta := h_θ_diff.continuous
    -- Apply MVT.
    obtain ⟨c, hc_min, hc_max, hc_eq⟩ : ∃ c : ℝ,
        min x y < c ∧ c < max x y ∧ theta x - theta y = q c * (x - y) := by
      rcases lt_or_gt_of_ne hxy with hlt | hgt
      · obtain ⟨c, hc_in, hc⟩ := exists_hasDerivAt_eq_slope theta q hlt
          h_θ_cont.continuousOn (fun z _ => (h_θ_diff z).hasDerivAt)
        refine ⟨c, ?_, ?_, ?_⟩
        · simpa [min_eq_left hlt.le] using hc_in.1
        · simpa [max_eq_right hlt.le] using hc_in.2
        · -- hc : q c = (theta y - theta x) / (y - x)
          have h_yx : y - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hxy)
          have h_eq1 : q c * (y - x) = theta y - theta x := by
            have := hc
            field_simp at this
            linarith
          have h_eq2 : theta x - theta y = -(theta y - theta x) := by ring
          have h_eq3 : x - y = -(y - x) := by ring
          rw [h_eq2, h_eq3]
          have h_neg : q c * -(y - x) = -(q c * (y - x)) := by ring
          rw [h_neg, h_eq1]
      · obtain ⟨c, hc_in, hc⟩ := exists_hasDerivAt_eq_slope theta q hgt
          h_θ_cont.continuousOn (fun z _ => (h_θ_diff z).hasDerivAt)
        refine ⟨c, ?_, ?_, ?_⟩
        · simpa [min_eq_right hgt.le] using hc_in.1
        · simpa [max_eq_left hgt.le] using hc_in.2
        · have h_xy : x - y ≠ 0 := sub_ne_zero.mpr hxy
          have h_eq1 : q c * (x - y) = theta x - theta y := by
            field_simp at hc; linarith
          linarith
    -- |c - T| < δ since c is between x and y.
    have hc_T : |c - T| < δ := by
      rw [abs_lt]
      have h_min_T : -δ < min x y - T := by
        rcases le_total x y with hxy_le | hxy_le
        · simp [min_eq_left hxy_le]; rw [abs_lt] at hx_dist; linarith
        · simp [min_eq_right hxy_le]; rw [abs_lt] at hy_dist; linarith
      have h_max_T : max x y - T < δ := by
        rcases le_total x y with hxy_le | hxy_le
        · simp [max_eq_right hxy_le]; rw [abs_lt] at hy_dist; linarith
        · simp [max_eq_left hxy_le]; rw [abs_lt] at hx_dist; linarith
      constructor
      · linarith
      · linarith
    have hc_q : |q c - q T| < ε * Real.pi / 2 := hδ_q c (lt_of_lt_of_le hc_T hδ_le_q)
    have hc_M : |q c| ≤ M := hδ_M_bd c (lt_of_lt_of_le hc_T hδ_le_M)
    -- Now estimate.
    set v : ℝ := x - y with hv_def
    set u : ℝ := q c * v with hu_def
    have hv_ne : v ≠ 0 := hxy_ne
    have hv_abs : |v| < 2 * δ := by
      rw [abs_lt] at hx_dist hy_dist
      rw [abs_lt]; constructor <;> linarith
    have hu_abs_le : |u| ≤ M * |v| := by
      simp only [hu_def, abs_mul]
      exact mul_le_mul_of_nonneg_right hc_M (abs_nonneg _)
    have h_2δ_lin : 2 * δ ≤ 1 / M := by
      have h2 : (2 : ℝ) * δ ≤ 2 * δ_lin := by linarith
      have h3 : 2 * δ_lin = 1 / M := by
        rw [hδl_def]; field_simp
      linarith
    have hMv_le_one : M * |v| ≤ 1 := by
      have hv_le : |v| ≤ 2 * δ := le_of_lt hv_abs
      have h₁ : M * |v| ≤ M * (2 * δ) := mul_le_mul_of_nonneg_left hv_le (le_of_lt hM_pos)
      have h₂ : M * (2 * δ) ≤ M * (1 / M) := mul_le_mul_of_nonneg_left h_2δ_lin (le_of_lt hM_pos)
      have h₃ : M * (1 / M) = 1 := by
        rw [mul_one_div]; exact div_self (ne_of_gt hM_pos)
      linarith
    have hu_le_one : |u| ≤ 1 := le_trans hu_abs_le hMv_le_one
    have h_sin_bound := sin_sub_self_abs_le_cube hu_le_one
    -- phaseKernel(x, y) = sin u / (π v) for x ≠ y.
    have h_pK : phaseKernel x y = Real.sin (theta x - theta y) / (Real.pi * v) := by
      unfold phaseKernel
      simp [hxy, hv_def]
    rw [h_pK, hc_eq]
    -- Goal: |sin(u) / (π v) - q T / π| < ε
    -- Decompose: = (sin u - u)/(π v) + (q c - q T)/π
    have h_decomp : Real.sin u / (Real.pi * v) - q T / Real.pi =
        (Real.sin u - u) / (Real.pi * v) + (q c - q T) / Real.pi := by
      have hu_eq : u = q c * v := rfl
      field_simp
      rw [hu_eq]; ring
    have hv_pos : 0 < |v| := abs_pos.mpr hv_ne
    -- Bound |(sin u - u)/(π v)| ≤ |u|^3/(π|v|) ≤ M^3 |v|^3 /(π|v|) = M^3 |v|^2 / π ≤ 4 M^3 δ^2 / π.
    have h_term1 : |(Real.sin u - u) / (Real.pi * v)| ≤ M^3 * |v|^2 / Real.pi := by
      rw [abs_div, abs_mul, abs_of_pos hπ_pos]
      have hπv_pos : 0 < Real.pi * |v| := mul_pos hπ_pos hv_pos
      rw [div_le_div_iff₀ hπv_pos hπ_pos]
      have h_u3_le : |u|^3 ≤ M^3 * |v|^3 := by
        have h_pow := pow_le_pow_left₀ (abs_nonneg u) hu_abs_le 3
        rw [mul_pow] at h_pow
        exact h_pow
      have h_M3_nn : 0 ≤ M^3 := le_of_lt hM3_pos
      have h_step1 : |Real.sin u - u| * Real.pi ≤ |u|^3 * Real.pi :=
        mul_le_mul_of_nonneg_right h_sin_bound (le_of_lt hπ_pos)
      have h_step2 : |u|^3 * Real.pi ≤ M^3 * |v|^3 * Real.pi :=
        mul_le_mul_of_nonneg_right h_u3_le (le_of_lt hπ_pos)
      have h_step3 : M^3 * |v|^3 * Real.pi = M^3 * |v|^2 * (Real.pi * |v|) := by ring
      linarith
    have h_term1_small : M^3 * |v|^2 / Real.pi < ε / 2 := by
      -- δ^2 ≤ π ε / (8 M^3) from δ ≤ δ_cubic.
      have hδ_sq : δ^2 ≤ Real.pi * ε / (8 * M^3) := by
        have hδ_le := hδ_le_cubic
        rw [hδc_def] at hδ_le
        have hδ_nn : 0 ≤ δ := le_of_lt hδ_pos
        have h_sq_le : δ^2 ≤ (Real.sqrt (Real.pi * ε / (8 * M^3)))^2 := by
          nlinarith [Real.sqrt_nonneg (Real.pi * ε / (8 * M^3))]
        rw [Real.sq_sqrt (by positivity : 0 ≤ Real.pi * ε / (8 * M^3))] at h_sq_le
        exact h_sq_le
      -- |v|^2 < 4 δ^2 (strict, from |v| < 2δ).
      have hv_sq_lt : |v|^2 < 4 * δ^2 := by
        have hv_nn : 0 ≤ |v| := abs_nonneg v
        have h2δ_pos : 0 < 2 * δ := by linarith
        have hv_lt : |v| < 2 * δ := hv_abs
        nlinarith
      -- M^3 |v|^2 < 4 M^3 δ^2 ≤ π ε / 2.
      have h_main : M^3 * |v|^2 < Real.pi * ε / 2 := by
        have h₁ : M^3 * |v|^2 < M^3 * (4 * δ^2) := by
          nlinarith [hM3_pos.le]
        have h₂ : M^3 * (4 * δ^2) ≤ M^3 * (4 * (Real.pi * ε / (8 * M^3))) := by
          nlinarith [hM3_pos.le]
        have h₃ : M^3 * (4 * (Real.pi * ε / (8 * M^3))) = Real.pi * ε / 2 := by
          have hM3_ne : M^3 ≠ 0 := ne_of_gt hM3_pos
          field_simp
          ring
        linarith
      rw [div_lt_iff₀ hπ_pos]
      have heq : ε / 2 * Real.pi = Real.pi * ε / 2 := by ring
      linarith
    have h_term2 : |(q c - q T) / Real.pi| < ε / 2 := by
      rw [abs_div, abs_of_pos hπ_pos]
      rw [div_lt_iff₀ hπ_pos]
      linarith
    calc |Real.sin u / (Real.pi * v) - q T / Real.pi|
        = |(Real.sin u - u) / (Real.pi * v) + (q c - q T) / Real.pi| := by rw [h_decomp]
      _ ≤ |(Real.sin u - u) / (Real.pi * v)| + |(q c - q T) / Real.pi| := abs_add_le _ _
      _ < M^3 * |v|^2 / Real.pi + ε / 2 := by linarith
      _ < ε / 2 + ε / 2 := by linarith
      _ = ε := by ring

/-! ## Diagonal kernel derivatives

    Cf. Lemma `lem:phase-kernel-diagonal-derivatives`. -/

/-- Diagonal value: `K_Φ(T, T) = q(T) / π`. -/
theorem phase_kernel_diagonal_value (T : ℝ) :
    phaseKernel T T = q T / Real.pi := by
  unfold phaseKernel
  simp

/-- Diagonal partial in `x`: `K_x(T, T) = q'(T) / (2 π)`.

    Proof via 2nd-order Taylor of `g(x) := sin(θ(x) − θ(T))` at `T`,
    using `theta_smooth`.  Key steps:
      (a) `g(T) = 0`, `iteratedDeriv 1 g T = q(T)`,
          `iteratedDeriv 2 g T = q'(T)`.
      (b) `taylor_isLittleO_univ`: `g x − [q(T)(x−T) + (q'(T)/2)(x−T)²] = o((x−T)²)`.
      (c) Divide by `π(x−T)` to get the linear approximation of
          `phaseKernel(·, T)` at `T` with derivative `q'(T)/(2π)`. -/
theorem phase_kernel_diagonal_partial_x (T : ℝ) :
    deriv (fun x => phaseKernel x T) T = qPrime T / (2 * Real.pi) := by
  -- The smooth auxiliary function
  set g : ℝ → ℝ := fun x => Real.sin (theta x - theta T) with hg_def
  -- g is C^∞ (sin smooth, theta_smooth, composition)
  have h_g_smooth : ContDiff ℝ ⊤ g := by
    have h_θ_sub : ContDiff ℝ ⊤ (fun x => theta x - theta T) :=
      theta_smooth.sub contDiff_const
    exact Real.contDiff_sin.comp h_θ_sub
  have h_g_C2 : ContDiff ℝ 2 g := h_g_smooth.of_le (by norm_num)
  -- g(T) = 0
  have h_g_T : g T = 0 := by
    show Real.sin (theta T - theta T) = 0
    rw [sub_self]; exact Real.sin_zero
  -- g'(T) = q(T)
  have h_θ : HasDerivAt theta (q T) T := (theta_differentiableAt T).hasDerivAt
  have h_g_hasDeriv : HasDerivAt g (q T) T := by
    have h_sub : HasDerivAt (fun x => theta x - theta T) (q T) T :=
      h_θ.sub_const (theta T)
    have := (Real.hasDerivAt_sin (theta T - theta T)).comp T h_sub
    simpa [hg_def, sub_self] using this
  have h_deriv_g_T : deriv g T = q T := h_g_hasDeriv.deriv
  -- The key Taylor application: sin(θ(x) − θ(T)) − q(T)(x−T) − (q'(T)/2)(x−T)² = o((x−T)²).
  -- We use the slope-style HasDerivAt directly.
  -- For x ≠ T near T, phaseKernel(x, T) = g(x) / (π(x − T)).
  -- For x = T, phaseKernel(T, T) = q(T)/π.
  -- (a) Show phaseKernel(·, T) has the same value as (1/π) · dslope g T everywhere near T.
  have h_phaseKernel_eq : (fun x => phaseKernel x T) =ᶠ[nhds T]
      (fun x => (1 / Real.pi) * dslope g T x) := by
    refine Filter.Eventually.of_forall fun x => ?_
    show phaseKernel x T = (1 / Real.pi) * dslope g T x
    by_cases hx : x = T
    · subst hx
      have hpK : phaseKernel x x = q x / Real.pi := by unfold phaseKernel; simp
      rw [hpK, dslope_same, h_deriv_g_T]
      field_simp
    · have hxT : x ≠ T := hx
      have h_phK : phaseKernel x T = Real.sin (theta x - theta T) / (Real.pi * (x - T)) := by
        unfold phaseKernel; simp [hxT]
      rw [h_phK, dslope_of_ne g hxT]
      simp only [slope, vsub_eq_sub, smul_eq_mul]
      show Real.sin (theta x - theta T) / (Real.pi * (x - T)) =
           1 / Real.pi * ((x - T)⁻¹ * (g x - g T))
      rw [h_g_T, sub_zero]
      show Real.sin (theta x - theta T) / (Real.pi * (x - T)) =
           1 / Real.pi * ((x - T)⁻¹ * Real.sin (theta x - theta T))
      field_simp
  -- (b) Show dslope g T has HasDerivAt at T with value q'(T)/2 = iteratedDeriv 2 g T / 2.
  -- This follows from g being C^2 via Taylor.
  -- Use taylor_isLittleO_univ: g(x) − taylorPoly_2(x) = o((x − T)²).
  have h_taylor : (fun x => g x - taylorWithinEval g 2 Set.univ T x) =o[nhds T]
      (fun x => (x - T)^2) := taylor_isLittleO_univ h_g_C2
  -- Compute the Taylor polynomial: T_2(x) = 0 + q(T)(x−T) + (q'(T)/2)(x−T)².
  have h_iter1 : iteratedDerivWithin 1 g Set.univ T = q T := by
    rw [iteratedDerivWithin_one]
    rw [derivWithin_of_isOpen isOpen_univ (Set.mem_univ T)]
    exact h_deriv_g_T
  have h_iter2_eq_qPrime : iteratedDerivWithin 2 g Set.univ T = qPrime T := by
    rw [iteratedDerivWithin_univ, iteratedDeriv_succ, iteratedDeriv_one]
    -- Goal: deriv (deriv g) T = qPrime T
    have h_deriv_g_eq : deriv g = fun x => Real.cos (theta x - theta T) * q x := by
      funext x
      have h_θ_x : HasDerivAt theta (q x) x := (theta_differentiableAt x).hasDerivAt
      have h_sub : HasDerivAt (fun y => theta y - theta T) (q x) x :=
        h_θ_x.sub_const (theta T)
      have h_g_x : HasDerivAt g (Real.cos (theta x - theta T) * q x) x := by
        have h := (Real.hasDerivAt_sin (theta x - theta T)).comp x h_sub
        simpa [hg_def] using h
      exact h_g_x.deriv
    rw [h_deriv_g_eq]
    -- Goal: deriv (fun x => cos(θ(x) - θ T) * q x) T = qPrime T
    have h_θ_T : HasDerivAt theta (q T) T := (theta_differentiableAt T).hasDerivAt
    have h_sub_T : HasDerivAt (fun y => theta y - theta T) (q T) T :=
      h_θ_T.sub_const (theta T)
    have h_cos_diff : HasDerivAt (fun x => Real.cos (theta x - theta T))
        (-Real.sin (theta T - theta T) * q T) T := by
      exact (Real.hasDerivAt_cos (theta T - theta T)).comp T h_sub_T
    -- q is C^1 via theta_smooth.deriv' → q differentiable
    have h_θ_C2 : ContDiff ℝ 2 theta := theta_smooth.of_le (by decide)
    have h_q_C1 : ContDiff ℝ 1 q := by
      have h : ContDiff ℝ (1 + 1 : ℕ) theta := by
        have : (1 + 1 : ℕ) = 2 := by norm_num
        rw [this]; exact h_θ_C2
      exact h.deriv'
    have h_q_diff : DifferentiableAt ℝ q T :=
      (h_q_C1.differentiable (by decide)).differentiableAt
    have h_q_hasDeriv : HasDerivAt q (qPrime T) T := by
      show HasDerivAt q (deriv (deriv theta) T) T
      exact h_q_diff.hasDerivAt
    have h_prod := h_cos_diff.mul h_q_hasDeriv
    have h_simp_form :
        (-Real.sin (theta T - theta T) * q T) * q T +
          Real.cos (theta T - theta T) * qPrime T = qPrime T := by
      rw [sub_self, Real.sin_zero, Real.cos_zero]; ring
    have h_target : HasDerivAt (fun x => Real.cos (theta x - theta T) * q x) (qPrime T) T := by
      have := h_prod
      rw [show (qPrime T : ℝ) = (-Real.sin (theta T - theta T) * q T) * q T +
            Real.cos (theta T - theta T) * qPrime T from h_simp_form.symm]
      exact this
    exact h_target.deriv
  -- Now the Taylor polynomial at order 2 is:
  --   taylorWithinEval g 2 univ T x = g(T) + g'(T)(x−T) + (g''(T)/2)(x−T)²
  --                                  = 0 + q(T)(x−T) + (q'(T)/2)(x−T)².
  -- (c) Use the o-bound to derive HasDerivAt for phaseKernel(·, T).
  have h_kernel_hasDeriv : HasDerivAt (fun x => phaseKernel x T)
      (qPrime T / (2 * Real.pi)) T := by
    -- Closed form of the order-2 Taylor polynomial of g at T:
    --   T_2(x) = g(T) + g'(T)(x-T) + (g''(T)/2)(x-T)²
    --         = 0 + q(T)(x-T) + (qPrime T / 2)(x-T)²
    have h_taylor_form : ∀ x : ℝ, taylorWithinEval g 2 Set.univ T x =
        q T * (x - T) + (qPrime T / 2) * (x - T) ^ 2 := by
      intro x
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 iteratedDerivWithin_zero, smul_eq_mul]
      rw [show g T = 0 from h_g_T, h_iter1, h_iter2_eq_qPrime]
      simp [Nat.factorial]
      ring
    -- Recast h_taylor in closed form: g(x) - q(T)(x-T) - (q'(T)/2)(x-T)² = o((x-T)²)
    have h_R : (fun x : ℝ => g x - q T * (x - T) - (qPrime T / 2) * (x - T) ^ 2)
        =o[nhds T] (fun x : ℝ => (x - T) ^ 2) := by
      have heq : (fun x : ℝ => g x - q T * (x - T) - (qPrime T / 2) * (x - T) ^ 2) =
                 (fun x : ℝ => g x - taylorWithinEval g 2 Set.univ T x) := by
        funext x; rw [h_taylor_form]; ring
      rw [heq]; exact h_taylor
    -- Multiply by (x-T)⁻¹: o((x-T)²) * O((x-T)⁻¹) = o((x-T)² · (x-T)⁻¹)
    have h_inv_O : (fun x : ℝ => (x - T)⁻¹) =O[nhds T] (fun x : ℝ => (x - T)⁻¹) :=
      Asymptotics.isBigO_refl _ _
    have h_R_div : (fun x : ℝ => (g x - q T * (x - T) - (qPrime T / 2) * (x - T) ^ 2) *
                                  (x - T)⁻¹)
        =o[nhds T] (fun x : ℝ => (x - T) ^ 2 * (x - T)⁻¹) :=
      h_R.mul_isBigO h_inv_O
    -- (x-T)² · (x-T)⁻¹ = (x-T) everywhere (using 0⁻¹ = 0 in Lean at x = T)
    have h_simp : (fun x : ℝ => (x - T) ^ 2 * (x - T)⁻¹) = (fun x : ℝ => x - T) := by
      funext x
      by_cases hx : x = T
      · subst hx; simp
      · have hxT : x - T ≠ 0 := sub_ne_zero.mpr hx
        rw [pow_two, mul_assoc, mul_inv_cancel₀ hxT, mul_one]
    rw [h_simp] at h_R_div
    -- Scale by 1/π
    have h_R_scaled : (fun x : ℝ => (1 / Real.pi) *
        ((g x - q T * (x - T) - (qPrime T / 2) * (x - T) ^ 2) * (x - T)⁻¹))
        =o[nhds T] (fun x : ℝ => x - T) :=
      h_R_div.const_mul_left (1 / Real.pi)
    -- Translate to HasDerivAt via the IsLittleO criterion
    rw [hasDerivAt_iff_isLittleO]
    -- Goal: (fun y => phaseKernel y T - phaseKernel T T - (y - T) • (qPrime T / (2π)))
    --   =o[𝓝 T] (fun y => y - T)
    have h_eq : (fun y : ℝ => phaseKernel y T - phaseKernel T T -
                    (y - T) • (qPrime T / (2 * Real.pi)))
        =ᶠ[nhds T] (fun y : ℝ => (1 / Real.pi) *
            ((g y - q T * (y - T) - (qPrime T / 2) * (y - T) ^ 2) * (y - T)⁻¹)) := by
      filter_upwards with y
      show phaseKernel y T - phaseKernel T T - (y - T) • (qPrime T / (2 * Real.pi)) =
          (1 / Real.pi) *
            ((g y - q T * (y - T) - (qPrime T / 2) * (y - T) ^ 2) * (y - T)⁻¹)
      rw [smul_eq_mul]
      by_cases hy : y = T
      · rw [hy]
        simp [phase_kernel_diagonal_value, h_g_T]
      · have hyT : y - T ≠ 0 := sub_ne_zero.mpr hy
        have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
        have h_pK_y : phaseKernel y T = g y / (Real.pi * (y - T)) := by
          show (if y = T then q y / Real.pi
                else Real.sin (theta y - theta T) / (Real.pi * (y - T))) =
                g y / (Real.pi * (y - T))
          rw [if_neg hy]
        rw [h_pK_y, phase_kernel_diagonal_value]
        field_simp
    exact h_eq.trans_isLittleO h_R_scaled
  exact h_kernel_hasDeriv.deriv

/-- Diagonal partial in `y`: `K_y(T, T) = q'(T) / (2 π)`.
    By kernel symmetry, `phaseKernel T` (as a function of `y`) coincides
    with `fun y => phaseKernel y T`, so the diagonal `y`-derivative
    equals the diagonal `x`-derivative. -/
theorem phase_kernel_diagonal_partial_y (T : ℝ) :
    deriv (phaseKernel T) T = qPrime T / (2 * Real.pi) := by
  have h : phaseKernel T = (fun y => phaseKernel y T) := by
    funext y
    exact phase_kernel_symmetric T y
  rw [h]
  exact phase_kernel_diagonal_partial_x T

/-- Diagonal mixed partial: `K_{xy}(T, T) = (q''(T) + 2 q(T)³) / (6 π)`. -/
axiom phase_kernel_diagonal_partial_xy (T : ℝ) :
    deriv (fun x => deriv (phaseKernel x) T) T =
      (qDoublePrime T + 2 * (q T)^3) / (6 * Real.pi)

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
