Claim

[confirmed] The `\Phi_K`-visible hidden state is geometrically the choice of an affine lift of the canonical quotient-level order-`7` class inside the fixed-sector plane `\mathfrak f=\operatorname{span}\{I,S\}`. More concretely: once `A_5^{\mathfrak f}=u_5I+v_5S` is fixed, the raw septic representative `A_7^{\mathfrak f}` is defined only up to translation by the line `\mathbf C A_5^{\mathfrak f}`, while `\Phi_K` reads the `S`-component. Therefore the residual hidden scalar is not a mysterious extra invariant; it is the coordinate of a lift along the quintic line, and Bottleneck D must show that the first surviving odd coefficient is independent of that lift, equivalently that package differences along a corrected reduced-package fiber land in `\ker\Phi_K=\mathbf C I\oplus\mathbf C D\oplus\mathbf C K` through the first surviving odd order.

[conditional on `v_5\neq 0`] The hidden scalar is not removable by quotient geometry alone: translation by `c_2A_5^{\mathfrak f}` changes the `\Phi_K`-visible component by `c_2v_5`, so on any patch where `v_5` is nonzero the quotient package `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` does not by itself determine the visible septic coordinate.

[candidate] The right conceptual formulation of D is a descent/section theorem: either there is a canonical `\Phi_K`-compatible section of the affine line bundle of septic lifts over corrected reduced-package fibers, or the corrected transport law forces the first visible odd jet to descend without choosing a section. In either form, the hidden state should be treated as affine-bundle geometry over the reduced package, not as an extra independent field.

Status

heuristic

Evidence

- [confirmed] `\Phi_K(X)=x_{12}+x_{21}` is exactly the `S`-coefficient extractor in the basis `I,D,S,K`, so `\ker\Phi_K=\mathbf C I\oplus\mathbf C D\oplus\mathbf C K`.
- [confirmed] The paper already identifies the canonical order-`7` datum as the quotient class `[A_7^{\mathfrak f}]\in \mathfrak f/\mathbf C A_5^{\mathfrak f}`, equivalently the determinant `\Delta_7=u_7v_5-u_5v_7`; raw representatives `(u_7,v_7)` are non-canonical.
- [confirmed] The projected septic gauge law is translation
  \[
  A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+c_2A_5^{\mathfrak f}.
  \]
  So the hidden freedom is exactly motion parallel to the quintic line.
- [confirmed] Applying `\Phi_K` to that translation changes the visible scalar by `c_2v_5`. Hence quotienting by `\mathbf C A_5^{\mathfrak f}` does not automatically kill `\Phi_K`-visibility.
- [conditional on Bottleneck C] Once the corrected reduced package is canonically identified with `\widehat\Psi` on the exceptional divisor, D becomes the statement that the affine lift-coordinate cannot vary in any `\Phi_K`-visible way along a corrected reduced-package fiber through the first surviving odd order.
- [candidate] This suggests a redirect: prove that corrected coincidence packages carry a natural connection/transport law whose holonomy along reduced-package fibers lies in `\ker\Phi_K`, rather than trying to prove raw representative equality.

Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:406-415` — definition of `\Phi_K`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7004-7062` — fixed-sector quintic/septic package, quotient-level order-`7` datum, non-canonicity of raw septic representatives.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7065-7191` — projected septic gauge law and gauge invariance of `\Delta_7`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11368-11408` — amplitude-invariant strengthened datum `\widehat\Psi`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:2214-2307` — corrected transverse scalar `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))` and its odd expansion.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:23123-23155` — basis `I,D,S,K` for scalar extraction.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:24985-25030` and `26369-26398` — current endgame split and statement that the remaining burden is package-to-first-nonzero-odd-jet.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-kerphik-hidden-state/report.md:1-90` — prior sharp theorem target for D.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-hidden-state-geometry/notes/geometry-summary.md` — local derivation notes for the affine-line interpretation.

Dependencies

- The fixed-sector basis and septic gauge law already in the paper.
- Bottleneck C to canonically identify the corrected reduced package on the exceptional divisor with `\widehat\Psi(m)`.
- A corrected package-to-transform comparison theorem strong enough to control lift variation through the first surviving odd order.

Strongest objection

This geometric reinterpretation does not prove that the affine lift-coordinate is actually constrained by the corrected two-atom package. The hidden line could still carry genuine `\Phi_K`-visible variation unless an additional transport, symmetry, or functoriality theorem kills it. So the affine-bundle picture sharpens what must be shown, but does not itself close D.

Needed for promotion

1. Formulate the corrected order-`7` package over a fixed reduced-package fiber as an affine line of lifts parallel to `\mathbf C A_5^{\mathfrak f}`.
2. Prove that the corrected package-to-transform map sends differences of lifts in a common fiber to `\ker\Phi_K` through order `2N-1`, or equivalently that the first visible odd coefficient is constant on that fiber.
3. If direct constancy is too hard, isolate the smallest missing statement as a transport/holonomy lemma for the affine lift line.

Honest verdict: the hidden `\Phi_K`-visible scalar looks canonical only after one more theorem. What is already clear is the geometry: the residual state is an affine lift-coordinate along the quintic line inside the fixed-sector plane, not a new primitive field. That redirects D toward an affine-bundle descent theorem or a `\ker\Phi_K`-valued transport law, and away from trying to read the first visible odd jet from `\widehat\Psi` alone.