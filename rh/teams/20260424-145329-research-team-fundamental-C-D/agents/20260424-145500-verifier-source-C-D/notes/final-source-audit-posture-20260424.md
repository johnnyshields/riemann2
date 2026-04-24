# Final source-audit posture — 2026-04-24

## Stable audit rules for this cycle

### 1. Bottleneck C: affine-fiber / scalar-normalization claims
- The paper **does** prove the amplitude-invariant datum
  \[
  \widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right)
  \]
  and its scaling law.
- The paper **does not** thereby prove corrected-package diagonal collapse on the collision divisor.
- So any C claim built only from affine-fiber language, scalar normalization, or the scaling invariance of `\widehat\Psi` remains **missing**, not proved.
- Honest sourced split for C remains:
  1. existence / extension of the corrected reduced package to `\delta=0`;
  2. `\kappa`-independence / diagonal merger;
  3. identification of the diagonal value with `\widehat\Psi(m)`.
- This 3-way split is a **verifier decomposition**, not a paper-stated theorem stack.

### 2. Bottleneck D-min
- The draft supports the septic algebra
  \[
  A_5^{\mathfrak f}=u_5I+v_5S,
  \qquad
  A_7^{\mathfrak f}=u_7I+v_7S,
  \qquad
  \Delta_7=u_7v_5-u_5v_7,
  \]
  plus the gauge law and the extracted datum `\widehat\Psi`.
- On a good patch `\{c\neq 0, v_5\neq 0\}`, one may derive a local scalar
  \[
  T:=v_7/c.
  \]
- But `T=v_7/c` is only a **patchwise derived scalar**, not a canonical global definition in the paper.
- Therefore any D-min claim must keep the patch hypothesis explicit and must not treat `T` as already-promoted package data.
- The theorem-level target for D remains transform-side:
  equality modulo
  \[
  \ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K,
  \]
  equivalently constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers.

### 3. Theorem E / finite-core rewrite
- The draft supports the queue
  \[
  C \to D \to \text{finite-core endgame rewrite}.
  \]
- It does **not** support the claim that `C + D` alone makes the contradiction formal.
- The first-nonzero-odd-jet endgame rewrite remains a genuine theorem obligation, because the current final contradiction theorem is still pair-like and the `rem:wip-final-endgame-status` remark explicitly says the general finite-core branch still needs reformulation.
- So theorem E should be source-audited as **missing unless the deposit provides a new theorem-level replacement** for the current pair-like contradiction.

## Red lines for promotion
- Reject any C closure claim that cites only blow-up regularity, same-tower pointwise facts, affine-fiber normalization, or `\widehat\Psi` scaling.
- Reject any D-min closure claim that suppresses the patch hypothesis behind `T=v_7/c` or silently upgrades `T` into a canonical global coordinate.
- Reject any theorem-E closure claim that treats the first-nonzero-odd-jet rewrite as bookkeeping instead of a new theorem.

## Basis / notation caution
- The fixed-sector package is written in the `(I,S,D,J)` basis in the one-pair package section.
- Later coefficient extraction for D uses `(I,D,S,K)`.
- Any report moving between these must signal the basis translation explicitly.

## Current honest verdict
- C affine-fiber / scalar-normalization: **conditional at best, currently missing as a theorem**.
- D-min: **patchwise reduction useful, global theorem still missing**.
- Theorem E: **still missing; remains an actual endgame rewrite theorem**.
