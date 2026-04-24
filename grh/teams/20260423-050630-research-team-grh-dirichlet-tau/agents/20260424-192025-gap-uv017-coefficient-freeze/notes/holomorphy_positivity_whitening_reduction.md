# UV-017 Holomorphy / Positivity / Whitening Reduction

Date: 2026-04-24

## Fixed-midpoint holomorphy

At a fixed \(m\in I\) with
\[
2im\notin Z(\Xi_\chi),\qquad 1+2im\notin Z(\Xi_\chi),
\]
the completed-function input gives a local holomorphic logarithmic-derivative
\[
D_\chi(t):=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it)
\]
on a complex neighborhood \(U_m\) of \(m\). On the real boundary interval the
staged source theorem identifies
\[
q_\chi^{\mathrm{pair}}(t)=D_\chi(t).
\]
After shrinking \(U_m\), choose a holomorphic primitive
\[
\Theta_\chi^{\mathrm{pair}}(t)
\]
with derivative \(q_\chi^{\mathrm{pair}}\). Then the displayed paired
same-point entries are holomorphic in \(s\), since they are polynomials in
\[
q_\chi^{\mathrm{pair}}(m\pm s/2),\quad
q_\chi^{\mathrm{pair}\,\prime}(m\pm s/2),\quad
q_\chi^{\mathrm{pair}\,\prime\prime}(m\pm s/2).
\]

For the mixed block, put
\[
\Delta(s):=
\Theta_\chi^{\mathrm{pair}}(m-s/2)
-\Theta_\chi^{\mathrm{pair}}(m+s/2).
\]
Then \(\Delta\) is holomorphic and odd, hence \(\Delta(s)=O(s)\). The
derivative relation \(q=\Theta'\) gives
\[
\sin\Delta(s)+q(m+s/2)s\cos\Delta(s)=O(s^2),
\]
\[
\sin\Delta(s)+q(m-s/2)s\cos\Delta(s)=O(s^2),
\]
and
\[
\begin{aligned}
&\left(q(m-s/2)+q(m+s/2)\right)s\cos\Delta(s)\\
&\qquad+\left(2-q(m-s/2)q(m+s/2)s^2\right)\sin\Delta(s)
=O(s^3).
\end{aligned}
\]
Thus every apparent pole in \(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)\)
is removable at \(s=0\).

This proves fixed-\(m\) holomorphy/removable singularities for the literal
finite-\(s\) chart. It does not by itself provide a uniform microscopic radius
\(|s|<\rho_0/Q\) over a family of \(m\)'s; that needs a pole-clearance and
derivative-control hypothesis.

## Same-point positivity

At \(s=0\), the displayed same-point block is
\[
G_{\chi,m}^{0}
=\frac1\pi
\begin{pmatrix}
2q_0 & q_1/2\\
q_1/2 & (q_2+2q_0^3)/12
\end{pmatrix},
\]
where
\[
q_j:=q_\chi^{\mathrm{pair}\,(j)}(m).
\]
On the real boundary, this \(2\times2\) Hermitian/symmetric block is positive
definite exactly when
\[
q_0>0
\]
and
\[
2q_0q_2+4q_0^4-3q_1^2>0.
\]
The displayed formulas and staged source theorem do not imply this determinant
condition from current scope alone. Formula-shape positivity is false for a
general local phase: \(q(t)=1+K(t-m)\) has \(q_0=1\), \(q_1=K\), \(q_2=0\),
and the determinant is negative for large \(K\).

So same-point positivity/nondegeneracy must remain an explicit finite local
hypothesis. A sharp version is:
\[
q_\chi^{\mathrm{pair}}(t)>0,\qquad
2qq''+4q^4-3(q')^2\ge \kappa>0
\]
on the real microscopic window, plus a small-variation condition extending the
spectral gap to the complex \(s\)-disk needed for holomorphic functional
calculus.

## Whitening

If the paired same-point blocks are holomorphic on an \(s\)-disk and have a
spectral gap at \(s=0\), then after shrinking the disk their spectra avoid
\(0\), and a holomorphic branch of the inverse square root exists by
holomorphic functional calculus. Under this conditional gap,
\[
\widehat\Omega_{\chi}^{\mathrm{pair},\mathrm{corr}}(s;m)
=
G_{\chi,m,-}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
G_{\chi,m,+}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}
\]
is holomorphic.

This is exactly the RH whitening mechanism transported to the displayed chart.
It is not a consequence of the source theorem alone because the required
same-point gap is not proved.

## Unit-coordinate preservation

The admissibility checks do not alter the unit-coordinate calculation. On the
pure value path
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
=\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m),
\qquad
q_{\chi,\alpha}^{\mathrm{pair}}=q_{\chi,0}^{\mathrm{pair}}+\alpha,
\]
one still has
\[
\frac{d}{d\alpha}
\left(q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\right)
=1,
\]
with derivative and curvature coordinates frozen, and
\[
\Delta_{\chi,\alpha}^{\mathrm{pair}}(s)
=\Delta_{\chi,0}^{\mathrm{pair}}(s)-\alpha s.
\]
Holomorphic whitening changes the matrix derivative but not the scalar
coefficient: the derivative after whitening is precisely
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\). A separate check is still needed if
a downstream scalar readout is applied after the matrix-level whitened block.

## Smallest live hypotheses

For UV-017, the finite list is:

1. local holomorphic paired phase on the required microscopic disk, with uniform
   radius if the theorem needs one;
2. same-point positivity/nondegeneracy via the explicit determinant gap above,
   or an equivalent spectral-gap hypothesis;
3. holomorphic inverse-square-root whitening from that gap;
4. derivative-form freeze-rule remainder criterion;
5. scalar-readout unit normalization if the theorem leaves matrix level.
