# Claim

The next viable UV-022 construction is a cross-effect package built from the
analytic corrected-whitening transfer:
\[
\mathcal I_{\mathcal T}(a_1X_1,a_2X_2)
:=
\mathcal T(a_1X_1+a_2X_2)
-\mathcal T(a_1X_1)
-\mathcal T(a_2X_2).
\]
This automatically kills one-amplitude inputs and starts with an \(a_1a_2\)
interaction term. It is a better package-definition layer than the signed
finite-amplitude lift.

This does not close UV-010. The diagonal / collision vanishing needed for the
\(\delta^2\mathcal H_7^q\) edge law is not automatic; it remains the
package-level merger or renormalization theorem.

# Status

computational

# Evidence

Source support:

- The corrected-whitening transfer has a homogeneous expansion
  \[
  \mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)
  \]
  with uniform bounds. Refs:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553`.
- The source criterion wants one-amplitude collapse and then studies the
  interaction remainder. Refs:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189`.
- The finite-amplitude source-summed route fails, so a different
  lift/transport object is required. Refs:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`.

I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/scripts/cross_effect_harness.js`.
It models an analytic transfer \(T=T_1+T_2+T_3\) and the cross-effect
\(T(a_1x_1+a_2x_2)-T(a_1x_1)-T(a_2x_2)\). Output:

```text
one_amplitude_left = 0
one_amplitude_right = 0
swap_difference = 0
interaction = 822024
interaction_over_a1a2 = -68502
has_a1a2_factor = true
diagonal_cross_effect = 31200
diagonal_cross_effect_over_a1a2 = -2600
```

Three-bin separation:

- **proved/computational:** analytic cross-effects have exact one-amplitude
  collapse and an \(a_1a_2\) factor by construction; they are symmetric if the
  underlying transfer is evaluated on \(a_1X_1+a_2X_2\).
- **candidate:** for UV-022, take \(X_i=X^{[1]}(h_i)\), the missing
  source-weight-linear corrected block input, and define the package interaction
  by the cross-effect of \(\mathcal T_{Q,R}\) or its order-7 coefficient.
- **missing:** collision/diagonal vanishing is not automatic. The harness shows
  a nonzero diagonal cross-effect when \(X_1=X_2\). A merger, renormalization,
  or same-reduced-image theorem must kill this before the \(\delta^2\) edge law
  follows.

# Baseline / delta

Baseline: UV-022 had a whitening-side linear functor candidate
\(\mathcal T_1\), but the source-weight-linear input \(X^{[1]}\) was still
missing. A purely linear package would be additive and have no two-atom
interaction.

Delta: the package should use the analytic cross-effect of \(\mathcal T\), not
only \(\mathcal T_1\). This keeps exact one-amplitude collapse while retaining
the quadratic \(a_1a_2\) interaction channel where the UV-010 Hessian must live.
The next obstruction is now specifically diagonal/collision vanishing of this
cross-effect in the order-7 quotient output.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` - analytic
  corrected-whitening transfer and homogeneous expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932` - source criterion and
  interaction remainder.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189` - finite-order inputs:
  swap, one-amplitude collapse, diagonal merger.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227` - naive
  finite-amplitude source-summed route fails.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`
  - \(\mathcal T_1\) candidate.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184202-explorer-UV022-cross-effect-package/scripts/cross_effect_harness.js`
  - cross-effect harness.

# Dependencies

- A canonical source-weight-linear input \(X^{[1]}(h)\) for one atom.
- A definition of the two-atom input as \(a_1X^{[1]}(h_1)+a_2X^{[1]}(h_2)\)
  or a corrected variant with the same source-weight-linear part.
- Extraction of the order-7 quotient component from the cross-effect.
- A diagonal/collision theorem proving the cross-effect quotient component
  vanishes to second order in the collision chart.

# Strongest objection

The cross-effect can be nonzero on the diagonal. The harness makes this explicit.
Therefore this construction by itself does not avoid diagonal merger; it merely
places the missing merger/renormalization condition on a concrete object. A
positive UV-010 proof still has to show that the order-7 quotient component of
this cross-effect vanishes on the collision locus, or subtract a source-honest
diagonal counterterm.

# Needed for promotion

1. Define \(X^{[1]}(h)\) from corrected blocks.
2. Define the analytic cross-effect package
   \(\mathcal I_{\mathcal T}(a_1X^{[1]}(h_1),a_2X^{[1]}(h_2))\).
3. Project its order-7 output to the good-patch midpoint quotient.
4. Prove the projected cross-effect is swap-even and collision-vanishing, hence
   has the \(\delta^2\mathcal H_7^q\) edge form.
5. Verify that no free \(P(m,\kappa)\) term remains, or identify it as the exact
   remaining obstruction.

# Autoresearch next step

continue: mine whether the diagonal value of the cross-effect can be subtracted
canonically by same-reduced-image germ, collision-functoriality, or a
source-honest polarization counterterm.

verify: source verifier should check that the cross-effect is compatible with
the paper's finite-order source criterion and does not silently assume diagonal
merger.

blocked: no process blocker. Mathematical blocker is diagonal/collision
vanishing of the order-7 quotient cross-effect.

terminal: terminal for "use only the linear term \(\mathcal T_1\) as the
two-atom package." The interaction lives in the cross-effect. Not terminal for
the cross-effect route.
