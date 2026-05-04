/-
The Riemann–Siegel phase function and its derivatives.

This module isolates the heavyweight log-Gamma / digamma infrastructure
underpinning the Riemann–Siegel phase used in `rh_rebuild.tex` Sections
2–3.

The paper's `θ` is the unique holomorphic branch of `log Γ z` on
`Re z > 0` normalized to be real on the positive real axis, restricted
to `z = 1/4 + i t / 2`.  This branch is C^∞ on its full domain and
agrees with the principal branch only away from the principal cut of
`Complex.log` traversed by `t ↦ Γ(1/4 + i t / 2)`.

We therefore keep `theta` abstract (a primitive symbol satisfying the
asymptotic theorems below) and quarantine the principal-branch
expression as `thetaPrincipal`, which is **not** the active phase.  A
future bridge theorem `thetaPrincipal_eq_theta_of_no_branch_crossing`
relates the two off the branch cut.

WARNING: Earlier drafts defined `theta` directly via
`Complex.log ∘ Complex.Gamma`.  That definition is *unsafe* — at branch
crossings of `t ↦ Γ(1/4 + i t / 2)`, the principal logarithm has 2π
jumps, and `deriv (principal-branch theta)` does not equal `deriv
(continuous-branch theta)`.  The matrix kernel `sin(θ(x) − θ(y))` is
unaffected, but the derivatives `q = θ'`, `q' = θ''`, `q'' = θ'''`
(used in `J(T)` and `D_J(T)`) are not.  Do not revert.

Maps to the LaTeX as follows:
  RH.RiemannSiegelTheta.theta
      ↔ θ(t) of `def:riemann-siegel-phase` (continuous branch)
  RH.RiemannSiegelTheta.q, qPrime, qDoublePrime
      ↔ q = θ', q' = θ'', q'' = θ'''
  RH.RiemannSiegelTheta.thetaPrincipal
      ↔ principal-branch expression `Im(log Γ(1/4 + i t / 2))
              − (t/2) log π`,
        principal-branch expression only; no global equality with
        `theta` is asserted here.

Theorems:
  theta_derivative_asymptotics       ↔ Lemma `lem:theta-derivative-asymptotics`
  theta_derivative_asymptotics_dyadic ↔ same on `[T/2, 2T]` window
  phase_derivative_lower_bound       ↔ Lemma `lem:phase-derivative-lower-bound`
-/

import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Taylor
import Mathlib.Topology.Order.Compact

namespace RH.RiemannSiegelTheta

open Real Complex

/-! ## Abstract phase function

`theta` is the continuous Riemann–Siegel phase: the unique holomorphic
branch of `log Γ z` on `Re z > 0` (real on the positive axis), evaluated
along `z(t) = 1/4 + i t / 2`, minus `(t/2) log π`.  It is treated as an
abstract primitive in this module; its concrete construction (and the
proof that it is C^∞ on `(0, ∞)`) is part of the deferred
`theta_derivative_asymptotics`.

The kernel `sin(θ(x) − θ(y))` and its derivatives only ever consume
`theta`, `q`, `qPrime`, `qDoublePrime` through the asymptotic
statements below; no caller should unfold `theta` to a closed form. -/

/-- The continuous Riemann–Siegel phase.

This is intentionally primitive at this stage.  The paper defines it via
the holomorphic branch of `log Γ` on `Re z > 0`; until that branch is
constructed in Lean, `theta` should not be implemented by the principal
branch. -/
opaque theta : ℝ → ℝ

/-- First derivative of the phase, `q := θ'`. -/
noncomputable def q (t : ℝ) : ℝ := deriv theta t

/-- Second derivative of the phase, `q' := θ''`. -/
noncomputable def qPrime (t : ℝ) : ℝ := deriv (deriv theta) t

/-- Third derivative of the phase, `q'' := θ'''`. -/
noncomputable def qDoublePrime (t : ℝ) : ℝ := deriv (deriv (deriv theta)) t

/-! ## Principal-branch quarantine (not the active phase)

The principal-branch expression is recorded so a future bridge theorem
can relate it to the continuous-branch `theta` away from branch-cut
crossings of `t ↦ Γ(1/4 + i t / 2)`.  It is **not** used elsewhere in
this module or downstream. -/

/-- Principal-branch expression for the Riemann–Siegel phase, using
    `Complex.log` (principal logarithm).  This is not the paper's
    `θ`.  On intervals where the principal branch is continuous and
    agrees with the chosen holomorphic branch, it should differ from
    `theta` by an additive constant in `2πℤ`; no global equality or
    derivative statement is asserted here. -/
noncomputable def thetaPrincipal (t : ℝ) : ℝ :=
  (Complex.log (Complex.Gamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2))).im -
    (t / 2) * Real.log Real.pi

/-! ## Riemann–Siegel asymptotics

Differentiated Stirling for `log Γ` (or, equivalently, asymptotic
expansion of `digamma` at the half-period scale `t → ∞`).  Mathlib has
the leading term of Stirling but not the polynomial corrections, so
these are recorded as proof obligations.  Two window variants are
provided; dyadic is the paper's actual `I_T ⊂ [T/2, 2T]` interface. -/

/-- Smoothness of the continuous Riemann–Siegel phase on the real line.
    The paper definition (holomorphic branch of `log Γ` on `Re z > 0`,
    evaluated along `z = 1/4 + i t / 2`) is C^∞ on `(0, ∞)`; we record
    the strongest form (C^∞ on all of ℝ) as the foundational axiom.
    This implies `Differentiable ℝ theta` and `ContDiff ℝ k theta` for
    every `k`. -/
axiom theta_smooth : ContDiff ℝ ⊤ theta

/-- `theta` is differentiable at every real `t`.  Derived from the
    smoothness axiom. -/
theorem theta_differentiableAt (t : ℝ) : DifferentiableAt ℝ theta t :=
  (theta_smooth.differentiable (by decide)).differentiableAt

/-- `theta` is C^k for every k. -/
theorem theta_contDiff (k : ℕ∞) : ContDiff ℝ k theta :=
  theta_smooth.of_le le_top

/-- Dyadic-window form of differentiated theta asymptotics, matching the
    paper's `I_T ⊂ [T/2, 2T]` interface.  This is the preferred interface
    for downstream packet arguments and is the foundational analytic
    input from differentiated Stirling. -/
axiom theta_derivative_asymptotics_dyadic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T t : ℝ, T₀ ≤ T → T / 2 ≤ t → t ≤ 2 * T →
      |q t - ((1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2))|
        ≤ C / t^4 ∧
      |qPrime t - 1 / (2 * t)| ≤ C / t^3 ∧
      |qDoublePrime t - (-1) / (2 * t^2)| ≤ C / t^4

/-- Differentiated theta asymptotics on the surrogate window
    `[T - 1, T + 1]`.  Combines the three derivative bounds:
    `q  = (1/2) log(t/(2π)) - 1/(48 t²) + O(t⁻⁴)`,
    `q' = 1/(2t) + O(t⁻³)`, and
    `q'' = -1/(2t²) + O(t⁻⁴)`.

    Derived from `theta_derivative_asymptotics_dyadic`: for `T ≥ 2`,
    the inclusion `[T - 1, T + 1] ⊂ [T/2, 2T]` is automatic, so the
    dyadic bound applies. -/
