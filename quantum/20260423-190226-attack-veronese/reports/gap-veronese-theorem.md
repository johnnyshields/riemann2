# gap-veronese-theorem

- **Claim**: For the real Veronese curve
  \[
  v_n(t)=(1,t,\dots,t^n)^T\in \mathbb R^{n+1},
  \qquad
  \psi_n(t)=\frac{v_n(t)}{\|v_n(t)\|},
  \]
  the clean general family theorem is at **order \(n-1\)** for the ambient osculating subspaces
  \[
  A_{n-1}(t)=\operatorname{span}\{\psi_n(t),\partial_t\psi_n(t),\dots,\partial_t^{\,n-1}\psi_n(t)\}
  =\operatorname{span}\{v_n(t),v_n'(t),\dots,v_n^{(n-1)}(t)\}.
  \]
  These are codimension-\(1\) hyperplanes with exact normal
  \[
  N_n(t)=\bigl((-t)^n,\binom n1(-t)^{n-1},\dots,\binom nk(-t)^{\,n-k},\dots,1\bigr)^T,
  \]
  equivalently the coefficient vector of \((x-t)^n\). Hence
  \[
  A_{n-1}(t)=N_n(t)^\perp.
  \]
  Therefore for endpoints \(u,v\), the principal-angle cosines between \(A_{n-1}(u)\) and \(A_{n-1}(v)\), equivalently the singular values of any bilaterally whitened cross-Gram representative built from endpoint bases of these subspaces in the common ambient \(\mathbb R^{n+1}\), are
  \[
  \underbrace{1,\dots,1}_{n-1\text{ times}},\qquad
  \sigma_n(u,v)=\frac{\left|\sum_{k=0}^n \binom nk^2 (uv)^k\right|}
  {\sqrt{\left(\sum_{k=0}^n \binom nk^2 u^{2k}\right)
  \left(\sum_{k=0}^n \binom nk^2 v^{2k}\right)}}.
  \]
  This recovers the qutrit case \(n=2\) and quartit case \(n=3\). The strongest exact Veronese-family statement in the present scope is this **ambient order-\(n-1\) subspace/principal-angle theorem**; not a transport-free matrix theorem, and not yet a general theorem for lower orders \(r<n-1\).
- **Status**: proved
- **Evidence**: Proved: \(A_{n-1}(t)=\operatorname{span}\{v_n,\dots,v_n^{(n-1)}\}\) because \(\psi_n=\|v_n\|^{-1}v_n\), so \((\psi_n,\partial_t\psi_n,\dots,\partial_t^{\,n-1}\psi_n)\) is obtained from \((v_n,v_n',\dots,v_n^{(n-1)})\) by an invertible lower-triangular same-point change of basis, exactly as in the quartit benchmark. Proved: \(N_n(t)\cdot v_n(s)=(s-t)^n\). Differentiating in \(s\) gives \(N_n(t)\cdot v_n^{(j)}(t)=0\) for \(0\le j\le n-1\). Since those \(n\) vectors are linearly independent, their span is the codimension-\(1\) hyperplane \(N_n(t)^\perp\). Proved: for codimension-\(1\) hyperplanes in \(\mathbb R^{n+1}\), the principal-angle cosines are \(1,\dots,1\) and the cosine between unit normals. Here
  \[
  N_n(u)\cdot N_n(v)=\sum_{k=0}^n \binom nk^2 (uv)^{n-k}
  \]
  which is the same polynomial as \(\sum_{k=0}^n \binom nk^2 (uv)^k\) after reindexing, and similarly
  \[
  \|N_n(t)\|^2=\sum_{k=0}^n \binom nk^2 t^{2k}.
  \]
  So the displayed \(\sigma_n(u,v)\) follows. Proved: \(n=2\) gives \(N_2(t)=(t^2,-2t,1)\) and recovers the qutrit benchmark formula. Proved: \(n=3\) gives \(N_3(t)=(-t^3,3t^2,-3t,1)\) and recovers the quartit benchmark formula. Conditional: this singular-value interpretation is the quantum-side output only in the fixed ambient / identity or scalar-phase setting where endpoint subspaces are compared inside the same \(\mathbb R^{n+1}\). Missing: any canonical higher-jet matrix representative or equally clean closed formula for general lower-order \(O_r\) or \(A_r\) with \(r<n-1\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:318-340`; `quantum/paper/jet_gram_quantum_note.md:382-404`; `quantum/paper/jet_gram_quantum_note.md:501-545`; `quantum/findings.md:53-64`; `quantum/findings.md:115-131`; `quantum/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`; `quantum/20260423-135052-attack-quartit-osculating/reports/gap-quartit-principal-angles.md:3-43`; `quantum/20260423-190226-attack-veronese/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Elementary linear algebra of osculating spaces and principal angles; invertible lower-triangular change from normalized derivatives to raw polynomial derivatives; the codimension-\(1\) hyperplane fact for order \(n-1\) Veronese osculation; fixed common ambient \(\mathbb R^{n+1}\) for endpoint comparison.
- **Strongest objection**: The theorem is clean precisely because order \(n-1\) gives a codimension-\(1\) ambient osculating hyperplane, so everything collapses to one normal vector. That does not by itself produce a general theorem for lower orders \(r<n-1\), for value-channel-free \(O_r\), or for transport-independent matrix entries.
- **Needed for promotion**: State it narrowly as the order-\(n-1\) ambient Veronese theorem. Include the explicit normal \(N_n(t)\), the identity \(N_n(t)\cdot v_n(s)=(s-t)^n\), and the resulting singular-value formula. Do not promote any stronger claim about canonical higher-jet matrices or about all lower orders \(r\).
