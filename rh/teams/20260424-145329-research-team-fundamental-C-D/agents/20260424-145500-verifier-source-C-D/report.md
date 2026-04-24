Claim

Source-audit map for Bottlenecks C and D: the exact paper loci, internal dependencies, and the citation / definition assumptions most likely to fail when research reports claim closure.

Status

open

Evidence

## Must-fix before any promotion

- **C is not yet a sourced theorem; it is only a theorem target.** The paper does not currently contain a proved statement of
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
  \]
  The source-audit burden is therefore internal: any report claiming C must cite a new theorem, not only the existing blow-up regularity / parity passages. The present text around the collision chart only yields defect factorization and the statement that package-level coincidence / collision-functoriality remains open.
- **D likewise has no proved package-to-transform theorem in the current draft.** The draft already defines the visible scalar side \(H_m\), the extractor \(\Xi^{(N)}_{\zeta,\le H}\), and the fixed-sector basis containing the \(S\)-direction seen by \(\Phi_K\), but it does not prove that equal corrected reduced-package fibers force odd corrected-block differences into
  \[
  \ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K
  \]
  through the first surviving odd order. Any report that claims D from the existing text alone is overstating what the paper proves.

## Should-fix / vulnerable assumptions to audit in incoming reports

- **C depends on three distinct obligations that should not be conflated:**
  1. well-posed analytic extension of the corrected reduced two-atom package to the exceptional divisor \(\delta=0\) after \(2\omega=\kappa\delta\);
  2. \(\kappa\)-independence / diagonal-collapse of that exceptional-divisor trace;
  3. identification of the common diagonal value with the one-pair datum \(\widehat\Psi(m)\).
  A report that proves only (1) has not closed C.
- **The strongest current paper support for C is negative/scoping, not positive closure.** The draft explicitly says the honest remaining order-7 burden is package-level coincidence / collision-functoriality rather than more raw septic algebra or another pointwise field. That is useful provenance for non-goals, but not evidence of closure.
- **D must be audited at transform level, not raw-septic level.** The fixed-sector package gives canonical \(A_5^{\mathfrak f}\) and gauge-sensitive septic representatives, while \(\Delta_7\) is gauge-invariant. So reports that assert literal equality of raw order-7 data are suspect unless they also prove a gauge choice is canonical. The source-audit target should instead be constancy modulo \(\ker\Phi_K\), equivalently constancy of the first nonzero odd \(\Xi^{(N)}_{\zeta,\le H}\).
- **Definitions are spread across distant sections.** A valid D argument must tie together: \(\Phi_K\) and the visible direction; the odd expansion of \(H_m\); the finite-core localization of the first surviving odd coefficient; the fixed-sector basis / gauge law; and the later package-level queue remarks. Missing any one of these usually means a hidden definitional gap.
- **There is line-drift risk in prior summaries.** The current file places `rem:wip-explicit-pointwise-bridge-good-patch-detector` at line 21278 and `rem:wip-final-endgame-status` at line 26370, not 21277 / 26369. Use the actual label lines from the draft when citing.

## Nit

- The phrase "corrected reduced-package fiber" is now standard in cycle reports, but I do not yet see a single canonical theorem-statement definition of that exact phrase in the draft. Incoming reports should define the fiber they use, not assume the phrase is already formalized.
- For C, reports should distinguish the corrected two-atom package object itself from its reduced image; some prior notes slide between these.

Exact refs

- `rh/proof_of_rh.tex:406-423` — definition of \(\Phi_K\) and visible direction.
- `rh/proof_of_rh.tex:2214-2307` — definition / odd expansion of \(H_m\).
- `rh/proof_of_rh.tex:2953-2969` — first surviving odd coefficient localized to finite cores.
- `rh/proof_of_rh.tex:3984-4190` — exact surviving expansion and \(\Xi^{(N)}_{\zeta,\le H}\) extraction machinery.
- `rh/proof_of_rh.tex:6988-7190` — fixed-sector basis, \(A_5^{\mathfrak f}\), \(A_7^{\mathfrak f}\), \(\Delta_7\), and septic gauge law.
- `rh/proof_of_rh.tex:10780-10809` — honest remaining order-7 target is same reduced image germ / collision-functoriality, not raw septic equality.
- `rh/proof_of_rh.tex:11368-11585` — one-pair strengthened package and exact two-pair coincidence target \(\widehat\Psi\).
- `rh/proof_of_rh.tex:12139-12189` — weaker exact route (continuity + diagonal collapse) versus stronger source-level diagonal-merger route.
- `rh/proof_of_rh.tex:12385-12610` — collision/cancellation chart, blow-up variables, and package-level coincidence queue.
- `rh/proof_of_rh.tex:21277-21329` — explicit pointwise bridge remark: remaining burden is package-level / provenance-sensitive, not another pointwise field.
- `rh/proof_of_rh.tex:23123-23155` — `I,D,S,K` basis used for coefficient extraction.
- `rh/proof_of_rh.tex:26370-26398` — finite-core branch must use the first nonzero odd jet; current endgame still pair-like.
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-143000-C-proof-obligations/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-Bmkappa-killer/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-kerphik-hidden-state/report.md`

Dependencies

- For C: a canonical corrected two-atom package object on the collision/cancellation chart; analytic extension to \(\delta=0\); a diagonal-merger / collision-functoriality theorem; identification of the diagonal value with \(\widehat\Psi\).
- For D: Bottleneck C in a precise fiber form; a canonical notion of corrected reduced-package fiber; the existing \(H_m\) / \(\Xi^{(N)}_{\zeta,\le H}\) extractor stack; and a theorem that same fibers force odd corrected-block differences into \(\ker\Phi_K\) through the first surviving odd order.

Strongest objection

The present map is mostly an internal source audit because C and D are not yet backed by external bibliography claims; they are theorem obligations inside the draft. So the key risk is not mis-citing outside literature, but promoting a heuristic package theorem as if the existing internal line stack already proved it.

Needed for promotion

- For any claimed closure of C: cite a new precise theorem establishing all three parts (extension, \(\kappa\)-independence, identification with \(\widehat\Psi\)).
- For any claimed closure of D: cite a new precise theorem phrased modulo \(\ker\Phi_K\) or equivalently in terms of constancy of the first nonzero \(\Xi^{(N)}_{\zeta,\le H}\) on corrected reduced-package fibers.
- In both cases: define the package / fiber objects used, and do not rely on queue remarks as if they were proved lemmas.

Honest verdict:

The source-audit posture for this cycle is clear: C and D are not currently supported by proved paper theorems, only by a sharp internal dependency stack and accurate theorem targets. When the research reports land, I should audit them against this map and reject any closure claim that uses blow-up regularity, pointwise same-tower facts, or raw septic algebra as a substitute for the missing package-level theorems.