theorem theta_derivative_asymptotics :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T → ∀ t : ℝ, T - 1 ≤ t → t ≤ T + 1 →
      |q t - ((1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2))|
        ≤ C / t^4 ∧
      |qPrime t - 1 / (2 * t)| ≤ C / t^3 ∧
      |qDoublePrime t - (-1) / (2 * t^2)| ≤ C / t^4 := by
  obtain ⟨T₀', C', hT₀'_pos, hC'_nn, hasymp⟩ := theta_derivative_asymptotics_dyadic
  refine ⟨max T₀' 2, C', ?_, hC'_nn, ?_⟩
  · exact lt_max_of_lt_right (by norm_num)
  intro T hT t ht_lo ht_hi
  have hT_T₀' : T₀' ≤ T := le_trans (le_max_left _ _) hT
  have hT_2 : (2 : ℝ) ≤ T := le_trans (le_max_right _ _) hT
  have h_half : T / 2 ≤ t := by linarith
  have h_double : t ≤ 2 * T := by linarith
  exact hasymp T t hT_T₀' h_half h_double

/-- Phase-derivative lower bound (P2):
    on retained packets at sufficiently large `T`,
    `q(t) ≥ (1/2) log(T/(4π)) - C/T²`.

    Extracted from `theta_derivative_asymptotics` by combining the
    asymptotic `q t = (1/2) log(t/(2π)) - 1/(48 t²) + O(t⁻⁴)` with the
    window inclusion `t ≥ T - 1 ≥ T/2` (valid for `T ≥ 2`), which gives
    `log(t/(2π)) ≥ log(T/(4π))` and `t² ≥ T²/4`. -/
