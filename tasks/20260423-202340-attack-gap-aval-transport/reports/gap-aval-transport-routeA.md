# Claim

Conditional on a paired Dirichlet or \\(\tau\\) realization providing:

1. an exact local value slot \\(S(m)=q(m)-B(m)\\) in the corrected whitened deformation,
2. the same symmetric constant-background local jet algebra with background slope \\(B(m)\\), and
3. the same local whitening/normal-form interface used in the manuscript,

the following `A_val` package transports by local algebra alone:

- the explicit pure value-channel derivative \\(A_{\val}(x)\\) with \\(x=B(m)\sigma\\);
- the transverse cancellation \\(\Phi_K(A_{\val})=0\\);
- the small-\(x\) expansion and size law \\(\|A_{\val}(x)\|_F\asymp x/B(m)\\);
- the linear leading-term decomposition \\(\Delta=S(m)A_{\val}+R\\) once the coefficient slot is exact;
- the formal calibration identities obtained by pairing against the anomaly matrix and applying the linear functional \\(\Psi_{x,d}\\).

What becomes automatic after exact slot identification is the local leading-channel interface, not the analytic input that makes the remainder negligible or realizes the corrected block in that family.

Separation:

- proved: inside the manuscript's local algebra, the items above are consequences of differentiating the whitened constant-background block and of linearity/Taylor expansion.
- conditional on [paired family has exact slot + same local normal form]: the same formulas and identities carry over verbatim with \\(B_\zeta(m)\\) replaced by the family's local slope \\(B(m)\\) and with the family's exact slot coefficient \\(S(m)\\).
- missing: any theorem that a paired Dirichlet or \\(\tau\\) family actually satisfies those hypotheses, plus the remainder-dominance and corrected odd/transverse package needed to use the interface.

# Status

proved

# Evidence

The constant-background package is explicit. In lines 446--565 the manuscript perturbs only the value channel by \\(q_1=q_2=B+\alpha\\), freezes all derivative/curvature data, differentiates the jet-limit whitened block, and obtains a closed formula for \\(A_{\val}(x)\\). No zeta-specific source theorem is used in that calculation; the ingredients are the local matrices \\(M\\), \\(N_{12}\\), the phase gap \\(\Delta_0=-B\sigma\\), and the whitening map.

The next consequences are algebraic. Lines 567--599 prove \\(\Phi_K(A_{\val})=0\\) by exact cancellation of the off-diagonal entries. Lines 601--659 derive the small-\(x\) expansion and the size law \\(\|A_{\val}(x)\|_F\asymp x/B\\) by Taylor expansion of \\(\sin x\\) and \\(\cos x\\). These steps depend only on the explicit formula already obtained.

The calibration interface is also local once the anomaly matrix is fixed. Lines 661--794 pair \\(A_{\val}(x)\\) with the local toy anomaly matrix \\(M(d)\\), show the pairing is nonzero to first order, and define the linear functional \\(\Psi_{x,d}\\). The conclusions \\(\Psi_{x,d}(A_{\val})\asymp x/B\\) and
\\[
\Psi_{x,d}(\Delta)=c_{x,d}\,\frac{x}{B}S(m)+\Psi_{x,d}(R)
\\]
follow by the same local asymptotics and by linearity.

The corrected decomposition at lines 1497--1622 isolates the formal transport statement. Once a family has a corrected whitened block \\(\widehat\Omega^{\corr}\\) analytic in the value parameter and an exact background point \\(S(m)=0\\), Taylor expansion gives
\\[
\Delta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R(m,\sigma),
\\]
with \\(R:=\Delta-SA_{\val}\\) by definition. This is local algebra plus analyticity of whitening. The family-specific work lies in proving that the first-order coefficient is the desired exact slot and that the corrected object exists with the needed control.

Therefore, in a paired Dirichlet or paired \\(\tau\\) realization, exact slot identification would automatically give:

- the leading-channel term \\(S(m)A_{\val}\\) in the corrected local deformation;
- transverse invisibility of that leading channel under \\(\Phi_K\\);
- the small-slot scaling law \\(A_{\val}=O(x/B)\\) with first nonzero contribution off-diagonal;
- the formal calibration identity against the paired family's anomaly matrix, provided that anomaly matrix sits in the same local coordinate model.

This matches the paired-slot note: after exact slot identification, the leading-channel interface is automatic; what remains is remainder dominance, corrected odd/transverse realization, denominator/whitening control, boundary estimates, and calibration uniformity.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:6-37`
- `paper/proof_of_rh.tex:431-469` for the symmetric constant-background setup and definition of \\(A_{\val}\\)
- `paper/proof_of_rh.tex:471-565` for the explicit formula for \\(A_{\val}(x)\\)
- `paper/proof_of_rh.tex:567-599` for \\(\Phi_K(A_{\val})=0\\)
- `paper/proof_of_rh.tex:601-659` for the small-\(x\) expansion and \\(\|A_{\val}(x)\|_F\asymp x/B\\)
- `paper/proof_of_rh.tex:661-737` for pairing with the anomaly matrix
- `paper/proof_of_rh.tex:739-794` for the canonical calibration functional and linearity step
- `paper/proof_of_rh.tex:1497-1622` for the corrected decomposition \\(\Delta=S(m)A_{\val}+R\\)

# Dependencies

- Exact family-specific identification of the local value slot coefficient \\(S(m)=q(m)-B(m)\\).
- A paired-family corrected whitened block with the same local normal-form variables \\(m,\sigma,x=B(m)\sigma\\).
- Analyticity of the whitening map in the relevant positive-definite regime.
- A family-specific anomaly matrix in the same local coordinate system if one wants the calibration functional, not just the decomposition.

# Strongest objection

The transported package is smaller than it may look. The manuscript proves that once the exact slot and local constant-background model are in hand, the `A_val` algebra follows. It does not prove that a paired Dirichlet or \\(\tau\\) family really has the same corrected local block, the same first-order coefficient, or a compatible anomaly matrix. Those are exactly the hard realization steps. So from current scope alone, one should not claim that the non-zeta families inherit more than the formal leading-channel algebra.

# Needed for promotion

- A theorem in the paired family that the corrected local deformation has an exact coefficient slot \\(\Delta^{\pair}=S^{\pair}(m)A_{\val}^{\pair}+R^{\pair}\\) with the first-order coefficient equal to the local value-channel derivative.
- Verification that the paired family's constant-background jet algebra produces the same \\(A_{\val}\\) formula after replacing \\(B_\zeta(m)\\) by the family's local slope \\(B(m)\\), or a precise modified formula if not identical.
- A compatible anomaly matrix and nonvanishing pairing statement for the paired family if calibration is to be transported.
- The remaining analytic burdens listed in the paired-slot note: remainder dominance, corrected odd/transverse realization, denominator/whitening control, boundary estimates, and calibration uniformity.
- An adversarial check for failure modes in non-self-dual or genuinely complex settings, where the symmetric real-background cancellations behind \\(\Phi_K(A_{\val})=0\\) may require modification.

Honest verdict: exact slot identification would transport the local `A_val` interface, but only that interface. The manuscript's current algebra makes the leading-channel formulas automatic after realization; it does not make the realization or the remainder analysis automatic.
