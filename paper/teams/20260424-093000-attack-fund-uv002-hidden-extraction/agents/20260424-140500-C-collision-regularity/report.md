## Claim

If the actual corrected reduced two-atom package germ \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\omega,\delta)\) is analytic in the blow-up chart and swap-even, then Bottleneck C is still not closed. Those hypotheses imply only that the exceptional-divisor trace
\[
B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)
\]
is an analytic function of \((m,\kappa)\). The extra theorem still needed is a genuine diagonal-merger / collision-functoriality theorem, equivalently canonical diagonal specialization,
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]
so the exceptional-divisor value is \(\kappa\)-independent and equal to the one-pair reduced package.

## Status

proved

## Evidence

- The collision-cancellation chart introduces the swap action \((m,\omega,\delta)\mapsto(m,-\omega,-\delta)\), so swap-evenness only removes odd terms in the blow-up variables; it does not constrain the full \(\delta=0\) trace as a function of \(\kappa=2\omega/\delta\).
- The local regularity remark shows the model consequence of analyticity plus swap-evenness: one gets a factorization of the form \(E(m,\omega,\delta)=\delta^2\mathcal H(m,\kappa,\delta^2)\) for corrected defects after also imposing diagonal vanishing. This is a regularity statement, not a diagonal-value identification theorem for the reduced package.
- The draft’s exact two-point source criterion isolates the missing nonlinear input as diagonal merger \(\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h\). This is precisely the package theorem that fixes the coincident value, rather than merely proving smoothness/evenness near coincidence.
- The honest order-7 and later package discussion repeatedly says that what remains is a provenance-sensitive statement such as same reduced image germ at coincidence or collision-functoriality. That is exactly the theorem needed to kill the free exceptional-divisor mode \(B(m,\kappa)\).

## Exact refs

- `paper/proof_of_rh.tex:10794-10809`
- `paper/proof_of_rh.tex:11888-11932`
- `paper/proof_of_rh.tex:12168-12189`
- `paper/proof_of_rh.tex:12385-12445`
- `paper/proof_of_rh.tex:12447-12510`
- `paper/proof_of_rh.tex:12513-12559`
- `paper/proof_of_rh.tex:12562-12584`
- `paper/proof_of_rh.tex:12606-12609`
- `paper/proof_of_rh.tex:21293-21329`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-69`

## Dependencies

- The blow-up-chart definition of the collision/cancellation package near \(h_1=h_2\).
- The strengthened coincidence algebra already in the draft, which becomes formal once the diagonal specialization is fixed.
- The team convention that \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)\) denotes the analytic extension to the exceptional divisor after writing \(2\omega=\kappa\delta\).

## Strongest objection

This conclusion depends on treating the reduced package as an honest analytic germ on the blown-up chart with a well-defined exceptional-divisor value. If the actual corrected reduced package is only defined modulo further gauge choices, then one must first prove that the exceptional-divisor value is canonically defined before one can ask for equality with \(\widehat\Psi(m)\).

## Needed for promotion

1. State the corrected reduced two-atom package on the collision/cancellation blow-up chart with a canonical exceptional-divisor convention.
2. Prove diagonal merger / collision-functoriality for the actual corrected package at coincidence.
3. Deduce the exact diagonal specialization
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]
which removes the free analytic \(B(m,\kappa)\) term.
4. Then Bottleneck C is formal from the existing strengthened coincidence algebra.

Honest verdict: analyticity and swap-evenness buy only blow-up regularity. The extra theorem is not another regularity statement; it is canonical diagonal specialization, equivalently collision-functoriality / diagonal merger forcing the exceptional-divisor trace to be \(\kappa\)-independent and equal to \(\widehat\Psi(m)\).
