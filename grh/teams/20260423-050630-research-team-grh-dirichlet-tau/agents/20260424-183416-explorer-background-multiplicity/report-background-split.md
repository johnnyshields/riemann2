# Claim

For the fixed quotient
\[
\Phi_\chi^{\mathrm{pair}}(s)
=\Xi_\chi(2s-1)/\Xi_\chi(2s),
\qquad
\Xi_\chi=\Lambda_\chi\Lambda_{\bar\chi},
\]
and the sign-audited boundary convention
\[
\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\,\prime},
\]
the completed-Hadamard source package, under the standard primitive
nonprincipal completed-\(L\) inputs, has no residual background after
subtracting all completed zeros with multiplicity:
\[
q_\chi^{\mathrm{pair}}(t)
=S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t),
\qquad
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=0.
\]
Equivalently, on regular boundary intervals,
\[
q_\chi^{\mathrm{pair}}(t)
=-\frac12
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}{\Phi_\chi^{\mathrm{pair}}}
\left(\frac12+it\right)
=D_\chi(t),
\]
where
\[
D_\chi(t)=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
If instead one writes a raw \(L\)-factor source using only the nontrivial zeros
of \(L(w,\chi)\) and \(L(w,\bar\chi)\), then the background is not zero by
definition: gamma, trivial-zero, pole, and raw Hadamard-normalization edge
differences belong to \(B_{\chi,\mathrm{raw}}^{\mathrm{pair}}\). The
conductor/scaling constant cancels in this fixed edge-difference convention.

# Status

proved

# Evidence

The sign-audited chain rule gives
\[
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}{\Phi_\chi^{\mathrm{pair}}}
\left(\frac12+it\right)
=2\frac{\Xi_\chi'}{\Xi_\chi}(2it)
-2\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
=-2D_\chi(t).
\]
Thus the positive scalar in the fixed convention is carried by
\(-\frac12\Phi'/\Phi\), matching the prior one-zero computation and the
adversarial sign audit.

For primitive nonprincipal \(\chi\), under the standard completed
order-one Hadamard input,
\[
\frac{\Xi_\chi'}{\Xi_\chi}(w)
=b_\chi+\sum_\rho m_\rho
\left(\frac1{w-\rho}+\frac1{\rho}\right).
\]
Taking the edge difference cancels both \(b_\chi\) and \(1/\rho\), leaving
\[
D_\chi(t)=
\sum_\rho m_\rho
\left(\frac1{1+2it-\rho}-\frac1{2it-\rho}\right).
\]
The compact-convergence lane and audit already checked that this summand is
\(O_I(|\rho|^{-2})\), with locally uniform compact convergence and fixed
derivative convergence away from edge hits. Therefore, in the completed-zero
normalization, the source split is theorem-ready modulo citation of the
standard completed-\(L\) inputs:
\[
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
=\Re\sum_\rho m_\rho
\left(\frac1{1+2it-\rho}-\frac1{2it-\rho}\right),
\qquad
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=0.
\]

The raw-factor split is a different convention. With conductor
\(\mathfrak q_\chi\) and parity \(a_\chi\),
\[
\Lambda(w,\chi)
=\left(\frac{\mathfrak q_\chi}{\pi}\right)^{(w+a_\chi)/2}
\Gamma\left(\frac{w+a_\chi}{2}\right)L(w,\chi),
\]
so
\[
\frac{\Xi_\chi'}{\Xi_\chi}(w)
=\log(\mathfrak q_\chi/\pi)
+\psi((w+a_\chi)/2)
+L'/L(w,\chi)+L'/L(w,\bar\chi).
\]
The \(\log(\mathfrak q_\chi/\pi)\) term cancels between \(1+2it\) and
\(2it\). The gamma background is
\[
B_{\gamma,\chi}^{\mathrm{pair}}(t)
=\Re\left[
\psi\left(\frac{1+a_\chi+2it}{2}\right)
-\psi\left(\frac{a_\chi+2it}{2}\right)\right].
\]
If \(T_\eta\) and \(P_\eta\) denote raw trivial-zero and pole multisets for
\(L(w,\eta)\), \(\eta\in\{\chi,\bar\chi\}\), then
\[
B_{\chi,\mathrm{raw}}^{\mathrm{pair}}
=B_{\gamma,\chi}^{\mathrm{pair}}
+B_{\mathrm{triv},\chi}^{\mathrm{pair}}
-B_{\mathrm{pole},\chi}^{\mathrm{pair}}
+B_{\mathrm{Had},\chi}^{\mathrm{pair}},
\]
with
\[
B_{\mathrm{triv},\chi}^{\mathrm{pair}}(t)
=\Re\sum_{\eta\in\{\chi,\bar\chi\}}\sum_{\tau\in T_\eta}
m_{\eta,\tau}
\left(\frac1{1+2it-\tau}-\frac1{2it-\tau}\right),
\]
\[
B_{\mathrm{pole},\chi}^{\mathrm{pair}}(t)
=\Re\sum_{\eta\in\{\chi,\bar\chi\}}\sum_{p\in P_\eta}
n_{\eta,p}
\left(\frac1{1+2it-p}-\frac1{2it-p}\right),
\]
and \(B_{\mathrm{Had}}\) equal to the real edge difference of any residual raw
Hadamard exponential. For primitive nonprincipal characters the raw pole set
is empty. In a completed-Hadamard edge-difference normalization,
\(B_{\mathrm{Had}}=0\); a nonzero \(B_{\mathrm{Had}}\) is a raw normalization
artifact.

This separates the two normalizations: completed zeros give
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\), while raw \(L\)-zeros require a
nonzero bookkeeping \(B_{\chi,\mathrm{raw}}^{\mathrm{pair}}\) unless the gamma,
trivial-zero, pole, and raw exponential pieces are folded back into the
completed zero multiset.

This proves the background-split subclaim from standard completed-\(L\)
bookkeeping. It does not by itself close UV-016, because promotion still needs
source citations for the standard completed-function inputs and an adversarial
check that the paper statement does not mix raw and completed normalizations.

# Baseline / delta

Baseline: UV-016 had compact zero-regularization checked, but the explicit
\(B_\chi^{\mathrm{pair}}\) split remained missing; UV-021 fixed the sign
normalization as negative boundary exponent with positive source scalar
\(-\frac12\Phi'/\Phi\).

Delta: this report resolves the \(B\)-split burden as a clean normalization
choice. The theorem-facing completed-Hadamard package can state
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) after subtracting all completed
zeros with multiplicity. The older safe component list remains valid only for
the raw \(L\)-factor convention, where those components are bookkeeping terms
created by not completing first.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:47` through `:66` fixes the sign convention and records compact edge-difference cancellation.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:5` through `:22` states UV-016 and its current reduction to explicit \(B_\chi^{\mathrm{pair}}\) plus source citations.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:61` through `:75` states UV-021 and the chosen source-normalization convention.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md:3` through `:39` gives the prior Jason log-derivative and multiplicity bookkeeping result.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py:1` through `:28` is the prior sign-check script; previous recorded output was `minus_half_log_derivative=4` and `plus_half_log_derivative=-4`.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md:3` through `:37` verifies the fixed-quotient sign convention.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:3` through `:21` accepts compact zero convergence in the scoped completed-Hadamard form.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:38` through `:67` lists the standard completed-function assumptions used by that audit.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:45` through `:57` gives the Hadamard edge-difference cancellation.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:93` through `:129` identifies \(D_\chi\), \(\Phi'/\Phi=-2D_\chi\), and leaves the \(B\)-split open.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:51` through `:64` scopes the post-theorem \(B_\chi^{\mathrm{pair}}\) and multiplicity bookkeeping.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:49` through `:76` records the sign audit update and the prior safe \(B\)-component list.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:36` through `:57` is the blueprint source theorem with \(q=B+S\).
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_candidate.tex:71` through `:84` records the earlier component-list version of the source package.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29` through `:55` gives the positive strip-edge one-zero kernel.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:106` through `:125` lists the source-theorem checklist items this report addresses.
- `C:/workspace/riemann2/grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:1` records this derivation note.

# Dependencies

- Primitive nonprincipal Dirichlet character, or explicit pole-removal
modification for principal characters.
- Standard completed-\(L\) facts: \(\Xi_\chi\) entire of order one, genus-one
Hadamard product, zero multiset with analytic multiplicity, and paired
functional equation/real boundary compatibility.
- Compact interval avoids edge hits \(2it=\rho\) and \(1+2it=\rho\); if a zero
at \(\rho=0\) appears, its finite factor is separated before using the
\(1/\rho\) regularized product notation.
- The source scalar is interpreted in the sign-audited convention:
\(\Phi=e^{-2i\Theta}\), \(q=\Theta'\), positive zero layer
\(-\frac12\Phi'/\Phi\).
- Raw \(L\)-factor \(B\) formulas require a declared raw Hadamard
normalization and explicit treatment of gamma/trivial-zero cancellations on
intervals crossing those singularities.

# Strongest objection

The completed \(B=0\) formula is theorem-ready only after the paper cites the
standard primitive nonprincipal completed-\(L\) package in the exact form used
by the compact-convergence audit. Without that source citation, the result is
a derived bookkeeping reduction from standard inputs, not yet a promoted
paper theorem. A second objection is normalization drift: if the paper keeps
the older raw component-list language while also summing completed zeros, it
will double-count gamma/trivial-zero structure.

# Needed for promotion

1. Add or cite a standard source for primitive Dirichlet completed functions:
entire order one, genus-one Hadamard product, zero multiplicities, and the
functional equation properties needed for the paired boundary scalar.
2. Rewrite the UV-016 source statement to declare the completed-Hadamard
normalization first:
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) and
\(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\) sums all completed zeros with
multiplicity.
3. Move the raw \(L\)-factor component list to a bookkeeping remark, explicitly
marked as a different normalization, with conductor/scaling component equal
to zero in the fixed edge-difference convention.
4. State edge-exclusion and possible \(\rho=0\)/principal-character
modifications.
5. Get an adversarial source-normalization verifier to check that the
completed-zero statement does not double-count gamma/trivial-zero terms.

# Autoresearch next step

verify: assign an adversarial source-normalization check before promotion.
The verifier should cite a standard primitive Dirichlet completed-\(L\)
reference for the exact inputs used here, then audit the proposed theorem
wording for normalization drift: if \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\)
sums all completed zeros of \(\Xi_\chi=\Lambda_\chi\Lambda_{\bar\chi}\), then
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) and gamma/trivial-zero data must
not be added again. Gamma, trivial-zero, pole, and raw Hadamard terms belong
only to the separate raw \(L\)-factor bookkeeping remark.
