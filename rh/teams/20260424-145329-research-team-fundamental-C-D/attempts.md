# Attempts

Legacy row-by-row ledger for this team before resume is preserved in `attempts.tsv`.
New resume attempts should be logged here in markdown.

| Agent | Target | Claim / route | Status | Evidence | Action | Description |
|---|---|---|---|---|---|---|
| verifier-source-CDE | C-FS2 actual-formula source check | Source audit of the `R` determinant slot and centered `D_2` channel | keep | `agents/20260424-160000-verifier-source-CDE/report-cfs2-actual-formulas-source-check.md` | Carry negative forward | Source audit confirms the current paper does not define the actual two-atom fixed triple, does not compute `R` on the exceptional divisor, and does not kill the centered `D_2=2\kappa(AV_1-BU_1)` channel. |
| coordinator | resume checkpoint | Focused in-place restart on C-FS2/C-FS3 | keep | `collation.md`, `dispatch.md`, `findings.md`, `attempts.tsv` | Dispatch focused C attack | Primary target is actual construction/control of the septic quotient-defect representative `R`, or a theorem that `\det(R,A_5^{\mathfrak f})` descends and has no exceptional slope/provenance dependence. |
| verifier-adversarial-C-R-channel | C R determinant channel | `R_\kappa` pressure harness and centered `D_2` channel | keep | `agents/20260424-165509-verifier-adversarial-C-R-channel/report.md`; `scripts/r_channel_pressure_test.js` | Use as acceptance test | Any future C-FS2/C-FS3 closure must explicitly exclude determinant perturbations shifting the reduced third coordinate by `\varepsilon\kappa`, or prove an actual formula/theorem killing the channel. |

## Frontier summaries

- **Current best:** C is the queue head. The formal C-FS3 countermodel and actual-formula/source/adversarial checks show that fixed codomain, scalar normalization, blow-up analyticity, swap-evenness, and the displayed order-3/5/7 formulas do not control the exceptional trace `B(m,\kappa)`. The smallest positive target is to construct the actual corrected two-atom fixed triple and control `\det(R,A_5^{\mathfrak f})`.
- **Keep:** the C-FS2/C-FS3 scoped negatives; the D transform-level state-locality target modulo `\ker\Phi_K`; the E projected-defect/lower-control split.
- **Discard:** routes deriving C from weak formal package properties, scalar normalization alone, raw affine-lift patching, or existing formula display without computing/controlling `R`.
- **Blocked:** no coordinator blocker. Mathematical blocker is the missing actual corrected two-atom package construction and determinant-slot control.
- **Next:** wait for the C gap-closer, actual-package explorer, and source verifier deposits; then test any positive route against the adversarial `R_\kappa` harness.
