# Audit of what the paper actually proves about state-locality on the residual fixed-shear corner

1. The paper proves an exact reduction from the residual fixed-shear corner to a package-level parity/diagonal-vanishing criterion for the actual corrected cubic and quintic defects. Along an involutive branch
   \[
   (h_1,h_2)=(h(t),h(-t)),
   \]
   if the actual corrected defects satisfy
   \[
   E_{12}^{(3)}(t)=E_{12}^{(3)}(-t),\qquad E_{12}^{(5)}(t)=E_{12}^{(5)}(-t),
   \]
   and vanish at coincidence, then
   \[
   E_{12}^{(3)}(t),E_{12}^{(5)}(t)=O(t^2),
   \]
   hence the residual branch is excluded.

2. The paper also proves quotient-visible transport descent. Every parity-normalized finite transport jet descends to the quotient variable
   \[
   u=t^2,
   \]
   and on the quartic--sextic rung every finite quotient-visible transport state
   \[
   \mathcal T_N(t)=(\Theta_0(t),\dots,\Theta_N(t))
   \]
   is locally an analytic function of the single scalar
   \[
   Q(t)=\widehat Q(t^2).
   \]
   There is no third local reset beyond the involution \(t\leftrightarrow -t\).

3. What the paper does **not** provide is an actual formula expressing the corrected two-pair defects themselves as functions of this descended state. The only theorem of that shape is explicitly conditional:
   \[
   E_{12}^{(3)}(t)=\mathfrak e_3(\mathcal T_N(t)),\qquad E_{12}^{(5)}(t)=\mathfrak e_5(\mathcal T_N(t))
   \]
   is assumed, not derived.

4. Likewise, the stronger package statement is also conditional. The paper assumes a state-local form
   \[
   \mathcal P_2(t)=\mathfrak P_2\bigl(a_1(t),a_2(t);\mathcal T_N(t),\mathcal T_N(t)\bigr)
   \]
   together with the merger law
   \[
   \mathfrak P_2(a_1,a_2;Y,Y)=(a_1+a_2)\mathfrak F(Y),
   \]
   and then concludes \(\mathcal I_2(t)\equiv 0\). Again, this is a clean conditional bridge, not an already-proved identification of the actual package.

5. So the sharp source-backed status is:
   - [confirmed] the paper reduces the residual exact fixed-shear corner to proving swap-invariance + coincidence-vanishing for the actual corrected defects;
   - [confirmed] the paper proves that every finite quotient-visible transport coordinate descends and that no extra finite-order quotient-visible hidden reset survives;
   - [confirmed] the paper does **not** yet prove that the actual corrected two-pair defects or package factor through the descended transport state;
   - [candidate] the first unresolved object is therefore exactly the relational/provenance-sensitive lift variable suggested by the affine-bundle picture.

6. This means the affine-bundle redirect is now tighter than before: Bottleneck D is not asking for another quotient-visible transport scalar. It asks for one of two things:
   - a theorem deriving state-locality of the actual corrected two-pair defects/package from the corrected package object; or
   - an explicit first relational term showing why such state-locality fails.
