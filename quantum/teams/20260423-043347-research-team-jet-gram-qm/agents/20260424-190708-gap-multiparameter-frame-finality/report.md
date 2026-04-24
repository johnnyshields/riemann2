**Claim**

UV-011 can close negatively from the present hypotheses. For a \(C^r\)
pure-state ray field \([\psi]:M\to \mathbb P(\mathcal H)\) in a fixed ambient
Hilbert space, the multiparameter raw, projected, Berry-covariant, and
symmetrized jet constructions determine the canonical filtered subspaces
\[
O_r(x)=\operatorname{span}\{P_x\partial^\alpha\psi(x):1\le |\alpha|\le r\}
\]
and
\[
A_r(x)=\operatorname{span}\{\psi(x)\}\oplus O_r(x),
\]
but they do not determine a canonical ordered frame or entrywise comparison
matrix from the ray-field/subspace data alone. At two endpoints \(x_-,x_+\),
the exact surviving basis-free package consists of the endpoint subspaces
\(O_r(x_\pm)\) and \(A_r(x_\pm)\), their orthogonal projectors, the
cross-contractions \(C_O=\Pi_{O,-}|_{O_+}\) and
\(C_A=\Pi_{A,-}|_{A_+}\), the positive compressions \(C_O^*C_O,C_OC_O^*\) and
\(C_A^*C_A,C_AC_A^*\), the polar partial isometries on the nonzero-overlap
sectors, and the corresponding principal-angle spectra. Any orthonormal-frame
matrix for these data is only defined up to the biunitary orbit of the promoted
UV-012 theorem.

This no-go is scoped to data determined by the ray field and the canonical
subspace hierarchy alone. It does not rule out matrices after adding a metric,
preferred coordinates, a source connection, a dynamical law, an experimental
protocol, symmetry breaking, or another explicit frame-selecting convention.

**Status**

proved

**Evidence**

Proved. Raw mixed partials and projected raw jets are not ordered canonical
arrays. Under phase gauge, multivariate Leibniz changes order-\(k\) derivatives
by the original order-\(k\) derivative plus lower-order derivatives. Under a
chart change, the multivariate chain rule changes the top order by the
symmetric-power Jacobian action and adds lower-order terms. Thus the full
order-\(\le r\) span is invariant, while the ordered coordinate list and any
Gram or whitened matrix built entrywise from that list is not invariant under
the non-unitary block-upper-triangular coordinate law.

Proved. The Berry-covariant multiparameter hierarchy repairs gauge covariance
of the generators but not frame canonicity. The ordered covariant jets
\(\nabla_{a_k}\cdots\nabla_{a_1}\psi\) are gauge-covariant and generate the
same \(O_r\) filtration as the projected raw mixed partials. The symmetrized-jet
report proves that changing the order of covariant derivatives only changes
the result by lower-filtration terms, so symmetrized covariant jets generate
the same subspace filtration. This is a canonical generator theorem for
subspaces, not a rule selecting a basis of those subspaces.

Proved. Once the endpoint data has been reduced to \(O_r(x_\pm)\) or
\(A_r(x_\pm)\), the promoted UV-012 theorem applies. If \(S_-,S_+\) denotes
either endpoint pair and \(U_\pm\) are orthonormal frame isometries, then
\[
A=U_-^*U_+
\]
is a frame matrix for the canonical cross-contraction
\(C=\Pi_-|_{S_+}:S_+\to S_-\). All changes of endpoint orthonormal frames act
as \(A\mapsto L^*AR\), and every such frame matrix arises this way. Rectangular
SVD classifies this orbit by singular values, which are the principal-angle
cosines. Therefore an entrywise matrix is not selected by the ray-field
subspace data alone; only the orbit, or an SVD normal form encoding the same
singular values, is canonical.

Conditional. If extra structure selects coordinates or frames, it can produce
matrices. Examples include fixed parameter coordinates, a chosen source
connection/metric, a dynamical or transport law, a laboratory protocol, or a
simple nonzero principal spectrum giving matched principal directions up to
phase/sign on that sector. These are additional hypotheses, not consequences
of the multiparameter ray-field hierarchy alone.

Conditional. There is a nearby positive basis-free tensor story, but it is not
an ordered matrix/frame package. Without extra source connection, the full
order-\(k\) derivative is not a tensor because chart changes add lower-order
terms. What is intrinsic from the jet filtration is the associated-graded
principal-symbol class, equivalently a map from \(\operatorname{Sym}^kT_xM\)
into the quotient \(O_k(x)/O_{k-1}(x)\) or \(A_k(x)/A_{k-1}(x)\). With an
explicit source connection one may instead form a tensor-valued symmetrized
covariant derivative in a horizontal bundle. Either object is basis-free
tensor/filter data; neither selects an ordered frame of \(O_r\) nor an
entrywise endpoint comparison matrix.

Missing. No residual mathematical substatement remains for the negative
UV-011 closure under the stated scope. The only promotion requirement is an
adversarial check that the note's wording says "from the ray-field/subspace
data alone" and does not exclude extra-structure matrix constructions.

