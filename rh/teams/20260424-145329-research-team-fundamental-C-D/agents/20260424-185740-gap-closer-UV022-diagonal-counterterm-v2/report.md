# Claim

The diagonal self-subtraction / polarization counterterm route does not close
UV-022 from the current paper source. It can be made into a useful reduction:
if the order-7 quotient cross-effect is source-honestly renormalized so that,
in the UV-010 collision chart, the normalized defect is analytic, swap-even in
\((\omega,\delta)\), and zero at \((\omega,\delta)=(0,0)\), then the
\(\delta^2\mathcal H_7^q\) edge form follows formally. The current draft does
not prove the source input that gives those hypotheses.

In generic analytic corrected-whitening transfers, subtracting the diagonal
self cross-effect kills the diagonal value but does not force
\(\delta^2\)-divisibility. Higher homogeneous terms \(\mathcal T_{p\ge3}\) can
leave a first-order collision term.

# Status

open

# Evidence

Three-bin separation:

- **Proved / source-supported:** the corrected-whitening transfer is analytic
  and has a homogeneous expansion
  \[
  \mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X).
  \]
  Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553`.
- **Proved / source-supported:** the finite-order source criterion gives the
  formal \(a_1a_2(h_1-h_2)^2\) factor once an actual package satisfies swap
  symmetry, exact one-amplitude collapse, and diagonal merger. Refs:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932`.
- **Proved / source-supported:** the collision chart gives the edge-law
  template: an actual defect analytic in \((m,\omega,\delta)\), swap-even under
  \((\omega,\delta)\mapsto(-\omega,-\delta)\), and zero at
  \((\omega,\delta)=(0,0)\) has the form
  \[
  E(m,\omega,\delta)=\delta^2\mathcal H(m,\kappa,\delta^2),
  \qquad
  \kappa=2\omega/\delta.
  \]
  Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12510`.
- **Conditional:** a diagonal counterterm would be enough only if it is defined
  for the actual order-7 quotient component, in the same quotient target, and
  is proved source-honest rather than imposed as a formal subtraction. The paper
  describes this as a remaining package-level theorem, not a proved result.
  Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:12139-12189`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12513-12584`, and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:23072-23109`.
- **Missing:** no inspected source line proves that the order-7 quotient output
  of the cross-effect sees only the quadratic homogeneous transfer
  \(\mathcal T_2\), or that all \(\mathcal T_{p\ge3}\) contributions are
  quotient-invisible through order 7.
- **Missing:** no inspected source line defines the source-weight-linear
  two-atom input \(X^{[1]}\) or a diagonal counterterm before quotient
  extraction. The draft explicitly says the naive source-summed whitened route
  is even in the source weight and cannot supply the required linear merger law.
  Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`.

I rebuilt the abandoned scratch idea under this owned directory and tested it
with exact polynomial algebra:

`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-gap-closer-UV022-diagonal-counterterm-v2/scripts/diagonal_counterterm_v2_harness.py`

Script SHA: `8f324a17f2e0ac5d5b22724953dc647c54a912f8`.

Relevant output:

```text
[quadratic_transfer]
one_amplitude_left_zero = True
one_amplitude_right_zero = True
swap_difference_zero = True
diagonal_value_zero = True
divisible_by_delta_squared = True
first_delta_terms = 0
first_delta_terms_after_a2_equals_minus_a1 = 0

[cubic_transfer]
one_amplitude_left_zero = True
one_amplitude_right_zero = True
swap_difference_zero = True
diagonal_value_zero = True
divisible_by_delta_squared = False
first_delta_terms_after_a2_equals_minus_a1 = 12*a1^3*d + 84*a1^3*m*d + 111*a1^3*m^2*d + 252*a1^3*m^3*d + 135*a1^3*m^4*d + 162*a1^3*m^5*d

