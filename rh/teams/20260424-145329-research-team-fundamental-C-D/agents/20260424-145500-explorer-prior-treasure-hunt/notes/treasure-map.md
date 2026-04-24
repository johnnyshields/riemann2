# Treasure map from prior cycle

## C-relevant

- [confirmed] **Minimal proof-obligation split for C** is stable across the final wave: 
  1. well-posed exceptional-divisor trace after `2\omega=\kappa\delta`;
  2. `\kappa`-independence / diagonal collapse `B(m,\kappa)=B_0(m)`;
  3. identification `B_0(m)=\widehat\Psi(m)`.
  The real blocker is step 2, not notation or regularity. Refs: prior agent reports `20260424-145000-Bmkappa-killer/report.md`, `20260424-143000-C-proof-obligations/report.md`.
- [confirmed] **Smallest theorem-ready corrected package object for C** is the fixed-ambient triple
  `\mathfrak P^{\corr}_2=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`
  with reduction
  `\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)`.
  This avoids both raw septic gauge baggage and moving-quotient codomains. Refs: `20260424-145000-corrected-package-object/report.md`, `20260424-143000-reduced-package-object/report.md`.
- [confirmed] **Negative/do-not-retry for C**: reduced-coordinate or regularity-only refinements do not kill the free exceptional-divisor term `B(m,\kappa)`. The needed new input is genuine diagonal merger / collision functoriality for the actual corrected two-atom package. Ref: `20260424-133500-C-failure/report.md`.
- [confirmed] **B and C are not literally the same theorem** on the current draft. C needs reduced diagonal collapse to `\widehat\Psi(m)`; B additionally needs scalar normalization strong enough to force raw defect vanishing / raw merger on the diagonal. Ref: `20260424-121500-bc-shared-blocker/report.md`.

## D-relevant

- [confirmed] **Transform-level formulation is the clean theorem target.** D should be stated as constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers modulo `\ker\Phi_K`, equivalently agreement of corrected odd blocks up to the first surviving odd order modulo `\mathbf C I\oplus \mathbf C D\oplus \mathbf C K`. Ref: `20260424-145000-kerphik-hidden-state/report.md`.
- [confirmed] **Kernel geometry is completely sharp:** 
  `\ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K`, `\Phi_K(S)=2`.
  So the first visible direction is the symmetric off-diagonal `S` line; the septic gauge direction is generically visible when `v_5\neq 0`. Ref: `20260424-112500-phik-kernel-structure/report.md`.
- [confirmed] **Best current enlarged visible proxy** on `v_5\neq 0` is
  `\widetilde\Psi_{\min}=(x,Y,S,T)` with `T=v_7/c`.
  This restores exactly the one missing visibly `\Phi_K`-sensitive septic scalar. Refs: `20260424-114500-T-scalar/report.md`, `20260424-123500-T-fiber/report.md`.
- [confirmed] **Negative/do-not-retry for D**: do not promote `\widetilde\Psi_{\min}` to theorem object without a finite-determination / hidden-state lemma. It encodes only normalized order-7 data, and the draft does not bound the first surviving odd order by `7`. Ref: `20260424-123500-T-fiber/report.md`.

## Finite-core contradiction

- [confirmed] The prior cycle keeps the contradiction stack as `C -> D -> contradiction`; nothing in the late wave bypasses D once C lands.
- [candidate] If a future argument can only produce septic-order data, the exact obstruction to contradiction is now pinpointed: one must either prove finite determination from the normalized septic package or prove a uniform bound `N\le 4` for the first surviving odd order. Ref: `20260424-123500-T-fiber/report.md`.

## Support-only 2/4-point mixed

- [confirmed] **Do not let enlarged-package work absorb local support theorems.** An enlarged package theorem can sharpen C-D, but does not subsume the good-patch edge law or the exact fixed-shear corner law unless those local laws are explicitly built into the package theorem itself. Ref: `20260424-110500-enlarged-vs-edgelaw/report.md`.
- [confirmed] This supports the current dispatch non-goal: 2-point / 4-point mixed material is support-only under C/D, not an independent queue head.

## Negative / do-not-retry

- [confirmed] For C, stop searching for a better reduced coordinate or more blow-up regularity as if that would force diagonal collapse; the free datum is exactly `B(m,\kappa)`.
- [confirmed] For D, stop assuming reduced `\widehat\Psi` fibers are enough; the septic gauge line is generically `\Phi_K`-visible.
- [confirmed] Do not oversell `\widetilde\Psi_{\min}`: it is a diagnostic proxy, not yet a canonical theorem object.

## Possible capture misses

- [candidate] `collation.md` already carries the main C-split, corrected-package object, `\ker\Phi_K` structure, and `T`-proxy. I do **not** see a clean capture of the exact negative theorem from `20260424-133500-C-failure/report.md`: namely the scoped reusable no-go that **from current blown-up reduced-package hypotheses alone**, diagonal collapse is not forced because `B(m,\kappa)` remains a free analytic trace.
- [candidate] I also do **not** see an explicit capture of the precise distinction from `20260424-121500-bc-shared-blocker/report.md` that **B and C differ by one scalar-normalization law**. Current collation often treats B as formal after C; that is directionally right, but this report warns the implication is not tautological from present definitions.
- [candidate] I do **not** see a crisp capture of the `20260424-123500-T-fiber/report.md` obstruction that `\widetilde\Psi_{\min}` is exactly the normalized septic package and therefore still needs either finite determination or a uniform odd-order bound. Current collation mentions heuristic status, but not this exact obstruction.
