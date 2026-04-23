Claim

Within primitive nonprincipal complex characters, parity should remain neutral for the first paired-source theorem. Fixing to even or to odd gives the same kind of simplification: it freezes one archimedean gamma-factor template and its matching trivial-zero/background bookkeeping across the statement. From current scope alone, there is no evidence that even parity or odd parity materially shortens the exact paired-source burden. The safest wording is narrower: for the paired theorem-facing formulation, one may fix a parity to avoid an `a_\chi\in\{0,1\}` case split, but neither parity currently deserves priority.

Status

open

Evidence

Proved from the supplied notes.

- The project priority note already gives the controlling boundary: fixing parity is only a statement-level simplifier, not a theorem-level reduction of burden.
- The paired-source note says the paired route still leaves the real work open: exact source theorem, exact local-slot identification, denominator comparability, corrected whitening, odd/transverse realization, and boundary control. None of those are stated there as parity-sensitive at the theorem-statement level.
- The subclass verifier already scope-weakened the stronger claim `complex with fixed parity is the cleanest subclass` to the narrower statement that fixed parity is only a presentation simplifier unless further analytic savings are proved.
- The odd-package note makes a separate point that matters here: the downstream `odd/transverse` package is an independent theorem target. That `odd` is the parity of the realized transverse scalar, not the parity of the Dirichlet character. So odd characters do not receive a bookkeeping bonus from that downstream label alone.

Conditional on standard facts.

- For a primitive character `\chi`, the completed factor has one of the two standard archimedean types indexed by `a_\chi\in\{0,1\}`; `\bar\chi` has the same parity. Hence the paired object `\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)` stays within a single gamma template once parity is fixed.
- Even parity and odd parity therefore each remove the same kind of theorem-statement nuisance: a mixed `a_\chi=0` versus `a_\chi=1` case split in the background term and corresponding trivial-zero bookkeeping.
- Odd parity may look superficially closer to the repo's later `odd` package, but that is only terminological. From current scope alone, character parity does not supply the realized odd holomorphic transverse scalar or its boundary control.

Missing.

- No supplied note proves that even parity gives simpler exact background identification than odd parity, or vice versa.
- No supplied note proves that one parity interacts better with compact-interval regularization, exact `S(m)`-slot realization, denominator control, whitening, or boundary transport.
- No supplied note proves that the trivial-zero pattern in one parity yields a shorter first paired-source theorem once the full bookkeeping is written out.
- No head-to-head theorem statement is currently written comparing the even and odd primitive-complex paired formulations on the same checklist.

Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:18-25`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:40-55`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:66-73`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:6-20`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:22-49`
- `/mnt/c/workspace/riemann2/tasks/20260423-191325-attack-gap-dirichlet-subclass/reports/verifier-adversarial-dirichlet-subclass.md:1-4`
- `/mnt/c/workspace/riemann2/tasks/20260423-191325-attack-gap-dirichlet-subclass/reports/verifier-adversarial-dirichlet-subclass.md:19-29`
- `/mnt/c/workspace/riemann2/tasks/20260423-191325-attack-gap-dirichlet-subclass/reports/verifier-adversarial-dirichlet-subclass.md:65-72`

Dependencies

- The supplied `grh/` notes are treated as the boundary for what is proved versus still open.
- Standard primitive Dirichlet completed-`L` facts: parity parameter `a_\chi\in\{0,1\}`, identical parity for `\chi` and `\bar\chi`, and parity-dependent gamma/trivial-zero bookkeeping.
- The repo's distinction between front-end theorem statement choices and the still-missing exact source/local-slot theorem.
- The explicit separation between character parity and the independent odd/transverse realization package.

Strongest objection

The strongest objection is that the report may be undercounting a real asymmetry in the trivial-zero or background bookkeeping between even and odd characters. It is possible that, once the theorem is written in full detail, one parity will have a genuinely shorter correction term or cleaner compact-interval normalization. Current scope does not prove that. It proves only the weaker point that fixed parity removes a case split, and that the main open burdens sit elsewhere.

Needed for promotion

1. Write one theorem-facing paired-source statement for primitive nonprincipal complex characters of even parity and one of odd parity, with the full proposed background term shown explicitly.
2. Compare those two statements on the same checklist: gamma factor, trivial-zero corrections, compact-interval normalization, exact local-slot identification target, and any boundary terms.
3. Check explicitly whether either parity simplifies the unified `B_\chi^{\mathrm{pair}}` bookkeeping beyond merely freezing `a_\chi`.
4. Keep the current wording neutral unless such a comparison shows a real savings.
5. Honest verdict: for the first paired-source theorem, parity is a scoped bookkeeping choice, not a priority choice. Fix one parity if a cleaner statement is wanted, but do not currently prefer even over odd or odd over even.
