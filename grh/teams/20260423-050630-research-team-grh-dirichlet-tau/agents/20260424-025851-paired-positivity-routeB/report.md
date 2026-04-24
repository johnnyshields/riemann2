# Claim

Same-point positivity/nondegeneracy should not be left hidden inside an unexpanded generic phrase like `minimal local admissibility`.

The strongest safe formulation is:

`At slot level one may keep a single local-admissibility bundle, but that bundle must state explicitly a paired local spectral-gap / whitening clause: the corrected same-point blocks are holomorphic on the microscopic disk and remain uniformly positive definite there, so holomorphic inverse-square-root whitening is defined. This is a hypothesis for exact paired-slot meaning, not yet a quantitative transport or remainder theorem.`

So the safe answer is:

1. positivity does not need to become a separate downstream theorem endpoint co-equal with transport or remainder dominance;
2. but it does deserve its own named hypothesis line inside the paired local package, because in the manuscript it is not automatic from a bare generic admissibility label and is justified through an actual baseline spectral-gap plus perturbation argument.

# Status

conditional

# Evidence

Proved:

- `paired_slot_hypotheses.md` already isolates `positive same-point blocks` as part of the minimal hypothesis stack needed before the exact paired slot identity is even well-posed, alongside microscopic holomorphy and inverse-square-root whitening. So positivity is already singled out at the content level, not buried as an unnamed afterthought.
- `corrected_whitening_transport.md` treats `holomorphic corrected whitening with positive same-point blocks` as a distinct front-end ingredient of the safe bundle, while keeping value-channel realization, boundary control, and remainder dominance separate. This supports the conclusion that positivity belongs to the local definability layer, not the downstream quantitative layer.
- In the manuscript, Proposition `Corrected finite-s holomorphic whitening` states not merely holomorphy of the corrected same-point blocks, but also their uniform positive definiteness on the microscopic disk; only then are the holomorphic inverse square roots and the whitened block obtained. Thus same-point positivity/nondegeneracy is a logically separate clause in the proof of well-posed whitening, not a consequence of the word `holomorphic` alone.
- The proof at `paper/proof_of_rh.tex:1436-1456` is explicitly a spectral-gap stability argument: a baseline gap at `s=0` plus perturbative control implies positivity on the disk, then holomorphic functional calculus yields `G_{m,\pm}^{\corr}(s)^{-1/2}`. That is exactly local spectral-gap content.
- Later in the manuscript's pair-local rigidity discussion, the cubic-leading proposition and its follow-up remark explicitly list `x_1\neq x_2` as a logically distinct `background same-point nondegeneracy condition`. This reinforces that same-point nondegeneracy is already treated as its own structural input, not merely as generic admissibility shorthand.

Conditional on [a faithful paired analogue of the manuscript local package]:

- The paired theorem statement can still use a bundled heading such as `minimal local admissibility`, but only if one of the displayed subclauses is explicit spectral-gap wording, e.g. `paired local whitening admissibility: the corrected same-point blocks remain uniformly positive definite on the microscopic disk`.
- If the theorem statement is intended to show the logical fault lines cleanly, an even safer presentation is to split the local package into two named lines: `(i) microscopic holomorphy/removable-singularity control` and `(ii) same-point spectral-gap / whitening admissibility`. This avoids implying that positivity is formally automatic once holomorphy is granted.
- What should still remain outside this named positivity clause is any quantitative transport conclusion: preserved post-whitening scale, denominator-comparability as a theorem endpoint, remainder smallness, and odd/transverse boundary control.

Missing:

- A paired-family proof that the same-point positivity/nondegeneracy clause follows from the intended paired hypotheses, rather than being imported as a free-standing local assumption.
- A paired theorem statement fixing the exact naming convention: whether the safe clause is called `same-point positivity`, `same-point nondegeneracy`, or `paired local spectral-gap / whitening admissibility`.
- A paired adversarial check that `uniform positive definiteness on the microscopic disk` is the right invariant statement, rather than a weaker pointwise positivity at the base point or a stronger transport-scale assertion.

Honest verdict: positivity should not be advertised as a separate downstream theorem, but it also should not stay hidden inside an opaque generic admissibility label. The manuscript evidence supports giving it an explicit named local spectral-gap / whitening hypothesis line.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-18,25-37,46-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:11-22,24-27`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1457`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1436-1456`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5996-6086`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-024215-paired-admissibility-boundary-routeB/report.md:35-56,78-87`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-024215-paired-admissibility-boundary-routeA/report.md:16-37,57-66`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-022935-paired-slot-hypotheses-routeB/report.md:34-56,90-99`

# Dependencies

- The supplied slot-hypotheses and corrected-whitening-transport notes.
- The manuscript's corrected-whitening proposition as the model for what local positivity/nondegeneracy actually buys.
- The manuscript's cubic-leading section, where same-point nondegeneracy is already treated as a distinct structural input.

# Strongest objection

The manuscript evidence may still be too one-family specific to justify a separately named paired `spectral-gap` hypothesis rather than the plainer phrase `positive same-point blocks`. In the paper, the positivity statement is matrix positivity of the corrected same-point blocks and only indirectly a spectral-gap statement via the lower-bound proof. So the safest naming may be `same-point positivity/nondegeneracy for holomorphic whitening`, with `local spectral-gap` used only as explanatory gloss, not as the formal theorem title.

# Needed for promotion

- Write the paired slot theorem with an explicit local clause for same-point positivity/nondegeneracy, rather than leaving it implicit inside `minimal admissibility`.
- Decide the final label by conservatism: likely `same-point positivity/nondegeneracy` or `whitening admissibility`, with `spectral-gap` mentioned only if the paired proof really establishes a uniform lower bound on the microscopic disk.
- Prove a paired analogue of corrected holomorphic whitening that separates `(i) microscopic holomorphy` from `(ii) positivity/nondegeneracy sufficient for inverse-square-root whitening`.
- Verify adversarially whether the paired route truly gives uniform positivity on the disk, or only background-point nondegeneracy plus a perturbative radius depending on additional transport inputs.
