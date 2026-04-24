## Claim

The cleanest proof skeleton for the exact paired local-slot identification theorem is the following theorem-facing statement plus ordered proof plan.

**Theorem target.** Let
\[
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\qquad
\Phi_\chi^{\pair}(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}.
\]
Assume on a compact interval \(I\subset \mathbf R\) that the paired source package is available with exact decomposition
\[
q_\chi^{\pair}(t)=B_\chi^{\pair}(t)+S_\chi^{\pair}(t),
\]
and that the paired corrected local family near each midpoint-scale pair \((m,\sigma)\) admits:
\[
\text{symmetric local normal form},\quad
\text{microscopic holomorphy},\quad
\text{same-point positivity/nondegeneracy},\quad
\text{holomorphic whitening}.
\]
Define the pure paired value-channel derivative by varying only the common paired value slot,
\[
q^{\pair}_{\chi,1}=q^{\pair}_{\chi,2}=B_\chi^{\pair}(m)+\alpha,
\qquad
S_\chi^{\pair}(m)=\alpha,
\]
with all derivative, mixed-jet, and curvature data frozen at paired background value, and set
\[
A_{\val,\chi}^{\pair}(m,\sigma)
:=
\left.\frac{\partial}{\partial \alpha}
\widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\right|_{\alpha=0}.
\]
Then the exact paired local deformation satisfies
\[
\Delta_\chi^{\pair}(m,\sigma)
=
S_\chi^{\pair}(m)A_{\val,\chi}^{\pair}(m,\sigma)
+
R_\chi^{\pair}(m,\sigma),
\]
so \(S_\chi^{\pair}(m)=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)\) is exactly the coefficient occupying the manuscript-local leading value slot.

**Ordered proof plan.**

1. **[New paired-family work]** Prove the compact-interval paired source decomposition \(q_\chi^{\pair}=B_\chi^{\pair}+S_\chi^{\pair}\) with one unified background and explicit multiplicity/regularization bookkeeping.
2. **[New paired-family work]** Write the paired corrected local family in a symmetric normal form that identifies one common paired value slot and specifies the freeze rules for all non-value local data.
3. **[New paired-family work]** Prove the minimal admissibility package for that paired family: microscopic holomorphy of same-point and mixed blocks, same-point positivity/nondegeneracy, and existence of holomorphic inverse-square-root whitening.
4. **[Transported manuscript-local algebra]** Apply the manuscript whitening expansion to the paired corrected family: analyticity of the whitening map gives a first-order expansion around paired background \(S_\chi^{\pair}(m)=0\).
5. **[New paired-family work]** Identify the coefficient of the linear term in that expansion with the exact upstairs scalar \(S_\chi^{\pair}(m)\), not merely with a nearby source-normalized surrogate.
6. **[Transported manuscript-local algebra]** Declare the Fr\'echet derivative in the pure paired value direction to be \(A_{\val,\chi}^{\pair}(m,\sigma)\), yielding
   \[
   \Delta_\chi^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_\chi^{\pair}.
   \]
7. **[Transported manuscript-local consequence]** Conclude that, once step 5 is done, the manuscript's local leading-channel algebra needs no further theorem: the coefficient is already identified exactly.

**Separation of proof state.**

- **proved:** steps 4, 6, and the formal implication in step 7 are already present at manuscript level once a local family with admissible whitening exists.
- **conditional:** the theorem is correct as a source-normalized proof skeleton if steps 1 to 5 are assumed.
- **missing:** the actual paired theorem burden is concentrated in steps 1 to 5, especially exact slot identification in step 5.

Honest verdict: the proof skeleton is clean and short, but it is not closed from current scope alone. The manuscript already supplies the local algebra after admissible paired whitening is in place; the real unresolved content is the paired source package plus the proof that the same scalar \(S_\chi^{\pair}(m)\) is exactly the local first-order slot coefficient.

## Status

conditional

## Evidence

**Proved.**

- The manuscript already has the model local value-channel rule: vary one common value slot \(q_1=q_2=B+\alpha\), freeze derivative and curvature data, and define \(A_{\val}\) as the first derivative at \(\alpha=0\).
- The manuscript already has the corrected-whitened expansion template: after holomorphic whitening is available, the corrected local deformation expands around background value parameter \(S(m)=0\) with linear term \(S(m)A_{\val}(m,\sigma)\).
- The paired notes already isolate the safe theorem-facing split: an upstairs paired source theorem, then a downstairs exact local-slot identification theorem, with the same one-scalar value-channel convention.

**Conditional on [paired source package + paired admissibility + exact slot identification].**

- The full paired theorem follows by transporting the manuscript whitening algebra to the paired corrected family.
- The theorem-facing paired value direction is still one-scalar: vary only the common paired value slot, freeze all non-value local data, then differentiate the paired corrected whitened block.
- Once the coefficient of the linear term is shown to be exactly \(S_\chi^{\pair}(m)\), the leading-slot identification is immediate.

**Missing.**

- A theorem-ready compact-interval construction of \(q_\chi^{\pair}\), \(B_\chi^{\pair}\), and \(S_\chi^{\pair}\) with exact bookkeeping.
- A paired local symmetric normal form that canonically identifies the common paired value slot.
- A paired analogue of corrected finite-\(s\) holomorphic whitening with explicit same-point positivity/nondegeneracy for holomorphic whitening.
- The exact proof that the coefficient of the first-order paired value-channel derivative is the same upstairs scalar \(S_\chi^{\pair}(m)\).

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:8-22,24-46,48-57`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29,31-59,61-77`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:7-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-021955-paired-slot-theorem-routeA/report.md:3-35,43-62,78-92`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-070213-paired-value-channel-routeA/report.md:3-32,40-59,75-104`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-081055-paired-freeze-rules-routeA/report.md:3-18,24-31,42-58`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1457`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1566`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1569-1613`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1640-1679`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5711-5790`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:12168-12227`

## Dependencies

- Compact-interval paired source theorem for \(\Phi_\chi^{\pair}\) with unified background \(B_\chi^{\pair}\).
- Exact paired scalar definition \(S_\chi^{\pair}(m)=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)\).
- Paired local symmetric normal form identifying one common paired value slot.
- Paired corrected same-point and mixed blocks.
- Microscopic holomorphy and same-point positivity/nondegeneracy sufficient for holomorphic whitening.
- Exact proof that the paired first-order value coefficient is the same scalar \(S_\chi^{\pair}(m)\).

## Strongest objection

The skeleton is theorem-facing rather than theorem-complete: it depends on a not-yet-proved claim that the paired corrected local family carries a canonically identified one-scalar value direction whose first-order coefficient is exactly the upstairs scalar \(S_\chi^{\pair}(m)\). Without that exact identification, the transport from manuscript local algebra to the paired family remains only source-normalized and schematic.

## Needed for promotion

1. Prove the compact-interval paired source decomposition with explicit conductor, gamma, trivial-zero/pole, convergence, and multiplicity bookkeeping.
2. Write the paired local symmetric normal form and freeze rules so the common paired value slot is explicit.
3. Prove the paired admissibility package: microscopic holomorphy, same-point positivity/nondegeneracy, and holomorphic whitening.
4. Show that varying \(S_\chi^{\pair}(m)\) changes only that common paired value slot to first order, with all non-value local data frozen.
5. Prove the exact identity
   \[
   \Delta_\chi^{\pair}(m,\sigma)
   =
   S_\chi^{\pair}(m)A_{\val,\chi}^{\pair}(m,\sigma)
   +
   R_\chi^{\pair}(m,\sigma)
   \]
   as a genuine paired theorem rather than a transported template.
