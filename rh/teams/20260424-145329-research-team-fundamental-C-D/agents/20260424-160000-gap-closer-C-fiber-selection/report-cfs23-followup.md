# Follow-up report: C-FS2 / C-FS3

## Claim

Route A succeeds as a scoped countermodel to C-FS3. There is an explicit formal fixed-codomain package with
\[
V_C=\mathbf C\times\mathfrak f\times\mathbf C,
\qquad
\mathcal R(C,UI+VS,\Delta)=\left(U/C,V/C,\Delta/C^2\right),
\]
analytic blow-up coordinates \((m,\kappa,t)\), \(t=\delta^2\), swap-evenness, scalar-normalized homogeneous degrees \((1,1,2)\), and central-slope value \(\widehat\Psi(m)\), but with nonconstant exceptional trace
\[
B(m,\kappa)=\bigl(Y(m),X(m),Z(m)+\varepsilon\kappa\bigr),
\qquad \varepsilon\neq0.
\]
Thus C-FS3 does not follow from fixed codomain, reduction, blow-up analyticity, swap-evenness, or scalar normalization alone. A genuine diagonal-merger / collision-functoriality theorem is necessary. The model also separates C-FS2 from C-FS3: even with no extra codomain coordinate beyond \((C,A^{\mathfrak f},\Delta)\), C-FS3 can fail.

## Status

computational

## Evidence

Define a formal package germ in the collision blow-up chart
\[
2\omega=\kappa\delta,
\qquad t=\delta^2.
\]
Under atom swap \((\omega,\delta)\mapsto(-\omega,-\delta)\), both \(\kappa\) and \(t\) are invariant. Let
\[
C=c(m),
\qquad
U=c(m)Y(m),
\qquad
V=c(m)X(m),
\]
and
\[
\Delta=c(m)^2\left(Z(m)+\varepsilon\kappa+tR(m,\kappa,t)\right).
\]
Then
\[
\mathfrak P_{\mathrm{toy}}(m,\kappa,t)=(C,UI+VS,\Delta)
\in \mathbf C\times\mathfrak f\times\mathbf C.
\]
Applying the reduction gives
\[
\mathcal R(\mathfrak P_{\mathrm{toy}})
=\left(Y(m),X(m),Z(m)+\varepsilon\kappa+tR(m,\kappa,t)\right).
\]
On the exceptional divisor \(t=0\),
\[
B(m,\kappa)=\left(Y(m),X(m),Z(m)+\varepsilon\kappa\right),
\]
so
\[
\partial_\kappa B_3=\varepsilon\neq0.
\]
If \(Z(m)=\Delta_7(m)/c(m)^2\), then at \(\kappa=0\) the central value is
\[
B(m,0)=\widehat\Psi(m).
\]
The model still fails slope-independence.

Script check:

- Script: `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/formal_countermodel.py`.
- Output excerpt:

```text
R = (Y, X, Z + eps*kappa + r*t)
B = (Y, X, Z + eps*kappa)
swap_invariant = True
dB3/dkappa = eps
B_at_kappa_0 = (Y, X, Z)
```

This verifies the algebraic reduction, swap invariance in the blow-up chart, and nonconstant \(B\).

Three-bin result:

- [proved/computational] The formal properties above are compatible with nonconstant \(B(m,\kappa)\).
- [conditional] If a future theorem proves the actual corrected package has diagonal merger, the model is excluded by that extra theorem.
- [missing] No current audited source supplies that diagonal-merger theorem for the actual corrected package.

## Baseline / delta

Baseline: verifier reviews left C-FS2/C-FS3 as the primary C frontier. Prior reports already noted the free-trace template
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,
\delta)=B(m,\kappa)+\delta^2R(m,\kappa,\delta^2)
\]
as admissible under analyticity and swap-evenness.

Delta: the present pass constructs a concrete fixed-codomain formal package realizing that freedom while satisfying the exact reduction \(\mathcal R\) and the homogeneous scalar normalization. This is stronger than the prior abstract free-trace warning. It shows C-FS3 is independent of C-FS2 at the level of formal axioms: a package can land in \(\mathbf C\times\mathfrak f\times\mathbf C\) with no extra coordinate and still retain a slope-dependent third reduced component.

