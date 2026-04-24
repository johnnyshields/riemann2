# UV-013 gap report: `O_r` versus `A_r`

## Claim

UV-013 can close with a role criterion plus a scoped no-global-winner theorem.

**Proved.** For a normalized pure-state family with projected jets
\(j_k=P\partial^k\psi\), \(P=I-|\psi\rangle\langle\psi|\), one has the
orthogonal pointwise decomposition
\[
A_r(\lambda)=\operatorname{span}\{\psi(\lambda)\}\oplus O_r(\lambda),
\qquad
O_r(\lambda)=\operatorname{span}\{j_1(\lambda),\dots,j_r(\lambda)\}.
\]
The restricted orthogonal projector \(P:A_r\to O_r\) has kernel
\(\operatorname{span}\{\psi\}\) and induces the canonical Hilbert-space quotient
\[
A_r/\operatorname{span}\{\psi\}\cong O_r.
\]

**Role criterion.** Use \(O_r\) when the intended object is horizontal,
value-channel-removed jet geometry, or when the state line/fidelity channel
should be quotiented out before comparing higher differential data. Use \(A_r\)
when the intended object is a transport-free ambient endpoint subspace package,
the exact unitary/Krylov specialization, or a projector-test package whose
subspace includes the state line.

**No-global-winner theorem.** From the current invariant package alone, no unique
global choice between \(O_r\) and \(A_r\) is forced. They answer different
questions related by quotient/extension, and neither dominates the other as the
right object for all roles. \(O_r\) can carry richer or finer benchmark
principal-angle data than \(A_r\), while \(A_r\) retains the state line and
supports the cleanest ambient/Krylov theorem. A universal preference would add
an external objective not present in the current invariants.

## Status

proved

## Evidence

No scripts were needed; the argument is linear algebra plus prior deposited
benchmark and quotient reports.

**Proved:** \(O_r\subset \psi^\perp\) because every generator is projected by
\(P=I-|\psi\rangle\langle\psi|\). The definitions then give
\(A_r=\operatorname{span}\{\psi\}\oplus O_r\). For any \(v=a\psi+o\in A_r\),
\(Pv=o\), so \(P|_{A_r}\) is surjective onto \(O_r\) with kernel
\(\operatorname{span}\{\psi\}\). Orthogonality makes the induced quotient map
isometric.

**Proved:** \(O_r\) is the correct object for value-channel-removed geometry:
it is exactly the quotient of the ambient package by the state line. This matches
the original horizontal/jet-normalized motivation and the first-order QGT bridge.

**Proved:** \(A_r\) is the correct object when the state line belongs in the
ambient endpoint package. The current note states the strongest transport-free
two-point theorem at the ambient-subspace level, and exact unitary orbits give
\[
A_r(t)=e^{-itH}\operatorname{span}\{\psi_0,H\psi_0,\dots,H^r\psi_0\},
\]
while \(O_r(t)\) is the compressed/value-channel-removed counterpart.

**Confirmed by benchmarks:** the qutrit \(O_1\), quartit \(O_2\), and
Veronese \(O_{n-1}\) reports prove that the value-channel-free data is not
merely a weaker shadow of \(A_r\). In the quartit benchmark, \(O_2\) has two
generally nontrivial principal-angle cosines while \(A_2\) retains only their
product as its single nontrivial ambient cosine.

**Missing:** a stronger physical objective that would make one role universally
preferred. That is not missing for UV-013 closure, because the UV explicitly
allows a criterion or a precise statement that no unique global winner is forced.
It remains relevant only to UV-014 if a future protocol chooses one object.

Honest verdict: UV-013 is closed from the present invariant package. The
promotable statement is not "prefer \(O_r\)" or "prefer \(A_r\)" globally; it is
the role criterion above and the scoped no-global-winner theorem.

## Baseline / delta

Baseline: prior reports had separately established the decomposition
\(A_r=\operatorname{span}\{\psi\}\oplus O_r\), the quotient interpretation
\(O_r\cong A_r/\operatorname{span}\{\psi\}\), and benchmark evidence where
\(O_r\) is richer-than-overlap and sometimes finer than \(A_r\). The paper still
listed as open the decision criterion for using \(O_r\) versus \(A_r\).

Delta: this report converts those pieces into a closure: a role criterion based
on quotient versus ambient extension, plus a scoped no-global-winner theorem
from the current invariant package. It improves the baseline by stating what
would and would not count as a universal selection principle.

