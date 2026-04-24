# Explorer report: incidence lower model

## Claim

[confirmed] Finite-core incidence geometry in the current draft gives zero-set / affine-dependence constraints, not by itself a contradiction-scale lower bound for the first surviving odd transformed scalar.

[confirmed] The positive-kernel section gives a clean sufficient analytic target for `E_2`: weighted-average or pointwise one-sided control of `H_{\core}^{(2N-1)}` on `0\le s\le N/Q^2`, or direct lower control of `\Xi_{\core}^{(N)}`.

[candidate] A theorem sufficient for the contradiction is:

**Candidate `E_2` theorem, weighted/direct lower model.** Assume C, D, and `E_1` place the genuine corrected finite core in a defect-free affine-incidence lane on a good patch. Let `2N-1` be the first surviving odd order of the corrected finite-core transverse scalar `H_{\core}` and let
\[
\mathcal L(m)\asymp \frac{x(m)}{B_\zeta(m)}S(m)
\]
be the contradiction-scale lower quantity. Then the incidence lane must supply one of the following additional analytic controls:

1. weighted sign/lower law
\[
\sigma\int_0^N\kappa_N(u)H_{\core}^{(2N-1)}(u/Q^2)\,du
\ge c_N Q^{4N-2}\mathcal L(m);
\]
2. pointwise sign/lower law
\[
\sigma H_{\core}^{(2N-1)}(s)
\ge c_N Q^{4N-2}\mathcal L(m),
\qquad 0\le s\le N/Q^2;
\]
3. coefficient lower bound plus tail domination
\[
|c_{2N-1}^{\core}|
\ge c_N Q^{2N+2}\mathcal L(m),
\]
with coherent leading sign and
\[
\sum_{k\ge1}h_k(1^2,\dots,N^2)
|c_{2N-1+2k}^{\core}|Q^{-2k}
\le \theta |c_{2N-1}^{\core}|,
\qquad \theta<1.
\]

Under any of these, the existing positive-kernel / exact-tail formula gives
\[
|\Xi_{\core}^{(N)}(m)|\gtrsim \mathcal L(m),
\]
which is the lower input needed for the finite-core contradiction.

## Status

open

## Evidence

[confirmed] Proposition `prop:n-point-odd-positive-kernel` states that for any odd analytic germ `F`,
\[
(\mathcal P_{N,Q}F)
=
\frac{N(-1)^{N+1}}{\binom{2N-2}{N-1}}Q^{-(4N-2)}
\int_0^N\kappa_N(u)F^{(2N-1)}(u/Q^2)\,du,
\]
with `\kappa_N\ge0` and strictly positive on `(0,N)`. Corollary `cor:n-point-sign-transfer` transfers one-sided sign on `F^{(2N-1)}` over the microscopic interval to the sign of the `N`-point scalar. Thus weighted or pointwise one-sided lower control is sufficient without further incidence input.

[confirmed] Proposition `prop:corrected-n-point` and Remark `rem:xi-zeta-exact-surviving-expansion` give the exact surviving coefficient expansion
\[
\Xi_\zeta^{(N)}(m)=(-1)^{N+1}(2N-1)N!(N-1)!
\sum_{k\ge0}c_{2N-1+2k}(m)h_k(1^2,\dots,N^2)Q^{-(2N+2k+2)}.
\]
The weights `h_k(1^2,\dots,N^2)` are positive complete homogeneous polynomials, so coefficient-side lower control requires no-cancellation or tail domination.

[confirmed] The defect-free finite-core incidence section proves affine dependence statements only under low-order defect-free hypotheses. Theorem `thm:defect-free-quintic-circuit-reduction` turns cubic/quintic vanishing into affine dependence of `\Xi(h_j)`. Proposition `prop:defect-free-lifted-affine-dependence-vpatch` turns cubic/quintic/septic defect-free vanishing into affine dependence of lifted points `Q_v(h_j)`. The nearby corollaries reduce minimal bad cores to coincidence/collinearity/coplanarity for `k=2,3,4`.

[confirmed] The lifted incidence geometry then controls where exact incidence can happen: shrinking lifted triples concentrate into `K_v=0`, shrinking lifted quadruples into `T_v=0`, and nonmixed exact tangent-plane contacts force zeros of `\mathcal R`. These are exclusion / zero-forcing statements. They do not provide a sign or lower size for `H_{\core}^{(2N-1)}`.

[confirmed] `rem:minimal-core-reformulation` explicitly says the finite-core endgame is two-stage: extract defect-corrected coincidence information for `\widehat\Psi`, then convert it into affine-line incidence constraints for `\Gamma`. The statement stops before any weighted-average lower law.

[conditional on C, D, and E1] If corrected package data descends to the defect-free affine-incidence lanes, the remaining `E_2` obligation is analytic: tie the incidence defect to sign/variation/tail domination of the corrected finite-core transverse scalar on the microscopic interval.

## Baseline / delta

