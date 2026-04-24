# Report: C fiber selection

## Claim

Bottleneck C is not closed by the current affine septic-lift local model. The correct reduced object for C has already quotiented away raw septic representatives; the surviving obstruction is the exceptional-divisor trace
\[
B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0),
\]
not the local representative coordinate \(T=v_7/c\) or a patch cocycle for \(\lambda/c\). The sharpest current reduction is a four-part fiber-selection theorem: construct the actual corrected two-atom exceptional-divisor package, prove no C-codomain state survives beyond a single trace \(B(m,\kappa)\), prove diagonal merger makes \(B\) independent of \(\kappa\), and identify the common value with \(\widehat\Psi(m)\).

## Status

open

## Evidence

[proved] The one-pair order-
\(7\) fixed-sector package supplies only canonical quotient data and determinant data. The paper proves the fixed-sector septic ambiguity is exactly the affine line
\[
A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f},
\]
with raw local gauges \(v_7=0\) or \(u_7=0\), and that \([A_7^{\mathfrak f}]\) and \(\Delta_7\) are unaffected by this raw representative choice. This supports the local affine-lift model but does not construct the actual corrected two-atom exceptional-divisor object.

[proved] The amplitude-invariant one-pair target is
\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right),
\]
and its scaling law makes it the right reduced diagonal value once a merger law exists. The exact strengthened two-pair coincidence proposition shows how cubic/quintic/septic quotient identities imply equality of \(\widehat\Psi\), but it does not prove those identities for the actual corrected two-atom package.

[proved] The source-level route already isolates the necessary merger identity
\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h,
\]
and the draft states this as an open source-level input. The weaker quotient route also leaves continuity plus diagonal collapse of the actual corrected two-atom quotient germ as assumptions.

[proved] The collision-cancellation chart gives the correct blow-up variables and the parity/projective factorization template. But after setting \(\kappa=2\omega/\delta\), analyticity and swap-evenness allow an arbitrary exceptional-divisor trace
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,\delta)=B(m,\kappa)+\delta^2R(m,\kappa,\delta^2).
\]
They do not force \(B(m,\kappa)=\widehat\Psi(m)\).

[confirmed] First-wave C work already proved that the local affine-lift patch transition is base-controlled: on the overlap \(u_5v_5\neq0\),
\[
S_u=-\frac{x}{Y}S_v,
\qquad
\frac{\Delta_7}{u_5v_5}=\frac{\Delta_7/c^2}{(u_5/c)(v_5/c)}.
\]
Thus patching is not the hidden obstruction. The current pass adds the negative clarification that this local representative affine line is not itself the C trace: the proposed C object \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\) and reduction \(\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)\) deliberately remove raw septic gauge.

[missing] No source in the current draft proves that the actual corrected two-atom package has no relational/provenance-sensitive exceptional-divisor datum beyond the reduced trace \(B(m,\kappa)\). No source proves the diagonal-merger theorem that kills the \(\kappa\)-dependence of \(B\). The fixed-shear quotient-visible transport results rule out finite quotient-visible resets from their tested scope, but they explicitly leave actual corrected package state-locality open.

## Baseline / delta

Baseline before this pass: C was reduced to fiber selection after the affine-lift cocycle was shown to be base-controlled. The strongest obstruction was that the actual corrected two-atom package might carry extra hidden dependence invisible in the one-pair affine-lift model.

Delta from this pass: the C fiber is sharpened away from raw septic representative selection. The raw affine line \(A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}\) is one-pair gauge freedom; Bottleneck C concerns the exceptional-divisor trace of \(\mathcal R\circ\mathfrak P_2^{\corr}\). Therefore a valid C proof must establish an actual corrected two-atom package theorem, not merely choose a local gauge section. This leaves a smaller list of concrete missing statements C-FS1--C-FS4 below.

## Attempt status

keep

## Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7004-7062` — fixed-sector quintic/septic coefficients, \(\Delta_7\), quotient-level order-
  \(7\) interpretation, raw representative non-canonicity.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7065-7191` — projected septic gauge law and gauge invariance of \(\Delta_7\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7892-8003` — quotient-septic closure and affine line of raw septic representatives.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:8004-8033` — local gauges \(v_7=0\) and \(u_7=0\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11368-11450` — definition and scaling law of \(\widehat\Psi\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11476-11585` — exact strengthened two-pair coincidence through order \(7\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` — source-level factorization criterion and open diagonal-merger input.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12192-12228` — naive source-summed whitened model cannot supply one-atom linearity.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12385-12511` — collision-cancellation chart and parity/projective factorization frontier.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12513-12610` — remaining two-pair/package-level fronts and minimal-core target \(\widehat\Psi\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:22380-22640` and `23072-23108` — no finite quotient-visible hidden reset from tested fixed-shear scope, and actual state-local/package collapse remains open.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:26369-26398` — final endgame still acknowledges raw order-
  \(7\) ambiguity and finite-core branch.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md:106-118` — current C obstruction: patching controlled; fiber selection remains.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-C-diagonal-merger/report.md:1-101` — prior C affine-lift patch-cocycle reduction.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-C-diagonal-merger/notes/20260424-followup-patch-transition-controlled.md:1-40` — patch-transition calculation.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-package-functoriality/report.md:1-73` — C as package functoriality/descent.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md:1-68` — fixed-ambient triple \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\).
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-133500-C-failure/report.md:1-76` — scoped no-go: reduced blow-up hypotheses leave free \(B(m,\kappa)\).
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/fiber-selection-reduction.md` — scratch reduction for this pass.
- UV refs: UV-002 (`rem:wip-pairlike-finitecore` at `rh/proof_of_rh.tex:5605`) and UV-003 (`rem:wip-parity-projective-factorization-collision-blow-up` at `rh/proof_of_rh.tex:12448`).

## Dependencies

- One-pair fixed-sector package and quotient-septic closure.
- The fixed-ambient corrected two-atom package candidate \(\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\).
- The reduction map \(\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)\).
- Collision-cancellation chart convention: \(2\omega=\kappa\delta\), analytic continuation to \(\delta=0\).
- A not-yet-proved actual package functoriality / diagonal-merger theorem.
- A not-yet-proved no-extra-exceptional-state theorem excluding relational/provenance-sensitive two-atom data in the C codomain.

## Strongest objection

The report still does not construct \(\mathfrak P_2^{\corr}\) from the actual corrected two-atom formulas. It only shows that the local affine-lift fiber should not be mistaken for a proof of C and reduces the missing theorem to C-FS1--C-FS4. A future construction of the corrected package might reveal either no extra state, as hoped, or an additional relational/provenance-sensitive exceptional-divisor datum not represented by the one-pair affine-line model.

## Needed for promotion

1. **C-FS1: corrected exceptional-divisor package.** Define \(\mathfrak P_2^{\corr}\) as an analytic fixed-codomain two-atom germ on the collision chart \((m,\kappa,\delta^2)\), with \(\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P_2^{\corr}\) extending to \(\delta=0\).
2. **C-FS2: no extra exceptional state.** Prove that, after reduction, the actual corrected package on \(\delta=0\) carries no relational/provenance-sensitive C-codomain datum beyond a single trace \(B(m,\kappa)\).
3. **C-FS3: diagonal merger / slope independence.** Prove \(B(m,\kappa)=B_0(m)\), not from analyticity or swap-evenness alone, but from actual collision functoriality of the corrected package.
4. **C-FS4: diagonal identification.** Prove \(B_0(m)=\widehat\Psi(m)\), using compatibility with one-amplitude collapse and the scaling law of \(\widehat\Psi\).
5. Adversarially test C-FS2 against possible hidden two-atom relational data and C-FS3 against the known free-trace model \(B(m,\kappa)\).

## Honest verdict

C remains open. The useful advance is negative/sharpening: the affine septic-lift local model is coherent and its patch cocycle is base-controlled, but it is not yet the actual corrected two-atom exceptional-divisor theorem. The raw one-pair affine line is gauge freedom; Bottleneck C is the slope-dependent exceptional trace of the reduced corrected two-atom package. The smallest honest target is C-FS1--C-FS4, with C-FS2 and C-FS3 the live fiber-selection blockers.

## Autoresearch next step

continue: attack C-FS2 directly by searching the corrected two-atom formulas for the first relational/provenance-sensitive datum that is not represented in \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\); if none appears in the finite order-
\(7\) package, formulate a conditional no-extra-state theorem with explicit scope.

verify: adversarial verifier should try to build a model with the same one-pair affine-lift cocycle and same reduced base \(\widehat\Psi\), but with a nonconstant analytic trace \(B(m,\kappa)\) or an extra two-atom relational datum surviving \(\mathcal R\).

blocked: no coordinator action required; promotion is blocked by missing C-FS1--C-FS4 proof, not by file access or source ambiguity.

terminal: not terminal; the target is reduced, not closed.
