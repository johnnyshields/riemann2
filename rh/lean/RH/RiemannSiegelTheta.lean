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
import Mathlib.Analysis.Calculus.Deriv.Basic

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

    Recorded as a proof obligation; proving it requires the chain rule
    on `Complex.log ∘ Complex.Gamma` away from branch cuts and
    `Complex.digamma = logDeriv Complex.Gamma`. -/
theorem q_eq_digamma (t : ℝ) :
    q t = (1 / 2) * (Complex.digamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2)).re -
          (1 / 2) * Real.log Real.pi := by
  -- TODO: chain rule on `Complex.log ∘ Complex.Gamma` away from branch cuts;
  -- needs `Complex.differentiableAt_Gamma` + `digamma_def` + branch-cut handling.
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

    Reduces to the first asymptotic of `theta_derivative_asymptotics`
    via `t ∈ [T/2, 2T]`. -/
theorem phase_derivative_lower_bound :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T : ℝ, T₀ ≤ T → ∀ t : ℝ, T - 1 ≤ t → t ≤ T + 1 →
    q t ≥ (1/2) * Real.log (T / (4 * Real.pi)) - C / T^2 := by
  -- TODO: extract from `theta_derivative_asymptotics`.
  sorry

end RH.RiemannSiegelTheta
