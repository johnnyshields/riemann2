## Claim

The component priority should be tightened.

From the present zeta-source scope alone, only one piece separates cleanly as an independent first target:

1. the quotient/phase identification fixing
   \[
   \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
   \qquad
   \phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
   \qquad
   q(t)=\Phi'(t).
   \]

Everything else is better proved together in one bundled source theorem:

2. the single-zero contribution formula for the manuscript's normalized phase;
3. the compact-interval summed identity / regularization away from real singularities;
4. the identification of the residual background term as the object later called `B_\zeta`, `B_{\Aut}`, or `B_{\bg}`;
5. the zero multiplicity convention.

So the safest priority choice for an RH agent is not five quasi-independent tasks, and not even three equally independent theorem parts. It is:

- first, fix the source object and its normalization to the manuscript variable `q`;
- then prove the remaining zero-expansion package as one theorem.

## Status

open

## Evidence

Proved.

1. The canonical draft already has a source-light local package before the zeta cut point: abstract phase kernel, jet-limit blocks, finite-`s` removable singularities, and whitening all depend only on a real phase `\Phi` and `q=\Phi'`.
2. The source-specific jump occurs exactly when the paper writes
   \[
   q(t)=B_\zeta(t)+S(t)
   \]
   and then uses `S(m)` as the value-channel amplitude. This confirms that the real paper-facing dependency is the realization of the manuscript's `q`, not another local-kernel theorem.
3. The paper already uses the strip-edge kernel profile
   \[
   f_{\beta,\gamma}(m)=
   \frac{1-\beta}{(1-\beta)^2+(2m-\gamma)^2}
   +
   \frac{\beta}{\beta^2+(2m-\gamma)^2}
   \]
   and later states
   \[
   S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
   \]
   So the kernel side is already built into the manuscript architecture.

Conditional on the archived quotient template.

4. The archived derivation shows a natural two-stage dependency. First it fixes the candidate quotient and normalization:
   \[
   \phi(s)=\Lambda(2s-1)/\Lambda(2s),
   \qquad
   \phi(\tfrac12+it)=e^{-2i\Phi(t)},
   \qquad
   \partial_s\log\phi(\tfrac12+it)=2q(t).
   \]
   That is the genuinely independent bridge from the manuscript variable to a completed object.
5. Once that bridge is fixed, the single-zero formula, the compact-interval sum, and the background term come from the same logarithmic-derivative expansion. In the archive proof, the same computation that identifies one zero contribution also declares that gamma-factor, trivial-zero, and pole terms are bundled into one background term and that summation is taken on compact intervals avoiding singularities.
6. For that reason, the later items are not naturally independent in the way the first item is. They share one proof environment: the same quotient, the same branch/sign/factor-of-`2` normalization, the same log-derivative decomposition, and the same regularization scope.

Missing.

7. The canonical paper does not yet prove that its own phase `\Phi` is the phase of the specific quotient `\Lambda(2s-1)/\Lambda(2s)`. This is the cleanest independent missing theorem.
8. The canonical paper also does not yet present one theorem that simultaneously fixes the single-zero source contribution, the compact-interval summation/regularization, the background object, and the multiplicity convention. Those pieces remain unstated canonically and are intertwined enough that splitting them into separate paper priorities would likely duplicate setup and obscure the real dependency chain.
9. The current paper's shifting notation among `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` is evidence that background identification is downstream of the same source theorem, not a cleanly prior theorem on its own.

Separated into the common brief bins.

10. Proved: the source-light local geometry; the strip-edge kernel profile as the manuscript's working scalar kernel; the use of `S(m)` as a formal positive zero sum inside the draft.
11. Conditional on the quotient/source theorem: the identification of manuscript `q` with a completed scattering quotient; the exact source meaning of `S(m)`; every later calibration statement that treats `S(m)` as a realized value-channel amplitude.
12. Missing: the canonical quotient-phase theorem and the bundled zero-expansion theorem just described.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:15-18,28-34,47-62,153-162,197-202`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-23,25-36`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-18,24-40,42-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-12,23-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:8-18,21-38,48-62,73-83`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:753-811`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1532-1619`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:3-20,42-57,81-93`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/verifier-adversarial-zeta-source-theorem.md:12-22,41-68,99-109`
- `/mnt/c/workspace/riemann2/tasks/20260424-001046-attack-gap-rh-patch-plan/reports/gap-rh-patch-plan-routeB.md:5-6,18-29,31-37,69-71`

## Dependencies

- One canonical theorem fixing the quotient object and the manuscript normalization `\phi(\tfrac12+it)=e^{-2i\Phi(t)}`, `q=\Phi'`.
- One downstream bundled theorem for the normalized log-derivative expansion on compact singularity-free intervals, including: single-zero contribution, summed identity / regularization, background identification, and multiplicity convention.
- The existing source-light local kernel / jet / whitening package already in `paper/proof_of_rh.tex`.

## Strongest objection

The main risk in this priority choice is understating the load carried by the bundled theorem. Saying `only the quotient identification is real mathematics` would be false. The safer claim is narrower: the quotient identification is the only piece that is cleanly independent. The remaining pieces are still mathematical content, but they are better proved together because they arise from the same completed-object expansion and the same regularization choices.

## Needed for promotion

1. For RH-facing planning, rewrite the priority memo as `one independent source-identification theorem, then one bundled zero-expansion theorem`.
2. Keep paper-facing wording in three bins:
   proved: local kernel package;
   conditional on the source theorem: realized `q=B_\zeta+S` and downstream `S(m)` calibration uses;
   missing: canonical quotient identification and bundled zero-expansion theorem.
3. Do not prioritize background unification or multiplicity as stand-alone theorem fronts.
4. Do not describe the single-zero contribution and compact-interval summation as fully separate proof targets unless there is a concrete reason to split the log-derivative argument.

Honest verdict: for an RH agent, the truly independent piece is the quotient/phase identification. After that, the safe move is to keep the zero contribution, compact-interval summation, background identification, and multiplicity in one theorem package. Proved: the local source-light package and the manuscript kernel model. Conditional: every source-realized use of `S(m)`. Missing: the canonical bridge from manuscript `q` to the completed quotient, and the bundled theorem that turns that bridge into the exact zeta source package.
