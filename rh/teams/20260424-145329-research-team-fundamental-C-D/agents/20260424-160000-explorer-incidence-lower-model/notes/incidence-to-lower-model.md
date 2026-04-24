# Incidence-to-lower-model scratch

## Harness

Team dir: `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D`.
Task: mine finite-core incidence geometry and positive-kernel sections for a direct route from `\widehat\Psi`-side incidence constraints to weighted-average/direct-`\Xi` lower control. Ground truth: candidate `E_2` theorem sufficient for contradiction, or obstruction showing incidence alone lacks sign/no-cancellation control.

## Read inputs

- `findings.md` lines 119--132: finite-core lower-model transfer theorem E is open; lower model should control `\Xi_{\core}^{(N)}` or one-sided `H_{\core}^{(2N-1)}`.
- `collation.md` lines 138--142 and 95--104: E split into `E_1` descent and `E_2` weighted-average/direct-`\Xi` lower control; bare coefficient nonvanishing is insufficient.
- `agents/20260424-145500-gap-closer-UV002-contradiction/report.md` lines 11--56: weighted-average/direct-`\Xi` theorem is minimal; coefficient theorem needs tail domination/no-cancellation.
- `proof_of_rh.tex:3583--3609`: positive kernel `\kappa_N\ge0`, strictly positive on `(0,N)`.
- `proof_of_rh.tex:3650--3687`: sign transfer from one-sided control of `F^{(2N-1)}`.
- `proof_of_rh.tex:3976--3996` and `4018--4036`: exact surviving coefficient tail with positive weights `h_k(1^2,\dots,N^2)`.
- `proof_of_rh.tex:12676--12979`: defect-free incidence gives affine dependence of `\Xi(h_j)` or `Q_v(h_j)`, reducing bad cores to `k\le4` incidence lanes.
- `proof_of_rh.tex:13933--15239`: incidence lanes imply derivative-geometry restrictions (`K_v=0`, `T_v=0`, zeros of `\mathcal R`) and local sterility/sign-definite exclusions.
- `proof_of_rh.tex:26369--26609`: final contradiction currently pair-like only; finite-core branch still needs first nonzero odd jet reformulation.

## Structural separation

[confirmed] The paper's positive-kernel result turns a one-sided lower bound for `\sigma H_{\core}^{(2N-1)}(s)` on `0\le s\le N/Q^2` into one-sided lower control of `\sigma(-1)^{N+1}\Xi_{\core}^{(N)}`. This is a true analytic transfer, independent of incidence geometry.

[confirmed] The incidence theorems are zero-set / affine-dependence theorems: under defect-free low-order assumptions a bad core forces affine dependence of normalized points, and shrinking / exact contacts force derivative invariants to vanish or be sign-definite sterile. These statements do not assign a sign or size to the first nonzero odd derivative of the corrected transverse scalar.

[confirmed] The exact coefficient expansion has positive universal weights but coefficients may have arbitrary signs. Thus coefficient nonvanishing or incidence nondegeneracy alone does not imply lower control for `\Xi^{(N)}` unless a no-cancellation or tail-domination statement is added.

[conditional on E1 plus a sign/variation law] If corrected finite-core data descends to one of the defect-free incidence lanes and the incidence defect controls the sign and size of `H_{\core}^{(2N-1)}` on the microscopic interval, then the positive-kernel proposition yields the desired direct lower bound.

[candidate] A sufficient `E_2` theorem should be stated not as "incidence constraints imply nonzero coefficient" but as: after choosing the first nonzero odd order `2N-1`, the incidence defect functional `\mathcal I_N` selected by the finite-core lane satisfies either a pointwise one-sided law
`\sigma H_{\core}^{(2N-1)}(s) \ge c_N \mathcal L(m)` for all `0\le s\le N/Q^2`,
or a weighted law
`\sigma \int_0^N \kappa_N(u)H_{\core}^{(2N-1)}(u/Q^2)du \ge c_N Q^{4N-2}\mathcal L(m)`,
where `\mathcal L(m)=(x(m)/B_\zeta(m))S(m)` or its finite-core replacement.

## Obstruction from incidence alone

Incidence constraints are invariant under replacing the scalar germ by a sign-reversing or high-order perturbed odd germ that preserves the same affine dependence data but changes the weighted positive-kernel average. More concretely, the data `\widehat\Psi(h_j)` and lifted incidence relations among `Q_v(h_j)` constrain only cubic/quintic/septic normalized coordinates and determinant vanishings. The later coefficients `c_{2N-1+2k}^{\core}` in the transformed scalar are not fixed by those relations in the cited statements. Since
\[
\Xi_{\core}^{(N)}=(-1)^{N+1}(2N-1)N!(N-1)!\sum_{k\ge0}c_{2N-1+2k}^{\core}h_k(1^2,\dots,N^2)Q^{-(2N+2k+2)},
\]
positive weights alone do not prevent an adversarial higher-tail cancellation. Therefore incidence alone lacks sign/no-cancellation control unless strengthened by an analytic monotonicity, variation, complete-monotonicity, or tail-domination theorem for the corrected finite-core transverse scalar.

## Candidate sufficient theorem template

Let `\mathcal C` be the genuine corrected finite core after C, D, and E1, on a good patch and in one of the `k=2,3,4` incidence lanes. Let `2N-1` be the first surviving odd order of the corrected core scalar `H_{\core}` and let `\mathcal L(m)` be the contradiction-scale lower quantity, expected `\asymp (x(m)/B_\zeta(m))S(m)`. Suppose the incidence lane supplies a nonzero normalized defect `\mathfrak D(\mathcal C)` and constants `c,\theta>0` such that either:

1. weighted sign law:
\[
\sigma\int_0^N\kappa_N(u)H_{\core}^{(2N-1)}(u/Q^2)du\ge c Q^{4N-2}\mathcal L(m);
\]
2. pointwise sign law:
\[
\sigma H_{\core}^{(2N-1)}(s)\ge c Q^{4N-2}\mathcal L(m),\quad 0\le s\le N/Q^2;
\]
3. coefficient plus tail domination:
\[
|c_{2N-1}^{\core}|\ge cQ^{2N+2}\mathcal L(m),\quad
\sum_{k\ge1}h_k|c_{2N-1+2k}^{\core}|Q^{-2k}\le \theta |c_{2N-1}^{\core}|,
\]
with coherent sign of the leading term.

Then `|\Xi_{\core}^{(N)}|\gtrsim \mathcal L(m)`, and the final contradiction can use the already-proved zeta-side exponentially small upper bound.

## Decision

Route decision: keep as obstruction / candidate theorem target. The exploration redirects E2: do not try to squeeze lower control out of incidence determinants alone. The next useful research attack is a source-level analytic sign/variation/tail-domination theorem for the corrected finite-core scalar on the microscopic interval, possibly tied to sign-definite derivative invariants (`K_v`, `T_v`, `\mathcal R`) rather than to incidence zero sets alone.
