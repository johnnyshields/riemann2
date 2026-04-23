# Claim

1. [confirmed] The phase-kernel, jet-limit, value-channel, odd-channel, and discrete odd-moment package in the cited regions are mostly degree-1 phase algebra. Once one has a real scalar phase \(\Phi\) with real derivative \(q=\Phi'\), the formulas in `paper/proof_of_rh.tex:149-299`, `426-850`, `2212-2322`, and `2975-3169` port with only background-term replacement.
2. [confirmed] For a primitive Dirichlet character \(\chi\), one should not work with the raw complex-valued boundary function \(L(\tfrac12+it,\chi)\). The clean direct replacement is a self-dual real-valued completion on the critical line, for example
   \[
   F_\chi(t):=e^{-i\arg \varepsilon_\chi/2}\,\Lambda\!\left(\tfrac12+it,\chi\right),
   \]
   where \(\Lambda(s,\chi)\) is the primitive completed \(L\)-function and \(\varepsilon_\chi\) is the root number. By the standard functional equation,
   \(F_\chi(t)\in\mathbf R\) for real \(t\). A paired object involving \(\chi\) and \(\bar\chi\) is a safe alternative, but it is not the first thing to try.
3. [conditional] The zeta-side decomposition appears degree-1 generic after replacing \(B_\zeta\) by the conductor-plus-gamma background for \(\chi\), and replacing the zero contribution by the corresponding completed-\(L\) zero term. The formal calibration package then survives unchanged, but the analytic input has to be reproved in the new background.
4. [candidate] The cleanest abstraction for the RH paper itself is to separate the current architecture into:
   \(i\) a universal real-phase local package;
   \(ii\) a degree-1 analytic-input package (background size, positivity/nondegeneracy of the local value scale, curvature control);
   \(iii\) a zeta-specific endgame package.
5. [candidate] The strongest likely failure mode for complex characters is not the local kernel algebra; it is any step that silently uses a single real self-dual object with \(t\mapsto -t\) symmetry, positivity of \(S(m)\), or zeta-specific scattering normalization without rechecking the Dirichlet analogue.

# Status

heuristic

# Evidence

Proved inside the cited draft regions:

- The phase kernel and jet blocks depend only on a real phase \(\Phi\) and its derivatives \(q,q',q''\); no zeta-specific identity enters the formulas for \(K_\Phi\), \(J(T)\), \(N_{12}\), or the finite-\(s\) block. See `paper/proof_of_rh.tex:149-269`.
- The value-channel derivative \(A_{\val}\) is derived in a constant-background symmetric regime from the whitened local block and the scalar relation \(\Delta_0=-B\sigma\). The explicit formula and the vanishing \(\Phi_K(A_{\val})=0\) use only this phase algebra. See `paper/proof_of_rh.tex:431-599`.
- The odd transverse scalar \(H_m(s)=\Phi_K(\widehat\Omega^{\corr}(s;m))\) is odd because symmetric placement exchanges the two jets under \(s\mapsto -s\). This is swap symmetry, not a zeta-only global symmetry. See `paper/proof_of_rh.tex:2214-2322`.
- The \(N\)-point coefficients and Mellin symbol are purely discrete odd-moment cancellation statements once an odd holomorphic scalar \(H_m\) is available. See `paper/proof_of_rh.tex:2977-3169`.
- The late endgame remarks explicitly state that pure planar/intrinsic geometry is universal and that any final contradiction must use source-specific structure beyond generic affine geometry. That statement supports the degree-1/generic split proposed here. See `paper/proof_of_rh.tex:25915-25922`, `25956-25990`, `26280-26299`.

Conditional on standard degree-1 completed-\(L\) facts:

- For primitive \(\chi\), the completed function
  \(\Lambda(s,\chi)=(q_\chi/\pi)^{(s+a_\chi)/2}\Gamma((s+a_\chi)/2)L(s,\chi)\)
  satisfies \(\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi)\) with \(|\varepsilon_\chi|=1\). On the critical line this gives
  \(\Lambda(\tfrac12+it,\chi)=\varepsilon_\chi\overline{\Lambda(\tfrac12+it,\chi)}\), hence the rotated boundary value \(F_\chi(t)\) above is real. This is the clean reason the current framework can still use a real phase for complex characters.
- After this rotation, the local formulas in the cited draft should carry over with \(B_\zeta\) replaced by the conductor-plus-gamma background derivative and with the zero contribution rewritten for the \(\chi\)-zeros of the completed object. This covers the architecture around `paper/proof_of_rh.tex:271-299`, `739-850`, `2214-2322`, and `2977-3169`.
- The odd-channel cancellation should remain valid for any degree-1 completed object once one has the analogue of the corrected whitening holomorphy and a bound of the form
  \(|H_m(s)|\ll L_\chi(m)S_\chi(m)^2/Q_\chi^3\). The discrete cancellation itself is character-blind.

Missing or not checked in the draft:

- The draft's local value scale \(S(m)=q_\zeta(m)-B_\zeta(m)\) is used as a positive calibration amplitude and enters the curvature bound \(|S''(m)|\ll L(m)S(m)^2\). See `paper/proof_of_rh.tex:285-299`, `753-779`, `2231`, `2306`, `26301-26364`. For primitive complex \(\chi\), the exact analogue of positivity, size, and curvature control has not been derived here.
- The notation and proofs still lean on a zeta/scattering background split. Even if the degree-1 Dirichlet replacement exists, one has to rewrite every place where \(B_\zeta(m)\asymp Q\), \(S(m)\ll Q^2\), or the scattering normalization is used quantitatively. See `paper/proof_of_rh.tex:439-445`, `803-839`, `2203-2209`, `26301-26364`, `26424-26533`.
- If one instead passes to a paired product such as \(\Lambda(s,\chi)\Lambda(s,\bar\chi)\), the resulting object is more obviously self-dual but changes the zero multiplicities and the phase bookkeeping. That route is safer structurally but less faithful to the present single-channel calibration.

# Exact refs

- Common brief: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md`
- Universal phase-kernel and jet formulas: `paper/proof_of_rh.tex:149-269`
- Zeta-side split and curvature input: `paper/proof_of_rh.tex:271-299`
- Value-channel derivative and calibration: `paper/proof_of_rh.tex:431-850`
- Odd corrected scalar and odd microscopic expansion: `paper/proof_of_rh.tex:2214-2322`
- Discrete odd-moment projector: `paper/proof_of_rh.tex:2977-3169`
- Endgame remarks on universality ceiling and need for source-specific structure: `paper/proof_of_rh.tex:25915-25922`, `25956-25990`, `26280-26299`, `26424-26533`
- Standard external facts used conditionally: primitive Dirichlet completion, functional equation, and root number reality relation on the critical line.

# Dependencies

- Standard functional equation for primitive Dirichlet \(L\)-functions.
- A self-dual real-valued normalization on the critical line, preferably the rotated completion \(F_\chi(t)\).
- A Dirichlet analogue of the background split \(q=B+S\) with explicit conductor-plus-gamma background.
- A Dirichlet analogue of positivity/nondegeneracy for the local value scale and of the curvature estimate replacing `paper/proof_of_rh.tex:296-300`.
- A check that corrected whitening and microscopic holomorphy survive with the new background package.

# Strongest objection

The report's positive conclusion is structural, not closure-level. The draft regions show that the local algebra is generic once a real scalar phase exists, but they do not by themselves produce the needed Dirichlet phase object, positivity package, or curvature estimate. The most serious risk is that a single complex-character channel may not deliver the same sign-definite local value scale that zeta uses in calibration, forcing either a different normalization or a paired \((\chi,\bar\chi)\) object. So the statement "the framework extends directly to primitive complex characters" is too strong without a fresh analytic derivation of \(S_\chi(m)\), its sign, and its curvature control.

# Needed for promotion

1. Write a degree-1 abstract lemma package isolating exactly which parts of `paper/proof_of_rh.tex:149-850`, `2212-2322`, and `2975-3169` only require a real phase \(\Phi\), real background \(B\), and a curvature bound.
2. For primitive \(\chi\), define the preferred self-dual real-valued boundary object and derive the corresponding phase derivative \(q_\chi(t)\).
3. Prove the analogue of \(q=B+S\) with explicit conductor-plus-gamma background and identify whether \(S_\chi(m)\) is sign-definite, merely nonnegative, or must be replaced by a different amplitude.
4. Recheck the calibration theorem with the Dirichlet background constants: which steps only need \(B(m)\asymp Q\), and which steps use more specific zeta/scattering structure.
5. Decide whether the single rotated completion is sufficient or whether the proof architecture is cleaner on a paired self-dual object involving \(\chi\) and \(\bar\chi\).

Honest verdict: the cleanest present exploration is that the local phase-kernel and odd-\(N\)-point machinery are degree-1 generic, but complex characters should enter through a self-dual real-valued completed object, not through raw \(L(\tfrac12+it,\chi)\). The likely hard part is not the local kernel algebra; it is rebuilding the zeta-side calibration inputs with conductor, gamma, and root-number bookkeeping and checking where positivity of the value scale is genuinely used.
