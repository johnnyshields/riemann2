#!/usr/bin/env python3
"""
Generate band-specific zeta-zero ordinate files for the deep proxy scan.

Uses parallel Hardy Z(t) sign-change bracketing followed by mpmath bisection,
mirroring the approach in scripts/zeta_bridge_agent2/gate1_actual_zero_proxy_zone_scan.py
(hardy_z_zeros_near). Output is a plain text file, one ordinate per line, suitable
for `gate1_zero_pilot.py --zeros`.

Default bands target T~1e3, T~1e4, T~1e5; each is widened slightly past the band
ends so tail-edge guards don't trip on every center.

Usage:
    python make_zero_bands.py --out-dir out/zero_bands
    python make_zero_bands.py --out-dir out/zero_bands --band 800,1200,zeros_T1e3.txt
    python make_zero_bands.py --out-dir out/zero_bands --workers 10 --pad 200
"""

from __future__ import annotations

# Pin BLAS/OpenMP threads before numpy import; we parallelize by process.
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import json
import multiprocessing as mp_ctx
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple

import numpy as np
import mpmath as mp


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def log(msg: str) -> None:
    print(f"[make_zero_bands] {msg}", flush=True)


# -----------------------------
# Worker functions (top-level for picklability)
# -----------------------------

def _siegelz_chunk(args) -> np.ndarray:
    xs, dps = args
    mp.mp.dps = dps
    out = np.empty(len(xs), dtype=float)
    for i, t in enumerate(xs):
        out[i] = float(mp.siegelz(t))
    return out


def _siegelz_bisect(args) -> float:
    a, b, fa, fb, dps, prec_dps = args
    mp.mp.dps = max(dps, prec_dps)

    def f(x):
        return mp.siegelz(x)

    # mpmath's findroot with bisection-like solver
    try:
        z = mp.findroot(f, (mp.mpf(a), mp.mpf(b)), solver="anderson")
        return float(z)
    except Exception:
        # Fallback: simple bisection
        lo, hi = mp.mpf(a), mp.mpf(b)
        flo, fhi = mp.mpf(fa), mp.mpf(fb)
        for _ in range(80):
            mid = (lo + hi) / 2
            fmid = mp.siegelz(mid)
            if fmid == 0:
                return float(mid)
            if flo * fmid < 0:
                hi, fhi = mid, fmid
            else:
                lo, flo = mid, fmid
        return float((lo + hi) / 2)


