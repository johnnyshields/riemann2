# Claim

The sharpest current theorem statement for Bottleneck C is the following corrected reduced-package diagonal-merger / collision-functoriality theorem.

Let

\[
h_1=m-\frac{\delta}{2},\qquad h_2=m+\frac{\delta}{2},\qquad 2\omega=\kappa\delta,
\]

and let

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\omega,\delta)
\]

denote the actual corrected reduced two-atom package on the punctured collision/cancellation chart. Assume this reduced package is canonically defined from the actual corrected two-atom package, is analytic after blow-up, and is swap-even, so for \(\delta\neq 0\)

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\omega,\delta)
=
\mathcal P^{\corr}_{\mathrm{red}}(m,\kappa,\delta^2)
\]

for an analytic germ \(\mathcal P^{\corr}_{\mathrm{red}}\).

Then the theorem to prove is:

\[
\boxed{
\mathcal P^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\qquad\text{for all }(m,\kappa)
}
\]

where

\[
\widehat\Psi(m)=
\left(
\frac{u_5(m)}{c(m)},
\frac{v_5(m)}{c(m)},
\frac{\Delta_7(m)}{c(m)^2}
\right)
\]

is the amplitude-invariant one-pair strengthened datum.

Equivalently, the exceptional-divisor value of the actual corrected reduced two-atom package is canonically defined, independent of \(\kappa\), and equal to the coincident-atoms one-pair reduced package. Equivalently again, the corrected two-atom package descends functorially to one reduced \(\widehat\Psi\)-germ at coincidence.

This is the final theorem-shaped form because weaker hypotheses such as blow-up analyticity, swap-evenness, quotient continuity, or weak diagonal continuity still allow a free exceptional-divisor trace

\[
B(m,\kappa):=\mathcal P^{\corr}_{\mathrm{red}}(m,\kappa,0),
\]

whereas the displayed identity kills that trace exactly.

# Status

heuristic

# Evidence

1. The draft already identifies \(\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)\) as the correct amplitude-invariant reduced one-pair datum for the downstream coincidence problem, so any diagonal specialization of the reduced two-atom package must land there, not in the affine curve \(\Gamma\).

2. The honest higher-order residual burden is repeatedly stated to be a provenance-sensitive package theorem, specifically same reduced image germ at coincidence or collision-functoriality of the corrected two-atom package.

3. In the collision/cancellation blow-up chart, analyticity plus swap-evenness explains the natural variables \((m,\kappa,\delta^2)\), but by itself does not identify the full exceptional-divisor trace; it only shows that such a trace can exist analytically.

4. The source-level template for the exact missing input is already isolated by the diagonal-merger criterion

\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h,
\]

whose reduced-package analogue is exactly the boxed theorem above.

5. Once the boxed identity holds, the slogan "same reduced image germ at coincidence" becomes a precise statement, and Bottleneck C is formal from the existing strengthened coincidence algebra.

# Exact refs

- `paper/proof_of_rh.tex:10780-10809`
- `paper/proof_of_rh.tex:11294-11307`
- `paper/proof_of_rh.tex:11368-11584`
- `paper/proof_of_rh.tex:11889-12008`
- `paper/proof_of_rh.tex:12447-12511`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:21295-21329`
- `paper/proof_of_rh.tex:21736-21763`
- `paper/proof_of_rh.tex:24522-24540`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-72`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-115`

# Dependencies

- A canonical definition of the actual corrected reduced two-atom package on the punctured collision/cancellation chart.
- Analytic blow-up extension after substituting \(2\omega=\kappa\delta\).
- Functorial reduction from the corrected two-atom package to the amplitude-invariant datum \(\widehat\Psi\).
- A genuine diagonal-merger / collision-functoriality statement for the actual corrected package, not the ruled-out naive source-summed model.

# Strongest objection

The statement is theorem-ready only if the symbol \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) is canonically fixed. If residual gauge choices remain hidden in that notation, then the value on \(\delta=0\) is not yet an invariant object, and the theorem must first specify the reduction convention before asserting equality with \(\widehat\Psi(m)\).

# Needed for promotion

1. Define \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) canonically on \(\delta\neq 0\) from the actual corrected two-atom package.
2. State explicitly that \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)\) means the analytic continuation of \(\mathcal P^{\corr}_{\mathrm{red}}(m,\kappa,\delta^2)\) to \(\delta=0\).
3. Prove the boxed diagonal specialization / collision-functoriality identity.
4. Cite the existing strengthened coincidence algebra to conclude same reduced image germ at coincidence.

Honest verdict: Bottleneck C is now reduced to one exact theorem statement and no weaker one will do. The right final form is the canonical exceptional-divisor identity

\[
\mathcal P^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]

equivalently reduced-package diagonal merger / collision-functoriality for the actual corrected two-atom package.
