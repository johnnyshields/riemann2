Claim

A separate scalar-normalization law is still needed to upgrade Bottleneck C to the fixed-shear package theorem B. C, with the current normalization, only identifies the corrected two-atom package after homogeneous reduction to the amplitude-invariant datum \(\widehat\Psi\); it does not force raw diagonal vanishing of the cubic/quintic defects or raw merger of the unreduced package. So C does not by itself imply B.

Status

proved

Evidence

- The prior `bc-shared-blocker` report identified the exact algebraic gap: reduced coincidence is weaker than raw defect vanishing. At coincidence \(h_1=h_2=m\), the exact strengthened-coincidence identities show that vanishing of the first two reduced-coordinate differences only forces
  \[
  E^{(5)}=(e/c)A_5^{\mathfrak f},
  \]
  where \(e=E^{(3)}/a_1\). This allows a common scalar rescaling and does not imply
  \[
  E^{(3)}=0,\qquad E^{(5)}=0.
  \]
  Provenance: prior report `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-121500-bc-shared-blocker/report.md`, and exact identities in `rh/proof_of_rh.tex:11650-11669`.
- Bottleneck C is phrased exactly at the reduced-package level. The active target is
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
  \]
  i.e. diagonal collapse after applying the homogeneous reduction
  \[
  \mathcal R(C,UI+VS,\Delta)=\left(\frac{U}{C},\frac{V}{C},\frac{\Delta}{C^2}\right).
  \]
  This quotient kills a common scalar and therefore cannot by itself recover raw merger. Provenance: `rh/proof_of_rh.tex:11368-11450`, `12385-12559`; prior reports `.../145000-corrected-package-object/report.md`, `.../145000-Bmkappa-killer/report.md`.
- By contrast, the fixed-shear package theorem B in the current draft is explicitly stronger. On the residual exact fixed-shear corner, the package-collapse corollary assumes the natural merger law
  \[
  \mathfrak P_2(a_1,a_2;Y,Y)=(a_1+a_2)\mathfrak F(Y),
  \]
  and concludes that the interaction remainder vanishes identically:
  \[
  \mathcal I_2(t)\equiv 0.
  \]
  This is raw package collapse, not reduced coincidence modulo scalar. Provenance: `rh/proof_of_rh.tex:22472-22505`.
- The weaker fixed-shear closure proposition below that corollary still needs diagonal vanishing of the actual cubic/quintic defects at the involutive base state:
  \[
  \mathfrak e_3(\mathcal T_N(0))=\mathfrak e_5(\mathcal T_N(0))=0.
  \]
  Reduced coincidence does not supply these raw vanishing statements; it only identifies the reduced class. Provenance: `rh/proof_of_rh.tex:22409-22470`.
- The scalar-normalization lemma near lines `23170ff.` is one-pair and centered-branch specific: it proves that the extracted cubic scalar \(c(s)\) is \(\Sigma\)-invariant and hence even on the centered one-pair branch. That is precisely a scalar law fixing a raw cubic coefficient before projectivization. Nothing in Bottleneck C, as currently formulated, imports this stronger raw scalar fixing into the two-atom fixed-shear package. Provenance: `rh/proof_of_rh.tex:23123-23275`.
- Therefore the distinction is real: C lives in the projective/amplitude-invariant normalization class; B needs an extra theorem that chooses the raw scalar representative compatibly with collision/fixed-shear descent, so that diagonal coincidence upgrades to actual defect-zero / package merger.

Exact refs

- `rh/proof_of_rh.tex:11368-11450` — definition and scaling law of \(\widehat\Psi\).
- `rh/proof_of_rh.tex:11650-11669` — exact reduced-coordinate defect identities showing reduced coincidence permits scalar freedom.
- `rh/proof_of_rh.tex:12385-12559` — collision-cancellation chart and statement that the honest target is package-level coincidence/functoriality.
- `rh/proof_of_rh.tex:22409-22470` — conditional state-local defect closure on the residual exact fixed-shear corner.
- `rh/proof_of_rh.tex:22472-22505` — stronger fixed-shear package-collapse corollary requiring raw merger law.
- `rh/proof_of_rh.tex:23123-23275` — canonical scalar extraction and \(\Sigma\)-invariant scalar normalization on the one-pair branch.
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-121500-bc-shared-blocker/report.md`.
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-Bmkappa-killer/report.md`.
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md`.

Dependencies

- The current interpretation of C as reduced-package coincidence via \(\mathcal R\).
- The exact strengthened-coincidence formulas for \(\widehat\Psi\).
- The draft’s fixed-shear corollaries distinguishing defect closure from full package merger.

Strongest objection

This conclusion depends on reading C exactly as a theorem in the reduced moduli \(\widehat\Psi\). If the coordinator strengthens C upstream so that the corrected two-atom package is canonically normalized before reduction — meaning the scalar representative is already fixed in the theorem statement — then the distinction would disappear. The current cited formulation does not yet include that stronger normalization.

Needed for promotion

- Record explicitly in collation that C does not imply B at present.
- If one wants B from C, add a new scalar law: a theorem fixing the raw scalar representative of the corrected two-atom package on the fixed-shear/collision divisor, compatible with swap/involution and one-pair normalization.
- Then show that reduced coincidence with \(\widehat\Psi\) plus this scalar law forces
  \[
  E^{(3)}=0,\qquad E^{(5)}=0,
  \]
  and hence the merger law needed in the fixed-shear package corollary.

Honest verdict: the under-captured distinction is real and matters now. C by itself is a projective/reduced coincidence theorem; B is a raw package-collapse theorem on the fixed-shear corner. An additional scalar-normalization law is still needed to pass from C to B.