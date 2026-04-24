# Claim

[confirmed] The displayed strip-edge kernel formulas support a conservative theorem at the kernel level, but not yet the stronger source theorem that would identify the manuscript's phase derivative with a fully normalized completed-log-derivative difference.

[proved] What is already fixed by the archived derivation and the paper's kernel formulas is the local strip-edge bookkeeping:

\[
f_{\beta,\gamma}(t)=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)
=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]

For a source quotient of the archived form
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
\qquad
\phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
\]
the zero bookkeeping is:

1. a nontrivial zero \(\rho\) contributes a pole at \(s=\rho/2\) and a zero at \(s=(1+\rho)/2\);
2. the real part of its logarithmic-derivative contribution on \(s=\tfrac12+it\) is \(2f_{\beta,\gamma}(t)\);
3. the factor of \(2\) is then canceled by the normalization \(\partial_s\log\phi(\tfrac12+it)=2q(t)\).

[conditional] The manuscript does not yet supply the rest of the source-level bookkeeping as a theorem: the sign convention relating \(q\), \(\Phi'\), and the scattering phase; the exact gamma-factor contribution; the trivial-zero and pole terms; the Hadamard exponential / constant term; and the convention that zeros are counted with multiplicity. Without that package, the paper safely has a strip-edge kernel identity, not yet a proved global source theorem.

[safe note now] A safe note can claim: each strip zero contributes a positive strip-edge kernel; the omitted-zero tail built from those kernels satisfies the displayed curvature estimate under the stated shell-convergence hypotheses; and the scalar \(S(m)\) is represented at manuscript level by an absolutely convergent strip-edge kernel sum.

[must remain conditional] A note should not yet claim: `q(t)=B_\zeta(t)+S(t)` as a fully normalized completed-function theorem; `B_\zeta` or `B_{\Aut}` as already fully derived explicit background terms; or that all gamma / trivial-zero / pole / Hadamard / multiplicity bookkeeping has been closed.

# Status

open

# Evidence

Proved.

1. The archived source derivation writes
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
\qquad
\phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
\qquad
q(t)=\Phi'(t)=-\delta'(t).
\]
For one nontrivial zero \(\rho=\beta+i\gamma\), it records a pole of \(\phi\) at \(\rho/2\) and a zero at \((1+\rho)/2\), so the logarithmic derivative contributes
\[
\frac{1}{s-\rho/2}-\frac{1}{s-(1+\rho)/2}.
\]
Evaluated at \(s=\tfrac12+it\), its real part is exactly \(2f_{\beta,\gamma}(t)\). Since the same archived derivation states \(\partial_s\log\phi(\tfrac12+it)=2q(t)\), the zero contribution to \(q\) is exactly \(f_{\beta,\gamma}(t)\). This fixes the factor-of-\(2\) bookkeeping and shows where the sign convention enters.

2. The manuscript itself uses only the kernel-level output. It states
\[
q(t)=B_\zeta(t)+S(t),
\qquad
S(m):=q_\zeta(m)-B_\zeta(m),
\]
then later gives the explicit formula
\[
S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
\]
At this level, the positivity and crude-growth arguments need only the kernel formula and the strip bound \(0\le \beta\le 1\).

3. The tail-curvature theorem also lives entirely at kernel level:
\[
T_{\far}(t)=\sum_{\rho\notin\mathcal L} f_{\beta_\rho,\gamma_\rho}(t),
\qquad
S_2\le \|B_{\Aut}''\|_{L^\infty(I)}+48\sum_{\rho\notin\mathcal L}\Delta_\rho^{-4}.
\]
This uses the second derivative of the explicit strip-edge kernel and shell counting. It does not require a completed-function source theorem once the needed convergence hypotheses are stated.

Conditional on a missing source theorem.

4. The manuscript prose calls \(B_\zeta\) the explicit background contribution and the archive calls the background the gamma / trivial-zero / pole part, but no theorem in the cited paper regions derives those terms from a completed quotient and shows that nothing else survives into the background. In particular, the archived derivation bundles the gamma factors, trivial zeros, and pole contributions into \(B_{\rm aut}\), but does not in the paper regions isolate the exact formula later denoted by \(B_\zeta\) or \(B_{\Aut}\).

