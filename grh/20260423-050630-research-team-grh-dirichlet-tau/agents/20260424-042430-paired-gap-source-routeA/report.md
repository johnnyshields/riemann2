Claim

The manuscript's baseline same-point gap input is the spectral gap
\(
\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q
\)
for the baseline jet-limit same-point block at \(s=0\), used in the corrected-whitening step to transport positivity from \(s=0\) to the microscopic disk. As written, this does not look derivable from the same paired compact source package alone; it looks like a separate local same-point positivity/nondegeneracy theorem (or explicitly assumed local clause) that must accompany the source package.

Status

conditional

Evidence

Proved:

1. The actual baseline gap input used by the manuscript is the \(s=0\) spectral gap of the baseline same-point block. In Proposition `prop:corrected-whitening`, after holomorphy is obtained from denominator comparability, the positivity step runs through three ingredients: perturbation smallness, baseline variation, and an explicit baseline spectral gap at \(s=0\). The proof states
\[
\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q
\]
and then combines this with
\(
\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\ll \rho_0 Q
\)
and
\(
\|R_{m,\pm}(s)\|=o(Q)
\)
to conclude
\(
\lambda_{\min}(G_{m,\pm}^{\corr}(s))\gg Q
\)
on the disk. So the same-point gap is a direct theorem input to whitening, not a cosmetic side remark.

2. The source-style theorem-facing package in the target region is the decomposition
\(
\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)
\)
inside the corrected local object. That proposition is explicitly about decomposition via the analytic whitening map once the corrected odd holomorphic package is already available. It does not itself prove positivity of the same-point blocks; it presupposes the holomorphic-whitening stage.

3. Denominator comparability in `prop:denominator-comparability` proves microscopic holomorphy of omitted-smooth terms, not positivity. The proof establishes lower bounds for the omitted-zero denominators and then uniform convergence/holomorphy of the differentiated sums. No same-point eigenvalue lower bound is extracted there.

Conditional on existing local package:

1. The manuscript's positivity mechanism is compatible with a theorem-facing package that sits next to the paired compact source theorem, but only if that package explicitly includes a local same-point positivity/nondegeneracy clause. The note `same_point_positivity.md` matches the proof architecture in the paper: baseline spectral gap + baseline variation + perturbation smallness + holomorphic functional calculus.

2. Under that extra local clause, the paired compact source package could plausibly be presented as part of one larger theorem-facing package: source decomposition for the corrected local deformation together with a local admissibility/whitening theorem. But that is source-plus-local-whitening, not source alone.

Missing:

1. In the target manuscript region, the baseline spectral gap
\(
\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q
\)
is invoked but not proved there from the same source decomposition machinery. The proof treats it as already available for the baseline jet-limit block.

2. I do not see evidence in these target sections that the paired compact source package by itself yields the baseline same-point gap. The decomposition theorem uses the whitening map after positivity is in place, so the logical direction is opposite: the source package depends on the same-point gap to define the theorem-facing whitened object cleanly.

3. Therefore the clean theorem split appears to be: denominator comparability/microscopic holomorphy from the source-side local analytic package, and same-point positivity/nondegeneracy from a separate local spectral-gap stability theorem. The notes `paired_slot_hypotheses.md` and `same_point_positivity.md` both support exactly this split.

Exact refs

- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`): holomorphy from denominator comparability, then positivity from baseline variation + perturbation + baseline spectral gap.
- `paper/proof_of_rh.tex:1436-1455`: explicit use of
  \(
  \lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q
  \)
  to conclude uniform positivity of `G_{m,\pm}^{\corr}(s)`.
- `paper/proof_of_rh.tex:1332-1390` (`lem:baseline-variation`): transport scale
  \(
  \|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\ll \rho_0 Q
  \).
- `paper/proof_of_rh.tex:856-946` (`prop:denominator-comparability`): denominator lower bounds and holomorphy only; no positivity conclusion.
- `paper/proof_of_rh.tex:1497-1621` (`prop:corrected-local-decomposition`): source-style decomposition of the corrected local deformation after the corrected whitening package is in force.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-18,31-52,61-70`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:7-15,25-39`.

Dependencies

- `prop:denominator-comparability` for holomorphy of omitted-smooth terms.
- `lem:baseline-variation` for transport from `s=0` to `|s|<\rho_0/Q`.
- `prop:block-perturbation` and the tail-curvature theorem for the `o(Q)` remainder bound.
- An independent baseline same-point spectral-gap input at `s=0` for `G_{m,\pm}^{(0)}(0)`.
- Holomorphic functional calculus to pass from positivity to holomorphic inverse square roots.

Strongest objection

The baseline gap might be derivable elsewhere in the manuscript from the same explicit local model that underlies the source package, so in a broad editorial sense one could still bundle both statements into one theorem-facing package. But in the target regions actually requested here, that derivation is not carried by the compact source decomposition itself; the gap functions as a separate local input to whitening.

Needed for promotion

1. A standalone local theorem proving
\(
\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q
\)
for the baseline same-point block from the explicit local model, with the midpoint-class hypotheses stated cleanly.
2. A theorem-level statement clarifying package boundaries: source decomposition supplies holomorphic corrected blocks, while same-point positivity/nondegeneracy is an additional local spectral-gap stability clause needed for whitening.
3. If the authors want a single theorem-facing package, it should be phrased explicitly as source package plus local whitening admissibility, not as source package alone.
