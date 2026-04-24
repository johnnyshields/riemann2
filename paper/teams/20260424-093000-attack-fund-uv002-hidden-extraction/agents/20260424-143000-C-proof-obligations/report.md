Claim

The sharp statement

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

breaks into three minimal proof obligations.

1. **Well-posed exceptional-divisor trace.** After writing \(2\omega=\kappa\delta\), the actual corrected reduced two-atom package must admit an analytic extension in \(\delta\) to \(\delta=0\). This makes
   \[
   B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)
   \]
   a genuine object rather than notation.
2. **Diagonal-collapse / \(\kappa\)-independence.** The exceptional-divisor trace must be independent of the approach slope \(\kappa\):
   \[
   B(m,\kappa)=B_0(m).
   \]
3. **Diagonal identification with the one-pair package.** That common diagonal value must equal the merged one-pair datum:
   \[
   B_0(m)=\widehat\Psi(m).
   \]

Equivalently, Bottleneck C is theorem-level once the corrected reduced package has a canonical diagonal specialization and that specialization is the one-pair package. The single obligation most likely to be the real blocker is (2): a genuine collision-functoriality / diagonal-merger theorem forcing \(\kappa\)-independence of the exceptional-divisor trace. Without it, the current hypotheses still allow an arbitrary analytic function \(B(m,\kappa)\).

Status

open

Evidence

The paper already isolates \(\widehat\Psi\) as the correct amplitude-invariant one-pair datum and proves exact two-pair coincidence through order \(7\) implies equality of \(\widehat\Psi\). The collision-chart remarks then identify the right blow-up variables \((m,\omega,\delta)\) and explain that the remaining two-point burden is package-level coincidence / collision-functoriality, not more raw septic algebra.

Within the current cycle, the collation sharpens this further: once the corrected reduced package is analytic and swap-even in the blow-up chart, Bottleneck C reduces exactly to the diagonal value on \(\delta=0\). The cycle summary records the same point in theorem form and names the free exceptional-divisor term \(B(m,\kappa)\) as the obstruction.

So the formal decomposition is:

- existence of the exceptional-divisor trace;
- collapse of that trace to a canonical diagonal value;
- identification of that value with the merged one-pair package.

Among these, the real mathematical burden is the second item. If one already had a diagonal-merger theorem for the actual corrected two-atom package, then the third item is the natural normalization target, and the first is mainly regularity/bookkeeping. By contrast, analyticity plus swap-evenness alone leave \(B(m,\kappa)\) completely free.

Exact refs

- `paper/proof_of_rh.tex:10794-10809` — honest order-7 target is not raw septic equality, but same reduced image germ / collision-functoriality.
- `paper/proof_of_rh.tex:11368-11585` — definition of \(\widehat\Psi\) and exact strengthened two-pair coincidence through order \(7\).
- `paper/proof_of_rh.tex:12385-12445` — collision/cancellation chart and blow-up variables \((m,\omega,\delta)\).
- `paper/proof_of_rh.tex:12447-12511` — analytic/swap-even blow-up factorization template for corrected defects.
- `paper/proof_of_rh.tex:12513-12559` — remaining burden split; package-level coincidence/functoriality is one of the three exact fronts.
- `paper/proof_of_rh.tex:12586-12610` — downstream target is first defect-corrected coincidence information for \(\widehat\Psi\).
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-72` — Bottleneck C sharpened to
  \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)\), with the free exceptional-divisor term explicitly identified.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:103-170` — same theorem statement and blocker `B(m,\kappa)`.

Dependencies

- A precise definition of the actual corrected reduced two-atom package in the collision/cancellation blow-up chart.
- Analytic extension to the exceptional divisor \(\delta=0\).
- A collision-functoriality / diagonal-merger statement for coincident atoms strong enough to descend after reduction.
- The established one-pair amplitude-invariant datum \(\widehat\Psi\).

Strongest objection

The notation \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) is still theorem-shaped rather than fully formalized in the paper text, so one could argue that obligation (1) and the normalization convention are themselves substantive. But the cycle collation already fixes the intended convention, and even after granting that convention the real freedom remains the arbitrary analytic trace \(B(m,\kappa)\). So definitional cleanup alone does not close C.

Needed for promotion

- State the corrected reduced two-atom package as a precise analytic germ on the blow-up chart.
- Prove a diagonal-merger / collision-functoriality theorem for coincident atoms that kills the free \(\kappa\)-dependence on the exceptional divisor.
- Show the merged diagonal package reduces exactly to the one-pair datum \(\widehat\Psi(m)\).
- Then restate Bottleneck C as the corollary
  \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)\).

Honest verdict: Bottleneck C is already reduced to one real mathematical obligation plus two formalization/identification obligations. The real blocker is not analyticity or notation; it is the missing theorem that the exceptional-divisor value is canonically forced by diagonal merger, i.e. that no free \(\kappa\)-dependent package trace survives at coincidence.