Baseline from `agents/20260424-145500-gap-closer-UV002-contradiction/report.md`: after C and D, the finite-core branch needs `E_1` descent to affine-incidence lanes and `E_2` weighted-average/direct-`\Xi` lower control; bare coefficient nonvanishing is insufficient.

Delta: this exploration sharpens the reason `E_2` is independent of incidence alone. The incidence theorems constrain finite configurations and derivative zero sets, while the positive-kernel lower bound needs sign/size of a scalar germ over a microscopic interval or a tail-domination theorem. Therefore a direct route from `\widehat\Psi` incidence to `\Xi` lower control must include a no-cancellation/sign/variation bridge; determinant incidence alone is not enough.

## Attempt status

keep

## Exact refs

- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md:119-132` — finite-core lower-model transfer E is open and should control `\Xi_{\core}^{(N)}` or `H_{\core}^{(2N-1)}`.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:95-104` — current frontier splits E into `E_1` incidence descent and `E_2` lower transfer; no-cancellation warning.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-UV002-contradiction/report.md:11-56` — prior exact weighted-average/direct-`\Xi` theorem templates and tail-domination obstruction.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3583-3609` — positive kernel `\kappa_N` and `N`-point representation.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3650-3687` — sign transfer and downstream target remark.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3976-3996` and `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:4018-4036` — exact surviving coefficient tail.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11368-11450` — `\widehat\Psi` definition and projective/amplitude normalization distinction.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12586-12610` — minimal-core two-stage reformulation.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12669-12979` — defect-free affine-dependence theorems and lifted `k\le4` incidence lanes.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:13933-15239` — osculating determinant, lifted `3`-point / `4`-point concentration, and nonmixed `\mathcal R` zero-forcing / sterility.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26369-26609` — final endgame remains pair-like; finite-core first-nonzero-odd-jet reformulation open.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-explorer-incidence-lower-model/notes/incidence-to-lower-model.md` — scratch synthesis for this report.

## Dependencies

- C: corrected reduced-package diagonal-collapse / collision-functoriality.
- D: transform-level hidden-state theorem modulo `\ker\Phi_K`, identifying the first surviving odd transform from corrected package fibers.
- `E_1`: descent from genuine corrected finite-core data to the defect-free affine-incidence lanes.
- A new analytic `E_2` ingredient: weighted sign law, pointwise sign law, direct `\Xi` lower law, variation control, or coefficient tail domination for the corrected finite-core scalar.
- Existing zeta-side `N`-point positive-kernel and finite-core localization machinery.

## Strongest objection

The candidate `E_2` theorem is sufficient but not proved, and it may be almost as hard as the original finite-core lower-model problem. The current incidence results are compatible with an adversarial higher odd tail: the same `\widehat\Psi` incidence data and lifted determinant vanishings can leave the later coefficients `c_{2N-1+2k}^{\core}` uncontrolled. Since all universal tail weights in `\Xi^{(N)}` are positive, higher coefficients with alternating signs can cancel the first surviving coefficient unless an additional sign, variation, complete-monotonicity, or tail-domination principle is proved from source structure. Thus incidence alone cannot be promoted to direct lower control.

## Needed for promotion

1. Prove C and D, or explicitly condition the theorem on them.
2. Prove `E_1`: genuine corrected finite-core data satisfies the low-order defect-free hypotheses needed to enter the `k=2,3,4` affine-incidence lanes.
3. Prove a genuine analytic bridge from the selected incidence lane to one of the sufficient `E_2` controls: weighted lower law, pointwise one-sided lower law, direct `\Xi` lower law, or coefficient lower bound plus tail domination.
4. Verify scaling of the lower quantity `\mathcal L(m)` against the final contradiction scale and the existing zeta-side upper bound.
5. Adversarially test whether the proposed sign/tail theorem survives hidden-state freedom and corrected multi-pair interactions above septic order.

## Honest verdict

[confirmed] The positive-kernel machinery already gives the exact form of a sufficient lower theorem. [confirmed] The finite-core incidence geometry does not by itself provide that theorem; it gives affine dependence and derivative zero-forcing/exclusion. [candidate] The best `E_2` target is therefore a sign/no-cancellation bridge attached to the incidence lane, not another determinant-incidence statement. Incidence alone lacks sign and tail control.

## Autoresearch next step

continue: attack the analytic bridge behind `E_2`: search for a source-structure reason that `H_{\core}^{(2N-1)}` has one-sided sign/variation control on `0\le s\le N/Q^2` once the core lies in a specific `k=2,3,4` incidence lane; alternatively prove a finite tail-domination estimate for the corrected finite-core scalar.

verify: adversarially construct or rule out two corrected finite-core scalar germs with the same `\widehat\Psi`/lifted incidence data but opposite or cancelling `\Xi^{(N)}` weighted averages.

blocked: no coordinator action needed.

terminal: not terminal; this is a structural obstruction plus candidate theorem shape, not a closure of E.
