# Claim

[confirmed] The cited strip-edge kernel package supports three distinct summation regimes, and they should not be conflated.

1. Finite local blocks such as the designated local core `\mathcal L` are honest finite sums, so reindexing and differentiation are trivial.
2. The omitted-zero tail
   \[
   T_{\far}(t)=\sum_{\rho\notin\mathcal L} f_{\beta_\rho,\gamma_\rho}(t)
   \]
   is safe only after one states the local absolute-convergence hypotheses explicitly: for `t\in I`, each omitted zero satisfies `|2t-\gamma_\rho|\ge \Delta_\rho`, the shell count is `\#\mathcal S_k\ll 2^kRQ`, and termwise differentiation is justified by the summable bound `|f_{\beta,\gamma}''(t)|\ll \Delta_\rho^{-4}`.
3. The full scalar
   \[
   S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
   \]
   is best read, from the cited source layer alone, as a positive strip-edge kernel sum that is absolutely convergent at fixed `m` because each summand is the pole difference
   \[
   f_{\beta,\gamma}(m)=\RePart\!\left(\frac{1}{1+2im-\rho}-\frac{1}{2im-\rho}\right)
   \]
   and therefore decays like `|2m-\gamma|^{-2}` in the tails.

[conditional] What is not yet justified in the cited source layer is the stronger source identification
\[
q(t)=\text{normalized completed-log-derivative difference} = B_\zeta(t)+S(t)
\]
with exact normalization, exact background term, and exact interpretation of the underlying completed-log-derivative sums. The raw Hadamard sum `\sum_\rho (s-\rho)^{-1}` is only conditionally meaningful; only the strip-edge difference of two such evaluations is manifestly absolutely convergent.

[confirmed] The strongest safe manuscript-level claim without committing to a full completed-function identity is: `S(m)` is a positive background-subtracted strip-edge zero kernel which serves as the scalar coefficient of the local value channel in
\[
\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
\]
and the tail curvature theorem is valid once its local convergence and zero-counting hypotheses are stated explicitly.

# Status

open

# Evidence

Proved from the cited formulas:

- The paper defines `q(t)=B_\zeta(t)+S(t)` and then defines `S(m):=q_\zeta(m)-B_\zeta(m)`. Later it states the explicit kernel formula
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
  \]
  with
  \[
  f_{\beta,\gamma}(m)=\frac{1-\beta}{(1-\beta)^2+(2m-\gamma)^2}+\frac{\beta}{\beta^2+(2m-\gamma)^2}.
  \]
- Each summand is nonnegative for `0\le \beta\le 1`, so once that formula is in force one gets `S(m)>0`. This is enough to make `L(m)=\log(3+|m|+1/S(m))` meaningful.
- Algebraically,
  \[
  f_{\beta,\gamma}(m)=\RePart\!\left(\frac{1}{1+2im-\rho}-\frac{1}{2im-\rho}\right),
  \]
  so the strip-edge kernel is a difference of two simple-pole terms. That difference has `|2m-\gamma|^{-2}` decay, unlike either completed-log-derivative zero sum taken separately.
- The tail theorem uses exactly this improved decay. For `t\in I`, omitted zeros satisfy `|2t-\gamma_\rho|\ge \Delta_\rho`, and the displayed estimate
  \[
  S_2\le \|B_{\Aut}''\|_{L^\infty(I)}+48\sum_{\rho\notin\mathcal L}\Delta_\rho^{-4}
  \]
  is the right termwise second-derivative bound once the tail sum is known to converge locally absolutely with two derivatives.
- The local package uses `S(m)` structurally, not cosmetically: the corrected local deformation is decomposed as
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma).
  \]
  So a positive scalar kernel sum is enough for the local value-channel statement itself.

Conditional on an explicit source theorem:

