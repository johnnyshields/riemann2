# gap-Or-veronese-theorem

- **Claim**: For the real Veronese curve
  \[
  v_n(t)=(1,t,\dots,t^n)^T,\qquad \psi_n(t)=\frac{v_n(t)}{\sqrt{D_n(t)}},\qquad D_n(t)=\sum_{k=0}^n t^{2k},
  \]
  the strongest exact value-channel-free theorem in the current scope is indeed for **order \(n-1\) only**. Let
  \[
  O_{n-1}(t)=\operatorname{span}\{j_1(t),\dots,j_{n-1}(t)\},\qquad j_k=(I-\psi_n\psi_n^T)\partial_t^k\psi_n .
  \]
  Define
  \[
  N_n(t)=\bigl((-t)^n,\binom n1(-t)^{n-1},\dots,\binom nk(-t)^{n-k},\dots,1\bigr)^T,
  \]
  the coefficient vector of \((x-t)^n\), and
  \[
  B_n(t)=\sum_{k=0}^n \binom nk^2 t^{2k},\qquad \nu_n(t)=\frac{N_n(t)}{\sqrt{B_n(t)}}.
  \]
  Then
  \[
  A_{n-1}(t)=\operatorname{span}\{\psi_n,\partial_t\psi_n,\dots,\partial_t^{\,n-1}\psi_n\}=N_n(t)^\perp,
  \]
  and since \(A_{n-1}(t)=\operatorname{span}\{\psi_n(t)\}\oplus O_{n-1}(t)\) with \(\psi_n(t)\perp N_n(t)\), one gets the exact codimension-\(2\) description
  \[
  O_{n-1}(t)=\psi_n(t)^\perp\cap N_n(t)^\perp,
  \qquad
  O_{n-1}(t)^\perp=\operatorname{span}\{\psi_n(t),\nu_n(t)\}.
  \]
  Therefore all nontrivial principal-angle data of \(O_{n-1}(u)\) versus \(O_{n-1}(v)\) are exactly the singular values of the explicit \(2\times2\) complement matrix
  \[
  M_n(u,v)=
  \begin{pmatrix}
  \dfrac{\sum_{k=0}^n (uv)^k}{\sqrt{D_n(u)D_n(v)}} &
  \dfrac{(u-v)^n}{\sqrt{D_n(u)B_n(v)}}\\[1.2ex]
  \dfrac{(v-u)^n}{\sqrt{B_n(u)D_n(v)}} &
  \dfrac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}}
  \end{pmatrix}.
  \]
  For \(n=2\) this recovers the qutrit \(O_1\) benchmark; for \(n=3\) it recovers the quartit \(O_2\) matrix. No equally clean exact closed formula is justified here for general lower orders \(r<n-1\).
- **Status**: proved
- **Evidence**: Proved: the note already establishes \(A_r=\operatorname{span}\{\psi\}\oplus O_r\), and the prior Veronese result proves \(A_{n-1}(t)=N_n(t)^\perp\). Proved: \(N_n(t)\cdot v_n(s)=(s-t)^n\), so in particular \(N_n(t)\cdot v_n(t)=0\), hence \(N_n(t)\perp \psi_n(t)\). Combining these gives \(O_{n-1}(t)=A_{n-1}(t)\cap \psi_n(t)^\perp=\psi_n(t)^\perp\cap N_n(t)^\perp\), so \(O_{n-1}(t)^\perp=\operatorname{span}\{\psi_n(t),\nu_n(t)\}\). Proved: \(\{\psi_n(t),\nu_n(t)\}\) is orthonormal, and the four cross-inner-products are explicit:
  \[
  \langle \psi_n(u),\psi_n(v)\rangle=\frac{\sum_{k=0}^n (uv)^k}{\sqrt{D_n(u)D_n(v)}},
  \]
  \[
  \langle \psi_n(u),\nu_n(v)\rangle=\frac{(u-v)^n}{\sqrt{D_n(u)B_n(v)}},
  \]
  \[
  \langle \nu_n(u),\psi_n(v)\rangle=\frac{(v-u)^n}{\sqrt{B_n(u)D_n(v)}},
  \]
  \[
  \langle \nu_n(u),\nu_n(v)\rangle=\frac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}}.
  \]
  Hence \(M_n(u,v)\) is an exact orthonormal-basis representative for the complement-plane comparison. Proved: for \(n=3\), where \(\dim O_2=2=\dim O_2^\perp\), its singular values are exactly the two \(O_2\) principal-angle cosines already recorded. Proved: for \(n=2\), the same construction reduces to the qutrit \(O_1\) benchmark, with one nontrivial line-angle recovered from the \(2\times2\) complement comparison. Conditional: the theorem is exact at the subspace/principal-angle level in the fixed ambient \(\mathbb R^{n+1}\); it is not a transport-independent higher-jet matrix theorem. Missing: a comparably sharp all-\(n\) closed-form diagonalization of \(M_n(u,v)\), and any general lower-order \(O_r\) theorem for \(r<n-1\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:316-355`; `quantum/paper/jet_gram_quantum_note.md:436-456`; `quantum/findings.md:54-80`; `quantum/findings.md:136-140`; `quantum/teams/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md:3-43`; `quantum/teams/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:25-65`; `quantum/teams/20260423-192859-attack-Or-veronese/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Elementary finite-dimensional principal-angle theory; the exact decomposition \(A_r=\operatorname{span}\{\psi\}\oplus O_r\); the order-\(n-1\) Veronese hyperplane theorem \(A_{n-1}(t)=N_n(t)^\perp\); the identity \(N_n(t)\cdot v_n(s)=(s-t)^n\); fixed common ambient comparison inside \(\mathbb R^{n+1}\).
- **Strongest objection**: The theorem is clean because order \(n-1\) is the codimension-\(2\) value-channel-free case sitting inside the codimension-\(1\) Veronese osculating hyperplane. That does not automatically yield a simpler closed-form singular-value formula for all \(n\), and it does not extend by the same argument to general lower orders \(r<n-1\) or to any canonical higher-jet matrix invariant.
- **Needed for promotion**: Promote only the narrow theorem: for the Veronese family, the exact value-channel-free statement is the order-\(n-1\) codimension-\(2\) complement-plane formula above. State explicitly that this is the strongest exact theorem currently justified, that it recovers qutrit \(O_1\) and quartit \(O_2\), and that no equally clean general theorem is yet proved for lower orders \(r<n-1\).
