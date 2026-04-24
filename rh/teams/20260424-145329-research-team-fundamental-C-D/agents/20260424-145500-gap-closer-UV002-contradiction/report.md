Claim

Assuming Bottleneck C and Bottleneck D in their current sharp forms, the finite-core contradiction for `UV-002` reduces to one smallest new theorem: a **finite-core lower-model transfer theorem** replacing the pair-like toy estimate in the current final contradiction theorem.

More precisely, the present pair-like endgame uses
\[
\Xi_{\toy}^{(N)}(u,d)=u^2\Phi_K(M(d))+O(u^4)
\]
and then calibrates `u^2 \asymp (x/B_\zeta(m))S(m)` to obtain a lower bound of size `\asymp (x/B_\zeta(m))S(m)`. For the genuine finite-core branch, the smallest replacement is not a new package theorem between C and D. It is a lower theorem on the first surviving odd finite-core channel.

The cleanest exact formulation is the following weighted-average theorem:

**Finite-core weighted-derivative transfer theorem.** If the actual same-scale core has first surviving odd order `2N-1`, and if C and D identify the corrected coincidence package fiber and its first nonzero transformed scalar, then there exists `\sigma\in\{\pm1\}` such that
\[
\sigma\int_0^N \kappa_N(u)
H_{\core}^{(2N-1)}\!\left(\frac{u}{Q^2}\right)du
\ge c_N\,Q^{4N-2}\,\frac{x(m)}{B_\zeta(m)}S(m),
\]
with `c_N>0` depending only on the finite-core package fiber and the fixed `N`-point kernel. By Proposition `prop:n-point-odd-positive-kernel`, this is exactly the lower-input needed to force
\[
|\Xi_{\core}^{(N)}(m)|\gtrsim \frac{x(m)}{B_\zeta(m)}S(m).
\]

A stronger but easier-to-state sufficient theorem is the pointwise version
\[
\sigma\,H_{\core}^{(2N-1)}(s)
\ge c_N\,Q^{4N-2}\,\frac{x(m)}{B_\zeta(m)}S(m)
\qquad
\left(0\le s\le \frac{N}{Q^2}\right),
\]
which implies the weighted-average statement because `\kappa_N\ge 0` and is strictly positive on `(0,N)`.

A direct transformed-scalar formulation is equivalent:
\[
|\Xi_{\core}^{(N)}(m)|\gtrsim \frac{x(m)}{B_\zeta(m)}S(m),
\]
with sign determined by the corrected package fiber.

There is also a coefficient-side route, but it is not equivalent by itself. Writing
\[
H_{\core}(z/Q^2)=\sum_{r\ge 0} c_{2r+1}^{\core}(m)\frac{z^{2r+1}}{Q^{2r+4}},
\]
a lower bound on the first surviving coefficient
\[
|c_{2N-1}^{\core}(m)|\gtrsim Q^{2N+2}\,\frac{x(m)}{B_\zeta(m)}S(m)
\]
is only sufficient together with a tail-domination statement such as
\[
\sum_{k\ge 1} h_k(1^2,\dots,N^2)
\bigl|c_{2N-1+2k}^{\core}(m)\bigr|Q^{-2k}
\le \theta\,\bigl|c_{2N-1}^{\core}(m)\bigr|
\qquad (\theta<1),
\]
or any equivalent sign/variation control preventing cancellation in the exact surviving expansion for `\Xi^{(N)}`. Without such extra control, the coefficient statement alone does not force a lower bound for `\Xi_{\core}^{(N)}`.

So the truly minimal new theorem is weighted-average/direct-`\Xi` control, not bare leading-coefficient nonvanishing.

The cleanest current stack is slightly more structured than my previous reduction:

1. **C**: corrected reduced-package diagonal-collapse / collision-functoriality
   \[
   \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
   \]
