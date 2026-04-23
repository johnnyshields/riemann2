# gap-spherical-witness

- **Claim**: For the non-Veronese spherical-twist benchmark
  \[
  \psi(t)=\bigl(\cos t\cos 2t,\ \cos t\sin 2t,\ \sin t\bigr)^T\in S^2\subset\mathbb R^3,
  \]
  there is a simple exact equal-overlap / different-angle witness:
  \[
  (u,v)=\left(0,\frac{\pi}{4}\right),
  \qquad
  (u',v')=\left(0,\frac{\pi}{2}\right).
  \]
  Both pairs have the same endpoint overlap, namely `0`, but they give different ambient `A_1` and value-channel-free `O_1` principal-angle data.
- **Status**: proved
- **Evidence**: Proved: the endpoint overlap is
  \[
  I(u,v)=\langle \psi(u),\psi(v)\rangle
  =\sin u\sin v+\cos u\cos v\cos 2(u-v).
  \]
  Hence
  \[
  I\!\left(0,\frac{\pi}{4}\right)=0,
  \qquad
  I\!\left(0,\frac{\pi}{2}\right)=0.
  \]
  Proved: the value-channel-free first-order line is `O_1(t)=span{\psi'(t)}`. The corresponding line-angle cosine is
  \[
  c_{O_1}(u,v)=\frac{\langle \psi'(u),\psi'(v)\rangle}{\|\psi'(u)\|\,\|\psi'(v)\|}.
  \]
  Direct evaluation gives
  \[
  c_{O_1}\!\left(0,\frac{\pi}{4}\right)=-\frac{\sqrt{30}}{30},
  \qquad
  c_{O_1}\!\left(0,\frac{\pi}{2}\right)=0.
  \]
  So the two pairs are already separated by `O_1`.

  Proved: the ambient first-order plane is `A_1(t)=span{\psi(t),\psi'(t)}` with normal `n(t)=\psi(t)\times\psi'(t)`. The ambient nontrivial principal-angle cosine is
  \[
  c_{A_1}(u,v)=\frac{\langle n(u),n(v)\rangle}{\|n(u)\|\,\|n(v)\|}.
  \]
  Direct evaluation gives
  \[
  c_{A_1}\!\left(0,\frac{\pi}{4}\right)=\frac{\sqrt{15}}{5},
  \qquad
  c_{A_1}\!\left(0,\frac{\pi}{2}\right)=-\frac{\sqrt5}{5}.
  \]
  So the two pairs are also separated on the ambient `A_1` side.
- **Exact refs**: `quantum/20260423-204337-attack-nonveronese/reports/gap-spherical-twist.md:3-17`; `quantum/20260423-215017-attack-spherical-witness/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The spherical-twist family lives in a fixed ambient `R^3`, so both `A_1` and `O_1` are exact ambient objects. The witness uses only direct trigonometric evaluation.
- **Strongest objection**: This is still benchmark-level and family-specific. It does not by itself imply a generic non-Veronese theorem, only that the richer-than-overlap phenomenon is not confined to polynomial families.
- **Needed for promotion**: A short sentence in the note or findings is justified. No further algebra is needed unless a broader non-Veronese family theorem is desired.
