#!/usr/bin/env python3
"""Adversarial verifier for the UV-026 Stage 1 source-table generator.

This script reruns the cited generator with its built-in demo, compares the
resulting manifest to the deposited manifest, and checks the normalization
contract fields needed by the Stage 1 source audit.
"""

from __future__ import annotations

import json
import subprocess
import sys
from hashlib import sha1
from pathlib import Path


ROOT = Path("C:/workspace/riemann2")
GENERATOR = ROOT / "rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py"
MANIFEST = ROOT / "rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json"
OWNED = ROOT / "rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator"
RERUN_MANIFEST = OWNED / "notes/stage1_source_table_manifest.rerun.json"
SUMMARY = OWNED / "notes/stage1_generator_verifier_output.json"


def file_sha1(path: Path) -> str:
    return sha1(path.read_bytes()).hexdigest().upper()


def matrix_table_shape(obj: object, order: int = 7) -> bool:
    if not isinstance(obj, list) or len(obj) != order + 1:
        return False
    for coeff in obj:
        if not isinstance(coeff, list) or len(coeff) != 2:
            return False
        for row in coeff:
            if not isinstance(row, list) or len(row) != 2:
                return False
            if not all(isinstance(x, str) for x in row):
                return False
    return True


def main() -> int:
    OWNED.joinpath("notes").mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [sys.executable, str(GENERATOR), "--out", str(RERUN_MANIFEST)],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
        check=False,
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rerun = json.loads(RERUN_MANIFEST.read_text(encoding="utf-8")) if RERUN_MANIFEST.exists() else {}
    src = GENERATOR.read_text(encoding="utf-8")

    norm = manifest.get("normalization", {})
    counts = manifest.get("minimal_scalar_inputs", {}).get("counts", {})
    removable = manifest.get("removable_singularity_check", {})
    tables = manifest.get("tables", {})

    source_strings = {
        "ordinary_z_substitution": "s_factor = Fraction(1, q_value**2)" in src
        and "taylor_from_derivs(q_derivs, sgn, q_value)" in src,
        "mixed_divisions": "n0_divs = [[1, 2], [2, 3]]" in src
        and "raw_divs = [[1, 2], [2, 3]]" in src,
        "D_Q_mixed_scaling": "scale_after = [[q_value**2, q_value], [q_value, Fraction(1)]]" in src,
        "tag_grade_axes": 'TAGS = ("1", "2")' in src and 'GRADES = ("1", "5")' in src,
        "linear_eta_from_integral": "eta = integral_difference(vals, q_value, SOURCE_DERIV_MIN, SOURCE_DERIV_MAX)" in src,
    }

    shape_checks = {
        "G0_minus": matrix_table_shape(tables.get("G0", {}).get("-")),
        "G0_plus": matrix_table_shape(tables.get("G0", {}).get("+")),
        "N0": matrix_table_shape(tables.get("N0")),
        "deltaG_all_tag_grade_sign": all(
            matrix_table_shape(
                tables.get("deltaG_lin", {})
                .get(tag, {})
                .get(grade, {})
                .get(sign)
            )
            for tag in ("1", "2")
            for grade in ("1", "5")
            for sign in ("-", "+")
        ),
        "M_scaled_all_tag_grade": all(
            matrix_table_shape(
                tables.get("M_scaled", {})
                .get(tag, {})
                .get(grade)
            )
            for tag in ("1", "2")
            for grade in ("1", "5")
        ),
    }

    checks = {
        "generator_exit_zero": proc.returncode == 0,
        "manifest_reproduced_exactly": manifest == rerun,
        "normalization_coordinate": norm.get("coordinate") == "ordinary z with s=z/Q^2",
        "normalization_pre_Phi_K": norm.get("pre_Phi_K") is True,
        "normalization_mixed_input_scaled": norm.get("mixed_input")
        == "M_i^[a] = Gr_a(mathfrak D_Q delta N_i^lin)",
        "normalization_tags": norm.get("tags") == ["1", "2"],
        "normalization_grades": norm.get("grades") == ["1", "5"],
        "normalization_order": norm.get("order") == 7,
        "count_baseline_10": counts.get("baseline_q_derivatives") == 10,
        "count_source_32": counts.get("source_r_derivatives") == 32,
        "count_total_42": counts.get("total") == 42,
        "removable_passed": removable.get("passed") is True,
        "N0_no_negative_powers": removable.get("N0_negative_powers") == [],
        "M_no_negative_powers": removable.get("M_negative_powers") == [],
        "work_order_covers_s3_to_z7": "WORK_ORDER = 10" in src
        and "ORDER = 7" in src
        and "BASE_DERIV_ORDER = 9" in src
        and "SOURCE_DERIV_MAX = 9" in src,
    }
    checks.update({f"source_{k}": v for k, v in source_strings.items()})
    checks.update({f"shape_{k}": v for k, v in shape_checks.items()})

    result = {
        "generator": str(GENERATOR),
        "manifest": str(MANIFEST),
        "rerun_manifest": str(RERUN_MANIFEST),
        "generator_sha1": file_sha1(GENERATOR),
        "manifest_sha1": file_sha1(MANIFEST),
        "rerun_manifest_sha1": file_sha1(RERUN_MANIFEST) if RERUN_MANIFEST.exists() else None,
        "subprocess_returncode": proc.returncode,
        "subprocess_stdout": proc.stdout,
        "subprocess_stderr": proc.stderr,
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "conditional_scope": [
            "demo verifies algebra and schema, not actual zeta source jets",
            "actual finite-grade split r_i^[1], r_i^[5] remains external",
            "script accepts rational Fraction inputs, not arbitrary symbolic expressions",
            "r^(0)=r^(1)=0 is a source-removal convention; invalid inputs are not rejected at parse time",
        ],
    }
    SUMMARY.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "generator_sha1": result["generator_sha1"],
        "manifest_sha1": result["manifest_sha1"],
        "rerun_manifest_sha1": result["rerun_manifest_sha1"],
        "all_checks_passed": result["all_checks_passed"],
        "failed_checks": [k for k, v in checks.items() if not v],
        "summary": str(SUMMARY),
    }, indent=2))
    return 0 if result["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
