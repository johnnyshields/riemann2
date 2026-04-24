## Claim

Noether's local-admissibility reduction is correct as a reduction for the
literal displayed UV-017 finite-\(s\) chart. The mixed block apparent poles are
removable with the claimed orders, including the \(s^{-3}\) entry. The
same-point positivity condition at \(s=0\) is exactly
\[
q>0,\qquad 2qq''+4q^4-3(q')^2>0,
\]
up to the positive global \(1/\pi\) factor. Holomorphic inverse-square-root
whitening follows from holomorphic same-point blocks plus a spectral gap by the
same functional-calculus mechanism used in the RH draft, and this whitening
does not introduce a hidden scalar coefficient at matrix level when
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) is defined after whitening.

This does not close UV-017. From the displayed chart alone, the determinant gap
is an explicit local hypothesis, not a consequence of the completed source
identity. Uniform microscopic radius, freeze-rule remainder for the actual
paired object, and scalar readout normalization also remain open unless
assumed.

Honest verdict: certify Noether's reduction as a stable UV-017 finding. The
next sharp target is the paired determinant/spectral-gap theorem for the actual
completed source \(q_\chi^{\mathrm{pair}}\).

## Status

proved

## Evidence

**Proved.**

- The saved exact algebra script
  `scripts/check_uv017_local_admissibility.py` verifies the mixed-block
  numerator orders. Its SHA256 is
  `E47E7D5809B297ADF83EDEA8CAE1EDE168F144C6F7871FB0565E5AAF1D239DCA`.
  Relevant output:
  `upper numerator order: 2`,
  `lower numerator interior order: 2`,
  `(2,2) numerator order: 3`.
  The same output gives the leading quotient after removing the denominators,
  including
  \[
  \frac{\text{(2,2) numerator}}{s^3}
  =
  \frac13q_0^3+\frac16q_2+O(s^2),
  \]
  so the \(s^{-3}\) apparent pole is removable.
- The same script verifies the determinant algebra for the displayed
  same-point block. Before the positive global \(1/\pi^2\) determinant factor,
  \[
  \det
  \begin{pmatrix}
  2q_0&q_1/2\\
  q_1/2&(q_2+2q_0^3)/12
  \end{pmatrix}
  =
  \frac{4q_0^4+2q_0q_2-3q_1^2}{12}.
  \]
  Therefore Sylvester's criterion gives exactly
  \(q_0>0\) and \(2q_0q_2+4q_0^4-3q_1^2>0\).
- This matches the displayed \(G\) and \(N\) formulas in
  `paper-updates.md:176-230` and the RH source formulas in
  `rh/proof_of_rh.tex:222-257`, `rh/proof_of_rh.tex:948-979`, and
  `rh/proof_of_rh.tex:1392-1457`.
- Noether's fixed-\(m\) holomorphy reduction is sound with one interpretation
  made explicit: the local holomorphic extension is \(D_\chi(t)\), not the
  real-part operator \(\Re D_\chi(t)\). On the real boundary, the staged source
  theorem identifies \(q_\chi^{\mathrm{pair}}=\Re D_\chi=D_\chi\) because
  \(D_\chi\) is real there; the holomorphic phase uses a local primitive of
  the holomorphic \(D_\chi\). See
  `notes/holomorphy_positivity_whitening_reduction.md:7-32` and
  `paper-updates.md:43-51`.
- The whitening claim matches the RH mechanism: once the same-point blocks are
  holomorphic and their spectra avoid \(0\), holomorphic functional calculus
  gives \(G_{\pm}^{-1/2}\), and the whitened block is a holomorphic product.
  See `rh/proof_of_rh.tex:1392-1457`. Matrix whitening changes the matrix
  derivative defining \(A_{\mathrm{val}}\), but not the scalar source
  coefficient.

**Conditional.**

- Fixed-\(m\) holomorphy is formal only after a local edge-zero-free
  neighborhood is chosen. A uniform disk such as \(|s|<\rho_0/Q\) over a
  family of \(m\)'s needs explicit pole-clearance and derivative-control
  hypotheses.
- The determinant condition is necessary and sufficient for the real
  \(s=0\) same-point block. Positivity on a real microscopic window or on the
  complex disk for whitening still needs a uniform spectral-gap or
  small-variation statement.
- Holomorphic inverse-square-root whitening is conditional on that spectral
  gap. It is not supplied by the source package, the formula display, or
  denominator holomorphy alone.
- If a scalar readout is applied after the matrix-level whitened block, this
  audit does not certify coefficient normalization after readout.

