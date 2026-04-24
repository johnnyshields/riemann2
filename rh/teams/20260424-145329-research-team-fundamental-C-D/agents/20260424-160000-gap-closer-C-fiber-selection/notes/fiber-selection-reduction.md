# C fiber-selection reduction

## Baseline

The first-wave C work already separated the local affine septic-lift cocycle from the remaining hidden datum. On the one-pair local gauges,
\[
S_v=\frac{\Delta_7}{c v_5},\qquad S_u=-\frac{\Delta_7}{c u_5},
\]
and on overlap
\[
S_u=-\frac{x}{Y}S_v,
\qquad x=\frac{v_5}{c},\quad Y=\frac{u_5}{c}.
\]
The transition is base-controlled by \(\widehat\Psi=(Y,x,\Delta_7/c^2)\). Patching the affine lift is not the obstruction.

## Route A: direct affine-fiber construction

The one-pair order-7 fixed-sector package proves only:

- canonical quotient class \([A_7^{\mathfrak f}]\in \mathfrak f/\mathbf C A_5^{\mathfrak f}\);
- canonical determinant \(\Delta_7\);
- raw representatives lie in the affine line \(A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}\).

This supports an affine-line local model, but it does not construct the actual corrected two-atom exceptional-divisor object. The proposed fixed-ambient two-atom triple
\[
\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
\]
with reduction
\[
\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)
\]
removes raw septic gauge from the C object. That is useful, but it also shows that C cannot be closed by selecting a raw septic representative: the reduction has already quotiented away that representative. The surviving free trace is an exceptional-divisor value
\[
B(m,\kappa)=\mathcal R(\mathfrak P_2^{\corr})(m,\kappa,0),
\]
not a gauge section of the one-pair affine line.

Route A therefore does not close. The clean reduction is: prove the actual corrected two-atom package extends to an exceptional-divisor state whose only non-base freedom is this one scalar trace, and then prove that trace is diagonal-merged. The current paper proves neither existence nor no-extra-datum for the actual two-atom object.

## Route B: diagonal-merger / collision functoriality

If the actual corrected two-atom package satisfies a fixed-codomain merger law
\[
\mathfrak P_2^{\corr}(a_1,m;a_2,m)=(a_1+a_2)F_m
\]
compatible with \(\mathcal R\), then
\[
\mathcal R(\mathfrak P_2^{\corr}(a_1,m;a_2,m))=\widehat\Psi(m)
\]
by the scaling law of \(\widehat\Psi\). This would kill \(B(m,\kappa)\).

But the paper explicitly leaves this merger law conditional. Worse, the naive source-summed corrected-block model cannot supply it: finite-order coefficients along a weighted one-atom path are even analytic in the source weight, so they cannot produce the required linear one-atom law unless trivial. Thus diagonal merger is not derivable from the current corrected-block formulas alone.

Route B reduces C to a genuine package functoriality theorem; it does not prove it.

## Route C / fallback: smallest missing substatements

The smallest theorem stack that would close C is:

1. **C-FS1: corrected exceptional-divisor package.** Define \(\mathfrak P_2^{\corr}\) as an analytic fixed-codomain two-atom germ on the collision chart \((m,\kappa,\delta^2)\), with reduction \(\widetilde\Psi^{\corr}_{\rm red}=\mathcal R\circ\mathfrak P_2^{\corr}\) extending to \(\delta=0\).
2. **C-FS2: no extra exceptional state.** Show that the restriction of the actual corrected package to \(\delta=0\), modulo the reduction, is controlled only by the merged one-pair base and a single exceptional-divisor trace \(B(m,\kappa)\); no relational/provenance-sensitive two-atom datum survives in the C codomain.
3. **C-FS3: diagonal merger / slope-independence.** Prove \(B(m,\kappa)=B_0(m)\), equivalently the exceptional-divisor trace is independent of collision slope \(\kappa\).
4. **C-FS4: diagonal identification.** Prove \(B_0(m)=\widehat\Psi(m)\) by compatibility with one-amplitude collapse and the scaling law of \(\widehat\Psi\).

C-FS3 is the strongest blocker if C-FS1 and C-FS2 are granted. Without C-FS3, the analytic normal form
\[
\widetilde\Psi^{\corr}_{\rm red}(m,\kappa,\delta)=B(m,\kappa)+\delta^2R(m,\kappa,\delta^2)
\]
remains compatible with analyticity, swap-evenness, scalar normalization, and reduced blow-up coordinates.

## Honest result

The affine-lift work improves the local model but does not by itself kill \(B(m,\kappa)\). In fact, it clarifies why the raw septic fiber and the C trace should not be conflated. The one-pair affine line is gauge freedom of representatives; Bottleneck C is an exceptional-divisor trace of the actual corrected two-atom reduced package. The smallest honest advance is the four-substatement reduction above, with C-FS2/C-FS3 as the live fiber-selection claims.
