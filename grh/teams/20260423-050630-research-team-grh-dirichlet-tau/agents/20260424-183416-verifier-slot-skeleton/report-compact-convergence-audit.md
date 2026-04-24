## Claim

The compact convergence claim is correct in the following scoped form. For a
primitive nonprincipal character, assuming the standard completed-function
inputs for
\[
\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\]
the paired edge-difference zero series
\[
\sum_{\rho}m_\rho\Re\left(
{1\over 1+2it-\rho}-{1\over 2it-\rho}
\right)
\]
is absolutely and uniformly convergent on compact intervals avoiding edge hits
\(2it=\rho\) and \(1+2it=\rho\). The same holds after any fixed number of
\(t\)-derivatives. The reason is exactly Beauvoir's cancellation: in the
genus-one logarithmic derivative, the Hadamard constant and the \(1/\rho\)
regularizers cancel in the difference
\(\Xi_\chi'/\Xi_\chi(1+2it)-\Xi_\chi'/\Xi_\chi(2it)\), leaving summands
\(O_I(|\rho|^{-2})\).

This proves only the compact zero-regularization layer of UV-016. It does not
prove the full source identity
\(q_\chi^{\mathrm{pair}}=B_\chi^{\mathrm{pair}}+S_\chi^{\mathrm{pair}}\),
does not identify the explicit \(B_\chi^{\mathrm{pair}}\) background, and does
not resolve the phase sign except by exposing the same sign boundary checked in
`report-sign-audit.md`.

## Status

proved

## Evidence

**Proved.**

- The proof states the needed entire-function hypotheses explicitly:
  primitive nonprincipal \(\chi\), \(\Xi_\chi\) entire of order one, paired
  functional equation, and a zero multiset counted with multiplicity. See
  `agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:7-14`.
- For a genus-one entire function away from zeros,
  \[
  \Xi_\chi'/\Xi_\chi(z)=b_\chi+\sum_\rho m_\rho((z-\rho)^{-1}+\rho^{-1})
  \]
  in the regularized locally uniform sense. Subtracting the same expression at
  \(w_+(t)=1+2it\) and \(w_-(t)=2it\) cancels \(b_\chi\) and \(\rho^{-1}\)
  termwise. See
  `agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:36-57`.
- For compact \(I\), the large-zero bound
  \[
  |(w_+(t)-\rho)^{-1}-(w_-(t)-\rho)^{-1}|
  \le C_I|\rho|^{-2}
  \]
  is uniform in \(t\in I\). Since order one gives
  \(\sum_\rho m_\rho|\rho|^{-2}<\infty\), the Weierstrass test proves absolute
  uniform convergence. See
  `agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:59-76`.
- Fixed \(t\)-derivatives are also summable: the \(n\)-th derivative of a
  reciprocal is \(O_{I,n}(|\rho|^{-n-1})\) for large \(\rho\), and
  \(n+1\ge2\) for \(n\ge1\). This proves termwise differentiation for each
  fixed derivative order. See
  `agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:78-81`.
- Multiplicity is handled correctly for this layer. The summability statement
  uses the zero multiset with analytic multiplicity \(m_\rho\), so coincident
  zeros from \(\Lambda(s,\chi)\) and \(\Lambda(s,\overline\chi)\) add their
  orders in \(\Xi_\chi\).

**Conditional.**

- The result is conditional on the standard completed Dirichlet package being
  cited or proved wherever promoted: entire order one for nonprincipal
  primitive \(\Lambda(s,\chi)\), order one for the product \(\Xi_\chi\), and
  the genus-one Hadamard product with multiplicities.
- The proof as written is clean for primitive nonprincipal characters. If the
  principal/zeta case is included, poles must be removed or treated as
  background terms before applying an entire-function Hadamard product.
- If \(\Xi_\chi\) has a zero at \(\rho=0\), the displayed \(1/\rho\) regularizer
  must be replaced by the standard separate finite \(m_0/z\) factor. This does
  not harm compact convergence once the corresponding edge hit \(2it=0\) is
  excluded, but it should be stated before promotion.
