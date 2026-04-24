# Collation

## Capture sweep before resume - 20260424-183112

Read `HANDOFF-20260424.md`, `INDEX.md`, `findings.md`, the paper open-problem
block, top-level reports, recent lore, and the `agents/*/reports/*.md`
inventory. The existing `findings.md` already captures the promoted claims from
the older deposits: first-order QGT bridge, first-jet transport caveats,
higher-jet subspace survival, multiparameter subspace/covariant jets, the
operator package, benchmark families, exact unitary/Krylov specialization, Kato
transport, and Kato curvature obstruction.

No prior report requires immediate paper demotion. The live capture miss is
structural rather than mathematical: the team dir had no `uv.md`,
`attempts.md`, `dispatch.md`, or `collation.md`, and one older subdir,
`agents/20260424-040334-attack-biunitary-classification/`, has no report.
Filed UV-011 through UV-015 from the current open-problem frontier and assigned
the missing biunitary classification question to UV-012.

Honest verdict: the quantum track is not blocked on rediscovering examples.
The next useful cycle should decide whether the operator/subspace package is
final, and if not, identify the exact extra structure that selects a matrix or
frame.

## Deep read update - 20260424-183451

Read all top-level files, all `agents/*/reports/*.md`, and the agent notes. The
prior attack sequence already moved from broad analogy to a mature theorem
stack. The strongest unresolved theorem-sized target is not a new benchmark or a
new covariant-jet hierarchy; it is the missing biunitary classification of
orthonormal-frame comparison matrices for a fixed subspace pair. This is the
only old agent brief with no report, and it is exactly the theorem needed to
turn the current operator package into an explicit negative closure of the
general matrix-canonicity problem.

Decision: revise the resume from a default balanced roster to a focused UV-012
attack with one gap-closer and one adversarial verifier. UV-011, UV-013,
UV-014, and UV-015 remain open, but they are lower leverage until UV-012 is
settled.

## Gap return - 20260424-183451

`agents/20260424-183451-gap-biunitary-matrix-finality/report.md` gives the
missing finite-dimensional orbit theorem for UV-012. For fixed endpoint
subspaces with orthonormal frame maps \(U_-:\mathbb C^p\to S_-\) and
\(U_+:\mathbb C^q\to S_+\), the comparison matrix
\(A=U_-^*U_+\) is the matrix of the canonical cross-contraction
\(C=\Pi_-|_{S_+}\). Changing frames gives exactly \(A\mapsto L^*AR\), and
every orthonormal-frame comparison matrix for the same pair arises in this way.
The rectangular SVD classifies the orbit by singular values, including
rank-deficient and unequal-dimensional cases. These singular values are the
principal-angle cosines.

Provisional verdict: keep. If an adversarial verifier accepts the naturality
wording, UV-012 should close negatively from the fixed subspace-pair data alone:
the canonical object is the operator/principal-angle package, while an entrywise
matrix requires extra frame-selecting structure except in the already qualified
simple-spectrum diagonal-frame sector.

## Verifier return - 20260424-183451

`agents/20260424-183451-verifier-biunitary-finality/report.md` accepts the
gap report for promotion. The verifier checked the frame-coordinate identity
\(U_-^*CU_+=U_-^*U_+\), the exact left-right frame-change law, rectangular SVD
classification including rank-deficient and unequal-dimensional cases, and the
normal-form caveat. A sorted SVD diagonal is only an orbit representative
encoding dimensions and singular values; it is not an endpoint-selected
comparison matrix.

Decision: promote UV-012 with scoped wording. The theorem closes the
frame-comparison matrix question for data determined by the fixed subspace pair
alone. It does not rule out matrices built from extra dynamical, transport,
ordering, or symmetry-breaking structure.

## Promotion - UV-012

Promoted the verified theorem into
`quantum/paper/jet_gram_quantum_note.md` after the cross-contraction/polar
paragraph. The note now states the full biunitary-orbit classification for
orthonormal-frame comparison matrices, including rectangular/rank-deficient
normal-form caveats, and the safe-claims/open-problems list no longer treats the
fixed-subspace endpoint matrix question as open.

Updated `findings.md` with the confirmed orbit theorem and removed the matching
missing frame/matrix bullet. Removed UV-012 from `uv.md`.

