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
