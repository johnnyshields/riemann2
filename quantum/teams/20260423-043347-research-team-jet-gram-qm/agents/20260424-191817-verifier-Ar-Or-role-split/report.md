# UV-013 verifier report: `O_r` versus `A_r` role split

## Claim

The UV-013 gap report is acceptable for promotion after wording fixes. The
decomposition and quotient statement are correct:
\[
A_r(\lambda)=\operatorname{span}\{\psi(\lambda)\}\oplus O_r(\lambda),
\qquad
O_r(\lambda)\cong A_r(\lambda)/\operatorname{span}\{\psi(\lambda)\}.
\]
This supports a scoped role criterion: `O_r` is the horizontal or
value-channel-removed object; `A_r` is the ambient endpoint subspace when the
state line is meant to remain inside the tested or transported subspace. The
current invariant package does not force a unique global winner.

The promotion must not say that the unlabeled principal-angle data of
`A_r(\lambda_-)` and `A_r(\lambda_+)` identifies the state line inside `A_r`.
It also must not say that `O_r` universally dominates `A_r`. The correct
statement is role-dependent and benchmark-scoped.

## Status

proved

## Evidence

No scripts were needed; this verifier pass is a linear-algebra and scope check
against the deposited reports.

Proved: the decomposition/quotient argument is valid. The note defines
\(j_k=(I-|\psi\rangle\langle\psi|)\partial_\lambda^k\psi\), so every generator
of `O_r` lies in \(\psi^\perp\). Hence the decomposition of `A_r` as the state
line plus `O_r` is orthogonal, and the restricted projector onto \(\psi^\perp\)
induces an isometric quotient map from `A_r/span{psi}` to `O_r`.

Proved: this is sufficient for a mathematical role criterion. If the intended
object removes the value/fidelity channel before comparing differential data,
`O_r` is the canonical quotient object. If the intended object is the ambient
endpoint subspace used in the current transport-free theorem, the Krylov
specialization, or an ideal membership test for the full subspace including the
state line, `A_r` is the object.

Conditional on wording: `A_r` contains the state line as part of its definition,
but the principal-angle multiset of an unlabeled pair of `A_r` subspaces does
not by itself mark which line inside each subspace is \(\operatorname{span}\psi\).
So promoted wording may say that `A_r` keeps the state line in the subspace or
projector being tested; it must not say that `A_r` principal-angle data alone
recovers the state line or fidelity channel.

Conditional on wording: benchmark evidence proves that `O_r` is not merely a
weaker shadow of `A_r`, and in the quartit `O_2` benchmark it is finer at the
principal-angle level. That does not imply universal dominance. The exact safe
claim is that neither package dominates for all roles from the current invariant
data alone.

Missing: a natural physical or experimental objective selecting one object in
all contexts. That missing item is not needed for UV-013 closure because UV-013
allows a scoped operational distinction or a precise no-global-winner statement.
It remains relevant to UV-014.

Honest verdict: accept the gap report for promotion with the caveats above.
UV-013 can close as a scoped role split, not as a physical selection theorem.

## Baseline / delta

Baseline: `jet_gram_quantum_note.md` already states the `O_r`/`A_r` split, the
quotient paragraph, the benchmark comparison, the Krylov specialization, and
the unsafe/open claims around a unique global choice. The UV-013 gap report
proposed turning that material into a closure.

Delta: this verifier pass confirms the closure but narrows its language. The
accepted promotion should be a role criterion plus scoped no-global-winner
statement. It should explicitly avoid two overclaims: state-line recovery from
unlabeled `A_r` principal angles, and universal superiority of `O_r` over
`A_r`.

## Attempt status

terminal

## Exact refs

- `quantum/paper/jet_gram_quantum_note.md:320-361` gives the definitions,
  decomposition, and quotient paragraph.
- `quantum/paper/jet_gram_quantum_note.md:363-368` gives the current benchmark
  comparison and role split.
