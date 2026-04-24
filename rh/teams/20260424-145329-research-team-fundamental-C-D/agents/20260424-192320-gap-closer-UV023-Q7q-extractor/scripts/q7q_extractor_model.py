from collections import defaultdict


def add(v, w):
    return (v[0] + w[0], v[1] + w[1])


def det(v, a):
    return v[0] * a[1] - a[0] * v[1]


def sum_terms(terms):
    total = (0, 0)
    for v in terms.values():
        total = add(total, v)
    return total


def select_bidegree(terms, keep):
    return {k: v for k, v in terms.items() if k == keep}


def complement_bidegree(terms, keep):
    return {k: v for k, v in terms.items() if k != keep}


def q_class_zero(v, a5):
    # On a nonzero A5 line in the 2D fixed sector, det(v, A5)=0 is equivalent
    # to v lying in C A5, hence to zero in f / C A5.
    return det(v, a5) == 0


def bad_nonlinear_scalar_extractor(terms, a5):
    # Model a post-quotient/post-scalar nonlinear extraction. This is not a
    # proposed definition; it is the adversarial warning that bidegree
    # projection arguments need a linear fixed-target coefficient extractor.
    s = det(sum_terms(terms), a5)
    return s * s


def main():
    a5_midpoint = (2, 5)

    # Vectors are fixed-sector coefficients u I + v S in the target
    # f / C A5(m).  The cubic entries model a finite-order witness of total
    # grade (1,1,5) reaching septic order through a p=3 transfer.
    terms = {
        (1, 1): (7, 11),   # quadratic transfer, desired source bidegree
        (1, 2): (3, 7),    # cubic (1,1,5)-type witness, nonzero quotient class
        (2, 1): (4, 6),    # another non-(1,1) source bidegree
    }

    pi11_terms = select_bidegree(terms, (1, 1))
    non11_terms = complement_bidegree(terms, (1, 1))

    q_full = sum_terms(terms)
    q_pi11 = sum_terms(pi11_terms)
    q_non11 = sum_terms(non11_terms)

    print("[fixed_target_quotient_extractor]")
    print(f"A5_midpoint={a5_midpoint}")
    print(f"Q7q_full_vector={q_full}")
    print(f"Q7q_pi11_vector={q_pi11}")
    print(f"Q7q_non11_vector={q_non11}")
    print(f"Q7q_non11_det_coordinate={det(q_non11, a5_midpoint)}")
    print(f"Q7q_non11_zero_in_quotient={q_class_zero(q_non11, a5_midpoint)}")

    print("\n[representative_gauge_check]")
    gauge_shift = (4, 10)  # 2 * A5_midpoint
    shifted_witness = add(terms[(1, 2)], gauge_shift)
    print(f"witness_det={det(terms[(1, 2)], a5_midpoint)}")
    print(f"shifted_witness_det={det(shifted_witness, a5_midpoint)}")
    print(f"gauge_independent={det(terms[(1, 2)], a5_midpoint) == det(shifted_witness, a5_midpoint)}")

    print("\n[cubic_115_witness]")
    print("witness_grade=(1,1,5)")
    print("total_grade=7")
    print(f"witness_vector={terms[(1, 2)]}")
    print(f"witness_det_coordinate={det(terms[(1, 2)], a5_midpoint)}")
    print(f"witness_survives_fixed_Q7q={not q_class_zero(terms[(1, 2)], a5_midpoint)}")

    print("\n[nonlinear_extraction_warning]")
    nonlinear_full = bad_nonlinear_scalar_extractor(terms, a5_midpoint)
    nonlinear_pi11 = bad_nonlinear_scalar_extractor(pi11_terms, a5_midpoint)
    nonlinear_non11 = bad_nonlinear_scalar_extractor(non11_terms, a5_midpoint)
    print(f"bad_nonlinear_full={nonlinear_full}")
    print(f"bad_nonlinear_pi11={nonlinear_pi11}")
    print(f"bad_nonlinear_non11={nonlinear_non11}")
    print(f"bad_nonlinear_additive_over_bidegrees={nonlinear_full == nonlinear_pi11 + nonlinear_non11}")

    print("\n[conclusion]")
    print("fixed_target_Q7q_can_be_linear_and_quotient_valued = true")
    print("determinant_is_only_a_good_patch_coordinate = true")
    print("fixed_Q7q_kills_non_11_generically = false")
    print("compatibility_needs_quotient_invisibility_theorem = true")
    print("current_source_defines_matrix_valued_cross_effect_coefficient = false")


if __name__ == "__main__":
    main()
