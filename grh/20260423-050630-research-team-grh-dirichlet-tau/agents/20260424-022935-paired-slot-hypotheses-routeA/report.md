## Claim

The paired exact slot identity
\[
\Delta_\chi^{\pair}(m,\sigma)
=
S_\chi^{\pair}(m)\,A_{\val,\chi}^{\pair}(m,\sigma)
+
R_\chi^{\pair}(m,\sigma)
\]
is a well-posed exact theorem only under a slightly stronger package than the bare upstairs source theorem. The clean minimal hypothesis stack is:

1. **Object-definition hypotheses.**
   - Fix a primitive nonprincipal Dirichlet character \(\chi\), a compact interval \(I\subset\mathbb R\), and the paired quotient
     \[
     \Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\bar\chi),
     \qquad
     \Phi_\chi^{\pair}(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}.
     \]
   - Assume a boundary-phase/phase-derivative package on a complex neighborhood of \(I\) strong enough to define the paired phase derivative \(q_\chi^{\pair}(t)\).
   - Assume an exact compact-interval source decomposition
     \[
     q_\chi^{\pair}(t)=B_\chi^{\pair}(t)+S_\chi^{\pair}(t)
     \qquad (t\in I),
     \]
     where \(B_\chi^{\pair}\) absorbs all conductor/scaling, gamma-derivative, and trivial-zero/pole bookkeeping, and \(S_\chi^{\pair}\) has exact convergence/regularization and multiplicity conventions.
   - Assume a paired local symmetric normal form, with corrected same-point and mixed local blocks built on a microscopic symmetric window \([m-\sigma/2,m+\sigma/2]\subset I\), and assume just enough holomorphy/removable-singularity structure that the corrected paired whitened block and its background block at \(S_\chi^{\pair}(m)=0\) are defined.
   - Assume the same-point paired blocks stay positive definite on that microscopic disk so the inverse square roots and whitening map exist holomorphically there. This is part of object definition, not a downstream estimate: without it, \(\Delta_\chi^{\pair}\) and \(A_{\val,\chi}^{\pair}\) are not even canonically defined.
   - Assume the pure paired value-channel derivative is defined as the first derivative of the paired whitened block at background value \(S_\chi^{\pair}(m)=0\); call it \(A_{\val,\chi}^{\pair}(m,\sigma)\).

2. **Stronger estimate hypotheses, not needed for the exact theorem itself.**
   - Microscopic denominator comparability and omitted-smooth holomorphy with quantitative bounds.
   - Corrected-whitening transport estimates and preserved post-\(\Phi_K\) scale.
   - Any smallness estimate on \(R_\chi^{\pair}\), such as \(\Psi(R_\chi^{\pair})=o((x/B)S_\chi^{\pair})\).
   - Odd/transverse realization, boundary estimates, and any calibration or endgame consequence.

So the honest minimal statement is: the paired source theorem plus the local holomorphic-whitening setup needed to define the paired corrected deformation and its first value-channel derivative make the exact identity well-posed; quantitative denominator/whitening/remainder bounds are separate stronger hypotheses.

## Status

open

## Evidence

**Proved.**

- The note record already separates the paired theorem burden into two linked pieces: upstairs paired source realization and downstairs exact local-slot identification.
- The manuscript shows the local pattern of the exact identity: once the corrected local deformation and background-whitened object are defined, one expands the whitening map at background value and obtains an exact decomposition \(\Delta=S A_{\val}+R\) with \(R\) defined by subtraction.
- The manuscript also separates this exact identity from stronger estimates: remainder dominance and the odd/transverse package occur only after the exact split is already in place.

**Conditional on [paired local holomorphic-whitening setup + paired compact-interval source theorem].**

- The paired identity is well-posed if one has both: `(i)` an exact compact-interval definition of \(S_\chi^{\pair}=q_\chi^{\pair}-B_\chi^{\pair}\), and `(ii)` a paired analogue of the manuscript's corrected local deformation in which the whitened block, its background value, and its first value-channel derivative are analytically defined.
- Positive-definiteness/holomorphic inverse-square-root hypotheses belong on the definition side, not on the downstream-estimate side, because the manuscript's \(\Delta\) is itself defined from a corrected whitened block.
- Denominator comparability and corrected-whitening transport can be kept out of the theorem statement only if their role has already been compressed into the object-definition hypotheses above. They are needed quantitatively later, but only their definitional residue is needed to state the exact theorem.

**Missing.**

- A paired compact-interval source theorem giving a theorem-ready \(q_\chi^{\pair}=B_\chi^{\pair}+S_\chi^{\pair}\) with all bookkeeping explicit.
- A paired corrected local deformation theorem showing the same-point and mixed local blocks are holomorphic and whitenable on a microscopic symmetric disk.
- A proof that the coefficient appearing in the first-order paired value channel is exactly the same scalar \(S_\chi^{\pair}(m)\) from the compact-interval source decomposition, not merely a nearby paired strip-edge kernel.
- A proof that no stronger denominator/whitening estimate beyond bare holomorphic definability is secretly needed just to formulate the exact paired identity.

Honest verdict: the minimal analytic package is `source theorem + local definability of the corrected paired whitened block and its first value-channel derivative`. The exact paired identity does **not** need remainder smallness, odd/transverse realization, or boundary control. But it likely **does** need a small analytic whitening/positivity hypothesis package on the definition side; otherwise `\Delta_\chi^{\pair}` and `A_{\val,\chi}^{\pair}` are not yet well-posed objects.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:84-108,146-176`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:11-22,24-46`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/aval_transport.md:8-25,27-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-23,24-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:8-20`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:18-27,29-55,66-87`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-021955-paired-slot-theorem-routeA/report.md:30-35,56-62,83-92`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-021955-paired-slot-theorem-routeB/report.md:38-46,75-84`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:431-469,471-599`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-903`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1457`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1621`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2060-2087`

## Dependencies

- Exact compact-interval paired source theorem for \(\Phi_\chi^{\pair}\).
- Unified paired background bookkeeping \(B_\chi^{\pair}\) with convergence/regularization and multiplicity conventions.
- Paired local symmetric normal form and corrected local block construction on microscopic symmetric windows.
- Holomorphic positive-definite same-point blocks so that whitening and the background expansion at \(S_\chi^{\pair}(m)=0\) are defined.

## Strongest objection

The sharpest uncertainty is where to draw the line between `definition hypotheses` and `transport/estimate hypotheses`. The notes correctly quarantine denominator comparability and corrected-whitening transport as stronger downstream packages, but the manuscript's exact identity is formulated inside a corrected whitened object. So a paired theorem cannot literally avoid all whitening-side analytic assumptions; it can only avoid their quantitative estimate forms. Current evidence supports that distinction, but does not yet prove it in a paired family.

## Needed for promotion

1. Prove a compact-interval paired source theorem with explicit \(B_\chi^{\pair}\) and \(S_\chi^{\pair}\).
2. State and prove a paired local holomorphic-whitening setup sufficient to define the corrected paired deformation and background value-channel derivative.
3. Prove that the coefficient in the paired first-order local expansion is exactly the scalar \(S_\chi^{\pair}(m)\) from the source theorem.
4. Verify adversarially that denominator comparability and corrected-whitening transport are needed only quantitatively after the exact identity, not for its bare well-posedness beyond the minimal definability hypotheses above.
