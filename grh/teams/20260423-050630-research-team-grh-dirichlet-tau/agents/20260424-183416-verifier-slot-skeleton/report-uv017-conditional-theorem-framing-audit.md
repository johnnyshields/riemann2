## Claim

The staged completed source package plus the verified paired finite-\(s\) chart
display can support a clean conditional UV-017 theorem statement, but not an
unconditional paired construction theorem and not a GRH/slot-realization
closure. The strongest honest statement is a matrix-level conditional local
normal-form theorem:

> Assume the completed-Hadamard paired source convention, so
> \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(m)
> =q_\chi^{\mathrm{pair}}(m)\) and
> \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(m)=0\). Assume the actual paired
> corrected local object is represented, with no additional correction map, by
> the displayed finite-\(s\) chart with phase
> \(\Theta_\chi^{\mathrm{pair}}\) and
> \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\). Assume
> microscopic holomorphy or value-parameter differentiability, same-point
> positivity/nondegeneracy, holomorphic inverse-square-root whitening, a pure
> value freeze rule for all non-value coordinates, and matrix-level definition
> of \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\). Then the matrix-level corrected
> local deformation has
> \[
> \Delta_\chi^{\mathrm{pair}}
> =
> S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(m)
> A_{\mathrm{val},\chi}^{\mathrm{pair}}
> +R_\chi^{\mathrm{pair}},
> \]
> with unit source coefficient, and the pure-value derivative of the remainder
> after subtracting the displayed linear term is zero.

That theorem is conditional but useful. From current staged text alone, it
should not be promoted as "the actual paired corrected blocks are constructed"
or as UV-017 closure. The staged chart definition needs a guard sentence or a
definition/hypothesis split to prevent "corrected" from hiding an extra map.

Honest verdict: promote only a conditional local chart theorem if every
hypothesis below is explicit. Do not promote an exact paired source-to-slot
realization theorem from the staged text alone.

## Status

open

## Evidence

**Proved from the staged source package and verifier lane.**

- The completed source theorem fixes the quotient and sign convention:
  \[
  \Phi_\chi^{\mathrm{pair}}(1/2+it)
  =e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},\qquad
  q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime},
  \qquad
  q_\chi^{\mathrm{pair}}=-\frac12\Phi'/\Phi.
  \]
  See `paper-updates.md:17-40` and
  `report-paper-updates-final-check.md:20-31`.
- In completed-Hadamard normalization, the staged source statement gives
  \(q_{\chi,\mathrm{comp}}^{\mathrm{pair}}
  =B_{\chi,\mathrm{comp}}^{\mathrm{pair}}
  +S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\) with
  \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\), distinct completed zeros, and
  analytic multiplicity. See `paper-updates.md:52-88` and
  `report-paper-updates-final-check.md:33-48`.
- The displayed paired \(G\), \(N\), and \(\widehat\Omega\) formulas are
  faithful literal substitutions of the RH finite-\(s\) formulas. The formula
  audit found no entry-level sign, endpoint, \(q_+\)/\(q_-\), \(s\)-power,
  \(1/\pi\), or whitening-order mismatch. See
  `paper-updates.md:163-229` and
  `report-uv017-finite-s-formula-audit.md:26-78`.
- In the displayed chart, the pure value path
  \(\Theta_{\chi,\alpha}^{\mathrm{pair}}
  =\Theta_{\chi,0}^{\mathrm{pair}}+\alpha(t-m)\) gives
  \(q_{\chi,\alpha}^{\mathrm{pair}}
  =q_{\chi,0}^{\mathrm{pair}}+\alpha\), freezes \(q'\) and \(q''\), changes
  the phase gap by \(-\alpha s\), and gives \(da/dS=1\) when
  \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\) and \(B\) is
  frozen. See `paper-updates.md:230-272` and
  `report-unit-coordinate-chart.md:49-71`.
