## Claim

The enlarged reduced package

\[
\bigl(\widehat\Psi,[\delta c:\delta v_5:\delta u_5:\delta\lambda]\bigr)
\]

is the right next candidate, but on the present draft it is **not yet enough** to determine the first surviving odd jet, equivalently the first nonzero \(\Xi_{\zeta,\le H}^{(N)}\), by itself. It removes the antisymmetric hidden \(\lambda\)-shear direction only projectively; a remaining affine magnitude / diagonal-value mode can still feed a \(\Phi_K\)-visible \(A_5^{\mathfrak f}\)-component through the first odd order.

## Status

open

## Evidence

- Bottleneck D is package-side only: once the first surviving odd coefficient \(c_{2N-1}(m)\) is identified, the \(N\)-point transformed scalar \(\Xi_\zeta^{(N)}\) and its finite-core localization are already complete.
- The current package compression already shows that reduced \(\widehat\Psi\) alone is insufficient; the mixed branch naturally carries an additional projective hidden class

\[
[\delta c:\delta v_5:\delta u_5:\delta\lambda].
\]

- The strengthened coincidence theorem controls only

\[
\widehat\Psi(h)=\left(\frac{u_5}{c},\frac{v_5}{c},\frac{\Delta_7}{c^2}\right),
\]

so it forgets exactly the kind of affine amplitude information that can survive in the raw two-atom package.
- The moving-\(\lambda\)-shear compactness theorem gives only projective freezing of

\[
[\delta c:\delta v_5:\delta u_5:\delta\lambda],
\]

not affine freezing. The text states explicitly that even when affine shears converge one gets only asymptotic transport, not exact repeated-source transport for one fixed triple.
- The obstruction is visible after applying \(\Phi_K\). Since \(\Phi_K(X)=x_{12}+x_{21}\), with

\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

one has \(\Phi_K(I)=0\) and \(\Phi_K(S)=2\). Therefore for

\[
A_5^{\mathfrak f}=u_5 I+v_5 S
\]

the quintic fixed-sector direction is \(\Phi_K\)-visible:

\[
\Phi_K(A_5^{\mathfrak f})=2v_5.
\]

So a residual deformation in the \(A_5^{\mathfrak f}\)-gauge direction is not automatically killed in the odd scalar channel.
- The septic quotient law itself exhibits this leftover affine freedom: replacing a septic representative by

\[
A_{7,1}^{\mathfrak f}\mapsto A_{7,1}^{\mathfrak f}+\eta A_{5,1}^{\mathfrak f}
\]

leaves \(\Delta_7\) unchanged, because the determinant against \(A_{5,1}^{\mathfrak f}\) drops out, but this same \(A_5^{\mathfrak f}\)-direction is \(\Phi_K\)-visible. Thus quotient-level coincidence plus projective shear data still leave an affine modulus that can matter to \(H_m=\Phi_K(\widehat\Omega_\zeta^{\corr})\).
- Conclusion: the enlarged package is enough to isolate the *direction* of the hidden shear defect, but not its \(\Phi_K\)-relevant affine magnitude through the first surviving odd order.

## Exact refs

- `paper/proof_of_rh.tex:408-422`
- `paper/proof_of_rh.tex:567-597`
- `paper/proof_of_rh.tex:6983-7001`
- `paper/proof_of_rh.tex:7013-7059`
- `paper/proof_of_rh.tex:11587-11671`
- `paper/proof_of_rh.tex:11705-11774`
- `paper/proof_of_rh.tex:11888-11992`
- `paper/proof_of_rh.tex:12257-12383`
- `paper/proof_of_rh.tex:12385-12610`
- `paper/proof_of_rh.tex:21142-21217`
- `paper/proof_of_rh.tex:21277-21329`
- `paper/proof_of_rh.tex:2214-2307`
- `paper/proof_of_rh.tex:2990-3015`
- `paper/proof_of_rh.tex:3984-4190`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-78`

## Dependencies

- The odd-holomorphic extractor and exact surviving-expansion for \(H_m\) and \(\Xi_\zeta^{(N)}\).
- The strengthened coincidence identities for \(\widehat\Psi\).
- Projective compactness of the moving \(\lambda\)-shear defect class.
- The quotient-septic gauge law showing residual freedom along \(\mathbf C A_5^{\mathfrak f}\).

## Strongest objection

This is a structural argument from the present formulas, not a constructed counterexample inside the full corrected two-atom package. In principle the actual corrected package could satisfy an additional hidden-state lemma forcing the remaining affine modulus to lie in \(\ker \Phi_K\) through the first surviving odd order. The present draft does not prove that lemma.

## Needed for promotion

1. Strengthen the package datum from the projective hidden class to an affine class, or prove that its missing scale is \(\Phi_K\)-invisible through the first surviving odd order.
2. Equivalently, prove a hidden-state lemma: equal fibers of

\[
\bigl(\widehat\Psi,[\delta c:\delta v_5:\delta u_5:\delta\lambda]\bigr)
\]

force agreement of the corrected two-atom block modulo \(\ker \Phi_K\) up to the first surviving odd order.
3. Then deduce constancy of the first nonzero odd jet of \(H_m\), hence of the first nonzero \(\Xi_{\zeta,\le H}^{(N)}\), on those fibers.

Honest verdict: the smallest larger package is a genuine improvement over reduced \(\widehat\Psi\) alone, but it still falls one affine parameter short of a theorem. The live blocker is no longer an unknown hidden direction; it is the \(\Phi_K\)-visible scale of that direction.