## Attempt status

keep

## Exact refs

- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/formal-countermodel-CFS23.md` — formal construction and scope.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/formal_countermodel.py` — algebraic verification script.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report.md:100-106` — C-FS1--C-FS4 reduction.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/report.md:15-43`, `143-151` — adversarial C kill condition and promotion requirements.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-source-CDE/report.md:75-80`, `89-99` — source audit: C-FS2/C-FS3 missing and scalar normalization not diagonal collapse.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-explorer-corrected-package-object/report.md:1-37`, `73-82` — fixed-codomain package schema and C-FS map.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11368-11450` — \(\widehat\Psi\) and scaling law.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` — diagonal merger is an input in the source-level criterion.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12385-12511` — collision-cancellation chart and parity/projective factorization.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12513-12610` — remaining two-pair/package-level fronts.

## Dependencies

- The formal model uses the fixed C codomain and reduction map from the current C package schema.
- It depends on the blow-up convention \(2\omega=\kappa\delta\), with \(t=\delta^2\), and the induced swap invariance of \((\kappa,t)\).
- It uses the scalar-normalization scaling pattern \((C,A,\Delta)\mapsto(\lambda C,
\lambda A,
\lambda^2\Delta)\).
- It does not depend on the actual corrected two-atom formulas; therefore it is a scoped independence/countermodel result, not a proof that the actual package has nonconstant \(B\).

## Strongest objection

The countermodel is formal. It may not be realizable by the actual corrected two-atom whitening formulas or by any package respecting true one-amplitude collapse and diagonal merger. That objection is exactly the point: those true package-functoriality identities are additional missing theorems. The countermodel only rules out proving C-FS3 from the weaker currently audited properties.

## Needed for promotion

- Treat the following as a reusable negative: fixed codomain, \(\mathcal R\), blow-up analyticity, swap-evenness, scalar normalization, and a central-slope match to \(\widehat\Psi\) do not force \(B(m,\kappa)\) to be constant.
- To promote C, supply an actual package theorem excluding the \(\varepsilon\kappa\) deformation. The theorem can be either:
  1. diagonal collision functoriality / merger for \(\mathfrak P_2^{\corr}\); or
  2. a stronger source-level identity implying \(\partial_\kappa B=0\) on the exceptional divisor.
- For C-FS2, still inspect actual order-
  \(3,5,7\) corrected two-atom formulas for relational/provenance-sensitive data. This countermodel does not settle C-FS2; it shows C-FS2 alone is insufficient for C-FS3.
- Submit any proposed diagonal-merger proof to adversarial review against the explicit \(\varepsilon\kappa\) deformation.

## Honest verdict

C-FS3 is formally independent of the currently audited C package properties. The next proof cannot be a scalar-normalization, fixed-codomain, or swap-evenness argument. It must use real collision functoriality of the actual corrected package. C-FS2 remains open as an actual-formula question, but even a positive C-FS2 no-extra-codomain-state result would not close C unless it also kills the slope-dependent \(\varepsilon\kappa\) deformation.

## Autoresearch next step

continue: inspect actual corrected two-atom order-
\(3,5,7\) formulas for C-FS2, focusing on whether any relational/provenance-sensitive datum can enter \(\Delta^{\corr}\) while preserving the fixed codomain; if no such datum appears, formulate a conditional theorem: “through order \(7\), assuming the package is exactly the fixed triple and all two-atom dependence enters only via \((C,A^{\mathfrak f},\Delta)\), C-FS2 holds, but C-FS3 remains a separate merger axiom.”

verify: adversarial verifier should test any C-FS3 proof against the explicit deformation \(\Delta\mapsto\Delta+c^2\varepsilon\kappa\), and source verifier should ask which actual corrected formula forbids this term.

blocked: no coordinator blocker; route A completed as a scoped countermodel. Route B actual-formula inspection remains.

terminal: terminal only for the false subroute “derive C-FS3 from fixed codomain + \(\mathcal R\) + blow-up/swap/scalar normalization.” Not terminal for C-FS2/C-FS3 overall.
