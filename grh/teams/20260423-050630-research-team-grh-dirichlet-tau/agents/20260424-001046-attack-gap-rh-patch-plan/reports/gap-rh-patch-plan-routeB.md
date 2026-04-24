# gap-rh-patch-plan-routeB

**Claim**

The highest-value, lowest-risk editorial restructure is to split the RH draft into an explicit source-light local package and a separate zeta-source package, with the calibration and odd-channel estimates stated as conditional on the source package wherever they currently depend on `S(m)`, `B_\zeta`, or the realized decomposition `q=B_\zeta+S`.

**Status**

open

**Evidence**

Proved:

- The draft already has a genuinely source-light local geometry block at the front: the phase-kernel definition, jet-limit matrices, finite-`s` removable-singularity analysis, and holomorphic whitening are formulated for a general phase `\Phi` and its derivative `q`, not yet for a specific zeta source. See `paper/proof_of_rh.tex:145-269` and `1392-1458`.
- The abstract odd-germ mechanism is structurally local once a corrected odd holomorphic scalar exists with boundary control. In the present draft that mechanism is encoded in the odd holomorphic transverse channel and the later `N`-point odd-moment machinery. The portability note's Layer 1 / Layer 2 split matches this reading. See `paper/proof_of_rh.tex:2212-2322`, `2975ff.`, and `grh/.../notes/local_package_theorem.md:10-43`.

Conditional on zeta-source input:

- The first explicit source-specific jump happens in `\section{Zeta-side decomposition}`, where the paper writes `q(t)=B_\zeta(t)+S(t)` and defines `S(m):=q_\zeta(m)-B_\zeta(m)` before an explicit theorem identifying the manuscript phase derivative with the scattering quotient source. See `paper/proof_of_rh.tex:271-300` and `grh/.../notes/source_theorem_gap.md:11-40`.
- The calibration chain is local algebra only after the realized scalar slot exists. In the current draft `\Delta_\zeta=S(m)A_{\val}+R_\zeta`, the calibration theorem, the cutoff choice, and the sharpened remainder estimate all depend on `S(m)`, `B_\zeta(m)`, and the source-realized value channel. See `paper/proof_of_rh.tex:739-850`.
- The corrected local deformation decomposition presently treats `S(m)A_{\val}` as an available first-order term inside the full corrected object. That is a clean interface theorem once the source package is in place, but not part of the unconditional local package. See `paper/proof_of_rh.tex:1497-1683` and `grh/.../notes/local_package_theorem.md:29-43`.
- The boundary estimate and odd-expansion bounds are currently presented as unconditional statements in the zeta draft, but their size bounds use `L(m)S(m)^2` and therefore sit downstream of the source realization and curvature package. See `paper/proof_of_rh.tex:2214-2322`.
- The endgame still uses source-specific quantities in the lower/upper bound comparison, so it should remain outside any generic local theorem. See `paper/proof_of_rh.tex:26366-26479`.

Missing:

- The paper lacks a standalone theorem that fixes the source object and proves the manuscript's own phase derivative/source identity. The missing pieces are exactly the quotient choice, phase normalization, single-zero contribution identity, multiplicity convention, compact-interval convergence/regularization, and unified background identification. See `grh/.../notes/source_theorem_gap.md:22-40`.
- The introduction still presents the whole architecture as one continuous zeta-side proof strategy, without explicitly telling the reader which pieces are generic local geometry and which pieces are zeta realization. See `paper/proof_of_rh.tex:105-126`.

Highest-value, lowest-risk restructure:

- Keep Sections 1--2 and the holomorphic-whitening package as the local geometry package.
- Move the editorial boundary to the start of `\section{Zeta-side decomposition}` and explicitly label everything from `q=B_\zeta+S` onward as zeta-source input or downstream of it.
- Add one short roadmap paragraph near the end of the introduction stating three bins: local geometry proved in source-light form; zeta-source realization conditional / pending canonical source theorem; RH endgame downstream of both.
- Reframe the calibration theorem, corrected local decomposition, and boundary estimate as interface results: they are proved local algebra once the source theorem supplies the exact scalar slot and the curvature package supplies the needed bounds.
- Do not move the endgame architecture. Only insert a local/source boundary and restate dependencies.

**Exact refs**

- `paper/proof_of_rh.tex:105-126`
- `paper/proof_of_rh.tex:145-269`
- `paper/proof_of_rh.tex:271-300`
- `paper/proof_of_rh.tex:739-850`
- `paper/proof_of_rh.tex:1392-1458`
- `paper/proof_of_rh.tex:1497-1683`
- `paper/proof_of_rh.tex:2212-2322`
- `paper/proof_of_rh.tex:26366-26479`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:13-18,22-45,153-162,197-201`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:6-58`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:6-54`

**Dependencies**

- A canonical zeta source theorem for `q` and `S`.
- The existing local kernel / jet / whitening package.
- The current calibration and curvature bookkeeping, but now described as downstream interface material rather than part of the source-light theorem.

**Strongest objection**

The draft's current later sections are already deeply written in zeta notation, so a sharper editorial split may expose that some statements now labeled as propositions would need weaker headlines or explicit hypotheses rather than mere prose reframing. In particular, the boundary estimate and calibration package may read less final once their dependence on the missing source theorem is made explicit.

**Needed for promotion**

- Verify section-by-section which theorem statements can stay unconditional and which must acquire an explicit source-realization hypothesis.
- Draft exact replacement wording for the introduction and for the opening paragraph of `\section{Zeta-side decomposition}`.
- Check that every use of `S(m)`, `B_\zeta`, `L(m)`, or `q_\zeta` is either inside the zeta-source package or explicitly downstream of it.

Honest verdict:

The restructure is worth doing. It is low risk because it mostly changes theorem boundaries and reader guidance, not mathematics. The clean boundary is: local phase geometry, whitening, and odd-germ/projector algebra on one side; the zeta realization `q=B_\zeta+S`, the exact `S(m)` slot, and every calibration or size estimate involving `S(m)` on the other. Proved: the source-light local package exists in substantial form. Conditional: the interface and zeta-side estimates once the source theorem is supplied. Missing: the canonical zeta source theorem itself and the explicit editorial separation that tells the reader this is the architecture.