[mixed_transfer]
one_amplitude_left_zero = True
one_amplitude_right_zero = True
swap_difference_zero = True
diagonal_value_zero = True
divisible_by_delta_squared = False
first_delta_terms_after_a2_equals_minus_a1 = 84*a1^3*d + 588*a1^3*m*d + 777*a1^3*m^2*d + 1764*a1^3*m^3*d + 945*a1^3*m^4*d + 1134*a1^3*m^5*d
```

This separates the route cleanly. The quadratic Hessian-like part behaves as
desired. Generic cubic and higher analytic transfer terms pass the superficial
tests but fail the \(\delta^2\) test, including on the leading cancellation
substitution \(a_2=-a_1\). Therefore diagonal self-subtraction is not a theorem
unless the paper supplies an additional structural reason eliminating the first
collision derivative.

# Baseline / delta

Baseline: prior UV-022 work identified \(\mathcal T_1\) as the whitening-side
linear functor and the analytic corrected-whitening cross-effect as the right
two-atom interaction package. The live obstruction was diagonal/collision
vanishing of its order-7 quotient component.

Delta: this pass rejects the bare diagonal-counterterm shortcut. It sharpens
the missing theorem to one of three precise inputs:

1. The septic quotient component of the renormalized cross-effect receives only
   the quadratic homogeneous transfer \(\mathcal T_2\).
2. The higher \(\mathcal T_{p\ge3}\) transfer contributions are
   quotient-invisible through order 7.
3. A provenance-sensitive same-reduced-image germ or collision-functoriality
   theorem kills the first collision derivative of the renormalized order-7
   quotient component in the UV-010 chart.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - UV-022 frontier and prior negative/positive captures.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-022 target.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md`
  - first UV-010/UV-022 wave synthesis.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md:326`
  - UV-022 cross-effect continuation brief.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553`
  - analytic corrected-whitening transfer and homogeneous expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932`
  - finite-order source criterion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12139-12189`
  - remaining source-level merger and quotient-diagonal inputs.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  - even-amplitude obstruction for the naive source-summed whitened model.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12510`
  - collision-cancellation chart and conditional edge-law template.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12513-12584`
  - package-level coincidence/functoriality remains conditional.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23072-23109`
  - residual fixed-shear corner still needs package-level collapse.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183418-gap-closer-UV010-actual-hessian-construction/report.md`
  - current source does not expose the actual two-atom quotient Hessian.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183713-explorer-UV010-source-weight-linearization/report.md`
  - signed source-weight lift fails exact one-amplitude collapse.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`
  - \(\mathcal T_1\) is the whitening-side linear functor, but \(X^{[1]}\) is missing.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/report.md`
  - cross-effect package has one-amplitude collapse but diagonal value need not vanish.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184812-gap-closer-UV022-diagonal-counterterm/scripts/diagonal_counterterm_harness.py`
  - abandoned scratch input only; not used as provenance.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-gap-closer-UV022-diagonal-counterterm-v2/scripts/diagonal_counterterm_v2_harness.py`
  - owned exact harness, SHA `8f324a17f2e0ac5d5b22724953dc647c54a912f8`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-185740-gap-closer-UV022-diagonal-counterterm-v2/notes/diagonal-counterterm-v2-map.md`
  - source-bin and route map.

# Dependencies

- A canonical source-weight-linear input \(X^{[1]}(h)\) for corrected blocks
  through order 7.
- A source-honest analytic cross-effect package for the actual two-atom order-7
  quotient output.
- A definition of the diagonal counterterm in the same moving or midpoint
  quotient target, before determinant scalarization.
- Good-patch quotient trivialization on \(A_5^{\mathfrak f}(m)\neq0\), or an
  explicit convention at the rank-jump locus.
- A proof that the renormalized order-7 quotient component is analytic and
  swap-even in the UV-010 chart and has no first collision derivative.

# Strongest objection

Lemma `lem:minimal-source-level-two-point-criterion` can be read as saying that
one-amplitude collapse plus diagonal merger formally implies the quadratic
factor. The counterterm does enforce diagonal value zero by definition, so one
might think this closes the route. The objection is that this would define a
new package unless the counterterm is source-honest for the actual corrected
blocks. The harness shows why this distinction matters: a generic analytic
cross-effect with diagonal self-subtraction satisfies the superficial identities
but still leaves an order-\(\delta\) term from higher homogeneous transfer
pieces. The paper currently states the merger/collision-functoriality input as
missing, not proved.

# Needed for promotion

1. Define \(X^{[1]}(h)\) for the actual corrected block triple through order 7.
2. Define the order-7 quotient component of the corrected-whitening
   cross-effect before determinant scalarization.
3. Define a diagonal counterterm in the same quotient bundle, or prove the
   diagonal component vanishes without subtraction.
4. Prove that the renormalized quotient component is analytic in
   \((m,\omega,\delta)\), swap-even, and zero at the collision point. Equivalent
   finite check: the first \(\delta\)-coefficient after the leading
   cancellation relation \(a_2=-a_1\) vanishes in the quotient.
5. Prove that \(\mathcal T_{p\ge3}\) terms are either absent from the septic
   quotient component or quotient-invisible through order 7.
6. Apply the UV-010 good-patch quotient chart and state the edge law
   \[
   \overline E_{12}^{(7;1)}
   =
   \delta^2\mathcal H_7^q(m,\kappa,\delta^2).
   \]

# Autoresearch next step

continue: attack the homogeneous-transfer filtration. For the order-7 quotient
output, determine whether only the quadratic \(\mathcal T_2\) cross term can
contribute when \(X=X^{[1]}\), or whether a concrete \(\mathcal T_3\) channel
survives. If a \(\mathcal T_3\) channel survives, UV-022 should file the first
collision derivative as the sharp missing substatement rather than continue
with diagonal counterterms.

verify: source-audit whether the paper's finite-order model through order 7
ever proves "higher corrected-whitening homogeneous terms are quotient-invisible
in the septic component." Adversarially test any positive answer by adding a
cubic transfer perturbation like the harness.

blocked: no process blocker. Mathematical blocker is the missing source theorem
that kills the first collision derivative of the renormalized order-7 quotient
cross-effect.

terminal: terminal for "diagonal self-subtraction alone proves the
\(\delta^2\) edge law." Not terminal for a stronger theorem proving quadratic
homogeneous filtration or source-level collision functoriality.

Honest verdict: the current source provides the formal templates but not the
extra structure needed by the counterterm route. The clean missing theorem is:
after constructing the actual source-weight-linear order-7 two-atom input, the
renormalized quotient cross-effect has zero first collision derivative in the
UV-010 chart, equivalently its septic quotient output is governed only by the
quadratic homogeneous transfer or by a proven same-reduced-image /
collision-functoriality law.
