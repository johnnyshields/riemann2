## Claim

For the fixed paired quotient
\[
\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s),
\qquad
\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\]
standard completed-\(L\) bookkeeping gives a theorem-adjacent package, not a closed UV-016 theorem. The log-derivative is
\[
\frac{(\Phi_\chi^{\mathrm{pair}})'}{\Phi_\chi^{\mathrm{pair}}}(s)
=2\frac{\Xi_\chi'}{\Xi_\chi}(2s-1)-2\frac{\Xi_\chi'}{\Xi_\chi}(2s).
\]
For a positive strip-edge source term \(S_\chi^{\mathrm{pair}}\), the compatible boundary convention is
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},\qquad
q_\chi^{\mathrm{pair}}(t)=(\Theta_\chi^{\mathrm{pair}})'(t),
\]
so that
\[
\frac{(\Phi_\chi^{\mathrm{pair}})'}{\Phi_\chi^{\mathrm{pair}}}
\!\left(\tfrac12+it\right)=-2q_\chi^{\mathrm{pair}}(t).
\]
With the positive-exponent convention \(e^{2i\Theta}\) and the same \(q=\Theta'\), the nontrivial-zero contribution has the opposite sign. Thus a positive source split \(q_\chi^{\mathrm{pair}}=B_\chi^{\mathrm{pair}}+S_\chi^{\mathrm{pair}}\) either needs the negative-exponent convention above, or an explicit redefinition such as \(q=-\Theta'\) or an inverse quotient. This is a correction candidate against the current paired quotient-normalization notes and needs adversarial verification before promotion.

For a zero \(\rho=\beta+i\gamma\) of \(\Xi_\chi\), with analytic multiplicity \(m_\rho\), the positive zero contribution is
\[
m_\rho K_\rho(t),\qquad
K_\rho(t)=
\Re\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)
=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]
The zero multiset is the nontrivial zero multiset of \(\Xi_\chi\): zeros from \(\Lambda(s,\chi)\) and \(\Lambda(s,\overline\chi)\) are both counted, and coincident or repeated zeros are counted with the summed analytic order in the product. Multiplicity belongs in the same compact regularized identity as the zero sum; it is not a distinct-ordinate convention and not a slot-realization claim.

The unified \(B_\chi^{\mathrm{pair}}\) should contain exactly the non-source terms left after removing the nontrivial-zero kernel multiset: conductor/scaling terms from the two completed factors and the \(2s-1,2s\) scaling; gamma-derivative terms; trivial-zero corrections; and pole corrections if the character choice leaves a pole. If a proof uses a Hadamard product with an exponential constant, its boundary derivative is also background bookkeeping, not part of \(S_\chi^{\mathrm{pair}}\); the current theorem-adjacent safe public list remains conductor/scaling, gamma-derivative, and trivial-zero or pole corrections.

## Status

open

## Evidence

