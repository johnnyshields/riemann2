Claim

The manuscript safely supports an algebraic strip-edge kernel lemma and a conditional summed-tail theorem, but not a standalone theorem identifying the full scalar or phase derivative with an unqualified global completed-function zero sum. The strongest safe export is a note whose main theorem is: for each strip zero \(\rho=\beta+i\gamma\) with \(0\le \beta\le 1\),
\[
K_\rho(t):=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)
=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}>0,
\]
and, conditional on an explicit convergence / regularization package, finite local blocks and omitted-zero tails built from these kernels admit the stated positivity and curvature bounds. From the present manuscript formulas alone, one should not export a theorem saying that \(q\) itself already has a fully normalized completed-log-derivative realization, nor that an arbitrary regularized full zero sum can be differentiated termwise without hypotheses.

Status

open

Evidence

Proved.

1. The single-zero kernel identity is immediate from the displayed formula
\[
f_{\beta,\gamma}(t)=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}
=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right).
\]
For \(0\le \beta\le 1\), both summands are nonnegative, so every individual strip zero contributes a positive strip-edge kernel.

2. The tail-curvature argument is also genuinely supported once stated with its local hypotheses. The manuscript defines
\[
T_{\far}(t)=\sum_{\rho\notin\mathcal L} f_{\beta_\rho,\gamma_\rho}(t)
\]
and proves the shell estimate
\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-4}\ll Q/R^3,
\qquad
S_2\le \|B_{\Aut}''\|_{L^\infty(I)}+48\sum_{\rho\notin\mathcal L}\Delta_\rho^{-4}.
\]
This is the correct consequence of summing the second-derivative bounds for the individual kernels over omitted shells.

3. The manuscript also uses the positive scalar only at the strip-edge-difference level in the local block package:
\[
\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma).
\]
That local value-channel decomposition is safe once \(S(m)\) is supplied by the positive kernel formula.

Conditional on hypotheses.

4. Proposition 3.13 only gives holomorphy and termwise differentiation of the omitted-zero sums under an explicit hypothesis: the corresponding real-line shell sums must converge. So the summed theorem is not unconditional even on the zeta side; it depends on shell convergence, denominator comparability on \(|s|<\rho_0/Q\), and the needed derivative order.

5. The global formula
\[
S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
\]
is safe as an absolutely convergent strip-edge difference because each term decays like \(|2m-\gamma|^{-2}\) after the cancellation between the two strip edges. But the stronger source reading,
\[
q(t)=B_\zeta(t)+S(t)
\]
as an exact completed-log-derivative decomposition, still needs a theorem fixing the normalization in \(t\), the background bookkeeping, multiplicities, and the regularization of the underlying pole sums. The manuscript states this split and uses it, but the quoted strip-edge formulas do not by themselves prove that source theorem.

Missing.

6. The strongest theorem actually supported by the cited formulas is therefore not a family-level or source-level realization theorem. It is:
   safe theorem: a positive single-zero strip-edge kernel lemma, plus a conditional theorem for finite local blocks and omitted-zero tails under stated shell-convergence and differentiation hypotheses.

7. Hypotheses still needed for any standalone note are: zeros summed with multiplicity; shell counting near height \(m\); absolute convergence of the strip-edge difference or an equivalent regularization theorem; termwise differentiation up to the derivative order used; denominator comparability away from the strip-edge poles on the microscopic disk; and, if one wants a source identity for \(q\), exact background terms including gamma, pole, trivial-zero, and Hadamard-constant contributions.

8. Safe export into `grh/paper` is a note titled around `positive strip-edge zero kernel` or `strip-edge kernel identity for background-subtracted zero sums`. Its abstract can safely claim: the manuscript formulas isolate a positive kernel attached to each strip zero; omitted-zero tails satisfy the displayed curvature bounds under explicit shell-convergence hypotheses; and this sharpens the object-selection problem for later GRH-family work. It should not claim any Dirichlet, tau, family-realization, or completed-function portability theorem.

