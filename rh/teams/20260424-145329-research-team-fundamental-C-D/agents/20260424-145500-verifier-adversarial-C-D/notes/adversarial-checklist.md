# Adversarial checklist for Bottlenecks C and D

Prepared before current-cycle research deposits land.

## Bottleneck C — corrected reduced-package diagonal collapse

Target claim shape:
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

### Main kill questions

1. **Is the package object actually defined canonically?**
   - Reject any argument that reasons with `\mathfrak P^{\corr}_2` or `\widetilde\Psi^{\corr}_{\mathrm{red}}` before fixing the exact corrected two-atom package and its codomain.
   - Watch for silent replacement of a raw septic representative by the determinant-type scalar `\Delta^{\corr}` without proving that the order-7 two-atom datum canonically descends.

2. **Does the argument prove more than analytic extension + symmetry?**
   - Analyticity in the blow-up chart and swap-evenness only permit an exceptional-divisor trace
     \[
     B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)
     \]
     to be an arbitrary analytic function of `\kappa`.
   - Any proof that concludes `\kappa`-independence from parity, continuity, or quotient-visible regularity alone is insufficient.

3. **Where is diagonal collision-functoriality actually used?**
   - The only theorem shape currently strong enough is that reduced corrected two-atom package formation commutes with diagonal merger.
   - Demand an explicit passage from
     \[
     \mathfrak P^{\corr}_2(a_1,m;a_2,m)
     \]
     to the merged one-pair package `(a_1+a_2)F_m`, and then after reduction to `\widehat\Psi(m)`.

4. **Does the reduction survive `\delta=0` honestly?**
   - Since `\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)` is defined only for `C\neq 0`, any diagonal-specialization proof must justify extension across the exceptional divisor rather than substituting `\delta=0` formally.

5. **Is the conclusion really the actual one-pair datum?**
   - Even if the diagonal value is `\kappa`-independent, the proof still needs `B_0(m)=\widehat\Psi(m)`, not merely equality to some convention-dependent one-pair package.

### Strongest default objection for C

Without a canonical diagonal collision-functoriality theorem, the current structure leaves a free analytic exceptional-divisor trace `B(m,\kappa)`. That alone kills any claimed closure of C.

## Bottleneck D — hidden-state / package-to-transform factorization

Target claim shape:
\[
\Delta A_{2r+1}(m)\in \ker\Phi_K=\mathbf C I\oplus\mathbf C D\oplus\mathbf C K
\qquad (0\le r\le N-1),
\]
or equivalently constancy of the first nonzero transformed odd scalar on corrected reduced-package fibers.

### Main kill questions

1. **Is D being proved from the right equivalence relation?**
   - Demand a precise definition of “same corrected reduced-package fiber.”
   - Reject arguments that slide between raw package equality, reduced-package equality, and coincidence of one extracted scalar.

2. **Does the proof neutralize the hidden septic gauge direction?**
   - The one-pair gauge law
     \[
     A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}
     \]
     leaves `\Delta_7` invariant but can change the `S`-component, hence can be `\Phi_K`-visible on raw representatives.
   - Any proof that uses only reduced `\widehat\Psi` data but never kills this visible hidden direction is not enough.

3. **Is the claim transform-level rather than raw-block-level?**
   - The defensible target is vanishing of `\Phi_K(\Delta\widehat\Omega)` through order `2N-1`, not literal equality of odd corrected blocks.
   - Reject raw coefficient equalities unless an additional normalization theorem is supplied.

4. **Is dependence on C explicit and honest?**
   - D should depend on Bottleneck C or an equivalent corrected reduced-package coincidence theorem.
   - If a proof of D secretly assumes diagonal collapse or fiber-canonicity without naming it, mark the dependency missing.

5. **Is the first surviving odd order stable across the claimed fiber?**
   - To conclude constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}`, the proof must show both: same vanishing through lower odd orders and equality of the first visible coefficient.
   - A proof that gives only “same order generically” or “same leading term up to invisible error” is too weak.

### Strongest default objection for D

Bare reduced-package coincidence does not yet force every hidden `\Phi_K`-visible septic mode into `\ker\Phi_K`; the surviving hidden gauge direction can still change the first visible odd scalar unless an additional theorem kills it.

## Dependency watch

- C must not be claimed from D, and D must not be claimed from C, in a circular way.
- Any finite-core contradiction report must state exactly which missing substatement is still needed from C and which from D.
- Support from 2-point or 4-point mixed lanes only counts if it produces an actual theorem-level input for C or D.

## Initial verdict posture

- Favor `rejected` over `open` when a report claims closure but uses only analyticity/symmetry for C, or only reduced-state coincidence for D.
- Use `open` when the report correctly isolates a new minimal missing theorem but does not prove it.
- Ask: what exact statement kills the free `B(m,\kappa)` term for C, and what exact statement kills the hidden `\Phi_K`-visible direction for D?
