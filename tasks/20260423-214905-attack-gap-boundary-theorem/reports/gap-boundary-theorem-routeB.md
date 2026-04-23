## Claim

As a transport target, the boundary theorem is not the right next standalone theorem after corrected whitening. The partial corrected-whitening bundle already covers the holomorphic/positive-definite whitening stage and the post-`\Phi_K` transfer scale, but the boundary estimate in `paper/proof_of_rh.tex` still uses additional inputs that are not part of that bundle: value-channel cancellation in the transverse slot, cutoff-internalization of the full corrected scalar, and the quantitative domination step `S_2 \ll L(m)S(m)^2` on the boundary. The safer next standalone target is the combined corrected transverse realization-and-boundary theorem described in the odd-package note.

## Status

open

## Evidence

### Proved

The current corrected-whitening bundle already contains the three items identified in `corrected_whitening_transport.md`: denominator comparability plus omitted-smooth holomorphy; holomorphic corrected whitening with positive same-point blocks; preserved post-`\Phi_K` transfer scale. In the paper these are realized by Proposition `Microscopic denominator comparability and omitted-smooth holomorphy`, Proposition `Corrected finite-s holomorphic whitening`, and Proposition `Whitened mixed-block transfer with preserved Q^{-3} scale`. These are exactly the inputs needed to define the corrected whitened block holomorphically and to control the correction seen after whitening at size `S_2/Q^3`.

The boundary proposition does reuse those proved inputs directly. Its proof cites the corrected local decomposition, the cutoff-compatibility statement, `\Phi_K(A_{\val})=0`, and the corrected-whitening transfer bound. So part of the boundary theorem is genuinely downstream of corrected whitening rather than disjoint from it.

### Conditional on extra family-specific input

The boundary theorem becomes transportable only if the family already supplies a realized corrected transverse scalar in the right odd slot. The paper defines `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))`, and the odd-package note says the family-specific missing theorem is exactly: produce the corrected odd holomorphic transverse scalar, prove the microscopic denominator/whitening control needed to define it, and prove the boundary estimate on `|s|=\rho_0/Q`. Under that package, the odd germ and later Cauchy/projector steps are already universal.

Likewise, the boundary proof assumes the leading value channel disappears after projection. In the zeta draft this is supplied by the explicit antisymmetry computation `\Phi_K(A_{\val})=0`. For transport, this is not part of the narrow whitening bundle. It is available only once the family has identified the correct transverse slot and proved the corresponding value-channel cancellation there.

### Missing

Three ingredients used by the boundary proof are not already in the partial corrected-whitening bundle.

First, the proof needs the full corrected scalar, not just the whitened matrix package. This enters through the corrected local decomposition and cutoff-compatibility propositions, whose role is to show that auxiliary-near, tail, jet-correction, and estimation terms are internal to `H_{m,R}(s)` so that no external remainder survives at the boundary stage. That internalization is broader than whitening alone.

Second, the proof needs transverse value-channel annihilation after realization of the odd scalar. The corrected-whitening note explicitly lists `value-channel slot realization` as still separate. Without that step, one cannot replace the full boundary scalar by `\Phi_K(R_\zeta)`.

Third, the proof needs a quantitative domination step on the boundary: `S_2 \ll L(m)S(m)^2`. The corrected-whitening note and odd-package note both leave `boundary control for the odd scalar` and `remainder dominance` outside the safe transported bundle. From local whitening data alone one only gets the scale `\Phi_K(\widehat\Omega_\zeta^{\corr}-\widehat\Omega_\zeta^{(0)})\ll S_2/Q^3`; converting this into the final boundary bound requires the extra comparison between `S_2` and `L(m)S(m)^2` in the corrected regime.

Therefore the boundary theorem is not the minimal next theorem after corrected whitening. The minimal next theorem is the combined corrected transverse realization-and-boundary theorem, of which the boundary estimate is only one clause.

## Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-22`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:8-38`
- `paper/proof_of_rh.tex:567-598` for `\Phi_K(A_{\val})=0`
- `paper/proof_of_rh.tex:856-946` for denominator comparability and omitted-smooth holomorphy
- `paper/proof_of_rh.tex:1392-1457` for corrected finite-`s` holomorphic whitening
- `paper/proof_of_rh.tex:1497-1622` for corrected local decomposition
- `paper/proof_of_rh.tex:1624-1683` for cutoff compatibility
- `paper/proof_of_rh.tex:1693-2048` for preserved post-`\Phi_K` transfer scale
- `paper/proof_of_rh.tex:2050-2210` for the sharpened calibration remainder and the `S_2=o(xQ^2S(m))` dominance template
- `paper/proof_of_rh.tex:2212-2292` for the boundary estimate and its proof
- `paper/proof_of_rh.tex:2294-2321` for the odd holomorphic expansion derived from the boundary estimate

## Dependencies

- corrected-whitening bundle: denominator comparability, holomorphic/positive corrected whitening, preserved post-`\Phi_K` transfer scale
- transverse-slot realization for the family
- cutoff-internalization of auxiliary/tail/error terms into the corrected scalar
- transverse value-channel cancellation in the realized slot
- boundary domination comparing `S_2` to `L(m)S(m)^2`

## Strongest objection

One could argue that the paper already states the boundary estimate immediately after corrected whitening, so calling it the next theorem is only a matter of presentation. The objection is real. The reason I still reject that packaging as the right transport target is that the proof itself uses inputs outside the narrow whitening bundle, and the transport notes explicitly separate those inputs. So the issue is not order of exposition but theorem granularity.

## Needed for promotion

- Isolate a family-level theorem whose hypotheses explicitly include: realized corrected odd/transverse scalar, cutoff-internalization of the full corrected object, transverse value-channel cancellation, and boundary domination.
- Prove that theorem in one package, or split it into two packages with a hard interface: `realization + slot cancellation` and `boundary domination`.
- Only after that treat the odd Cauchy coefficient bounds and `N`-point projector step as transported.
- Do not claim that corrected whitening alone implies the boundary theorem.

Honest verdict: as a transport target, the boundary theorem is downstream of corrected whitening but is not the right next standalone theorem. The right next target is the combined corrected transverse realization-and-boundary package.