**Missing.**

1. A proof that the actual completed paired source
   \(q_\chi^{\mathrm{pair}}\) satisfies \(q>0\) and
   \(2qq''+4q^4-3(q')^2\ge\kappa>0\) on the needed real window, or an
   equivalent spectral-gap statement.
2. A uniform pole-clearance radius and derivative-control package if UV-017 is
   stated uniformly in \(m\).
3. A derivative-form freeze-rule remainder theorem for the actual paired
   object, not only the conditional chart theorem.
4. A scalar-readout normalization theorem if UV-017 leaves the matrix level.

## Baseline / delta

Baseline: the previous verifier lane cleared the finite-\(s\) \(G\), \(N\),
and \(\widehat\Omega\) entries, and the conditional theorem framing isolated
local admissibility as an explicit hypothesis block.

Delta: this audit independently verifies the local-admissibility algebra. The
removable-singularity and determinant formulas are no longer vague
admissibility clauses; they reduce to exact finite statements. The only live
positivity problem is proving the determinant/spectral gap for the actual
paired source, or keeping it as a local whitening hypothesis.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-164`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:176-230`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:277-306`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:308-357`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:360-374`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-83`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:133-148`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:156-188`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-holomorphy-positivity-whitening.md:1-16`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-holomorphy-positivity-whitening.md:24-92`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-holomorphy-positivity-whitening.md:94-106`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-holomorphy-positivity-whitening.md:151-174`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:7-62`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:64-101`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:103-146`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/scripts/check_uv017_local_admissibility.py`
- script SHA256:
  `E47E7D5809B297ADF83EDEA8CAE1EDE168F144C6F7871FB0565E5AAF1D239DCA`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- Literal paired finite-\(s\) chart and no-extra-correction-map guard.
- Local holomorphic extension of the paired boundary source, using \(D_\chi\)
  as the holomorphic object and \(\Re D_\chi\) only as the real-boundary scalar
  notation.
- Local holomorphic primitive \(\Theta_\chi^{\mathrm{pair}}\).
- Same-point determinant/spectral gap for \(G_{\chi,m,\pm}\).
- Holomorphic functional calculus for \(G^{-1/2}\) once spectra avoid \(0\).
- Derivative-form freeze-rule remainder and scalar-readout normalization before
  UV-017 closure.

## Strongest objection

Same-point positivity is still unsupported from the displayed chart and source
package alone. The determinant contains \(q'\) and \(q''\); a general positive
local \(q\) can make \(2qq''+4q^4-3(q')^2\) negative. Thus any promoted wording
that derives whitening from source normalization, edge-zero avoidance, or
formula shape alone would overclaim from current staged text alone.

## Needed for promotion

1. Add or retain a fixed-\(m\) holomorphy/removable-singularity lemma for the
   literal chart, explicitly using the holomorphic \(D_\chi\) extension rather
   than \(\Re D_\chi\).
2. Keep uniform radius as a separate pole-clearance/derivative-control
   hypothesis unless proved.
3. State the determinant gap exactly:
   \(q>0\) and \(2qq''+4q^4-3(q')^2\ge\kappa>0\), or an equivalent lower
   spectral bound for the same-point blocks.
4. Derive holomorphic inverse-square-root whitening from that spectral gap by
   functional calculus; do not treat whitening as source-theorem output.
5. Keep derivative-form freeze-rule remainder and scalar readout normalization
   as explicit assumptions or separate theorems.

Next sharp attack target: prove or disprove the determinant/spectral gap for
the actual completed paired source. The most focused version is to analyze
\[
\mathcal D[q]:=2qq''+4q^4-3(q')^2
\]
for the completed strip-edge zero kernel \(q_\chi^{\mathrm{pair}}\), starting
with the one-zero kernel and then testing whether completed-zero tails preserve
a positive lower bound on the microscopic window. If that fails, the determinant
gap should stay as an explicit local whitening hypothesis.

## Autoresearch next step

continue: attack \(\mathcal D[q]>0\) for the one-zero positive strip-edge
kernel, then add perturbative tail terms to see whether a spectral-gap
stability theorem is plausible for the paired completed-zero source.

verify: if a determinant-gap proof is proposed, check it against large
derivative local phases and against completed-zero tail perturbations; those
are the two obvious failure modes.

Ledger destination: `findings.md` for the stable reduction that fixed-\(m\)
holomorphy/removable singularities are formal while positivity is exactly the
determinant gap; `attempts.md` as a kept verifier pass; no `uv.md` closure.