theorem phase_derivative_lower_bound :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T → ∀ t : ℝ, T - 1 ≤ t → t ≤ T + 1 →
    q t ≥ (1/2) * Real.log (T / (4 * Real.pi)) - C / T^2 := by
  obtain ⟨T₀', C', hT₀'_pos, hC'_nn, hasymp⟩ := theta_derivative_asymptotics
  refine ⟨max T₀' 2, 1/12 + 16 * C', ?_, ?_, ?_⟩
  · exact lt_max_of_lt_right (by norm_num)
  · positivity
  intro T hT t ht_lo ht_hi
  have hT_T₀' : T₀' ≤ T := le_trans (le_max_left _ _) hT
  have hT_2 : (2 : ℝ) ≤ T := le_trans (le_max_right _ _) hT
  have hT_pos : 0 < T := by linarith
  have ht_pos : 0 < t := by linarith
  have ht_half : T / 2 ≤ t := by linarith
  obtain ⟨h_q_bound, _, _⟩ := hasymp T hT_T₀' t ht_lo ht_hi
  have h_q_lo : (1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2) - C' / t^4 ≤ q t := by
    have h_abs := abs_le.mp h_q_bound
    linarith [h_abs.1]
  have h_log_mono : Real.log (T / (4 * Real.pi)) ≤ Real.log (t / (2 * Real.pi)) := by
    apply Real.log_le_log (by positivity)
    rw [div_le_div_iff₀ (by positivity : (0:ℝ) < 4 * Real.pi)
        (by positivity : (0:ℝ) < 2 * Real.pi)]
    nlinarith [Real.pi_pos]
  have h_t_sq_lower : T^2 / 4 ≤ t^2 := by nlinarith
  have h_t_sq_pos : 0 < t^2 := by positivity
  have h_T_sq_pos : 0 < T^2 := by positivity
  have h_one_48 : 1 / (48 * t^2) ≤ 1 / (12 * T^2) := by
    rw [div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith
  have h_T_ge_1 : (1 : ℝ) ≤ T := by linarith
  have h_t_4_lower : T^4 / 16 ≤ t^4 := by nlinarith
  have h_T_sq_ge_1 : (1 : ℝ) ≤ T^2 := by nlinarith [h_T_ge_1]
  have h_T4_ge_T2 : T^2 ≤ T^4 := by nlinarith [h_T_sq_ge_1]
  have h_Cp_t4 : C' / t^4 ≤ 16 * C' / T^2 := by
    rw [div_le_div_iff₀ (by positivity) h_T_sq_pos]
    nlinarith [hC'_nn]
  have h_chain :
      (1/2) * Real.log (T / (4 * Real.pi)) - 1 / (12 * T^2) - 16 * C' / T^2 ≤ q t := by
    have h1 : (1/2) * Real.log (T / (4 * Real.pi)) ≤ (1/2) * Real.log (t / (2 * Real.pi)) := by
      linarith
    linarith
  have h_T_sq_ne : T^2 ≠ 0 := ne_of_gt h_T_sq_pos
  have h_combine_const :
      (1/2) * Real.log (T / (4 * Real.pi)) - 1 / (12 * T^2) - 16 * C' / T^2 =
      (1/2) * Real.log (T / (4 * Real.pi)) - (1/12 + 16 * C') / T^2 := by
    field_simp
    ring
  linarith

/-- Dyadic phase-derivative lower bound, matching the paper's retained
    packet interface `I_T ⊂ [T/2, 2T]`. -/
theorem phase_derivative_lower_bound_dyadic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T t : ℝ, T₀ ≤ T → T / 2 ≤ t → t ≤ 2 * T →
    q t ≥ (1/2) * Real.log (T / (4 * Real.pi)) - C / T^2 := by
  obtain ⟨T₀', C', hT₀'_pos, hC'_nn, hasymp⟩ := theta_derivative_asymptotics_dyadic
  refine ⟨max T₀' 2, 1/12 + 16 * C', ?_, ?_, ?_⟩
  · exact lt_max_of_lt_right (by norm_num)
  · positivity
  intro T t hT ht_lo ht_hi
  have hT_T₀' : T₀' ≤ T := le_trans (le_max_left _ _) hT
  have hT_2 : (2 : ℝ) ≤ T := le_trans (le_max_right _ _) hT
  have hT_pos : 0 < T := by linarith
  have ht_pos : 0 < t := by linarith
  obtain ⟨h_q_bound, _, _⟩ := hasymp T t hT_T₀' ht_lo ht_hi
  have h_q_lo : (1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2) - C' / t^4 ≤ q t := by
    have h_abs := abs_le.mp h_q_bound
    linarith [h_abs.1]
  have h_log_mono : Real.log (T / (4 * Real.pi)) ≤ Real.log (t / (2 * Real.pi)) := by
    apply Real.log_le_log (by positivity)
    rw [div_le_div_iff₀ (by positivity : (0:ℝ) < 4 * Real.pi)
        (by positivity : (0:ℝ) < 2 * Real.pi)]
    nlinarith [Real.pi_pos]
  have h_t_sq_lower : T^2 / 4 ≤ t^2 := by nlinarith
  have h_T_sq_pos : 0 < T^2 := by positivity
  have h_one_48 : 1 / (48 * t^2) ≤ 1 / (12 * T^2) := by
    rw [div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith
  have hT_ge_one : (1 : ℝ) ≤ T := by linarith
  have h_t_4_lower : T^4 / 16 ≤ t^4 := by nlinarith
  have h_T_sq_ge_one : (1 : ℝ) ≤ T^2 := by nlinarith [hT_ge_one]
  have h_T4_ge_T2 : T^2 ≤ T^4 := by nlinarith [h_T_sq_ge_one]
  have h_Cp_t4 : C' / t^4 ≤ 16 * C' / T^2 := by
    rw [div_le_div_iff₀ (by positivity) h_T_sq_pos]
    nlinarith [hC'_nn]
  have h_chain :
      (1/2) * Real.log (T / (4 * Real.pi)) - 1 / (12 * T^2) - 16 * C' / T^2 ≤ q t := by
    have h1 : (1/2) * Real.log (T / (4 * Real.pi)) ≤ (1/2) * Real.log (t / (2 * Real.pi)) := by
      linarith
    linarith
  have h_combine_const :
      (1/2) * Real.log (T / (4 * Real.pi)) - 1 / (12 * T^2) - 16 * C' / T^2 =
      (1/2) * Real.log (T / (4 * Real.pi)) - (1/12 + 16 * C') / T^2 := by
    field_simp
    ring
  linarith

/-! ## Taylor remainder bounds (infrastructure for rate axioms)

    These compact-interval Lagrange remainder bounds are foundational
    pieces for closing `same_point_jet_limit_rate` and
    `cross_block_jet_limit_rate`.  They follow from `theta_smooth` plus
    Mathlib's `taylor_mean_remainder_lagrange_iteratedDeriv`. -/

/-- Order-2 Taylor remainder for `q` at `T` on the unit interval.
    Asserts the existence of a uniform constant `K ≥ 0` such that for
    every `h ∈ [-1, 1]`,
        `|q(T+h) − (q(T) + q'(T) h + q''(T) h²/2)| ≤ K |h|³`.

    Proof: `q ∈ C^∞` (via `theta_smooth`), so `iteratedDeriv 3 q` is
    continuous and bounded on `[T − 1, T + 1]`.  Apply Lagrange
    remainder with `n = 2` to get the bound. -/
theorem q_taylor_remainder_2 (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ 1 →
      |q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2 / 2)| ≤ K * |h|^3 := by
  -- q is C^∞, so iteratedDeriv 3 q is continuous.
  have hθ_C4 : ContDiff ℝ 4 theta := theta_smooth.of_le (by decide)
  have h_q_C3 : ContDiff ℝ 3 q := by
    have h : ContDiff ℝ (3 + 1 : ℕ) theta := by
      rw [show (3 + 1 : ℕ) = 4 from by norm_num]; exact hθ_C4
    exact h.deriv'
  have h_iter3_cont : Continuous (iteratedDeriv 3 q) :=
    h_q_C3.continuous_iteratedDeriv 3 (by decide)
  -- Bound on the compact set [T-1, T+1].
  have h_compact : IsCompact (Set.Icc (T - 1) (T + 1)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - 1) (T + 1)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 3 q y|) (Set.Icc (T - 1) (T + 1)) :=
    (continuous_abs.comp h_iter3_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ := h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 3 q ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 6, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · -- Apply Lagrange remainder for q on uIcc T (T+h).
    have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have h_q_C3_on : ContDiffOn ℝ 3 q (Set.uIcc T (T + h)) := h_q_C3.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne h_q_C3_on
    -- The interval has unique-diff structure, since T ≠ T+h.
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    -- Compute the Taylor polynomial: T₂(T+h) = q T + qPrime T · h + qDoublePrime T · h²/2.
    have h_taylor_form : taylorWithinEval q 2 (Set.uIcc T (T + h)) T (T + h) =
        q T + qPrime T * h + qDoublePrime T * h^2 / 2 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 q (Set.uIcc T (T + h)) T = q T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 q (Set.uIcc T (T + h)) T = qPrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_q_C3.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      have h_iter2 : iteratedDerivWithin 2 q (Set.uIcc T (T + h)) T = qDoublePrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_q_C3.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      rw [h_iter0, h_iter1, h_iter2]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    -- |iteratedDeriv 3 q ξ| ≤ K₀ since ξ ∈ uIoo T (T+h) ⊂ [T-1, T+1].
    have hξ_in_Icc : ξ ∈ Set.Icc (T - 1) (T + 1) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - 1) (T + 1) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · -- h < 0
          have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -1 ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · -- h > 0
          have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ 1 := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have h_iter3_bound : |iteratedDeriv 3 q ξ| ≤ K₀ :=
      hymax hξ_in_Icc
    -- Now bound the remainder.
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2 / 2) =
        iteratedDeriv 3 q ξ * h^3 / 6 := by
      have h_fact : ((2 + 1).factorial : ℝ) = 6 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_6 : |(6 : ℝ)| = 6 := by norm_num
    rw [h_abs_6, div_le_iff₀ (by norm_num : (0:ℝ) < 6)]
    have hpow_nn : 0 ≤ |h|^3 := pow_nonneg (abs_nonneg _) 3
    calc |iteratedDeriv 3 q ξ| * |h|^3
        ≤ K₀ * |h|^3 :=
          mul_le_mul_of_nonneg_right h_iter3_bound hpow_nn
      _ = K₀ / 6 * |h|^3 * 6 := by ring

/-- Order-3 Taylor remainder for `theta` at `T` on the unit interval.
    Asserts the existence of a uniform constant `K ≥ 0` such that for
    every `h ∈ [-1, 1]`,
        `|theta(T+h) − (theta T + q T h + qPrime T h²/2 + qDoublePrime T h³/6)| ≤ K |h|⁴`.

    Proof: `theta ∈ C^∞`, so `iteratedDeriv 4 theta` is continuous and
    bounded on `[T − 1, T + 1]`.  Apply Lagrange remainder with `n = 3`. -/
theorem theta_taylor_remainder_3 (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ 1 →
      |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
        qDoublePrime T * h^3 / 6)| ≤ K * |h|^4 := by
  have hθ_C4 : ContDiff ℝ 4 theta := theta_smooth.of_le (by decide)
  have h_iter4_cont : Continuous (iteratedDeriv 4 theta) :=
    hθ_C4.continuous_iteratedDeriv 4 (by decide)
  have h_compact : IsCompact (Set.Icc (T - 1) (T + 1)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - 1) (T + 1)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 4 theta y|)
      (Set.Icc (T - 1) (T + 1)) :=
    (continuous_abs.comp h_iter4_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 4 theta ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 24, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have hθ_C4_on : ContDiffOn ℝ 4 theta (Set.uIcc T (T + h)) := hθ_C4.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne hθ_C4_on
    -- Unique-diff structure on uIcc.
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    -- Compute Taylor polynomial.
    have h_taylor_form : taylorWithinEval theta 3 (Set.uIcc T (T + h)) T (T + h) =
        theta T + q T * h + qPrime T * h^2 / 2 + qDoublePrime T * h^3 / 6 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 theta (Set.uIcc T (T + h)) T = theta T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 theta (Set.uIcc T (T + h)) T = q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C4.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      have h_iter2 : iteratedDerivWithin 2 theta (Set.uIcc T (T + h)) T = qPrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C4.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      have h_iter3 : iteratedDerivWithin 3 theta (Set.uIcc T (T + h)) T = qDoublePrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C4.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (3 : ℕ) = 2 + 1 from rfl, iteratedDeriv_succ,
            show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      rw [h_iter0, h_iter1, h_iter2, h_iter3]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    -- Bound iteratedDeriv 4 theta on [T-1, T+1].
    have hξ_in_Icc : ξ ∈ Set.Icc (T - 1) (T + 1) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - 1) (T + 1) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -1 ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ 1 := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have h_iter4_bound : |iteratedDeriv 4 theta ξ| ≤ K₀ :=
      hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : theta (T + h) -
        (theta T + q T * h + qPrime T * h^2 / 2 + qDoublePrime T * h^3 / 6) =
        iteratedDeriv 4 theta ξ * h^4 / 24 := by
      have h_fact : ((3 + 1).factorial : ℝ) = 24 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_24 : |(24 : ℝ)| = 24 := by norm_num
    rw [h_abs_24, div_le_iff₀ (by norm_num : (0:ℝ) < 24)]
    have hpow_nn : 0 ≤ |h|^4 := pow_nonneg (abs_nonneg _) 4
    calc |iteratedDeriv 4 theta ξ| * |h|^4
        ≤ K₀ * |h|^4 :=
          mul_le_mul_of_nonneg_right h_iter4_bound hpow_nn
      _ = K₀ / 24 * |h|^4 * 24 := by ring

/-- Order-3 Taylor remainder for `q` at `T` on the unit interval.
    Asserts the existence of a uniform constant `K ≥ 0` such that for
    every `h ∈ [-1, 1]`,
        `|q(T+h) − (q(T) + q'(T) h + q''(T) h²/2 + q'''(T) h³/6)| ≤ K |h|⁴`,
    where `q'''(T) = iteratedDeriv 3 q T = iteratedDeriv 4 theta T`.
    Apply Lagrange remainder with `n = 3`. -/
theorem q_taylor_remainder_3 (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ 1 →
      |q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2 / 2 +
        iteratedDeriv 3 q T * h^3 / 6)| ≤ K * |h|^4 := by
  have hθ_C5 : ContDiff ℝ 5 theta := theta_smooth.of_le (by decide)
  have h_q_C4 : ContDiff ℝ 4 q := by
    have h : ContDiff ℝ (4 + 1 : ℕ) theta := by
      rw [show (4 + 1 : ℕ) = 5 from by norm_num]; exact hθ_C5
    exact h.deriv'
  have h_iter4_cont : Continuous (iteratedDeriv 4 q) :=
    h_q_C4.continuous_iteratedDeriv 4 (by decide)
  have h_compact : IsCompact (Set.Icc (T - 1) (T + 1)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - 1) (T + 1)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 4 q y|)
      (Set.Icc (T - 1) (T + 1)) :=
    (continuous_abs.comp h_iter4_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 4 q ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 24, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have h_q_C4_on : ContDiffOn ℝ 4 q (Set.uIcc T (T + h)) := h_q_C4.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne h_q_C4_on
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    have h_taylor_form : taylorWithinEval q 3 (Set.uIcc T (T + h)) T (T + h) =
        q T + qPrime T * h + qDoublePrime T * h^2 / 2 +
        iteratedDeriv 3 q T * h^3 / 6 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 q (Set.uIcc T (T + h)) T = q T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 q (Set.uIcc T (T + h)) T = qPrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_q_C4.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      have h_iter2 : iteratedDerivWithin 2 q (Set.uIcc T (T + h)) T = qDoublePrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_q_C4.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      have h_iter3 : iteratedDerivWithin 3 q (Set.uIcc T (T + h)) T =
          iteratedDeriv 3 q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_q_C4.contDiffAt.of_le (by decide)) hT_mem]
      rw [h_iter0, h_iter1, h_iter2, h_iter3]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have hξ_in_Icc : ξ ∈ Set.Icc (T - 1) (T + 1) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - 1) (T + 1) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -1 ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ 1 := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have h_iter4_bound : |iteratedDeriv 4 q ξ| ≤ K₀ :=
      hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : q (T + h) - (q T + qPrime T * h + qDoublePrime T * h^2 / 2 +
        iteratedDeriv 3 q T * h^3 / 6) = iteratedDeriv 4 q ξ * h^4 / 24 := by
      have h_fact : ((3 + 1).factorial : ℝ) = 24 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_24 : |(24 : ℝ)| = 24 := by norm_num
    rw [h_abs_24, div_le_iff₀ (by norm_num : (0:ℝ) < 24)]
    have hpow_nn : 0 ≤ |h|^4 := pow_nonneg (abs_nonneg _) 4
    calc |iteratedDeriv 4 q ξ| * |h|^4
        ≤ K₀ * |h|^4 :=
          mul_le_mul_of_nonneg_right h_iter4_bound hpow_nn
      _ = K₀ / 24 * |h|^4 * 24 := by ring

