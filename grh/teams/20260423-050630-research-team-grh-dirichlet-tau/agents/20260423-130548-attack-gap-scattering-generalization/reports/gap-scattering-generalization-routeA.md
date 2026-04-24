# Claim

- [confirmed] The draft's zero kernel
  \[
  f_{\beta,\gamma}(t)=
  \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
  +
  \frac{\beta}{\beta^2+(2t-\gamma)^2}
  \]
  has the clean interpretation
  \[
  f_{\beta,\gamma}(t)
  =\RePart\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right),
  \qquad \rho=\beta+i\gamma.
  \]
  Equivalently,
  \[
  2f_{\beta,\gamma}(t)
  =\ImPart\!\left(2i\Bigl[\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\Bigr]\right).
  \]
- [confirmed] Summing over zeros, the positive scalar
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
  \]
  is therefore naturally the zero contribution to a strip-edge completed-log-derivative difference, hence to a scattering-type phase derivative, rather than a quantity tied to raw critical-line values \(\zeta(\tfrac12+it)\).
- [conditional] The manuscript strongly suggests that \(q(t)\) is a half-phase derivative of a completed quotient such as
  \[
  \frac{\xi(1+2it)}{\xi(2it)},
  \]
  with background terms removed, but the focused regions do not state that realization explicitly. The factor-of-\(2\) normalization between \(q\) and the full argument derivative is not fixed in the cited passages.

# Status

- proved: the algebraic identity for \(f_{\beta,\gamma}(t)\) above, its positivity, and the fact that \(S(m)\) is built as a zero-sum of these kernels.
- heuristic: interpreting \(S(m)\) as the zero part of a completed-function scattering quotient derivative.
- open: whether the current manuscript already proves the exact completed-quotient formula for \(q(t)\) with all background, trivial-zero, and normalization terms matched exactly.

# Evidence

- The local package defines \(q(t)=\Phi'(t)\) abstractly, then specializes to a zeta/scattering decomposition \(q=B_\zeta+S\) and uses the positive scalar \(S(m):=q_\zeta(m)-B_\zeta(m)\); see lines 149--160 and 273--292.
- The tail theorem defines the omitted-zero contribution by summing \(f_{\beta,\gamma}(t)\); see lines 345--369. The late crude bound rewrites the same scalar as
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m),
  \]
  with every term nonnegative; see lines 26301--26327.
- For \(\rho=\beta+i\gamma\),
  \[
  \RePart\!\frac{1}{1+2it-\rho}=
  \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2},
  \qquad
  \RePart\!\left(-\frac{1}{2it-\rho}\right)=
  \frac{\beta}{\beta^2+(2t-\gamma)^2}.
  \]
  Adding gives exactly \(f_{\beta,\gamma}(t)\).
- Hence
  \[
  S(t)=\RePart\sum_\rho\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right).
  \]
  If one inserts the zero part of the Hadamard logarithmic derivative for the completed function \(\xi\), this is the zero contribution to
  \[
  \frac12\ImPart\left(\frac{d}{dt}\log\frac{\xi(1+2it)}{\xi(2it)}\right).
  \]
  This matches the manuscript's repeated description of \(q\) as a zeta/scattering phase derivative more naturally than any formula based on raw critical-line values.
- The positivity of \(S(m)\) is then structural: each zero contributes a positive strip Poisson kernel measuring the change between the two vertical edges \(\RePart s=0\) and \(\RePart s=1\). That is the right sign mechanism for a completed quotient/scattering channel.

# Exact refs

- `paper/proof_of_rh.tex:149-160` for the abstract phase derivative \(q(t)=\Phi'(t)\).
- `paper/proof_of_rh.tex:271-301` for the zeta/scattering split \(q=B_\zeta+S\), the definition of \(S(m)\), and the curvature bound.
- `paper/proof_of_rh.tex:345-369` for the omitted-zero tail and the explicit kernel \(f_{\beta,\gamma}(t)\).
- `paper/proof_of_rh.tex:1471-1505` and `1527-1621` for the role of \(S(m)\) as the value-channel amplitude in the corrected local deformation.
- `paper/proof_of_rh.tex:26301-26327` for the late exact identity \(S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)\).
- `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:37-42,51-66` for the cycle-level warning that a completed-\(L\) realization theorem is still missing.

# Dependencies

- The identification of \(f_{\beta,\gamma}\) with a completed-log-derivative difference uses only the algebra of the displayed formula and the standard zero-term form of the logarithmic derivative of a completed entire function.
- Interpreting this as the manuscript's actual \(q(t)\) requires the intended scattering-phase normalization: the phase should be the half-argument of a unit-modulus quotient, or an equivalent convention differing by a fixed factor/sign.
- Exact equality between the manuscript's \(B_\zeta\) and the non-zero contribution from the completed quotient requires bookkeeping for gamma factors, trivial zeros, and any Hadamard exponential constant.

# Strongest objection

- The focused passages never write an explicit formula such as
  \[
  q(t)=\frac12\ImPart\left(\frac{d}{dt}\log\frac{\xi(1+2it)}{\xi(2it)}\right)
  =\ImPart\, i\left(\frac{\xi'}{\xi}(1+2it)-\frac{\xi'}{\xi}(2it)\right),
  \]
  nor do they define the scattering matrix whose phase is being differentiated. So the completed-quotient reading is the cleanest reconstruction from the kernel formula, but it is not yet a proved theorem of the manuscript from the cited text alone.
- There is also notation slippage: line 287 writes \(S(m):=q_\zeta(m)-B_\zeta(m)\), while the surrounding text uses \(q(t)\). That makes the intended source object recoverable, but not fully formalized.

# Needed for promotion

- Add one explicit lemma giving the zeta/scattering realization of \(q\), including the exact normalization factor:
  \[
  q(t)=B_\zeta(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)
  \]
  with \(f_{\beta,\gamma}(t)=\RePart\bigl((1+2it-\rho)^{-1}-(2it-\rho)^{-1}\bigr)\).
- State whether the phase is the argument of the completed quotient itself or half its argument. That removes the current factor-of-\(2\) ambiguity.
- Isolate \(B_\zeta\) explicitly as the remaining completed-function contribution: gamma factor, trivial zeros, pole cancellation, and any constant/exponential term.
- Smallest concrete unresolved sub-statements:
  1. Prove the exact completed-quotient identity for \(q(t)\) used by the draft.
  2. Prove that after removing \(B_\zeta\), the residual zero term is exactly the positive sum \(S(t)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)\).
  3. Fix the normalization so that the local value-channel scalar in the later jet analysis is unambiguously this scattering density.
- Honest verdict: the zero kernel itself is clear, clean, and strongly points to a completed-function scattering quotient. What is missing is not the kernel algebra but the manuscript-level theorem that names the quotient and matches all normalization and background terms exactly.
