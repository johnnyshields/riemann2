## Claim

The current reduced-`\widehat\Psi` coincidence theorem is not the genuine minimal package theorem for the `UV-002` queue. It is too strong for Bottleneck C, because C reduces to a smaller diagonal-collapse statement at coincidence, and it is too weak for Bottleneck D, because equal reduced-`\widehat\Psi` fibers do not yet control the first surviving odd jet.

## Status

heuristic

## Evidence

- The draft itself already separates the package target from raw septic equality: the honest order-`7` target is stated as same reduced image germ or collision-functoriality, not raw representative equality.
- But the current collation sharpens Bottleneck C further: once analyticity and swap-evenness of the actual corrected reduced package germ are granted, the remaining content is only diagonal-collapse at `\delta=0`, namely `\kappa`-independent diagonal value agreeing with the one-pair reduced package. That is strictly smaller than full same-reduced-image-germ.
- The draft’s current package datum is exactly `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)`, and the minimal-core reformulation treats extraction as a two-stage problem: first coincidence information for `\widehat\Psi`, then conversion to the downstream geometric/extraction constraint.
- The extractor side is already complete: `H_m`, the odd coefficients, finite-core localization, and `\Xi_\zeta^{(N)}` already isolate the first surviving odd jet once package-side factorization is available.
- The current collation also says reduced-`\widehat\Psi` fibers are not enough for Bottleneck D: a hidden `\Phi_K`-visible one-dimensional septic-gauge direction survives, so D still needs either a hidden-state lemma showing that the forgotten directions are `\Phi_K`-invisible through first surviving odd order, or one extra visible scalar/equivalent larger package state.
- Therefore the honest minimal split is:
- for C: a smaller diagonal-collapse / `\kappa`-independence theorem at coincidence;
- for D: a separate hidden-state theorem (or enlarged package datum), not the full reduced-germ theorem by itself.

## Exact refs

- `paper/proof_of_rh.tex:10780-10810`
- `paper/proof_of_rh.tex:11368-11585`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:14198-14243`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/proof_of_rh.tex:26369-26398`
- `paper/proof_of_rh.tex:2214-2307`
- `paper/proof_of_rh.tex:2953-2969`
- `paper/proof_of_rh.tex:3984-4190`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-119`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-124`

## Dependencies

- The current Bottleneck C reformulation in team collation.
- The current Bottleneck D hidden-state obstruction in team collation.
- The in-draft definition of `\widehat\Psi` and the zeta-side odd-jet extractor already proved.

## Strongest objection

The sharp D-side claim about a surviving one-dimensional `\Phi_K`-visible hidden direction is not yet packaged as a canonical theorem in the draft itself; at present it is carried by team collation rather than a finished in-paper statement. So the conclusion that reduced-`\widehat\Psi` is too weak for D is structurally convincing, but not yet paper-level closed.

## Needed for promotion

1. State C in its smaller exact form: diagonal-collapse at coincidence, i.e. `\kappa`-independent diagonal value matching the one-pair reduced package.
2. State D separately as a hidden-state lemma: the quotient from raw package data to the chosen reduced datum forgets only `\Phi_K`-invisible directions through the first surviving odd order, or else retain the one extra visible scalar explicitly.
3. Only after that decide whether a reduced-germ theorem is still worth keeping as a corollary or organizational wrapper.

Honest verdict: reduced-`\widehat\Psi` coincidence is no longer the minimal package theorem. A smaller theorem should replace it on Bottleneck C, while Bottleneck D still needs an additional hidden-state theorem beyond reduced-germ equality.
