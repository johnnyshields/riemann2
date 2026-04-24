# Determinant-slot reduction for C-R control

## Setup

Work in the fixed sector
\[
\mathfrak f=\operatorname{span}\{I,S\}.
\]
Write
\[
A_5^{\mathfrak f}=uI+vS,
\qquad
R=r_u I+r_vS.
\]
The determinant convention used by the paper gives
\[
\det(R,A_5^{\mathfrak f})=r_u v-u r_v.
\]

The source theorem at `rh/proof_of_rh.tex:11587-11775` proves that this scalar
is independent of the representative of the septic quotient-defect class, since
adding \(\xi A_5^{\mathfrak f}\) to \(R\) does not change the determinant. It
does not compute \(R\), and it does not prove that the quotient class descends
to the collision state.

## Linear algebra reduction

On every C-good patch where \(A_5^{\mathfrak f}\neq 0\), the map
\[
[R]\in \mathfrak f/\mathbf C A_5^{\mathfrak f}
\longmapsto
\det(R,A_5^{\mathfrak f})\in \mathbf C
\]
is an isomorphism.

Proof. The functional \(R\mapsto \det(R,A_5^{\mathfrak f})\) has kernel
\(\mathbf C A_5^{\mathfrak f}\). If \(u\neq0\), the equation
\[
r_u v-u r_v=0
\]
gives \(r_v=(v/u)r_u\), so \(R=(r_u/u)A_5^{\mathfrak f}\). If \(v\neq0\),
the same argument gives \(r_u=(u/v)r_v\). Since the quotient has dimension
one, the induced map is an isomorphism.

Thus the C determinant slot is not a weaker projection of the quotient defect:
it is exactly the one-dimensional quotient-defect class. Controlling
\(\det(R,A_5^{\mathfrak f})\) is equivalent to controlling \([R]\).

## Deformation test

Let \(\tau=c^2\varepsilon\kappa\). On the patch \(u\neq0\),
\[
R_\kappa=-\frac{\tau}{u}S
\]
satisfies
\[
\det(R_\kappa,A_5^{\mathfrak f})=\tau.
\]
On the patch \(v\neq0\),
\[
R_\kappa=\frac{\tau}{v}I
\]
does the same. Therefore the pinned deformation
\[
R\mapsto R+R_\kappa,
\qquad
\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa
\]
is always available at the quotient-class level unless an actual-package
theorem restricts \([R]\). Fixed codomain and representative-independence do not
restrict it.

The script
`scripts/determinant_slot_linear_algebra.js` checks this algebra on three
numeric samples and also checks the centered template
\[
D_2=2\kappa(A V_1-B U_1).
\]

## Smallest positive theorem target

The smallest useful C-FS2/C-FS3 target is not "choose a better representative
of \(R\)." Representative freedom is already gone after passing to the
determinant.

The target is the following quotient-class state-locality theorem.

Let the actual corrected two-atom package define, in the collision chart
\[
2\omega=\kappa\delta,\qquad t=\delta^2,
\]
a normalized septic quotient-defect class
\[
\mathcal R_7(m,\kappa,t)\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m,\kappa,t)
\]
whose representative is the \(R\) appearing in the defect-thickened identity.
Then on the exceptional divisor \(t=0\) one must prove:

1. **Descent:** \(\mathcal R_7(m,\kappa,0)\) factors through the descended
   collision state, not through independent provenance data.
2. **Fiber constancy for C:** along a fixed descended collision state,
   \[
   \partial_\kappa\det(\mathcal R_7(m,\kappa,0),A_5^{\mathfrak f}(m))=0.
   \]
3. **Merger normalization:** on the diagonal-merger state, the descended value
   agrees with the one-pair septic quotient value.

Equivalently, after subtracting the descended collision-state value, the
residual class must vanish in
\(\mathfrak f/\mathbf C A_5^{\mathfrak f}\). By the linear algebra above, this
is equivalent to vanishing of the determinant slot.

## Relation to the centered objection

The centered package shows
\[
D_2=2\kappa(A V_1-B U_1).
\]
The state-locality theorem must either force
\[
A V_1-B U_1=0
\]
in the actual corrected package, or identify this expression as a descended
state derivative that is constant on the relevant exceptional fiber. Without one
of those two statements, the centered channel remains a live obstruction.

## Honest verdict

The determinant control problem has been reduced to a quotient-class
state-locality theorem for the actual corrected two-atom septic defect. The
reduction is proved by two-dimensional linear algebra. The actual C closure is
still missing because the draft does not define the actual corrected two-atom
fixed triple or compute the exceptional-divisor class \(\mathcal R_7\).
