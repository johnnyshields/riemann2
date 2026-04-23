# Report

- **Claim**
  On the residual involutive exact fixed-shear branch 
  \[
  (h_1,h_2)=(h(t),h(-t)),
  \]
  the package-level content behind
  \[
  E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0
  \]
  is exactly the coincident-atom diagonal merger law for the actual corrected two-atom package. More precisely, if the actual corrected cubic/quintic outputs come from a two-atom package \(\mathfrak P_2\) with one-atom package \(F_h\), then diagonal coincidence at \(t=0\) is equivalent to
  \[
  \mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h,
  \]
  and this is the single narrow blocker on Bottleneck B. The present draft does not prove this merger law; the naive source-summed corrected-block model obstructs it because its extracted finite-order coefficients are even analytic in the source weight and therefore cannot supply the required linear dependence on \(a_1+a_2\).

- **Status**
  open

- **Evidence**
  The residual involutive closure proposition is already formal once two inputs are available: swap-evenness and diagonal vanishing of the actual corrected cubic/quintic defects. This is stated explicitly in Proposition~\ref{prop:residual-involutive-defect-criterion-fixed-shear-corner} and Corollary~\ref{cor:package-level-reduction-residual-fixed-shear-corner}. The stronger state-local closure proposition shows the same thing after descent: if the defects factor through the descended transport state and vanish at the involutive basepoint, then the residual branch dies.

  The only nonformal part is therefore the exact value at coincidence. In the draft's two-atom language, that value is the diagonal restriction of the corrected two-atom package. Lemma~\ref{lem:minimal-source-level-two-point-criterion} identifies the exact needed law: swap symmetry, one-amplitude collapse, and the diagonal merger identity
  \[
  \mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h.
  \]
  On the diagonal this identity is exactly what makes the interaction remainder vanish, hence exactly what forces the cubic/quintic defect values at coincidence to be zero.

  The narrow obstruction is also explicit. Remark~\ref{rem:audit-even-amplitude-obstruction-naive-source-summed-two-point} shows that for the naive source-summed corrected-block construction,
  \[
  G^{\corr}_{a,h,\pm}(s)=a\,\mathcal G_{h,\pm}(a^2;s),
  \qquad
  N^{\corr}_{a,h}(s)=a\,\mathcal N_h(a^2;s),
  \]
  so whitening cancels the overall factor \(a\), and every extracted finite-order coefficient becomes an even analytic function of the source weight. Therefore that model cannot furnish analytic one-atom linearity or coincident-atom additivity unless it vanishes identically. This kills the most obvious local proof of diagonal coincidence and isolates the missing theorem: a different lift/transport/package object whose coincident restriction is truly linear in the total weight.

- **Exact refs**
  `paper/proof_of_rh.tex:11889-11992`
  `paper/proof_of_rh.tex:12170-12228`
  `paper/proof_of_rh.tex:12452-12489`
  `paper/proof_of_rh.tex:22302-22505`
  `paper/proof_of_rh.tex:22966-23109`
  `paper/proof_of_rh.tex:24525-24540`
  `paper/proof_of_rh.tex:24985-25030`
  `paper/proof_of_rh.tex:25119-25123`

- **Dependencies**
  A precise actual corrected two-atom package object on the exact fixed-shear involutive branch.
  A proof that its diagonal restriction at coincident atoms is merger-linear in \((a_1,a_2)\), or an equally strong quotient-level diagonal-collapse theorem implying the same cubic/quintic vanishing.
  Swap symmetry of the package along the involutive parametrization.

- **Strongest objection**
  This report does not prove the diagonal merger law itself. It only sharpens Bottleneck B to that single exact statement and shows why the current naive corrected-block formulas are insufficient. A different package representative could still satisfy the merger law after additional transport/provenance structure is inserted, so this is an obstruction to the present route, not a no-go theorem for diagonal coincidence from every possible route.

- **Needed for promotion**
  Prove for the actual corrected two-atom package, on coincident atoms, either
  \[
  \mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h
  \]
  or directly
  \[
  E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0
  \]
  in a form independent of the projective blow-up parameter \(\kappa\). Equivalently: construct a package/lift whose diagonal restriction preserves first-order total-weight linearity after whitening/transport, since the raw source-summed corrected-block model does not.

Honest verdict: theorem-shaped progress is the exact reduction of Bottleneck B to one package statement: coincident-atom diagonal merger for the actual corrected two-atom package. The narrowest current blocker is that the existing naive corrected-block construction is even in source weight after whitening and therefore cannot deliver the required diagonal coincidence law.