- The RH template supplies the local algebraic pattern: define a pure value
  derivative, use holomorphic whitening, and write the local deformation as a
  value-channel linear term plus residual. See `rh/proof_of_rh.tex:446-469`,
  `rh/proof_of_rh.tex:1392-1457`, `rh/proof_of_rh.tex:1497-1613`, and
  `rh/proof_of_rh.tex:5665-5790`.

**Conditional hypotheses that must stay explicit.**

- Source-normalization alias: if the UV-017 text writes
  \(B_\chi^{\mathrm{pair}}\) and \(S_\chi^{\mathrm{pair}}\), it must say these
  are the completed-Hadamard quantities
  \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) and
  \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\), or else state a separate broader
  source package. Raw \(L\)-factor background terms cannot be silently mixed
  into this theorem.
- Chart-realization hypothesis: the actual paired corrected blocks must be
  represented by the displayed finite-\(s\) local chart, with no additional
  correction map. If any further correction map is present, its derivative in
  the value coordinate must be named and checked for unit coefficient.
- Local admissibility: microscopic holomorphy/removable singularities in \(s\),
  value-parameter differentiability or joint holomorphy in the local
  coordinates, same-point positivity/nondegeneracy, and holomorphic inverse
  square roots are hypotheses, not consequences of the source theorem or the
  display.
- Freeze rule: derivative, curvature, mixed-jet/phase-gap background,
  source-background, correction, multiplicity, cutoff, and normalization-gauge
  coordinates must be declared non-value directions and have zero first
  variation along the pure value path.
- Remainder criterion: \(R_\chi^{\mathrm{pair}}\) may be defined residually, but
  the theorem must also state the derivative criterion
  \[
  \left.\partial_\alpha
  \bigl(R_\chi^{\mathrm{pair}}\text{ along the pure value path}\bigr)
  \right|_{\alpha=0}=0
  \]
  after subtracting the displayed \(S A_{\mathrm{val}}\) term. Otherwise the
  identity is tautological.
- Scalar readout: if the final object is not the matrix-level
  \(\widehat\Omega_\chi^{\mathrm{pair},\mathrm{corr}}\), then
  \(A_{\mathrm{val}}\) must be defined after the readout or the readout's
  derivative on the matrix value slot must be normalized separately.

**Missing from current staged text alone.**

1. A theorem block that actually states the conditional matrix-level UV-017
   result after the chart definition.
2. A guard sentence in the chart definition: "No further correction map is
   included in this local chart; any additional correction must be named and
   checked for unit value-coordinate derivative."
3. A definition/hypothesis split: one definition for the displayed abstract
   finite-\(s\) chart, and one realization hypothesis saying the actual paired
   corrected blocks instantiate that chart.
4. An explicit \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) definition at the same
   level as \(\Delta_\chi^{\mathrm{pair}}\), preferably matrix-level unless a
   scalar readout is included.
5. The local admissibility and derivative-form freeze-rule clauses as theorem
   hypotheses, not only as a paragraph saying they remain before promotion.

No computation was run for this audit.

## Baseline / delta

Baseline: the prior verifier lane established that UV-017 reduces to a
unit-coordinate local normal-form lemma, and the finite-\(s\) formula audit
cleared the displayed matrix entries.

Delta: this audit confirms that a clean conditional theorem is now possible,
but only if the staged chart is treated as an explicit hypothesis/definition
and paired with a local admissibility theorem-hypothesis block. The remaining
problem is no longer matrix-entry correctness. It is theorem framing: preventing
the chart hypothesis from being read as actual paired construction,
holomorphy/positivity/whitening closure, freeze-rule remainder, or scalar
readout normalization.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:95-148`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:156-188`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-73`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:17-88`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-162`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:163-229`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:230-284`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:1-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:149-179`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md:3-46`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-paper-updates-final-check.md:20-64`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:1-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:63-100`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md:1-34`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-finite-s-formula-audit.md:1-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-finite-s-formula-audit.md:80-100`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:1-41`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:73-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md:1-63`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md:84-108`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- UV-016 completed-Hadamard source theorem, including the sign-audited quotient,
  real-part projection, compact zero series, edge exclusions, and raw/completed
  separation.