Proved from standard completed-\(L\) bookkeeping:
- The paired object and quotient shape are fixed in the source notes and candidate text.
- The chain rule gives the displayed log-derivative identity.
- A nontrivial zero of \(\Xi_\chi\) contributes \(2(1/(2it-\rho)-1/(1+2it-\rho))\) to \((\Phi_\chi^{\mathrm{pair}})'/\Phi_\chi^{\mathrm{pair}}\) on the boundary. Therefore the positive strip-edge kernel \(K_\rho\) is the contribution to \(-\tfrac12(\Phi'/\Phi)\), not to \(+\tfrac12(\Phi'/\Phi)\).
- The one-zero kernel identity and positivity are already isolated in the strip-edge note.
- Product multiplicity is standard analytic multiplicity: orders add in \(\Xi_\chi=\Lambda(s,\chi)\Lambda(s,\overline\chi)\).

Computational sanity check:
- `scripts/check_one_zero_sign.py` evaluates the simple test \(\beta=1/2,\gamma=0,t=0\). Output: `log_derivative_contribution=-8`, `positive_kernel=4`, `minus_half_log_derivative=4`, `plus_half_log_derivative=-4`. This supports the sign diagnosis and leaves the proof burden mathematical, not numerical.

Conditional on compact regularization:
- The formal zero package becomes a compact-interval identity only after the paired convergence/regularization mechanism proves that the regularized sum over the \(\Xi_\chi\) zero multiset can be exchanged with the boundary log-derivative on the chosen compact interval.
- The unified \(B_\chi^{\mathrm{pair}}\) becomes theorem-ready only when the conductor/scaling, gamma-derivative, trivial-zero/pole, and any Hadamard-normalization terms are fixed in the same convention as \(q_\chi^{\mathrm{pair}}\).
- The immediate post-theorem block can safely name \(B_\chi^{\mathrm{pair}}\), its component list, multiplicity bookkeeping, and scoped notation aliases.

Missing:
- A verified convention decision resolving the conflict between the currently recorded positive-exponent paired normalization and the positive zero-kernel source split for the fixed quotient.
- The paired compact-interval convergence/regularization theorem.
- A theorem-ready \(B_\chi^{\mathrm{pair}}\) formula in the same convention as the log-derivative identity.
- A compact-source multiplicity proposition saying explicitly that zeros are counted with analytic multiplicity in \(\Xi_\chi\), with coincident orders added.
- Exact realization of \(S_\chi^{\mathrm{pair}}(m)\) as the later manuscript value-channel slot; this report does not claim it.

## Baseline / delta

Baseline: the current cycle already fixes \(\Phi_\chi^{\mathrm{pair}}\) as the paired object, keeps UV-016 as blueprint/schema only, and places unified \(B_\chi^{\mathrm{pair}}\) plus multiplicity immediately after the theorem rather than inside the theorem body. Prior paired normalization reports recorded the positive-exponent convention \(e^{2i\Theta}\) as the safest interface if a phase is named.

Delta: this pass preserves the immediate bookkeeping-block scope but sharpens the source sign. For the quotient exactly as fixed, the positive strip-edge zero kernel is compatible with \(q=-\tfrac12(\Phi'/\Phi)\), equivalently the negative boundary phase convention with \(q=\Theta'\). If the team keeps \(e^{2i\Theta}\), it must change the source sign convention, use the inverse quotient, or explicitly define \(q=-\Theta'\); otherwise \(S_\chi^{\mathrm{pair}}\) is sign-reversed at the one-zero level.

## Attempt status

keep

## Exact refs

- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:19-31`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:40-44`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:66-70`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:5-13`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/attempts.md:15-32`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/dispatch.md:30-33`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/dispatch.md:60-67`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-69`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:80-99`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-21`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:37-64`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:19-38`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:24-57`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:73-99`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:38-53`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:106-125`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29-55`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:99-118`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeA/report.md:13-35`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeA/report.md:60-67`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeB/report.md:3-12`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeB/report.md:42-52`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-171036-paired-bookkeeping-block-verifier/report.md:3-17`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-171036-paired-bookkeeping-block-verifier/report.md:40-44`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-112325-paired-background-placement-routeA/report.md:21-25`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-112325-paired-background-placement-routeB/report.md:11-19`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-103532-paired-multiplicity-routeA/report.md:11-21`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-103532-paired-multiplicity-routeB/report.md:15-21`
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py:12-28`
- Script SHA256: `18598716D7404EC34E320FBE82DDF1E3AFA9D8E91AC4F51C58C70F4F9743BBB8`

## Dependencies

- The standard analytic fact that the logarithmic derivative of a meromorphic product counts zeros and poles with analytic multiplicity.
- The fixed quotient orientation \(\Xi_\chi(2s-1)/\Xi_\chi(2s)\). Reversing the quotient reverses the sign diagnosis.
- Regular boundary intervals avoiding zeros, poles, gamma singularities, and trivial-zero singularities.
- A later compact regularization theorem that justifies the zero sum and the background split on compact intervals.
- A later convention decision for whether \(q_\chi^{\mathrm{pair}}\) is defined as \(\Theta'\), \(-\Theta'\), \(+\tfrac12\Phi'/\Phi\), or \(-\tfrac12\Phi'/\Phi\).

## Strongest objection

The report conflicts with the current paired quotient-normalization route that recommended the positive exponent \(e^{2i\Theta}\). A verifier may find that those reports implicitly changed a sign elsewhere, inverted the quotient, or intended \(S_\chi^{\mathrm{pair}}\) to be the negative of the raw zero contribution. Until that is checked, this report should be treated as a sign-correction candidate, not as a promoted convention. The one-zero calculation shows that the fixed quotient plus \(q=\Theta'\) plus positive source kernel cannot all coexist with \(e^{2i\Theta}\).

## Needed for promotion

- An adversarial sign audit starting from the fixed quotient and writing all three objects in one place: boundary phase, log-derivative bridge, and \(q=B+S\).
- A choice between negative boundary exponent, redefining \(q\), or replacing the quotient by its inverse.
- A theorem-ready \(B_\chi^{\mathrm{pair}}\) derivation in that convention, including conductor/scaling, gamma derivatives, trivial-zero corrections, pole corrections if present, and any Hadamard-normalization term used by the proof.
- A compact regularization lemma for the \(\Xi_\chi\) nontrivial-zero multiset on regular compact intervals.
- A multiplicity paragraph saying that zero sums are over the \(\Xi_\chi\) multiset with analytic multiplicity, including added orders at coincidences.
- Separate later proof of exact \(S_\chi^{\mathrm{pair}}(m)\)-slot realization.

## Autoresearch next step

verify: run an adversarial source-sign check against `20260424-155603-paired-quotient-normalization-routeA/report.md` and decide whether the paired program should keep the quotient and use \(e^{-2i\Theta}\), keep \(e^{2i\Theta}\) but redefine \(q\), or invert the quotient before drafting the theorem-adjacent bookkeeping block.
