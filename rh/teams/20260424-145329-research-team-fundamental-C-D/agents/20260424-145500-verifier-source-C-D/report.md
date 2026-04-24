Claim

Second-pass source audit of the current C/D research deposits. The reports mostly cite the right paper neighborhoods, but two recurrent source-discipline failures remain: theorem-shaping reductions are sometimes stated as if they were already formalized in the draft, and patchwise derived coordinates are sometimes spoken of as canonical global package data.

Status

open

Evidence

## Must-fix

- **`gap-closer-C-diagonal-merger/report.md`: the C1/C2/C3 split is an audit decomposition, not a paper-stated theorem stack.** The cited draft lines support: the abstract merger lemma; the weaker quotient-diagonal route; the exact remaining source-level input; and the collision/cancellation blow-up setup. They do not define named obligations `C1`, `C2`, `C3` in the paper. So this split is useful, but it must be labeled as a derived reduction. In particular, the further claim that only C2 is “genuinely open” is stronger than the cited draft support, because C1 still depends on a corrected package object and analytic extension that are not theorem-level in the current text.
- **`gap-closer-D-kerphik/report.md`: `T=v_7/c` is a patchwise hidden scalar, not a canonical draft definition.** The cited paper lines do support the algebra
  \[
  A_5^{\mathfrak f}=u_5I+v_5S,
  \qquad
  A_7^{\mathfrak f}=u_7I+v_7S,
  \qquad
  \Delta_7=u_7v_5-u_5v_7,
  \]
  and the gauge law, as well as the amplitude-invariant datum \(\widehat\Psi\). But the reduction to a single visible scalar
  \[
  T:=v_7/c
  \]
  is a local algebraic reduction on a \(v_5\)-patch, not a canonical global package theorem presently stated in the draft. The report is honest later about this, but the source basis does not justify treating `T` as already formalized package data.
- **`gap-closer-UV002-contradiction/report.md`: “becomes formal” overstates the current source support.** The cited lines do support the queue `C \to D \to` finite-core endgame rewrite. But the rewrite itself is still a real theorem obligation, not mere bookkeeping: `rem:wip-final-endgame-status` says the general branch still needs reformulation in terms of the first nonzero odd jet. So C and D do not yet make the contradiction formal in the ordinary proof sense.

## Should-fix

- **`explorer-package-functoriality/report.md` is structurally plausible but partly unsourced as a paper claim.** The cited lines support the target datum \(\widehat\Psi\), the abstract merger-axiom template, and the statement that the live burden is package-level / provenance-sensitive. They do not yet support the proposed “universal property” or “projective descent” reformulation as a theorem already latent in the paper. Those parts should remain tagged as candidate structure.
- **`explorer-support-lanes/report.md` cites the mixed residual corner correctly, but its D-language is theorem-shaping.** The residual-corner lines support the claim that quotient-visible finite transport is already compressed and that any still-live obstruction must be provenance-sensitive or non-finite-order. They do not yet prove that the first surviving `\Phi_K`-visible odd coefficient is fiber-constant modulo `\ker\Phi_K`; that remains the proposed D theorem.
- **Across the reports, “corrected reduced-package fiber” still lacks one canonical theorem-definition in the draft.** Several reports use it coherently, but source-audit wise it remains a cycle term of art. Any promotion path must define the package / fiber object explicitly rather than rely on shared team shorthand.

## Nit

- The line references for current draft labels should use the actual current lines, e.g. `rem:wip-explicit-pointwise-bridge-good-patch-detector` at line 21278 and `rem:wip-final-endgame-status` at line 26370.
- In the fixed-sector basis, the one-pair package section uses `(I,S,D,J)`, while later coefficient extraction for D uses `(I,D,S,K)`. Reports should signal this basis translation explicitly to avoid accidental symbol drift between `J` and `K`.

Exact refs

- `rh/proof_of_rh.tex:7004-7190` — fixed-sector quintic/septic coefficients, `\Delta_7`, septic gauge law.
- `rh/proof_of_rh.tex:11368-11585` — amplitude-invariant strengthened datum `\widehat\Psi` and exact strengthened two-pair coincidence.
- `rh/proof_of_rh.tex:11888-12040` — abstract merger lemma for quadratic two-point factorization.
- `rh/proof_of_rh.tex:12042-12166` — weaker quotient-diagonal route.
- `rh/proof_of_rh.tex:12168-12228` — exact remaining source-level input and naive source-summed obstruction.
- `rh/proof_of_rh.tex:12777-12792` — lifted `v_5`-patch coordinates.
- `rh/proof_of_rh.tex:10780-10809` — honest order-7 target is package-level coincidence / collision-functoriality, not raw septic equality.
- `rh/proof_of_rh.tex:24166-24210` — mixed local exhaustion and `C_1=C_3=C_5=0` finite scalar descent target on the clean branch.
- `rh/proof_of_rh.tex:24518-24612` — live attack routes; actual package merger vs weaker quotient route; residual exact fixed-shear corner.
- `rh/proof_of_rh.tex:24985-25030` — finite-core split; local blow-up regularity + quotient transport + package-level coincidence.
- `rh/proof_of_rh.tex:25420-25485` — residual corner compressed to quotient-visible finite transport; remaining issue is provenance-sensitive or non-finite-order.
- `rh/proof_of_rh.tex:26370-26398` — present endgame still pair-like; general branch still needs first-nonzero-odd-jet reformulation.
- Audited deposits:
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-package-functoriality/report.md`
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-C-diagonal-merger/report.md`
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-D-kerphik/report.md`
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-UV002-contradiction/report.md`
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-support-lanes/report.md`
- Supporting note deposited here:
  - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-verifier-source-C-D/notes/second-pass-audit-current-deposits.md`

Dependencies

- A clear distinction between (i) what the draft currently proves, (ii) what current cycle reports derive as the sharpest reduction, and (iii) what remains only candidate structure.
- For C: a theorem-level corrected package object and diagonal-merger / collision-functoriality statement.
- For D: a theorem-level package-to-transform bridge modulo `\ker\Phi_K`, not only patchwise septic algebra.

Strongest objection

The current deposits are generally careful, but they lean on a real temptation: once a reduction is sharp and repeated across cycles, it begins to read like an existing theorem. Source-audit wise that is still a defect. The present draft does not yet contain theorem-level definitions of the corrected reduced-package fiber or a canonical global hidden scalar `T`; those are report-level reductions, not yet paper-level facts.

Needed for promotion

- When using `C1/C2/C3`, label them explicitly as a verifier / report decomposition unless and until the paper states them as named subtheorems.
- When using `T=v_7/c`, state the patch hypothesis `\{c\neq 0, v_5\neq 0\}` and treat `T` as a local derived scalar, not a canonical package coordinate.
- Keep D phrased at transform level: constancy modulo `\ker\Phi_K`, equivalently constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers.
- Keep the UV-002 stack phrased honestly as `C + D + finite-core endgame rewrite`, where the third item is still a genuine theorem obligation.

Honest verdict:

The deposits are useful and mostly source-aware. The main corrections are about status discipline, not line-hunting: `T=v_7/c` is sourced only as a patchwise derived scalar, and the `C1/C2/C3` split is sourced only as a sharp audit decomposition. Neither is yet a theorem-level object of the draft. So the right verdict is: the reports sharpen the queue correctly, but they do not convert those sharpenings into already-proved paper content.