# Claim

The current `A_{\val}` transport conclusion is not yet safely scoped if it is stated as a whole transported "package." From current scope alone, the strongest defensible statement is narrower:

conditional on a target family having the same symmetric constant-background local jet model and a family-level corrected holomorphic whitening/decomposition theorem, the explicit first-order value-channel matrix `A_{\val}` and the identity `\Phi_K(A_{\val})=0` transport as local algebra. What does **not** follow from current scope alone is that exact slot identification by itself transports the corrected decomposition `\Delta=S(m)A_{\val}+R`, the calibration denominator, the calibrated identity `\Psi_{x,d}(\Delta)=c_{x,d}(x/B)S+\Psi_{x,d}(R)`, or the remainder-dominance / odd-transverse consequences.

So the transport statement is only safe when split into three bins:

- proved: inside the manuscript's constant-background local algebra, `A_{\val}` is explicit, `\Phi_K(A_{\val})=0`, and `\|A_{\val}(x)\|_\F\asymp x/B` for small `x`.
- conditional on [same local jet algebra + family-level corrected whitening/decomposition]: the family has a first-order value-channel term with the same `A_{\val}` profile.
- missing: any theorem that exact slot identification alone yields the corrected decomposition, any compatible family anomaly matrix and denominator lower bound, and any quantitative remainder control needed for calibration or the odd/transverse chain.

# Status

open

# Evidence

The manuscript's proved core is genuinely local. Proposition `prop:explicit-Aval` derives `A_{\val}` by differentiating the symmetric constant-background whitened jet block with respect to a scalar value perturbation while all derivative/curvature data are frozen (`paper/proof_of_rh.tex:446-565`). Corollary `cor:PhiK-Aval-zero` and Lemma `lem:Aval-small-x` are immediate consequences of that explicit matrix formula (`paper/proof_of_rh.tex:567-659`). These pieces are portable only to the extent that another family realizes the same local algebraic model.

The first overreach appears at the decomposition step. In the draft, `\Delta_\zeta=S(m)A_{\val}+R_\zeta` is not obtained from exact slot identification alone; it is stated only after the family-specific corrected finite-`s` holomorphic whitening and corrected local deformation have been built (`paper/proof_of_rh.tex:1392-1458,1497-1622`). The proof explicitly expands the analytic whitening map around the background value-channel parameter and identifies the first-order coefficient there (`paper/proof_of_rh.tex:1569-1606`). That is stronger than merely knowing an exact downstairs slot scalar. Route A blurs this distinction when it says the linear leading-term decomposition comes once the coefficient slot is exact. Route B is closer to the safe reading: the decomposition itself is a separate theorem burden.

The second overreach is the calibration functional. In the manuscript, `\Psi_{x,d}` is defined using the toy anomaly matrix `M(d)` and the denominator `\langle A_{\val}(x),M(d)\rangle_\F` (`paper/proof_of_rh.tex:661-794`). Transporting this requires more than the `A_{\val}` formula: one needs a compatible family anomaly matrix in the same coordinates, a nonvanishing denominator statement, and uniformity for small `x`. None of that follows from exact slot identification from current scope alone. The variable-`x` remark makes this explicit even in the zeta draft itself: the calibration chain is still conditional on a uniform variable-`x` rewrite (`paper/proof_of_rh.tex:5500-5598`). So route A's wording that the "formal calibration identities" transport once the anomaly matrix is fixed is too loose unless it is clearly labeled as a separate additional hypothesis, not part of the automatic post-slot package.

The third overreach is any implication toward transverse or remainder conclusions. The separate remainder note says only that after exact scalar-slot identification, remainder dominance is the next bottleneck for the calibrated value-channel subchain (`grh/.../remainder_dominance.md:8-38`). The draft proves that the calibrated remainder bound needs the additional quantitative hypothesis `S_2=o(xQ^2S(m))` (`paper/proof_of_rh.tex:2050-2209`). Separately, the odd/transverse channel uses `\Phi_K(A_{\val})=0` only to remove the leading value channel; the actual boundary estimate and odd expansion still depend on the corrected transfer and boundary control (`paper/proof_of_rh.tex:2214-2321`). So `A_{\val}` transport does not carry the later zeta-side consequences except in the very weak sense that it identifies the piece that disappears under `\Phi_K`.

