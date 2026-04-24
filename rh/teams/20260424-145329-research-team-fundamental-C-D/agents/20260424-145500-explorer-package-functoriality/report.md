Claim

Three structural observations redirect Bottleneck C toward a functoriality theorem for the corrected package object rather than another blow-up-regularity argument.

1. [confirmed] The correct ambient shape for C is a morphism from the corrected two-atom package to the amplitude-invariant strengthened datum, and the only nonformal missing step is compatibility of that morphism with diagonal merger.
2. [conditional on existence of an analytic corrected two-atom package germ \(\mathfrak P^{\corr}_2\) valued in a fixed ambient space] The diagonal-specialization problem is naturally a universal property: any reduced invariant built functorially from \((C,A^{\mathfrak f},\Delta)\) and homogeneous of degrees \((1,1,2)\) is forced to factor through the one-pair datum \(\widehat\Psi\) on the merged diagonal, provided the package itself respects one-amplitude collapse and coincident-atom additivity.
3. [candidate] The best route to \(\kappa\)-independence is to prove that the exceptional divisor remembers only the projective source direction \(\Theta_{m,\theta}=\cos\theta\,\mathcal D_m+\sin\theta\,\mathcal D_m'\) up to the same scaling law already built into \(\widehat\Psi\); then different collision slopes become different presentations of one merged package, not different states.

Status

heuristic

Evidence

- [confirmed] The paper already defines the one-pair strengthened datum
  \[
  \widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right)
  \]
  and proves its exact two-pair coincidence criterion. This identifies the target codomain for any corrected reduced two-atom package and shows that the third coordinate is forced to have quadratic scaling in the cubic scalar. Provenance: `rh/proof_of_rh.tex:11368-11585`.
- [confirmed] The minimal source-level lemma isolates the exact formal input needed for quadratic factorization: swap symmetry, one-amplitude collapse, and diagonal merger
  \[
  \mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h.
  \]
  So once a genuine package object exists in a fixed ambient space, divisibility by \((h_1-h_2)^2\) is formal. This means the search should focus on proving merger for the actual corrected package, not on inventing a new asymptotic expansion. Provenance: `rh/proof_of_rh.tex:11888-12040`, `12168-12189`.
- [confirmed] The weaker quotient route has the same shape: continuity plus exact diagonal collapse already excludes exact close two-point cores. Again the live obstruction is not local quadratic analysis but existence of a corrected object with a true diagonal-collapse law. Provenance: `rh/proof_of_rh.tex:12042-12166`.
- [confirmed] The collision/cancellation chart shows that close cancellation is organized by the projective source direction
  \[
  \Theta_{m,\theta}=\cos\theta\,\mathcal D_m+\sin\theta\,\mathcal D_m',\qquad \mathcal D_h=(c(h),u_5(h),v_5(h)).
  \]
  After blow-up, parity alone gives only a quadratic factorization in \(\delta\) with parameter \(\kappa=2\omega/\delta\); it does not constrain the value on the exceptional divisor. So the free term \(B(m,\kappa)\) can only be removed by a theorem identifying different \(\kappa\)-approaches as the same merged package state after reduction. Provenance: `rh/proof_of_rh.tex:12385-12511`; prior-cycle reports `.../20260424-143000-C-proof-obligations/report.md`, `.../20260424-145000-Bmkappa-killer/report.md`.
- [confirmed] The draft explicitly states that the honest remaining order-7 burden is package-level and provenance-sensitive: same reduced image germ or collision-functoriality, not another local pointwise field. This aligns C with a categorical/functorial statement rather than with more source-detector algebra. Provenance: `rh/proof_of_rh.tex:12513-12559`, `21277-21329`.
- [conditional on existence of an analytic corrected two-atom package germ in the triple codomain \(\mathbf C\times\mathfrak f\times\mathbf C\)] The prior-cycle package-object report gives the natural reduced map
  \[
  \mathcal R(C,UI+VS,\Delta)=\left(\frac{U}{C},\frac{V}{C},\frac{\Delta}{C^2}\right).
  \]
  Under this reduction, diagonal merger would automatically identify the merged diagonal with \(\widehat\Psi(m)\). So C is best viewed as proving that the corrected two-atom package is a functorial lift of the already-canonical one-pair package. Provenance: prior-cycle report `.../20260424-145000-corrected-package-object/report.md`; compatible with `rh/proof_of_rh.tex:11368-11450`.
