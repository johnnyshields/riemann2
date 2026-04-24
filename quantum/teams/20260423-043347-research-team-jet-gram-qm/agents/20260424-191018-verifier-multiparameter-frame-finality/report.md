**Claim**

The primary UV-011 gap report is correct enough for promotion after wording
fixes. Under the present hypotheses, the multiparameter raw projected,
Berry-covariant, and symmetrized jet constructions determine canonical
filtrations \(O_r(x)\) and \(A_r(x)=\operatorname{span}\{\psi(x)\}\oplus O_r(x)\),
and hence the endpoint projector/cross-contraction/polar/principal-angle
operator package. They do not determine an ordered frame, ordered coordinate
array, entrywise Gram matrix, or whitened comparison matrix from the ray-field
and its canonical subspace hierarchy alone.

This is a scoped negative closure of UV-011, not a ban on all matrices under
extra structure. Extra coordinates, a source metric or connection, dynamics,
transport, a measurement protocol, symmetry breaking, or simple nonzero
principal spectrum may select representatives under additional hypotheses.
Associated-graded or tensor-valued jet symbols are also legitimate basis-free
objects, but they are not the ordered matrix/frame package asked for by UV-011.

**Status**

proved

**Evidence**

Proved. Raw mixed partial and projected-jet arrays are not canonical ordered
arrays. Under a phase change, the order-\(\le r\) projected jets transform by an
invertible block-upper-triangular law with lower-order contamination. Under a
chart change, the multivariate chain rule gives an invertible top-order
symmetric-power Jacobian action plus lower-order terms. These transformations
preserve the full filtered span, but they are not unitary frame changes of a
fixed ordered list. Therefore Gram blocks and bilaterally whitened matrices
built entrywise from such lists are not invariant objects unless extra
coordinate/frame data is retained.

Proved. The Berry-covariant hierarchy repairs gauge covariance of the generators
and gives a clean span theorem, but it does not choose a frame. The ordered
covariant words \(\nabla_{a_k}\cdots\nabla_{a_1}\psi\) are gauge-covariant and
generate the same \(O_r\) filtration as raw projected mixed partials. Their
indices still depend on chosen tangent coordinates or chosen tangent vectors,
and the hierarchy supplies no canonical ordering or orthonormal basis of the
resulting endpoint subspaces.

Proved. The symmetrized-jet theorem removes ordering dependence only modulo the
lower filtration and therefore only at the filtration/span level. It supports
the statement that the common symmetrized subspace data is canonical; it does
not produce an ordered basis of \(O_r\), an entrywise endpoint matrix, or a
canonical whitening convention.

Proved. The UV-012 theorem is being used only after endpoint data has been
reduced to canonical subspaces \(O_r(x_\pm)\) or \(A_r(x_\pm)\). At that point,
orthonormal-frame comparison matrices for the canonical cross-contraction form
one biunitary orbit \(A\mapsto L^*AR\), classified by principal-angle singular
values. This is exactly the correct finality statement for frame matrices from
the subspace pair alone.

Conditional. An associated-graded object is a different basis-free survivor,
not a closure of the ordered matrix/frame request. The intrinsic filtration can
support principal-symbol style maps into quotients such as
\(O_k/O_{k-1}\) or \(A_k/A_{k-1}\); with an explicit source connection one may
form tensor-valued covariant derivatives. These objects may deserve separate
development, but they do not select endpoint frames or entrywise comparison
matrices.

Missing. No residual mathematical substatement remains for UV-011 under the
scope "from the multiparameter ray-field/canonical subspace data alone." The
remaining work is wording: the promoted paragraph must preserve that scope and
must not imply that extra-structure matrix constructions or basis-free tensor
objects are impossible.

No scripts were needed; this verification is a formal check against the cited
jet-transformation, covariant-span, symmetrized-span, and finite-dimensional
linear-algebra reports.

**Baseline / delta**

Baseline: the current note already proves the multiparameter covariant and
symmetrized hierarchy at the subspace level, the multiparameter ambient
subspace theorem, the endpoint operator package, the simple-spectrum frame
corollary, the repeated-spectrum no-go, and the UV-012 biunitary-orbit theorem.
The open problem at `quantum/paper/jet_gram_quantum_note.md:804-808` asks
whether a multiparameter covariant-jet hierarchy supplies a canonical ordered
matrix/frame package beyond this subspace theorem.

Delta: I accept the gap report's negative closure, with a narrower promotion
boundary. The closure is not "no matrix can ever be natural"; it is "the present
multiparameter ray-field hierarchy canonically determines filtrations and the
operator/principal-angle package, and after that reduction any orthonormal-frame
comparison matrix is only a UV-012 biunitary-orbit representative unless extra
frame-selecting structure is added."

**Attempt status**

terminal

**Exact refs**

- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-190708-gap-multiparameter-frame-finality/report.md` for the primary UV-011 gap report under verification.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md` for the current confirmed multiparameter hierarchy, operator package, simple/repeated spectrum results, and remaining UV-011 missing item.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md` for UV-011, `quantum-open-multiparameter-matrix-frame`.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/attempts.md` for the current UV-011 gap report and this verifier assignment.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/dispatch.md` for the UV-011 ground-truth check and non-goals.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md` for the UV-012 promotion history and provisional keep verdict on UV-011.
- `quantum/paper/jet_gram_quantum_note.md:279-299` for the multiparameter Berry-covariant and symmetrized hierarchy statement and the matrix/frame gap.
- `quantum/paper/jet_gram_quantum_note.md:398-403` for the multiparameter ambient-subspace theorem.
- `quantum/paper/jet_gram_quantum_note.md:405-437` for endpoint projectors, cross-contractions, polar partial isometry, and the UV-012 biunitary-orbit theorem.
- `quantum/paper/jet_gram_quantum_note.md:439-465` for the simple-spectrum frame corollary and repeated-spectrum no-go.
- `quantum/paper/jet_gram_quantum_note.md:765-808` for safe claims, unsafe claims, and the open-problem list.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-140931-attack-multiparameter-osculating/reports/gap-multiparameter-theorem.md` and `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-140931-attack-multiparameter-osculating/reports/verifier-adversarial.md` for the multiparameter raw/projected subspace theorem and adversarial check.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-235606-attack-multiparameter-covariant-jets/reports/gap-multiparameter-covariant-jets.md` for the Berry-covariant hierarchy and span equality.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-010555-attack-symmetrized-jets/reports/gap-symmetrized-jets.md` for the symmetrized-span theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-134344-attack-higher-jets/reports/gap-higher-jet-theorem.md` for the one-parameter raw higher-jet triangular transformation pattern.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-gap-biunitary-matrix-finality/report.md` and `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-verifier-biunitary-finality/report.md` for the UV-012 orbit theorem and verification.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-024917-attack-frame-criterion/reports/gap-frame-criterion.md` and `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-023315-attack-degenerate-nogo/reports/gap-degenerate-nogo.md` for the sharp simple-spectrum exception and repeated-spectrum no-go.

**Dependencies**

Fixed ambient Hilbert space; \(C^r\) pure-state ray field; normalized local
lifts; local phase gauges; chart changes with invertible Jacobian; inclusion of
all mixed partials of total order at most \(r\); projected raw jets; the
Berry-covariant derivative and its span theorem; the symmetrized covariant-jet
span theorem; finite-dimensional or finite-rank endpoint subspaces; orthogonal
projectors; principal angles; polar decomposition; rectangular SVD; and the
unitary-equivariant meaning of "canonical from the ray-field/subspace data
alone."

**Strongest objection**

The word "canonical" can hide extra hypotheses. A source metric could identify
preferred tangent frames in special geometries; a connection or dynamics could
define transport; a laboratory protocol could prescribe coordinates; and simple
nonzero principal spectrum already gives matched principal directions up to
phase/sign on that sector. Those are not counterexamples to the negative
UV-011 closure, because they add frame-selecting structure beyond the
multiparameter ray field and its canonical \(O_r,A_r\) filtrations. Promotion
must keep this distinction explicit.

**Needed for promotion**

Promote a short negative theorem with wording close to:

> For a multiparameter \(C^r\) pure-state ray field in a fixed ambient Hilbert
> space, the raw projected, Berry-covariant, and symmetrized jet constructions
> determine the canonical filtrations \(O_r\) and \(A_r\). Hence at two endpoints
> they determine the orthogonal projectors, cross-contractions, polar partial
> isometries on nonzero-overlap sectors, and principal-angle spectra. They do
> not determine an ordered frame, ordered coordinate array, entrywise Gram
> matrix, or whitened comparison matrix from the ray-field/subspace data alone.
> Raw coordinate arrays transform by block-upper-triangular gauge/chart laws;
> covariant and symmetrized jets repair gauge covariance and the generated
> filtration, but do not select bases. After reduction to endpoint subspaces,
> every orthonormal-frame comparison matrix is a representative of the UV-012
> biunitary orbit classified by the principal-angle singular values.

Add a caveat immediately after it:

> This does not exclude matrices after adding explicit frame-selecting
> structure, nor does it exclude associated-graded or tensor-valued jet symbols
> as separate basis-free objects. The simple nonzero-spectrum sector gives only
> the already-stated conditional principal-frame normal form, up to phase/sign.

Avoid these wordings:

- "No multiparameter matrix can be canonical" without "from the ray-field and
  canonical subspace data alone."
- "Berry-covariant jets give a canonical ordered frame."
- "Symmetrization removes ordering dependence" without "at the filtration/span
  level."
- "The associated-graded tensor closes UV-011" unless UV-011 is explicitly
  reframed away from ordered frames/matrices.
- "UV-012 rules out matrices before endpoint reduction to \(O_r\) or \(A_r\)."
- "Simple spectrum gives a canonical full matrix package" without the nonzero
  sector and phase/sign qualifications.

Honest verdict: accept the gap report for promotion after these wording fixes;
UV-011 need not remain open unless the coordinator wants to broaden it to
extra-structure or tensor-valued constructions.

**Autoresearch next step**

terminal: UV-011 is negatively closed under the stated scope after promotion
wording is tightened as above.