5. The paper regions also do not fix the Hadamard bookkeeping. A completed-function logarithmic derivative normally contains a regularized zero sum plus a constant or exponential-factor contribution. The strip-edge difference
\[
\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}
\]
is absolutely summable in \(\rho\), but the individual edge sums are not. So one still needs a theorem saying exactly whether \(S\) is defined primarily by an absolutely convergent strip-edge difference, or by subtracting two regularized completed-log-derivative evaluations with their constants absorbed into the background.

6. Multiplicity bookkeeping is also still hidden. The shell counts and the global sum \(S(m)=\sum_\rho f_\rho(m)\) are only source-correct if zeros are summed with multiplicity. That convention is not spelled out in the cited paper regions.

Missing.

7. The paper does not yet provide one theorem that simultaneously fixes:
the exact source object; the sign convention; the factor-of-\(2\) normalization from \(2s\); the gamma-factor formula; the trivial-zero terms; the pole terms; the Hadamard constant; and multiplicities.

8. Because that theorem is missing, the strongest safe statement is narrower than the surrounding rhetoric. Safe: `positive strip-edge zero kernel`, `absolutely convergent strip-edge kernel sum`, `conditional omitted-tail curvature bound`. Not yet safe: `fully normalized completed-log-derivative identity for q`.

9. Honest verdict: the hidden bookkeeping is real and mostly source-level, not kernel-level. The factor of `2` and the pole-versus-zero sign are recoverable from the archive. Gamma, trivial-zero, pole, Hadamard, and multiplicity bookkeeping are still conditional in the paper-level theorem chain.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44` for the report schema and writing discipline.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:11-18,21-38,50-59,69-79` for the current conservative boundary: candidate quotient reading yes, realization theorem no.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:17-25,29-42,60-67,99-118` for the conservative theorem already isolated and for the explicit statement that the full normalized completed-function identity is not yet claimed.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299` for `q(t)=B_\zeta(t)+S(t)`, `S(m):=q_\zeta(m)-B_\zeta(m)`, and `L(m)`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-369` for the omitted-zero tail `T_{\far}` and the kernel-level curvature bound.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364` for the explicit global kernel formula `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` and the crude bound.
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598` for the archived source quotient `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, the zero and pole locations, the real-part computation `2f_{\beta,\gamma}(t)`, and the normalization `\partial_s\log\phi(\tfrac12+it)=2q(t)`.
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:11733-11736,11824-11833` for the archived identification of `B_\zeta` as archimedean / trivial-zero background and of `S(m)` as the background-subtracted zero density.

# Dependencies

- A source theorem deriving the manuscript normalization of `q` from a specific completed quotient or completed-log-derivative difference.
- Explicit formulas for the gamma-factor, trivial-zero, and pole contributions absorbed into `B_\zeta` or `B_{\Aut}`.
- A decision about Hadamard regularization: whether `S` is primary at strip-edge-difference level or as a difference of regularized edge evaluations.
- A stated convention that all zero sums count multiplicity.
- The local shell-convergence and termwise-differentiation hypotheses already required by the tail theorem.

# Strongest objection

The manuscript currently uses a source-level decomposition `q=B_\zeta+S` while proving only the kernel-level identities that would result from such a decomposition. The missing step is not cosmetic. Without explicit source bookkeeping, one cannot tell whether the background has absorbed every gamma / trivial-zero / pole / Hadamard contribution with the correct sign and factor, or whether the notation is silently switching between an absolutely convergent strip-edge sum and a regularized completed-log-derivative sum.

# Needed for promotion

- State one source theorem fixing the exact completed object, the sign convention, and the factor-of-`2` normalization.
- Write the explicit background formula and show that it contains exactly the gamma-factor, trivial-zero, pole, and any Hadamard constant terms.
- State that all zero sums are with multiplicity.
- Distinguish explicitly between the absolutely convergent strip-edge difference and any regularized individual edge sums.
- Keep the `strip_edge_kernel_note.tex` boundary for now: kernel theorem yes, full source theorem still conditional.
