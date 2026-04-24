## Claim

On Bottleneck B, the exact fixed-shear package problem can be sharpened to one narrow diagonal input. Along the involutive branch \
\[
(h_1,h_2)=(h(t),h(-t)),
\]
swap-evenness of the actual corrected cubic/quintic defects is formal once those defects are extracted functorially from an atom-symmetric two-atom package, because atom swap is exactly \
\(t\mapsto -t\) on the repeated-value locus. The only remaining non-formal package input needed to fire the existing closure theorem is diagonal merger at coincidence, equivalently
\[
E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0
\]
for the actual corrected defects. A sufficient theorem shape is: the actual corrected two-atom package satisfies the exact diagonal law
\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h
\]
at coincidence. Then the extracted cubic/quintic interaction defects vanish on the diagonal, and Corollary `cor:package-level-reduction-residual-fixed-shear-corner` closes the residual exact fixed-shear corner.

## Status

heuristic

## Evidence

- The residual corner has already been reduced to package inputs: Proposition `prop:residual-involutive-defect-criterion-fixed-shear-corner` and Corollary `cor:package-level-reduction-residual-fixed-shear-corner` say it is enough to prove swap invariance along the involutive branch and vanishing on coincident atoms.
- On that branch, the local repeated-value locus is exactly \
  \((t,-t)\), so atom swap is the involution itself; any atom-symmetric package therefore yields even pulled-back defects in `t`.
- The earlier finite-order package lemma shows that once one has one-amplitude collapse plus the exact diagonal merger law
  \
  \(\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h\), the interaction remainder is divisible by \
  \(a_1a_2(h_1-h_2)^2\). This is stronger than mere diagonal vanishing and is exactly the kind of package statement Bottleneck B needs.
- The draft itself says the naive source-summed corrected block model does not supply the required linear merger law, so the obstruction is not transport classification or swap parity; it is this exact coincidence law for the actual corrected package.

## Exact refs

- `paper/proof_of_rh.tex:11888-11930`
- `paper/proof_of_rh.tex:12385-12510`
- `paper/proof_of_rh.tex:21736-21763`
- `paper/proof_of_rh.tex:21808-21850`
- `paper/proof_of_rh.tex:22409-22505`
- `paper/proof_of_rh.tex:22966-23109`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:24-29`

## Dependencies

- The actual corrected cubic/quintic defects must arise functorially from an atom-symmetric two-atom package.
- The extraction from that package to the displayed defects must respect coincidence evaluation.
- No stronger state-locality hypothesis is needed for this reduction; only the exact diagonal merger/vanishing input is.

## Strongest objection

The functorial passage from the full actual corrected two-atom package to the specific displayed defects `E_{12}^{(3)}` and `E_{12}^{(5)}` is not written as a theorem in the exact fixed-shear section. Without that explicit extraction statement, one cannot yet promote the diagonal package identity to diagonal value-zero for the named defects purely formally.

## Needed for promotion

1. State the actual corrected two-atom package theorem with explicit atom symmetry.
2. Prove the exact coincidence law
   \
   \(\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h\)
   for that package, or prove directly that the extracted defects satisfy `E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0`.
3. Add the short extraction lemma saying package symmetry on the involutive branch gives `t`-evenness of `E_{12}^{(3)}` and `E_{12}^{(5)}`.
4. Then invoke Corollary `cor:package-level-reduction-residual-fixed-shear-corner`.

Honest verdict: the single narrowest exact blocker for Bottleneck B is no longer generic state-locality. It is the diagonal coincidence law for the actual corrected two-atom package, i.e. proving that the extracted cubic/quintic defect germ vanishes at coincidence on the involutive fixed-shear branch.
