Claim

Source check of `gap-closer-C-fiber-selection/report-cfs23-followup.md`, `notes/formal-countermodel-CFS23.md`, and `scripts/formal_countermodel.py`. The formal countermodel correctly stays within the currently audited weak source-supported properties and shows that C-FS3 cannot be derived from fixed codomain, `\mathcal R`, blow-up analyticity, swap-evenness, scalar normalization, and central-slope match alone. I found no paper line beyond the explicitly missing diagonal merger / same-reduced-image-germ / collision-functoriality targets that forbids adding `c^2\varepsilon\kappa` to the formal `\Delta` coordinate.

Status

open

Evidence

## Proved / source-supported

- The formal model uses the same fixed-codomain schema audited as conditional target:
  \[
  V_C=\mathbf C\times\mathfrak f\times\mathbf C,
  \qquad
  \mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2).
  \]
  This schema is not paper-constructed, but it is the accepted C target from the continuation audit.
- The blow-up chart uses
  \[
  \kappa=2\omega/\delta,
  \qquad t=\delta^2.
  \]
  Under swap `(\omega,\delta)\mapsto(-\omega,-\delta)`, both `\kappa` and `t` are invariant, so a term analytic in `(m,\kappa,t)` is swap-even in the blown-up chart. Paper support: `rh/proof_of_rh.tex:12385-12511`.
- The paper proves only the one-pair scaling law
  \[
  (c,A_5^{\mathfrak f},\Delta_7)\mapsto(\lambda c,\lambda A_5^{\mathfrak f},\lambda^2\Delta_7),
  \]
  and the invariant value `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)`. The model's `\Delta=c^2(Z+\varepsilon\kappa+tR)` has the corresponding homogeneous degree. Paper support: `rh/proof_of_rh.tex:11368-11450`.
- I reran the deposited script. Output:
  ```text
  R = (Y, X, Z + eps*kappa + r*t)
  B = (Y, X, Z + eps*kappa)
  swap_invariant = True
  dB3/dkappa = eps
  B_at_kappa_0 = (Y, X, Z)
  ```
  This verifies the algebraic reduction and the nonconstant exceptional trace within the formal model.

## Conditional

- The countermodel is conditional/scoped because it is not claimed to arise from the actual corrected two-atom whitening formulas. Its valid conclusion is independence from the weak audited properties, not falsity of C for the actual package.
- If a future theorem supplies actual diagonal merger, same reduced image germ at coincidence, or collision-functoriality for `\mathfrak P^{\corr}_2`, then the model is excluded by that additional theorem.

## Missing

- No audited paper source defines the actual corrected two-atom package as a fixed-codomain germ and then proves a constraint excluding
  \[
  \Delta\mapsto \Delta+c^2\varepsilon\kappa.
  \]
- The paper explicitly frames the needed source input as diagonal merger / collision-functoriality, not as a consequence of scaling or parity alone. Refs: `rh/proof_of_rh.tex:11888-12189`, `12513-12560`, `12562-12584`.

## Must-fix

- Any future C-FS3 closure must name the actual formula or theorem that kills `\partial_\kappa B_3`. Fixed codomain, scalar normalization, and swap-even blow-up analyticity are insufficient.
- Do not cite `\widehat\Psi` scaling, `\Delta_7` gauge invariance, or quotient-level order-7 closure as forbidding `c^2\varepsilon\kappa`; they do not address slope-independence of the exceptional divisor for the actual two-atom corrected package.

## Should-fix

- The countermodel report should remain labeled `computational` or `formal/scoped negative`, not `proved` about the actual package.
- When captured, phrase the reusable negative as: “From the currently audited formal properties alone, C-FS3 is not forced.” Do not overstate it as an actual obstruction to the corrected package.

## Nit

- The variable `\kappa` in this countermodel is the blow-up slope `2\omega/\delta`, not the one-pair coefficient named `\kappa(h)` in earlier local coefficient formulas; future notes should disambiguate if both appear nearby.

Baseline / delta

Baseline: final six-report source audit said C-FS2/C-FS3 were missing and scalar normalization was not diagonal collapse. Delta: this source check confirms the new formal countermodel is a valid scoped negative against deriving C-FS3 from the audited weak formal properties. It sharpens the source requirement: the missing theorem must explicitly kill `\partial_\kappa B`, not merely restate fixed codomain or homogeneous scaling.

Attempt status

keep

Exact refs

- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md:4-15`, `23-62`, `79-83`, `122-134` — countermodel claim, construction, bins, scope.
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/formal-countermodel-CFS23.md:17-65`, `77-96` — formal model and scoped consequence.
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/formal_countermodel.py` — algebraic verification; rerun output quoted above.
- `rh/proof_of_rh.tex:10780-10844` — quotient-level order-7 closure remains locally free; successful route must be provenance-sensitive.
- `rh/proof_of_rh.tex:11368-11450` — `\widehat\Psi` and scaling law only.
- `rh/proof_of_rh.tex:11888-12189` — diagonal merger is a hypothesis/input in the source-level criterion, not a theorem for the actual package.
- `rh/proof_of_rh.tex:12385-12511` — blow-up chart and parity/projective factorization WIP; reduction, not closure.
- `rh/proof_of_rh.tex:12513-12560` and `12562-12584` — same reduced image germ / collision-functoriality listed as conditional remaining package-level targets.
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-source-CDE/notes/source-check-CFS23-countermodel.md` — scratch source-check note.

Dependencies

- Depends on the final six-report source audit's classification of the fixed-codomain package as a schema/target, not paper-defined object.
- Depends on the paper's blow-up chart convention and scaling law.
- Does not depend on actual corrected two-atom formulas; this is why the result is only a scoped negative.

Strongest objection

The strongest objection is realizability: the formal deformation `\Delta\mapsto\Delta+c^2\varepsilon\kappa` may not come from the actual corrected two-atom whitening formulas or may violate a genuine merger/functoriality identity not included among the weak audited properties. That objection does not damage the stated scoped negative; it identifies exactly the missing theorem needed to promote C-FS3.

Needed for promotion

- To promote C-FS3, produce a source-supported theorem for the actual corrected package proving slope independence of `B(m,\kappa)`, e.g. diagonal merger / collision-functoriality / same reduced image germ.
- The proof must explicitly rule out the formal deformation `c^2\varepsilon\kappa` or show why the actual formulas cannot contain it.
- Re-submit to adversarial/source verification before any paper edit.

Honest verdict:

The C-FS3 countermodel is source-valid as a scoped formal negative. It correctly shows that current audited properties do not force `\kappa`-independence. No paper line beyond the missing diagonal-merger/collision-functoriality family forbids the `c^2\varepsilon\kappa` addition. This does not refute C for the actual corrected package; it blocks a weak proof route and sharpens the missing source theorem.

Autoresearch next step

continue: source-check the next C-FS2 actual-formula inspection; require it to distinguish no-extra codomain state from slope-independence.
verify: adversarial verifier should test any C-FS3 proof by asking exactly where `c^2\varepsilon\kappa` is excluded.
blocked: no source-auditor blocker; C-FS3 promotion remains blocked by missing actual package merger/functoriality.
terminal: terminal for the weak route “derive C-FS3 from fixed codomain + `\mathcal R` + blow-up/swap/scaling”; not terminal for C.
