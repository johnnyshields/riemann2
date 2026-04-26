#!/usr/bin/env python3
"""
Targeted watch-interval rerun.

Stress-tests the four watch centers (m0 ~= 27.7179, 109.099, 171.662, 199.640)
across an expanded grid:

    c_I    in {0.025, 0.05, 0.1, 0.2, 0.5, 1.0}
    kappa  in {0.0625, 0.125, 0.25, 0.5, 1.0, 2.0}
    W_abs  in {20, 50, 100, 200, 500}            (absolute, NOT W_factor / Q)
    R      in {4, 8, 12, 16}
    nquad  in {257, 513, 1025}

This is NOT a generic gate1 pilot scan; it's a focused diagnostic on already-
flagged centers. Tail windows are absolute so we can sweep widths without
having Q rescale them.

Reuses the existing kernels from gate1_pilot. Parallelized at the
(center, c_I, kappa, W_abs, R_jet, nquad) row level via a multiprocessing
Pool. Streaming CSV writes; no resume (the rerun is small enough to redo).
"""

from __future__ import annotations

# Pin BLAS / OpenMP to 1 thread per process before any numpy import.
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import argparse
import csv
import math
import multiprocessing as mp_proc
import time
from typing import Dict, List, Tuple

import gate1_pilot
from gate1_pilot import (
    _classify_row,
    _rel_diff,
    ensure_dir,
    finite_difference_jets_zero_proxy,
    integrate_zero_proxy,
    load_or_generate_zeros,
    log,
    safe_log,
    write_csv,
)


WATCH_CENTERS_DEFAULT = [27.7179, 109.099, 171.662, 199.640]

_FIELDNAMES = [
    "center_type", "m0", "Q",
    "c_I", "Delta", "kappa", "eps",
    "W_abs", "W_factor_equiv",
    "nquad", "R_jet", "local_zero_count",
    "E_I", "S_I", "B_eff", "J_max", "J_rms",
    "tail_drift_rel", "quad_drift_rel", "tail_edge", "status",
]


def _init_worker(zeros: List[float]) -> None:
    """Set gate1_pilot._W_ZEROS so worker copies of integrate_zero_proxy etc.
    that close over the module's global state see the data."""
    gate1_pilot._W_ZEROS = zeros


