# gap-Or-richness

- **Claim**: For the real Veronese family at order \(n-1\), the value-channel-free two-point data is generically not determined by endpoint overlap alone for every \(n\ge 2\). More precisely, let \(M_n(u,v)\) be the explicit \(2\times2\) complement matrix for \(O_{n-1}(u),O_{n-1}(v)\) from the deposited `O_{n-1}` Veronese theorem. Then
  \[
  \det M_n(u,v)=\frac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}}=c_n(u,v),
  \]
  where \(c_n\) is exactly the nontrivial ambient \(A_{n-1}\) principal-angle cosine. Since \(c_n\) is generically not a function of overlap alone for all \(n\ge2\), the full `O_{n-1}` principal-angle data is also generically not determined by overlap alone for all \(n\ge2\).
- **Status**: proved
- **Evidence**: Proved in the deposited `O_{n-1}` Veronese theorem: the complement matrix is
  \[
  M_n(u,v)=
  \begin{pmatrix}
  \dfrac{\sum_{k=0}^n (uv)^k}{\sqrt{D_n(u)D_n(v)}} &
  \dfrac{(u-v)^n}{\sqrt{D_n(u)B_n(v)}}\\[1.2ex]
  \dfrac{(v-u)^n}{\sqrt{B_n(u)D_n(v)}} &
  \dfrac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}}
  \end{pmatrix}.
  \]
  Its determinant is therefore the lower-right entry plus the product of the off-diagonal terms:
  \[
  \det M_n(u,v)=\frac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}},
  \]
  exactly the ambient \(A_{n-1}\) cosine from the deposited ambient Veronese theorem. Proved in the deposited ambient richness corollary: this \(c_n(u,v)\) is generically not a function of overlap alone for every \(n\ge2\), since the Jacobian \(\det \partial(I_n,c_n)/\partial(u,v)\) is nonzero at \((0,1)\). Therefore the `O_{n-1}` singular-value pair, whose product is \(|\det M_n|=|c_n|\), cannot be determined by overlap alone either. This yields the desired all-`n` benchmark-family corollary on the value-channel-free side.
- **Exact refs**: `quantum/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md:3-23`; `quantum/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md:3-43`; `quantum/20260423-194242-attack-veronese-richness/reports/gap-veronese-richness.md:3-21`; `quantum/findings.md:50-64,115-131`; `quantum/20260423-194725-attack-Or-richness/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The deposited ambient Veronese theorem; the deposited `O_{n-1}` Veronese theorem; the deposited ambient richness corollary for all \(n\ge2\); determinant as a symmetric function of the singular values.
- **Strongest objection**: This is a corollary about generic non-determinacy from overlap alone, not a full closed-form diagonalization of the `O_{n-1}` singular values for all \(n\). It says the `O_{n-1}` data is richer than overlap, but not how much richer in complete closed form.
- **Needed for promotion**: Add only as a short benchmark-family corollary: the value-channel-free Veronese family is generically richer than overlap for all \(n\ge2\). No stronger all-`n` singular-value formula is required for that claim.
