## Claim

The source-theorem gap is not yet reduced to bookkeeping items alone. The safe adversarial verdict is narrower: the repo supports a positive strip-edge kernel theorem and an archive-backed candidate source theorem, but the manuscript still lacks the theorem that identifies its own phase derivative \(q=\Phi'\) with the logarithmic derivative of the specific scattering quotient
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
\]
Without that source-identification step, the remaining items are not merely cosmetic bookkeeping around an already-fixed theorem; they still include the main theorem-level bridge from manuscript notation to the automorphic source object.

The strongest checklist safe to record in `grh/` is therefore:

1. `proved at kernel level`: for one zero \(\rho=\beta+i\gamma\),
   \[
   K_\rho(t)=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)
   =
   \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
   +
   \frac{\beta}{\beta^2+(2t-\gamma)^2},
   \]
   hence \(K_\rho(t)>0\) for \(0\le \beta\le 1\).
2. `proved at manuscript level`: the paper uses the absolutely convergent strip-edge sum
   \[
   S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
   \]
   and proves the omitted-tail curvature estimate from this kernel model.
3. `conditional on a missing source theorem`: the stronger identity
   \[
   q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)
   \]
   for the manuscript's own \(q\), with explicit quotient, branch normalization, background formula, multiplicity convention, and compact-interval convergence/regularization package.

Claims that need scoped weakening:

- `the gap is only bookkeeping` should be weakened to `once the source object and phase normalization are fixed, the remaining closure is bookkeeping on singularity-free compact intervals`.
- `q(t)=B_\zeta(t)+S(t)` should be treated in `grh/` as manuscript notation, not yet as a proved completed-quotient theorem.
- `B_\zeta` is the explicit automorphic background should be weakened to `the intended background term is the gamma/trivial-zero/pole contribution, but its exact identification with manuscript notation remains conditional`.
- `S(m)` is the source-derived background-subtracted zero density should be weakened to `the manuscript represents it by the strip-edge kernel sum; the scattering-source interpretation is archive-backed but not yet canonical`.

## Status

open

## Evidence

Proved in the manuscript or conservative `grh/` notes:

- The paper defines an abstract real phase \(\Phi\) and sets \(q(t):=\Phi'(t)\), but does not yet name the source object producing that phase.
- The paper states the split
  \[
  q(t)=B_\zeta(t)+S(t)
  \]
  and later gives
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
  \]
- The paper's tail-curvature argument is genuinely kernel-level: it uses the explicit strip-edge kernel and shell counting, not a completed-function theorem.
- `strip_edge_kernel_note.tex` deliberately records only the conservative layer: positive single-zero kernel plus conditional omitted-tail curvature, and explicitly says the full normalized completed-function identity for \(q\) is not yet claimed.
- `scattering_generalization.md` and `scattering_candidate_note.tex` make the same boundary explicit: the quotient reading sharpens the candidate object, but realization as a theorem of the draft is still missing.

Archive-backed but not canonical:

- The cited chat gives the exact quotient candidate
  \[
  \phi(s)=\Lambda(2s-1)/\Lambda(2s),
  \qquad
  \phi(\tfrac12+it)=e^{-2i\Phi(t)},
  \]
  and computes that one nontrivial zero contributes \(2f_{\beta,\gamma}(t)\) to \(\partial_s\log\phi\).
- The same archive states
  \[
  \partial_s\log\phi(\tfrac12+it)=2q(t)
  \]
  and concludes
  \[
  q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t).
  \]

What is still larger than bookkeeping:

- The manuscript phase \(\Phi\) is introduced abstractly in the phase-kernel section. The paper regions cited for the split never prove that this \(\Phi\) is the Eisenstein/scattering phase of the specific quotient \(\phi\). That is a source-identification theorem, not just term collection.
- The manuscript currently shifts among `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` without one source theorem proving they are the same object or specifying what each absorbs.
- The manuscript-level formula \(S(m)=\sum_\rho f_\rho(m)\) does not state multiplicity conventions or whether the sum is primary as an absolutely convergent strip-edge difference versus derived from a regularized completed-log-derivative identity. That distinction matters at source level.