/-- Order-5 Taylor remainder for `theta` at `T` on the unit interval.
    Asserts the existence of a uniform constant `K ≥ 0` such that for
    every `h ∈ [-1, 1]`,
        `|theta(T+h) − taylor_5(T+h)| ≤ K |h|⁶`,
    where `taylor_5(T+h) = theta T + q T h + qPrime T h²/2 +
        qDoublePrime T h³/6 + iteratedDeriv 4 theta T · h⁴/24 +
        iteratedDeriv 5 theta T · h⁵/120`.
    Apply Lagrange remainder with `n = 5`. -/
theorem theta_taylor_remainder_5 (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ 1 →
      |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
        qDoublePrime T * h^3 / 6 +
        iteratedDeriv 4 theta T * h^4 / 24 +
        iteratedDeriv 5 theta T * h^5 / 120)| ≤ K * |h|^6 := by
  have hθ_C6 : ContDiff ℝ 6 theta := theta_smooth.of_le (by decide)
  have h_iter6_cont : Continuous (iteratedDeriv 6 theta) :=
    hθ_C6.continuous_iteratedDeriv 6 (by decide)
  have h_compact : IsCompact (Set.Icc (T - 1) (T + 1)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - 1) (T + 1)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 6 theta y|)
      (Set.Icc (T - 1) (T + 1)) :=
    (continuous_abs.comp h_iter6_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 6 theta ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 720, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have hθ_C6_on : ContDiffOn ℝ 6 theta (Set.uIcc T (T + h)) := hθ_C6.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne hθ_C6_on
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    have h_taylor_form : taylorWithinEval theta 5 (Set.uIcc T (T + h)) T (T + h) =
        theta T + q T * h + qPrime T * h^2 / 2 + qDoublePrime T * h^3 / 6 +
        iteratedDeriv 4 theta T * h^4 / 24 +
        iteratedDeriv 5 theta T * h^5 / 120 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 theta (Set.uIcc T (T + h)) T = theta T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 theta (Set.uIcc T (T + h)) T = q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C6.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      have h_iter2 : iteratedDerivWithin 2 theta (Set.uIcc T (T + h)) T = qPrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C6.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      have h_iter3 : iteratedDerivWithin 3 theta (Set.uIcc T (T + h)) T = qDoublePrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C6.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (3 : ℕ) = 2 + 1 from rfl, iteratedDeriv_succ,
            show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      have h_iter4 : iteratedDerivWithin 4 theta (Set.uIcc T (T + h)) T =
          iteratedDeriv 4 theta T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C6.contDiffAt.of_le (by decide)) hT_mem]
      have h_iter5 : iteratedDerivWithin 5 theta (Set.uIcc T (T + h)) T =
          iteratedDeriv 5 theta T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C6.contDiffAt.of_le (by decide)) hT_mem]
      rw [h_iter0, h_iter1, h_iter2, h_iter3, h_iter4, h_iter5]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have hξ_in_Icc : ξ ∈ Set.Icc (T - 1) (T + 1) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - 1) (T + 1) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -1 ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ 1 := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have h_iter6_bound : |iteratedDeriv 6 theta ξ| ≤ K₀ :=
      hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2 +
        qDoublePrime T * h^3 / 6 + iteratedDeriv 4 theta T * h^4 / 24 +
        iteratedDeriv 5 theta T * h^5 / 120) =
        iteratedDeriv 6 theta ξ * h^6 / 720 := by
      have h_fact : ((5 + 1).factorial : ℝ) = 720 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_720 : |(720 : ℝ)| = 720 := by norm_num
    rw [h_abs_720, div_le_iff₀ (by norm_num : (0:ℝ) < 720)]
    have hpow_nn : 0 ≤ |h|^6 := pow_nonneg (abs_nonneg _) 6
    calc |iteratedDeriv 6 theta ξ| * |h|^6
        ≤ K₀ * |h|^6 :=
          mul_le_mul_of_nonneg_right h_iter6_bound hpow_nn
      _ = K₀ / 720 * |h|^6 * 720 := by ring

