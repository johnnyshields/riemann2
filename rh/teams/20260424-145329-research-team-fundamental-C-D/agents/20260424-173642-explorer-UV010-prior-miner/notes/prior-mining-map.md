# UV-010 Prior Mining Map

## Scope

Mined the prior UV-002 team, current team deposits, later summaries, and a narrow `rh/chats` search for:

- parked order-7 edge packages;
- quotient transport or moving-quotient repairs;
- `H_7` / `\mathcal H_7` analogues;
- hidden formulas relevant to UV-010.

No computational claim was made, so no script was needed.

## Confirmed Leads

1. **One-pair order-7 quotient closure is real, but it is not UV-010.**

   The prior team repeatedly confirms that the one-pair fixed-sector order-7 package is closed at the canonical quotient level: `A_7^{\mathfrak f}` is only meaningful modulo the quintic line, equivalently by `\Delta_7`. This is useful input for quotient conventions, but it does not construct the actual two-atom septic quotient edge defect.

   Exact refs:
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:38`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:40`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:49`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/handoff.md:87`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/handoff.md:89`
   - `rh/chats/20260418-202602-69e3e881-13f4-83e8-8804-ce366fbab3d3-tex-draft-audit.md:5834`
   - `rh/chats/20260418-202602-69e3e881-13f4-83e8-8804-ce366fbab3d3-tex-draft-audit.md:5877`

2. **The moving-quotient codomain repair is already parked.**

   Prior work noticed that a target like
   `\mathbf C \oplus \mathfrak f \oplus (\mathfrak f/\mathbf C A_5^{\mathfrak f})`
   is not literally fixed if the quotient line moves with \(h\). The parked repair is determinant scalarization: replace the quotient class by the gauge-invariant scalar `\Delta_7`, or for two-atom notation use
   `\Delta^{\corr}=\det(B,A^{\mathfrak f})`. This is a strong lead for UV-010 trivialization: on \(A_5^{\mathfrak f}(m)\neq0\), pair the moved quotient class with the midpoint \(A_5^{\mathfrak f}(m)\) to get a scalar test. It is not itself a formula for `\mathcal H_7^q`.

   Exact refs:
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/session-ses_246a.md:1572`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md:14`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-corrected-package-object/report.md:36`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-143000-reduced-package-object/report.md:58`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-115500-reduced-germ-definition/report.md:1`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-115500-reduced-germ-definition/report.md:111`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-explorer-corrected-package-object/report.md:29`

3. **The cubic/quintic edge-law template is the closest `H_7` analogue.**

   Prior and current summaries keep pointing to the same local template:
   `E_{12}^{(3)}=\delta^2\mathcal H_3` and
   `E_{12}^{(5)}=\delta^2\mathcal H_5`. The missing UV-010 object is exactly the analogous quotient-valued septic statement. No prior report or chat I found supplies the `\mathcal H_7^q` formula.

   Exact refs:
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:216`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:218`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/summary.md:221`
   - `rh/proof_of_rh.tex:12480`
   - `rh/proof_of_rh.tex:12482`
   - `rh/proof_of_rh.tex:12486`
   - `rh/proof_of_rh.tex:12488`

4. **Current UV-010 reduction identifies the exact obstruction object.**

   The best current formulation is `\mathfrak O_7=[\mathcal J_2^{(7)}]_{\delta=0}` in the septic quotient coordinate. It is the order-7 quotient interaction Hessian. Lower edge laws and abstract source axioms do not determine it; a formal `a_1a_2\delta^2P(m,\kappa)` term survives those tests.

   Exact refs:
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:333`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:337`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report-edge-law-followup.md:5`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/notes/septic-edge-law-obstruction.md:52`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report-UV010-adversarial.md:15`

## False Leads

1. **"Order-7 package is closed" is only a one-pair quotient statement.**

   It closes raw representative ambiguity for `[A_7^{\mathfrak f}]` / `\Delta_7`; it does not define a two-atom quotient edge defect or prove an edge law for `\overline E_{12}^{(7;1)}`.

2. **The fixed C codomain `\mathbf C\times\mathfrak f\times\mathbf C` avoids moving quotient language, but it can hide the UV-010 problem.**

   Determinant scalarization is clean for C, but UV-010 still needs the quotient-valued object before scalarization if the target is `[R]_{\mathrm{edge}}`.

3. **The weak quotient-diagonal route is too coarse.**

   It can exclude close bad two-point cores under assumptions, but prior reports already reject it as a construction of finite-order septic defects.

   Exact refs:
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-140500-C-weak-quotient/report.md:1`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md:83`

4. **The D-side `T=v_7/c` proxy is not UV-010.**

   It is a raw septic lift coordinate useful for hidden-state diagnosis. It is not the C quotient edge package, and prior treasure-hunt notes already warn not to promote it as the canonical theorem object.

   Exact refs:
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-prior-treasure-hunt/report.md:44`
   - `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-prior-treasure-hunt/notes/treasure-map.md:27`
   - `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-132500-T-proxy/report.md:101`

## Exact Next Source Checks

1. **Quotient target and trivialization.**

   Check `rh/proof_of_rh.tex:7004-7062`, `7065-7191`, and `7892-8033` for the exact one-pair quotient/determinant equivalence and gauge law. Then check whether the same determinant pairing can be used as a midpoint trivialization for a moving two-atom class in `rh/proof_of_rh.tex:11603-11638`.

2. **Finite-delta `R` versus edge `R`.**

   Check `rh/proof_of_rh.tex:11603-11775`. The file defines finite-delta `R` only after `\overline E_{12}^{(7;1)}` exists. The source check should separate that from an exceptional-divisor edge definition
   `-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0)`.

3. **Source criterion imports too much.**

   Check `rh/proof_of_rh.tex:11888-12040` and `12168-12189`. The criterion gives quadratic factorization under swap, one-amplitude collapse, and diagonal merger. For UV-010, verify whether any subpart proves the order-7 quotient edge package before merger; current evidence says no.

4. **Edge template has no order-7 quotient line.**

   Check `rh/proof_of_rh.tex:12385-12510`. It has the blow-up variables and the generic even edge-template, then displays only `\mathcal H_3` and `\mathcal H_5`. The missing source check is whether a quotient-valued order-7 defect can be inserted there without invoking state-locality or merger.

5. **Later summaries keep the split.**

   Check `rh/proof_of_rh.tex:24520-24610` and `24990-25030` for the later queue split: edge-law theorem, quotient-visible transport/state-local closure, and package coincidence/functoriality are separate.

## Working Conclusion

The prior archive does not contain a hidden `\mathcal H_7^q` formula. It contains two reusable ingredients:

1. determinant scalarization of a moving quotient class; and
2. the edge-law pattern for cubic/quintic defects.

The next positive UV-010 push should combine those only as a theorem statement:
construct an actual quotient-valued `\mathcal H_7^q`, trivialize it to the midpoint quotient on \(A_5^{\mathfrak f}(m)\neq0\), then optionally scalarize by determinant pairing. Any claim that determinant scalarization alone defines the edge package is still a false lead.
