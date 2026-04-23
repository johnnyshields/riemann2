## Claim

On the patch `\{c\neq 0, v_5\neq 0\}`, the enlarged candidate
\[
\widetilde\Psi_{\min}=(x,Y,S,T),\qquad x=\frac{v_5}{c},\ Y=\frac{u_5}{c},\ S=\frac{\Delta_7}{cv_5},\ T=\frac{v_7}{c},
\]
contains exactly the amplitude-invariant septic package and no higher odd-order data. Indeed
\[
\frac{u_7}{c}=S+\frac{YT}{x},
\]
so a fiber of `\widetilde\Psi_{\min}` is exactly a fiber of the normalized fixed-sector `7`-jet
\[
\left(\frac{u_5}{c},\frac{v_5}{c},\frac{u_7}{c},\frac{v_7}{c}\right).
\]
Therefore the desired Bottleneck D statement
"the first surviving odd jet, equivalently the first nonzero `\Xi_{\zeta,\le H}^{(N)}`, is constant on fibers of `\widetilde\Psi_{\min}`"
is equivalent to a finite-determination theorem saying that the first surviving odd jet of `H_m` is determined by this amplitude-invariant septic package.

The present draft does not prove that finite-determination statement. So the exact theorem is still open; the sharp obstruction is that `\widetilde\Psi_{\min}` records only normalized order-`7` data, while the finite-core branch is formulated in terms of the first nonzero odd jet of `H_m` with no proved bound forcing that jet to occur by order `7`.

## Status

open

## Evidence

- From the fixed-sector definitions,
  \[
  A_5^{\mathfrak f}=u_5 I+v_5 S,\qquad A_7^{\mathfrak f}=u_7 I+v_7 S,\qquad \Delta_7=u_7v_5-u_5v_7.
  \]
- On `v_5\neq 0`, the overlap coordinates are
  \[
  x=\frac{v_5}{c},\qquad Y=\frac{u_5}{c},\qquad S=\frac{\Delta_7}{cv_5}.
  \]
  Adding `T=v_7/c` gives
  \[
  S=\frac{u_7}{c}-\frac{u_5}{c}\frac{v_7/c}{v_5/c}=\frac{u_7}{c}-\frac{YT}{x},
  \]
  hence `u_7/c=S+YT/x`. So `\widetilde\Psi_{\min}` is equivalent to the normalized septic package.
- The zeta-side extractor is already complete: `H_m` has an odd expansion, `\Xi_\zeta^{(N)}` isolates the first surviving coefficient `c_{2N-1}`, and `\Xi_{\zeta,\le H}^{(N)}` localizes this to a finite core.
- But the finite-core branch is explicitly stated only in terms of the first nonzero odd jet of the corrected transverse scalar, not in terms of order-`7` package data. The draft says the first odd coefficient may cancel while a genuine anomaly survives at a higher odd order, and does not prove any upper bound placing the first surviving order at `\le 7`.

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` (`H_m` definition and odd expansion)
- `paper/proof_of_rh.tex:3984-4190` (`\Xi_\zeta^{(N)}` exact surviving expansion and finite-core localization)
- `paper/proof_of_rh.tex:7004-7062` (fixed-sector quintic/septic package and `\Delta_7`)
- `paper/proof_of_rh.tex:7065-7191` (septic gauge law and gauge invariance of `\Delta_7`)
- `paper/proof_of_rh.tex:7892-7974` (quotient-septic closure)
- `paper/proof_of_rh.tex:11368-11513` (amplitude-invariant strengthened datum `\widehat\Psi` and strengthened two-pair coincidence)
- `paper/proof_of_rh.tex:20853-21082` (overlap coordinates `x,Y,S` and secant-shadow package)
- `paper/proof_of_rh.tex:21142-21217` (same-tower closure for current explicit overlap/canonical package)
- `paper/proof_of_rh.tex:5604-5643` (`rem:wip-pairlike-finitecore`)
- `paper/proof_of_rh.tex:26369-26398` (`rem:wip-final-endgame-status`)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:56-126`

## Dependencies

- A hidden-state / finite-determination lemma: equal `\widetilde\Psi_{\min}` fibers force agreement of the corrected block modulo `\Phi_K`-invisible directions through the first surviving odd order.
- Or a theorem bounding the first surviving odd order by `7` (equivalently `N\le 4`) on the finite-core branch.
- Or a stronger package theorem showing that all higher-order fiber directions above the normalized septic package are `\Phi_K`-invisible through the first surviving odd order.

## Strongest objection

This is a sharp obstruction, not a counterexample. I did not construct two actual finite cores in the same `\widetilde\Psi_{\min}` fiber with different first surviving odd jets. So the report rules out promotion of the theorem from the present draft, but it does not prove the theorem false.

## Needed for promotion

1. Prove a finite-determination theorem: the first surviving odd jet of `H_m` depends only on the normalized septic package, equivalently on `\widetilde\Psi_{\min}`.
2. Or prove a uniform bound `N\le 4` for the finite-core branch.
3. Or prove that every higher-order variation inside a `\widetilde\Psi_{\min}` fiber is `\Phi_K`-invisible through the first surviving odd order.

Honest verdict: `\widetilde\Psi_{\min}` is the normalized fixed-sector `7`-jet in disguise. That makes it a clean diagnostic package, but not yet a theorem-level Bottleneck D object. The exact missing step is finite determination of the first surviving odd jet from this septic package, or an equivalent hidden-state lemma.
