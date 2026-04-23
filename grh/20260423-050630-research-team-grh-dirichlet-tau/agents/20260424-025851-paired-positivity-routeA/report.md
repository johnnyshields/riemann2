# Claim

In the manuscript, same-point positivity/nondegeneracy for whitening is not secured by denominator-side holomorphy alone. The actual local package is:

1. denominator comparability gives omitted-smooth holomorphy of the same-point and mixed blocks on the microscopic disk;
2. a separate perturbative positivity argument then keeps the corrected same-point blocks positive definite there by comparing them to a baseline jet-limit block with a spectral gap at `s=0`.

So for the paired slot theorem, the safe conclusion is:

- exact paired slot realization cannot come from source exactness alone;
- it also needs a distinct local admissibility/nondegeneracy hypothesis sufficient to define holomorphic inverse-square-root whitening;
- denominator comparability can remain only an upstream support for holomorphy/definability, not the whole same-point positivity mechanism.

Separated by proof state:

- proved in the current draft: `Prop. 1392-1458` proves positivity on the disk from three ingredients already cited there: denominator-comparability holomorphy, baseline variation, and a baseline spectral gap plus small perturbation.
- conditional: the step `lambda_min(G_{m,\pm}^{(0)}(0)) \gg Q` is used as a local spectral-gap input, so the whitening theorem is conditional on that baseline nondegeneracy package.
- missing for the paired theorem: a paired analogue proving or explicitly assuming same-point positive definiteness/nondegeneracy strong enough for holomorphic whitening, and a proof that the coefficient in the paired whitened expansion is exactly the paired source scalar.

# Status

conditional

# Evidence

The denominator-comparability proposition is purely a holomorphy statement. It bounds the microscopic denominators away from zero and concludes that the omitted-zero sums and required `t`-derivatives extend holomorphically on `|s|<\rho_0/Q`; its endpoint is holomorphy of `T_{\far}(t_\pm)` and hence of `g_{\sm}(t_\pm)`, not positivity of the same-point matrices. See `paper/proof_of_rh.tex:856-946`.

The whitening proposition states the real positivity mechanism explicitly. In `paper/proof_of_rh.tex:1418-1424`, holomorphy of the corrected blocks is attributed to Proposition `\ref{prop:denominator-comparability}` plus removable singularities. But positivity is handled separately in `paper/proof_of_rh.tex:1426-1455`: the draft combines the perturbation estimate `\sup \|R_{m,\pm}(s)\|=o(Q)`, the baseline variation bound `\sup \|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\ll \rho_0 Q`, and the baseline spectral-gap input `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` to deduce `\lambda_{\min}(G_{m,\pm}^{\corr}(s))\gg Q` on the disk. Only after that does holomorphic functional calculus produce `G_{m,\pm}^{\corr}(s)^{-1/2}`.

The block perturbation proposition confirms that the corrected same-point blocks are controlled by a small remainder around a baseline block, not by denominator holomorphy itself. It writes

`G_{m,\pm}^{\corr}(s)=G_{m,\pm}^{(0)}(s)+R_{m,\pm}(s)`

and proves `\|R_{m,\pm}(s)\|\ll S_2` under tail-curvature-type estimates. See `paper/proof_of_rh.tex:948-1133`.

The baseline variation lemma shows that positivity is transported away from `s=0` by continuity of the baseline block, again a distinct local matrix argument rather than a denominator argument. See `paper/proof_of_rh.tex:1332-1390`.

The paired-slot notes already anticipated this split only at a high level: `paired_slot_hypotheses.md` lists `microscopic holomorphy`, `positive same-point blocks`, and `well-defined inverse-square-root whitening` as separate items in the minimal local admissibility package. `denominator_theorem.md` narrows denominator comparability to carrying omitted-zero control into the microscopic disk, supplying omitted-smooth holomorphy, and supporting corrected-whitening admissibility. Those notes are consistent with the manuscript: denominator control contributes the holomorphy piece, but same-point positivity/nondegeneracy is a distinct local requirement.

For the paired slot theorem this means the manuscript interface is not `source theorem + denominator holomorphy` alone. The theorem identity

`\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`

is proved only after introducing the analytic whitening map `\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}` on the open set where the same-point blocks remain uniformly positive definite. See `paper/proof_of_rh.tex:1569-1606`. So the paired analogue needs that same local nondegeneracy input before the exact paired slot statement is even well-posed.

Honest verdict:

- proved: denominator comparability secures microscopic holomorphy;
- proved only with extra local input: same-point positivity on the disk comes from baseline spectral gap plus perturbative stability;
- missing for the paired theorem: a paired theorem or hypothesis delivering the same-point positive-definite/nondegenerate blocks needed for holomorphic whitening.

# Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946` (`Microscopic denominator comparability and omitted-smooth holomorphy`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:948-1133` (`Entry-by-entry perturbation estimate for the corrected same-point blocks`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1332-1390` (`Baseline same-point variation`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458` (`Corrected finite-s holomorphic whitening`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1621` (`corrected local deformation admits the decomposition ...`)
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-24,31-37,46-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:8-20`

# Dependencies

- The manuscript's own local package: denominator-comparability holomorphy, block perturbation, baseline variation, and the asserted baseline spectral gap at `s=0`.
- The note-level interpretation that paired exact-slot realization should inherit the manuscript interface.
- Reading `paper/proof_of_rh.tex` as the authoritative statement of what whitening actually uses.

# Strongest objection

The weakest point is the status of the baseline spectral-gap input `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`. In the focus region it is invoked but not proved, so one could object that my `distinct local hypothesis` language overstates what is theorem-level versus what is merely imported from elsewhere in the draft. But that objection reinforces, rather than weakens, the main conclusion: same-point positivity is not coming from denominator-side holomorphy alone.

# Needed for promotion

- A precise citation or proof elsewhere in the manuscript of the baseline jet-limit spectral gap at `s=0`, so the positivity package can be classified as fully proved rather than imported.
- A paired local theorem or explicit hypothesis giving the analogue of `G_{m,\pm}^{\corr}(s)\succ 0` on a microscopic disk and hence holomorphic inverse-square-root whitening.
- A paired proof that the first-order coefficient inside the whitened paired deformation is exactly the compact-interval source scalar `S_\chi^{\mathrm{pair}}(m)`, not a post-whitening surrogate.
