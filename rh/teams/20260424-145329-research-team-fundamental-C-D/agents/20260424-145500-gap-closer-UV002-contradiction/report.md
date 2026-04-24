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

Equivalently, one may phrase the same target one coefficient lower: if
\[
H_{\core}(z/Q^2)=\sum_{r\ge 0} c_{2r+1}^{\core}(m)\frac{z^{2r+1}}{Q^{2r+4}},
\]
then it is enough to prove
\[
|c_{2N-1}^{\core}(m)|\gtrsim Q^{2N+2}\,\frac{x(m)}{B_\zeta(m)}S(m),
\]
with sign determined by the corrected package fiber. By the exact surviving expansion for `\Xi^{(N)}`, this coefficient statement already yields the contradiction-scale lower bound.

So the endgame stack is now sharp:

1. **C**: corrected reduced-package diagonal-collapse / collision-functoriality
   \[
   \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
   \]
2. **D**: corrected package fibers determine the first surviving odd order and leading transformed scalar, equivalently constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers modulo `\ker\Phi_K`.
3. **E**: finite-core lower-model transfer theorem as above.

This shows that `UV-007` is not an extra independent package theorem. It is the in-paper placeholder for E: rewriting the final contradiction from the pair-like toy lower model to a first-nonzero-odd-jet finite-core lower model.

Status

open

Evidence

The current final contradiction theorem is structurally a comparison between a lower model on the anomaly side and an exponentially small upper bound on the zeta side. On the zeta side, the machinery is already fully general in `N`: the `N`-point operator isolates the first surviving odd coefficient, admits a positive-kernel representation in terms of the first surviving derivative, and localizes the transformed scalar to a fixed finite core. So the zeta side is already written in the right finite-core language.

What remains pair-like is only the lower side. The current proof inserts the toy expansion `\Xi_{\toy}^{(N)}(u,d)=u^2\Phi_K(M(d))+O(u^4)` and the calibration theorem producing `u^2\asymp (x/B_\zeta)S(m)`. That is exactly where the argument still assumes first-odd-jet nondegeneracy of a pair-core normal form. The paper itself says so in `rem:wip-pairlike-finitecore` and `rem:wip-final-endgame-status`.

The positive-kernel representation sharpens the missing target. For any odd analytic germ `F`, the `N`-point scalar is a positive average of `F^{(2N-1)}` over the microscopic interval. Therefore a theorem giving one-sided lower control of the actual finite-core corrected scalar at the first surviving odd order would transfer directly to a contradiction-driving lower bound for `\Xi^{(N)}`. This means the smallest replacement for the pair-like toy theorem is not a full new toy model from scratch; it is enough to prove a finite-core first-surviving-derivative lower law, or any equivalent lower model that implies it.

C and D fit exactly into this picture. C supplies the canonical corrected coincidence package fiber. D says that on that fiber the first surviving odd order and leading transformed scalar are fixed. Once those are granted, E is the only remaining theorem: extract from that package fiber a nontrivial lower model at order `2N-1` strong enough to dominate the exponentially small zeta-side upper bound.

Separate three things:

- **proved:** the `N`-point operator isolates the first surviving odd order and has a positive-kernel formula; the zeta-side transformed scalar is finite-core localized; the current contradiction theorem works in the pair-like branch.
- **conditional on C and D:** the finite-core branch reduces to one new lower-model theorem E; no extra package/extraction theorem remains between D and the contradiction.
- **missing:** a theorem turning the finite-core package fiber into a lower bound for `H_{\core}^{(2N-1)}` or directly for `\Xi_{\core}^{(N)}`.

Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:5300-5473` — Proposition `prop:toy-n-point-direct`; current pair-like lower model.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:739-839` — canonical calibration theorem and remainder-cutoff theorem yielding `u^2\asymp (x/B_\zeta(m))S(m)` in the pair-like route.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3520-3687` — odd-projector factorization, positive-kernel representation, and sign transfer from the first surviving derivative.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:3853-4190` — Proposition `prop:corrected-n-point`, exact surviving expansion, and finite-core localization of `\Xi_{\zeta,\le H}^{(N)}`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12586-12610` — `rem:minimal-core-reformulation`; downstream finite-core extraction should first use `\widehat\Psi`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:24985-25030` — finite-core endgame split; live burden is package-level coincidence / functoriality plus downstream reformulation.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:5604-5643` — `rem:wip-pairlike-finitecore`; genuine finite-core branch must use the first nonzero odd jet.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26369-26398` — `rem:wip-final-endgame-status`; general finite-core branch still needs reformulation in terms of the first nonzero odd jet.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26554-26609` — current final contradiction theorem is pair-like only.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/handoff.md:164-299` — prior-cycle reduction to `C -> D -> finite-core contradiction`.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-kerphik-hidden-state/report.md:1-90` — current sharp form of D.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-143000-C-proof-obligations/report.md:1-76` and `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md:1-68` — current sharp form of C.

Dependencies

- Bottleneck C in the diagonal-specialization form `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`.
- Bottleneck D in the transform-level form: corrected package fibers force equality of first surviving odd order and leading transformed scalar modulo `\ker\Phi_K`.
- A finite-core lower-model transfer theorem E, stated either directly for `\Xi_{\core}^{(N)}` or via a one-sided lower law for `H_{\core}^{(2N-1)}` on the microscopic interval.
- The existing zeta-side `N`-point extractor, positive-kernel, and finite-core localization machinery.

Strongest objection

The reduction to E still leaves open what analytic object should play the role of the pair-like toy anomaly matrix `M(d)`. In the pair-like route, calibration and the toy `u^2` law are explicit. In the genuine finite-core branch, the package fiber may determine the first surviving odd order and leading transformed scalar abstractly without yet giving a usable lower model on the microscopic interval. So E is a real theorem, not just a rewriting exercise. The present paper does not yet construct the finite-core analogue of `M(d)` or prove that its first surviving odd contribution has controlled sign or modulus across the required interval.

Needed for promotion

- Prove C.
- Prove D.
- State and prove E in one of two equivalent forms:
  1. **Direct transformed-scalar form:** `|\Xi_{\core}^{(N)}(m)|\asymp (x(m)/B_\zeta(m))S(m)` with sign or modulus determined by the corrected package fiber; or
  2. **Derivative-transfer form:** a one-sided lower law for `H_{\core}^{(2N-1)}` on `0\le s\le N/Q^2`, then invoke the positive-kernel `N`-point formula.
- Rewrite `rem:wip-pairlike-finitecore`, `rem:wip-final-endgame-status`, and the final contradiction theorem to replace the pair-like toy lower input by E.

Honest verdict: the next concrete attack after C and D is no longer vague. The smallest missing theorem is a finite-core lower-model transfer theorem E. The cleanest formulation is probably derivative-side, because the paper already proves that the `N`-point operator is a positive average of the first surviving derivative. What is missing is not another package theorem, but a proof that the corrected finite-core package fiber forces a nontrivial first-surviving-odd lower law strong enough to drive the same final comparison.

Autoresearch next step

continue: attack theorem E directly by mining the fixed-core decomposition and the positive-kernel `N`-point formula for the weakest sufficient hypothesis on `H_{\core}^{(2N-1)}`; try to reduce E to a package-fiber statement about the sign or modulus of the first surviving derivative on `0\le s\le N/Q^2`.
verify: adversarially check whether the positive-kernel route really avoids needing a full finite-core toy model, or whether hidden oscillation of `H_{\core}^{(2N-1)}` on the microscopic interval breaks the transfer.
blocked: no coordinator action needed yet.
terminal: not terminal; target sharpened from “rewrite the endgame” to the single theorem E above.