2. **D**: corrected package fibers determine the first surviving odd order and leading transformed scalar, equivalently constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers modulo `\ker\Phi_K`.
3. **E\(_1\)**: convert the resulting defect-corrected coincidence information for `\widehat\Psi` into the affine-incidence constraints singled out by `rem:minimal-core-reformulation`.
4. **E\(_2\)**: from those incidence constraints, derive weighted-average / direct-`\Xi` lower control for the first surviving odd finite-core channel.

The new point from the draft is that `E\(_1\)` is not vague. In the defect-free finite-core model, bad finite cores already force affine dependence of the normalized quintic or lifted septic points. Concretely, if the multi-pair interaction contributes nothing through the relevant low orders, then a bad core forces affine dependence of
\[
\Xi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)}\right)
\]
and, on a good `v_5`-patch, affine dependence of
\[
Q_v(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)v_5(h)}\right).
\]
So the exact downstream geometric target is: prove enough corrected finite-core defect-vanishing / descent to place the genuine bad core into the already-developed `k=2,3,4` affine-incidence lanes.

Thus `UV-007` is still the in-paper placeholder for the post-pair-like rewrite, but that rewrite is not a single formal sentence after D. The draft itself points to a two-stage finite-core reformulation: first `\widehat\Psi`-side coincidence, then affine-incidence control, then the analytic weighted-average/direct-`\Xi` lower law.
Status

open

Evidence

The current final contradiction theorem is structurally a comparison between a lower model on the anomaly side and an exponentially small upper bound on the zeta side. On the zeta side, the machinery is already fully general in `N`: the `N`-point operator isolates the first surviving odd coefficient, admits a positive-kernel representation in terms of the first surviving derivative, and localizes the transformed scalar to a fixed finite core. So the zeta side is already written in the right finite-core language.

What remains pair-like is only the lower side. The current proof inserts the toy expansion `\Xi_{\toy}^{(N)}(u,d)=u^2\Phi_K(M(d))+O(u^4)` and the calibration theorem producing `u^2\asymp (x/B_\zeta)S(m)`. That is exactly where the argument still assumes first-odd-jet nondegeneracy of a pair-core normal form. The paper itself says so in `rem:wip-pairlike-finitecore` and `rem:wip-final-endgame-status`.

The positive-kernel representation sharpens the missing target. For any odd analytic germ `F`, the `N`-point scalar is a positive average of `F^{(2N-1)}` over the microscopic interval, with exact prefactor `Q^{-(4N-2)}`. Therefore a theorem giving one-sided lower control of the actual finite-core corrected scalar at the first surviving odd order transfers directly to a contradiction-driving lower bound for `\Xi^{(N)}` once it is stated at the correct scale. This means the smallest replacement for the pair-like toy theorem is not a full new toy model from scratch; it is enough to prove weighted-average control of the first surviving derivative, or any equivalent direct lower law for `\Xi_{\core}^{(N)}`.

The coefficient expansion gives a useful sufficient variant but also exposes a hidden obstruction. The exact surviving formula
\[
\Xi_{\core}^{(N)}(m)
=
(-1)^{N+1}(2N-1)N!(N-1)!
\sum_{k\ge 0}
c_{2N-1+2k}^{\core}(m)
h_k(1^2,\dots,N^2)
Q^{-(2N+2k+2)}
\]
has a universal positive tail weight `h_k(1^2,\dots,N^2)>0`, but the coefficients `c_{2N-1+2k}^{\core}(m)` need not share one sign. So bare lower control of `c_{2N-1}^{\core}(m)` is not enough by itself: one also needs sign or tail domination to prevent cancellation by higher surviving odd jets.

