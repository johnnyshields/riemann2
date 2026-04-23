Claim

Assume a clean reduced-germ theorem for the actual corrected two-atom package: near coincidence, the package descends functorially to a single reduced germ, with diagonal value equal to the one-pair reduced package at coincident atoms. Then the immediate consequences split as follows.

1. Fixed-shear package theorem (B): on the residual exact fixed-shear involutive branch, Bottleneck B is essentially formal. The existing exact fixed-shear machinery already reduces the quotient-visible transport state to one scalar and rules out any further finite hidden reset; the only remaining input is diagonal-collapse / merger of the actual corrected package at coincidence. A clean reduced-germ theorem supplies exactly that input, so the actual corrected cubic/quintic defects become swap-even with zero diagonal value, yielding the needed vanishing at coincidence and hence the existing conditional fixed-shear closure theorem applies.

2. Hidden extraction theorem (D): a reduced-germ theorem does not by itself close Bottleneck D on the present draft. Its exact immediate effect is to reduce D to a pure fiber-invariance statement: prove that the first surviving odd jet of `H_m`, equivalently the first nonzero `\Xi_{\zeta,\le H}^{(N)}`, is constant on fibers of the reduced package map, or equivalently that every raw-package direction forgotten by the quotient to the reduced germ is `\Phi_K`-invisible through the first surviving odd order. If the reduced-germ theorem is strengthened to include the extra `\Phi_K`-visible hidden scalar now known to survive (current best candidate: the septic gauge scalar, visible for instance as `T=v_7/c` on `v_5\neq 0`), then the hidden extraction theorem becomes formal from the already-built zeta-side extractor. Without that strengthening, Bottleneck D remains open but strictly sharpened.

Status

heuristic

Evidence

The draft already isolates Bottleneck B as a diagonal-collapse / merger problem on the exact fixed-shear involutive branch. On that branch, the quotient-visible transport state has local rank `1`, and no further finite hidden reset survives. The existing closure proposition only asks that the corrected cubic/quintic defects factor through that descended state and vanish at the diagonal point; the stronger package-collapse corollary asks the same merger law at equal states. A reduced-germ theorem with correct diagonal value therefore gives the missing hypothesis directly.

For Bottleneck D, the draft and current collation both say the extractor side is already complete: `H_m`, its odd coefficients, `\Xi_\zeta^{(N)}`, and finite-core localization are all done. The remaining issue is package-to-jet factorization. The collation further records that equal reduced-`\widehat\Psi` fibers are not enough on the present draft because a septic-gauge direction is generically `\Phi_K`-visible. So reduced-germ coincidence alone sharpens D to the hidden-state lemma rather than closing it outright.

Exact refs

- `paper/proof_of_rh.tex:5604-5643` (`rem:wip-pairlike-finitecore`)
- `paper/proof_of_rh.tex:11368-11450` (definition and role of `\widehat\Psi`)
- `paper/proof_of_rh.tex:11476-11585` (`prop:exact-strengthened-two-pair-coincidence`)
- `paper/proof_of_rh.tex:11888-12189` (`lem:minimal-source-level-two-point-criterion`, `rem:wip-source-level-reduction-two-point-branch`)
- `paper/proof_of_rh.tex:12447-12610` (`rem:wip-parity-projective-factorization-collision-blow-up`, `rem:what-remains-two-pair-rewrite`, `rem:current-three-front-compression-two-point-endgame`, `rem:minimal-core-reformulation`)
- `paper/proof_of_rh.tex:21736-21763` (residual exact fixed-shear corner compressed to provenance-sensitive package data)
- `paper/proof_of_rh.tex:22409-22529` (`prop:conditional-state-local-defect-closure-fixed-shear-corner`, `cor:stronger-state-local-package-collapse-fixed-shear-corner`)
- `paper/proof_of_rh.tex:24985-25030` (three-layer finite-core split)
- `paper/proof_of_rh.tex:26369-26398` (`rem:wip-final-endgame-status`)
- `paper/proof_of_rh.tex:2953-2969` (`cor:extracted-odd-jet-core-localization`)
- `paper/proof_of_rh.tex:3984-4190` (surviving-expansion and finite-core localization for `\Xi_\zeta^{(N)}`)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-120`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:90-124`

Dependencies

- A precise statement of the reduced-germ theorem, including what data are remembered and the exact diagonal value at coincidence.
- For Bottleneck B: enough package regularity to identify the actual corrected cubic/quintic defects as functions of the descended reduced package on the involutive fixed-shear branch.
- For Bottleneck D: either a proof that forgotten raw-package directions are `\Phi_K`-invisible through the first surviving odd order, or an enlarged reduced package retaining the minimal extra visible scalar.

Strongest objection

The phrase “reduced-germ theorem” is doing two different jobs unless stated sharply: diagonal merger on the fixed-shear branch, and fiber control for the `\Phi_K`-visible hidden directions. The first is enough for B, but the second is stronger and is exactly where D still fails on the present draft. So one cannot honestly say “reduced-germ theorem closes D” unless the theorem already includes the extra hidden-state control.

Needed for promotion

1. State the reduced-germ theorem with an explicit diagonal-merger clause at coincidence.
2. Show that on the fixed-shear involutive branch the actual corrected cubic/quintic defects factor through that reduced package, so Proposition `prop:conditional-state-local-defect-closure-fixed-shear-corner` or Corollary `cor:stronger-state-local-package-collapse-fixed-shear-corner` applies verbatim.
3. Separate the hidden extraction consequence into two bins: either prove `H_{\mathrm{core}}=\mathfrak H(\mathcal P_{\mathrm{red}})` / first-surviving-jet constancy on reduced-package fibers, or explicitly enlarge the reduced package by the minimal extra `\Phi_K`-visible scalar and prove constancy there.

Honest verdict: a clean reduced-germ theorem would likely close Bottleneck B immediately, but for Bottleneck D it only sharpens the problem to the exact hidden-state lemma unless the theorem is strengthened to retain the remaining `\Phi_K`-visible scalar.