9. Phrases needing scoped weakening:
   `write the zeta/scattering phase derivative as q(t)=B_\zeta(t)+S(t)` should become `treat q(t) as decomposed into B_\zeta(t)+S(t), conditional on the source decomposition theorem` unless that theorem is supplied.
   `S is the background-subtracted zero contribution` should become `S is the background-subtracted strip-edge zero contribution at the level of the displayed kernel formulas`.
   `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` should become `S(m)` is represented by an absolutely convergent strip-edge kernel sum, or by a difference of regularized edge-evaluations, depending on the chosen source theorem.
   `the zeta/scattering phase derivative` should become `the phase derivative in the current manuscript normalization` unless the completed-function identification is written out.

10. Honest verdict: the paper has a solid positive strip-edge kernel formula and a usable conditional tail package. It does not yet have, from these formulas alone, the stronger global theorem that the surrounding prose sometimes suggests.

Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299` for the asserted split `q(t)=B_\zeta(t)+S(t)`, the definition `S(m):=q_\zeta(m)-B_\zeta(m)`, and the dependence of `L(m)` on `1/S(m)`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-396` for the omitted-zero tail, the explicit kernel `f_{\beta,\gamma}`, the shell decomposition, and the curvature bound driven by `\sum \Delta_\rho^{-4}`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946` for the exact conditional hypothesis: differentiated omitted-zero sums converge uniformly on the microscopic disk provided the corresponding real-line shell sums converge.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1565` for the safe local use `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364` for the global kernel formula `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` and the crude bound `S(m)\ll Q^2`.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:6-18,28-38,49-59` for the matching conservative reading: positive strip-edge kernel yes, portability / realization no.
- `/mnt/c/workspace/riemann2/tasks/20260423-131531-attack-gap-strip-edge-kernel/reports/gap-strip-edge-kernel-routeA.md:3-21,65-74,92-100` for the strongest safe algebraic layer already isolated.
- `/mnt/c/workspace/riemann2/tasks/20260423-131531-attack-gap-strip-edge-kernel/reports/gap-strip-edge-kernel-routeB.md:3-31,66-80,101-111` for the key adversarial distinction between finite sums, strip-edge-difference sums, and conditionally regularized source sums.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44` for the required proved / conditional / missing separation and 7-field schema.

Dependencies

- Single-zero positivity depends only on the strip hypothesis \(0\le \Re\rho\le 1\).
- Tail curvature depends on shell counting, the omitted-zero separation condition \(\Delta_\rho>R\), and termwise differentiation justified by convergent shell sums.
- Any holomorphic-in-\(s\) formulation depends on denominator comparability on the microscopic disk.
- Any source-level theorem for `q` depends on a full completed-function derivation with exact normalization, background bookkeeping, and regularization conventions.

Strongest objection

The manuscript currently slides between three non-equivalent objects: finite local zero sums, the absolutely convergent strip-edge difference kernel, and underlying completed-log-derivative pole sums that require regularization. The positive-kernel formulas justify the second object. They do not by themselves justify the third. So any theorem statement or prose that reads as if the source identity for `q` is already proved is stronger than the displayed formulas support.

Needed for promotion

1. State a standalone lemma for the single-zero strip-edge kernel identity and positivity.
2. State a separate summed theorem with all hypotheses explicit: multiplicities, shell convergence, derivative order, and denominator comparability.
3. If the note wants a source identity for `q`, add a theorem deriving it from the completed object with full gamma / pole / trivial-zero / Hadamard bookkeeping and the exact `t` normalization.
4. Scope every use of `background-subtracted zero contribution`, `zeta/scattering phase derivative`, and `global zero sum` to the strip-edge-difference level unless item 3 is supplied.
5. Honest verdict: safe export is a conservative strip-edge kernel note. The stronger completed-function reading remains conditional on a missing source theorem.