So the route reports are right that the residual work is mostly source-level, but they understate one point: before the gamma/trivial-zero/pole/Hadamard items, the paper still needs the theorem that the manuscript's own \(q\) comes from the specific scattering quotient at all.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44` for required schema and scoped-negation discipline.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:11-18,21-38,50-59,69-79` for the conservative boundary: candidate quotient reading yes, realization theorem no.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:60-67,69-92,124-138` for the same conditional boundary and missing realization list.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:17-24,29-42,69-85,99-118` for the strongest already-safe kernel theorem and the explicit refusal to claim the full source identity.
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/gap-source-theorem-routeA.md:3-30,80-85,109-133` for the route-A theorem target and its four proposed closure items.
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/gap-source-theorem-routeB.md:3-31,75-94,121-125` for the route-B conservative kernel/source separation and hidden bookkeeping list.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160` for the abstract phase-kernel definition and `q(t):=\Phi'(t)`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299` for `q(t)=B_\zeta(t)+S(t)`, `S(m):=q_\zeta(m)-B_\zeta(m)`, and the curvature estimate.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-369` for the omitted-tail kernel definition and curvature bound using `B_{\Aut}`.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1490` for the later notation switch to `B_{\bg}` in the fixed-core decomposition.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364` for the manuscript-level global kernel formula `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` and the bound using `B_\zeta(m)\asymp Q`.
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598` for the quotient candidate, zero contribution computation, normalization `\partial_s\log\phi(\tfrac12+it)=2q(t)`, and the candidate exact decomposition.

## Dependencies

- A source-identification theorem fixing that the manuscript phase \(\Phi\) is the scattering phase of the specific quotient \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) on singularity-free compact intervals.
- A branch-normalization/sign theorem proving the exact relation between `q`, `\Phi'`, and `\partial_s\log\phi`, including the factor of \(2\).
- A single-zero source contribution theorem proving that each nontrivial zero contributes exactly \(f_{\beta,\gamma}(t)\) to the manuscript's \(q\).
- An explicit background theorem identifying which terms are absorbed into `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`, or replacing these with one fixed notation.
- A source-level convention that zeros are summed with multiplicity.
- A compact-interval convergence/regularization statement clarifying whether the primary object is the absolutely convergent strip-edge difference, or a regularized completed-log-derivative difference whose constants are absorbed into background.

## Strongest objection

The phrase `only bookkeeping remains` is still too strong. From the current manuscript scope alone, one does not yet have a theorem that the phase derivative used throughout the draft is the derivative of the specific Eisenstein scattering phase at all. Until that identification is proved, the gamma/trivial-zero/pole/Hadamard work is not merely tidying up an already-fixed source theorem; it is part of establishing the source theorem itself. Put differently: the kernel layer is solid, the candidate source object is plausible and archive-backed, but the manuscript has not yet closed the map `manuscript q` -> `specific completed quotient`.

## Needed for promotion

Safe checklist for `grh/` now:

1. Record only the kernel theorem as proved: positive strip-edge single-zero kernel, manuscript-level strip-edge sum for \(S(m)\), and conditional omitted-tail curvature under the stated shell-convergence package.
2. Record the source theorem as conditional, with this exact checklist:
   \(a\) fix the quotient object \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\);
   \(b\) prove the branch/sign/factor-of-\(2\) normalization for the manuscript phase;
   \(c\) prove the single-zero contribution identity;
   \(d\) state the multiplicity convention;
   \(e\) prove the compact-interval convergence/regularization statement;
   \(f\) identify the full background term and unify the notation `B_\zeta`, `B_{\Aut}`, `B_{\bg}`.
3. Do not record `the gap is reduced to bookkeeping items` without scope. Safe replacement: `once the quotient-phase identification is supplied, the remaining closure reduces to explicit source bookkeeping on singularity-free compact intervals`.
4. Do not record `q=B_\zeta+S` as an already-derived automorphic theorem in `grh/`. Safe replacement: `the manuscript uses this split, and the archive supplies a candidate source derivation, but the source theorem is not yet canonical`.

Honest verdict: the gap is smaller than a new conceptual program but larger than route-A/route-B bookkeeping language suggests. The positive strip-edge kernel layer is safe. The archive gives a credible source theorem template. What is still missing is the manuscript theorem that its own phase derivative is the scattering-phase derivative of that specific quotient, plus the explicit background/multiplicity/regularization package. So the safest record in `grh/` is `kernel theorem proved; source theorem still conditional`.
