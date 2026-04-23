## Claim

The cleanest theorem-facing paired analogue of the manuscript's pure value-channel deformation
\[
q_1=q_2=B+\alpha
\]
is a one-scalar paired background shift after the paired local symmetric normal form is fixed:

\[
q_{\chi,1}^{\pair}=q_{\chi,2}^{\pair}=B_\chi^{\pair}(m)+\alpha,
\qquad
S_\chi^{\pair}(m)=\alpha,
\]

with all derivative, curvature, and other non-value local data frozen at their paired background values. Equivalently, one deforms only the common paired value slot and keeps the rest of the paired corrected local family fixed. The corresponding theorem-facing derivative should then be defined by

\[
A_{\val,\chi}^{\pair}(m,\sigma)
:=
\left.\frac{\partial}{\partial \alpha}
\widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\right|_{\alpha=0},
\]

where \(\widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\) is the paired corrected whitened block under that pure paired value-channel deformation.

What must be fixed before this derivative is well-defined is not mainly the derivative formula itself, but the paired corrected-whitening interface: one must first specify the paired corrected same-point and mixed blocks, prove microscopic holomorphy, state an explicit same-point positivity/nondegeneracy hypothesis strong enough to define holomorphic inverse-square-root whitening, and only then define the first derivative in the pure paired value direction.

Honest theorem-facing split:

- proved: this is exactly the right manuscript-shaped local template in the unpaired model;
- conditional: the same one-scalar paired template is the cleanest safe paired formulation;
- missing: a paired local theorem that makes the common paired value slot and its corrected whitening package explicit enough to prove that \(A_{\val,\chi}^{\pair}\) is canonically defined.

## Status

conditional

## Evidence

**Proved.**

- In the manuscript's local model, the pure value channel is genuinely one-scalar: `proof_of_rh.tex:446-469` perturbs the two local values by the same parameter \(\alpha\), freezing all derivative and curvature data, and defines \(A_{\val}\) as the first derivative at \(\alpha=0\).
- In the corrected-whitened setting, `proof_of_rh.tex:1531-1621` again uses a one-scalar background expansion: the corrected local deformation is expanded around background value-channel parameter \(S(m)=0\), and the first-order coefficient is exactly the pure value-channel derivative.
- `paired_aval.md:7-28` already isolates the safe paired transport rule: the theorem-facing paired object is the first derivative of the paired corrected whitened local block in the pure paired value channel, taken at paired background value \(S_\chi^{\pair}(m)=0\).
- `paired_slot_hypotheses.md:12-29,31-59` fixes the minimal analytic package: exact paired source scalar \(S_\chi^{\pair}\), paired local symmetric normal form, microscopic holomorphy, same-point positivity/nondegeneracy, holomorphic whitening, and then the first-order paired value-channel derivative.

**Conditional on [paired local symmetric slot realization + corrected whitening admissibility].**

- The cleanest paired deformation is still one-scalar, not a two-parameter perturbation. The manuscript's role of \(q_1=q_2=B+\alpha\) is: one common value slot varies, everything else is frozen. The closest faithful paired translation is therefore: after the paired local symmetric normal form identifies the common paired value slot, set that slot equal to \(B_\chi^{\pair}(m)+\alpha\), equivalently \(S_\chi^{\pair}(m)=\alpha\).
- This formulation is cleaner than trying to transport the explicit toy-matrix formula from `prop:explicit-Aval`. What survives theorem-facingly is the one-scalar deformation direction inside the corrected paired whitened family, not the explicit unpaired closed form.
- The derivative is well-defined only after the paired corrected blocks are themselves well-defined on a microscopic disk and the same-point blocks stay positive/nondegenerate there so that the holomorphic inverse square roots exist. This follows the exact logic of `proof_of_rh.tex:1392-1414` and `1569-1606`.
- The safest wording is therefore local and conditional: `Assume the compact-interval paired source package, the paired local symmetric normal form, and same-point positivity/nondegeneracy for holomorphic whitening. Then the pure paired value-channel derivative is the first derivative of the paired corrected whitened block with respect to the common paired value scalar alpha at alpha=0.`

**Missing.**

- A paired proposition that explicitly writes the analogue of the manuscript's common-value slot, rather than only referring abstractly to \(S_\chi^{\pair}\) or to a paired corrected family.
- A paired theorem proving that the corrected same-point and mixed blocks are holomorphic on a microscopic disk and that the same-point blocks remain sufficiently positive/nondegenerate there for holomorphic inverse-square-root whitening.
- A paired proof that the exact coefficient of the first-order corrected-whitening expansion is the same compact-interval scalar \(S_\chi^{\pair}(m)\), not merely a nearby paired source quantity.
- Any paired explicit formula analogous to the unpaired explicit matrix formula for \(A_{\val}\).

Honest verdict: the cleanest paired theorem-facing parameterization is a one-parameter common-value deformation, `common paired value slot = B_chi^pair(m)+alpha`, equivalently `S_chi^pair(m)=alpha`, with every non-value local datum frozen. But this remains conditional until the paired corrected-whitening object and its same-point positivity/nondegeneracy package are written and proved explicitly.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_aval.md:7-28`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29,31-59,68-77`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-486`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1414`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1621`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5711-5789`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-064009-paired-aval-routeA/report.md:3-24,42-64,79-96`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-022935-paired-slot-hypotheses-routeA/report.md:11-37,51-64,82-98`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-031030-paired-spectral-gap-routeA/report.md:3-29,37-61,75-91`

## Dependencies

- Exact compact-interval paired source scalar \(S_\chi^{\pair}(m)=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)\).
- A paired local symmetric normal form that identifies the common paired value slot near \((m,\sigma)\).
- Explicit paired corrected same-point and mixed local blocks.
- Microscopic holomorphy of those blocks.
- Same-point positivity/nondegeneracy on the microscopic disk, sufficient for holomorphic inverse-square-root whitening.
- A precise statement of what is frozen under the pure paired value deformation.

## Strongest objection

The notation
\[
q_{\chi,1}^{\pair}=q_{\chi,2}^{\pair}=B_\chi^{\pair}(m)+\alpha
\]
is the cleanest manuscript-facing compression, but it is still slightly schematic: the current paired record has not yet written the paired local normal form in a way that canonically identifies these two displayed value slots inside the corrected family. So the one-scalar deformation is almost certainly the right interface, but the exact slot-level formula still needs a paired local construction before it becomes a theorem rather than a clean proposal.

## Needed for promotion

1. Write the paired local symmetric normal form explicitly enough to identify the common paired value slot at \((m,\sigma)\).
2. State and prove a paired analogue of corrected finite-\(s\) holomorphic whitening, separating microscopic holomorphy from same-point positivity/nondegeneracy.
3. Define the pure paired value deformation inside that corrected local family with all non-value data frozen.
4. Prove that
   \[
   A_{\val,\chi}^{\pair}(m,\sigma)
   =
   \left.\partial_\alpha \widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\right|_{\alpha=0}
   \]
   is well-defined and canonical.
5. Prove that the coefficient in the exact paired slot expansion is exactly \(S_\chi^{\pair}(m)\).
