# Actual-formula inspection for C-FS2/C-FS3

## Question

Inspect the actual corrected order-
\(3,5,7\) formulas for evidence that either:

1. relational/provenance-sensitive data can enter the fixed C triple \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\); or
2. the formulas explicitly forbid the adversarial \(c^2\varepsilon\kappa\) deformation in \(\Delta^{\corr}\).

## Findings

### 1. The paper does not define an actual two-atom fixed C triple

The paper defines the one-pair fixed-sector package \((c,A_5^{\mathfrak f},\Delta_7)\), the abstract conditional source criterion, and the defect-thickened identities involving \(E_{12}^{(3)}\), \(E_{12}^{(5)}\), and \(\overline E_{12}^{(7;1)}\). It does not define
\[
(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
\]
as an actual corrected two-atom analytic germ. The current C triple is a theorem-ready schema from the team reports, not a paper object.

This means no paper formula can presently prove C-FS2 unconditionally. At best, one can state a conditional no-extra-state theorem for an assumed fixed-triple construction.

### 2. The defect-thickened third coordinate has an explicit septic quotient-defect slot

In `proof_of_rh.tex:11603-11669`, the third \(\widehat\Psi\) coordinate satisfies
\[
\frac{\Delta_1}{c_1^2}-\frac{\Delta_2}{c_2^2}
=
\frac{-\lambda c_2^2\det(A_{7,2}^{\mathfrak f},E)+c_2^2\det(R,A_{5,1}^{\mathfrak f})+\Delta_2(2\lambda c_2 e-e^2)}{c_1^2c_2^2},
\]
where \(e=E_{12}^{(3)}/a_1\), \(E=E_{12}^{(5)}/a_1\), and \(R\) is a representative of \(-a_1^{-1}\overline E_{12}^{(7;1)}\).

The term
\[
\det(R,A_{5,1}^{\mathfrak f})
\]
is the relevant C-codomain channel: it is independent of the representative of the quotient defect, hence it is a fixed scalar compatible with the \(\Delta\)-coordinate. But the paper does not compute \(R\) for the actual corrected two-atom exceptional divisor. Thus a relational/provenance-sensitive septic quotient defect can enter the fixed C triple through this determinant scalar unless a merger/state-locality theorem sets or controls \(R\).

### 3. The explicit centered order-
\(7\) formulas contain \(\kappa\)-linear determinant coefficients

The centered Taylor package gives
\[
\Delta_7(s)=D_2s^2+D_4s^4+D_6s^6+\cdots,
\]
with
\[
D_2=\widehat U_1V_1-U_1\widehat V_1.
\]
The displayed formulas for \(\widehat U_1\) and \(\widehat V_1\) both have an overall \(2\kappa\) factor. Therefore
\[
D_2=2\kappa(A V_1-B U_1)
\]
for the corresponding channel linear forms \(A,B\). There is no paper identity at these lines forcing
\[
A V_1-B U_1=0.
\]
The script `scripts/centered_delta_kappa_check.py` encodes this coefficient template and outputs

```text
D2 = 2*A*V1*kappa - 2*B*U1*kappa
dD2/dkappa = 2*A*V1 - 2*B*U1
generic_nonzero_condition = 2*(A*V1 - B*U1)
example_value = 2*k
```

This is not a proof that the actual C exceptional trace contains exactly \(\varepsilon\kappa\). It is evidence that the actual displayed order-
\(7\) coefficient language does not forbid \(\kappa\)-linear third-coordinate dependence; indeed the formulas visibly allow it unless a separate identity cancels the determinant combination.

### 4. The actual corrected formula audit supports a scoped negative, not C-FS2 closure

The strongest source-backed statement is:

- [proved] Raw septic representative ambiguity is removed by \(\Delta\); pure same-point septic terms vanish in the odd germ; weight-one septic determinant reduces to the direct \(K_1\) transport slice.
- [proved] The order-
  \(7\) determinant channel can carry transport/provenance data through \(u_{7,K_1},v_{7,K_1}\), and the centered coefficients are \(\kappa\)-linear.
- [missing] There is no actual two-atom fixed-triple construction proving all such determinant data is determined only by the reduced base \(\widehat\Psi\), nor any paper identity forbidding a \(c^2\varepsilon\kappa\)-type deformation.

## Scoped negative / countermodel shape

A source-consistent countermodel shape is:

1. Keep the fixed codomain \(\mathbf C\times\mathfrak f\times\mathbf C\) and reduction \(\mathcal R\).
2. Let the cubic and quintic components satisfy the expected blow-up edge laws or even match the central base.
3. Add to the septic quotient-defect representative \(R\) a relational/provenance-sensitive component whose determinant with \(A_{5,1}^{\mathfrak f}\) equals \(c^2\varepsilon\kappa\) on the exceptional divisor.
4. This changes \(\Delta^{\corr}\) by \(c^2\varepsilon\kappa\), hence changes the third reduced coordinate by \(\varepsilon\kappa\), without adding a new codomain coordinate.

This is not excluded by the audited formulas because \(R\) is not computed for the actual corrected two-atom package, and the centered determinant coefficients already carry \(\kappa\)-linear transport terms.

## Conditional no-extra-state theorem if one wants a positive route

The strongest conditional C-FS2 theorem I can state is:

> Assume an actual corrected two-atom order-
> \(3,5,7\) fixed-sector package \(\mathfrak P_2^{\corr}\) is constructed in \(\mathbf C\times\mathfrak f\times\mathbf C\), and assume its order-
> \(7\) component is obtained by taking the determinant of a fixed-sector quotient class \([A_7^{\mathfrak f,\corr}]\) against \(A_5^{\mathfrak f,\corr}\), with all pure raw-septic gauges modded out by the proven one-pair gauge law. Then through order \(7\), no raw septic representative state survives in the C codomain; all C-visible data is represented by \((C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})\). However, this theorem does not imply \(\kappa\)-independence of \(\Delta^{\corr}/(C^{\corr})^2\); a separate diagonal-merger identity is needed to rule out determinant-level relational terms such as \(c^2\varepsilon\kappa\).

This is C-FS2 only after assuming the fixed-triple construction and determinant-compression hypothesis. It leaves C-FS3 open.
