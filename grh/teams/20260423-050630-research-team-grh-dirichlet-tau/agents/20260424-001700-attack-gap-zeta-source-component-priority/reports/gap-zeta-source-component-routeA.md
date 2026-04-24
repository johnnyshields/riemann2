## Claim

From the present zeta-source scope alone, the best first component to prove is
the quotient / phase normalization theorem. My leverage ranking is:

1. quotient / phase normalization;
2. single-zero contribution;
3. compact-interval summation / regularization;
4. background identification;
5. multiplicity convention.

Reason for the ranking:

- quotient / phase normalization has the highest leverage because it is the
  gateway theorem that canonically identifies the manuscript variable
  \(q=\Phi'\) with the specific completed quotient
  \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\). Without that identification, the RH
  draft still has only an abstract zeta-side split, not a proved source theorem.
- single-zero contribution is next because it turns the normalized quotient into
  the exact positive strip-edge kernel already used later for tail curvature and
  for the value scale \(S(m)\). This is the first place where the source theorem
  feeds the downstream local estimates in their actual manuscript form.
- compact-interval summation / regularization is third because it upgrades the
  one-zero identity to the full paper-facing formula on singularity-free compact
  intervals. It is necessary for full closure, but it depends on the first two
  pieces and does not by itself identify the source object.
- background identification is fourth because it is mathematically load-bearing
  for exposition, but it is a unification item rather than the first missing
  theorem-level bridge.
- multiplicity convention is fifth because it is necessary for a canonical
  statement, but it adds the least new leverage once the source theorem is in
  place.

Strongest honest verdict: the draft's best first zeta-source milestone is not
the compact-interval theorem and not background cleanup. It is the quotient /
phase normalization theorem. That is the narrowest first result that changes the
RH draft from using an abstract source split to using a canonically identified
zeta source object.

## Status

open

## Evidence

Proved in the canonical draft.

1. The draft already marks the exact paper boundary where the argument stops
   being source-light and starts using zeta-specific data: it introduces the
   zeta-side split
   \[
   q(t)=B_\zeta(t)+S(t),
   \qquad
   S(m):=q_\zeta(m)-B_\zeta(m).
   \]
   So the main paper-facing gap is the source theorem sitting behind this split,
   not a generic local-geometry theorem.
2. The draft already contains the single-zero kernel profile
   \[
   f_{\beta,\gamma}(t)=
   \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
   +
   \frac{\beta}{\beta^2+(2t-\gamma)^2},
   \]
   and uses it in the tail-curvature theorem. So once the quotient is canonically
   linked to \(q\), the next immediate downstream payoff is the source-level
   identification of this already-used kernel.
3. The draft later uses
   \[
   S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
   \]
   as a paper-facing input. That means the compact-interval summed identity is
   certainly needed, but the manuscript has already organized the later RH chain
   around a source scalar whose real bottleneck is the missing canonical origin
   of \(q\) itself.
4. The draft uses three background names across nearby layers:
   \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\). This makes background
   identification necessary, but the background issue appears after the primary
   source object has been fixed.

Conditional on archive and `grh/` provenance.

5. The archived derivation supplies the exact quotient candidate
   \[
   \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
   \qquad
   \phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
   \qquad
   \partial_s\log\phi\!\left(\tfrac12+it\right)=2q(t),
   \]
   and from that derives the one-zero contribution \(f_{\beta,\gamma}(t)\) and
   the full compact-interval decomposition
   \[
   q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t).
   \]
   This supports the leverage ranking: the quotient / phase normalization really
   is the front door, the single-zero computation is the next step, and the
   compact-interval sum comes after those.
6. The `grh/` notes independently describe the zeta source gap as one localized
   package with three theorem-level parts plus two explicit
   identification/convention items, and they place the quotient / phase
   normalization first in that package.
7. The RH patch-plan note says the highest-value, lowest-risk patch is to add a
   canonical zeta-source subsection at the start of the zeta-side decomposition.
   That patch would justify `q`, `B_\zeta`, `S`, and the positive strip-edge
   kernel representation. This again points to source identification as the most
   leveraged first theorem.

Missing in the canonical draft.

8. The paper still does not prove that its own abstract manuscript phase
   \(\Phi\) is the phase of the specific quotient
   \(\Lambda(2s-1)/\Lambda(2s)\). This is the main missing bridge.
9. The paper still does not canonically prove the branch, sign, and factor-of-2
   normalization linking that quotient to \(q=\Phi'\).
10. The paper still does not present one theorem deriving the single-zero source
   contribution for the manuscript's \(q\), then summing it on compact
   singularity-free intervals.
11. The paper still does not canonically fix the relation among
   \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\), or visibly attach `counted with
   multiplicity` to the zero sums.

Separation by proof-state.

- proved: the kernel profile is already in the draft; the zeta-side split is in
  the draft; the later RH chain already uses \(S(m)\) as a positive source
  scalar.
- conditional on archive support: the specific completed quotient, the precise
  phase normalization, the one-zero derivation from that quotient, and the full
  compact-interval decomposition.
- missing canonically: the quotient / phase identification theorem, the theorem
  deriving the single-zero contribution for manuscript \(q\), the compact
  summation / regularization theorem, the explicit background identification,
  and the multiplicity convention.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:153-163`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-23`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-18,22-40,42-54`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1490`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2087`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26327`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeA.md:71-109`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:1-20,42-57,73-93`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/verifier-adversarial-zeta-source-theorem.md:5-23,41-69,84-111`

## Dependencies

- A canonical quotient / phase normalization theorem fixing
  \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) and the normalization
  \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), \(q=\Phi'\).
- A canonical single-zero source contribution theorem deriving the kernel
  \(f_{\beta,\gamma}(t)\) for that normalized phase.
- A compact-interval convergence or regularization theorem justifying the summed
  identity away from real singularities.
- One explicit canonical relation among \(B_\zeta\), \(B_{\Aut}\), and
  \(B_{\bg}\).
- An explicit multiplicity convention for all zero sums.

## Strongest objection

The main risk in ranking leverage is to underrate the compact-interval theorem
or the background identification just because the quotient / phase theorem comes
first logically. Full source closure still needs all five items. In particular,
the paper already uses full summed formulas and already carries three background
names, so neither summation nor background identification is dispensable. The
claim here is narrower: if only one first component is to be attacked for
maximum leverage back to the RH draft, it should be the quotient / phase
normalization because that is the only item that canonically changes the status
of the manuscript variable \(q\) from abstract notation to a specific zeta source
object.

## Needed for promotion

- Prove first the quotient / phase normalization theorem in a canonical zeta-source
  subsection at the start of the zeta-side decomposition.
- Immediately after that, promote the single-zero source contribution theorem so
  the already-used positive strip-edge kernel has canonical source provenance.
- Then state the compact-interval summation / regularization theorem away from
  real singularities.
- Attach one explicit background-identification statement and one explicit
  multiplicity convention to that same localized source package.

Honest verdict: the best first component is quotient / phase normalization. The
kernel package downstream is already structurally waiting for it. Without it,
the RH draft still lacks the canonical theorem that says what its zeta-side
phase actually is.
