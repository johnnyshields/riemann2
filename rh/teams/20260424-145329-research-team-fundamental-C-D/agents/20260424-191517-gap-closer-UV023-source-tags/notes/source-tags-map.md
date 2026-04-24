# UV-023 Source Tags Map

Own lane: `gap-closer-UV023-source-tags`.

## Candidate Construction

Let \(E=A_1(M_2)^3\) be the perturbation-triple space used by
`prop:differentiated-whitening-transfer`. If a source-defined one-atom linear
input
\[
L_h\in E
\]
were available before whitening, the natural two-atom tagged input would be
\[
X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2}.
\]
For any analytic \(E\)- or output-valued expression
\[
F(a_1,a_2)=\sum_{\alpha,\beta\ge 0}F_{\alpha,\beta}a_1^\alpha a_2^\beta,
\]
the source bidegree projector is then the coefficient projection
\[
\Pi_{1,1}F:=a_1a_2F_{1,1}.
\]
This is a source-side projection because it acts on the formal atom tags before
determinant scalarization or quotient-coordinate choices.

For the corrected-whitening cross-effect
\[
C=\mathcal T(a_1L_{h_1}+a_2L_{h_2})
-\mathcal T(a_1L_{h_1})
-\mathcal T(a_2L_{h_2}),
\]
the homogeneous degree-\(p\) piece has mixed source bidegrees
\((i,p-i)\), \(1\le i\le p-1\). Therefore \(\Pi_{1,1}C\) keeps only the
quadratic transfer piece. This is the formal reason the route is attractive.

## Source Obstruction

The inspected paper source does not provide the required \(L_h\). It provides:

- `rh/proof_of_rh.tex:2415-2553`: analytic corrected-whitening transfer
  \(\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)\) for arbitrary
  perturbation triples.
- `rh/proof_of_rh.tex:2597-2674`: one-pair weighted input
  \(X_\rho=\mathfrak D_Q(\delta G,\delta N)\), with linear-in-kernel behavior
  modulo terms containing at least two pair kernels.
- `rh/proof_of_rh.tex:12192-12227`: the naive source-summed whitened package is
  even in the source weight, so it is not the desired source-linear object.

Thus the formal \(L_h\) cannot be identified with an actual paper-defined
two-atom source-linear corrected-block input. Defining it as "the linear
source-tag part" would add a new projection not currently in the draft.

## Quotient Compatibility

Even if \(X^{[1]}\) and \(\Pi_{1,1}\) are introduced formally, the target
\[
Q_7^q(C)=Q_7^q(\Pi_{1,1}C)
\]
does not follow from tag algebra. It is equivalent to
\[
Q_7^q((1-\Pi_{1,1})C)=0,
\]
i.e. all non-\((1,1)\) source bidegrees are invisible to the fixed-target
order-7 quotient extraction.

The one-pair quotient-septic closure at `rh/proof_of_rh.tex:7892-8033` is not
this statement. It closes the one-pair fixed-sector quotient class; it does not
define the two-atom corrected-whitening cross-effect quotient channel or prove
that the channel is source-bidegree filtered.

## Smallest Missing Objects

Definitions:

1. A source-linear corrected-block input functor \(h\mapsto L_h\) before
   whitening, tied to the actual two-atom corrected blocks through order \(7\).
2. A fixed-target order-7 quotient extraction \(Q_7^q\) for the resulting
   corrected-whitening cross-effect before determinant scalarization.

Theorem:

3. Source-bidegree quotient compatibility:
   \(Q_7^q((1-\Pi_{1,1})C)=0\).

The projector itself is standard once the source tags exist. The missing part is
not the algebra of \(\Pi_{1,1}\); it is the source-defined input plus proof that
the actual quotient extraction ignores all non-\((1,1)\) bidegrees.
