# Claim

On the residual exact fixed-shear corner \(\{S=0\}\cap\{K_v=0\}\), Bottleneck B reduces to a single diagonal-extension statement for the actual corrected cubic/quintic defect germ. More precisely: if along the involutive branch \((h_1,h_2)=(h(t),h(-t))\) the actual corrected defects admit a descended germ
\[
E_{12}^{(3)}(t)=\mathcal E_3(a_1(t),a_2(t),u(t)),\qquad
E_{12}^{(5)}(t)=\mathcal E_5(a_1(t),a_2(t),u(t)),\qquad u=t^2,
\]
with \(\mathcal E_3\) and \(\mathcal E_5\) continuous/analytic at the merged state \(u=0\), and with diagonal value
\[
\mathcal E_3(a_1,a_2,0)=\mathcal E_5(a_1,a_2,0)=0,
\]
then swap-evenness is automatic and the residual corner closes by the existing fixed-shear criterion. So the single narrowest exact blocker is proving this diagonal value-zero / diagonal-collapse statement for the actual corrected defect package on the involutive quotient branch.

# Status

heuristic

# Evidence

- The draft already compresses the residual corner to the involutive quotient branch: every finite parity-normalized transport jet descends to the quotient variable \(u=t^2\); on the quartic--sextic rung every finite quotient-visible transport state is locally a function of the single scalar \(Q\); and no third local reset survives beyond \(t\leftrightarrow -t\).
- Proposition `conditional-state-local-defect-closure-fixed-shear-corner` already proves the needed implication: if the actual corrected cubic/quintic defects are analytic functionals of the descended transport state and vanish at the diagonal state, then they are \(O(t^2)\), hence \(O((h_1-h_2)^2)\), and the bad branch is excluded on compact good patches.
- Corollary `package-level-reduction-residual-fixed-shear-corner` shows the package theorem itself needs only two inputs: swap invariance along the involutive branch and vanishing on coincident atoms.
- Once the branch is written through the quotient variable \(u=t^2\), swap invariance is not an extra burden: any descended germ in \(u\) is automatically even in \(t\). What remains is the diagonal value at \(u=0\).
- This matches the older weaker exact route: Proposition `conditional-exact-two-point-exclusion-qabs` reduces exact two-point exclusion to continuity plus diagonal collapse of the actual corrected two-atom quotient germ. Bottleneck B is the fixed-shear specialization of that same diagonal-collapse issue.

# Exact refs

- `paper/proof_of_rh.tex:12042-12137` — weaker exact route via continuity + diagonal collapse of the actual corrected two-atom quotient germ.
- `paper/proof_of_rh.tex:12447-12510` — blown-up swap-even/diagonal-vanishing package shape for actual corrected defects.
- `paper/proof_of_rh.tex:12537-12555` — residual corner reduced to quotient-diagonal closure / package theorem / coincidence theorem.
- `paper/proof_of_rh.tex:21740-21763` — quotient descent, rank-one transport state, no hidden reset, and the explicit statement that any remaining obstruction is relational/provenance-sensitive.
- `paper/proof_of_rh.tex:22409-22505` — state-local defect closure and stronger package collapse on the involutive branch.
- `paper/proof_of_rh.tex:22966-23109` — residual involutive defect criterion and package-level reduction to swap-evenness + coincidence vanishing.
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:90-106` — Bottleneck B target statement.
- `paper/tasks/20260424-090000-other-uv002-fundamental/reports/coordinator-current-convergence.md:23-27,61-63` — current convergence that the blocker is package-side coincidence, not extractor-side algebra.

# Dependencies

- A definition of the actual corrected cubic/quintic defect germ on normalized two-atom data that remains meaningful on the involutive quotient branch.
- Continuity or analyticity of that defect germ at the merged state \(u=0\).
- A diagonal-collapse / coincidence-vanishing identity for the actual corrected package at coincident atoms.

# Strongest objection

The reduction above does not prove that the actual corrected package really descends to the quotient-visible state. The live possibility left by the draft is that the defect germ depends on genuinely relational or provenance-sensitive two-atom data that survives after quotient transport descent. If so, diagonal value-zero is not formal from \(u=t^2\) alone.

# Needed for promotion

1. Prove that the actual corrected cubic/quintic defects on the involutive fixed-shear branch extend as a continuous or analytic germ in the descended quotient-diagonal state up to \(u=0\).
2. Prove diagonal collapse at coincidence: at merged atoms the corrected two-atom defect equals zero (or equivalently the corrected two-atom package merges to the one-atom package with zero interaction defect).
3. Then invoke `prop:residual-involutive-defect-criterion-fixed-shear-corner` or `prop:conditional-state-local-defect-closure-fixed-shear-corner` to exclude the residual corner.

Honest verdict: the transport side is already compressed as far as it needs to go for Bottleneck B. The narrow live blocker is not another fixed-shear classification lemma; it is the exact diagonal value-zero / diagonal-collapse theorem for the actual corrected cubic/quintic defect germ on the involutive quotient branch.
