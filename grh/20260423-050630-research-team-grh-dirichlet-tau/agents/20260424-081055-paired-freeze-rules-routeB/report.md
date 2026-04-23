## Claim

The strongest safe theorem-facing statement is conditional: once one fixes a source-normalized common paired value slot
`q_\chi^{pair}(m)=B_\chi^{pair}(m)+\alpha` (equivalently `S_\chi^{pair}(m)=\alpha`) and freezes the non-value local data in the corrected paired whitening interface, the first-order paired value deformation is a one-scalar local algebraic perturbation. What is local is the linear first-order whitening algebra after the slots are fixed; what is not yet local is the identification of the common paired source slot, the exact freeze rules, and any claim of canonicity or source-freeness.

## Status

open

## Evidence

Proved.

- The manuscript already isolates the local algebraic content of a pure value deformation: in the single-slot model it varies the value parameter while freezing derivative and curvature data at background level, then defines the value derivative from that frozen deformation (`paper/proof_of_rh.tex:446-469`). This is the correct template for what a freeze rule means algebraically.
- Independently of source normalization, the corrected-whitening map has a first-order linearization depending only on the three first-order block variations (`paper/proof_of_rh.tex:5711-5747`), and after whitening at the coincident background this reduces to
  `\widetilde B_1=\widetilde{\dot N}_1-\frac12\widetilde{\dot G}_{-,1}-\frac12\widetilde{\dot G}_{+,1}`
  (`paper/proof_of_rh.tex:5749-5790`). This is the genuinely local algebraic part of any paired freeze rule.

Conditional on named hypotheses.

- The paired value-channel note says the theorem-facing paired deformation is still one-scalar only after the paired source slot and local whitening interface are fixed, with safest wording `common paired value slot = B_\chi^{pair}(m)+\alpha`, equivalently `S_\chi^{pair}(m)=\alpha`, and with non-value local data frozen (`.../notes/paired_value_channel.md:7-19`).
- The paired slot hypotheses note says the exact paired slot theorem is not well-posed from the upstairs source theorem alone; it needs a compact-interval paired source theorem, symmetric local normal form, corrected-whitening admissibility, microscopic holomorphy, same-point positivity/nondegeneracy, and a first-order paired value-channel derivative in that corrected local object (`.../notes/paired_slot_hypotheses.md:7-29`).
- The same note further sharpens that denominator comparability is not itself a theorem endpoint here, but that its definability residue enters through holomorphy/whitening admissibility, while same-point positivity/nondegeneracy must remain an explicit local hypothesis line rather than being hidden in generic admissibility (`.../notes/paired_slot_hypotheses.md:31-59`).

Missing.

- No cited source here proves that the common paired slot, or the exact list of frozen versus varying coordinates, is canonically determined by local algebra alone.
- No cited source here upgrades the paired statement to `purely local`, `canonical`, or `source-free`; the value-channel note explicitly warns against that (`.../notes/paired_value_channel.md:16-30`).
- No cited source here closes the downstream quantitative pieces needed to promote the paired slot identity into a final theorem package: remainder dominance, corrected-whitening transport, odd/transverse realization, and boundary estimates (`.../notes/paired_slot_hypotheses.md:61-77`).

Safe theorem-facing wording.

- `Conditional on a fixed source-normalized common paired value slot q_\chi^{pair}(m)=B_\chi^{pair}(m)+\alpha (equivalently S_\chi^{pair}(m)=\alpha), on microscopic holomorphy, and on same-point positivity/nondegeneracy sufficient for holomorphic whitening, the paired corrected local block depends to first order on the value deformation through a one-scalar frozen-data perturbation; the induced first-order term is obtained by the local whitening linearization, while the choice of paired source slot and freeze convention is part of the normalization data, not yet an intrinsic local theorem.`

This is stronger than saying merely `source plus minimal admissibility`, but still avoids the unsafe words `canonical`, `purely local`, and `source-free`.

## Exact refs

- `paper/proof_of_rh.tex:446-469`
- `paper/proof_of_rh.tex:5711-5790`
- `paper/proof_of_rh.tex:25981-25989`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:7-30`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-77`

## Dependencies

- compact-interval paired source theorem with unified `B_\chi^{pair}` and exact `S_\chi^{pair}`
- symmetric paired local normal form
- corrected paired same-point and mixed blocks
- microscopic holomorphy
- same-point positivity/nondegeneracy for holomorphic whitening
- well-defined inverse-square-root whitening
- first-order paired value-channel derivative in the corrected local object

## Strongest objection

The current record cleanly identifies the local first-order algebra only after the paired source slot and whitening interface have already been fixed. That leaves the central vulnerability: the freeze rule may still be partly an artifact of the chosen source normalization rather than an intrinsic local law. Any theorem statement that suppresses that dependence would overclaim exactly where the notes are most cautious.

## Needed for promotion

- Prove an invariant paired-slot identification theorem showing that the common paired value coordinate and the freeze convention do not depend on an unspoken source normalization choice.
- Isolate the paired analogue of the local first-order whitening formula as a stated lemma/proposition in the manuscript, not only by analogy with the unpaired value-channel calculation.
- Prove microscopic holomorphy together with explicit same-point positivity/nondegeneracy for holomorphic whitening in the paired setting.
- Derive the exact paired identity `\Delta_\chi^{pair}=S_\chi^{pair}A_{val,\chi}^{pair}+R_\chi^{pair}` under those hypotheses and then close the remainder-dominance and transport estimates needed downstream.
