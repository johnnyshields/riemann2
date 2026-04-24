# Claim

The next concrete attack on D-min is now sharper: from the current draft alone, the affine-bundle descent / `\ker\Phi_K` transport problem is **not** a missing pointwise highest-new scalar problem above normalized septic data. On the good overlap patch, the current explicit highest-new package is same-tower over the single source field \(r=q^{(7)}\), and no second primitive pointwise highest-new generator appears. Therefore any still-live failure of D-min must be genuinely **relational / transport-level / nonlocal**, not a missed local pointwise visible scalar beyond the affine lift-coordinate.

Equivalently, from the present explicit package formulas alone one can reduce D-min to the following smaller missing theorem:

> **D-min-rel.** Along corrected reduced-package fibers, any two corrected packages with the same normalized septic lift differ only by a relational/provenance-sensitive transport state whose contribution to the corrected odd block is in `\ker\Phi_K` through the first surviving odd order.

This is weaker than full finite determination and sharper than the earlier vague hidden-state statement.

# Status

open

# Evidence

- The order-`7` fixed-sector package is closed canonically only at quotient level:
  \[
  [A_7^{\mathfrak f}]\in \mathfrak f/\mathbf C A_5^{\mathfrak f},
  \qquad
  \Delta_7=\Delta_{7,K_1}.
  \]
  What remains non-unique is exactly the raw representative inside the affine line
  \[
  A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}.
  \]
  On `v_5\neq 0`, this is the affine lift-coordinate `T=v_7/c`.
- After my earlier reductions, the only visible order-`7` freedom over fixed `\widehat\Psi` is `T`. The new question is whether there is any *further* pointwise visible hidden state above this normalized septic lift.
- The same-tower closure theorem answers that for the **current explicit pointwise package** on a good overlap patch: every currently explicit pointwise highest-new field built from the quotient-septic package, overlap fields, dual tangent-line fields, and exact fixed-shear overlap constructions lies in
  \[
  K_{\mathrm{low}}\langle r\rangle,
  \qquad r=q^{(7)},
  \]
  and no second primitive pointwise highest-new generator appears.
- The theorem itself explicitly warns about scope: this covers only the present explicit pointwise package and does **not** address nonlocal, relational, or downstream transported-state obstructions. That caveat is exactly the remaining home of D-min.
- Independently, the stronger conditional package-collapse result on the involutive branch shows that **if** one had state-locality plus the natural merger law for the corrected two-pair package, then the interaction remainder vanishes identically there. So the residual burden is not another local symbolic coefficient identity; it is establishing the needed state-locality / merger transport theorem for the actual corrected package.
- Combining these gives a sharper negative conclusion from tested scope: from the current explicit local package formulas alone, there is no evidence for an additional local visible scalar beyond the normalized septic lift. Any surviving obstruction must come from how package state is transported or remembered across coincidence fibers, not from a missed local generator.

# Exact refs

- `rh/proof_of_rh.tex:7892-8033` — quotient-septic closure and local gauge-fixing of raw septic representatives.
- `rh/proof_of_rh.tex:21142-21217` — same-tower closure for the current explicit highest-new overlap/canonical package; no second primitive pointwise highest-new generator appears.
- `rh/proof_of_rh.tex:21219-21253` — best current external-looking rank-two coupling still remains same-tower over `r=q^{(7)}` and its derivative.
- `rh/proof_of_rh.tex:22472-22499` — stronger conditional package collapse on the involutive branch from state-locality plus merger law.
- `rh/proof_of_rh.tex:22507-22509` onward — any remaining residual obstruction on that corner is genuinely relational.
- Prior reductions in this agent dir:
  - `report.md` — reduction of D to the visible scalar `T=v_7/c`.
  - `notes/followup-finite-determination.md` — finite determination and `N\le 4` not derivable from current draft.

# Dependencies

- Bottleneck C, to identify corrected reduced-package fibers canonically.
- The earlier reduction of visible septic freedom to `T=v_7/c`.
- Same-tower closure and conditional state-local package collapse on the involutive branch.

# Strongest objection

This is still a scoped reduction, not a proof of D-min. Same-tower closure only rules out a second **currently explicit pointwise** highest-new generator; it does not exclude a hidden nonlocal transport scalar, branch-memory effect, or other provenance-sensitive datum that becomes `\Phi_K`-visible only after downstream package transport.

# Needed for promotion

1. Prove a corrected-package **state-locality / transport theorem**: once the normalized septic lift is fixed on a reduced-package fiber, all remaining higher-order package memory is relational but `\Phi_K`-invisible through the first surviving odd order.
2. Or prove the natural merger law for the actual corrected package on coincidence fibers strongly enough to invoke the involutive-branch collapse corollary.
3. Or construct an explicit counterexample schema showing how a nonlocal transported state could keep the same normalized septic lift while changing the first visible odd jet. That would sharpen D-min from “open” to a smaller relational obstruction.

# Autoresearch next step

- continue: attack the relational route directly by tracing where the draft still allows nonlocal / provenance-sensitive transported state after same-tower closure; specifically inspect the remarks immediately following `cor:stronger-state-local-package-collapse-fixed-shear-corner` and the exact fixed-shear residual package discussion to isolate the smallest missing state-locality axiom for D-min.
- verify: ask the adversarial verifier to test whether same-tower closure really rules out every additional local `\Phi_K`-visible scalar beyond `T`, or only the highest-new ones in the current explicit overlap package.
- blocked: coordinator should only intervene if a broader search across chats / older team dirs is needed for a prior state-locality theorem on the exact fixed-shear corner.
- terminal: not terminal; this note narrows D-min from a generic hidden-state theorem to a relational transport theorem.