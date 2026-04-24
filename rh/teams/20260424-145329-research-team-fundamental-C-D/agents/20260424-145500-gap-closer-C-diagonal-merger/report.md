Claim

Bottleneck C does not close from the present draft, but it reduces to one exact package-side axiom set. Let
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ \mathfrak P^{\corr}_2
\]
be the corrected reduced two-atom package in the blow-up chart \(2\omega=\kappa\delta\). Then
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]
is forced once the actual corrected package satisfies the same three merger axioms already isolated abstractly in the source-level lemma, transported to the corrected reduced package:

1. swap symmetry;
2. one-amplitude collapse;
3. diagonal merger / collision-functoriality at coincidence.

More precisely, the smallest honest unresolved sub-statements are:

- **C1. Well-posed blow-up object.** Define the actual corrected package \(\mathfrak P^{\corr}_2\) on the collision/cancellation chart with analytic extension of \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) to \(\delta=0\).
- **C2. Diagonal merger on the corrected package.** For coincident atoms,
  \[
  \mathfrak P^{\corr}_2(a_1,m;a_2,m)
  =
  \mathfrak P^{\corr}_1(a_1+a_2,m),
  \]
  equivalently after reduction,
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)
  \text{ is independent of }\kappa.
  \]
- **C3. Reduced identification.** The merged one-pair package reduces to \(\widehat\Psi(m)\).

Among these, only C2 is genuinely open on the current draft; C1 and C3 are mostly formalization/normalization once the corrected package object is fixed. Route B gives a narrower conditional form: on the involutive fixed-shear branch, state-locality plus the natural merger law already imply package collapse, so the unresolved issue is extending that merger law from the descended-state model to the actual corrected package on the full collision chart.

Status

open

Evidence

The paper already proves an abstract finite-dimensional lemma: any analytic two-atom package with swap symmetry, one-amplitude collapse, and diagonal merger has interaction remainder divisible by \(a_1a_2(h_1-h_2)^2\). So the structural theorem shape is known. The draft also states explicitly that the live two-point burden is to verify these identities for the actual corrected package, and separately offers a weaker quotient-diagonal route requiring continuity plus exact diagonal collapse.

For Bottleneck C, the prior cycle already sharpened the target from vague “same reduced image germ” to the exact exceptional-divisor identity
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]
with the obstruction named as the free analytic trace
\[
B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0).
\]
The blow-up parity/projective factorization remark only yields \(\delta^2\)-divisibility for corrected defects; it does not constrain the value of \(B(m,\kappa)\). So analyticity and swap-evenness alone are too weak.

The cleanest reduction is therefore: prove the actual corrected package enjoys the same diagonal merger principle already isolated abstractly. Then \(\kappa\)-independence is formal, and identification with \(\widehat\Psi\) is the normalization of the merged one-pair package. Without that theorem, the current hypotheses leave a completely free analytic exceptional-divisor function.

A useful partial redirect appears later on the involutive fixed-shear branch: if the corrected package is state-local in a descended state \(\mathcal T_N\) and obeys the natural merger law \(\mathfrak P_2(a_1,a_2;Y,Y)=(a_1+a_2)\mathfrak F(Y)\), then package collapse is formal there. This supports the diagnosis that the true missing ingredient is merger/functoriality, not further local blow-up algebra.

Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11888-12040` — abstract source-level lemma: swap symmetry + one-amplitude collapse + diagonal merger imply quadratic two-point factorization.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12042-12088` — weaker exact route via continuity plus diagonal collapse of the actual corrected two-atom quotient germ.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12139-12165` — the weaker exact route is explicitly a continuity/diagonal-collapse problem.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12168-12189` — exact remaining source-level input: swap symmetry, one-amplitude collapse, diagonal merger for the actual corrected two-atom package.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12447-12511` — blow-up parity/projective factorization only gives \(\delta^2\mathcal H(m,\kappa,\delta^2)\), not diagonal-value rigidity.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12513-12559` — remaining burden compressed to exact fixed-shear quotient transport, package-level coincidence/functoriality, and related fronts.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12586-12610` — downstream reduced target datum is \(\widehat\Psi\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11303-11307` — what remains architectural is verification for the actual corrected two-atom package and extension to multi-pair/minimal-core.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:24524-24536` — current live route restated: verify the three identities for the actual corrected package, or else the weaker quotient route.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:22472-22490` — on the involutive branch, state-locality plus natural merger law imply stronger package collapse.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-78` — prior-cycle sharpening of C to the exact identity with free exceptional-divisor term \(B(m,\kappa)\).
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md:20-24` — current cycle briefing: real blocker is \(\kappa\)-independence / diagonal merger for \(\mathfrak P_2^{\corr}\).
- UV refs: `UV-002`, `UV-003`, `UV-007`; labels `rem:wip-pairlike-finitecore`, `rem:wip-parity-projective-factorization-collision-blow-up`, `rem:wip-final-endgame-status`.

Dependencies

- A precise definition of the corrected two-atom package object \(\mathfrak P^{\corr}_2\) and of its reduction map \(\mathcal R\).
- Analytic extension of \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) to the exceptional divisor in the blow-up chart.
- A theorem transferring diagonal merger / collision-functoriality from coincident atoms to the corrected reduced package.
- Identification of the merged one-pair package with the amplitude-invariant datum \(\widehat\Psi(m)\).
- For the narrower Route B variant: state-locality on the involutive branch and the natural merger law there.

Strongest objection

This reduction still relies on a nontrivial inference: that once the corrected package is formalized, C1 and C3 are merely bookkeeping while C2 is the only real theorem. If the actual corrected package carries extra hidden gauge/state not removed by \(\mathcal R\), then diagonal merger at the unreduced level may not descend cleanly, and the split “formalization vs real blocker” could be too optimistic. The involutive-branch corollary supports the diagnosis but does not prove the full collision-chart statement.

Needed for promotion

- Define \(\mathfrak P^{\corr}_2\) and \(\widetilde\Psi^{\corr}_{\mathrm{red}}\) canonically on the collision/cancellation chart.
- Prove the exact corrected-package diagonal merger theorem
  \[
  \mathfrak P^{\corr}_2(a_1,m;a_2,m)=\mathfrak P^{\corr}_1(a_1+a_2,m)
  \]
  or an equivalent collision-functoriality statement strong enough to force \(\kappa\)-independence of the exceptional-divisor trace.
- Show that the merged one-pair reduction is exactly \(\widehat\Psi(m)\).
- Failing full closure, it is enough to prove a descended-state version on the full collision chart, not just on the involutive branch, together with a theorem that the actual corrected package factors through that descended state.

Honest verdict: I do not see a direct proof of Bottleneck C from the present draft. The honest gain is a sharper reduction: C is equivalent to a concrete diagonal-merger / collision-functoriality theorem for the actual corrected package, with the smallest unresolved list now C1–C3 above and the only genuinely hard item appearing to be C2.