/-- Order-5 Taylor remainder for `Real.sin` at `0` (global bound).
    `|sin u − (u − u³/6 + u⁵/120)| ≤ |u|⁶ / 720` for every `u ∈ ℝ`.

    Proof: Apply `taylor_mean_remainder_lagrange_iteratedDeriv` to
    `Real.sin` on `uIcc 0 u` for `u ≠ 0` with `n = 5`, then use the
    universal bound `|iteratedDeriv 6 Real.sin ξ| ≤ 1`. -/
theorem sin_taylor_remainder_5 (u : ℝ) :
    |Real.sin u - (u - u^3/6 + u^5/120)| ≤ |u|^6 / 720 := by
  by_cases hu : u = 0
  · subst hu; simp
  · have h_ne : (0 : ℝ) ≠ u := Ne.symm hu
    have h_sin_C6_on : ContDiffOn ℝ 6 Real.sin (Set.uIcc 0 u) :=
      Real.contDiff_sin.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne h_sin_C6_on
    have h_min_lt_max : min (0:ℝ) u < max 0 u := by
      rcases lt_or_gt_of_ne hu with hlt | hgt
      · simp [min_eq_right hlt.le, max_eq_left hlt.le, hlt]
      · simp [min_eq_left hgt.le, max_eq_right hgt.le, hgt]
    have h_unique : UniqueDiffOn ℝ (Set.uIcc (0:ℝ) u) :=
      uniqueDiffOn_Icc h_min_lt_max
    -- Compute Taylor polynomial of sin at 0 to order 5: u - u³/6 + u⁵/120.
    have h_taylor_form : taylorWithinEval Real.sin 5 (Set.uIcc 0 u) 0 u =
        u - u^3/6 + u^5/120 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 sub_zero, smul_eq_mul]
      have h0_mem : (0:ℝ) ∈ Set.uIcc (0:ℝ) u := Set.left_mem_uIcc
      have h_sin_C : ContDiffAt ℝ 6 Real.sin 0 := Real.contDiff_sin.contDiffAt
      -- Functional equalities for iteratedDeriv k Real.sin.
      have h_iter1_func : iteratedDeriv 1 Real.sin = Real.cos := by
        rw [iteratedDeriv_one, Real.deriv_sin]
      have h_iter2_func : iteratedDeriv 2 Real.sin = -Real.sin := by
        rw [show (2:ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, h_iter1_func,
            Real.deriv_cos']
        funext x; simp [Pi.neg_apply]
      have h_iter3_func : iteratedDeriv 3 Real.sin = -Real.cos := by
        rw [show (3:ℕ) = 2 + 1 from rfl, iteratedDeriv_succ, h_iter2_func]
        rw [deriv.neg', Real.deriv_sin]
        funext x; rfl
      have h_iter4_func : iteratedDeriv 4 Real.sin = Real.sin := by
        rw [show (4:ℕ) = 3 + 1 from rfl, iteratedDeriv_succ, h_iter3_func]
        rw [deriv.neg', Real.deriv_cos']
        funext x; simp
      have h_iter5_func : iteratedDeriv 5 Real.sin = Real.cos := by
        rw [show (5:ℕ) = 4 + 1 from rfl, iteratedDeriv_succ, h_iter4_func, Real.deriv_sin]
      have h_iter_eq : ∀ k ≤ 5,
          iteratedDerivWithin k Real.sin (Set.uIcc 0 u) 0 = iteratedDeriv k Real.sin 0 := by
        intro k hk
        exact iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_sin_C.of_le (by exact_mod_cast (by omega : k ≤ 6))) h0_mem
      have h0v : iteratedDeriv 0 Real.sin 0 = 0 := by
        rw [iteratedDeriv_zero]; exact Real.sin_zero
      have h1v : iteratedDeriv 1 Real.sin 0 = 1 := by
        rw [h_iter1_func]; exact Real.cos_zero
      have h2v : iteratedDeriv 2 Real.sin 0 = 0 := by
        rw [h_iter2_func]; show (-Real.sin) 0 = 0
        simp [Pi.neg_apply, Real.sin_zero]
      have h3v : iteratedDeriv 3 Real.sin 0 = -1 := by
        rw [h_iter3_func]; show (-Real.cos) 0 = -1
        simp [Pi.neg_apply, Real.cos_zero]
      have h4v : iteratedDeriv 4 Real.sin 0 = 0 := by
        rw [h_iter4_func]; exact Real.sin_zero
      have h5v : iteratedDeriv 5 Real.sin 0 = 1 := by
        rw [h_iter5_func]; exact Real.cos_zero
      rw [h_iter_eq 0 (by norm_num), h_iter_eq 1 (by norm_num),
          h_iter_eq 2 (by norm_num), h_iter_eq 3 (by norm_num),
          h_iter_eq 4 (by norm_num), h_iter_eq 5 (by norm_num)]
      rw [h0v, h1v, h2v, h3v, h4v, h5v]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have h_iter6_bound : |iteratedDeriv 6 Real.sin ξ| ≤ 1 :=
      Real.abs_iteratedDeriv_sin_le_one 6 ξ
    have h_h_eq : u - 0 = u := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : Real.sin u - (u - u^3/6 + u^5/120) =
        iteratedDeriv 6 Real.sin ξ * u^6 / 720 := by
      have h_fact : ((5 + 1).factorial : ℝ) = 720 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_720 : |(720 : ℝ)| = 720 := by norm_num
    rw [h_abs_720, div_le_iff₀ (by norm_num : (0:ℝ) < 720)]
    have hpow_nn : 0 ≤ |u|^6 := pow_nonneg (abs_nonneg _) 6
    calc |iteratedDeriv 6 Real.sin ξ| * |u|^6
        ≤ 1 * |u|^6 := mul_le_mul_of_nonneg_right h_iter6_bound hpow_nn
      _ = |u|^6 / 720 * 720 := by ring

/-- sin Taylor remainder at an arbitrary point `y` to order 1.

    For any `y, u : ℝ`,
        `|sin(y + u) − (sin y + cos y · u)| ≤ u²/2`.

    Proof: Apply Lagrange remainder for `Real.sin` on `uIcc y (y+u)`
    with `n = 1`, then use `Real.abs_iteratedDeriv_sin_le_one`. -/
theorem sin_taylor_at_quad (y u : ℝ) :
    |Real.sin (y + u) - (Real.sin y + Real.cos y * u)| ≤ u^2 / 2 := by
  by_cases hu : u = 0
  · subst hu; simp
  · have h_ne : y ≠ y + u := fun e => hu (by linarith)
    have h_sin_C2_on : ContDiffOn ℝ 2 Real.sin (Set.uIcc y (y + u)) :=
      Real.contDiff_sin.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne h_sin_C2_on
    have h_min_lt_max : min y (y + u) < max y (y + u) := by
      rcases lt_or_gt_of_ne hu with hlt | hgt
      · have h1 : y + u < y := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : y < y + u := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc y (y + u)) :=
      uniqueDiffOn_Icc h_min_lt_max
    -- Taylor polynomial of sin at y to order 1: sin y + cos y · u.
    have h_taylor_form : taylorWithinEval Real.sin 1 (Set.uIcc y (y + u)) y (y + u) =
        Real.sin y + Real.cos y * u := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hy_mem : y ∈ Set.uIcc y (y + u) := Set.left_mem_uIcc
      have h_sin_C : ContDiffAt ℝ 2 Real.sin y := Real.contDiff_sin.contDiffAt
      have h_iter1_func : iteratedDeriv 1 Real.sin = Real.cos := by
        rw [iteratedDeriv_one, Real.deriv_sin]
      have h_iter_eq : ∀ k ≤ 1,
          iteratedDerivWithin k Real.sin (Set.uIcc y (y + u)) y =
            iteratedDeriv k Real.sin y := by
        intro k hk
        exact iteratedDerivWithin_eq_iteratedDeriv h_unique
            (h_sin_C.of_le (by exact_mod_cast (by omega : k ≤ 2))) hy_mem
      have h0v : iteratedDeriv 0 Real.sin y = Real.sin y := by
        rw [iteratedDeriv_zero]
      have h1v : iteratedDeriv 1 Real.sin y = Real.cos y := by
        rw [h_iter1_func]
      rw [h_iter_eq 0 (by norm_num), h_iter_eq 1 (by norm_num)]
      rw [h0v, h1v]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have h_iter2_bound : |iteratedDeriv 2 Real.sin ξ| ≤ 1 :=
      Real.abs_iteratedDeriv_sin_le_one 2 ξ
    have h_h_eq : (y + u) - y = u := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : Real.sin (y + u) - (Real.sin y + Real.cos y * u) =
        iteratedDeriv 2 Real.sin ξ * u^2 / 2 := by
      have h_fact : ((1 + 1).factorial : ℝ) = 2 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_2 : |(2 : ℝ)| = 2 := by norm_num
    rw [h_abs_2, div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    have hpow_nn : 0 ≤ |u|^2 := pow_nonneg (abs_nonneg _) 2
    have h_pow_eq : |u|^2 = u^2 := by rw [sq_abs]
    calc |iteratedDeriv 2 Real.sin ξ| * |u|^2
        ≤ 1 * |u|^2 := mul_le_mul_of_nonneg_right h_iter2_bound hpow_nn
      _ = u^2 := by rw [h_pow_eq]; ring
      _ = u^2 / 2 * 2 := by ring

/-- Theta Taylor remainder at order 1, parameterized by radius `R > 0`:
    there is a uniform constant `K ≥ 0` on `[T - R, T + R]` such that for
    every `h ∈ [-R, R]`,
        `|theta(T + h) − (theta T + q T · h)| ≤ K · h²`. -/
theorem theta_taylor_remainder_1_on (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) - (theta T + q T * h)| ≤ K * h^2 := by
  have hθ_C2 : ContDiff ℝ 2 theta := theta_smooth.of_le (by decide)
  have h_iter2_cont : Continuous (iteratedDeriv 2 theta) :=
    hθ_C2.continuous_iteratedDeriv 2 (by decide)
  have h_compact : IsCompact (Set.Icc (T - R) (T + R)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - R) (T + R)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 2 theta y|)
      (Set.Icc (T - R) (T + R)) :=
    (continuous_abs.comp h_iter2_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 2 theta ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 2, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have hθ_C2_on : ContDiffOn ℝ 2 theta (Set.uIcc T (T + h)) := hθ_C2.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne hθ_C2_on
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    have h_taylor_form : taylorWithinEval theta 1 (Set.uIcc T (T + h)) T (T + h) =
        theta T + q T * h := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 theta (Set.uIcc T (T + h)) T = theta T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 theta (Set.uIcc T (T + h)) T = q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C2.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      rw [h_iter0, h_iter1]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have hξ_in_Icc : ξ ∈ Set.Icc (T - R) (T + R) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - R) (T + R) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -R ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ R := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have hξ_bound : |iteratedDeriv 2 theta ξ| ≤ K₀ := hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : theta (T + h) - (theta T + q T * h) =
        iteratedDeriv 2 theta ξ * h^2 / 2 := by
      have h_fact : ((1 + 1).factorial : ℝ) = 2 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_2 : |(2 : ℝ)| = 2 := by norm_num
    rw [h_abs_2, div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    have hpow_nn : 0 ≤ |h|^2 := pow_nonneg (abs_nonneg _) 2
    have h_pow_eq : |h|^2 = h^2 := by rw [sq_abs]
    calc |iteratedDeriv 2 theta ξ| * |h|^2
        ≤ K₀ * |h|^2 := mul_le_mul_of_nonneg_right hξ_bound hpow_nn
      _ = K₀ * h^2 := by rw [h_pow_eq]
      _ = K₀ / 2 * h^2 * 2 := by ring

/-- Theta Taylor remainder at order 2, parameterized by radius `R > 0`:
    there is a uniform constant `K ≥ 0` on `[T - R, T + R]` such that for
    every `h ∈ [-R, R]`,
        `|theta(T + h) − (theta T + q T · h + qPrime T · h²/2)| ≤ K · |h|³`. -/
theorem theta_taylor_remainder_2_on (T R : ℝ) (hR : 0 < R) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ R →
      |theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2)| ≤ K * |h|^3 := by
  have hθ_C3 : ContDiff ℝ 3 theta := theta_smooth.of_le (by decide)
  have h_iter3_cont : Continuous (iteratedDeriv 3 theta) :=
    hθ_C3.continuous_iteratedDeriv 3 (by decide)
  have h_compact : IsCompact (Set.Icc (T - R) (T + R)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - R) (T + R)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 3 theta y|)
      (Set.Icc (T - R) (T + R)) :=
    (continuous_abs.comp h_iter3_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 3 theta ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 6, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have hθ_C3_on : ContDiffOn ℝ 3 theta (Set.uIcc T (T + h)) := hθ_C3.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne hθ_C3_on
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    have h_taylor_form : taylorWithinEval theta 2 (Set.uIcc T (T + h)) T (T + h) =
        theta T + q T * h + qPrime T * h^2 / 2 := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 theta (Set.uIcc T (T + h)) T = theta T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 theta (Set.uIcc T (T + h)) T = q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C3.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      have h_iter2 : iteratedDerivWithin 2 theta (Set.uIcc T (T + h)) T = qPrime T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C3.contDiffAt.of_le (by decide)) hT_mem]
        rw [show (2 : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one]
        rfl
      rw [h_iter0, h_iter1, h_iter2]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have hξ_in_Icc : ξ ∈ Set.Icc (T - R) (T + R) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - R) (T + R) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -R ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ R := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have hξ_bound : |iteratedDeriv 3 theta ξ| ≤ K₀ := hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : theta (T + h) - (theta T + q T * h + qPrime T * h^2 / 2) =
        iteratedDeriv 3 theta ξ * h^3 / 6 := by
      have h_fact : ((2 + 1).factorial : ℝ) = 6 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_6 : |(6 : ℝ)| = 6 := by norm_num
    rw [h_abs_6, div_le_iff₀ (by norm_num : (0:ℝ) < 6)]
    have hpow_nn : 0 ≤ |h|^3 := pow_nonneg (abs_nonneg _) 3
    calc |iteratedDeriv 3 theta ξ| * |h|^3
        ≤ K₀ * |h|^3 := mul_le_mul_of_nonneg_right hξ_bound hpow_nn
      _ = K₀ / 6 * |h|^3 * 6 := by ring

