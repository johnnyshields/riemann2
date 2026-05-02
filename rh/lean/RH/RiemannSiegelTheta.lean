/-
The Riemann–Siegel phase function and its derivatives.

Concrete definitions used throughout `RH/`.  This module isolates the
heavyweight digamma / log-Gamma infrastructure from the rest of the
formalization.

Maps to the LaTeX as follows:
  RH.RiemannSiegelTheta.theta
      ↔ θ(t) of `def:riemann-siegel-phase`
  RH.RiemannSiegelTheta.q, qPrime, qDoublePrime
      ↔ q = θ', q' = θ'', q'' = θ'''

Theorems:
  theta_derivative_asymptotics       ↔ Lemma `lem:theta-derivative-asymptotics`
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

namespace RH.RiemannSiegelTheta

open Real Complex

/-! ## Concrete definitions

`theta` is defined via the principal branch of `Complex.log ∘ Complex.Gamma`
on `1/4 + i t / 2`.  The principal branch has `2π` discontinuities; the
*continuous* Riemann–Siegel phase used in the paper differs by a piecewise
constant `2π k(t)`, but the kernel `sin(θ(x) − θ(y))` is `2π`-periodic in
each argument and thus invariant under this choice.

The first three derivatives `q`, `qPrime`, `qDoublePrime` are defined as
iterated `deriv` of `theta` to match the LaTeX usage `q = θ′`,
`q′ = θ″`, `q″ = θ‴`. -/

/-- Riemann–Siegel phase, principal branch.

    `θ(t) = Im(log Γ(1/4 + i t / 2)) − (t/2) log π`. -/
noncomputable def theta (t : ℝ) : ℝ :=
  (Complex.log (Complex.Gamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2))).im -
    (t / 2) * Real.log Real.pi

/-- First derivative of the phase, `q := θ'`. -/
noncomputable def q (t : ℝ) : ℝ := deriv theta t

/-- Second derivative of the phase, `q' := θ''`. -/
noncomputable def qPrime (t : ℝ) : ℝ := deriv (deriv theta) t

/-- Third derivative of the phase, `q'' := θ'''`. -/
noncomputable def qDoublePrime (t : ℝ) : ℝ := deriv (deriv (deriv theta)) t

/-! ## Closed-form expression for `q` via digamma

    Differentiating `t ↦ Complex.log (Complex.Gamma (1/4 + i t / 2))` gives
    `(i/2) · ψ(1/4 + i t / 2)`, where `ψ = Complex.digamma`.  Taking the
    imaginary part:
        `q(t) = (1/2) Re(ψ(1/4 + i t / 2)) − (1/2) log π`.

    The chain rule applies away from branch cuts: we require
    `Γ(1/4 + i t / 2) ∈ slitPlane`. -/

/-- The affine map `t ↦ 1/4 + i t / 2` has derivative `i/2`. -/
private lemma z_hasDerivAt (t : ℝ) :
    HasDerivAt (fun s : ℝ => (1 : ℂ) / 4 + Complex.I * (s : ℂ) / 2)
      (Complex.I / 2) t := by
  have h1 : HasDerivAt (fun s : ℝ => (s : ℂ)) (1 : ℂ) t :=
    Complex.ofRealCLM.hasDerivAt
  have h2 := h1.const_mul Complex.I
  have h3 := h2.div_const 2
  have h4 := h3.const_add ((1 : ℂ) / 4)
  convert h4 using 1
  ring

/-- For real `t`, `1/4 + i t / 2` is never a non-positive integer
    (since its real part is `1/4 > 0`). -/
private lemma z_ne_neg_nat (t : ℝ) :
    ∀ m : ℕ, ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2) ≠ -m := by
  intro m heq
  have h_re : ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2).re = ((-(m : ℂ)).re : ℝ) := by
    rw [heq]
  simp at h_re
  -- h_re : 1/4 = -↑m, contradiction since 1/4 > 0 and m ≥ 0
  have hm : (0 : ℝ) ≤ m := Nat.cast_nonneg m
  linarith

/-- `q t = (1/2) Re(digamma(1/4 + i t / 2)) − (1/2) log π`,
    provided `Γ(z(t)) ∈ slitPlane`.

    The proof chains: `z_hasDerivAt t : HasDerivAt z (i/2) t`,
    `Complex.differentiableAt_Gamma z (z_ne_neg_nat t) :
        DifferentiableAt ℂ Γ z`,
    `HasDerivAt.scomp` to get `HasDerivAt (Γ ∘ z) ((i/2) Γ'(z)) t`,
    `HasDerivAt.clog_real h_slit` to get
        `HasDerivAt (log Γ ∘ z) ((i/2) Γ'(z) / Γ(z)) t`,
    composition with `Complex.imCLM` (Im as a `ℝ-CLM`), and
    `Complex.digamma = logDeriv Γ` to identify `Γ'(z)/Γ(z) = ψ(z)`.

    TODO: bridging `.im` between `HasDerivAt` and `Complex.imCLM`-composition
    needs careful elaboration; `h.im` is not a primitive on `HasDerivAt`. -/
theorem q_eq_digamma (t : ℝ)
    (h_slit : Complex.Gamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2) ∈
              Complex.slitPlane) :
    q t = (1 / 2) * (Complex.digamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2)).re -
          (1 / 2) * Real.log Real.pi := by
  sorry