Next move: use this theorem as leverage on UV-011. The remaining matrix problem
is narrower: whether multiparameter covariant-jet structure adds a genuine
natural frame/order beyond the already-safe subspace hierarchy, or whether the
same frame-selection obstruction closes it negatively.

## Gap return - UV-011

`agents/20260424-190708-gap-multiparameter-frame-finality/report.md` argues for
a scoped negative closure of UV-011. The proof combines the existing
block-upper-triangular chart/gauge laws for raw mixed partials, the
Berry-covariant and symmetrized-jet span theorems, and the promoted UV-012
biunitary-orbit theorem. The claimed survivor is the filtered subspace data
\(O_r,A_r\), endpoint projectors, cross-contractions, polar partial isometries,
and principal-angle spectra. Ordered frames and entrywise matrices require
extra frame-selecting structure.

Provisional verdict: keep pending adversarial verification. The main wording
risk is scope: the theorem must say "from the ray-field/subspace data alone" and
must not exclude tensor-valued associated-graded objects or matrices built after
adding a source metric, connection, dynamics, protocol, or symmetry breaking.

## Verifier return and promotion - UV-011

`agents/20260424-191018-verifier-multiparameter-frame-finality/report.md`
accepts the UV-011 gap report for promotion with scope fixes. The verifier
confirmed that raw mixed-partial arrays fail as ordered canonical data under
block-upper-triangular phase/chart laws; Berry-covariant and symmetrized jets
repair gauge covariance and span generation but do not choose bases; and UV-012
is applied only after reduction to endpoint subspaces `O_r` or `A_r`.

Promoted the scoped no-go into `quantum/paper/jet_gram_quantum_note.md` and
removed UV-011 from `uv.md`. The promoted wording leaves room for matrices
after adding explicit frame-selecting structure and for associated-graded or
tensor-valued jet symbols as separate basis-free objects.

Remaining open UVs: UV-013 (`O_r` versus `A_r`), UV-014 (natural
dynamical/experimental protocol), and UV-015 (nonbenchmark genericity).

## Gap return - UV-013

`agents/20260424-191454-gap-Ar-Or-role-split/report.md` proposes closing UV-013
with a role criterion plus no-global-winner theorem. The exact relation
\(A_r=\operatorname{span}\{\psi\}\oplus O_r\) and the quotient theorem identify
`O_r` as the horizontal/value-channel-removed object. `A_r` is the ambient
extension when the state line belongs in the endpoint package, including the
transport-free ambient theorem, unitary/Krylov specialization, and projector
tests. Benchmark reports show `O_r` is not merely weaker and can be finer at the
principal-angle level, while `A_r` keeps state-line information.

Provisional verdict: keep pending adversarial verification. The verifier should
check that the role criterion does not imply `A_r` principal-angle data alone
identifies the state line, and does not imply `O_r` universally dominates `A_r`.

## Verifier return and promotion - UV-013

`agents/20260424-191817-verifier-Ar-Or-role-split/report.md` accepts the UV-013
role split for promotion. The verifier confirmed the decomposition and quotient
criterion, and narrowed the wording: `A_r` contains the state line by
definition, but unlabeled `A_r` principal-angle data does not identify that line;
benchmark refinements show `O_r` can be finer in some roles, not that it
universally dominates.

Promoted the role criterion into `quantum/paper/jet_gram_quantum_note.md` and
removed UV-013 from `uv.md`. Stronger physical selection is deferred to UV-014,
not treated as a blocker for UV-013.

Remaining open UVs: UV-014 (natural dynamical/experimental protocol) and UV-015
(nonbenchmark genericity).

## Gap return - UV-014

`agents/20260424-192133-gap-natural-protocol/report.md` proposes a positive
closure for UV-014 under coherent reflection access. For endpoint projectors
\(\Pi_\pm\), define \(R_\pm=2\Pi_\pm-I\). On each principal two-plane, the
unitary \(R_-R_+\) has eigenphases \(\pm2\theta_i\), so phase estimation or
alternating-reflection dynamics estimates the principal-angle spectrum. This is
stronger operationally than the one-shot yes/yes test, but it recovers the same
canonical endpoint operator data rather than a new invariant or matrix.

Provisional verdict: keep pending adversarial verification. The verifier should
check the coherent-reflection access assumption, the principal-plane sign
convention, and the wording boundary between "natural protocol" and "new
invariant."

