Claim

The smallest precise theorem-ready corrected two-atom package object that the current notation supports is the canonical order-\(3,5,7\) fixed-sector triple
\[
\mathfrak P^{\corr}_2(m,\omega,\delta)
:=
\bigl(C^{\corr}(m,\omega,\delta),\ A^{\mathfrak f,\corr}(m,\omega,\delta),\ \Delta^{\corr}(m,\omega,\delta)\bigr)
\in \mathbf C\times \mathfrak f\times \mathbf C,
\]
with
\[
A^{\mathfrak f,\corr}=U^{\corr}I+V^{\corr}S.
\]
This is smaller and cleaner than a package with a raw septic representative, and more theorem-ready than a package whose third component lives in a moving quotient space. The canonical reduction map is then
\[
\mathcal R(C,U I+V S,\Delta):=\left(\frac{U}{C},\frac{V}{C},\frac{\Delta}{C^2}\right),
\qquad C\neq 0,
\]
so the corrected reduced package is exactly
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}:=\mathcal R\circ \mathfrak P^{\corr}_2.
\]
In collision/blow-up variables \(2\omega=\kappa\delta\), Bottleneck C is then the single diagonal-specialization theorem
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

Status

heuristic

Evidence

The one-pair canonical package already exists at exactly this level: cubic scalar \(c\), quintic fixed-sector vector \(A_5^{\mathfrak f}=u_5I+v_5S\), and canonical septic determinant \(\Delta_7\). The draft also records that the raw septic representative \((u_7,v_7)\) is not canonical, while the determinant / quotient-level order-\(7\) content is. So for theorem C the right unreduced two-atom object should keep only the canonically meaningful order-\(7\) scalar and not carry an unnecessary raw septic gauge.

Using a quotient-class third component is also avoidable here. A package of the form \((C,A^{\mathfrak f},[B])\) lands in a moving quotient \(\mathfrak f/\mathbf C A^{\mathfrak f}\), which is awkward for an analytic theorem statement on the collision chart. The determinant scalar \(\Delta=\det(B,A^{\mathfrak f})\) is gauge-invariant and lands in a fixed ambient space, and after division by \(C^2\) reproduces the already-established one-pair reduced coordinate \(\Delta_7/c^2\). So the current notation supports a theorem-ready object only after this compression to \(\mathbf C\times \mathfrak f\times \mathbf C\).

This is also exactly the amount of data needed for C and no more. The target diagonal value \(\widehat\Psi(m)=(u_5/c,v_5/c,\Delta_7/c^2)\) already lives in these three reduced coordinates. Extra data such as \(T=v_7/c\) belongs to the hidden-state enlargement on D, not to the definition side of C.

Exact refs

- `paper/proof_of_rh.tex:7004-7062` for the canonical one-pair order-\(3,5,7\) package and the non-canonicity of raw septic representatives.
- `paper/proof_of_rh.tex:7976-8001` for the order-\(7\) quotient-level closure and the remaining raw septic gauge freedom.
- `paper/proof_of_rh.tex:11331-11382` for the strengthened one-pair package and the reduced datum `\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)`.
- `paper/proof_of_rh.tex:11459-11585` for the exact two-pair coincidence theorem whose conclusion is equality of `\widehat\Psi`.
- `paper/proof_of_rh.tex:12385-12445` for the collision/cancellation chart `(m,\omega,\delta)` and blow-up motivation.
- `paper/proof_of_rh.tex:12552-12610` for the package-level coincidence target and the statement that the finite-core object should be `\widehat\Psi` rather than only the affine curve `\Gamma`.
- `paper/proof_of_rh.tex:24985-25030` for the current queue split and the package-level coincidence front.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:72-77` for the current decomposition of C as `\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P^{\corr}_2` plus diagonal specialization.

Dependencies

This definition depends on having an actual corrected two-atom order-\(3,5,7\) package extracted canonically on the punctured collision chart, with swap compatibility and analytic extension after writing \(2\omega=\kappa\delta\). It also depends on the order-\(7\) two-atom component admitting the same determinant-type canonicalization as on the one-pair side.

Strongest objection

The current draft does not yet construct the actual corrected two-atom order-\(7\) package canonically enough to justify the notation \(\mathfrak P^{\corr}_2\) as an existing analytic object. So the claim here is about the smallest theorem-ready codomain and normalization the present notation can support, not about a proved construction already in the paper.

Needed for promotion

Introduce `\mathfrak P^{\corr}_2` explicitly as the corrected two-atom fixed-sector triple
`(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})` on the collision/cancellation chart, prove that
`\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P^{\corr}_2` descends analytically to `(m,\kappa,\delta^2)`, and then state theorem C exactly as
`\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`.

Honest verdict:

The smallest precise `\mathfrak P^{\corr}_2` is not a raw corrected block tuple and not a moving quotient-class package. It is the canonical fixed-ambient triple `(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`, because that is the least data from which the theorem-C object `\widetilde\Psi^{\corr}_{\mathrm{red}}` can be defined exactly and compared to `\widehat\Psi(m)` on the exceptional divisor.
