## Claim

On the patch `v_5\neq 0`, the enlarged visible package
\[
\widetilde\Psi_{\min}=(x,Y,S,T),\qquad x=\frac{v_5}{c},\quad Y=\frac{u_5}{c},\quad S=\frac{\Delta_7}{c v_5},\quad T=\frac{v_7}{c},
\]
is the sharpest currently plausible candidate for determining the first surviving odd jet of `H_m`, equivalently the first nonzero `\Xi_{\zeta,\le H}^{(N)}`. Reason: `(x,Y,S)` is just the reduced order-`7` package `\widehat\Psi` rewritten on `v_5\neq 0`, and the extra scalar `T` restores the only missing visibly `\Phi_K`-sensitive septic direction of the raw fixed-sector pair. But this is still only a heuristic candidate, not a proved theorem: one still needs a hidden-state lemma that the first surviving odd jet depends on finite-core data only through this enlarged order-`7` state and not through deeper package directions.

## Status

heuristic

## Evidence

The paper defines the fixed-sector septic pair by
\[
A_7^{\mathfrak f}=u_7 I+v_7 S
\]
and shows the raw pair `(u_7,v_7)` is noncanonical only up to the one-dimensional gauge shift
\[
(A_7^{\mathfrak f})^{\new}=A_7^{\mathfrak f}+c_2 A_5^{\mathfrak f},
\]
while the quotient class or determinant `\Delta_7=u_7v_5-u_5v_7` is gauge-invariant. So the unresolved order-`7` freedom is exactly one-dimensional.

The strengthened reduced package is
\[
\widehat\Psi=\left(\frac{u_5}{c},\frac{v_5}{c},\frac{\Delta_7}{c^2}\right).
\]
On `v_5\neq 0`, this is equivalent to `(x,Y,S)` because
\[
x=\frac{v_5}{c},\qquad Y=\frac{u_5}{c},\qquad \frac{\Delta_7}{c^2}=xS.
\]
So `(x,Y,S)` remembers only the quotient-level septic datum, not the raw septic `S`-component.

Adding
\[
T=\frac{v_7}{c}
\]
recovers the full normalized septic fixed-sector pair. Indeed,
\[
\frac{\Delta_7}{c^2}=x\frac{u_7}{c}-Y\frac{v_7}{c}=xS,
\]
so on `x\neq 0`
\[
\frac{u_7}{c}=S+\frac{Y}{x}T.
\]
Hence `(x,Y,S,T)` reconstructs both `u_7/c` and `v_7/c`, i.e. the full order-`7` fixed-sector datum modulo overall amplitude scaling.

This matters for the odd jet because `\Phi_K(X)=x_{12}+x_{21}` and, in the basis
\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
one has `\Phi_K(I)=0` and `\Phi_K(S)=2`. So among the fixed-sector septic coordinates, `v_7/c=T` is exactly the visible scalar for the transverse functional, while the reduced package `(x,Y,S)` forgets it.

This matches the current queue refinement in `collation.md`: equal reduced-`\widehat\Psi` fibers are not enough, and the next plausible enlargement is exactly one additional visible scalar, identified there as the septic gauge parameter in visible form `T=v_7/c`.

What is still missing is theorem-level control that no higher-order or non-order-`7` hidden variation can change the first surviving odd jet once `(x,Y,S,T)` is fixed. The paper only guarantees that the corrected scalar depends analytically on the input block data, not that the dependence truncates at this enlarged order-`7` package.

## Exact refs

- `paper/proof_of_rh.tex:7004-7062` for the fixed-sector quintic/septic coefficients, `\Delta_7`, and the statement that the raw septic pair is noncanonical up to the quintic line.
- `paper/proof_of_rh.tex:7065-7191` for the projected septic gauge law and gauge invariance of `\Delta_7`.
- `paper/proof_of_rh.tex:7948-7973` for the explicit one-dimensional hidden parameter `\chi` in `A_7^{\mathfrak f}=A_{7,K_1}^{\mathfrak f}+\chi A_5^{\mathfrak f}`.
- `paper/proof_of_rh.tex:10788-10843` for the statement that quotient-level order `7` is closed but still too free for the later endgame.
- `paper/proof_of_rh.tex:11368-11449` for the strengthened datum `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` and its scaling meaning.
- `paper/proof_of_rh.tex:11476-11584` for exact strengthened two-pair coincidence and equality of `\widehat\Psi`.
- `paper/proof_of_rh.tex:12230-12254` for the audit that quotient and patch-gauge routes are blind to the repeated-node shear parameter.
- `paper/proof_of_rh.tex:14198-14243` and `15714-15725` for the reduced secant/tangent package `(x,Y,S)` and its geometric role.
- `paper/proof_of_rh.tex:2214-2307` for the odd scalar `H_m` and its odd-jet expansion.
- `paper/proof_of_rh.tex:23132-23135` together with `3984-4190` for the `\Phi_K`-visible transverse channel and the first surviving `\Xi_{\zeta}^{(N)}` extraction.
- `paper/proof_of_rh.tex:2576-2587` for analytic dependence of the corrected scalar perturbation on block input data.
- `paper/proof_of_rh.tex:24985-25030` for the current endgame compression placing the hidden extraction theorem after package-side coincidence.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-113` for the current exact Bottleneck D refinement and the explicit proposal `\widetilde\Psi_{\min}=(x,Y,S,T)`.

## Dependencies

- The package/coincidence front must first identify the relevant finite-core corrected block up to reduced-package fiber.
- A hidden-state lemma is needed: fixing `(x,Y,S,T)` must force agreement of the corrected block modulo `\Phi_K`-invisible directions through the first surviving odd order.
- One must rule out additional dependence of the first odd jet on higher odd coefficients or non-order-`7` hidden transport data.

## Strongest objection

Nothing in the current draft proves that the first surviving odd jet is determined by any finite order-`7` package, even the enlarged one. The paper only isolates a one-dimensional missing visible septic scalar inside the present order-`7` model. It does not yet exclude the possibility that two finite-core packages with the same `(x,Y,S,T)` still differ in higher-order or provenance-sensitive directions that change the first nonzero `H_m` jet.

## Needed for promotion

1. Prove a package-to-transform factorization theorem saying the first surviving odd jet of `H_m` is constant on fibers of `(x,Y,S,T)`, or equivalently that the quotient from the raw corrected package to `(x,Y,S,T)` loses only `\Phi_K`-invisible directions through that order.
2. Show that no additional higher-order visible scalar beyond `T` enters before the first surviving odd order.
3. Then combine with the existing `H_m` and `\Xi_{\zeta,\le H}^{(N)}` extractor machinery to identify the first nonzero transformed scalar from the enlarged package.

Honest verdict: `T=v_7/c` is the best current one-dimensional enlargement and it plausibly repairs the exact defect of reduced-`\widehat\Psi` fibers. I do not see paper evidence that it already suffices theoremically; the live blocker is now a hidden-state lemma showing that `(x,Y,S,T)` captures every `\Phi_K`-visible direction through the first surviving odd order.
