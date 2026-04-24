# gap-twist-family

- **Claim**: For the real spherical twist family
  \[
  \psi_k(t)=\bigl(\cos t\cos kt,\ \cos t\sin kt,\ \sin t\bigr)^T\in S^2\subset\mathbb R^3,
  \qquad k\in\mathbb Z_{\ge2},
  \]
  the richer-than-overlap behavior persists for every \(k\ge2\). An exact equal-overlap witness is
  \[
  (u,v)=\left(0,\frac{\pi}{2}\right),
  \qquad
  (u',v')=\left(0,\frac{\pi}{2k}\right).
  \]
  Both pairs have the same endpoint overlap `0`, but their `A_1` and/or `O_1`
  angle data differ for every \(k\ge2\).
- **Status**: proved
- **Evidence**: Proved: the overlap at \(u=0\) is
  \[
  I_k(0,v)=\cos v\cos(kv).
  \]
  Therefore
  \[
  I_k\!\left(0,\frac{\pi}{2}\right)=0,
  \qquad
  I_k\!\left(0,\frac{\pi}{2k}\right)=0.
  \]
  For the value-channel-free side,
  \[
  c_{O_1}^{(k)}\!\left(0,\frac{\pi}{2}\right)
  =-\frac{k\sin(\pi k/2)}{\sqrt{k^2+1}}.
  \]
  Hence if \(k\) is even, this is `0`. On the other hand,
  \[
  c_{O_1}^{(k)}\!\left(0,\frac{\pi}{2k}\right)
  =\frac{-k\sin(\pi/2k)+\cos(\pi/2k)}{\sqrt{k^2+1}\sqrt{k^2\cos^2(\pi/2k)+1}}.
  \]
  For \(k\ge2\), writing \(x=\pi/(2k)\), one has \(x>1/k\) and \(\tan x>x\), so
  \(k\tan x>1\). Therefore \(\cos x-k\sin x<0\), hence this second value is nonzero. So for every even \(k\ge2\), the two equal-overlap pairs are separated already by `O_1`.

  For the ambient side,
  \[
  c_{A_1}^{(k)}\!\left(0,\frac{\pi}{2}\right)
  =\frac{\cos(\pi k/2)}{\sqrt{k^2+1}}.
  \]
  Hence if \(k\) is odd, this is `0`. On the other hand,
  \[
  c_{A_1}^{(k)}\!\left(0,\frac{\pi}{2k}\right)
  =\frac{k\bigl(2k\cos^2(\pi/2k)+\sin(\pi/k)\bigr)}{\sqrt{k^2+1}\sqrt{k^2\sin^2(\pi/k)+4k^2\cos^4(\pi/2k)+4}}.
  \]
  Its numerator is strictly positive for every \(k\ge2\), so this second value is nonzero. Thus for every odd \(k\ge3\), the two equal-overlap pairs are separated by `A_1`.

  Therefore for every \(k\ge2\), the family \(\psi_k\) exhibits richer-than-overlap behavior on at least one of the two canonical first-order sides, and hence the phenomenon is not confined to polynomial families.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:582-600`; `quantum/findings.md:172-180`; `quantum/teams/20260423-204337-attack-nonveronese/reports/gap-spherical-twist.md:3-17`; `quantum/teams/20260423-215017-attack-spherical-witness/reports/gap-spherical-witness.md:3-18`; `quantum/20260424-033611-attack-twist-family/notes/coordinator-brief.md:3-10`.
- **Dependencies**: Fixed ambient `R^3`; direct trigonometric formulas for overlap and the `A_1` / `O_1` angle data; the elementary inequality `tan x > x` for `x > 0`.
- **Strongest objection**: The theorem is still benchmark-family scoped, and the witness splits by parity: even `k` is cleanest on the `O_1` side, odd `k` on the `A_1` side. It does not say both sides are richer-than-overlap for every `k`.
- **Needed for promotion**: A short benchmark-family remark in the note is justified if desired, but the current single `k=2` spherical example is already enough for the main narrative.
