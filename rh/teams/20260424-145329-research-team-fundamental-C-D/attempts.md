# Attempts

Legacy row-by-row ledger for this team before resume is preserved in `attempts.tsv`.
New resume attempts should be logged here in markdown.

| Agent | Target | Claim / route | Status | Evidence | Action | Description |
|---|---|---|---|---|---|---|
| verifier-source-CDE | C-FS2 actual-formula source check | Source audit of the `R` determinant slot and centered `D_2` channel | keep | `agents/20260424-160000-verifier-source-CDE/report-cfs2-actual-formulas-source-check.md` | Carry negative forward | Source audit confirms the current paper does not define the actual two-atom fixed triple, does not compute `R` on the exceptional divisor, and does not kill the centered `D_2=2\kappa(AV_1-BU_1)` channel. |
| coordinator | resume checkpoint | Focused in-place restart on C-FS2/C-FS3 | keep | `collation.md`, `dispatch.md`, `findings.md`, `attempts.tsv` | Dispatch focused C attack | Primary target is actual construction/control of the septic quotient-defect representative `R`, or a theorem that `\det(R,A_5^{\mathfrak f})` descends and has no exceptional slope/provenance dependence. |

## Frontier summaries

- **Current best:** C is the queue head. The formal C-FS3 countermodel and actual-formula/source/adversarial checks show that fixed codomain, scalar normalization, blow-up analyticity, swap-evenness, and the displayed order-3/5/7 formulas do not control the exceptional trace `B(m,\kappa)`. The smallest positive target is to construct the actual corrected two-atom fixed triple and control `\det(R,A_5^{\mathfrak f})`.
- **Keep:** the C-FS2/C-FS3 scoped negatives; the D transform-level state-locality target modulo `\ker\Phi_K`; the E projected-defect/lower-control split.
- **Discard:** routes deriving C from weak formal package properties, scalar normalization alone, raw affine-lift patching, or existing formula display without computing/controlling `R`.
- **Blocked:** no coordinator blocker. Mathematical blocker is the missing actual corrected two-atom package construction and determinant-slot control.
- **Next:** focused in-place resume with one gap-closer on `R` determinant control, one explorer on actual package construction/source mining, and two verifiers for adversarial/source pressure on any proposed C closure.
