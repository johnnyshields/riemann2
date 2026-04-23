# Claim

The exact Bottleneck C theorem

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

is not forced by the current draft-level hypotheses. The sharp exact blocker is an exceptional-divisor freedom: after passage to the collision/cancellation blow-up chart, the presently available assumptions allow the corrected reduced two-atom package germ to have an arbitrary analytic diagonal value

\[
B(m,\kappa):=\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0),
\]

with no theorem in the read Bottleneck C material forcing either `\kappa`-independence or equality to `\widehat\Psi(m)`. Therefore the theorem is open, and the missing input is exactly a diagonal-merger / collision-functoriality statement for the actual corrected two-atom package before or at reduction.

# Status

proved

# Evidence

1. The paper already identifies the honest order-`7` target as a provenance-sensitive package theorem, explicitly “same reduced image germ at coincidence” or “collision-functoriality,” not raw septic equality. So Bottleneck C is a package theorem, not a transport theorem.

2. On the residual exact fixed-shear corner, every finite quotient-visible transport jet descends to the quotient variable `u=t^2`, and on the quartic--sextic rung every such finite state is locally a function of the single scalar `Q` alone, with no third local reset beyond `t\leftrightarrow -t`. This removes finite quotient-visible hidden transport, but it does not identify the actual corrected package with that transport state.

3. The strongest conditional closure theorem on that corner is still explicitly state-local: if the corrected package is already a function of the descended transport state and satisfies the natural merger law, then the interaction remainder collapses. The current draft does not prove that state-locality for the actual corrected package.

4. In the collision/cancellation blow-up chart, swap-compatible analyticity only gives a germ in `(m,\kappa,\delta^2)`. At that level one may write abstractly

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,\delta)
=B(m,\kappa)+\delta^2 R(m,\kappa,\delta^2),
\]

with arbitrary analytic `B(m,\kappa)`. This preserves swap-evenness in the blown-up variables and is compatible with the current formal package-side freedom. Hence the divisor value at `\delta=0` is not determined by the existing transport-descent results alone.

5. So the exact missing theorem is not another quotient-visible transport lemma. It is a diagonal-collapse law for the actual corrected reduced package, equivalently a theorem proving that the exceptional-divisor value is forced to be the one-pair reduced datum `\widehat\Psi(m)`.

# Exact refs

- `paper/proof_of_rh.tex:10794-10809`
- `paper/proof_of_rh.tex:10817-10838`
- `paper/proof_of_rh.tex:11368-11409`
- `paper/proof_of_rh.tex:11445-11449`
- `paper/proof_of_rh.tex:12447-12469`
- `paper/proof_of_rh.tex:12548-12559`
- `paper/proof_of_rh.tex:21740-21763`
- `paper/proof_of_rh.tex:22302-22405`
- `paper/proof_of_rh.tex:22409-22505`
- `paper/proof_of_rh.tex:22507-22529`
- `paper/proof_of_rh.tex:24523-24612`
- `paper/proof_of_rh.tex:25420-25441`

# Dependencies

- Definition of the one-pair amplitude-invariant strengthened datum `\widehat\Psi`.
- The quotient-transport descent and rank-one/no-hidden-reset results on the fixed-shear residual corner.
- The collision/cancellation blow-up chart and its swap-compatible `(m,\kappa,\delta)` parametrization.
- A not-yet-proved actual corrected two-atom package theorem tying package value to the one-pair diagonal.

# Strongest objection

The obstruction argument is meta-level: it proves only that the currently cited hypotheses do not force Bottleneck C. It does not prove that the actual corrected package fails the theorem. A stronger regularity statement in the original unsheared variables, or a genuine pre-reduction diagonal merger theorem for the corrected package, could still force `B(m,\kappa)=\widehat\Psi(m)`.

# Needed for promotion

1. State the actual corrected reduced two-atom package germ precisely in the paper's notation.
2. Prove a diagonal-merger / collision-functoriality theorem for the corrected package on coincident atoms.
3. Deduce that the exceptional-divisor value is `\kappa`-independent and equals the one-pair datum `\widehat\Psi(m)`.
4. Then Bottleneck C becomes formal, and the existing strengthened coincidence algebra can be applied downstream.

Honest verdict: the sharp result is an obstruction, not a closure. The current draft already kills finite quotient-visible hidden transport, but it still leaves one free package-side divisor function `B(m,\kappa)`. Bottleneck C closes exactly when that freedom is removed by a real diagonal-merger theorem for the actual corrected two-atom package.