## Verifier return and promotion - UV-014

`agents/20260424-192735-verifier-natural-protocol/report.md` accepts the
two-reflection protocol for promotion. The verifier checked the principal
two-plane calculation, the \(\theta=0\) and \(\theta=\pi/2\) exceptional
sectors, the common orthogonal-complement padding, and the unequal-dimensional
bookkeeping. The promoted claim is conditional on coherent reflection access and
adequate state preparation or sampling.

Promoted the reflection/phase-estimation paragraph into
`quantum/paper/jet_gram_quantum_note.md`, updated `findings.md`, and removed
UV-014 from `uv.md`. The text states that this is a protocol for reading the
existing principal-angle/operator package, not a new invariant, matrix
representative, or universal Hamiltonian model.

Remaining open UV: UV-015 (nonbenchmark genericity).

## Gap return - UV-015

`agents/20260424-193527-gap-nonbenchmark-genericity/report.md` gives a
finite-jet genericity theorem for first-order value-channel-free data. For
normalized \(C^2\) curves in dimension at least \(3\), the local independence of
endpoint overlap and the `O_1` line-angle scalar is detected by an endpoint
2-jet determinant \(\Delta\). The report proves that \(\Delta\ne0\) is an open
dense condition on the admissible endpoint 2-jet chart, with pullback versions
for submersive finite-dimensional curve families and non-identically-zero
analytic/algebraic families.

The report includes `scripts/verify_o1_jet_determinant.py`; rerun locally, it
checks the normalized seed constraints and returns `C = 1/2`,
`Delta = 1/4*sqrt(2)`, with SHA256
`9290A89C67780A4D35DC3B5E19892B1135E39B643170D2B55F55D2CA6680FD13`.

Provisional verdict: keep pending adversarial verification. The verifier should
check the determinant formula, the endpoint-jet interpolation/density step, and
the scope caveats: first-order `O_1`, real-open-dense complex interpretation,
and no blanket claim for all higher `O_r/A_r` observables.

## Verifier return and promotion - UV-015

`agents/20260424-194246-verifier-nonbenchmark-genericity/report.md` accepts the
finite-jet genericity theorem for promotion. The verifier independently checked
the endpoint formulas, the admissible seed jet, the nonzero determinant, the
local sphere-chart interpolation of endpoint 2-jets, and the finite-family
pullback hypotheses. It also added
`agents/20260424-194246-verifier-nonbenchmark-genericity/scripts/verify_uv015_seed.py`,
whose SHA256 is
`85F3F3E3A40A74F2DD851727C78FCEC67417C02FE263D06AC0601BB4C9949D5D` and whose
output again gives `C = 1/2`, `Delta = 1/4*sqrt(2)`.

Promoted the scoped first-order real finite-jet `O_1` genericity theorem into
`quantum/paper/jet_gram_quantum_note.md`, updated `findings.md`, and removed
UV-015 from `uv.md`. The text does not claim genericity for all higher
`O_r/A_r` observables, for arbitrary finite-dimensional families without rank
hypotheses, or for holomorphic complex-Zariski genericity.

Honest verdict: all UV entries in the quantum ledger are now closed. A
subsequent hardening/audit pass should check the note globally before declaring
the whole quantum side track final.

## Hardening sweep - post-UV ledger

The first coordinator hardening sweep found stale global language left over from
the pre-promotion state. In `quantum/paper/jet_gram_quantum_note.md`, the
opening package summary still framed the matrix question as open, and the
multiparameter section still said the matrix story remained unresolved. These
were updated to match the promoted UV-011/UV-012 state: the canonical object is
the subspace/operator/principal-angle package; fixed-frame matrices are
classified only up to a biunitary orbit; and entrywise representatives require
extra frame-selecting structure.

`findings.md` had grown to 263 lines, past the briefing-size limit. I pruned it
to 110 lines, kept only active briefing material, and created
`quantum/findings-in-paper.md` as a grep index for matured findings absorbed
into `quantum/paper/jet_gram_quantum_note.md`.

Grep check after the edit found no remaining `matrix story remains unresolved`,
`## Missing`, or live `UV-`/`rem:wip` marker in the active note and UV ledger.
The remaining post-prune work is an independent hardening read focused on stale
scope language, proof-state consistency, and whether any precise new UV should
be filed rather than treating this as closed.