def _process_task(task: Tuple) -> Dict:
    """Compute one row for (m0, c_I, kappa, W_abs, R_jet, nquad)."""
    (m0, c_I, kappa, W_abs, R_jet, nquad) = task
    zeros = gate1_pilot._W_ZEROS
    if zeros is None:
        return {}

    Q = math.log(m0 / (2.0 * math.pi))
    if Q <= 1.0:
        return {}

    Delta = c_I / Q
    eps = kappa / Q
    W = W_abs
    W2 = 2.0 * W_abs
    tail_edge = (m0 - W2 < zeros[0]) or (m0 + W2 > zeros[-1])

    E_I, S_I, local_zero_count = integrate_zero_proxy(
        zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W, n_nodes=nquad,
    )
    if not math.isfinite(E_I):
        return {}

    E_half, _, _ = integrate_zero_proxy(
        zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W,
        n_nodes=max(32, nquad // 2),
    )
    quad_drift_rel = _rel_diff(E_I, E_half) if math.isfinite(E_half) else float("nan")

    E_2W, _, _ = integrate_zero_proxy(
        zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W2, n_nodes=nquad,
    )
    tail_drift_rel = _rel_diff(E_I, E_2W) if math.isfinite(E_2W) else float("nan")

    J_max, J_rms = finite_difference_jets_zero_proxy(
        zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W, R=R_jet,
    )
    B_eff = -safe_log(E_I) / math.log(Q)

    status = _classify_row(
        B_eff=B_eff, J_max=J_max,
        tail_drift_rel=tail_drift_rel, quad_drift_rel=quad_drift_rel,
        tail_edge=tail_edge,
    )

    return {
        "center_type": "watch_center",
        "m0": m0,
        "Q": Q,
        "c_I": c_I,
        "Delta": Delta,
        "kappa": kappa,
        "eps": eps,
        "W_abs": W_abs,
        "W_factor_equiv": W_abs * Q,
        "nquad": nquad,
        "R_jet": R_jet,
        "local_zero_count": local_zero_count,
        "E_I": E_I,
        "S_I": S_I,
        "B_eff": B_eff,
        "J_max": J_max,
        "J_rms": J_rms,
        "tail_drift_rel": tail_drift_rel,
        "quad_drift_rel": quad_drift_rel,
        "tail_edge": tail_edge,
        "status": status,
    }


def parse_float_list(s: str) -> List[float]:
    return [float(x.strip()) for x in s.split(",") if x.strip()]


def parse_int_list(s: str) -> List[int]:
    return [int(x.strip()) for x in s.split(",") if x.strip()]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="gate1_out_watch")
    ap.add_argument("--zeros", type=int, default=500)
    ap.add_argument("--centers", default=",".join(str(x) for x in WATCH_CENTERS_DEFAULT))
    ap.add_argument("--c-I", default="0.025,0.05,0.1,0.2,0.5,1.0")
    ap.add_argument("--kappa", default="0.0625,0.125,0.25,0.5,1.0,2.0")
    ap.add_argument("--W-abs", default="20,50,100,200,500")
    ap.add_argument("--R", default="4,8,12,16")
    ap.add_argument("--nquad", default="257,513,1025")
    ap.add_argument("--workers", type=int,
                    default=max(1, min((os.cpu_count() or 2) - 2, 10)),
                    help="number of worker processes; 1 = serial. "
                         "Default: max(1, min(cpu_count - 2, 10)).")
    args = ap.parse_args()

    ensure_dir(args.outdir)

    centers = parse_float_list(args.centers)
    c_I_values = parse_float_list(args.c_I)
    kappa_values = parse_float_list(args.kappa)
    W_abs_values = parse_float_list(args.W_abs)
    R_values = parse_int_list(args.R)
    nquad_values = parse_int_list(args.nquad)

    log(f"loading or generating {args.zeros} zeros")
    zeros = load_or_generate_zeros(args.outdir, n_zeros=args.zeros)
    log(f"have {len(zeros)} zeros: gamma_1={zeros[0]:.4f}, gamma_N={zeros[-1]:.4f}")

    tasks: List[Tuple] = []
    for m0 in centers:
        Q = math.log(m0 / (2.0 * math.pi))
        if Q <= 1.0:
            log(f"skipping m0={m0}: Q={Q:.4f} <= 1.0")
            continue
        for c_I in c_I_values:
            for kappa in kappa_values:
                for W_abs in W_abs_values:
                    for R_jet in R_values:
                        for nquad in nquad_values:
                            tasks.append((m0, c_I, kappa, W_abs, R_jet, nquad))

    log(f"watch rerun plan: {len(centers)} centers x {len(c_I_values)} c_I "
        f"x {len(kappa_values)} kappa x {len(W_abs_values)} W_abs "
        f"x {len(R_values)} R x {len(nquad_values)} nquad = {len(tasks)} rows")

    out_csv = os.path.join(args.outdir, "watch_rerun.csv")
    if os.path.exists(out_csv):
        os.remove(out_csv)
    fout = open(out_csv, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(fout, fieldnames=_FIELDNAMES)
    writer.writeheader()
    fout.flush()

    rows: List[Dict] = []
    t0 = time.time()
    progress_every = max(1, len(tasks) // 50)
    log(f"progress prints every {progress_every} rows, workers={args.workers}")

    try:
        if args.workers <= 1:
            log("running serial (workers <= 1)")
            _init_worker(list(zeros))
            for idx, task in enumerate(tasks):
                row = _process_task(task)
                if row:
                    writer.writerow(row)
                    rows.append(row)
                    fout.flush()
                if (idx + 1) % progress_every == 0 or idx + 1 == len(tasks):
                    elapsed = time.time() - t0
                    rate = (idx + 1) / elapsed if elapsed > 0 else 0
                    eta = (len(tasks) - idx - 1) / rate if rate > 0 else 0
                    log(f"  rows {idx+1}/{len(tasks)}  written={len(rows)}  "
                        f"elapsed={elapsed:.1f}s  rate={rate:.1f}/s  eta={eta:.1f}s")
        else:
            method = "fork" if "fork" in mp_proc.get_all_start_methods() else "spawn"
            log(f"running in process pool with {args.workers} workers (start_method={method})")
            ctx = mp_proc.get_context(method)
            with ctx.Pool(processes=args.workers, initializer=_init_worker,
                          initargs=(list(zeros),)) as pool:
                for idx, row in enumerate(
                    pool.imap_unordered(_process_task, tasks, chunksize=8)
                ):
                    if row:
                        writer.writerow(row)
                        rows.append(row)
                        fout.flush()
                    if (idx + 1) % progress_every == 0 or idx + 1 == len(tasks):
                        elapsed = time.time() - t0
                        rate = (idx + 1) / elapsed if elapsed > 0 else 0
                        eta = (len(tasks) - idx - 1) / rate if rate > 0 else 0
                        log(f"  rows {idx+1}/{len(tasks)}  written={len(rows)}  "
                            f"elapsed={elapsed:.1f}s  rate={rate:.1f}/s  eta={eta:.1f}s")
    finally:
        fout.close()

    log(f"wrote {len(rows)} rows to {out_csv}")

    # Top-50 by B_eff among rows that pass tail_edge / drift gates.
    accept = [r for r in rows
              if not r.get("tail_edge")
              and r.get("status") not in ("reject_tail_edge", "reject_tail_unstable",
                                          "reject_quad_unstable")
              and math.isfinite(float(r["B_eff"]))]
    top = sorted(accept, key=lambda r: float(r["B_eff"]), reverse=True)[:50]
    top_path = os.path.join(args.outdir, "watch_rerun_top_by_Beff.csv")
    write_csv(top_path, top)
    log(f"wrote {len(top)} top rows to {top_path}")

    # Per-center best summary.
    by_center: Dict[float, Dict] = {}
    for r in accept:
        m0 = float(r["m0"])
        cur = by_center.get(m0)
        if cur is None or float(r["B_eff"]) > float(cur["B_eff"]):
            by_center[m0] = r

    log("best (post-gate) row per watch center:")
    for m0 in sorted(by_center):
        r = by_center[m0]
        print({
            "m0": m0, "Q": r["Q"], "B_eff": r["B_eff"], "E_I": r["E_I"],
            "J_max": r["J_max"], "J_rms": r["J_rms"],
            "c_I": r["c_I"], "kappa": r["kappa"], "W_abs": r["W_abs"],
            "R_jet": r["R_jet"], "nquad": r["nquad"],
            "tail_drift_rel": r["tail_drift_rel"],
            "quad_drift_rel": r["quad_drift_rel"],
            "status": r["status"],
        }, flush=True)

    # Status distribution overall.
    from collections import Counter
    status_counts = Counter(r["status"] for r in rows)
    log(f"status distribution: {dict(status_counts)}")


if __name__ == "__main__":
    main()
