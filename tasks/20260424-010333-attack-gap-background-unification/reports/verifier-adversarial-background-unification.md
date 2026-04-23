## Claim

The background-unification conclusion is not closed from the current draft text.

- `one canonical symbol with parenthetical aliases` is the right safe fix only in a scoped, role-level form.
- It is not currently safe to write unqualified exact aliasing such as `B_\zeta=B_{\Aut}=B_{\bg}` or to say that the later symbols `refer to this same background term` without qualification.
- The strongest safe RH-facing wording I can support from the manuscript alone is:

`We write q(t)=B_\zeta(t)+S(t), where B_\zeta is the explicit background term and S is the background-subtracted zero contribution. In the later local and fixed-core decompositions, the symbols B_{\Aut} and B_{\bg} denote the local background role corresponding to B_\zeta in those decompositions.`

- Claims that need scoped weakening:
  - any sentence asserting literal identity of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`;
  - any sentence saying the issue is purely terminological or only bookkeeping;
  - any sentence saying no mathematical bridge is needed;
  - any sentence saying the later symbols are merely aliases, without adding `in those decompositions` or an equivalent scope restriction.

## Status

open

## Evidence

Separate three things: proved / conditional / missing.

### Proved

- The manuscript explicitly introduces `B_\zeta` as the top-level background symbol in
  `q(t)=B_\zeta(t)+S(t)`, and it uses `B_\zeta(m)` as the reader-facing scale in the calibration and contradiction chain. See `paper/proof_of_rh.tex:273-277`, `285-291`, `439-444`, `2058-2209`, `5497-5567`, `26326-26592`.
- The manuscript separately introduces `B_{\Aut}` only inside the local smooth split
  `g_{\sm}(t)=B_{\Aut}(t)+T_{\far}(t)`, and uses it in local analytic control such as curvature and holomorphic continuation of the smooth remainder. See `paper/proof_of_rh.tex:278-283`, `361-369`, `897-945`.
- The manuscript later introduces `B_{\bg}` only inside the fixed-core cutoff-dependent split
  `g_{\sm,R}(t)=B_{\bg}(t)+T_{\far,R}(t)` and in the derived background block/base-point notation `\widehat\Omega_{\bg}^{\corr,R}` and `D\mathcal W_{(\bg)}[\dot G_-,\dot N,\dot G_+]`. See `paper/proof_of_rh.tex:1471-1537`, `1590-1605`, `5932-5951`.
- The upstream notes already place `explicit background identification` inside the larger missing zeta-source package, not as a completed fact. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:27-31` and `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:15-20`.

### Conditional on intended semantics

- If the coordinator's intended semantics is only that all three notations isolate the same background contribution at different descriptive layers, then one canonical symbol with parenthetical aliases is a reasonable paper-facing cleanup.
- If the intended semantics is literal equality of objects on the relevant intervals, then that identification still needs to be stated and justified; the current text does not already prove it.
- Route B becomes safe only after weakening `same background term` to `background role corresponding to B_\zeta in those decompositions`, unless the exact identification is supplied elsewhere.

### Missing

- No displayed definition or theorem states whether `B_\zeta` and `B_{\Aut}` are the same function, or whether one is a global source term and the other its local analytic component.
- No displayed definition or theorem states whether `B_{\bg}` is literally the same background object as `B_{\Aut}` or `B_\zeta`, rather than a background base point adapted to the fixed-core corrected package.
- No bridge explains why the value-channel scalar defined by `S(m):=q_\zeta(m)-B_\zeta(m)` is exactly the scalar that parametrizes the expansion around the `B_{\bg}` background state `S(m)=0`.
- The symbol `q_\zeta` used in `S(m):=q_\zeta(m)-B_\zeta(m)` is not defined elsewhere in the draft portion I checked; the ambient decomposition is written with `q(t)`, not `q_\zeta(t)`. This blocks any claim that the notation mismatch is already harmless.

## Exact refs

- Top-level background split and `S(m)` definition: `paper/proof_of_rh.tex:273-291`
- Calibration uses of `B_\zeta(m)`: `paper/proof_of_rh.tex:439-444`, `2058-2209`, `5497-5567`, `26326-26592`
- Local smooth split with `B_{\Aut}`: `paper/proof_of_rh.tex:278-283`, `361-369`, `897-945`
- Fixed-core split with `B_{\bg}` and background base point: `paper/proof_of_rh.tex:1471-1537`, `1590-1605`
- Later schematic use of `D\mathcal W_{(\bg)}[...]`: `paper/proof_of_rh.tex:5932-5951`
- Missing-package guidance: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:27-31`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:15-20`
- Prior attack reports under review: `tasks/20260424-010333-attack-gap-background-unification/reports/gap-background-unification-routeA.md`; `tasks/20260424-010333-attack-gap-background-unification/reports/gap-background-unification-routeB.md`

## Dependencies

- This verdict depends only on the cited notes, the two route reports, and the current manuscript text.
- Any upgrade from role-level correspondence to exact aliasing depends on the missing source-normalization / explicit-background-identification package.
- This report does not depend on endgame closure or family portability.

## Strongest objection

My recommended weakening may be too cautious if the intended manuscript semantics is already exact identity and the omitted bridge is genuinely trivial. But from the current text alone, that identity is not proved, and an RH agent should not collapse `corresponding background role` into `same object` without a stated bridge. Any impossibility claim here is only `from the current text alone`.

## Needed for promotion

- Keep `B_\zeta` as the canonical reader-facing symbol, since it is already the stable symbol in the calibration and contradiction chain.
- If the goal is a minimal safe wording patch now, use parenthetical aliases only with scope, e.g. `in the later local and fixed-core decompositions` or equivalent.
- Weaken route B's candidate sentence from `refer to this same background term` to `denote the corresponding local background role` unless exact equality is explicitly defined.
- Repair the `q` versus `q_\zeta` mismatch before claiming the notation is fully unified.
- If exact aliasing is intended, add one explicit bridge sentence or theorem giving the identification and the value-channel compatibility with the `S(m)=0` background base point.

Honest verdict: the safe conclusion is narrower than `routeB` presently states. `one canonical symbol with parenthetical aliases` is the right low-risk fix only as scoped correspondence language. Exact aliasing is still missing. For an RH agent, the strongest safe wording is to keep `B_\zeta` canonical and say that `B_{\Aut}` and `B_{\bg}` denote the corresponding background role in the later decompositions, not yet the same proved object.