/-- Theta Taylor remainder at order 1: there is a uniform constant `K ≥ 0`
    on `[T - 1, T + 1]` such that for every `h ∈ [-1, 1]`,
        `|theta(T + h) − (theta T + q T · h)| ≤ K · h²`.

    Proof: use `theta_smooth ⊃ ContDiff 2`, apply Lagrange remainder
    with `n = 1`, and bound `|iteratedDeriv 2 theta|` on `[T - 1, T + 1]`. -/
theorem theta_taylor_remainder_1 (T : ℝ) :
    ∃ K : ℝ, 0 ≤ K ∧ ∀ h : ℝ, |h| ≤ 1 →
      |theta (T + h) - (theta T + q T * h)| ≤ K * h^2 := by
  have hθ_C2 : ContDiff ℝ 2 theta := theta_smooth.of_le (by decide)
  have h_iter2_cont : Continuous (iteratedDeriv 2 theta) :=
    hθ_C2.continuous_iteratedDeriv 2 (by decide)
  have h_compact : IsCompact (Set.Icc (T - 1) (T + 1)) := isCompact_Icc
  have h_nonempty : (Set.Icc (T - 1) (T + 1)).Nonempty :=
    ⟨T, by constructor <;> linarith⟩
  have h_cont_on : ContinuousOn (fun y => |iteratedDeriv 2 theta y|)
      (Set.Icc (T - 1) (T + 1)) :=
    (continuous_abs.comp h_iter2_cont).continuousOn
  obtain ⟨ymax, hymax_mem, hymax⟩ :=
    h_compact.exists_isMaxOn h_nonempty h_cont_on
  set K₀ : ℝ := |iteratedDeriv 2 theta ymax| with hK₀_def
  have hK₀_nn : 0 ≤ K₀ := abs_nonneg _
  refine ⟨K₀ / 2, by positivity, ?_⟩
  intro h hh
  by_cases hh_zero : h = 0
  · subst hh_zero; simp
  · have h_ne : T ≠ T + h := fun e => hh_zero (by linarith)
    have hθ_C2_on : ContDiffOn ℝ 2 theta (Set.uIcc T (T + h)) := hθ_C2.contDiffOn
    obtain ⟨ξ, hξ_mem, hξ_eq⟩ :=
      taylor_mean_remainder_lagrange_iteratedDeriv h_ne hθ_C2_on
    have h_min_lt_max : min T (T + h) < max T (T + h) := by
      rcases lt_or_gt_of_ne hh_zero with hlt | hgt
      · have h1 : T + h < T := by linarith
        rw [min_eq_right h1.le, max_eq_left h1.le]; exact h1
      · have h1 : T < T + h := by linarith
        rw [min_eq_left h1.le, max_eq_right h1.le]; exact h1
    have h_unique : UniqueDiffOn ℝ (Set.uIcc T (T + h)) :=
      uniqueDiffOn_Icc h_min_lt_max
    have h_taylor_form : taylorWithinEval theta 1 (Set.uIcc T (T + h)) T (T + h) =
        theta T + q T * h := by
      rw [taylor_within_apply]
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
                 add_sub_cancel_left, smul_eq_mul]
      have hT_mem : T ∈ Set.uIcc T (T + h) := Set.left_mem_uIcc
      have h_iter0 : iteratedDerivWithin 0 theta (Set.uIcc T (T + h)) T = theta T := by
        simp [iteratedDerivWithin_zero]
      have h_iter1 : iteratedDerivWithin 1 theta (Set.uIcc T (T + h)) T = q T := by
        rw [iteratedDerivWithin_eq_iteratedDeriv h_unique
            (hθ_C2.contDiffAt.of_le (by decide)) hT_mem,
            iteratedDeriv_one]
        rfl
      rw [h_iter0, h_iter1]
      simp [Nat.factorial]
      ring
    rw [h_taylor_form] at hξ_eq
    have hξ_in_Icc : ξ ∈ Set.Icc (T - 1) (T + 1) := by
      have h_uIoo_subset : Set.uIoo T (T + h) ⊆ Set.Icc (T - 1) (T + 1) := by
        intro y hy
        rcases lt_or_gt_of_ne hh_zero with hlt | hgt
        · have hh' : T + h < T := by linarith
          rw [Set.uIoo, min_eq_right hh'.le, max_eq_left hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_lo : -1 ≤ h := by rcases abs_le.mp hh with ⟨h1, _⟩; exact h1
          constructor <;> linarith
        · have hh' : T < T + h := by linarith
          rw [Set.uIoo, min_eq_left hh'.le, max_eq_right hh'.le] at hy
          obtain ⟨hy1, hy2⟩ := hy
          have hh_hi : h ≤ 1 := by rcases abs_le.mp hh with ⟨_, h2⟩; exact h2
          constructor <;> linarith
      exact h_uIoo_subset hξ_mem
    have hξ_bound : |iteratedDeriv 2 theta ξ| ≤ K₀ := hymax hξ_in_Icc
    have h_h_eq : (T + h) - T = h := by ring
    rw [h_h_eq] at hξ_eq
    have h_eq : theta (T + h) - (theta T + q T * h) =
        iteratedDeriv 2 theta ξ * h^2 / 2 := by
      have h_fact : ((1 + 1).factorial : ℝ) = 2 := by simp [Nat.factorial]
      have := hξ_eq
      rw [h_fact] at this
      exact this
    rw [h_eq, abs_div, abs_mul, abs_pow]
    have h_abs_2 : |(2 : ℝ)| = 2 := by norm_num
    rw [h_abs_2, div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    have hpow_nn : 0 ≤ |h|^2 := pow_nonneg (abs_nonneg _) 2
    have h_pow_eq : |h|^2 = h^2 := by rw [sq_abs]
    calc |iteratedDeriv 2 theta ξ| * |h|^2
        ≤ K₀ * |h|^2 := mul_le_mul_of_nonneg_right hξ_bound hpow_nn
      _ = K₀ * h^2 := by rw [h_pow_eq]
      _ = K₀ / 2 * h^2 * 2 := by ring

end RH.RiemannSiegelTheta
