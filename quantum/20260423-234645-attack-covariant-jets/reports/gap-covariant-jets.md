# gap-covariant-jets

- **Claim**: For a one-parameter normalized local lift \(t\mapsto |\psi(t)\rangle\), there is an exact higher-order gauge-covariant jet hierarchy with the same osculating subspaces as the raw projected jets. Let
  \[
  a(t):=\langle\psi(t),\partial_t\psi(t)\rangle,
  \qquad
  P_t:=I-|\psi(t)\rangle\langle\psi(t)|,
  \]
  and define the covariant derivative on vector fields along the curve by
  \[
  \nabla_t\xi:=P_t\bigl(\partial_t\xi-a(t)\xi\bigr).
  \]
  If \(\xi\) transforms covariantly under phase gauge, \(\xi\mapsto e^{i\chi(t)}\xi\), then so does \(\nabla_t\xi\). Define recursively
  \[
  h_{[1]}:=\nabla_t\psi=j_1,
  \qquad
  h_{[k+1]}:=\nabla_t h_{[k]}.
  \]
  Then each \(h_{[k]}\in \psi(t)^\perp\) is gauge-covariant, and for every \(r\ge1\)
  \[
  \operatorname{span}\{h_{[1]},\dots,h_{[r]}\}=O_r(t)=\operatorname{span}\{j_1(t),\dots,j_r(t)\},
  \qquad
  j_k=P_t\partial_t^k\psi.
  \]
  More precisely, each \(h_{[k]}\) is an upper-triangular combination of the raw projected jets:
  \[
  h_{[k]}=j_k+\sum_{m<k} b_{km}(t)j_m.
  \]
- **Status**: proved
- **Evidence**: Proved: under \(|\psi\rangle\mapsto e^{i\chi}|\psi\rangle\), one has \(a\mapsto a+i\chi'\), \(P_t\mapsto P_t\), and therefore
  \[
  \nabla_t(e^{i\chi}\xi)=e^{i\chi}\nabla_t\xi.
  \]
  So the hierarchy is exactly gauge-covariant. Proved: for \(j_m=P_t\partial_t^m\psi\), one computes
  \[
  \nabla_t j_m=P_t\partial_t(P_t\partial_t^m\psi)-a j_m
  =j_{m+1}-\langle\psi,\partial_t^m\psi\rangle j_1-a j_m,
  \]
  where the only nontrivial term from \(\partial_tP_t\) contributes along \(j_1\). Hence \(\nabla_t j_m\) lies in
  \(\operatorname{span}\{j_1,j_m,j_{m+1}\}\), so the map is upper-triangular on the raw jet filtration. Starting with \(h_{[1]}=j_1\), induction gives
  \(h_{[k]}=j_k+\sum_{m<k}b_{km}j_m\), proving equality of spans at every order.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:196-246`; `quantum/findings.md:50-58,158-166`; `quantum/20260423-234645-attack-covariant-jets/notes/coordinator-brief.md:3-12`.
- **Dependencies**: One-parameter normalized local lift; the Berry connection scalar \(a(t)=\langle\psi,\partial_t\psi\rangle\); the projected raw jets \(j_k=P_t\partial_t^k\psi\); projector calculus for \(\partial_tP_t\).
- **Strongest objection**: This theorem is one-parameter only. In several parameters, ordering and mixed derivatives introduce additional choices, so this does not yet provide the full multiparameter higher-order covariant hierarchy one would ultimately want.
- **Needed for promotion**: Add it to the note as the one-parameter higher-order covariant-jet theorem. Narrow the open problem from “find any higher-order covariant hierarchy” to “extend this one-parameter hierarchy to a satisfactory multiparameter version.”
