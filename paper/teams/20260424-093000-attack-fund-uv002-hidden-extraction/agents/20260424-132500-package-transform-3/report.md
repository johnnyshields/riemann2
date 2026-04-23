## Claim

The cleanest next theorem form for Bottleneck D is a transform-level factorization, not a coefficient-level one:

Let `\mathcal P_{\le H}^{\corr}` denote the corrected finite-core coincidence package at depth `H`, taken modulo directions whose contribution to the corrected block is `\Phi_K`-invisible through the relevant odd order. Then for each `N\ge 1` there should exist a scalar functional
\[
\mathfrak T_{N,H}
\]
on these package fibers such that
\[
\Xi_{\zeta,\le H}^{(N)}(m)=\mathfrak T_{N,H}\bigl(\mathcal P_{\le H}^{\corr}(m)\bigr).
\]
Equivalently, equal corrected coincidence packages modulo `\Phi_K`-invisible directions force equality of `\Xi_{\zeta,\le H}^{(N)}`.

In this form the first surviving odd order is recovered as
\[
N_*(m):=\min\{N\ge 1:\mathfrak T_{N,H}(\mathcal P_{\le H}^{\corr}(m))\neq 0\},
\]
and, by the already-proved surviving-expansion and finite-core localization, `N_*(m)` is exactly the index of the first nonzero odd jet of `H_m`, with leading coefficient determined by the same package fiber.

This is one step sharper than the current slogan "package control determines the first surviving odd coefficient of `H_m`": it pins the bridge to the already-canonical transformed scalar `\Xi_{\zeta,\le H}^{(N)}` and makes the hidden-state issue exactly the quotient by `\Phi_K`-invisible directions.

## Status

heuristic

## Evidence

- The zeta-side extractor is already complete: `H_m` has an odd microscopic expansion, `\Xi_\zeta^{(N)}` has an exact surviving-coefficient expansion, and `\Xi_{\zeta,\le H}^{(N)}` is already localized to a fixed finite core up to exponentially small error.
- The draft already reformulates the finite-core problem in two stages: first obtain defect-corrected coincidence information for `\widehat\Psi`, then convert that information into the downstream endgame. Bottleneck D is exactly the missing second-stage conversion.
- Current team convergence further sharpens that the missing issue is not to invent a better reduced coordinate tuple, but to prove that quotienting the corrected package down to the usable coincidence state discards only `\Phi_K`-invisible directions through the first surviving odd order.
- Therefore the theorem target should be stated directly on `\Xi_{\zeta,\le H}^{(N)}`. Once such factorization exists, the already-written surviving-expansion machinery recovers the first surviving odd coefficient `c_{2N-1}(m)` formally.

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` (`H_m` definition and odd expansion)
- `paper/proof_of_rh.tex:3857-4190` (`\Xi_\zeta^{(N)}` exact surviving expansion and finite-core localization)
- `paper/proof_of_rh.tex:11368-11513` (`\widehat\Psi` and exact strengthened two-pair coincidence)
- `paper/proof_of_rh.tex:12586-12610` (two-stage finite-core reformulation)
- `paper/proof_of_rh.tex:5604-5643` (pair-like versus finite-core fork)
- `paper/proof_of_rh.tex:26369-26398` (current endgame status remark)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:64-144`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:117-124`
- `paper/tasks/20260424-090000-other-uv002-fundamental/reports/coordinator-current-convergence.md:21-28,50-63`

## Dependencies

- Bottleneck C in its exact current form: corrected reduced-package diagonal collapse / coincidence theorem strong enough to define the corrected coincidence package canonically.
- A hidden-state lemma: passing from the raw corrected finite-core package to the coincidence package forgets only `\Phi_K`-invisible directions through the first surviving odd order.
- Enough package functoriality to compare two finite cores on the same corrected coincidence fiber.

## Strongest objection

The notation for the corrected finite-core coincidence package is not yet frozen in the paper. Writing `\mathcal P_{\le H}^{\corr}` is theorem-shaping shorthand, not existing canonical notation. More seriously, the present draft does not yet prove that the residual hidden fiber is exactly `\Phi_K`-invisible through the relevant odd order; that is the core missing theorem, not a bookkeeping detail.

## Needed for promotion

1. Fix the canonical package object after Bottleneck C: the corrected coincidence package whose fiber relation is actually used in the theorem.
2. Prove equality of package fibers implies equality of the corrected block modulo `\Phi_K`-invisible directions through odd order `2N-1`.
3. Deduce transform-level factorization `\Xi_{\zeta,\le H}^{(N)}=\mathfrak T_{N,H}(\mathcal P_{\le H}^{\corr})`.
4. State the corollary that the minimal nonzero `\mathfrak T_{N,H}` recovers the first surviving odd jet of `H_m`.

Honest verdict: the theorem is now sharpest at the transform level. The package-to-`H_m` slogan should be replaced by package-to-`\Xi_{\zeta,\le H}^{(N)}` factorization modulo `\Phi_K`-invisible directions; the remaining gap is the hidden-state lemma that justifies that quotient.
