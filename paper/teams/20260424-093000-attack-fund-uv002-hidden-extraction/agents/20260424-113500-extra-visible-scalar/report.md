## Claim

Beyond reduced-`\widehat\Psi`, the smallest extra `\Phi_K`-visible scalar that must be retained is the one-dimensional septic gauge coordinate `\chi` along the raw fixed-sector fiber
\[
A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}.
\]
Equivalently, since reduced-`\widehat\Psi` already contains `x=v_5/c`, the minimal extra visible datum can be taken as the normalized visible scalar `x\chi` (or any equivalent affine/projective `\lambda`-shear coordinate on the same one-dimensional fiber). No larger new reduced package coordinate is forced by the present paper.

## Status

proved

## Evidence

- The canonical order-`7` quotient data are already closed by `[A_7^{\mathfrak f}]` or `\Delta_7`; what remains non-unique is only the raw representative along the one-dimensional line `\mathbf C A_5^{\mathfrak f}`.
- The projected septic gauge law is exactly
  \[
  (A_7^{\mathfrak f})^{\new}=A_7^{\mathfrak f}+c_2A_5^{\mathfrak f},
  \]
  so the hidden raw fiber is one-dimensional.
- `\Phi_K` kills diagonal directions and sees the symmetric off-diagonal direction `S`; with `A_5^{\mathfrak f}=u_5I+v_5S`, one gets
  \[
  \Phi_K(A_5^{\mathfrak f})=2v_5.
  \]
  Therefore motion along the septic gauge fiber is generically not `\Phi_K`-invisible.
- Reduced-`\widehat\Psi` already knows
  \[
  x=\frac{v_5}{c},\qquad Y=\frac{u_5}{c},\qquad \frac{\Delta_7}{c^2}=xS,
  \]
  hence also `S=\Delta_7/(cv_5)` on the `v_5\neq 0` package side. So the missing scalar is not another quotient/septic invariant; it is the affine coordinate on the residual raw septic fiber.
- The mixed two-point compactness section identifies the same leftover direction as the projective `\lambda`-shear defect class ` [\delta c:\delta v_5:\delta u_5:\delta\lambda] `, confirming that the live hidden state is one-dimensional after quotient data are fixed.

## Exact refs

- `paper/proof_of_rh.tex:7046-7062`
- `paper/proof_of_rh.tex:7065-7153`
- `paper/proof_of_rh.tex:11368-11449`
- `paper/proof_of_rh.tex:12257-12334`
- `paper/proof_of_rh.tex:20853-20924`
- `paper/proof_of_rh.tex:24987-25029`
- `paper/proof_of_rh.tex:26390-26397`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:64-104`

## Dependencies

- Uses only the fixed-sector septic gauge law, the definition of reduced-`\widehat\Psi`, and the projective `\lambda`-shear compactness package already in the draft.
- To turn this into a theorem about the first surviving odd jet of `H_m`, one still needs the package-to-`H_m` hidden-state lemma.

## Strongest objection

This identifies the smallest surviving hidden scalar geometrically, but it does not prove that retaining `\chi` (or `x\chi`) is sufficient for the actual corrected two-atom package to determine the first surviving odd jet. The missing theorem is still the fiber-invariance statement linking package equality plus this scalar to agreement modulo `\ker\Phi_K` through odd order `2N-1`.

## Needed for promotion

1. State the hidden scalar in the paper as the affine coordinate on the raw septic fiber `A_7^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}`.
2. Prove that equal reduced-`\widehat\Psi` data together with equality of this scalar imply corrected-block agreement modulo `\ker\Phi_K` through the first surviving odd order.
3. Then deduce constancy of the first surviving odd coefficient of `H_m`, equivalently of the first nonzero `\Xi_{\zeta,\le H}^{(N)}`.

Honest verdict: the sharp next blocker is one-dimensional. The package does not need a whole new reduced curve coordinate beyond reduced-`\widehat\Psi`; it needs the hidden septic gauge scalar `\chi` on the raw `A_7^{\mathfrak f}` fiber, equivalently its visible combination `x\chi` or the same projective `\lambda`-shear class.
