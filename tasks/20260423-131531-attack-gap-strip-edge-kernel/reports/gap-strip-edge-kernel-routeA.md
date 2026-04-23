Claim

The strongest honest strip-edge theorem suggested by the cited formulas is the following two-layer statement.

Proved algebraic layer. For any complex number \(\rho=\beta+i\gamma\) with \(0\le \beta\le 1\), define
\[
K_\rho(t):=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right).
\]
Then for every real \(t\),
\[
K_\rho(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}>0.
\]
So each strip zero contributes a positive edge-resolvent kernel, namely the sum of the two Poisson-type kernels attached to the strip edges \(\Re s=1\) and \(\Re s=0\).

Conditional summation layer. If a zero family admits a background-subtracted phase derivative whose zero part is representable by a termwise-differentiable sum of these kernels,
\[
S(t)=\sum_\rho K_\rho(t),
\]
with the relevant shell sums convergent, then \(S(t)\ge 0\) pointwise, the omitted tail has curvature controlled by the summed single-zero bound, and the manuscript's tail estimate is exactly the consequence of summing this positive strip-edge kernel over omitted zeros.

Sharp stopping point. From the manuscript formulas alone one does not have a theorem that every new completed \(L\)-function produces such a representation, nor a theorem that an arbitrary regularized full zero sum may always be differentiated termwise without an explicit convergence package.

Status

proved

Evidence

Proved.

1. Pure algebraic identity. Writing \(\rho=\beta+i\gamma\),
\[
\frac{1}{1+2it-\rho}=\frac{1-\beta-i(2t-\gamma)}{(1-\beta)^2+(2t-\gamma)^2},
\qquad
\frac{1}{2it-\rho}=\frac{-\beta-i(2t-\gamma)}{\beta^2+(2t-\gamma)^2}.
\]
Taking real parts and subtracting gives exactly
\[
K_\rho(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]
For \(0\le \beta\le 1\), both summands are nonnegative and at least one is strictly positive, so \(K_\rho(t)>0\) for all real \(t\).

2. This is the manuscript's kernel. The paper defines the zero contribution and then uses exactly this explicit function \(f_{\beta,\gamma}(t)\) in the tail decomposition and again in the crude bound for \(S(m)\). So the manuscript already treats the background-subtracted scalar as a sum of positive single-zero kernels.

3. Pure single-zero curvature bound. Differentiating
\[
g_a(u):=\frac{a}{a^2+u^2}
\]
twice gives
\[
g_a''(u)=-\frac{2a}{(a^2+u^2)^2}+\frac{8au^2}{(a^2+u^2)^3}.
\]
Hence
\[
|g_a''(u)|\le \frac{2a}{(a^2+u^2)^2}+\frac{8a u^2}{(a^2+u^2)^3}
\le \frac{10a}{(a^2+u^2)^2}
\le \frac{10}{|u|^4}
\]
for \(u\ne 0\) and \(a\in[0,1]\). Since \(K_\rho(t)\) is the sum of two such terms with \(u=2t-\gamma\), any \(t\) in an interval \(I\) with \(\Delta_\rho:=\operatorname{dist}(2I,\gamma)>0\) satisfies
\[
|K_\rho''(t)|\ll \Delta_\rho^{-4}.
\]
The paper records the concrete constant \(48\) after summation; this is consistent with the algebraic shape of the kernel.

Conditional on convergence / regularization.

4. If one may write \(S(t)=\sum_\rho K_\rho(t)\) with shell convergence sufficient for termwise differentiation up to order \(2\), then positivity of each \(K_\rho\) gives \(S(t)\ge 0\), and the tail curvature estimate follows by summing the single-zero \(\Delta_\rho^{-4}\) bound over omitted zeros.

5. The manuscript's holomorphic-whitening package states exactly this kind of conditional passage: omitted-zero sums and their derivatives converge uniformly on the microscopic disk provided the corresponding real-line shell sums converge. That is the correct analytic hypothesis separating the algebraic kernel theorem from the global summed theorem.

Missing.

6. The formulas do not by themselves produce a portability theorem to new families. They do not prove that a generic completed \(L\)-function has a background subtraction whose zero channel is exactly this kernel, and they do not prove a canonical regularization theorem for conditionally convergent full zero sums beyond the specific zeta-side package already built in the manuscript.

Exact refs

- `paper/proof_of_rh.tex:271-299` for the split `q(t)=B_\zeta(t)+S(t)` and the role of `S` as the background-subtracted zero contribution.
- `paper/proof_of_rh.tex:345-369` for `T_{\far}(t)=\sum_{\rho\notin\mathcal L} f_{\beta_\rho,\gamma_\rho}(t)` and the tail curvature estimate driven by `\sum \Delta_\rho^{-4}`.
- `paper/proof_of_rh.tex:351-355` for the explicit kernel
  `f_{\beta,\gamma}(t)=((1-\beta)/((1-\beta)^2+(2t-\gamma)^2)) + (\beta/(\beta^2+(2t-\gamma)^2))`.
- `paper/proof_of_rh.tex:856-903`, especially `889-899`, for the manuscript's explicit convergence hypothesis: omitted-zero sums and required derivatives converge uniformly provided the real-line shell sums converge.
- `paper/proof_of_rh.tex:26301-26327` and `26330-26364` for the global scalar identity `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` and the crude bound `S(m)\ll Q^2`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:6-18,28-38,49-59` for the matching interpretation of `S(m)` as a positive strip-edge zero kernel and the stated boundary that portability/family realization is still missing.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37` for the required proved / conditional / missing separation and 7-field schema.

Dependencies

- Algebraic layer depends only on the strip location \(0\le \Re \rho\le 1\).
- Summed positivity and curvature depend on a legitimate background-subtracted zero-sum representation and enough shell convergence to justify summation and termwise differentiation.
- The manuscript's concrete zeta-side use also depends on zero counting and zero-free-region input when passing from the kernel formula to the bounds `\sum \Delta_\rho^{-4}\ll Q/R^3` and `S(m)\ll Q^2`.

Strongest objection

The sentence "sum of positive kernels" is only unconditional at the single-zero level. At the global level it hides the hard analytic step: one needs a proved representation of the phase derivative by a background term plus a regularized zero sum, together with shell convergence strong enough for the derivatives used later. Without that package, positivity of the formal kernel does not itself define a valid global object.

Needed for promotion

1. State the single-zero theorem explicitly in the paper as an algebraic lemma, with the kernel written in resolvent form and in positive Poisson-kernel form.
2. State separately a summed-kernel theorem whose hypotheses are the exact convergence and regularization conditions already used implicitly in the tail-holomorphy package.
3. If this is to be exported beyond zeta, prove a family-specific background-subtracted logarithmic-derivative formula producing the same kernel, not just an analogy.
4. Honest verdict: the manuscript genuinely supports a positive strip-edge single-zero kernel theorem and a conditional summed-tail theorem. It does not yet support a family-independent summed-kernel theorem without additional regularization hypotheses.