C and D fit exactly into the first half of this picture. C supplies the canonical corrected coincidence package fiber. D says that on that fiber the first surviving odd order and leading transformed scalar are fixed. But the draft's own `rem:minimal-core-reformulation` adds one more structural obligation: finite-core endgame is a two-stage problem, first extracting defect-corrected coincidence information for `\widehat\Psi`, then converting that information into affine-incidence constraints. The nearby finite-core geometry sections make this more concrete: in the defect-free model, vanishing bad cores force affine dependence of `\Xi(h_j)` and, on a good `v_5`-patch, of the lifted points `Q_v(h_j)`, reducing minimal bad cores to the `k=2,3,4` coincidence/collinearity/coplanarity lanes. So after C and D, the remaining burden is not another corrected-package theorem, but a downstream descent theorem showing that the genuine corrected finite core satisfies enough low-order defect control to enter those affine-incidence lanes, and then an analytic theorem converting the resulting geometry into contradiction-scale lower control at order `2N-1`.

Separate three things:

- **proved:** the `N`-point operator isolates the first surviving odd order and has a positive-kernel formula; the zeta-side transformed scalar is finite-core localized; the current contradiction theorem works in the pair-like branch.
- **conditional on C and D:** the finite-core branch reduces to a downstream `\widehat\Psi \to` affine-incidence `\to \Xi` problem; no further corrected-package coincidence theorem appears to remain, but there is still a descent-to-incidence layer before the final lower-model transfer.
- **missing:** a theorem stack converting the genuine finite-core `\widehat\Psi` data into the same affine-dependence / coincidence / collinearity / coplanarity constraints already proved in the defect-free model, and then into either weighted-average lower control of `H_{\core}^{(2N-1)}` or direct lower control of `\Xi_{\core}^{(N)}`; bare control of the first surviving coefficient alone is still missing one extra no-cancellation input.

Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:5300-5473` — Proposition `prop:toy-n-point-direct`; current pair-like lower model.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:739-839` — canonical calibration theorem and remainder-cutoff theorem yielding `u^2\asymp (x/B_\zeta(m))S(m)` in the pair-like route.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3520-3687` — odd-projector factorization, positive-kernel representation, and sign transfer from the first surviving derivative.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3853-4190` — Proposition `prop:corrected-n-point`, exact surviving expansion, and finite-core localization of `\Xi_{\zeta,\le H}^{(N)}`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11331-11450` — definitions of `\Gamma(h)` and `\widehat\Psi(h)` and the geometric-versus-projective normalization split.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12586-12610` — `rem:minimal-core-reformulation`; downstream finite-core extraction is explicitly a two-stage `\widehat\Psi`-then-incidence problem.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12669-12979` — defect-free finite-core affine-dependence theorems reducing bad cores to affine dependence of `\Xi(h_j)` and lifted points `Q_v(h_j)`, hence to `k\le 4` coincidence/collinearity/coplanarity lanes.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:13933-15239` — osculating-determinant and lifted `3`-point / `4`-point geometry showing how affine circuits feed the existing `K_v` / `T_v` lanes.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:24985-25030` — finite-core endgame split; live burden is package-level coincidence / functoriality plus downstream reformulation.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26369-26398` — `rem:wip-final-endgame-status`; general finite-core branch still needs reformulation in terms of the first nonzero odd jet.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:5604-5643` — `rem:wip-pairlike-finitecore`; genuine finite-core branch must use the first nonzero odd jet.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26369-26398` — `rem:wip-final-endgame-status`; general finite-core branch still needs reformulation in terms of the first nonzero odd jet.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26554-26609` — current final contradiction theorem is pair-like only.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/handoff.md:164-299` — prior-cycle reduction to `C -> D -> finite-core contradiction`.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-kerphik-hidden-state/report.md:1-90` — current sharp form of D.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-143000-C-proof-obligations/report.md:1-76` and `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md:1-68` — current sharp form of C.

Dependencies

- Bottleneck C in the diagonal-specialization form `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`.
- Bottleneck D in the transform-level form: corrected package fibers force equality of first surviving odd order and leading transformed scalar modulo `\ker\Phi_K`.
- A downstream finite-core reformulation after C and D: first a descent theorem from genuine corrected finite-core data to the affine-dependence / lifted-incidence constraints already proved in the defect-free model, then a lower-model transfer theorem stated either directly for `\Xi_{\core}^{(N)}` or via weighted-average / pointwise one-sided control of `H_{\core}^{(2N-1)}` on the microscopic interval.
- The existing zeta-side `N`-point extractor, positive-kernel, and finite-core localization machinery.

