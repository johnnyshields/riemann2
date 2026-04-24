## Claim

The compact zero-regularization layer of UV-016 can be separated and proved: for the paired completed function \(\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline{\chi})\), the strip-edge difference
\[
\sum_{\rho} m_\rho\,\Re\left((1+2it-\rho)^{-1}-(2it-\rho)^{-1}\right)
\]
converges absolutely and uniformly on every compact interval avoiding edge zeros, and the same holds after fixed \(t\)-derivatives. Multiplicity is handled by the coefficient \(m_\rho\). Full UV-016 remains open from this agent scope alone because the source-normalized phase sign and theorem-ready explicit \(B_\chi^{\rm pair}\) split are not closed by this convergence proof.

## Status (proved|computational|heuristic|open|rejected)

proved

## Evidence

Proved: `notes/compact_regularization_reduction.md` gives the compact theorem and proof. The key point is that the genus-one Hadamard logarithmic derivative has nonabsolute individual zero sums, but the edge difference cancels the Hadamard constant and \(1/\rho\) regularizers. For \(w_-(t)=2it\), \(w_+(t)=1+2it\), and \(t\in I\), the summand is
\[
(w_+(t)-\rho)^{-1}-(w_-(t)-\rho)^{-1},
\]
which is \(O_I(|\rho|^{-2})\) for large \(\rho\). Since the completed paired function is order one, \(\sum_\rho m_\rho|\rho|^{-2}<\infty\). The Weierstrass test gives compact uniform convergence, and derivative convergence follows from the same bound after differentiation.

Proved: the one-zero real part is exactly the positive strip-edge kernel already isolated in `paper/strip_edge_kernel_note.tex`. The paired proof preserves multiplicities by summing each zero with coefficient \(m_\rho\); coincident zeros from the \(\chi\) and \(\overline{\chi}\) factors simply add.

Conditional: the proof uses standard completed Dirichlet \(L\)-function facts: \(\Xi_\chi\) is entire of order one, has the paired functional equation, and admits the genus-one Hadamard product with zeros counted by multiplicity. These are standard inputs but still need a source-audit pass before paper promotion.

Missing: the compact convergence theorem does not identify an explicit component formula for \(B_\chi^{\rm pair}\) in the raw \(L\)-factor split. It also exposes a sign-normalization boundary: for the fixed quotient \(\Phi_\chi^{\rm pair}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)\), the positive edge sum is \(D_\chi(t)=\Xi_\chi'/\Xi_\chi(1+2it)-\Xi_\chi'/\Xi_\chi(2it)\), while \((\Phi_\chi^{\rm pair})'/\Phi_\chi^{\rm pair}=-2D_\chi(t)\) on the boundary. A source-normalization theorem must choose the phase convention or inverse quotient that makes the positive edge sum the \(+S_\chi^{\rm pair}\) term.

No computation was run.

## Baseline / delta

Baseline: the team state and prior UV-016 verifier reports said the paired compact source package was blueprint/schema only, with compact-interval convergence/regularization, unified \(B_\chi^{\rm pair}\), and multiplicity still coupled open burdens.

Delta: this report upgrades the compact zero-summation subproblem from blueprint to a precise proof target with proof, conditional only on standard completed-\(L\) entire-function inputs. It also reduces the remaining UV-016 obstruction to two concrete theorem statements: phase-normalized \(q=B+S\) orientation, and explicit theorem-ready \(B_\chi^{\rm pair}\) background splitting in the same normalization.

## Attempt status (keep|discard|blocked|terminal|crash)

keep

## Exact refs

- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:5` - theorem target.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:11` - completed-\(L\) hypotheses.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:16` - compact strip-edge series and multiplicity convention.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:36` - Hadamard cancellation proof.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:59` - \(O(|\rho|^{-2})\) convergence estimate.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:83` - positive one-zero kernel.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:93` - phase and background boundary.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-183416-gap-compact-regularization\notes\compact_regularization_reduction.md:122` - smallest remaining theorem statements.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\notes\paired_source_package.md:7` - blueprint ceiling before this deposit.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\notes\paired_source_package.md:12` - regularization was the first real burden.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\notes\paired_source_package.md:61` - post-theorem \(B_\chi^{\rm pair}\) and multiplicity placement.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\paper\dirichlet_paired_source_package_candidate.tex:22` - paired object.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\paper\dirichlet_paired_source_package_candidate.tex:34` - blueprint theorem.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\paper\strip_edge_kernel_note.tex:29` - positive strip-edge kernel lemma.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\notes\quotient_normalization.md:8` - sign is the normalization issue.
- `C:\workspace\riemann2\grh\teams\20260423-050630-research-team-grh-dirichlet-tau\agents\20260424-143617-paired-regularization-plan-verifier\report.md:3` - prior endpoint was blueprint only.

## Dependencies

- Standard primitive nonprincipal Dirichlet completed-\(L\) package: \(\Lambda(s,\chi)\) entire of order one, paired product \(\Xi_\chi\) entire of order one, self-dual paired functional equation, and genus-one Hadamard product.
- A compact interval \(I\) avoiding edge zeros of \(\Xi_\chi\); for primitive nonprincipal characters this should be automatic for ordinary singularity-free source intervals, but it should still be stated.
- The project must choose a phase convention for \(\Phi_\chi^{\rm pair}\) or invert the quotient so that the positive edge sum has the \(+S_\chi^{\rm pair}\) orientation.
- A separate background-split theorem must identify \(B_\chi^{\rm pair}\) in conductor/gamma/trivial-zero or pole terms in the same normalization.

## Strongest objection

The proof may be judged too narrow because it proves convergence for the completed paired edge-difference sum, while UV-016 asks for a unified theorem-ready \(B_\chi^{\rm pair}\) and source identity. That objection is correct. The keep-value is that the first analytic obstruction, compact convergence/regularization of the zero contribution, is no longer the blocker once standard completed-function inputs are allowed. From this scope alone, the remaining blocker is not convergence but normalization: decide the phase sign and prove the explicit background split in the same convention.

## Needed for promotion

1. Source-audit the standard completed Dirichlet facts used in the proof.
2. Adversarially verify the phase-sign computation against the existing quotient-normalization notes.
3. Decide the theorem convention: positive edge sum via the current quotient with negative boundary phase, or positive boundary phase via the inverse quotient.
4. Prove the explicit \(B_\chi^{\rm pair}\) split in the chosen convention.
5. Then fold the compact convergence theorem, multiplicity coefficient \(m_\rho\), and \(B_\chi^{\rm pair}\) bookkeeping into one compact source-package statement.

## Autoresearch next step (continue|verify|blocked|terminal)

verify: send this compact convergence proof to an adversarial verifier, with special focus on the sign bridge \((\Phi_\chi^{\rm pair})'/\Phi_\chi^{\rm pair}=-2D_\chi\), the use of order-one Hadamard summability, and whether the completed-zero sum is compatible with the desired raw \(L\)-factor \(B_\chi^{\rm pair}\) split.