- `quantum/paper/jet_gram_quantum_note.md:370-386` gives the exact
  unitary/Krylov ambient role.
- `quantum/paper/jet_gram_quantum_note.md:598-618` gives the quartit `O_2`
  representative and its refinement over `A_2`.
- `quantum/paper/jet_gram_quantum_note.md:689-693` gives the qutrit `O_1`
  equal-overlap separation.
- `quantum/paper/jet_gram_quantum_note.md:755-758` gives the Veronese
  value-channel-free benchmark-family statement.
- `quantum/paper/jet_gram_quantum_note.md:814-826` marks a unique global
  `A_r`/`O_r` choice as unsafe/open.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-191454-gap-Ar-Or-role-split/report.md`
  is the primary report under review.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-141906-attack-Ar-vs-Or/reports/gap-Ar-vs-Or.md`
  establishes the original role split.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-034240-attack-quotient/reports/gap-quotient.md`
  establishes the quotient theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md`
  establishes the qutrit/quartit benchmark comparison.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-184631-attack-qutrit-O1-witness/reports/gap-qutrit-O1-witness.md`
  gives the explicit qutrit `O_1` witness.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-144313-attack-quartit-O2/reports/gap-quartit-O2.md`
  gives the quartit `O_2` representative and refinement.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md`
  gives the ambient Veronese theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md`
  gives the value-channel-free Veronese theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md`
  gives the exact Krylov/compressed-Krylov specialization.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md`
  records the confirmed decomposition, quotient, benchmark, and Krylov facts.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md` contains
  UV-013.

## Dependencies

Normalized pure-state family; fixed ambient Hilbert space for endpoint subspace
comparison; projected jets \(j_k=(I-|\psi\rangle\langle\psi|)\partial^k\psi\);
established `O_r` and `A_r` subspace invariance; locally constant ranks when
principal angles are compared; standard Hilbert-space quotient linear algebra;
standard finite-dimensional principal-angle theory for the benchmark
comparisons; prior qutrit, quartit, Veronese, quotient, and Krylov reports.

## Strongest objection

The phrase "right object" can demand a physical protocol, not just a
mathematical role split. The current evidence does not select a globally
preferred object for every physical or experimental use. It only proves that
the present invariant package naturally supplies two linked objects with
different roles, and that no unique global winner is forced without adding an
external objective. This is enough for UV-013 as worded, but it does not close
UV-014.

## Needed for promotion

Promote wording close to:

> The two subspace packages are related by
> \(A_r=\operatorname{span}\{\psi\}\oplus O_r\). The projector
> \(I-|\psi\rangle\langle\psi|\) therefore identifies
> \(A_r/\operatorname{span}\{\psi\}\) isometrically with \(O_r\). Thus `O_r`
> is the canonical horizontal or value-channel-removed jet object, while `A_r`
> is the ambient extension when the state line is meant to remain part of the
> endpoint subspace, as in the present ambient principal-angle theorem and the
> exact unitary/Krylov specialization. The current invariant package gives this
> role split, not a global selection rule. Benchmark families show that `O_r`
> can carry value-channel-free principal-angle data not determined by overlap,
> and in the quartit `O_2` benchmark it refines the corresponding `A_2` datum;
> `A_r` remains the cleaner object for ambient subspace and Krylov statements.

Avoid wording like:

- "`A_r` principal-angle data identifies the state line" or "`A_r` recovers
  fidelity information by itself."
- "`O_r` is always finer than `A_r`" or "`O_r` is the preferred object."
- "`A_r` is the correct physical object" without naming the ambient-subspace,
  Krylov, or full-subspace-test role.
- "No physical criterion can choose one" without the scope qualifier "from the
  current invariant package alone."

## Autoresearch next step

terminal: UV-013 is ready for coordinator promotion with the wording caveats
above. Any stronger physical selection criterion belongs to UV-014 rather than
blocking this closure.
