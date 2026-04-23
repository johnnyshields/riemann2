# Claim

The smallest honest list is:

1. `paper/proof_of_rh.tex:285-299` introduces the scalar zeta amplitude `S(m)` as a real background-subtracted value scale and immediately uses its positivity inside `L(m)=\log(3+|m|+1/S(m))` and its size inside the curvature bound `|S''(m)|\ll L(m)S(m)^2`.
2. `paper/proof_of_rh.tex:1540-1621`, `739-779`, and `2050-2209` use that same scalar as the coefficient of the distinguished value-channel derivative `A_{\val}` and then calibrate against the toy parameter by `u^2\asymp (x/B_\zeta(m))S(m)` after proving the remainder is smaller than the leading scalar term.
3. `paper/proof_of_rh.tex:26561-26608` uses the calibrated quantity `(x_0/B_\zeta(m))S(m)` as the toy-side lower scale in the final contradiction. Without a real nonnegative amplitude in the realized channel, this comparison does not close in the form written.

For a primitive Dirichlet realization, the replacement for `S(m)` cannot be just a complex critical-line value or an arbitrary complex phase derivative. It would have to be a real scalar amplitude `A_\chi(m)` attached to a chosen local channel such that:

- `A_\chi(m)` is real on the critical line;
- `A_\chi(m)` has sign compatible with the toy quantity `u^2` after whatever normalization/rotation defines the channel, ideally `A_\chi(m)\ge 0` on the admissible range;
- the corrected local deformation splits as `\Delta_\chi=A_\chi(m)A_{\val,\chi}+R_\chi` in the same one-dimensional direction;
- the projector/calibration functional sees that channel with nonvanishing real leading coefficient;
- the remainder is `o((x/B_\chi)A_\chi(m))`;
- the odd transverse scalar built after killing the value channel still satisfies a boundary bound of size `\ll L_\chi(m)A_\chi(m)^2/Q_\chi^3` or equivalent conductor-scaled form.

This is not proved in the current draft for Dirichlet families.

# Status

open

# Evidence

Proved from the current draft:

- The local odd-germ package itself is source-light once a channel has already been realized. In `2214-2322`, `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))` kills the leading value channel and only uses the size bound `|H_m(s)|\ll L(m)S(m)^2/Q^3`. This is a boundary-size statement, not a sign statement.
- The corrected local deformation is explicitly linearized in one scalar parameter at `S(m)=0`: `\Delta_\zeta=S(m)A_{\val}+R_\zeta` (`1540-1621`). This isolates the exact interface a new family must reproduce.
- The calibration mechanism itself is formal once such a scalar exists: `739-779` and `2050-2209` show that if the leading coefficient is a real dominant scalar and the remainder is negligible, then the toy parameter obeys `u^2\asymp (x/B_\zeta(m))S(m)`.

Conditional on a new Dirichlet realization theorem:

- A primitive Dirichlet channel could replace `S(m)` if one first constructs a real critical-line object whose local deformation is one-dimensional in the relevant value direction and whose amplitude is sign compatible with `u^2`.
- The boundary estimate and odd-projector layer should then port formally, with `Q` replaced by conductor-scale logarithmic control, provided the same whitening and denominator comparability survive.

Missing:

- The draft gives no primitive-Dirichlet theorem identifying a real amplitude `A_\chi(m)` that plays the role of `S(m)`.
- The draft gives no proof that a Dirichlet analogue of the calibration scalar is nonnegative or even real in the actual channel used. For complex characters this is the main obstruction.
- The draft gives no Dirichlet analogue of the zeta-side curvature input `|S''(m)|\ll L(m)S(m)^2` in a channel that is simultaneously real and sign compatible.
- The draft gives no Dirichlet remainder theorem of the form `\Psi(R_\chi)=o((x/B_\chi)A_\chi(m))`.
- The final contradiction as written needs a lower scale comparable to `u^2`; a merely complex or sign-changing amplitude would require a different statement, not a direct substitution.

Smallest concrete unresolved sub-statements:

1. Define a primitive-Dirichlet critical-line scalar `A_\chi(m)` that is real for real `m` and natural enough to enter the local whitening package.
2. Prove a decomposition `\Delta_\chi(m,\sigma)=A_\chi(m)A_{\val,\chi}(m,\sigma)+R_\chi(m,\sigma)` with the same one-dimensional leading channel.
3. Produce a calibration functional `\Psi_{x,d,\chi}` for which the leading term is real with fixed sign and satisfies `\Psi_{x,d,\chi}(\Delta_\chi)=c_{x,d,\chi}(x/B_\chi)A_\chi(m)+\Psi_{x,d,\chi}(R_\chi)` with `c_{x,d,\chi}>0` after normalization.
4. Prove `\Psi_{x,d,\chi}(R_\chi)=o((x/B_\chi)A_\chi(m))`.
5. Prove the conductor-uniform boundary bound needed for the odd transverse scalar after the value channel is removed.

# Exact refs

- `paper/proof_of_rh.tex:271-299`.
- `paper/proof_of_rh.tex:661-737`.
- `paper/proof_of_rh.tex:739-850`.
- `paper/proof_of_rh.tex:1529-1621`.
- `paper/proof_of_rh.tex:2050-2209`.
- `paper/proof_of_rh.tex:2212-2322`.
- `paper/proof_of_rh.tex:26301-26551`.
- `paper/proof_of_rh.tex:26561-26608`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:11-18,35-67`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-42`.

# Dependencies

- The local package boundary recorded in `notes/local_package_theorem.md`.
- The GRH/Dirichlet synthesis conclusion that portability becomes real only after a completed-`L` realization package with a real sign-compatible amplitude.
- The current RH draft's zeta-specific scalar `S(m)` and its curvature/remainder estimates.

# Strongest objection

The current calibration theorem already suppresses phase information in a way that is harmless only because the zeta channel supplies a real scalar `S(m)` with positive local meaning. For primitive Dirichlet families, especially complex characters, there is no proved one-channel object in the draft whose leading coefficient is simultaneously real, sign compatible with `u^2`, and large enough to dominate the remainder. From this scope alone, direct replacement of `S(m)` by a Dirichlet quantity is unsupported.

# Needed for promotion

Promotion would need an actual primitive-Dirichlet realization theorem proving all of the following in one package:

1. a real critical-line amplitude `A_\chi(m)` in the chosen channel;
2. a curvature/boundary theory for that amplitude strong enough to yield the analogue of `L(m)S(m)^2`;
3. a leading-channel decomposition and remainder estimate at the calibration scale;
4. a normalization in which the calibrated leading coefficient is positive real, so that the comparison with `u^2` is honest;
5. a rewritten final contradiction in conductor language using that new amplitude.

Honest verdict: the draft's portable part starts after one already has a real sign-compatible scalar channel. The Dirichlet problem is exactly to build that channel. No such realization is proved here.
