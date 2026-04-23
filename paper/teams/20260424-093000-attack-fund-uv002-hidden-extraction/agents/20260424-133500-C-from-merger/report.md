Claim

If the actual corrected two-atom package satisfies the pre-blow-up diagonal merger law

\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h,
\]

then Bottleneck C is formal as soon as the corrected reduced package has the already-assumed analytic blow-up extension to \((m,\kappa,\delta)\) and the reduction to the amplitude-invariant strengthened datum is functorial. Concretely, after writing

\[
h_1=m-\frac{\delta}{2},\qquad h_2=m+\frac{\delta}{2},\qquad 2\omega=\kappa\delta,
\]

the whole exceptional divisor \(\delta=0\) is the coincident-atom diagonal \(h_1=h_2=m\). The merger law therefore forces the raw diagonal package there to be exactly \((a_1+a_2)F_m\), hence its reduced value is

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

for every \(\kappa\). So the free exceptional-divisor trace \(B(m,\kappa)\) disappears, and the desired reduced-\(\widehat\Psi\) coincidence / same reduced image germ at coincidence follows immediately from the existing strengthened coincidence algebra.

Status

conditional on the analytic blow-up extension / reduction convention

Evidence

- Bottleneck C has already been sharpened to one exact missing statement: the diagonal exceptional-divisor value of the corrected reduced package must be \(\kappa\)-independent and equal the one-pair datum \(\widehat\Psi(m)\).
- On the pre-blow-up diagonal \(h_1=h_2=m\), the merger law identifies the two-atom package with the one-pair package \((a_1+a_2)F_m\).
- The reduced package is amplitude-invariant, so reducing \((a_1+a_2)F_m\) gives the same reduced datum as reducing \(F_m\), namely \(\widehat\Psi(m)\).
- Proposition `Exact strengthened two-pair coincidence through order 7` already shows that once the cubic/quintic/septic package identities are in place, coincidence of the reduced datum is the formal output. Here the merger law supplies the diagonal specialization needed to remove the free exceptional-divisor term.

Exact refs

- `paper/proof_of_rh.tex:10794-10809`
- `paper/proof_of_rh.tex:11476-11584`
- `paper/proof_of_rh.tex:11890-11979`
- `paper/proof_of_rh.tex:12042-12165`
- `paper/proof_of_rh.tex:12168-12189`
- `paper/proof_of_rh.tex:12447-12510`
- `paper/proof_of_rh.tex:12513-12559`
- `paper/proof_of_rh.tex:22472-22505`
- `paper/proof_of_rh.tex:22966-23109`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-62`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-115`

Dependencies

- The actual corrected two-atom package admits an analytic representation in the collision/cancellation blow-up chart.
- The reduced package map is defined by functorial passage from the corrected package to the amplitude-invariant strengthened datum \(\widehat\Psi\).
- The pre-blow-up merger law is for the actual corrected package, not the ruled-out naive source-summed model.

Strongest objection

The merger law alone is a statement on the literal diagonal \(h_1=h_2\). Bottleneck C is stated on the blown-up exceptional divisor. So one still needs the normalization/convention that the exceptional-divisor value means analytic continuation of the corrected reduced package after substituting \(2\omega=\kappa\delta\). Without that extension, the implication is not a theorem, only a slogan.

Needed for promotion

1. State the corrected reduced package \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,\delta)\) explicitly as the blow-up analytic extension of the actual corrected two-atom package.
2. Prove functoriality of reduction on the diagonal: reducing \((a_1+a_2)F_m\) gives \(\widehat\Psi(m)\).
3. Record the one-line consequence

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

and cite the existing strengthened coincidence algebra to conclude same reduced image germ at coincidence.

Honest verdict: yes, essentially immediately. The pre-blow-up diagonal merger law is exactly the missing input that kills the arbitrary exceptional-divisor term \(B(m,\kappa)\). The only residue is definitional: the draft must make the blow-up extension/reduction convention explicit so that the diagonal raw package identity can be read as the exceptional-divisor reduced identity.
