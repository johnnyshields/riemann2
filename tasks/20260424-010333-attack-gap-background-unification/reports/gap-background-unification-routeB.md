## Claim

The smallest safe background-name unification patch is **one canonical symbol with parenthetical aliases**, not a new theorem. The safest paper-facing choice is to keep `B_\zeta` as the canonical name, introduce it once at the start of `\section{Zeta-side decomposition}`, and say that the later notations `B_{\Aut}` and `B_{\bg}` denote the same explicit background term in the local/fixed-core decompositions under discussion.

## Status

heuristic

## Evidence

### Proved

- The naming split is real in the current draft. The first zeta-side decomposition uses
  `q(t)=B_\zeta(t)+S(t)` and `S(m):=q_\zeta(m)-B_\zeta(m)` at `paper/proof_of_rh.tex:273-291`.
- The smooth-remainder package later uses `g_{\sm}(t):=B_{\Aut}(t)+T_{\far}(t)` at
  `paper/proof_of_rh.tex:279-283`, and this notation is used again in the holomorphy and
  curvature estimates at `paper/proof_of_rh.tex:368-369, 818, 897, 944-945`.
- The fixed-core decomposition later switches again to `B_{\bg}` via
  `g_{\sm,R}(t):=B_{\bg}(t)+T_{\far,R}(t)` at `paper/proof_of_rh.tex:1471-1506`.
- The manuscript already treats `B_\zeta(m)` as the reader-facing background scalar in the
  main calibration and comparison formulas, for example at `paper/proof_of_rh.tex:439-444,
  2058-2209, 5497-5567, 26326-26592`. So `B_\zeta` is already the stable top-level name.
- The cited planning notes support a localized, minimal patch near the start of `\section{Zeta-side decomposition}` rather than a larger restructuring: see
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31` and
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-35`.

### Conditional on explicit identification already intended by the draft

- A safe low-risk sentence is:

  `We write q(t)=B_\zeta(t)+S(t), where B_\zeta is the explicit background term and S is the background-subtracted zero contribution. In the later local and fixed-core decompositions, the notations B_{\Aut} and B_{\bg} refer to this same background term, written with labels adapted to those decompositions.`

- This is safe **if** the coordinator intends `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` to be the same object, with only the surrounding decomposition changing. On that reading, the patch is purely terminological and does not add a new mathematical dependency.
- On that reading, a separate equivalence theorem is higher-risk than necessary. It would force the paper to prove an interval-by-interval identification statement that is closer to the larger source-normalization/background-identification package than to a naming cleanup.

### Missing

- I do not see, in the currently read portions, a single explicit sentence that identifies `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` as the same background contribution.
- I also do not see a proved interval-equivalence theorem already in place that would justify introducing a new named theorem solely for this unification task.
- The broader source-package notes mention `explicit background identification` as part of a bundled localized source theorem; that supports treating a new theorem here as a larger mathematical patch, not as the smallest safe naming patch.

## Exact refs

- `paper/proof_of_rh.tex:273-291`
- `paper/proof_of_rh.tex:368-369`
- `paper/proof_of_rh.tex:439-444`
- `paper/proof_of_rh.tex:818`
- `paper/proof_of_rh.tex:897, 944-945`
- `paper/proof_of_rh.tex:1471-1506`
- `paper/proof_of_rh.tex:2058-2209`
- `paper/proof_of_rh.tex:5497-5567`
- `paper/proof_of_rh.tex:26326-26592`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-35`

## Dependencies

- The recommendation depends on the intended manuscript semantics that the three background names are aliases for one explicit background term on the relevant local intervals.
- It does **not** depend on closing the endgame, proving portability to other families, or promoting the full bundled zeta-source theorem.

## Strongest objection

If `B_{\Aut}` or `B_{\bg}` is not literally the same object as `B_\zeta` but instead a modified background obtained after a different normalization or truncation convention, then an alias sentence would overstate the identification. In that case the safe patch is still not a new equivalence theorem; it is a more cautious wording such as `the later symbols isolate the background role corresponding to B_\zeta in those decompositions` until the exact identification is proved in the source package.

## Needed for promotion

- One coordinator check: confirm whether the intended semantics is exact aliasing (`B_\zeta=B_{\Aut}=B_{\bg}` on the intervals used) or only role-level correspondence.
- If exact aliasing is intended, promote the one-sentence canonical-name patch near `paper/proof_of_rh.tex:273-283` and use `B_\zeta` as the default reader-facing symbol thereafter.
- If only role-level correspondence is intended, keep `B_\zeta` canonical at first introduction and add a scoped parenthetical note for `B_{\Aut}` and `B_{\bg}` without asserting theorem-level equivalence.
