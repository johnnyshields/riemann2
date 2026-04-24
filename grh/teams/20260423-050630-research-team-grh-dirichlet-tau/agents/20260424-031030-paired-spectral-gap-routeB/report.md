# Claim

The strongest safe boundary sentence is:

`Same-point positivity/nondegeneracy may be stated as its own local whitening hypothesis line, but not as a theorem consequence of denominator transport alone: denominator comparability safely supplies microscopic holomorphy and removable-singularity control, while uniform positivity of the corrected same-point blocks is a separate spectral-gap stability input used to define holomorphic inverse-square-root whitening.`

So the safe separation is:

- positivity/nondegeneracy is separable at the statement level from denominator transport;
- it is not separable as something proved by denominator transport alone in the current manuscript;
- the entanglement is one-way: denominator transport feeds the holomorphy side of whitening admissibility, while positivity needs additional baseline-gap plus perturbative control.

# Status

conditional

# Evidence

Proved in the manuscript and notes:

- `paired_slot_hypotheses.md` already splits the minimal local package into `microscopic holomorphy`, `same-point positivity/nondegeneracy`, and `well-defined inverse-square-root whitening`, and explicitly says denominator comparability is not a co-equal slot-theorem endpoint but only a source of the minimal holomorphy residue. This supports a separate local hypothesis line for positivity.
- `denominator_theorem.md` assigns denominator comparability a narrow role: carrying omitted-zero control to the microscopic disk, supplying omitted-smooth holomorphy, and supporting corrected-whitening admissibility. Its safe wording does not claim that denominator transport alone proves positivity.
- `corrected_whitening_transport.md` packages the safe bundle as `(i) denominator comparability plus omitted-smooth holomorphy`, `(ii) holomorphic corrected whitening with positive same-point blocks`, `(iii) preserved transfer scale`. This is direct evidence that positivity sits at the whitening layer, not inside denominator comparability itself.
- In `paper/proof_of_rh.tex`, Proposition `Microscopic denominator comparability and omitted-smooth holomorphy` proves holomorphic extension of `T_{\far}(t_\pm)` and its derivatives on `|s|<\rho_0/Q`; its endpoint is holomorphy, not matrix positivity.
- In the later Proposition `Corrected finite-s holomorphic whitening`, the proof separates the two mechanisms: holomorphy comes from denominator comparability plus removable singularities, while positivity comes from the perturbation estimate, the baseline variation lemma, and the baseline lower bound `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`. Only after that positivity step does holomorphic functional calculus produce `G_{m,\pm}^{\corr}(s)^{-1/2}`.

Conditional on the paired family following the same architecture:

- same-point positivity/nondegeneracy can safely be given its own local hypothesis line, because the manuscript already treats it as a logically distinct whitening ingredient;
- denominator transport should remain named only for the holomorphy/removable-pole side unless a paired theorem actually derives uniform positive definiteness from the same transport package;
- the cleanest bundled wording is a two-line local package: `(i) microscopic holomorphy/removable-singularity control`, `(ii) same-point positivity/nondegeneracy sufficient for holomorphic whitening`.

Missing for a fully proved paired statement:

- a paired analogue of the baseline spectral-gap / perturbative-stability argument proving the corrected same-point paired blocks remain uniformly positive definite on the microscopic disk;
- a paired proof that this positivity line is independent of any stronger quantitative denominator-transport conclusions such as preserved post-whitening scale or remainder bounds;
- an adversarial check that the paired local object really needs uniform positivity on the disk, rather than a weaker base-point nondegeneracy or a stronger transport-scale statement.

Honest verdict:

- proved: denominator comparability supports microscopic holomorphy;
- conditional: same-point positivity/nondegeneracy can be a separate local hypothesis line for whitening admissibility;
- missing: a paired proof that this positivity line follows from the intended paired hypotheses rather than being imported as an extra assumption.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-24,31-45,54-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:6-27`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1332-1458`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1569-1575`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:6076-6086`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeA/report.md:26-50,68-76`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeB/report.md:20-40,59-68`

# Dependencies

- The three supplied notes as the intended paired-theorem boundary.
- The manuscript's corrected-whitening proof as the authoritative model for what is obtained from denominator comparability versus what requires positivity.
- The prior paired-positivity reports, used only as cross-checks against the manuscript split.

# Strongest objection

The manuscript may still leave positivity too entangled with the rest of corrected-whitening transport to justify calling it a completely standalone local line in the paired family. In particular, the proof of positivity on the disk uses a baseline spectral-gap input and perturbation bounds that may themselves depend on more analytic infrastructure than the notes currently expose. So the safe claim is only statement-level separability: positivity should be named separately, but not advertised as already derivable from denominator transport alone.

# Needed for promotion

- Prove a paired analogue of `Corrected finite-s holomorphic whitening` that explicitly separates holomorphy from positivity/nondegeneracy.
- Identify and cite the paired source of the baseline same-point spectral gap at the base point.
- Verify whether the paired perturbation bounds needed to preserve positivity are weaker than, equal to, or essentially the same as the current denominator-transport package.
