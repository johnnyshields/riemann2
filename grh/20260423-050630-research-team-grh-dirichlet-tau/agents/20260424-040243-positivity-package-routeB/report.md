# Claim

The same-point positivity package in the current manuscript is not genuinely separable from family-specific source data at theorem level.

What is transportable now is only the matrix-analytic blueprint:

- microscopic holomorphy of the corrected blocks;
- a baseline same-point spectral gap at `s=0` plus small baseline variation on `|s|<\rho_0/Q`;
- a small perturbation estimate for the corrected same-point blocks;
- holomorphic functional calculus turning positivity into holomorphic inverse-square-root whitening.

But the manuscript does not prove those inputs in a family-free way. The remaining source-specific inputs are:

1. the source-normalized baseline object `q_0`, built from the explicit local model plus affine jet `J_1[g_{\sm}]`, with its zeta-scale bounds `|q_0|\ll Q`, `|q_0'|\ll Q^2`, `|q_0''|\ll Q^3`, `|q_0'''|\ll Q^4`;
2. the baseline spectral-gap input `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` on the admissible midpoint class;
3. the source decomposition used to define the corrected object itself, namely `q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}` with `g_{\sm,R}=B_{\bg}+T_{\far,R}`;
4. the source-side value-channel normalization around `S(m)=0` and the identification of the first whitening derivative with `A_{\val}(m,\sigma)` attached to the fixed core `\mathcal C`.

So the safe verdict is:

- proved: same-point positivity is separable from denominator comparability alone;
- conditional: the positivity package is transportable if one imports a family-specific baseline-gap and value-channel interface;
- missing: a theorem that produces those inputs without leaning on zeta-specific or family-specific source realization.

Honest verdict: blueprint-level transportable, not theorem-level transportable.

# Status

conditional

# Evidence

The denominator theorem is not the positivity theorem. Proposition `Microscopic denominator comparability and omitted-smooth holomorphy` proves only holomorphy of `T_{\far}(t_\pm)` and `g_{\sm}(t_\pm)` on `|s|<\rho_0/Q`, assuming a zero-free-region lower bound on omitted-zero denominators. Its endpoint is microscopic holomorphy, not positivity or nondegeneracy of the same-point blocks. See `paper/proof_of_rh.tex:856-946`.

The actual positivity argument is Proposition `Corrected finite-s holomorphic whitening`. Its proof uses four inputs: holomorphy from denominator comparability; the perturbation bound `\sup\|R_{m,\pm}(s)\|=o(Q)` via Proposition `Entry-by-entry perturbation estimate` plus the tail-curvature theorem; the baseline variation bound `\sup\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\ll \rho_0 Q`; and the baseline spectral gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`. Only after combining those does the manuscript conclude uniform positive-definiteness and holomorphic inverse square roots. See `paper/proof_of_rh.tex:1392-1458`, especially `1418-1457`.

The perturbation and baseline-variation inputs are themselves stated using source-normalized baseline data, not an abstract family-free object. Proposition `Entry-by-entry perturbation estimate for the corrected same-point blocks` writes `q=q_0+\delta q`, where `q_0` is the baseline local-model-plus-affine-jet part, and assumes the microscopic remainder bounds together with the scale `|q_0(t_\pm)|\asymp Q`. See `paper/proof_of_rh.tex:948-1003`. Lemma `Baseline same-point variation` then uses the explicit same-point block formula built from `q_0` and the scale assumptions `|q_0|\ll Q`, `|q_0'|\ll Q^2`, `|q_0''|\ll Q^3`, `|q_0'''|\ll Q^4`. See `paper/proof_of_rh.tex:1332-1391`.

That means the positivity package still depends on a family-specific baseline model. In the current manuscript, that model is not presented as a theorem-level cross-family input schema; it is inherited from the zeta construction.

The dependence on source data becomes even more explicit in the fixed-core corrected-local-deformation package. Proposition `Corrected local deformation decomposition with fixed core` defines the corrected same-point blocks, mixed block, and whitened block from the decomposition `q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}` and then expands around the background value-channel parameter `S(m)=0`. The first-order coefficient is declared to be exactly the pure value-channel derivative `A_{\val}(m,\sigma)` associated with the fixed core `\mathcal C`. See `paper/proof_of_rh.tex:1497-1621`, especially `1502-1525`, `1531-1549`, and `1590-1606`.

The value-channel derivative itself is written in source-normalized form. In the explicit `A_{\val}` section the constant-background symmetric regime uses `B:=B_\zeta(m)` and `x=B\sigma`, and differentiates the jet-limit block with respect to a value perturbation `B+\alpha`. See `paper/proof_of_rh.tex:428-517`. So even the leading first-order direction used downstream by the positivity package is not yet stated independently of the source package.

The note files point in the same direction. `same_point_positivity.md` already says the package is separable from denominator holomorphy only at blueprint level and still imports source-normalized background/core data and the manuscript's `A_val` interface. `paired_slot_hypotheses.md` likewise separates microscopic holomorphy from same-point positivity/nondegeneracy and requires an explicit local admissibility package before whitening is even well-posed. See `same_point_positivity.md:5-23` and `paired_slot_hypotheses.md:12-23,31-52`.

Therefore the exact source-specific residue is not just a family-specific proof of denominator comparability. It is the family-specific production of the baseline block with the required gap and scales, together with the family-specific value-channel normalization identifying the first derivative as `A_{\val}`.

Honest verdict:

- proved: denominator holomorphy and same-point positivity are logically distinct;
- conditional: the positivity package transports once a family supplies the baseline-gap and value-channel hypotheses;
- missing: a theorem-level cross-family statement that packages those hypotheses canonically and proves them outside the zeta source realization.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:15-18,47-62,64-80,130-140`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:5-23`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-23,31-52,61-70`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:428-517` (`A_{\val}` in the `B:=B_\zeta(m)` normalization)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946` (denominator comparability gives holomorphy only)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:948-1003` (same-point perturbation written with `q=q_0+\delta q`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1332-1391` (baseline variation uses explicit `q_0` scales)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458` (positivity/holomorphic whitening proof)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1621` (fixed-core corrected deformation and expansion around `S(m)=0`)

# Dependencies

- The manuscript's corrected-whitening chain in `paper/proof_of_rh.tex`, especially the denominator-comparability, block-perturbation, baseline-variation, and corrected-local-deformation results.
- The note-level portability judgments in `same_point_positivity.md`, `paired_slot_hypotheses.md`, and `denominator_theorem.md`.
- The GRH bird's-eye summary distinguishing the portable local package from the still source-specific source theorem and value-channel realization.

# Strongest objection

The strongest objection is that I may be using too strong a notion of `transportable`. If one only wants a conditional local theorem of the form `given microscopic holomorphy, baseline same-point gap, and a named first-order value direction, holomorphic whitening follows`, then the package is already theorem-level transportable. I agree with that weaker reading. But under the mission's stronger reading, namely separability from family-specific source data, the answer is no: the current manuscript does not canonically produce the baseline gap or the `A_{\val}` interface without source-specific input.

# Needed for promotion

- State an abstract same-point positivity theorem whose hypotheses are explicit and family-neutral: microscopic holomorphy, baseline same-point nondegeneracy/gap, perturbative smallness, and a first-order value-channel parameter.
- Prove, for at least one non-zeta family, a source theorem that supplies those hypotheses in the manuscript's exact normalization.
- Decide paper language conservatively: `same-point positivity package` is presently safe as a reusable blueprint or conditional interface, not as a source-free theorem package.
