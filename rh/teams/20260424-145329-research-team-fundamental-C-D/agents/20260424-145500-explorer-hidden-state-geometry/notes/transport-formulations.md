# Transport / connection formulations for hidden lift geometry

1. The paper already uses the language of an affine line of raw septic representatives:
   \[
   A_{7,K_1}^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}.
   \]
   This is exactly the local model of the hidden-state fiber after lower data are fixed.

2. Two local gauge sections are already recorded:
   - on \(v_5\neq 0\), choose \(v_7^{\new}=0\), giving
     \[
     u_7^{\new}=\Delta_7/v_5;
     \]
   - on \(u_5\neq 0\), choose \(u_7^{\new}=0\), giving
     \[
     v_7^{\new}=-\Delta_7/u_5.
     \]
   These are not canonical globally, but they show the lift fiber is locally trivial as an affine line bundle.

3. Transition map between the two local sections on the overlap \(u_5v_5\neq 0\):
   starting from the \(v_7=0\) gauge with representative
   \[
   (u_7,v_7)=\left(\frac{\Delta_7}{v_5},0\right),
   \]
   the gauge parameter needed to reach \(u_7^{\new}=0\) is
   \[
   c_2=-\frac{u_7}{u_5}=-\frac{\Delta_7}{u_5v_5}.
   \]
   Then
   \[
   v_7^{\new}=c_2v_5=-\frac{\Delta_7}{u_5}.
   \]
   So the overlap cocycle is explicitly the scalar
   \[
   -\frac{\Delta_7}{u_5v_5}.
   \]
   This is the affine translation between the two obvious local sections.

4. Since \(\Phi_K\) extracts the \(S\)-component, the visible coefficient in these two gauges is respectively
   \[
   0
   \qquad\text{and}\qquad
   -\frac{\Delta_7}{u_5}.
   \]
   Therefore visibility is gauge-dependent even when the quotient datum is fixed. A transport theorem for D cannot be merely quotient-level; it must control the overlap translations or prove that the package-to-transform map annihilates them.

5. Candidate formulation A: affine-bundle descent.
   For the corrected two-atom package over a reduced-package base \(B\), let \(\mathcal A\to B\) be the affine line bundle of septic lifts parallel to \(A_5^{\mathfrak f}\). The corrected transform map should factor through the base after applying \(\Phi_K\) to the first surviving odd jet.

6. Candidate formulation B: connection / holonomy statement.
   Equip \(\mathcal A\to B\) with a local gauge one-form given by the translation parameter \(c_2\). Then D would follow if the induced holonomy on visible odd jets is \(\Phi_K\)-invisible, i.e. every closed transport along a reduced-package fiber produces change in \(\ker\Phi_K\).

7. Candidate formulation C: exact obstruction scalar.
   The smallest obstruction to D may be the transition scalar
   \[
   \tau:=\frac{\Delta_7}{u_5v_5}
   \]
   on \(u_5v_5\neq 0\). If corrected coincidence forces \(\tau\) to be constant, vanish, or enter only through the \(I\)-component after package-to-transform transfer, then the hidden visible lift-coordinate would collapse.

8. Strong caution: \(\tau\) is only a local overlap quantity; it is not yet shown to be intrinsic on the actual corrected two-atom package, and it blows up where \(u_5=0\) or \(v_5=0\). So it is a candidate diagnostic, not a promoted invariant.
