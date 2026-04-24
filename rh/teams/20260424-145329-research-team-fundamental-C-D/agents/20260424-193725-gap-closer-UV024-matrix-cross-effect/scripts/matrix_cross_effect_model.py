from collections import defaultdict


def mat_add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def mat_scale(c, a):
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))


def mat_zero():
    return ((0, 0), (0, 0))


def pi_f(a):
    # Projection of [[A,B],[C,D]] to span{I,S}; symmetrize off-diagonal.
    return ((a[0][0] + a[1][1]) / 2, (a[0][1] + a[1][0]) / 2)


def det_f(v, a5):
    return v[0] * a5[1] - a5[0] * v[1]


def is_gauge(v, a5):
    return det_f(v, a5) == 0


def add_vec(a, b):
    return (a[0] + b[0], a[1] + b[1])


def main():
    # Fixed midpoint quotient line A5^f = 2 I + 5 S.
    a5 = (2, 5)

    # Model fixed-sector order-7 coefficient contributions of a matrix
    # cross-effect after pi_f[z^7].  The labels encode source bidegree.
    b7_terms = {
        (1, 1): (7, 11),
        (1, 2): (3, 7),   # cubic (1,1,5)-type witness
        (2, 1): (4, 6),
        (2, 2): (10, 25), # gauge term: 5 * A5
    }

    kept_11 = b7_terms[(1, 1)]
    non11 = (0, 0)
    non11_by_tag = {}
    for tag, value in b7_terms.items():
        if tag != (1, 1):
            non11 = add_vec(non11, value)
            non11_by_tag[tag] = {
                "vector": value,
                "det_coordinate": det_f(value, a5),
                "is_A5_gauge": is_gauge(value, a5),
            }

    print("[conditional_matrix_cross_effect_definition]")
    print("matrix_cross_effect_before_PhiK = W(B+a1L1+a2L2)-W(B+a1L1)-W(B+a2L2)+W(B)")
    print("B7f = pi_f[z^7] matrix_cross_effect")
    print("definition_requires_actual_source_linear_Lh = true")

    print("\n[fixed_sector_terms]")
    print(f"A5_midpoint={a5}")
    print(f"B7f_11={kept_11}")
    print(f"B7f_non11_total={non11}")
    print(f"B7f_non11_det_coordinate={det_f(non11, a5)}")
    print(f"B7f_non11_is_A5_gauge={is_gauge(non11, a5)}")

    print("\n[non11_by_bidegree]")
    for tag in sorted(non11_by_tag):
        print(f"{tag}: {non11_by_tag[tag]}")

    print("\n[cubic_115_witness]")
    witness = b7_terms[(1, 2)]
    print("source_bidegree=(1,2)")
    print("finite_grades=(1,1,5)")
    print("total_grade=7")
    print(f"witness_B7f={witness}")
    print(f"witness_det_coordinate={det_f(witness, a5)}")
    print(f"witness_is_A5_gauge={is_gauge(witness, a5)}")

    print("\n[PhiK_warning]")
    # A term can be hidden by a scalar functional while still surviving in the
    # quotient.  This models why scalar-only checks do not prove UV-024.
    hidden_by_scalar = (3, 7)
    scalar_phi_value = 0
    print(f"hidden_by_scalar_vector={hidden_by_scalar}")
    print(f"scalar_phi_value={scalar_phi_value}")
    print(f"quotient_det_coordinate={det_f(hidden_by_scalar, a5)}")
    print(f"scalar_hidden_but_quotient_visible={scalar_phi_value == 0 and det_f(hidden_by_scalar, a5) != 0}")

    print("\n[conclusion]")
    print("conditional_B7f_definition_is_valid_once_matrix_C_exists = true")
    print("current_source_proves_actual_matrix_C_exists = false")
    print("non11_source_bidegrees_A5_gauge_generically = false")
    print("cubic_115_witness_survives_quotient_generically = true")
    print("promotion_needs_source_theorem_not_scalar_check = true")


if __name__ == "__main__":
    main()