No scripts were needed; the argument is formal differential geometry plus
finite-dimensional linear algebra from the cited deposited reports.

**Baseline / delta**

Baseline: the current paper already states that multiparameter covariant jets
span the same \(O_r\) spaces as raw mixed partial jets, that symmetrized
covariant jets generate the same filtration, and that the multiparameter
extension is safe at the subspace/principal-angle level while the matrix story
was unresolved. UV-012 has since promoted the biunitary-orbit finality theorem
for fixed endpoint subspace pairs.

Delta: this report combines those facts into the missing UV-011 finality
statement. The covariant-jet hierarchy supplies canonical filtered subspaces
and the corresponding projector/cross-contraction/polar/principal-angle
operator package. It does not supply a canonical ordered multiparameter
matrix/frame package unless extra frame-selecting structure is added. The
possible tensor-valued or associated-graded jet object is classified as a
different basis-free object, not a matrix/frame closure.

**Attempt status**

terminal

**Exact refs**

- `quantum/paper/jet_gram_quantum_note.md:280-299` for the
  multiparameter covariant and symmetrized jet hierarchy and the existing
  statement that the missing issue is the matrix/frame package.
- `quantum/paper/jet_gram_quantum_note.md:398-403` for the multiparameter
  ambient-subspace theorem.
- `quantum/paper/jet_gram_quantum_note.md:405-437` for projector
  compressions, cross-contractions, polar partial isometry, and the promoted
  biunitary matrix-finality paragraph.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md` for
  the current confirmed multiparameter hierarchy, operator package, and
  remaining UV-011 missing item.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md` for UV-011,
  `quantum-open-multiparameter-matrix-frame`.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/dispatch.md` for
  the UV-011 ground-truth check and non-goals.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/attempts.md` for
  the prior no-deposit handle and the current replacement target.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md` for
  the UV-012 promotion and the remaining matrix-story frontier.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/notes/resume-readthrough-20260424.md`
  for the reconstructed frontier.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-140931-attack-multiparameter-osculating/reports/gap-multiparameter-theorem.md`
  and
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-140931-attack-multiparameter-osculating/reports/verifier-adversarial.md`
  for the multiparameter subspace theorem and verifier.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-235606-attack-multiparameter-covariant-jets/reports/gap-multiparameter-covariant-jets.md`
  for the gauge-covariant hierarchy.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-010555-attack-symmetrized-jets/reports/gap-symmetrized-jets.md`
  for the symmetrized-span theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-134344-attack-higher-jets/reports/gap-higher-jet-theorem.md`
  for the one-parameter upper-triangular failure mode and subspace repair.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-gap-biunitary-matrix-finality/report.md`
  and
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-verifier-biunitary-finality/report.md`
  for the promoted UV-012 orbit theorem and adversarial verification.

**Dependencies**

Fixed ambient Hilbert space; finite-dimensional endpoint jet subspaces or
closed finite-rank truncations; \(C^r\) ray field; normalized local lifts;
phase-gauge covariance; chart changes with invertible Jacobian; inclusion of
all mixed partials of total order at most \(r\); Berry-covariant derivative
and symmetrized covariant-jet span theorem; standard orthogonal projectors,
principal angles, polar decomposition, and rectangular SVD.

**Strongest objection**

The negative statement depends on the phrase "from the ray-field/subspace data
alone." It does not prove that no useful matrix can exist after adding a source
metric, connection, coordinate convention, physical dynamics, measurement
protocol, or symmetry-breaking rule. It also does not reject an associated-
graded tensor-valued jet object. The point is narrower: none of those extra
choices is supplied by the canonical multiparameter covariant-jet hierarchy
itself, and after reduction to endpoint subspaces UV-012 leaves only a
biunitary orbit of frame matrices.

**Needed for promotion**

Run an adversarial verifier against the wording. If accepted, promote a short
negative theorem after the multiparameter matrix-finality discussion:

> For a multiparameter \(C^r\) ray field in a fixed ambient Hilbert space, the
> raw, projected, Berry-covariant, and symmetrized jet constructions determine
> the canonical filtrations \(O_r\) and \(A_r\), hence the endpoint projectors,
> cross-contractions, polar partial isometries, and principal-angle spectra.
> They do not determine an ordered frame or entrywise comparison matrix from
> the ray-field data alone. Raw coordinate arrays transform by non-unitary
> block-upper-triangular gauge/chart laws; covariant and symmetrized jets repair
> the generated filtration but do not choose bases. Once the data is reduced to
> endpoint subspaces, every orthonormal-frame comparison matrix belongs to the
> UV-012 biunitary orbit classified by principal-angle singular values.

Add a separate sentence that tensor-valued or associated-graded jet symbols may
be useful basis-free objects under their own hypotheses, but they are not the
ordered matrix/frame package asked for in UV-011.

**Autoresearch next step**

verify: send this negative UV-011 closure to an adversarial verifier before
removing UV-011 or editing the note. The verifier should test the scope of
"from ray-field/subspace data alone," the tensor-object caveat, and whether the
UV-012 theorem is being applied only after endpoint reduction to \(O_r\) or
\(A_r\).
