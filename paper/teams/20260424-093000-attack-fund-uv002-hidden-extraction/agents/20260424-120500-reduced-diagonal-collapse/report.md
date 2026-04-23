## Claim

The exact theorem

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

is not proved by the current draft. A sharp obstruction is proved instead: once the actual corrected two-atom package is reduced to an analytic germ in the blow-up variables
\[
(m,\kappa,\varepsilon),\qquad \varepsilon=\delta^2,
\]
swap symmetry imposes no restriction on the exceptional-divisor value at \(\varepsilon=0\), because the swap
\[
(m,\omega,\delta)\mapsto (m,-\omega,-\delta)
\]
fixes both \(\kappa=2\omega/\delta\) and \(\varepsilon=\delta^2\). Therefore an arbitrary analytic family
\[
G(m,\kappa,0)
\]
is compatible with the current blow-up-level hypotheses. The missing input is exactly a diagonal-merger theorem in the unblown chart, or an equivalent theorem that the corrected reduced package extends from an analytic raw two-atom germ and equals the one-pair reduced package on coincident atoms.

## Status

proved

## Evidence

1. The one-pair reduced target is already canonical:
\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right).
\]
So Bottleneck C has a precise diagonal target, not just a slogan. See `proof_of_rh.tex:11368-11409`.

2. Exact two-pair coincidence through order `7` is already formal once the corrected cubic/quintic/septic package satisfies the merger identities; then one gets
\[
\widehat\Psi(h_1)=\widehat\Psi(h_2).
\]
So the unresolved issue is not the algebra of `\widehat\Psi`, but whether the actual corrected two-atom package supplies the needed merger/coincidence input. See `proof_of_rh.tex:11476-11584`.

3. The paper already isolates the weaker quotient route as a pure continuity plus diagonal-collapse problem for the actual corrected two-atom quotient map. See `proof_of_rh.tex:12042-12137`. The package-side Bottleneck C is the strengthened reduced-package analogue of exactly this missing diagonal-collapse input.

4. The collision/cancellation chart is
\[
m=\frac{h_1+h_2}{2},\qquad \delta=h_2-h_1,\qquad \omega=\frac{\lambda-1}{\lambda+1},\qquad \kappa=\frac{2\omega}{\delta}.
\]
See `proof_of_rh.tex:12385-12445`.

5. On this chart, for defects that vanish on the collision locus, swap-even analyticity only yields a representation
\[
E(m,\omega,\delta)=\delta^2\,\mathcal H(m,\kappa,\delta^2).
\]
See `proof_of_rh.tex:12447-12511`. The same formalism shows why the reduced-package edge value is currently free: after passing to `(m,\kappa,\varepsilon)`, the swap acts trivially on `(\kappa,\varepsilon)`, so any analytic germ
\[
\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,\varepsilon)
\]
has unrestricted exceptional value `\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)` unless one adds a theorem tying it back to the diagonal `h_1=h_2`.

6. The remaining burden is explicitly described in the paper as package-level coincidence / same reduced image germ / collision-functoriality, not another low-order bookkeeping problem. See `proof_of_rh.tex:12513-12610`, `24985-25030`.

7. Exact source-level diagonal merger for the actual corrected two-atom package is already identified as the decisive finite-order input:
\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h.
\]
See `proof_of_rh.tex:12168-12189`. The naive source-summed whitened model cannot prove this because its extracted coefficients are even in the source weight. See `proof_of_rh.tex:12192-12228`.

## Exact refs

- `paper/proof_of_rh.tex:11368-11409`
- `paper/proof_of_rh.tex:11476-11584`
- `paper/proof_of_rh.tex:12042-12137`
- `paper/proof_of_rh.tex:12168-12228`
- `paper/proof_of_rh.tex:12385-12511`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-55`

## Dependencies

- The canonical one-pair reduced datum `\widehat\Psi`.
- The collision/cancellation blow-up chart `(m,\omega,\delta)` and its reduced variables `(m,\kappa,\delta^2)`.
- The existing exact coincidence algebra for `\widehat\Psi` under merger hypotheses.
- A missing theorem identifying the actual corrected two-atom package on the diagonal with the one-pair reduced package.

## Strongest objection

This is an obstruction from the current draft, not an impossibility theorem in absolute terms. If one proves that the actual corrected reduced package is the pullback of an analytic swap-even germ in the unblown variables `(m,\omega,\delta)`, or proves the exact diagonal merger theorem directly, then `\kappa`-independence on `\delta=0` becomes automatic and the obstruction disappears.

## Needed for promotion

1. Define the actual corrected reduced two-atom package as a genuine analytic raw germ before blow-up, or prove an equivalent extension theorem.
2. Prove the exact diagonal merger / coincidence law on coincident atoms:
   \[
   \widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
   \]
3. Then Bottleneck C is closed, and the later package-to-odd-jet theorem can use this reduced coincidence germ as input.

Honest verdict: the narrowest exact blocker is now clean. The present draft does not force the exceptional-divisor value of the corrected reduced package to be `\kappa`-independent. In blow-up variables that value can be an arbitrary analytic function of `\kappa`. What is missing is exactly an honest diagonal-merger theorem tying the reduced two-atom package back to the one-pair datum `\widehat\Psi(m)`.
