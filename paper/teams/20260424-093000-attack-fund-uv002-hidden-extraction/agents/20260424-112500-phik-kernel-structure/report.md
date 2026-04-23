## Claim

With the paper's matrix basis
\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
K=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
the transverse functional
\[
\Phi_K(X)=x_{12}+x_{21}
\]
kills exactly the three directions
\[
\ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K,
\qquad
\Phi_K(S)=2.
\]
So, in current package notation, the sharp hidden directions are:

1. diagonal/value directions: the cubic scalar `c`-mode (`D`), the fixed-sector quintic `u_5`-mode (`I`), and the leading value channel `A_{\val}`;
2. the antisymmetric off-diagonal shear direction (`K`).

The first package direction that is not in `\ker\Phi_K` is the symmetric off-diagonal fixed-sector direction `S`, i.e. the `v_5` component of
\[
A_5^{\mathfrak f}=u_5 I+v_5 S.
\]
Equivalently, after gauge-fixing on `v_5\neq 0` so `u_7=\lambda=\Delta_7/v_5`, the reduced variables
\[
Y=\frac{u_5}{c},\qquad x=\frac{v_5}{c},\qquad S=\frac{\Delta_7}{c\,v_5}=\frac{\lambda}{c}
\]
forget only projective/diagonal data plus the antisymmetric shear; any variation with nonzero `\delta v_5` is immediately `\Phi_K`-visible. In particular the septic gauge line
\[
\delta A_7^{\mathfrak f}=\chi A_5^{\mathfrak f}
\]
is not automatically invisible, because
\[
\Phi_K(\chi A_5^{\mathfrak f})=2\chi v_5,
\]
so it lies in `\ker\Phi_K` only on the exceptional locus `v_5=0`.

## Status

proved

## Evidence

- By definition, `\Phi_K` sums the two off-diagonal entries, so it annihilates every diagonal matrix and also the antisymmetric off-diagonal basis vector `K`, while `\Phi_K(S)=2`.
- The leading value channel is already known to be `\Phi_K`-invisible: `\Phi_K(A_{\val})=0`.
- In fixed-sector notation, `A_5^{\mathfrak f}=u_5 I+v_5 S`, so the `u_5` direction is invisible and the `v_5` direction is the first visible one.
- The septic gauge ambiguity is exactly motion along the line `\mathbf C A_5^{\mathfrak f}`. Applying `\Phi_K` to that line gives `2v_5` times the gauge parameter, so this hidden direction is generically visible unless `v_5=0`.
- The direct `q^{(7)}` slice distinguishes the same dichotomy: the `q^{(7)}` contribution is diagonal on the same-point side and off-diagonal only through the mixed shear slice, matching the decomposition into `\ker\Phi_K` directions plus the first visible `S`-direction.

## Exact refs

- `paper/proof_of_rh.tex:406-414` — definition of `\Phi_K`.
- `paper/proof_of_rh.tex:567-597` — `\Phi_K(A_{\val})=0`.
- `paper/proof_of_rh.tex:23132-23155` — basis `I,D,S,K` in the cubic-normalized frame.
- `paper/proof_of_rh.tex:7013-7021` — `A_5^{\mathfrak f}=u_5 I+v_5 S`.
- `paper/proof_of_rh.tex:7081-7084`, `8008-8021` — septic gauge line along `A_5^{\mathfrak f}`.
- `paper/proof_of_rh.tex:7553-7595`, `7655-7668` — direct `q^{(7)}` diagonal vs off-diagonal slice separation.
- `paper/proof_of_rh.tex:7892-8000` — quotient-septic closure and remaining raw affine line.
- `paper/proof_of_rh.tex:8414-8429` — `\mu=c/v_5`, `\lambda=\Delta_7/v_5`.
- `paper/proof_of_rh.tex:24380-24385`, `25533-25541` — current reduced package coordinates `Y=u_5/c`, `x=v_5/c`, `S=\Delta_7/(c v_5)`.

## Dependencies

- Uses only the paper's linear-algebra notation for `\Phi_K` and the fixed-sector package coordinates.
- Uses the local gauge description of the raw septic representative and the reduced variables on a good `v_5`-patch.

## Strongest objection

This identifies the linear directions that `\Phi_K` does and does not see, but it does not yet prove the hidden-state lemma itself: the paper still lacks a theorem that equal reduced-package fibers force the full corrected two-atom block to differ only by those `\ker\Phi_K` directions through the first surviving odd order.

## Needed for promotion

1. Prove that the raw-to-reduced quotient from the actual corrected package to the reduced package state loses only the `I,D,K` directions through the first surviving odd order.
2. Prove that these `\ker\Phi_K` directions cannot feed back into the first surviving odd coefficient of `H_m`, equivalently the first nonzero `\Xi_{\zeta,\le H}^{(N)}`.
3. Treat separately the exceptional locus `v_5=0`, where the septic gauge line can become `\Phi_K`-invisible.

Honest verdict: the sharp matrix-level answer is clean. `\Phi_K` sees only the symmetric off-diagonal `S` component. So the hidden directions are exactly diagonal/value plus antisymmetric shear, and the first genuinely visible package direction is the `v_5 S` direction, with the septic gauge line becoming visible as soon as `v_5\neq 0`.