- To identify `q` as a completed strip-edge logarithmic derivative, one still needs the exact normalization in `t`, the sign convention for `\Phi'`, and the full bookkeeping for gamma factors, trivial zeros, pole terms, and any Hadamard exponential constant.
- In that stronger reading, one must distinguish sharply between:
  \[
  \sum_\rho \frac{1}{1+2it-\rho},\qquad \sum_\rho \frac{1}{2it-\rho},\qquad \sum_\rho \left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right).
  \]
  The first two are completed-log-derivative style sums and need Hadamard regularization; the third is the locally absolutely convergent strip-edge difference actually used in the kernel formulas.

Missing or hidden assumptions:

- The cited source layer does not state a theorem that derives `q(t)=B_\zeta(t)+S(t)` from a completed function with exact normalization.
- The definition `S(m):=q_\zeta(m)-B_\zeta(m)` appears before the positive-kernel formula proving `S(m)>0`, so positivity and even the legitimacy of `1/S(m)` are deferred rather than declared as hypotheses or proved immediately.
- The tail theorem suppresses the hypotheses needed for termwise differentiation: zeros counted with multiplicity, shell counting uniform near height `m`, and the exclusion condition `\Delta_\rho>R` for every omitted zero.
- The crude bound lemma writes `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` as though it were an ordinary global zero sum; it should instead be read either as an absolutely convergent strip-edge kernel sum or as the difference of two regularized completed-log-derivative sums after a separate source theorem.

Honest verdict: the kernel formulas themselves are solid only at the strip-edge-difference level. The manuscript can safely claim a positive scalar kernel sum, local absolute convergence for the tail, and the resulting value-channel decomposition. It cannot yet claim, from the cited source layer alone, a fully normalized completed-function identity for `q` or `S`.

# Exact refs

- `paper/proof_of_rh.tex:149-160` for the abstract phase and `q(t)=\Phi'(t)`.
- `paper/proof_of_rh.tex:273-299` for `q(t)=B_\zeta(t)+S(t)`, `S(m):=q_\zeta(m)-B_\zeta(m)`, `L(m)`, and the curvature estimate.
- `paper/proof_of_rh.tex:345-396` for the omitted-zero tail, shell decomposition, and second-derivative tail bound.
- `paper/proof_of_rh.tex:1540-1565` for `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`.
- `paper/proof_of_rh.tex:26301-26364` for the explicit global kernel formula and crude bound.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44` for required report schema and writing discipline.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:6-18,28-38,49-59` for the current cycle's conservative boundary on scattering-style readings.

# Dependencies

- A source theorem identifying the manuscript's `q` with a specific completed strip-edge log-derivative difference, including the exact factor-of-`2` normalization in `t`.
- Explicit bookkeeping for the background term `B_\zeta`: gamma factor, trivial zeros, pole term, and any Hadamard constant.
- Standard zero counting near height `m` strong enough to justify the shell bounds used in the tail and crude-growth estimates.
- A stated convention that zeros are summed with multiplicity.

# Strongest objection

The manuscript currently slides from a local positive-kernel representation to a global completed-function reading without writing the source theorem that bridges them. That gap matters because the three summation regimes are not interchangeable: finite local sums are elementary, the strip-edge difference is absolutely convergent, but the underlying completed-log-derivative zero sums are only conditionally meaningful after regularization. Without an explicit theorem fixing normalization and background, the phrase `zeta/scattering phase derivative` is doing hidden work.

# Needed for promotion

- State one explicit theorem giving the exact completed-function identity for `q(t)` and the resulting decomposition `q=B_\zeta+S`.
- In that theorem, specify whether `S` is defined primarily as an absolutely convergent strip-edge difference of pole sums or as the residual term after subtracting the full background from a regularized completed-log-derivative.
- Add the missing hypotheses to the tail curvature theorem: multiplicities, shell counting input, and termwise differentiation justification.
- Move positivity of `S(m)` and the legitimacy of `L(m)` earlier in the logic, either as an immediate corollary of the kernel theorem or as an explicit standing hypothesis.
- Keep the conservative wording for portability and local use: `positive strip-edge zero kernel` and `scalar coefficient of the local value channel` are supported; `full completed-function realization` is still conditional.
