# Affine-bundle holonomy derivation

## Local model

Use the fixed-sector data
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
A_7^{\mathfrak f}=u_7I+v_7S,
\qquad
\Delta_7=u_7v_5-u_5v_7.
\]
The gauge law is translation by the quintic line:
\[
(u_7,v_7)\mapsto (u_7,v_7)+c_2(u_5,v_5).
\]
Thus the raw lift space over fixed \((u_5,v_5,\Delta_7)\), with \((u_5,v_5)\neq(0,0)\), is an affine line parallel to \(\mathbf C A_5^{\mathfrak f}\).

## Sections and overlap

On \(v_5\neq0\), the section \(s_v\) is
\[
v_7=0,
\qquad
u_7=\Delta_7/v_5.
\]
On \(u_5\neq0\), the section \(s_u\) is
\[
u_7=0,
\qquad
v_7=-\Delta_7/u_5.
\]
Starting from \(s_v=(\Delta_7/v_5,0)\), the gauge parameter needed to reach \(s_u\) is
\[
\Delta_7/v_5+c_2u_5=0
\quad\Rightarrow\quad
c_2=-\frac{\Delta_7}{u_5v_5}.
\]
So the overlap translation is exactly
\[
s_u=s_v-\frac{\Delta_7}{u_5v_5}A_5^{\mathfrak f}.
\]
This is base-controlled: in normalized variables
\[
Y=\frac{u_5}{c},\quad x=\frac{v_5}{c},\quad \Delta=\frac{\Delta_7}{c^2},
\]
it becomes
\[
c_2=-\frac{\Delta}{Yx}.
\]
The visible normalized \(S\)-coordinate \(T=v_7/c\) changes by
\[
T_u-T_v=c_2x=-\frac{\Delta}{Y}.
\]
Equivalently, if \(S_v:=\Delta_7/(cv_5)=\Delta/x\), then
\[
T_u=-\frac{\Delta}{Y}=-\frac{x}{Y}S_v.
\]
This matches the first-wave statement \(S_u=-(x/Y)S_v\).

## Exceptional loci

- At \(v_5=0\), the \(v_7=0\) section and \(S_v=\Delta/x\) blow up, but if \(u_5\neq0\) the \(u_7=0\) section remains valid.
- At \(u_5=0\), the \(u_7=0\) section and \(T_u=-\Delta/Y\) blow up, but if \(v_5\neq0\) the \(v_7=0\) section remains valid.
- At \(u_5=v_5=0\), the line \(\mathbf C A_5^{\mathfrak f}\) degenerates; the affine-bundle model itself is not the correct local object without a separate blow-up/preparation.

## Consequence for holonomy

The two-chart transition is a base function of \((Y,x,\Delta)=\widehat\Psi\). Hence this affine line bundle has no independent local holonomy datum on the overlap. Any corrected two-atom term that survives while fixed-shear quotient transport descends must either:

1. fail to factor through this base-controlled affine bundle, i.e. be genuinely relational/provenance-sensitive; or
2. be non-finite-order / outside the finite descended transport-state framework.

A term that factors through the descended fixed-shear base state is single-valued in \(u=t^2\). Under the conditional state-local defect closure hypotheses and diagonal vanishing, such a term is forced to \(O(t^2)\), so it cannot be the desired hidden \(\Phi_K\)-visible obstruction.