Strongest objection

The reduction after C and D still leaves open what analytic object should play the role of the pair-like toy anomaly matrix `M(d)`. In the pair-like route, calibration and the toy `u^2` law are explicit. In the genuine finite-core branch, the package fiber may determine the first surviving odd order and leading transformed scalar abstractly without yet giving a usable lower model on the microscopic interval. Moreover the draft's finite-core geometry theorems are proved only under defect-free low-order hypotheses: they show what incidence statement would follow if the corrected multi-pair interaction vanished through the relevant cubic/quintic/septic orders, but they do not yet show that the genuine corrected finite core satisfies that descent. So the post-C/D burden is a real theorem stack, not just a rewriting exercise. The coefficient route is weaker than it first looks, because higher odd coefficients enter `\Xi^{(N)}` with positive universal weights and can still cancel the leading term unless one adds a separate sign or tail-domination theorem.

Needed for promotion

- Prove C.
- Prove D.
- Prove the downstream descent from genuine corrected finite-core data to the defect-free affine-incidence model: enough low-order interaction control to force affine dependence of `\Xi(h_j)` or lifted points `Q_v(h_j)` for a bad finite core.
- Use the existing `k=2,3,4` geometric lanes to turn that descent into the relevant incidence obstruction.
- Then state and prove the analytic terminal theorem in one of the genuinely sufficient forms:
  1. **Direct transformed-scalar form:** `|\Xi_{\core}^{(N)}(m)|\asymp (x(m)/B_\zeta(m))S(m)` with sign or modulus determined by the corrected package fiber plus the derived incidence data; or
  2. **Derivative-transfer form:** weighted-average or pointwise one-sided control of `H_{\core}^{(2N-1)}` on `0\le s\le N/Q^2`, then invoke the positive-kernel `N`-point formula.
- If one insists on a coefficient-side theorem, add an explicit no-cancellation hypothesis or tail-domination theorem beyond lower control of `c_{2N-1}^{\core}(m)`.
- Rewrite `rem:wip-pairlike-finitecore`, `rem:wip-final-endgame-status`, and the final contradiction theorem to replace the pair-like toy lower input by E.

Honest verdict: my previous reduction to a single theorem E was too compressed. The next concrete attack after C and D is still downstream rather than package-level, but the draft now shows the intermediate target more concretely than I first thought. The genuine finite-core branch must descend from corrected package data to the defect-free affine-incidence model already developed in the paper: affine dependence of `\Xi(h_j)` or lifted points `Q_v(h_j)`, hence reduction to the existing `k=2,3,4` coincidence/collinearity/coplanarity lanes. Only after that geometric descent can one hope to extract a contradiction-scale lower law for the first surviving odd channel. The cleanest terminal formulation is still derivative-side or direct-`\Xi`, because the paper already proves that the `N`-point operator is a positive average of the first surviving derivative.

Autoresearch next step

continue: attack the descent-to-incidence step directly: identify the weakest corrected finite-core hypothesis that upgrades the paper's defect-free affine-dependence theorems to the genuine bad core, ideally enough to place the bad core into the existing `k=2,3,4` lifted geometry lanes.
verify: adversarially check whether the defect-free affine-incidence model can really be reached from C and D alone, or whether an extra low-order interaction-vanishing theorem is genuinely independent; also check whether any direct positive-kernel route can bypass this descent without smuggling in unproved no-cancellation or incidence control.
blocked: no coordinator action needed yet.
terminal: not terminal; target sharpened from a vague post-C/D “rewrite the endgame” step to the concrete finite-core lower-model transfer target `E`, now resolved more accurately as the two-stage stack `E_1` (descent to affine-incidence lanes) plus `E_2` (analytic weighted-average/direct-`\Xi` lower transfer).