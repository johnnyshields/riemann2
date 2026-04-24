# Second-pass source audit of current C/D deposits

## Must-fix

### 1. `gap-closer-C-diagonal-merger/report.md`
- The **C1/C2/C3 split is not a paper theorem stack**. It is a valid organizational reduction, but `C1`, `C2`, `C3` are not named or stated in `proof_of_rh.tex`.
- The source lines support only: (i) the abstract merger lemma (`11888-12040`), (ii) the weaker quotient-diagonal route (`12042-12166`), (iii) the live-source-input remark (`12168-12189`), and (iv) the blow-up chart / residual-burden discussion (`12447-12559`).
- So the report should be read as a **derived decomposition**, not as something already formalized in the draft.
- Its claim that only C2 is “genuinely open” is **too strong from the cited sources alone**. C1 depends on having a precise corrected package object and analytic extension to `\delta=0`; those are not already theorem-level in the paper.

### 2. `gap-closer-D-kerphik/report.md`
- The reduction to a single visible scalar
  \[
  T:=v_7/c
  \]
  is **patchwise and gauge-dependent**, not canonically formalized in the draft as the global hidden-state parameter for D.
- The cited lines do support the raw algebra:
  - `7004-7031`: `A_5^{\mathfrak f}=u_5I+v_5S`, `A_7^{\mathfrak f}=u_7I+v_7S`, `\Delta_7=u_7v_5-u_5v_7`;
  - `7065-7190`: septic gauge law;
  - `11368-11408`: `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)`;
  - `12777-12792`: `v_5`-patch coordinates.
- But the step “after C, exactly one uncontrolled `\Phi_K`-visible scalar remains” is a **useful finite reduction**, not a proved package theorem. It also depends on working on `\{c\neq 0, v_5\neq 0\}` and choosing the `v_5`-patch. That restriction must stay visible.

### 3. `gap-closer-UV002-contradiction/report.md`
- The claim that the finite-core contradiction becomes “formal” after C and D is **too strong** unless item (3) — the finite-core lower-model rewrite — is treated as a genuine remaining theorem. The report itself later qualifies this, but the opening sentence overstates the source support.
- The cited `rem:wip-final-endgame-status` (`26370-26398`) supports exactly that the missing branch is the first-nonzero-odd-jet reformulation, not that this rewrite is routine.

## Should-fix

### 4. `explorer-package-functoriality/report.md`
- Mostly well-scoped, but the “universal property” / “projective descent” language is **structural extrapolation**, not something formalized in the cited paper lines.
- Its source use is best read as: the paper supports the target codomain `\widehat\Psi`, the merger-axiom template, and the statement that the obstruction is package-level; it does **not** yet support the proposed categorical reformulation itself.

### 5. `explorer-support-lanes/report.md`
- Its negative-scoping claims are mostly sourced correctly.
- But the sentence that D should be proved as constancy of the first `\Phi_K`-visible odd coefficient modulo `\ker\Phi_K` is again **theorem-shaping**, not a statement presently proved in the draft.
- The references `25420-25440` and `25444-25485` support the residual-corner delimitation, not the package-to-transform theorem itself.

## Definition / line-ref checks

### `T=v_7/c`
- Correct as a **local algebraic coordinate choice** on the good patch where `c\neq 0`; it is consistent with:
  \[
  A_7^{\mathfrak f}=u_7I+v_7S,
  \qquad
  \widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2).
  \]
- But it is **not canonically named in the paper**. It is a derived local scalar used in the audit reports.

### `C1/C2/C3`
- Correct as an **audit decomposition**:
  1. existence / extension of the blow-up object,
  2. `\kappa`-independence / diagonal merger,
  3. identification with `\widehat\Psi`.
- Not correct if presented as already-formal paper labels or theorem names.

## Best current honest verdict
- The five reports are mostly useful and largely cite the right paper neighborhoods.
- The recurring source-audit risk is **promotion of theorem-shaping reductions into already-proved draft content**.
- Concretely: `T=v_7/c` is a patchwise derived hidden scalar, not a canonical draft definition; `C1/C2/C3` is a verifier-style decomposition, not a theorem stack stated in `proof_of_rh.tex`.
- No report I checked proves C or D from current paper text alone.