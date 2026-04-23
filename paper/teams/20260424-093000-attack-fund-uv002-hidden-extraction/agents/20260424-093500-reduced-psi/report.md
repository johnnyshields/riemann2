# Claim

Bottleneck C reduces to one exact package-side statement.

Let the actual corrected two-atom package admit a blown-up reduced quotient germ

\[
\widetilde{\mathfrak P}_2(m,\kappa,\delta^2)
\]

defined near coincidence in the collision/cancellation chart

\[
h_1=m+\frac{\delta}{2},\qquad h_2=m-\frac{\delta}{2},\qquad \kappa=\frac{2\omega}{\delta},
\]

with values in the cubic/quintic/septic quotient package for the actual corrected two-atom data, such that:

1. it is continuous in \((m,\kappa,\delta^2)\);
2. on \(\delta=0\), its value is independent of \(\kappa\);
3. its diagonal trace at \(\delta=0\) is the one-pair quotient germ \(F_m\).

Then the strengthened datum

\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right)
\]

has the same reduced image germ at coincidence. Equivalently, along any normalized exact bad two-point branch converging to coincidence, the limiting reduced package is forced to be the one-pair package at the collision point, hence the limiting reduced \(\widehat\Psi\)-value is unique and equals \(\widehat\Psi(m)\).

The single narrowest exact blocker is therefore:

prove that the actual corrected two-atom package has a \(\kappa\)-independent diagonal-collapse value at \(\delta=0\) in the blown-up collision/cancellation chart.

# Status

proved

# Evidence

- Proposition `Exact strengthened two-pair coincidence through order 7` already proves that exact cubic/quintic/septic package coincidence implies equality of the full reduced invariant `\widehat\Psi(h_1)=\widehat\Psi(h_2)`.
- Proposition `Conditional exact two-point exclusion from quotient diagonal collapse` shows the same structural pattern at quotient-germ level: continuity plus diagonal collapse is enough to force coincidence behavior at collision.
- The collision/cancellation blow-up remark isolates the correct local chart and shows that the first meaningful package information should be organized in \((m,\kappa,\delta^2)\), with parity killing linear terms.
- Combining these, Bottleneck C is not blocked by another algebraic identity inside `\widehat\Psi`; it is blocked by the missing package theorem that the actual corrected two-atom quotient package descends continuously to coincidence with a diagonal value independent of the cancellation slope `\kappa`.
- The naive source-summed whitened package cannot supply this by itself, because its finite-order coefficients are even analytic in the source weight and therefore cannot satisfy the required one-atom linearity / coincident-atom additivity unless trivial.

# Exact refs

- `paper/proof_of_rh.tex:10780-10809` — honest order-7 target reframed as same reduced image germ / collision-functoriality.
- `paper/proof_of_rh.tex:11310-11585` — one-pair quotient germ `F_h`, definition of `\widehat\Psi`, and exact strengthened two-pair coincidence proposition.
- `paper/proof_of_rh.tex:11994-12166` — conditional exact two-point exclusion from quotient diagonal collapse.
- `paper/proof_of_rh.tex:12168-12227` — exact source-level merger criterion and the failure of the naive source-summed whitened model.
- `paper/proof_of_rh.tex:12447-12499` — blow-up collision/cancellation chart, swap-evenness, and `\delta^2` factorization shape.
- `paper/proof_of_rh.tex:12513-12610` — current three-front compression and minimal-core reformulation placing Bottleneck C at reduced `\widehat\Psi` coincidence.
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-124`.
- `paper/tasks/20260424-090000-other-uv002-fundamental/reports/coordinator-current-convergence.md:21-28,50-63`.

# Dependencies

- A well-defined actual corrected two-atom quotient package near coincidence.
- Continuity of its reduced blow-up germ in \((m,\kappa,\delta^2)\).
- Exact diagonal collapse to the one-pair quotient germ `F_m`.
- Independence of that diagonal value from the cancellation slope `\kappa`.

# Strongest objection

The draft does not yet construct the reduced package object itself on the blow-up chart. So the reduction above is theorem-shaped but conditional on an object whose existence and continuity are still open. In particular, proving only swap-evenness or only quadratic defect factorization is not enough for Bottleneck C unless one also gets a diagonal value at `\delta=0` that is independent of `\kappa`.

# Needed for promotion

1. Define the actual corrected reduced two-atom quotient germ on the collision/cancellation blow-up chart.
2. Prove continuity to `\delta=0`.
3. Prove diagonal collapse `\widetilde{\mathfrak P}_2(m,\kappa,0)=F_m` and, crucially, that the left-hand side is independent of `\kappa`.
4. Invoke `paper/proof_of_rh.tex:11476-11585` to convert that package coincidence into equality of reduced `\widehat\Psi` data.

Honest verdict: Bottleneck C is sharper than “prove coincidence somehow.” The exact remaining burden is a single provenance-sensitive diagonal-collapse theorem for the actual corrected two-atom package: continuity in the blow-up chart and `\kappa`-independent value at `\delta=0`. Once that is in hand, the reduced `\widehat\Psi` coincidence statement is formal from the existing strengthened coincidence algebra.
