# UV-017 One-Zero Determinant Gap

Date: 2026-04-24

## Setup

For
\[
K_{\beta,\gamma}(t)
=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+\frac{\beta}{\beta^2+(2t-\gamma)^2},
\qquad 0<\beta<1,
\]
put
\[
x=2t-\gamma,\qquad y=x^2,\qquad c=\beta(1-\beta),\qquad u=\sqrt c.
\]
Then \(0<c\le 1/4\), \(y\ge 0\), and
\[
K_{\beta,\gamma}(t)=Q(y)
=\frac{y+c}{h(c,y)},\qquad
h(c,y)=y^2+(1-2c)y+c^2.
\]
The denominator is also
\[
h(c,y)=(y+\beta^2)(y+(1-\beta)^2)>0.
\]

The determinant expression uses \(t\)-derivatives:
\[
\mathcal D[q]=2qq''+4q^4-3(q')^2.
\]
Since \(x=2t-\gamma\),
\[
q'=2Q_x,\qquad q''=4Q_{xx},
\]
and, using \(y=x^2\),
\[
Q_x=2xQ_y,\qquad Q_{xx}=2Q_y+4yQ_{yy}.
\]
Thus
\[
\mathcal D[K]=16QQ_y+32yQQ_{yy}+4Q^4-48yQ_y^2.
\]

## Exact numerator

After clearing denominators,
\[
\mathcal D[K_{\beta,\gamma}](t)=\frac{P(c,y)}{h(c,y)^4},
\]
where
\[
\begin{aligned}
P(c,y)
&=(48c-12)y^4+(-192c^2+48c)y^3\\
&\quad +(288c^3-264c^2+48c)y^2\\
&\quad +(-192c^4+48c^3)y+(48c^5-12c^4).
\end{aligned}
\]
The exact factorization over \(u=\sqrt c\) is
\[
\boxed{
P(c,y)=
-12(1-4c)
\bigl(y^2+2(u-c)y+c^2\bigr)
\bigl(y^2-2(u+c)y+c^2\bigr).
}
\]

The first quadratic is strictly positive for \(y\ge0\), because
\[
u-c>0,\qquad c>0.
\]
Therefore the sign of \(\mathcal D[K]\) is controlled by
\[
H(y)=y^2-2(u+c)y+c^2,
\]
except for the prefactor \(1-4c\).

## Sharp sign condition

If \(\beta=1/2\), then \(c=1/4\) and \(1-4c=0\). Hence
\[
\mathcal D[K_{1/2,\gamma}](t)\equiv 0.
\]
This already fails the strict determinant gap.

If \(\beta\ne1/2\), then \(0<c<1/4\). The roots of \(H\) are
\[
y_\pm=u^2+u\pm u\sqrt{1+2u},
\qquad u=\sqrt{\beta(1-\beta)}.
\]
They are positive and distinct. Since the denominator and the first quadratic
are positive, and since the prefactor is negative after the leading minus sign,
\[
\mathcal D[K_{\beta,\gamma}](t)>0
\quad\Longleftrightarrow\quad
y_-<(2t-\gamma)^2<y_+.
\]
The expression is zero at the two boundary values and negative outside this
finite annulus:
\[
\mathcal D[K_{\beta,\gamma}](t)<0
\quad\text{for}\quad
0\le (2t-\gamma)^2<y_-
\quad\text{or}\quad
(2t-\gamma)^2>y_+.
\]

In particular,
\[
\mathcal D[K_{\beta,\gamma}](\gamma/2)
=-\frac{12(1-4c)}{c^4}
=-\frac{12(1-2\beta)^2}{\beta^4(1-\beta)^4}<0
\]
for \(\beta\ne1/2\), while for large \(|t|\),
\[
\mathcal D[K_{\beta,\gamma}](t)
\sim
-\frac{12(1-4c)}{(2t-\gamma)^8}.
\]

## Consequence for UV-017

The one-zero positive strip-edge kernel does not satisfy the same-point
determinant gap. The failure is exact, not numerical:

- off the critical line \(\beta\ne1/2\), the determinant expression is negative
  at the zero center \(t=\gamma/2\) and again in the far tails;
- on the critical line \(\beta=1/2\), the determinant expression is
  identically zero, so nondegeneracy still fails.

Thus the local whitening positivity hypothesis cannot be proved by a
one-zero determinant-positivity lemma for \(K_{\beta,\gamma}\) as stated. Any
positive theorem for the actual completed paired source must use additional
aggregate structure: multiplicity, functional-equation paired duplication,
background/correction terms, or a separate spectral-gap hypothesis.

## Script

The supporting exact arithmetic script is
`scripts/check_one_zero_determinant_gap.py`.

Recorded output includes:

- `SCRIPT_SHA256 B21EF132AC193F05054DED87A76C39B0CA96DD655C1FFB49DFF40EFD54C0156D`;
- `P factorization over u=sqrt(c) verified: True`;
- `At y=0: D[K] = -12(1-4c)/c^4`;
- `As y -> infinity: D[K] ~ -12(1-4c)/y^4`;
- `NONPOSITIVE_GRID_HIT 1/10000 0 -119952000000000000`.
