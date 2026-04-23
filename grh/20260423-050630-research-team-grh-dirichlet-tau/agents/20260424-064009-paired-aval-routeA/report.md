## Claim

The cleanest theorem-facing definition, mirroring the manuscript as closely as current scope allows, is the following conditional paired analogue of `paper/proof_of_rh.tex:465-469` and `1531-1606`.

Fix a primitive nonprincipal Dirichlet character \(\chi\), a midpoint \(m\), and a symmetric microscopic window \([m-\sigma/2,m+\sigma/2]\). Assume the paired corrected same-point and mixed blocks are defined and holomorphically whitenable, so that the paired corrected whitened block
\[
\widehat\Omega_{\chi}^{\pair,\corr}(\sigma;m)
\]
is defined, together with its paired background block at the background value-channel parameter
\[
S_\chi^{\pair}(m)=0.
\]
Then the safest theorem-facing definition is
\[
A_{\val,\chi}^{\pair}(m,\sigma)
:=
\left.\frac{\partial}{\partial \alpha}
\widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\right|_{\alpha=0},
\]
where \(\widehat\Omega_{\chi,\alpha}^{\pair,\corr}\) denotes the same paired corrected whitened family under a pure paired value-channel perturbation \(\alpha\) away from the background level, with the non-value local data frozen at background level exactly in the manuscript sense.

Equivalently: \(A_{\val,\chi}^{\pair}(m,\sigma)\) is the first derivative of the paired corrected whitened block with respect to the scalar paired value-channel parameter, taken at the paired background value \(S_\chi^{\pair}(m)=0\).

This is the cleanest current theorem-facing definition because it says exactly which background value is used and exactly which derivative is being taken, while not overclaiming any transported explicit formula, exact slot identity, or remainder theorem.

## Status

conditional

## Evidence

**Proved.**

- In the manuscript, the unpaired object is defined by
  \[
  A_{\val}(m,\sigma):=\left.\frac{\partial}{\partial\alpha}\Omega_\infty(T_1,T_2)\right|_{\alpha=0}
  \]
  under a pure value-channel perturbation \(q_1=q_2=B+\alpha\), with all derivative and curvature data frozen at background level.
- In the corrected local deformation step, the manuscript restates the same first-order role at the corrected-whitened level: the corrected whitened block is expanded around the background value-channel parameter \(S(m)=0\), and the first-order coefficient is declared to be exactly the pure value-channel derivative \(A_{\val}(m,\sigma)\).
- The paired notes already isolate the theorem-facing local hypothesis block needed to speak about a paired corrected whitened block and its first paired value-channel derivative: microscopic holomorphy, same-point positivity/nondegeneracy, holomorphic inverse-square-root whitening, and existence of the first paired value-channel derivative.

**Conditional on [paired corrected local whitening package].**

- The manuscript-style definition transports safely only as a first-order local algebra statement. So the paired theorem-facing definition should be the derivative of the paired corrected whitened block at the paired background value \(S_\chi^{\pair}(m)=0\), not an explicit transported matrix formula.
- Under the paired local symmetric normal form plus corrected-whitening admissibility, the notation
  \[
  A_{\val,\chi}^{\pair}(m,\sigma)
  =
  \left.\partial_\alpha \widehat\Omega_{\chi,\alpha}^{\pair,\corr}(\sigma;m)\right|_{\alpha=0}
  \]
  is the closest faithful analogue of the manuscript definition currently supported by the record.
- This wording correctly names both ingredients the user asked for: the background value is \(S_\chi^{\pair}(m)=0\), and the derivative is the first derivative in the pure paired value-channel direction, with the rest of the local deformation frozen at background level.

**Missing.**

- A paired local construction that writes the analogue of the manuscript's pure perturbation \(q_1=q_2=B+\alpha\) explicitly inside the paired corrected family, rather than only referring to a first-order paired value-channel direction abstractly.
- A paired proposition identifying the resulting first-order coefficient of the corrected whitening expansion with a canonically defined object \(A_{\val,\chi}^{\pair}\) rather than merely assuming its existence.
- Any paired explicit formula corresponding to `prop:explicit-Aval`.
- Any proof that the same scalar \(S_\chi^{\pair}(m)\) is exactly the coefficient of this derivative in
  \[
  \Delta_\chi^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_\chi^{\pair}.
  \]

Honest verdict: the theorem-facing definition is clean only as a conditional local interface. The safe statement is `derivative of the paired corrected whitened block in the pure value channel at paired background value S_chi^pair(m)=0`. Anything stronger currently overstates the record.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/aval_transport.md:8-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-29,31-37,68-77`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/whitening_interface.md:7-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:24-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-022935-paired-slot-hypotheses-routeA/report.md:27-30,47-55,57-64,87-97`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-052413-whitening-interface-routeA/report.md:3-19,32-46,70-87`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:471-565`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1527-1549`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1590-1606`

## Dependencies

- Exact compact-interval paired background scalar \(S_\chi^{\pair}(m)=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)\).
- Paired local symmetric normal form on the microscopic window around \(m\).
- Paired corrected same-point and mixed local blocks.
- Same-point positivity/nondegeneracy and holomorphic inverse-square-root whitening.
- A well-defined pure paired value-channel perturbation inside that corrected whitened family.

## Strongest objection

The notation \(\widehat\Omega_{\chi,\alpha}^{\pair,\corr}\) is theorem-facing but still partly schematic: the current record does not yet supply a paired manuscript-level proposition that writes the pure paired value perturbation as explicitly as the unpaired formula \(q_1=q_2=B+\alpha\). So the definition is clean and likely right at the interface level, but not yet backed by a fully written paired local construction.

## Needed for promotion

1. Write the paired corrected local deformation proposition with explicit notation for the paired corrected same-point, mixed, and whitened blocks.
2. State the pure paired value-channel perturbation explicitly inside that proposition.
3. Prove that the first derivative at \(S_\chi^{\pair}(m)=0\) exists and is the canonical object \(A_{\val,\chi}^{\pair}(m,\sigma)\).
4. Prove the exact slot identity \(\Delta_\chi^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_\chi^{\pair}\).
