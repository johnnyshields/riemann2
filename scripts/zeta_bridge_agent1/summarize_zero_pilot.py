#!/usr/bin/env python3
import csv
import math
import sys
from collections import Counter

def fnum(x):
    try:
        return float(x)
    except Exception:
        return float("nan")

def summarize(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"\n=== {path} ===")
    print(f"rows: {len(rows)}")

    status = Counter(r.get("status", "") for r in rows)
    print("status counts:")
    for k, v in status.most_common():
        print(f"  {k}: {v}")

    def val(row, col):
        return fnum(row.get(col, "nan"))

    numeric_cols = [
        "E_I", "S_I", "B_eff", "J_max", "J_rms",
        "tail_drift_rel", "quad_drift_rel", "local_zero_count",
    ]

    print("\nsummary:")
    for col in numeric_cols:
        xs = [val(r, col) for r in rows]
        xs = [x for x in xs if math.isfinite(x)]
        if not xs:
            continue
        xs.sort()
        def pct(p):
            return xs[int(p * (len(xs) - 1))]
        print(
            f"  {col}: "
            f"min={xs[0]:.6e}, "
            f"p25={pct(0.25):.6e}, "
            f"median={pct(0.50):.6e}, "
            f"p75={pct(0.75):.6e}, "
            f"max={xs[-1]:.6e}"
        )

    print("\nTop 20 by B_eff:")
    top = sorted(rows, key=lambda r: val(r, "B_eff"), reverse=True)[:20]
    cols = [
        "status", "center_type", "m0", "Q", "c_I", "kappa",
        "W_factor", "local_zero_count", "E_I", "S_I", "B_eff",
        "J_max", "tail_drift_rel", "quad_drift_rel",
    ]
    print(",".join(cols))
    for r in top:
        print(",".join(str(r.get(c, "")) for c in cols))

    print("\nRows with B_eff > 5:")
    print(sum(1 for r in rows if val(r, "B_eff") > 5))

    print("Rows with B_eff > 10:")
    print(sum(1 for r in rows if val(r, "B_eff") > 10))

    print("Rows with tail_drift_rel > 0.02:")
    print(sum(1 for r in rows if val(r, "tail_drift_rel") > 0.02))

    print("Rows with quad_drift_rel > 1e-5:")
    print(sum(1 for r in rows if val(r, "quad_drift_rel") > 1e-5))

if __name__ == "__main__":
    for path in sys.argv[1:]:
        summarize(path)