- [candidate] Because the blow-up edge datum uses only \(\mathcal D_m\) and \(\mathcal D_m'\), while the target reduction kills overall scaling exactly as in Lemma `scaling-law-strengthened-package`, there may be a reformulation of C in which the exceptional divisor is a map from projectivized first-order collision data to the same amplitude-invariant moduli point \(\widehat\Psi(m)\). In that reformulation, \(\kappa\)-independence would be a consequence of projective descent rather than a separate analytic miracle.
- [candidate] The repeated failure of naive source-summed whitened coefficients is informative: since that package is even in the source weight, the true corrected package for C probably cannot live at the raw whitened-coefficient level. It likely has to be defined after a provenance-sensitive renormalization or transport step that restores one-amplitude linearity before reduction. Provenance: `rh/proof_of_rh.tex:12192-12228`.

Exact refs

- `rh/proof_of_rh.tex:11368-11450` — definition and scaling law for \(\widehat\Psi\).
- `rh/proof_of_rh.tex:11476-11585` — exact strengthened two-pair coincidence through order \(7\).
- `rh/proof_of_rh.tex:11888-12040` — formal source-level quadratic factorization from swap symmetry, one-amplitude collapse, diagonal merger.
- `rh/proof_of_rh.tex:12042-12166` — weaker quotient-diagonal collapse route.
- `rh/proof_of_rh.tex:12168-12228` — exact remaining source-level input and no-go for naive source-summed whitened package.
- `rh/proof_of_rh.tex:12385-12511` — collision/cancellation chart and parity/projective factorization.
- `rh/proof_of_rh.tex:12513-12559` — package-level coincidence/functoriality isolated as a remaining front.
- `rh/proof_of_rh.tex:21277-21329` — current burden is package-level / provenance-sensitive, not another pointwise field.
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-143000-C-proof-obligations/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-Bmkappa-killer/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md`

Dependencies

- A precise analytic corrected two-atom package object \(\mathfrak P^{\corr}_2\) in a fixed codomain, preferably the triple \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\).
- Verification that this object satisfies swap symmetry and one-amplitude collapse.
- A theorem identifying coincident two-atom packages with the merged one-pair package before or after reduction.
- If the candidate projective-descent reformulation is pursued: a statement that the exceptional divisor depends only on projective first-order collision data and is compatible with the scaling law of \(\widehat\Psi\).

Strongest objection

The report identifies a structural reformulation, not a proof. In particular, it does not show that the actual corrected two-atom package admits the required fixed-codomain functorial lift, nor that projectivized first-order collision data is sufficient to determine the exceptional-divisor state. The hidden-state dependence could survive beyond the \((c,u_5,v_5)\)-directional data and invalidate the proposed descent picture.

Needed for promotion

- State \(\mathfrak P^{\corr}_2\) explicitly as an analytic corrected two-atom package in a fixed ambient codomain.
- Prove swap symmetry and one-amplitude collapse for that object.
- Prove a merger theorem: coincident atoms map to the merged one-pair package.
- Or, prove the candidate replacement: the exceptional divisor factors through projectivized first-order collision data and then through the homogeneous reduction \(\mathcal R\), forcing the value \(\widehat\Psi(m)\).
- Adversarially check that no hidden-state coordinate survives this reduction.

Honest verdict: the paper already says the obstruction is package-level, but the sharper redirection is this: C should be attacked as a functoriality / descent theorem for the corrected package object. Blow-up analyticity and parity only get to an exceptional-divisor state; they do not identify it. The plausible structural target is that the corrected package descends from collision data to the same amplitude-invariant moduli point \(\widehat\Psi(m)\), making \(\kappa\) a presentation parameter rather than a genuine extra state.