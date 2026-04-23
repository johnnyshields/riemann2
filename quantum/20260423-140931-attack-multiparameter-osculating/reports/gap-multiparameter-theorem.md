# gap-multiparameter-theorem

- **Claim**: Let \(M\) be a \(C^r\) parameter manifold, \(x\in M\), and \([\psi]:M\to \mathbb P(\mathcal H)\) a \(C^r\) pure-state ray field in a fixed ambient Hilbert space \(\mathcal H\). For any normalized local lift \(\psi\) on a chart \(\lambda=(\lambda^1,\dots,\lambda^d)\), define for each multi-index \(\alpha\) with \(1\le |\alpha|\le r\)
  \[
  \partial^\alpha_\lambda \psi,
  \qquad
  P=I-|\psi\rangle\langle\psi|,
  \qquad
  j_\alpha:=P\,\partial^\alpha_\lambda\psi,
  \]
  and
  \[
  \mathcal A_r(x):=\operatorname{span}\{\psi(x),\partial^\alpha_\lambda\psi(x):1\le |\alpha|\le r\}
  =\operatorname{span}\{\psi(x),j_\alpha(x):1\le |\alpha|\le r\}.
  \]
  Then \(\mathcal A_r(x)\) is exactly independent of the chosen local phase gauge and of the chosen local chart. Equivalently, the horizontal osculating subspace
  \[
  O_r(x):=\operatorname{span}\{j_\alpha(x):1\le |\alpha|\le r\}
  \]
  is also gauge- and chart-invariant. Consequently, for two points \(x_\pm\in M\) in the same ambient \(\mathcal H\), the principal angles between \(\mathcal A_r(x_-)\) and \(\mathcal A_r(x_+)\) are canonical transport-free two-point invariants. No corresponding canonical matrix built from an ordered list of multiparameter partial jets is proved.
- **Status**: proved
- **Evidence**: Proved: under a local phase change \(\tilde\psi=e^{i\chi}\psi\), multivariate Leibniz gives \(\partial^\alpha\tilde\psi=e^{i\chi}\partial^\alpha\psi+\sum_{|\beta|<|\alpha|}c_{\alpha\beta}\partial^\beta\psi\). So the ordered derivative jets up to order \(r\) transform by an invertible block-upper-triangular law, hence their span is unchanged; after applying \(P\), the same conclusion holds for the projected jets \(j_\alpha\). Proved: under a chart change \(\mu=\mu(\lambda)\) with invertible Jacobian at \(x\), multivariate chain rule / Faà di Bruno gives each \(\partial^\beta_\mu\psi\) as a linear combination of \(\partial^\alpha_\lambda\psi\) with \(1\le |\alpha|\le |\beta|\), and the top-order block is the invertible symmetric-power action of the Jacobian, so the span of all derivatives of order \(\le r\) is unchanged; again \(P\) preserves the corresponding statement for \(j_\alpha\). Proved: since \(j_\alpha=\partial^\alpha\psi-\psi\langle\psi,\partial^\alpha\psi\rangle\), one has \(\mathcal A_r=\operatorname{span}\{\psi,j_\alpha\}=\operatorname{span}\{\psi,\partial^\alpha\psi\}\). Conditional: if one chooses bases or whitening conventions inside these subspaces, one gets matrices whose entries depend on the non-scalar block-upper-triangular gauge/chart action; only subspace data, not raw matrix entries, is canonical. Missing: no exact multiparameter analogue of the one-parameter first-horizontal-jet whitened-matrix theorem is proved.
- **Exact refs**: `quantum/20260423-140931-attack-multiparameter-osculating/notes/coordinator-brief.md:3-14`; `quantum/paper/jet_gram_quantum_note.md:174-247`; `quantum/findings.md:46-58`; `quantum/20260423-140111-attack-transport-free-subspaces/reports/gap-transport-free-subspaces.md:3-23`.
- **Dependencies**: A fixed ambient Hilbert space \(\mathcal H\); a \(C^r\) pure-state ray field on a \(C^r\) parameter manifold; normalized local lifts; multivariate Leibniz rule for phase gauge; multivariate chain rule / Faà di Bruno for chart changes; invertibility of the chart Jacobian; standard principal-angle theory for finite-dimensional subspaces of \(\mathcal H\).
- **Strongest objection**: This theorem is exact only at the subspace level. In several parameters the ordered partial-jet array mixes across multi-indices of the same and lower total order under chart change, and gauge change adds lower-order terms as well; that destroys any claim that a raw multiparameter Gram block or bilaterally whitened matrix is chart/gauge invariant entrywise. Also, the transport-free principal-angle statement requires both endpoint subspaces to sit in the same ambient \(\mathcal H\).
- **Needed for promotion**: Promote only the ambient-subspace theorem: the order-\(r\) span of all mixed partial derivatives up to total order \(r\) is a well-defined ray-space object on a fixed ambient Hilbert space, and its endpoint principal angles are canonical transport-free invariants. Do not promote any stronger multiparameter matrix-valued claim without a separate covariant frame/transport theorem.
