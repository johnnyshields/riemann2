Claim

Assume the actual corrected reduced two-atom package on the collision/cancellation chart is represented by a germ
\[
\mathcal R(m,\omega,\delta)
\]
that is analytic in \((m,\omega,\delta)\), compatible with swap
\[
\mathcal R(m,-\omega,-\delta)=\mathcal R(m,\omega,\delta),
\]
and admits a reduced coincidence value on the diagonal. Then, after passing to
\[
\kappa=\frac{2\omega}{\delta},
\]
the reduced package has an expansion
\[
\mathcal R(m,\omega,\delta)=\mathcal R_0(m,\kappa)+\delta^2\mathcal R_1(m,\kappa,\delta^2),
\]
and the target statement “same reduced image germ at coincidence” is equivalent to the single exact condition that
\[
\mathcal R_0(m,\kappa)
\]
is independent of \(\kappa\) and equals the one-pair reduced value. In particular, Bottleneck C reduces to one narrow blocker: prove \(\kappa\)-independence of the diagonal-collapse value of the actual corrected reduced package at \(\delta=0\).

Status

proved

Evidence

The paper already isolates the collision/cancellation chart
\[
m=\frac{h_1+h_2}{2},\qquad \delta=h_2-h_1,\qquad \omega=\frac{\lambda-1}{\lambda+1}
\]
as the correct local chart for close cancelling two-point cores, with swap acting by
\[
(m,\omega,\delta)\mapsto(m,-\omega,-\delta).
\]
For any swap-even analytic germ, the Taylor expansion contains no odd total degree in \((\omega,\delta)\). Writing \(2\omega=\kappa\delta\), every even monomial \(\omega^a\delta^b\) with \(a+b\) even becomes
\[
\delta^{a+b}\Bigl(\frac{\kappa}{2}\Bigr)^a,
\]
so the germ reorganizes analytically as a function of \((m,\kappa,\delta^2)\). Therefore the only order-\(0\) datum visible at coincidence is the boundary value \(\mathcal R_0(m,\kappa)\). If that value is independent of \(\kappa\), then every approach direction in the blow-up gives the same reduced limiting package, hence the same reduced image germ at coincidence. Conversely, if different \(\kappa\) give different \(\mathcal R_0\), then the reduced image germ depends on approach direction and coincidence fails already on the diagonal boundary.

This matches the draft’s present convergence: the paper already says the honest order-7 target is not raw septic equality but same reduced image germ / collision-functoriality, and the current team collation already sharpens the live blocker to a \(\kappa\)-independent diagonal-collapse value at \(\delta=0\).

Exact refs

- `paper/proof_of_rh.tex:10794-10809`
- `paper/proof_of_rh.tex:12385-12445`
- `paper/proof_of_rh.tex:12447-12475`
- `paper/proof_of_rh.tex:12513-12559`
- `paper/proof_of_rh.tex:12586-12610`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:38-45`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-124`

Dependencies

- Existence of the actual corrected reduced two-atom package germ in the collision/cancellation chart.
- Swap compatibility/evenness of that reduced package.
- Identification of its diagonal value with the one-pair reduced package once \(\kappa\)-independence is known.

Strongest objection

The paper does not yet define the actual corrected reduced package as a proven analytic object in the collision/cancellation chart; without that object, the reduction above is only a theorem-shaped conditional reformulation, not closure of Bottleneck C itself.

Needed for promotion

1. Construct the actual corrected reduced package germ on the collision/cancellation chart.
2. Prove its swap compatibility.
3. Prove that the boundary value at \(\delta=0\) is independent of \(\kappa\).
4. Identify that common value with the one-pair reduced package; then reduced-`\widehat\Psi` coincidence is formal.

Honest verdict: I did not close Bottleneck C, but I reduced it to one exact blocker sharper than “package-level coincidence”: the only remaining local obstruction is the \(\kappa\)-dependence of the diagonal-collapse value of the actual corrected reduced package at coincidence.
