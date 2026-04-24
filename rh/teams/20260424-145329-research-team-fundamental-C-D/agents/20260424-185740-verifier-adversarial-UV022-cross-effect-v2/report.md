# Claim

The current UV-022 diagonal-counterterm route is a useful formal reduction but
cannot be promoted from the present sources. A source-honest diagonal
subtraction may kill the literal collision value, but it does not by itself
give the required `delta^2` edge divisibility for a nonlinear analytic
corrected-whitening cross-effect. In the restricted model where diagonal
subtraction does give an edge form, the free
`a_1a_2\delta^2P(m,\kappa)` quotient term survives.

Scoped negative: current sources do not justify a diagonal counterterm that
kills the order-7 quotient cross-effect without importing diagonal merger,
same-reduced-image collapse, or an unsourced off-diagonal/free-`P` subtraction.

# Status

rejected

# Evidence

Three-bin separation:

- **Proved from sources:** `rh/proof_of_rh.tex:2415-2553` gives an analytic
  corrected-whitening transfer with homogeneous expansion. It does not define a
  source-weight-linear actual two-atom input or a canonical diagonal
  counterterm for the order-7 quotient component.
- **Proved from sources:** `rh/proof_of_rh.tex:11888-12189` gets
  `a_1a_2(h_1-h_2)^2` factorization only after the finite-order source
  identities, including diagonal merger. `rh/proof_of_rh.tex:12192-12255`
  separately warns that naive source-summed whitened blocks are even in source
  weight and cannot supply analytic one-atom linearity.
- **Proved from sources:** `rh/proof_of_rh.tex:12385-12510` gives the
  collision-cancellation chart and an edge-law template only after an actual
  analytic defect is swap-even and collision-vanishing. It does not prove the
  UV-022 quotient cross-effect has those properties.
- **Computational:** I rebuilt the abandoned scratch idea under this agent dir
  and ran
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-verifier-adversarial-UV022-cross-effect-v2/scripts/uv022_cross_effect_v2_adversarial_check.js`.
  Script hash: `8b0eadfefff750bd3adea392938a4659cf5998df`.

Relevant output:

```text
renorm_one_amplitude_left_zero = true
renorm_one_amplitude_right_zero = true
renorm_swap_difference_zero = true
raw_diagonal_zero = false
renorm_diagonal_zero = true
renorm_delta2_divisible = false
renorm_terms_below_delta2 = 28
renorm_sample_a1_2_a2_-3_m_5_d_7 = -2413681038720
source_honest_counterterm_diagonal = 0
corrected_over_a1a2delta2 = 0
corrected_edge_value = 180
free_P_survives_source_honest_counterterm = true
unsourced_full_counterterm_residual = 0
unsourced_full_counterterm_is_source_honest = false
determinant_chart_shift_difference = 0
determinant_chart_free_edge = 0
determinant_chart_free_edge_value = 180
determinant_chart_kills_free_P = false
A5_zero_rank_jump_detected = true
A5_zero_error = rank jump: zero A5 line
```

The first block is the decisive adversarial test. For a nonlinear analytic
cross-effect, subtracting the diagonal value gives one-amplitude collapse,
swap symmetry, and literal diagonal vanishing, but still leaves 28 monomials
below `delta^2`. Thus diagonal subtraction is not a substitute for a
bidegree `(1,1)` source-linearity theorem or an actual source-level merger
identity.

The second block tests the more favorable scalar quotient model. A
source-honest diagonal term kills the diagonal and leaves edge value `180`,
namely the free `P(m,\kappa)` value. The only counterterm in the harness that
kills this residual is the full off-diagonal raw term; the script marks that
counterterm as not source-honest.

The determinant block confirms the UV-010 chart behavior: representative
shifts along `A_5^{\mathfrak f}` do not change the scalar, but the scalar edge
value `180` remains. The chart also still rank-jumps at
`A_5^{\mathfrak f}=0`.

# Baseline / delta

Baseline: UV-022 had a viable package shape,
`\mathcal T(a_1X_1+a_2X_2)-\mathcal T(a_1X_1)-\mathcal T(a_2X_2)`, with exact
one-amplitude collapse and an `a_1a_2` interaction channel. The open point was
diagonal/collision vanishing of the order-7 quotient component, possibly after
a source-honest diagonal counterterm.

Delta: this pass rejects the current counterterm route as promotion-ready.
There are two independent obstructions. First, diagonal subtraction for a
nonlinear analytic cross-effect does not generally imply `delta^2`
divisibility unless the order-7 output is already bidegree `(1,1)` after
source-weight linearization. Second, even a favorable diagonal subtraction
leaves the free `P(m,\kappa)` edge unless an actual source theorem computes or
forbids it.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` -
  autoresearch rules read before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-010 and UV-022 findings.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-022 target.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md`
  - UV-022 frontier and prior UV-010 verifier synthesis.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md`
  - `UV-022 cross-effect continuation 20260424-184643`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` - analytic
  corrected-whitening transfer.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` - finite-order
  source criterion and diagonal merger input.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12255` - even-amplitude and
  determinant-route audit warnings.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12510` -
  collision-cancellation chart and edge-law template.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-182546-verifier-adversarial-UV010-first-wave/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-182546-verifier-adversarial-UV010-first-wave/scripts/uv010_first_wave_adversarial_check.js`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/scripts/cross_effect_harness.js`.
