# Claim

Assume two inputs are available in the new family: 

1. a family source theorem for the corrected local deformation; and
2. exact identification of the family scalar occupying the manuscript's `S(m)` slot.

Even under those assumptions, the odd package does not yet transport. The smallest additional family-specific theorem still needed is a **family corrected transverse realization-and-boundary theorem**:

- in one chosen real critical-line channel, the corrected same-point and mixed blocks admit the same microscopic holomorphic whitening setup on `|s|<\rho_0/Q`;
- after applying the universal scalar functional `\Phi_K`, the resulting corrected transverse scalar `H_{m,\mathcal F}(s)` is odd and holomorphic;
- on the microscopic boundary `|s|=\rho_0/Q`, one has the family analogue of the zeta bound `|H_{m,\mathcal F}(s)| \ll Q^{-3}` times the appropriate family amplitude scale.

With that theorem in hand, the coefficient bounds are immediate by Cauchy, and the `N`-point odd projector transports without new family work. Without it, the odd/transverse package is still open.

# Status

open

# Evidence

Proved:

- The abstract Layer-1 theorem is already isolated in `notes/local_package_theorem.md`: once a real odd holomorphic scalar with microscopic boundary control exists, the draft supplies the odd expansion, Cauchy coefficient bounds, and the universal `N`-point projector.
- In the manuscript, `paper/proof_of_rh.tex:2294-2322` derives coefficient bounds entirely from odd holomorphy plus the boundary estimate. Nothing family-specific enters after those hypotheses are granted.
- The discrete projector in `paper/proof_of_rh.tex:2975-3169` is purely algebraic in the coefficients `a_j^{(N)}`. It is an operator on odd analytic germs, not a zeta-specific theorem.

Conditional on the assumed source theorem and exact scalar-slot identification:

- The leading-channel decomposition itself is no longer the blocker. `notes/positive_s_implication.md:17-24` says no second theorem of the form `\Delta = S A_{\val} + R` is needed once the exact scalar slot is identified.
- Remainder dominance then becomes the next bottleneck only for the calibrated value-channel subchain, not for the odd package as such. `notes/remainder_dominance.md:8-18,34-38` states this explicitly.

Missing:

- The manuscript's odd package starts at `paper/proof_of_rh.tex:2212-2322`, but its proof uses a zeta-specific corrected-whitening and tail-curvature/boundary chain. In particular, `paper/proof_of_rh.tex:2235-2292` proves the boundary estimate by combining corrected local decomposition, cutoff compatibility, `\Phi_K(A_{\val})=0`, and the zeta corrected transfer bound `S_2\ll L(m)S(m)^2`.
- The deeper coefficient-localization machinery in `paper/proof_of_rh.tex:2415-2910` is also family-sensitive. It uses the zeta one-pair kernel decomposition, shell counting, and exterior-zero bookkeeping to prove odd-coefficient decay. Those arguments do not transport from local algebra alone.
- The optimized cancellation depth `paper/proof_of_rh.tex:4215-4248` is therefore not available from the projector alone; it also needs family input controlling the surviving odd coefficients.

So the true missing theorem is not "coefficient bounds" and not "projector". It is the family theorem that realizes the corrected odd scalar with the required microscopic holomorphy, oddness, whitening gain, and boundary scale. The later coefficient and projector steps then follow formally.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-42`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-18,27-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:28-37,55-70`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:23-48`
- `paper/proof_of_rh.tex:2212-2322`
- `paper/proof_of_rh.tex:2415-2910`
- `paper/proof_of_rh.tex:2975-3169`
- `paper/proof_of_rh.tex:4215-4248`
- `paper/proof_of_rh.tex:1548-1683`

# Dependencies

- A chosen real critical-line family channel.
- Family-specific corrected local same-point and mixed-block formulas.
- Microscopic denominator comparability and a holomorphy radius of size `\rho_0/Q` in that channel.
- A corrected-whitening theorem with the same scale hierarchy needed to define `H_{m,\mathcal F}`.
- A family boundary estimate showing the corrected transverse scalar is `O(Q^{-3} \times \text{family amplitude})` on `|s|=\rho_0/Q`.

# Strongest objection

This may still understate the missing input. Oddness itself is not automatic in new families, especially for complex Dirichlet channels. If the family does not furnish a one-channel real involution matching the manuscript's `s \mapsto -s` symmetry and `\Phi_K(J_0 X J_0) = -\Phi_K(X)` mechanism, then even the proposed realization-and-boundary theorem is not enough. In that case the missing theorem must be strengthened to a full channel-symmetry theorem proving that the scalar functional and oddness mechanism survive in the chosen family channel.

# Needed for promotion

- State and prove a family theorem with hypotheses and conclusion in the Layer-1 form:
  `H_{m,\mathcal F}(s) = \Phi_K(\widehat\Omega^{\corr}_{\mathcal F}(s;m))` is real on the critical line, odd, and holomorphic on `|s|<\rho_0/Q`, with `|H_{m,\mathcal F}(s)| \ll Q^{-3}` times the family amplitude scale on `|s|=\rho_0/Q`.
- Make explicit which parts are family-specific:
  boundary estimate, denominator comparability, corrected-whitening gain, and possibly channel oddness.
- Mark as universal consequences once that theorem is available:
  Cauchy coefficient bounds from `paper/proof_of_rh.tex:2294-2322` and the projector package from `paper/proof_of_rh.tex:2975-3169`.
- Keep the calibrated value-channel subchain separate: remainder dominance is still an independent theorem after exact scalar-slot identification.

Honest verdict: after exact scalar-slot identification, the odd package is still blocked by one family-specific realization theorem for the corrected odd transverse scalar with microscopic whitening and `Q^{-3}` boundary control. The coefficient and projector pieces are already universal once that theorem exists.
