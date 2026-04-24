# Claim

Denominator comparability can stay `partial` at the paired slot stage, but only in the following precise sense:

it does not belong as an independent theorem endpoint of the paired exact-slot theorem, yet some denominator/holomorphy content must already be imported into that theorem insofar as it is needed to make the corrected paired local object and its first value-channel derivative well-defined.

The strongest safe boundary sentence is:

`The paired exact-slot theorem should not advertise denominator comparability as a separate endpoint, but it must assume or prove the minimal holomorphy/positivity consequences of denominator control needed to define the corrected paired deformation, the holomorphic whitening map, and the first value-channel derivative; all quantitative denominator transport and remainder bounds remain downstream.`

Concretely, the exact paired slot identity

`\Delta_\chi^{\mathrm{pair}}(m,\sigma)=S_\chi^{\mathrm{pair}}(m)A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)+R_\chi^{\mathrm{pair}}(m,\sigma)`

can safely import only this denominator-side residue into its own hypotheses:

1. enough microscopic holomorphy of the same-point and mixed paired blocks to define the corrected paired local deformation on a microscopic disk;
2. enough same-point positivity/nondegeneracy to take holomorphic inverse square roots and form the whitening map;
3. enough local regularity to define the first-order paired value-channel derivative inside that corrected whitened object.

What it should not import into the slot theorem statement itself is the stronger quantitative package:

1. denominator comparability as a named cross-family theorem endpoint;
2. preserved transport scale after whitening;
3. quantitative post-whitening transfer estimates;
4. any smallness or dominance bound for `R_\chi^{\mathrm{pair}}`;
5. odd/transverse realization or boundary estimates.

# Status

open

# Evidence

Proved:

- The supplied slot-hypotheses note already states that the exact paired slot theorem is not well-posed from the upstairs source theorem alone and already needs `minimal local analytic admissibility`; its listed admissibility content is microscopic holomorphy, positive same-point blocks, inverse-square-root whitening, and the first-order paired value-channel derivative.
- The denominator note narrows the role of denominator comparability to three front-end functions only: carrying omitted-zero control to the microscopic disk, supplying omitted-smooth holomorphy, and supporting corrected-whitening admissibility. This directly argues against making denominator comparability itself the slot theorem endpoint.
- The corrected-whitening transport note likewise packages denominator comparability only as the first ingredient in a partial intermediate bundle, explicitly separating it from value-channel slot realization and from boundary/remainder conclusions.
- In the manuscript, the exact coefficient identity is proved only after defining the corrected whitened local block through the analytic whitening map `\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}`; the proof of the decomposition `\Delta_\zeta=S(m)A_{\val}+R_\zeta` explicitly invokes holomorphy of this map on the region where the same-point blocks remain uniformly positive definite.
- The manuscript's corrected-whitening theorem depends on denominator comparability only through holomorphy of the omitted smooth part and its required derivatives. The proposition then adds positivity of the same-point blocks to obtain holomorphic inverse square roots and hence the corrected whitened block. This is exactly the `minimal imported residue` described above.
- The paired-slot-realization note places denominator/whitening control, remainder dominance, odd/transverse realization, and boundary estimates strictly downstream of the exact local-slot identification theorem target.

Conditional on [a faithful paired analogue of the manuscript local package]:

- The paired exact-slot theorem can likely keep denominator comparability itself out of the headline statement if it instead states directly the consequences it needs: holomorphic same-point/mixed blocks on the microscopic disk and holomorphic whitening through positive same-point blocks.
- If a paired theorem writer prefers theorem statements whose hypotheses name their provenance, then `denominator comparability sufficient for omitted-smooth holomorphy` can appear as a hypothesis clause, but still only as a support hypothesis rather than as a co-equal theorem endpoint.
- Full corrected-whitening transport, preserved `Q^{-3}` scale, and any estimate on `R_\chi^{\mathrm{pair}}` appear unnecessary for the exact identity itself and begin only once one wants quantitative remainder control or odd scalar transport.

Missing:

- A paired-family theorem that cleanly separates `bare definability consequences of denominator control` from the stronger quantitative transport consequences used later.
- A paired local theorem proving that the same denominator-side input needed for omitted-smooth holomorphy also suffices to secure the positivity/nondegeneracy assumptions required for holomorphic whitening, rather than merely being compatible with them.
- A paired proof that the scalar multiplying the first value-channel derivative is exactly the compact-interval source scalar `S_\chi^{\mathrm{pair}}(m)`, not a renormalized paired proxy produced after additional denominator normalization.

Honest verdict: denominator comparability cannot disappear completely at the paired slot stage, because the slot identity lives inside a holomorphically whitened local object. But it can remain `partial`: only its definability consequences belong at slot level, while its quantitative transport strength should stay outside the exact slot theorem.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29,38-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-22,24-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:8-20`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:11-22,24-46`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27,49-55,66-73`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-903`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1457`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1621`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754`

# Dependencies

- An exact compact-interval paired source package with unified background bookkeeping `B_\chi^{\mathrm{pair}}` and exact scalar `S_\chi^{\mathrm{pair}}`.
- A paired local symmetric normal form matching the manuscript interface for the corrected same-point and mixed blocks.
- Minimal denominator-side holomorphy input sufficient to extend the omitted smooth part and required derivatives to the microscopic disk.
- Same-point positivity/nondegeneracy strong enough to define holomorphic inverse square roots and the paired whitening map.
- A paired first-order value-channel derivative `A_{\mathrm{val},\chi}^{\mathrm{pair}}` defined in that corrected local object.

# Strongest objection

The present boundary may still understate how much denominator input is implicitly packed into `same-point positivity/nondegeneracy`. In the manuscript, denominator comparability feeds holomorphy directly, while positivity is proved using additional baseline spectral-gap and perturbation inputs. A paired theorem might therefore be unable to treat `holomorphy residue` and `positivity residue` as equally cheap front-end imports; more of the corrected-whitening package may have to move inside the exact-slot theorem than the current notes explicitly acknowledge.

# Needed for promotion

- State a paired exact-slot theorem in manuscript-interface form with hypotheses split into `source exactness`, `local symmetric normal form`, and `minimal local admissibility`.
- Prove a paired analogue of the corrected-whitening definability theorem that isolates the minimal denominator/holomorphy content needed only for object definition.
- Separate that theorem from a later paired transport theorem carrying the preserved scale and quantitative remainder estimates.
- Verify adversarially whether positivity/nondegeneracy at the paired slot stage follows from the same minimal denominator-side package or needs genuinely additional local spectral-gap hypotheses.