def find_zeros_in_range(
    lo: float,
    hi: float,
    step: float,
    dps: int,
    bisect_dps: int,
    workers: int,
) -> Tuple[np.ndarray, dict]:
    """Return (zeros, stats) for all zeros in [lo, hi]."""
    t0 = time.time()
    n_grid = int(np.ceil((hi - lo) / step)) + 1
    xs = lo + step * np.arange(n_grid)
    xs = xs[xs <= hi + 0.5 * step]

    log(f"  evaluating siegelz on {len(xs)} grid points "
        f"(step={step}, dps={dps}, workers={workers})...")

    if workers > 1 and len(xs) >= 4 * workers:
        chunks = np.array_split(xs, workers)
        chunk_args = [(np.asarray(c, dtype=float), dps) for c in chunks]
        # Use spawn or fork depending on platform support
        try:
            ctx = mp_ctx.get_context("fork")
        except ValueError:
            ctx = mp_ctx.get_context("spawn")
        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
            chunk_vals = list(ex.map(_siegelz_chunk, chunk_args))
        vals = np.concatenate(chunk_vals)
    else:
        vals = _siegelz_chunk((xs, dps))

    t_eval = time.time() - t0
    log(f"  siegelz evaluation: {t_eval:.1f}s, "
        f"sign changes ~ {int(np.sum(np.diff(np.sign(vals)) != 0))}")

    # Identify sign-change brackets.
    bracket_args = []
    exact_zeros: List[float] = []
    for i in range(len(xs) - 1):
        prev_x, prev_v = float(xs[i]), float(vals[i])
        x, v = float(xs[i + 1]), float(vals[i + 1])
        if prev_v == 0.0:
            exact_zeros.append(prev_x)
        elif v == 0.0 and i == len(xs) - 2:
            exact_zeros.append(x)
        elif prev_v * v < 0:
            bracket_args.append((prev_x, x, prev_v, v, dps, bisect_dps))

    log(f"  bisecting {len(bracket_args)} brackets...")

    t1 = time.time()
    bisect_zeros: List[float] = []
    if bracket_args:
        if workers > 1 and len(bracket_args) >= 2 * workers:
            try:
                ctx = mp_ctx.get_context("fork")
            except ValueError:
                ctx = mp_ctx.get_context("spawn")
            # Chunk brackets to amortize process spawn cost.
            with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
                bisect_zeros = list(ex.map(_siegelz_bisect, bracket_args, chunksize=max(1, len(bracket_args) // (workers * 4))))
        else:
            bisect_zeros = [_siegelz_bisect(a) for a in bracket_args]
    t_bis = time.time() - t1
    log(f"  bisection: {t_bis:.1f}s")

    zeros = np.array(
        sorted(set(round(z, 12) for z in (exact_zeros + bisect_zeros))),
        dtype=float,
    )
    zeros = zeros[(zeros >= lo) & (zeros <= hi)]

    stats = {
        "lo": lo, "hi": hi, "step": step, "dps": dps, "bisect_dps": bisect_dps,
        "n_grid": int(len(xs)), "n_brackets": int(len(bracket_args)),
        "n_zeros": int(len(zeros)),
        "t_eval_s": t_eval, "t_bisect_s": t_bis,
        "elapsed_s": time.time() - t0,
    }
    return zeros, stats


def write_zeros_file(zeros: np.ndarray, path: str) -> None:
    with open(path, "w") as f:
        for z in zeros:
            f.write(f"{z:.12f}\n")


def write_stats_sidecar(stats: dict, path: str) -> None:
    with open(path, "w") as f:
        json.dump(stats, f, indent=2)


def parse_band(spec: str) -> Tuple[float, float, str]:
    parts = [p.strip() for p in spec.split(",")]
    if len(parts) != 3:
        raise ValueError(f"Bad --band {spec!r}; expected lo,hi,filename")
    return float(parts[0]), float(parts[1]), parts[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=os.path.join(SCRIPT_DIR, "out", "zero_bands"))
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    parser.add_argument("--step", type=float, default=0.05,
                        help="Hardy-Z grid step. Smaller = safer for high heights.")
    parser.add_argument("--dps", type=int, default=30, help="Working precision for siegelz scan.")
    parser.add_argument("--bisect-dps", type=int, default=40, help="Precision for root bisection.")
    parser.add_argument("--pad", type=float, default=200.0,
                        help="Pad each band's [lo,hi] outward so tail windows have margin.")
    parser.add_argument("--band", action="append", default=None,
                        help="Override default bands. Format: lo,hi,filename. Repeatable.")
    parser.add_argument("--force", action="store_true", help="Recompute even if output exists.")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    if args.band:
        bands = [parse_band(b) for b in args.band]
    else:
        bands = [
            (800.0,    1200.0,   "zeros_T1e3.txt"),
            (8000.0,   12000.0,  "zeros_T1e4.txt"),
            (80000.0,  120000.0, "zeros_T1e5.txt"),
        ]

    log(f"Out dir: {args.out_dir}")
    log(f"Workers: {args.workers}, step={args.step}, pad={args.pad}, dps={args.dps}/{args.bisect_dps}")

    summary = []
    for (lo, hi, name) in bands:
        out_path = os.path.join(args.out_dir, name)
        sidecar = out_path + ".stats.json"
        if os.path.exists(out_path) and not args.force:
            n_existing = sum(1 for _ in open(out_path)) if os.path.exists(out_path) else 0
            log(f"[skip] {name}: exists with {n_existing} zeros (use --force to recompute).")
            summary.append({"name": name, "n_zeros": n_existing, "skipped": True})
            continue

        log(f"=== {name}: t in [{lo - args.pad}, {hi + args.pad}] (band [{lo}, {hi}] padded by {args.pad}) ===")
        zeros, stats = find_zeros_in_range(
            lo=lo - args.pad,
            hi=hi + args.pad,
            step=args.step,
            dps=args.dps,
            bisect_dps=args.bisect_dps,
            workers=args.workers,
        )
        write_zeros_file(zeros, out_path)
        stats.update({"out_path": out_path, "name": name, "band_lo": lo, "band_hi": hi, "pad": args.pad})
        write_stats_sidecar(stats, sidecar)
        log(f"  wrote {len(zeros)} zeros to {out_path}  (elapsed {stats['elapsed_s']:.1f}s)")
        summary.append({"name": name, **stats})

    log("=== summary ===")
    for s in summary:
        log(f"  {s.get('name')}: n_zeros={s.get('n_zeros')} elapsed={s.get('elapsed_s', 0):.1f}s skipped={s.get('skipped', False)}")


if __name__ == "__main__":
    main()
