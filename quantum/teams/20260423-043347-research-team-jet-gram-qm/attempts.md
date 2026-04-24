# Attempts

| Agent | Target | Claim / route | Status | Evidence | Action | Description |
|---|---|---|---|---|---|---|
| `20260424-183451-gap-biunitary-matrix-finality` | UV-012 | Prove fixed-subspace frame comparison matrices are exactly one biunitary orbit; singular values/principal angles are complete orbit data. | terminal | `agents/20260424-183451-gap-biunitary-matrix-finality/report.md` proves the frame-change law and rectangular SVD orbit classification; no scripts needed. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-012 removed from `uv.md`. | This is the focused matrix-finality route selected after the deep read. |
| `20260424-183451-verifier-biunitary-finality` | UV-012 | Adversarially test the matrix-finality theorem, especially rectangular zeros, normal-form wording, and simple/repeated-spectrum exceptions. | terminal | `agents/20260424-183451-verifier-biunitary-finality/report.md` accepts the theorem for promotion, scoped to orthonormal-frame comparison matrices from the fixed subspace pair alone. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-012 removed from `uv.md`. | This is the verifier pass required before changing UV-012 proof state. |
| `20260424-184452-gap-multiparameter-frame-finality` | UV-011 | Use the promoted UV-012 matrix-finality theorem plus multiparameter covariant-jet reports to decide whether any natural ordered matrix/frame package survives beyond subspace data. | crash | Agent handle stayed at `pending_init` and left no report. | Replaced by `20260424-190708-gap-multiparameter-frame-finality`. | No provenance beyond dispatch; do not cite as evidence. |
| `20260424-190708-gap-multiparameter-frame-finality` | UV-011 | Same UV-011 target: decide positive extra-structure theorem versus negative frame-selection obstruction for multiparameter covariant jets. | terminal | `agents/20260424-190708-gap-multiparameter-frame-finality/report.md` gives a scoped negative closure: multiparameter jets determine filtered subspaces and the operator/principal-angle package, but not ordered frames or entrywise matrices from ray-field/subspace data alone. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-011 removed from `uv.md`. | This is the adjacent matrix-story continuation after UV-012. |
| `20260424-191018-verifier-multiparameter-frame-finality` | UV-011 | Adversarially test the scoped no-go for multiparameter ordered frames/matrices and the associated-graded tensor caveat. | terminal | `agents/20260424-191018-verifier-multiparameter-frame-finality/report.md` accepts the no-go for promotion with scope caveats around extra structure and tensor-valued objects. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-011 removed from `uv.md`. | Verification required before changing UV-011 proof state. |
| `20260424-191454-gap-Ar-Or-role-split` | UV-013 | Decide whether `O_r` versus `A_r` has a role criterion or only a no-global-winner theorem. | terminal | `agents/20260424-191454-gap-Ar-Or-role-split/report.md` gives a role criterion: `O_r` for horizontal/value-channel-removed geometry, `A_r` for ambient state-line endpoint packages; no global winner is forced. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-013 removed from `uv.md`. | This is the next structural target after closing matrix/frame finality. |
| `20260424-191817-verifier-Ar-Or-role-split` | UV-013 | Adversarially test the `O_r`/`A_r` role criterion and no-global-winner theorem. | terminal | `agents/20260424-191817-verifier-Ar-Or-role-split/report.md` accepts promotion with caveats against state-line recovery and universal `O_r` dominance wording. | Promoted to `quantum/paper/jet_gram_quantum_note.md`; UV-013 removed from `uv.md`. | Verification required before changing UV-013 proof state. |
| `20260424-192133-gap-natural-protocol` | UV-014 | Test whether principal-angle/operator data has a natural two-projector/reflection measurement protocol beyond the thin yes/yes test, or only existing reformulations. | keep pending verification | `agents/20260424-192133-gap-natural-protocol/report.md` gives a positive two-reflection protocol: phase estimation on `(2Pi_- - I)(2Pi_+ - I)` returns phases `±2 theta_i` on principal two-planes. | Send to adversarial verifier before promotion or UV removal. | This is a coherent protocol for estimating existing principal-angle data, not a new invariant. |

## Frontier summaries

- **Current best:** The safe canonical core is the subspace/operator package:
  canonical endpoint subspaces, principal angles, projector compressions,
  cross-contraction, polar partial isometry, simple-spectrum frame corollary,
  repeated-spectrum no-go, finite-dimensional CS completeness, and the
  biunitary-orbit classification of all orthonormal-frame comparison matrices.
  In several parameters the raw/covariant/symmetrized jet hierarchies determine
  the `O_r`/`A_r` filtrations but no ordered matrix/frame from ray-field data
  alone.
- **Keep:** First-order QGT bridge; first-horizontal-jet reparameterization and
  singular-value theorem with transport caveats; higher-jet subspace theorem;
  multiparameter subspace/covariant/symmetrized hierarchy; Veronese and
  spherical-twist richer-than-overlap benchmarks; exact unitary/Krylov, Kato,
  and projector-leakage specializations.
- **Discard:** Any route claiming a canonical full matrix from raw higher jets
  under gauge/chart changes; any route treating oscillator singular values as
  richer-than-overlap; any route upgrading Kato transport to endpoint-canonical
  transport in nonzero curvature.
- **Blocked:** The prior
  `agents/20260424-040334-attack-biunitary-classification/` has only a
  coordinator brief and no deposited report. This has now been superseded by
  the deposited UV-012 gap and verifier reports.
- **Next:** Per user redirection on 2026-04-24, do not default to a 3+3+2
  roster. Attack UV-014 (natural protocol) next.
