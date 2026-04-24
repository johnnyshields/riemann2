## Claim

On a good overlap patch \(\{c\neq 0, v_5\neq 0\}\), the reduced secant/tangent package is only mildly sharper than the raw hidden-\(\lambda\)-shear package: it is the amplitude-invariant quotient of the raw projective defect data, and it removes exactly the obvious scalar-rescaling direction. It does **not** remove the live hidden-state obstruction beyond that, so most of the apparent sharpening is not a new theorem-level gain but a cleaner normalization.

## Status

proved

## Evidence

- The paper defines the raw mixed defect package by the projective class
  \([
  \delta(c):\delta(v_5):\delta(u_5):\delta(\lambda)
  ]\) on a good overlap patch.
- On the same patch it defines reduced coordinates
  \(x=v_5/c\), \(Y=u_5/c\), \(S=\lambda/c=\Delta_7/(cv_5)\).
- Linearizing the change of variables at a point with \(c\neq 0\) gives
  \[
  c\,\delta x=\delta v_5-x\,\delta c,\qquad
  c\,\delta Y=\delta u_5-Y\,\delta c,\qquad
  c\,\delta S=\delta\lambda-S\,\delta c.
  \]
  So the map
  \[
  (\delta c,\delta v_5,\delta u_5,\delta\lambda)\mapsto (\delta x,\delta Y,\delta S)
  \]
  has kernel exactly the scalar direction
  \((c,v_5,u_5,\lambda)\), i.e. common rescaling of the one-pair package.
- That scalar direction is already the redundancy singled out by the amplitude-invariant strengthened datum
  \(\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)\). Hence passing from raw to reduced package is the natural quotient by this already-visible normalization freedom.
- The secant-shadow formula confirms the same point globally: the projective shadow
  \[
  [x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1]
  \]
  is exactly the raw cross-determinantal package written in amplitude-invariant coordinates, not a new independent source of hidden-state control.
- Therefore the reduced package is genuinely more minimal, but only by modding out the trivial amplitude direction. It is not dramatically sharper than the raw hidden-\(\lambda\)-shear package in the sense needed for Extraction front D.

## Exact refs

- `paper/proof_of_rh.tex:11368-11449` — definition and scaling invariance of `\widehat\Psi`.
- `paper/proof_of_rh.tex:12257-12334` — raw projective moving-`\lambda`-shear defect package.
- `paper/proof_of_rh.tex:14216-14243` — reduced coordinates `(x,Y,S)` and tangent-contact package side.
- `paper/proof_of_rh.tex:20853-20924` — secant-shadow reduction and exact projective formula.
- `paper/proof_of_rh.tex:21692-21705` — route-status remark emphasizing the fully projective secant-shadow formulation.
- `paper/proof_of_rh.tex:24987-25029` — current endgame status placing `\widehat\Psi` and package-level coincidence at the center.

## Dependencies

- Work on a good overlap patch where \(c\neq 0\) and \(v_5\neq 0\).
- The comparison is between package states up to projectivization / local coincidence, not a claim about the full corrected block.

## Strongest objection

This comparison is at the level of package coordinates, not at the level of the actual corrected block entering \(H_m=\Phi_K(\widehat\Omega_\zeta^{\corr})\). A stronger theorem could still show that the reduced secant/tangent package interacts better with the corrected block than the raw package does. So this does not prove the reduced package is the final right hidden-state theorem target; it proves only that its apparent extra sharpness over the raw hidden-\(\lambda\)-shear package is mostly normalization-level.

## Needed for promotion

1. State the quotient explicitly in the draft: raw hidden-`\lambda` defect package modulo common scalar rescaling equals the reduced secant/tangent package on \(\{c\neq 0, v_5\neq 0\}\).
2. Then prove either that this quotient loses only `\Phi_K`-invisible directions through the first surviving odd order, or else enlarge the package further by the remaining `\Phi_K`-visible hidden mode.

Honest verdict: the reduced secant/tangent package is more minimal, but only by quotienting out the obvious amplitude gauge already implicit in `\widehat\Psi`. So it is only slightly sharper than the raw hidden-`\lambda`-shear package; the deeper hidden-state obstruction survives unchanged.