- Edge-zero exclusion must mean a positive distance from all finite exceptional
  hits in the compact interval. This follows because an entire function has only
  finitely many zeros in a bounded region, but the theorem statement should say
  \(I\) avoids \(2it\in Z_\chi^{\mathrm{pair}}\) and
  \(1+2it\in Z_\chi^{\mathrm{pair}}\).

**Missing.**

- The proof does not identify \(B_\chi^{\mathrm{pair}}\). It works with the
  completed function's zero multiset and the completed log-derivative
  difference; conductor/scaling, gamma-derivative, trivial-zero or pole
  corrections, and any Hadamard-normalization residue still need a separate
  background-split theorem.
- It does not prove the full compact source identity for the phase derivative
  \(q_\chi^{\mathrm{pair}}\). The quotient sign convention must be fixed first:
  for the fixed quotient,
  \[
  (\Phi_\chi^{\mathrm{pair}\,\prime}/\Phi_\chi^{\mathrm{pair}})(1/2+it)
  =-2D_\chi(t),
  \]
  where \(D_\chi(t)=\Xi_\chi'/\Xi_\chi(1+2it)-\Xi_\chi'/\Xi_\chi(2it)\).
- It does not establish local \(S_\chi^{\mathrm{pair}}(m)\)-slot realization,
  whitening, or any downstream UV-017 content.

No computation was run for this audit.

## Baseline / delta

Baseline: the team state treated UV-016 as a compact source-package blueprint,
with compact convergence/regularization, unified \(B_\chi^{\mathrm{pair}}\),
and multiplicity bookkeeping still coupled open burdens.

Delta: the compact zero-summation burden can be separated. Under standard
nonprincipal completed-function inputs, Beauvoir's proof is enough for compact
absolute/uniform convergence of the completed edge-difference zero series and
its fixed derivatives. The remaining UV-016 burdens are now sharper:
source-sign convention and explicit \(B_\chi^{\mathrm{pair}}\) background
splitting in the same normalization.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report.md:3-27`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report.md:29-33`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report.md:58-67`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:7-14`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:16-32`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:36-57`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:59-81`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:83-91`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:93-131`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:51-64`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:24-57`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29-55`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md`

## Dependencies

- Standard completed Dirichlet \(L\)-function source facts for primitive
  nonprincipal \(\chi\): entire order one, zero counting with analytic
  multiplicity, and genus-one Hadamard product.
- Compact interval \(I\) avoiding the edge-zero sets
  \(2it\in Z_\chi^{\mathrm{pair}}\) and
  \(1+2it\in Z_\chi^{\mathrm{pair}}\).
- A separate source-normalization decision for the sign of
  \(q_\chi^{\mathrm{pair}}\) relative to the fixed quotient.
- A separate explicit \(B_\chi^{\mathrm{pair}}\) derivation in the same
  convention.

## Strongest objection

The proof's conclusion is easy to overstate. It proves convergence of the
completed-function edge-difference zero contribution, not the source theorem.
The full UV-016 identity still has to connect this completed zero sum to the
chosen phase derivative \(q_\chi^{\mathrm{pair}}\) and to an explicit
\(B_\chi^{\mathrm{pair}}\) containing conductor/scaling, gamma, trivial-zero or
pole, and possible Hadamard-normalization terms. Without that second theorem,
the compact source package remains open even though the zero-series
regularization subproblem is solved.

## Needed for promotion

1. Cite or prove the standard primitive nonprincipal completed-\(L\) inputs,
   including order-one zero summability with multiplicity.
2. State the edge-zero exclusion precisely and handle any possible zero at
   \(\rho=0\) as a finite exceptional factor.
3. Keep the compact convergence theorem as a completed-zero regularization
   lemma, not as the full source package.
4. Combine it later with the sign convention from `report-sign-audit.md` and a
   separate explicit \(B_\chi^{\mathrm{pair}}\) background-split theorem.

## Autoresearch next step

continue: formulate the next lemma as an explicit background-split problem:
starting from the chosen sign convention for the fixed quotient, derive the
exact \(B_\chi^{\mathrm{pair}}\) components left after subtracting the compactly
convergent completed-zero edge sum.
