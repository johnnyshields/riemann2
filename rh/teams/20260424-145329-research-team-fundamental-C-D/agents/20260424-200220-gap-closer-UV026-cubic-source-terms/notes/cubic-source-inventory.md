# UV-026 Cubic Source Inventory

Input used: staged UV-025 tagged pre-whitening source block in
`paper-updates.md`.

## Cubic families in pre-\(\Phi_K\) whitening

Write
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]
Let the left and right inverse square-root factors have Frechet expansions
\[
L=L_0+L_1+L_2+L_3+\cdots,\qquad R=R_0+R_1+R_2+R_3+\cdots,
\]
and let
\[
N=N_0+Y
\]
because the mixed block is affine in its perturbation before the nonlinear
trigonometric/Taylor expansion is decomposed into pair-kernel degrees.

The cubic homogeneous part of \(LNR\) has seven families:

| Family | Cubic source | UV-026 status |
|---|---|---|
| \((3,0,0)\) | \(L_3N_0R_0\) | live unless identified as \(K_5/K_3/\)pure |
| \((0,0,3)\) | \(L_0N_0R_3\) | live unless identified as \(K_5/K_3/\)pure |
| \((2,1,0)\) | \(L_2YR_0\) | live unless identified as \(K_5/K_3/\)pure |
| \((0,1,2)\) | \(L_0YR_2\) | live unless identified as \(K_5/K_3/\)pure |
| \((2,0,1)\) | \(L_2N_0R_1\) | live unless identified as \(K_5/K_3/\)pure |
| \((1,0,2)\) | \(L_1N_0R_2\) | live unless identified as \(K_5/K_3/\)pure |
| \((1,1,1)\) | \(L_1YR_1\) | live unless identified as \(K_5/K_3/\)pure |

Each family can carry the finite grade multiset \((1,1,5)\). Since the UV-025
block retains source tags through \(\operatorname{Lin}_{\mathcal K}\), three
source-linear factors can produce non-\((1,1)\) monomials
\[
\tau_1^2\tau_2,\qquad \tau_1\tau_2^2.
\]

## Source mechanisms available

- \(K_5\) shadow: source proves
  \(A_{7,K_5}^{\mathfrak f}=c_2A_5^{\mathfrak f}\), but only after the term is
  known to be the one-pair normalization shadow \(c_2A_5+[B_2,A_5]\).
- \(K_3\) shadow: source proves \(A_{7,K_3}^{\mathfrak f}=0\), but only for the
  displayed one-pair \(K_3\) normalization shadow.
- Pure same-point sector: source proves it vanishes in the one-pair odd germ,
  but this does not automatically apply to source-coupled cubic whitening
  families with \(N_0\) or \(Y\).

## Conclusion

The staged UV-025 block gives source tags and a pre-whitening input, but it does
not identify the seven cubic whitening families with the one-pair \(K_5\),
\(K_3\), or pure sectors. UV-026 therefore remains open. The obstruction is
genuine for promotion, but still formal rather than an actual-package
counterexample until the order-7 fixed-sector coefficients are computed or
classified source-theoretically.
