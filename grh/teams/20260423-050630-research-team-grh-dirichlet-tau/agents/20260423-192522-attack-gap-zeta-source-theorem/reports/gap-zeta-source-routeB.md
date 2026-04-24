## Claim

The canonical source-theorem gap is small but not purely notational. The smallest safe paper-facing package is:

1. one source-identification theorem fixing the completed quotient
   \[
   \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
   \]
   and the branch/sign/factor-of-\(2\) normalization relating
   \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\) to the manuscript variable \(q(t)=\Phi'(t)\);
2. one single-zero contribution theorem proving that each nontrivial zero contributes exactly
   \(f_{\beta,\gamma}(t)\) to \(q(t)\);
3. one compact-interval convergence/regularization theorem justifying the summed identity on singularity-free intervals.

After that, the remaining work is notation cleanup:

4. unify `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` into one explicitly defined background term;
5. state that zero sums are with multiplicity.

So the minimal safe package is not a new conceptual program, but it is larger than bookkeeping alone. The true theorem content is items 1-3. Items 4-5 are cleanup once the source theorem exists.

## Status

open

## Evidence

Proved.

1. The paper already proves the kernel-level layer. It defines an abstract phase \(\Phi\) and \(q(t):=\Phi'(t)\), uses the split \(q=B_\zeta+S\), defines the omitted-zero tail from
   \[
   f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2},
   \]
   and proves the tail-curvature estimate from that kernel model.
2. The conservative `grh/` note isolates the strongest safe theorem currently supported: positive single-zero strip-edge kernel, plus conditional omitted-tail curvature under the shell-convergence hypotheses. It explicitly stops short of claiming a fully normalized completed-function identity for \(q\).
3. The canonical paper also uses the manuscript-level formula
   \[
   S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m),
   \]
   so the positive strip-edge kernel package is already paper-facing.

Conditional on archive provenance, not canonical.

4. The archived derivation gives exactly the missing source template: the quotient
   \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\), the normalization
   \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), the identity
   \(\partial_s\log\phi(\tfrac12+it)=2q(t)\), and the computation that one nontrivial zero contributes \(2f_{\beta,\gamma}(t)\) to \(\partial_s\log\phi\), hence \(f_{\beta,\gamma}(t)\) to \(q\).
5. Those archived steps show the missing bridge is specific and local. They do not suggest unrelated new machinery; they suggest one explicit source theorem plus its local bookkeeping consequences.

Missing.

6. The paper does not yet prove that its own abstract phase \(\Phi\) is the scattering phase of that specific quotient. This is theorem content, not notation cleanup.
7. The paper does not yet prove inside the canonical draft that the nontrivial-zero contribution to \(q\) is exactly the same kernel \(f_{\beta,\gamma}\) used later for tails and for \(S(m)\).
8. The paper does not yet state one compact-interval theorem clarifying whether the primary object is the absolutely convergent strip-edge difference, or a regularized completed-log-derivative identity whose constants are absorbed into background.
9. The paper currently shifts among `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` without one theorem fixing their relation. That is partly theorem-level background identification and partly notation cleanup.
10. The paper-level zero sums do not visibly state multiplicity. That is a small item, but it still needs to be said.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:6-18,22-40,42-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:17-25,29-42,69-97,99-118`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1490`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/gap-source-theorem-routeA.md:3-30,107-133`
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/gap-source-theorem-routeB.md:3-31,75-94,119-125`
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/verifier-adversarial-source-theorem-gap.md:3-37,77-128`

## Dependencies

- A source-identification theorem fixing the completed quotient and the branch/sign/factor-of-\(2\) normalization.
- A single-zero contribution theorem deriving \(f_{\beta,\gamma}(t)\) from that quotient for the manuscript's \(q\).
- A compact-interval convergence/regularization theorem for the summed identity and its local differentiation.
- One explicit definition of the background term, replacing or identifying `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`.
- A stated multiplicity convention for all zero sums.

## Strongest objection

The phrase `only bookkeeping remains` is still too strong. From the current paper alone, the map from the manuscript variable `q` to the specific quotient \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) is not yet proved. That map is the main missing theorem. Gamma/trivial-zero/pole/Hadamard cleanup comes after that, not before it.

## Needed for promotion

1. Promote only the three theorem-level items as genuinely missing mathematics:
   source identification, single-zero contribution, compact-interval convergence/regularization.
2. Treat `B_\zeta` / `B_{\Aut}` / `B_{\bg}` unification as explicit background cleanup attached to that theorem, not as an independent conceptual gap.
3. Add the multiplicity convention explicitly.
4. Keep the current paper-facing boundary narrow until then: `kernel theorem proved; source theorem conditional`.

Honest verdict: the gap is small and sharply localized. It does not require unrelated machinery. But it is not yet just notation. The minimal safe package is one local source theorem with three mathematical parts, followed by two small cleanup items.
