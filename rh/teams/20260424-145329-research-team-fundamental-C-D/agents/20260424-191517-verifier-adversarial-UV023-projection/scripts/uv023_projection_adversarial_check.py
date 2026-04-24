from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Term:
    label: str
    source_bidegree: tuple[int, int] | None
    finite_grade: int
    homogeneous_degree: int


def pi_11(terms: Iterable[Term]) -> list[Term]:
    return [term for term in terms if term.source_bidegree == (1, 1)]


def scalarize(terms: Iterable[Term]) -> list[Term]:
    """Determinant/scalar quotient chart after source tags have been forgotten."""
    return [
        Term(
            label=f"scalar({term.label})",
            source_bidegree=None,
            finite_grade=term.finite_grade,
            homogeneous_degree=term.homogeneous_degree,
        )
        for term in terms
    ]


def linear_q7(terms: Iterable[Term]) -> list[Term]:
    return [term for term in terms if term.finite_grade == 7]


def nonlinear_q7(terms: Iterable[Term]) -> list[Term]:
    """Toy quotient extraction with a cubic ratio/normalization correction.

    The correction models the hidden assumption under attack: a quotient or
    scalar extraction may combine lower pieces before source-bidegree projection.
    """
    result = linear_q7(terms)
    labels = {term.label for term in terms}
    if {"single_a_grade1", "single_b_grade1", "source_free_q7_grade5"} <= labels:
        result.append(Term("nonlinear_Q(single_a*single_b*q7)", (1, 1), 7, 3))
    return result


def labels(terms: Iterable[Term]) -> list[str]:
    return [term.label for term in terms]


def main() -> None:
    cross_effect_terms = [
        Term("T2_bidegree_11", (1, 1), 7, 2),
        Term("T3_cubic_witness_12_grade_115", (1, 2), 7, 3),
        Term("T3_cubic_witness_21_grade_115", (2, 1), 7, 3),
    ]
    package_terms = [
        *cross_effect_terms,
        Term("single_a_grade1", (1, 0), 1, 1),
        Term("single_b_grade1", (0, 1), 1, 1),
        Term("source_free_q7_grade5", (0, 0), 5, 1),
    ]

    pre_projection = pi_11(cross_effect_terms)
    scalarized = scalarize(cross_effect_terms)
    full_then_project = pi_11(nonlinear_q7(package_terms))
    project_then_q = nonlinear_q7(pi_11(package_terms))

    diagonal_value_zero = True
    first_collision_derivative_zero = False
    delta2_divisible = diagonal_value_zero and first_collision_derivative_zero

    print("[pre_quotient_bidegree_projection]")
    print(f"kept_terms = {labels(pre_projection)}")
    print(
        "kills_p_ge_3 = "
        f"{all(term.homogeneous_degree < 3 for term in pre_projection)}"
    )
    print()

    print("[after_determinant_scalarization]")
    print(f"visible_grade7_scalars = {labels(linear_q7(scalarized))}")
    print("source_tags_available_after_scalarization = false")
    print("posthoc_pi_11_well_defined = false")
    print()

    print("[quotient_extraction_commutation_test]")
    print(f"pi_11_after_Q = {labels(full_then_project)}")
    print(f"Q_after_pi_11 = {labels(project_then_q)}")
    print(f"commutes = {labels(full_then_project) == labels(project_then_q)}")
    print()

    print("[finite_order_cubic_witness]")
    print("witness_grades = (1, 1, 5)")
    print("total_grade = 7")
    print("can_reach_septic_channel = true")
    print("excluded_by_raw_finite_order_grading = false")
    print("excluded_by_pre_quotient_pi_11 = true")
    print()

    print("[diagonal_value_vs_edge_divisibility]")
    print(f"diagonal_value_zero = {str(diagonal_value_zero).lower()}")
    print(
        "first_collision_derivative_zero = "
        f"{str(first_collision_derivative_zero).lower()}"
    )
    print(f"delta2_divisible = {str(delta2_divisible).lower()}")


if __name__ == "__main__":
    main()
