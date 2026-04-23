## Claim

The smallest plausible Bottleneck D package enlargement is the reduced package together with one extra `\Phi_K`-visible septic scalar. On a `\{c\neq 0,\ v_5\neq 0\}` patch, write

\[
\widetilde\Psi_{\min}(h):=\Bigl(x(h),Y(h),S(h),T(h)\Bigr)
=\left(\frac{v_5}{c},\frac{u_5}{c},\frac{\Delta_7}{c\,v_5},\frac{v_7}{c}\right),
\]

equivalently `\widetilde\Psi_{\min}=(\widehat\Psi,T)` with `T=\Phi_K(A_7^{\mathfrak f})/2c`. The smallest theorem candidate is:

> If two finite-core corrected package germs have the same enlarged package germ `\widetilde\Psi_{\min}` at coincidence, then their corrected transverse scalars have the same first surviving odd order and the same leading odd coefficient. Equivalently, for each finite core the first nonzero `\Xi_{\zeta,\le H}^{(N)}` is determined by `\widetilde\Psi_{\min}`.

On the same patch this datum also determines the normalized septic pair, since

\[
\frac{u_7}{c}=Y\,\frac{v_7}{v_5}+S = \frac{YT+\Delta_7/c^2}{x}.
\]

So reduced `\widehat\Psi` plus the single extra scalar `T=v_7/c` is the smallest evident enlargement that restores the hidden raw septic direction seen by `\Phi_K`.

## Status

heuristic

## Evidence

- The extractor side is already complete: once a package-side factorization determines the first surviving odd jet, the existing `H_m` and `\Xi_\zeta^{(N)}` machinery applies immediately.
- Reduced `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` forgets the septic gauge fiber `A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}`.
- Along that fiber, `\Delta_7` is unchanged but `v_7/c` changes by `\chi\,v_5/c=\chi x`, so reduced `\widehat\Psi` alone cannot see the first `\Phi_K`-visible motion.
- Because `\Phi_K(X)=x_{12}+x_{21}`, the fixed-sector `S` coefficient is the visible channel; for `A_5^{\mathfrak f}=u_5I+v_5S` and `A_7^{\mathfrak f}=u_7I+v_7S`, the visible scalar is exactly `v_7` up to the fixed factor `2`.
- Once `T=v_7/c` is added, the raw normalized septic pair `(u_7/c,v_7/c)` is recovered from `(x,Y,S,T)`, so no smaller missing septic datum remains at this order on a `v_5\neq 0` patch.

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` (`H_m` definition and odd expansion)
- `paper/proof_of_rh.tex:2953-2969` (finite-core localization of the extracted odd jet)
- `paper/proof_of_rh.tex:3984-4190` (`\Xi_\zeta^{(N)}` surviving-expansion and finite-core localization)
- `paper/proof_of_rh.tex:7004-7062` (definitions of `A_5^{\mathfrak f}`, `A_7^{\mathfrak f}`, `\Delta_7`)
- `paper/proof_of_rh.tex:7065-7191` (septic gauge law and `\Delta_7` gauge invariance)
- `paper/proof_of_rh.tex:20853-20963` (overlap-patch variables `x,Y,S`)
- `paper/proof_of_rh.tex:24987-25004` (current strengthened invariant `\widehat\Psi`)
- `paper/proof_of_rh.tex:26390-26397` (raw order-7 ambiguity inside `A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}`)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-104`

## Dependencies

- A package-to-jet theorem showing that equal enlarged-package fibers force agreement of the corrected block modulo `\ker\Phi_K` through the first surviving odd order.
- The package/coincidence front for the actual corrected two-atom package.
- Restriction to a patch where `c\neq 0` and `v_5\neq 0`, so `x,Y,S,T` are defined.

## Strongest objection

`T=v_7/c` is not gauge invariant under the septic shift `A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}`; it is only a raw hidden scalar in a chosen local representative. So this is the smallest plausible enlarged package on the present draft, not yet a canonical theorem statement. A fully canonical version may need either a preferred gauge or a fiberwise statement phrased directly in terms of raw representatives modulo `\ker\Phi_K` through the target odd order.

## Needed for promotion

1. Prove that the first surviving odd jet of `H_m` is constant on fibers of `\widetilde\Psi_{\min}`.
2. Rephrase that constancy canonically, either by fixing a natural septic gauge or by stating the theorem on raw package fibers modulo `\ker\Phi_K`.
3. Deduce the corresponding factorization for the first nonzero `\Xi_{\zeta,\le H}^{(N)}`.

Honest verdict: the sharp minimal extra datum is one `\Phi_K`-visible septic scalar, naturally `T=v_7/c` on a `v_5\neq 0` patch. The best current theorem candidate is constancy of the first surviving odd jet on fibers of `\widetilde\Psi_{\min}=(x,Y,S,T)`. The remaining gap is canonicity and the actual proof that this enlarged package controls the corrected block through the first surviving odd order.