## Attempt status

terminal

## Exact refs

- `quantum/paper/jet_gram_quantum_note.md:343-368` states the current `O_r` /
  `A_r` split, the quotient paragraph, and the benchmark comparison.
- `quantum/paper/jet_gram_quantum_note.md:370-379` states the exact
  unitary/Krylov role split.
- `quantum/paper/jet_gram_quantum_note.md:598-618` states the quartit `O_2`
  representative and its strict refinement over `A_2`.
- `quantum/paper/jet_gram_quantum_note.md:689-693` states the qutrit `O_1`
  equal-overlap separation.
- `quantum/paper/jet_gram_quantum_note.md:755-758` states the value-channel-free
  Veronese benchmark-family corollary.
- `quantum/paper/jet_gram_quantum_note.md:814-820` currently marks a unique
  global `A_r`/`O_r` choice as unsafe.
- `quantum/paper/jet_gram_quantum_note.md:823-827` is the open-problem entry
  corresponding to UV-013.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md`
  records the confirmed decomposition, quotient theorem, benchmark refinement,
  and remaining missing criterion.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md` contains
  UV-013 verbatim.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/dispatch.md`
  contains the 20260424-191454 UV-013 ground-truth check.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/attempts.md`
  records this agent as the running UV-013 role-split target.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md`
  records UV-011 and UV-012 as promoted and UV-013 as the next structural target.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-141906-attack-Ar-vs-Or/reports/gap-Ar-vs-Or.md`
  proves the decomposition and initial split-role claim.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md`
  proves the qutrit and quartit `O_r` benchmark comparisons.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-034240-attack-quotient/reports/gap-quotient.md`
  proves the quotient theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-184631-attack-qutrit-O1-witness/reports/gap-qutrit-O1-witness.md`
  gives an explicit equal-overlap / different-`O_1` witness.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-144313-attack-quartit-O2/reports/gap-quartit-O2.md`
  proves the compact `O_2` representative and refinement over `A_2`.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md`
  proves the ambient order-\(n-1\) Veronese theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md`
  proves the value-channel-free order-\(n-1\) Veronese theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md`
  proves the exact Krylov/compressed-Krylov specialization.

## Dependencies

Fixed ambient Hilbert space; normalized pure-state family; projected jets
\(j_k=P\partial^k\psi\); established gauge/chart invariance of the \(O_r\) and
\(A_r\) subspace filtrations; locally constant ranks when comparing principal
angles; standard quotient Hilbert-space linear algebra; standard principal-angle
theory; prior qutrit, quartit, and Veronese benchmark theorems; exact unitary
orbit/Krylov theorem.

## Strongest objection

The phrase "right object" can mean a physical preference, not just a mathematical
role criterion. This report does not prove a new physical protocol selecting
one object in all contexts. It proves the scoped closure UV-013 asks for: from
the present invariant package, \(O_r\) is the quotient/horizontal object,
\(A_r\) is the ambient extension including the state line, and no unique global
winner is forced. A later UV-014 protocol could still choose one role for a
specific experiment or dynamics.

## Needed for promotion

Add a short theorem/remark near the existing `O_r`/`A_r` discussion:

> Since \(A_r=\operatorname{span}\{\psi\}\oplus O_r\), the restricted projector
> \(I-|\psi\rangle\langle\psi|\) identifies \(A_r/\operatorname{span}\{\psi\}\)
> isometrically with \(O_r\). Thus \(O_r\) is the canonical
> value-channel-removed or horizontal-jet object, while \(A_r\) is the canonical
> ambient extension when the state line is part of the endpoint package. The
> current invariants therefore give a role split, not a global selection rule:
> benchmark families show that \(O_r\) can carry finer value-channel-free
> principal-angle data, whereas \(A_r\) supports the cleanest ambient/Krylov
> theorem and projector test including the state line.

Before removing UV-013, run one adversarial verifier pass focused on two wording
risks: do not imply that \(A_r\) principal-angle data by itself identifies the
state line inside \(A_r\), and do not imply that \(O_r\) universally contains
more invariant information than \(A_r\).

## Autoresearch next step

verify: adversarially check the proposed role criterion and no-global-winner
wording, especially the state-line wording for `A_r` and the non-dominance claim
between endpoint principal-angle packages.
