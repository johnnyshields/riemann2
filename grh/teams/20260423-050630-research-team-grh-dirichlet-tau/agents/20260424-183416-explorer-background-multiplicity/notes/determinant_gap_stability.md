# Determinant-gap stability notes

## One-zero route

Noether's exact computation rejects the unpaired one-zero determinant route:
for a single
\[
K_{\beta,\gamma}(t)
=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+\frac{\beta}{\beta^2+(2t-\gamma)^2}
\]
one has \(\mathcal D[K]\equiv0\) at \(\beta=1/2\), while
\(\mathcal D[K](\gamma/2)<0\) if \(\beta\ne1/2\).

Thus source-kernel positivity alone is not the UV-017 determinant gap.

## Reflected double

The completed paired product does not normally contribute an isolated
off-critical zero. For \(\beta\ne1/2\), the functional-equation reflected zero
\(\beta\mapsto1-\beta\) has the same displayed \(K_{\beta,\gamma}\). Locally
at one ordinate this gives a reflected double \(2K_{\beta,\gamma}\).

Noether's notation gives
\[
c=\beta(1-\beta),\qquad y=(2t-\gamma)^2,\qquad
h=(y+\beta^2)(y+(1-\beta)^2),
\]
and \(K=(y+c)/h\). The scaling identity
\[
\mathcal D[\lambda K]
=\lambda^2\mathcal D[K]+4\lambda^2(\lambda^2-1)K^4
\]
therefore yields
\[
\mathcal D[2K]=\frac{N_2(c,y)}{h^4},
\]
where
\[
\begin{aligned}
N_2(c,y)
&=192cy^4+384c(1-2c)y^3\\
&\quad+192c(6c^2-4c+1)y^2\\
&\quad+384c^3(1-2c)y+192c^5.
\end{aligned}
\]
For \(0<c\le1/4\), every displayed coefficient is positive, since
\(1-2c>0\) and \(6c^2-4c+1>0\) on that interval. Hence
\[
\mathcal D[2K_{\beta,\gamma}](t)>0
\]
for every real \(t\), \(0<\beta<1\), and \(\gamma\).

This repairs the single-zero obstruction at the one-ordinate reflected-pair
level. On the critical line away from the central point, the reflection is not
a distinct same-ordinate zero in general; a simple critical-line zero still has
\(\mathcal D[K]\equiv0\) until a conjugate ordinate, multiplicity, or another
source term is included.

## Full completed orbit and tails

For a nonreal off-critical zero orbit in the completed paired product, the
local source contribution has the form
\[
q_{\mathrm{orb}}(t)
=2K_{\beta,\gamma}(t)+2K_{\beta,-\gamma}(t)
\]
up to analytic multiplicity. A generic noncentral critical-line conjugate pair
has instead \(K_{1/2,\gamma}+K_{1/2,-\gamma}\). Each off-critical
same-ordinate reflected double has a positive determinant gap, but
\(\mathcal D\) is nonlinear:
\[
\mathcal D[f+g]\ne\mathcal D[f]+\mathcal D[g].
\]
Therefore positivity of each \(2K\) summand does not prove positivity of their
sum.

The script-backed searches found no negative full-orbit examples, including
near-edge and critical-line random configurations, but this is only
computational evidence. A theorem would need either a genuine aggregate
inequality for sums of reflected doubles or an explicit compact spectral-gap
hypothesis.

Tails can be controlled only conditionally. If a core source \(q_0\) satisfies
\[
q_0\ge q_*>0,\qquad \mathcal D[q_0]\ge\kappa>0
\]
on a compact window and a tail \(r\) is small in \(C^2\), then
\(\mathcal D[q_0+r]\ge\kappa/2\) after a quantitative smallness condition
depending on the \(C^2\) size of \(q_0\). This is ordinary continuity of the
polynomial expression
\[
2qq''+4q^4-3(q')^2.
\]
It is not a source-alone proof: if the core gap is zero or negative, a small
tail does not provide a uniform repair without additional size information.
