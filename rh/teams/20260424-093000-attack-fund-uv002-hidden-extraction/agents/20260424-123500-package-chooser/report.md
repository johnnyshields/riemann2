## Claim

If only one package-side theorem is pursued next, it should be **A. the corrected reduced-package diagonal-collapse theorem**, not **B. fiber-invariance of the first surviving odd jet on `\widetilde\Psi_{\min}` fibers**.

## Status

heuristic

## Evidence

- Bottleneck C is now stated in exact theorem form inside the draft: prove the corrected reduced package has the same reduced image germ at coincidence, or equivalently a diagonal-collapse / `\kappa`-independence statement on the exceptional divisor. The draft treats this as the cleanest provenance-sensitive package theorem still missing.
- The paper already says that once such a reduced-image-germ / collision-functoriality statement holds, the quotient-septic collapse becomes formal. So A is an upstream package theorem with direct formal payoff.
- The minimal-core reformulation in the draft explicitly organizes the finite-core program into two stages: first extract defect-corrected coincidence information for `\widehat\Psi`, then convert that information into the affine-line / extraction constraints. This makes C structurally prior to D.
- By contrast, the current team collation records that the proposed enlarged package `\widetilde\Psi_{\min}=(x,Y,S,T)` is only a credible enlarged candidate used to test hidden-state obstructions, and is still too ad hoc and gauge-dependent to replace the main theorem target. The queue note there says to stay centered on the abstract reduced-`\widehat\Psi` coincidence theorem.
- The extractor side is already complete (`H_m`, odd coefficients, `\Xi_\zeta^{(N)}`, finite-core localization), so the remaining bridge theorem in Bottleneck D should be attacked after the package-side coincidence object is stabilized. Pursuing B first risks proving fiber-invariance for a provisional package that may not be canonical enough.

## Exact refs

- `paper/proof_of_rh.tex:10780-10809`
- `paper/proof_of_rh.tex:12447-12559`
- `paper/proof_of_rh.tex:12586-12610`
- `paper/proof_of_rh.tex:21293-21329`
- `paper/proof_of_rh.tex:2214-2307`
- `paper/proof_of_rh.tex:2953-2969`
- `paper/proof_of_rh.tex:3984-4190`
- `paper/proof_of_rh.tex:5604-5643`
- `paper/proof_of_rh.tex:26369-26398`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-125`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-124`

## Dependencies

- The corrected reduced package must be defined canonically enough that diagonal value / coincidence at `\delta=0` is meaningful and comparable to the one-pair reduced package.
- The package-side coincidence theorem must control the actual corrected two-atom package, not merely a quotient-visible shadow.
- Any later hidden-state lemma for Bottleneck D should be formulated only after the canonical reduced package target is fixed.

## Strongest objection

The team collation also says Bottleneck D is now the deepest exact blocker, so one could argue for attacking B first. But that conclusion comes with the warning that `\widetilde\Psi_{\min}` is diagnostic only and not yet canonical. A theorem on fibers of a provisional gauge-dependent package risks solving the wrong abstraction layer.

## Needed for promotion

1. Show that the actual corrected reduced two-atom package has a `\kappa`-independent diagonal value at `\delta=0` agreeing with the one-pair reduced package.
2. Deduce same reduced image germ at coincidence / collision-functoriality from that diagonal-collapse statement.
3. Then formulate the hidden-state lemma for the stabilized reduced package, deciding whether extra visible data beyond reduced `\widehat\Psi` are still necessary.

Honest verdict: pursue **A** next. The draft treats reduced-package diagonal collapse as the last clean canonical package theorem, while the `\widetilde\Psi_{\min}` fiber-invariance proposal is still a diagnostic proxy for Bottleneck D rather than the theorem the queue should center on.