- Scratch inspected but not cited as provenance:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184643-verifier-adversarial-UV022-cross-effect/scripts/uv022_cross_effect_adversarial_check.js`.
- Own script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-verifier-adversarial-UV022-cross-effect-v2/scripts/uv022_cross_effect_v2_adversarial_check.js`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-verifier-adversarial-UV022-cross-effect-v2/notes/uv022-cross-effect-v2-audit.md`.

# Dependencies

- A canonical source-weight-linear corrected-block input `X^{[1]}(h)`.
- A theorem that the order-7 quotient output of the cross-effect is bidegree
  `(1,1)` in `(a_1,a_2)`, or an equivalent source-level merger identity.
- A fixed-target quotient convention before subtracting diagonal values.
- The good-patch assumption `A_5^{\mathfrak f}(m)\neq0`, or a separate
  prepared/projectivized convention at the rank-jump locus.
- A source computation that kills or identifies the free
  `a_1a_2\delta^2P(m,\kappa)` quotient edge.

# Strongest objection

The script is an adversarial formal harness, not the actual corrected
two-atom order-7 package. The real package may contain source-level structure
that projects the order-7 quotient cross-effect to bidegree `(1,1)` and supplies
a canonical fixed-target diagonal counterterm. Current sources do not exhibit
that structure, so the negative is scoped to the present source window and the
cross-effect/counterterm claims currently on disk.

# Needed for promotion

1. Define `X^{[1]}(h)` from corrected blocks through order 7.
2. Prove the order-7 quotient cross-effect is exactly bidegree `(1,1)` after
   source-weight linearization, or prove an equivalent finite-order
   source-level merger identity.
3. Define a source-honest diagonal counterterm in the same fixed midpoint
   quotient without using downstream diagonal merger as an assumption.
4. Prove the corrected order-7 quotient output is divisible by `delta^2` in the
   UV-010 chart.
5. Compute or forbid the free `P(m,\kappa)` edge term.
6. State the `A_5^{\mathfrak f}(m)\neq0` patch, or give the exceptional
   convention.

# Autoresearch next step

continue: split the cross-effect by homogeneous degree and source bidegree.
The next viable positive target is the bidegree `(1,1)` projection of the
order-7 quotient output, not the full nonlinear cross-effect.

verify: source-audit whether the paper already defines a bidegree `(1,1)`
projection or same-reduced-image germ for corrected blocks through order 7.

blocked: no process blocker. Mathematical blocker is absence of a
source-honest bidegree `(1,1)` / diagonal-counterterm theorem.

terminal: terminal for promoting the current unsourced diagonal-counterterm
route and for killing `P(m,\kappa)` by a counterterm that depends on the
off-diagonal/free quotient term itself. Not terminal for a future bidegree
projection or actual source-level merger theorem.

Honest verdict: UV-022 remains open. The analytic cross-effect is still the
right object to investigate, but current diagonal subtraction is not enough.
The next attack should isolate the bidegree `(1,1)` order-7 quotient component
and source-audit whether that component has a canonical collision subtraction.