- Completed-source aliases for UV-017:
  \(B_\chi^{\mathrm{pair}}=B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) and
  \(S_\chi^{\mathrm{pair}}=S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\), unless a
  different source convention is explicitly declared.
- The displayed paired finite-\(s\) local chart with no unnamed correction map.
- Local admissibility: microscopic holomorphy, value-parameter
  differentiability or joint holomorphy, same-point positivity/nondegeneracy,
  and holomorphic inverse-square-root whitening.
- Exact pure value freeze rule and derivative-form remainder criterion.
- Matrix-level scope, or a separately normalized scalar readout.

## Strongest objection

The current staged text can support a conditional theorem, but only if
"corrected paired block" means exactly the displayed local chart. If the actual
paired construction later inserts any additional correction map, gauge
normalization, projection, scalar readout, or background adjustment, the unit
coefficient can be rescaled unless that map's value-coordinate derivative is
checked. This is the same UV-017 obstruction in a narrower form.

## Needed for promotion

Minimal theorem-facing statement:

```tex
\begin{theorem}[Conditional paired matrix value-slot]
Assume the completed-Hadamard paired source package on \(I\), and interpret
\(B_\chi^{\mathrm{pair}}\) and \(S_\chi^{\mathrm{pair}}\) in that completed
normalization. Fix \(m\in I\). Assume the actual paired corrected finite-\(s\)
local object is represented, with no further correction map, by the displayed
unit-coordinate chart, and assume microscopic holomorphy, value-parameter
differentiability, same-point positivity/nondegeneracy, and holomorphic
whitening for this chart. Let all non-value coordinates be frozen on the pure
value path
\(\Theta_{\chi,\alpha}^{\mathrm{pair}}
=\Theta_{\chi,0}^{\mathrm{pair}}+\alpha(t-m)\), with
\(B_\chi^{\mathrm{pair}}(m)\) frozen. Define
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) as the derivative of the post-whitened
matrix block with respect to the local value coordinate
\(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\) at the background.
Then the matrix-level corrected local deformation satisfies
\[
\Delta_\chi^{\mathrm{pair}}
=
S_\chi^{\mathrm{pair}}(m)A_{\mathrm{val},\chi}^{\mathrm{pair}}
+R_\chi^{\mathrm{pair}},
\]
and the pure-value derivative of \(R_\chi^{\mathrm{pair}}\) at the background is
zero after subtracting this displayed linear term.
\end{theorem}
```

Minimal clauses that prevent overclaim:

1. Add: "No further correction map is included in this local chart; any
   additional correction must be named and checked for unit value-coordinate
   derivative."
2. Split the staged definition into:
   `Definition (abstract paired finite-\(s\) chart)` and
   `Hypothesis (actual paired corrected blocks realize this chart)`.
3. State the completed-source alias for \(B_\chi^{\mathrm{pair}}\) and
   \(S_\chi^{\mathrm{pair}}\).
4. Promote the holomorphy/positivity/whitening clauses from "remaining
   hypotheses before promotion" into hypotheses of the conditional theorem.
5. Add the derivative-form freeze-rule remainder criterion.
6. Keep scalar readout outside the theorem, or define \(A_{\mathrm{val}}\)
   after the readout and check its derivative.

Do not promote beyond this conditional statement from current staged text
alone.

## Autoresearch next step

continue: draft and audit the exact conditional theorem block above against the
staged definition, with the definition/hypothesis split and no-extra-map guard.

verify: if any scalar readout or additional correction map is introduced, audit
its first value-coordinate derivative before allowing the coefficient claim to
leave the displayed matrix chart.

Ledger destination: `paper-updates.md` for the proposed conditional theorem
wording and guard clauses; `attempts.md` as a kept verifier framing audit; no
`uv.md` closure, since UV-017 remains open except under the listed hypotheses.