Therefore the safe scope is: `A_{\val}` transport is a local first-order interface statement, not a transported calibration/remainder/transverse package.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:16-37`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-38`
- `tasks/20260423-202340-attack-gap-aval-transport/reports/gap-aval-transport-routeA.md:9-18`
- `tasks/20260423-202340-attack-gap-aval-transport/reports/gap-aval-transport-routeB.md:5-33`
- `paper/proof_of_rh.tex:446-565` for the explicit constant-background derivation of `A_{\val}`
- `paper/proof_of_rh.tex:567-599` for `\Phi_K(A_{\val})=0`
- `paper/proof_of_rh.tex:601-659` for the small-`x` size law
- `paper/proof_of_rh.tex:661-794` for the calibration functional and its dependence on the anomaly denominator
- `paper/proof_of_rh.tex:1392-1458` for corrected finite-`s` holomorphic whitening
- `paper/proof_of_rh.tex:1497-1622` for the corrected local decomposition and identification of the first-order coefficient through analytic whitening
- `paper/proof_of_rh.tex:2050-2209` for the sharpened calibrated remainder estimate and the extra hypothesis `S_2=o(xQ^2S(m))`
- `paper/proof_of_rh.tex:2214-2321` for the odd/transverse channel, showing only the leading value channel is annihilated automatically
- `paper/proof_of_rh.tex:5500-5598` for the variable-`x` caveat still open even in the zeta draft

# Dependencies

- A precise separation between three claims: explicit local `A_{\val}` formula, corrected decomposition theorem, and calibrated / transverse consequences.
- A family-level analogue of corrected finite-`s` holomorphic whitening, not just an exact downstairs scalar slot.
- A family-level theorem that the first-order coefficient in the corrected whitened deformation is exactly the intended slot scalar.
- A compatible family anomaly matrix and a denominator lower bound if one wants any transported `\Psi_{x,d}` statement.
- Separate quantitative remainder and odd/transverse estimates if one wants anything beyond the first-order interface.

# Strongest objection

The strongest objection to the current transport conclusion is that it silently upgrades a local algebra computation into a family theorem. In the manuscript, `A_{\val}` is computed in a very specific symmetric constant-background model, while the corrected decomposition and the calibrated remainder statements come only after additional holomorphic whitening, transfer, and denominator inputs. From current scope alone, exact slot identification does not force those extra inputs. So any wording that says or implies "after exact slot identification, the `A_{\val}` package transports" is too strong unless "package" is cut back to the explicit first-order value-channel matrix and its immediate local identities.

# Needed for promotion

- Weaken any statement of automatic transport to: `after family-level realization of the same local model and corrected decomposition, the first-order value-channel matrix is the same explicit A_val and is annihilated by Phi_K`.
- Remove or weaken any wording that presents `\Delta=S(m)A_{\val}+R` as following from exact slot identification alone; require a separate family-level corrected whitening/decomposition theorem.
- Remove or weaken any wording that includes calibration identities in the automatic transport package; if retained, label them conditional on a compatible family anomaly matrix, denominator nonvanishing, and the same local coordinate model.
- Remove or weaken any wording that suggests remainder dominance, boundary control, odd/transverse expansion, or endgame-facing consequences come with `A_{\val}` transport.
- If a single roadmap sentence is wanted now, the safest version is: `After exact slot identification and a family-level corrected local decomposition in the same symmetric normal form, the explicit first-order value-channel matrix A_{\val} and the cancellation \Phi_K(A_{\val})=0 transport; calibration, remainder dominance, and odd/transverse control remain separate theorem burdens.`

Honest verdict: the transport statement is not safely scoped if it is read as a transported `A_{\val}` package. The safe core is only the explicit first-order local interface. The decomposition, calibration, and remainder/transverse consequences need weakening or explicit additional hypotheses.
