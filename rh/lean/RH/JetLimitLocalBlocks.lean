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

open Real RH.LocalKernelJetNormalization

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

    Real symmetric 2×2 Sylvester: a positive-definite real symmetric
    `[[a, b], [b, d]]` is characterized by `a > 0 ∧ a d - b² > 0`.  The
    forward direction uses `J 0 0 = 2 q / π` (so `e₁ᵀ J e₁ > 0` forces
    `q > 0`) and the determinant identity from `J_det`.  The reverse
    direction completes the square. -/
theorem algebraic_gram_criterion (T : ℝ) :
    (J T).PosDef ↔ 0 < q T ∧ 0 < D_J T := by
  sorry

/-- Same-point Gram positivity: at sufficiently large `T`, `J(T) ≻ 0`,
    with eigenvalue lower bound `λ_min(J(T)) ≥ (2 q(T) / π) (1 + o(1))`.

    Combines `algebraic_gram_criterion` with the Riemann–Siegel
    asymptotics from §2 (`phase_derivative_lower_bound`,
    `q_prime_asymptotic`, `q_double_prime_asymptotic`). -/
theorem same_point_gram_positivity :
    ∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T → (J T).PosDef := by
  sorry

end RH.JetLimitLocalBlocks
