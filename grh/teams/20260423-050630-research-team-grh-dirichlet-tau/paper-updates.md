# Paper Updates

Staged coordinator text for the GRH Dirichlet-tau resume team. Not applied to
any canonical paper. Current status: draft only; do not promote until the
clean-copy citation check is complete.

## Completed-Hadamard Paired Source Package Draft

Proposed replacement for the Stage 1 source-package wording in
`paper/dirichlet_paired_source_package_candidate.tex` and the corresponding
Stage 1 paragraph in `paper/dirichlet_paired_source_candidate.tex`.

```tex
\section{Completed paired source package}

Let \(\chi\) be a primitive nonprincipal Dirichlet character. Put
\[
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\qquad
\Phi_\chi^{\mathrm{pair}}(s):=
\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}.
\]
Let \(I\subset\mathbb R\) be compact and assume that
\[
2it\notin Z(\Xi_\chi),\qquad 1+2it\notin Z(\Xi_\chi)
\]
for every \(t\in I\). On \(I\) choose the boundary phase by
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t).
\]
Equivalently,
\[
q_\chi^{\mathrm{pair}}(t)
=-\frac12
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}
{\Phi_\chi^{\mathrm{pair}}}\!\left(\tfrac12+it\right).
\]

Define
\[
D_\chi(t):=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
Then \(q_\chi^{\mathrm{pair}}(t)=\Re D_\chi(t)\), and
\[
\Re D_\chi(t)
=
\Re\sum_{\rho\in Z(\Xi_\chi)}
m_\rho
\left(
\frac{1}{1+2it-\rho}
-\frac{1}{2it-\rho}
\right),
\]
where \(Z(\Xi_\chi)\) is the completed zero multiset and \(m_\rho\) is
analytic multiplicity in the product
\(\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\overline\chi)\).
The series converges absolutely and uniformly on \(I\), and the same is true
after any fixed number of \(t\)-derivatives.

Thus, in the completed-Hadamard normalization,
\[
q_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
=B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
+S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t),
\qquad
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=0,
\]
with
\[
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
:=
\Re\sum_{\rho\in Z(\Xi_\chi)}
m_\rho
\left(
\frac{1}{1+2it-\rho}
-\frac{1}{2it-\rho}
\right).
\]
```

Proposed raw-bookkeeping remark, separate from the theorem:

```tex
\begin{remark}[Raw \(L\)-factor bookkeeping]
The preceding source package uses completed zeros of
\(\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\overline\chi)\). In that
normalization there is no additional gamma, trivial-zero, pole, conductor, or
Hadamard-exponential background term. If one rewrites the same identity using
raw \(L(s,\chi)\) and \(L(s,\overline\chi)\) zeros only, the gamma,
trivial-zero, pole, and raw-Hadamard edge-difference terms must be placed in a
separate raw background. They must not be added to the completed-zero theorem,
or the source statement mixes two normalizations.
\end{remark}
```

Citation placeholders still needed before promotion:

- Primitive nonprincipal completed \(L\)-function package:
  Davenport, `Multiplicative Number Theory`, clean-copy chapters 9 and 12, or
  replacement exact Montgomery-Vaughan/Apostol references.
- Order-one Hadamard product, zero summability, and logarithmic derivative:
  Davenport clean-copy chapters 11 and 12, plus a standard complex-analysis
  theorem for analytic multiplicity in canonical products.
- \(L(1,\chi)\ne0\) and the zero-at-origin exclusion:
  clean textbook or DLMF-backed citation; keep a finite-factor clause if a
  broader variant ever permits \(\rho=0\).

Provenance:
`agents/20260424-183416-explorer-background-multiplicity/report-background-split.md`;
`agents/20260424-183416-gap-compact-regularization/report-source-audit.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md`;
`agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md`.