/-! ## Riemann–Siegel asymptotics

    Differentiated Stirling for `log Γ` (or, equivalently, asymptotic
    expansion of `digamma` at the half-period scale `t → ∞`).  Mathlib has
    the leading term of Stirling but not the polynomial corrections, so
    these are recorded as proof obligations. -/

/-- Differentiated theta asymptotics, uniform over a window
    `[T - 1, T + 1] ⊂ I_T`.  Combines the three derivative bounds of
    Lemma `lem:theta-derivative-asymptotics`:
    `q  = (1/2) log(t/(2π)) - 1/(48 t²) + O(t⁻⁴)`,
    `q' = 1/(2t) + O(t⁻³)`, and
    `q'' = -1/(2t²) + O(t⁻⁴)`. -/
theorem theta_derivative_asymptotics :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T → ∀ t : ℝ, T - 1 ≤ t → t ≤ T + 1 →
      |q t - ((1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2))|
        ≤ C / t^4 ∧
      |qPrime t - 1 / (2 * t)| ≤ C / t^3 ∧
      |qDoublePrime t - (-1) / (2 * t^2)| ≤ C / t^4 := by
  -- TODO: differentiate Stirling for `log Γ` to three orders.
  -- Mathlib has `Stirling.tendsto_stirlingSeq_atTop` (leading term only).
  -- The polynomial corrections `1/(12 z) − 1/(360 z³) + …` need to be derived.
  sorry

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
  -- Apply theta_derivative_asymptotics
  obtain ⟨h_q_bound, _, _⟩ := hasymp T hT_T₀' t ht_lo ht_hi
  have h_q_lo : (1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2) - C' / t^4 ≤ q t := by
    have h_abs := abs_le.mp h_q_bound
    linarith [h_abs.1]
  -- log(t/(2π)) ≥ log(T/(4π)) since t ≥ T/2.
  have h_log_mono : Real.log (T / (4 * Real.pi)) ≤ Real.log (t / (2 * Real.pi)) := by
    apply Real.log_le_log (by positivity)
    rw [div_le_div_iff₀ (by positivity : (0:ℝ) < 4 * Real.pi)
        (by positivity : (0:ℝ) < 2 * Real.pi)]
    nlinarith [Real.pi_pos]
  -- t² ≥ T²/4.
  have h_t_sq_lower : T^2 / 4 ≤ t^2 := by nlinarith
  have h_t_sq_pos : 0 < t^2 := by positivity
  have h_T_sq_pos : 0 < T^2 := by positivity
  have h_one_48 : 1 / (48 * t^2) ≤ 1 / (12 * T^2) := by
    rw [div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith
  -- t⁴ ≥ T⁴/16 ≥ T²/16 (for T ≥ 1, since T² ≤ T⁴).
  have h_T_ge_1 : (1 : ℝ) ≤ T := by linarith
  have h_t_4_lower : T^4 / 16 ≤ t^4 := by nlinarith
  have h_T_sq_ge_1 : (1 : ℝ) ≤ T^2 := by nlinarith [h_T_ge_1]
  have h_T4_ge_T2 : T^2 ≤ T^4 := by nlinarith [h_T_sq_ge_1]
  have h_Cp_t4 : C' / t^4 ≤ 16 * C' / T^2 := by
    rw [div_le_div_iff₀ (by positivity) h_T_sq_pos]
    nlinarith [hC'_nn]
  -- Combine
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

end RH.RiemannSiegelTheta
