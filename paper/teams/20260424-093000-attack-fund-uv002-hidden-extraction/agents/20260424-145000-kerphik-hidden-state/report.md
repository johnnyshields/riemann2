## Claim

The cleanest Bottleneck D statement is a transform-level hidden-state theorem.

Let `\mathcal P_1,\mathcal P_2` be two corrected finite-core coincidence-package germs over the same base point `m`, and assume they lie in the same corrected reduced-package fiber (after Bottleneck C, this means they determine the same reduced coincidence germ, equivalently the same reduced `\widehat\Psi`-state on the exceptional divisor). Let

```tex
\Delta\widehat\Omega(s):=\widehat\Omega^{\corr}_{\mathcal P_1}(s;m)-\widehat\Omega^{\corr}_{\mathcal P_2}(s;m)
=\sum_{r\ge 0}\Delta A_{2r+1}(m)\,s^{2r+1}.
```

Write

```tex
\ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K,
\qquad
\Phi_K(S)=2,
```

so the first `\Phi_K`-visible direction is the symmetric off-diagonal `S`-line. Then the hidden-state theorem should assert:

```tex
\Delta A_{2r+1}(m)\in \ker\Phi_K
\qquad (0\le r\le N-1),
```

where `2N-1` is the first surviving odd order of either package. Equivalently,

```tex
\Phi_K\bigl(\Delta\widehat\Omega(s)\bigr)=O\bigl(s^{2N+1}\bigr),
```

so the corrected transverse scalars have the same first surviving odd order and the same leading odd coefficient:

```tex
H_{\mathcal P_1}(s)-H_{\mathcal P_2}(s)=O\bigl(s^{2N+1}\bigr),
\qquad
c^{(\mathcal P_1)}_{2N-1}(m)=c^{(\mathcal P_2)}_{2N-1}(m).
```

By the existing odd-jet extractor, this is equivalent to saying that the minimal `N` for which `\Xi^{(N)}_{\zeta,\le H}(m)` is nonzero, and the value of that first nonzero transformed scalar, are constant on corrected reduced-package fibers.

## Status

heuristic

## Evidence

- `\Phi_K` is exactly the symmetric off-diagonal functional, so its kernel is the three-dimensional span of the diagonal/value directions and the antisymmetric off-diagonal shear direction.
- The zeta-side scalar is already defined as `H_m(s)=\Phi_K(\widehat\Omega^{\corr}_\zeta(s;m))`, and its odd Taylor coefficients `c_{2r+1}(m)` are already extracted canonically.
- The existing `N`-point machinery already shows that the first nonzero `\Xi_\zeta^{(N)}` is exactly the first surviving odd coefficient in transformed form.
- The one-pair package side already identifies the reduced package `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` and the septic gauge law `A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+c_2A_5^{\mathfrak f}`; this is exactly why Bottleneck D must be phrased modulo `\ker\Phi_K` rather than as literal raw-coefficient equality.
- Since `\Delta_7` is gauge-invariant but the raw septic representative is not, the right invariant conclusion is not equality of raw odd blocks, but equality after forgetting the `\Phi_K`-invisible directions through the first surviving odd order.

## Exact refs

- `paper/proof_of_rh.tex:406-423` (`\Phi_K` definition and toy visibility)
- `paper/proof_of_rh.tex:2214-2307` (`H_m`, oddness, and odd Taylor expansion)
- `paper/proof_of_rh.tex:2953-2969` (finite-core localization of the first surviving odd coefficient)
- `paper/proof_of_rh.tex:3984-4190` (exact surviving expansion and finite-core localization of `\Xi_\zeta^{(N)}`)
- `paper/proof_of_rh.tex:6988-7190` (fixed-sector basis, `A_5^{\mathfrak f}`, `A_7^{\mathfrak f}`, `\Delta_7`, septic gauge law)
- `paper/proof_of_rh.tex:11399-11408` (definition of `\widehat\Psi`)
- `paper/proof_of_rh.tex:23123-23155` (`I,D,S,K` basis used for coefficient extraction)
- `paper/proof_of_rh.tex:24985-25030` (current endgame split; package theorem before hidden extraction)
- `paper/proof_of_rh.tex:26369-26398` (finite-core branch must use the first nonzero odd jet)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:79-168`

## Dependencies

- Bottleneck C in its sharp form: corrected reduced-package coincidence / diagonal collapse.
- A precise notion of corrected reduced-package fiber for the actual two-atom package.
- The already-built odd-jet and `N`-point extractor machinery on the zeta side.

## Strongest objection

The present draft does not yet prove that bare reduced `\widehat\Psi` fibers kill every hidden `\Phi_K`-visible septic mode. The gauge law

```tex
A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}
```

shows a one-dimensional hidden septic direction, and on raw representatives its `S`-component is generically visible to `\Phi_K`. So the statement above is the right theorem target, but it is not yet proved from the current reduced-package algebra alone.

## Needed for promotion

1. Define the corrected reduced-package fiber canonically for the actual coincidence package after Bottleneck C.
2. Prove that two packages in the same fiber have odd corrected-block difference in `\ker\Phi_K` through order `2N-1`.
3. Invoke the existing `H_m` / `\Xi_{\zeta,\le H}^{(N)}` extraction machinery to conclude fiber-constancy of the first nonzero transformed scalar.

Honest verdict: the clean theorem statement is now sharp. The right conclusion is not raw package equality, but equality modulo `\ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K` through the first surviving odd order, equivalently constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on corrected reduced-package fibers. The blocker is proving that the hidden septic gauge direction contributes no extra `\Phi_K`-visible state beyond that fiber.
