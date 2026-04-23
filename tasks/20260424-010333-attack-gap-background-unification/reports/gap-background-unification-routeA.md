## Claim

The current manuscript uses three different background labels for closely related but not identical roles:

- `B_\zeta` is the active global zeta-side background term in the decomposition `q(t)=B_\zeta(t)+S(t)`, and it is the manuscript's main background scale in later calibration and endgame formulas.
- `B_{\Aut}` is the active local smooth-background term inside `g_{\sm}(t)=B_{\Aut}(t)+T_{\far}(t)`, and it is used only where curvature control and holomorphic extension of the smooth remainder are needed.
- `B_{\bg}` is not an active manuscript-wide symbol. It survives only in the fixed-core corrected-block subsection as an older baseline/background notation, where it plays the same formal role that `B_{\Aut}` plays in the earlier local-smooth split, and where it also induces the derived background block symbol `\widehat\Omega_{\bg}^{\corr,R}`.

Honest verdict: the draft has real notation drift, not three cleanly separated background objects. `B_\zeta` and `B_{\Aut}` can be read as compatible only if one supplies an unstated identification between the global explicit background and the local holomorphic background term. `B_{\bg}` reads as legacy notation from an older layer of the same package, not as a third independently defined object.

## Status

open

## Evidence

Proved from the current text alone:

- `B_\zeta` is explicitly introduced at the start of the zeta-side package by
  `q(t)=B_\zeta(t)+S(t)` with the sentence `B_\zeta` is the explicit background contribution and `S` is the background-subtracted zero contribution. See `paper/proof_of_rh.tex:273-277`.
- The manuscript then defines `S(m):=q_\zeta(m)-B_\zeta(m)` and uses `B_\zeta(m)` as the principal background magnitude in the calibration variable `x=B_\zeta(m)\sigma`, in the size of `A_{\val}`, in the calibrated toy/zeta comparison, and in the final contradiction. See `paper/proof_of_rh.tex:285-292`, `439-444`, `2050-2209`, `5495-5542`, `26301-26363`, `26440-26592`.
- `B_{\Aut}` is introduced only through the local smooth remainder split `g_{\sm}(t):=B_{\Aut}(t)+T_{\far}(t)`. Its actual uses are local analytic ones: curvature bounds through `\|B_{\Aut}''\|`, and holomorphic extension of `g_{\sm}(t_\pm)` by adding the holomorphic background term `B_{\Aut}(t_\pm)`. See `paper/proof_of_rh.tex:278-283`, `361-370`, `816-820`, `891-945`.
- `B_{\bg}` appears only in the fixed-core decomposition subsection, where the phase derivative is rewritten as `q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}` with `g_{\sm,R}=B_{\bg}+T_{\far,R}`. The same subsection defines the background whitened block `\widehat\Omega_{\bg}^{\corr,R}` and the derivative base point `D\mathcal W_{(\bg)}[\dot G_-,\dot N,\dot G_+]`. See `paper/proof_of_rh.tex:1460-1621`, especially `1471-1505`, `1527-1537`, `1590-1605`. Outside this lane, the only later surviving use is the reminder that the full value family is taken at the same background base point `D\mathcal W_{(\bg)}[...]`. See `paper/proof_of_rh.tex:5932-5951`.

Conditional on an unstated identification:

- The cleanest reading is that `B_{\Aut}` and `B_{\bg}` are intended to denote the same local smooth background object, just in two different notational layers: the earlier local-smooth split and the later fixed-core corrected-block split. This is suggested by the matching formulas `g_{\sm}=B_{\Aut}+T_{\far}` and `g_{\sm,R}=B_{\bg}+T_{\far,R}` and by the fact that both serve as the holomorphic smooth background added to a far-zero tail. See `paper/proof_of_rh.tex:281`, `897-945`, `1489-1505`.
- A second likely intended identification is that `B_\zeta` is the global explicit background whose local contribution is represented by `B_{\Aut}` or `B_{\bg}` once one passes to the corrected local package. The draft never states this equivalence directly.

Missing from the current text:

- No theorem or definition states whether `B_\zeta=B_{\Aut}` pointwise, or whether one is a global object and the other its local analytic component.
- No bridge explains why `S(m):=q_\zeta(m)-B_\zeta(m)` is the same value-channel scalar that appears in the fixed-core expansion around the `B_{\bg}` base point `S(m)=0`.
- `q_\zeta` is used in the definition of `S(m)` but is not defined in the displayed setup; the surrounding decomposition uses `q(t)`, not `q_\zeta(t)`. See `paper/proof_of_rh.tex:273-288`.
- No sentence explains whether `\widehat\Omega_{\bg}^{\corr,R}` is built from the same background symbol as the earlier `B_{\Aut}` term, or from the global `B_\zeta` background after local freezing.

## Exact refs

- Background/global split: `paper/proof_of_rh.tex:271-299`
- Local smooth split with `B_{\Aut}`: `paper/proof_of_rh.tex:278-283`, `302-396`, `852-946`
- Calibration uses of `B_\zeta`: `paper/proof_of_rh.tex:426-458`, `2050-2209`, `5487-5577`, `26301-26592`
- Fixed-core lane with `B_{\bg}` and `\widehat\Omega_{\bg}^{\corr,R}`: `paper/proof_of_rh.tex:1460-1621`
- Later surviving background-basepoint use `D\mathcal W_{(\bg)}[...]`: `paper/proof_of_rh.tex:5932-5951`
- Upstream guidance that the background identification is part of the missing zeta-source package: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:10-12,27-31`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-20`

## Dependencies

- The symbol map depends only on the current draft text and the two cited GRH notes.
- Any promotion from `conditional` to `proved` would require the missing zeta-source normalization/background-identification package flagged in the notes.

## Strongest objection

The report infers likely intended identifications from parallel formulas and roles. That inference is not yet a proved manuscript fact. In particular, the text does not itself rule out the possibility that `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` were meant to be genuinely different layers, with omitted transition formulas between them.

## Needed for promotion

- One canonical background definition, stated once.
- One explicit bridge saying how the local smooth term (`B_{\Aut}` or renamed replacement) is obtained from the global zeta background `B_\zeta`.
- One explicit statement that the fixed-core background base point `\widehat\Omega_{\bg}^{\corr,R}` is the same background normalization used in the earlier zeta-side decomposition.
- Repair the `q` versus `q_\zeta` mismatch in the definition of `S(m)`.
