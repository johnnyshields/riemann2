from collections import defaultdict


def mixed_bidegrees(p):
    return [(i, p - i) for i in range(1, p)]


def build_formal_cross_effect(max_degree=7):
    """Return symbolic source-bidegree coefficients for a generic cross-effect.

    A homogeneous degree-p transfer contributes mixed source bidegrees
    (i, p-i), 1 <= i <= p-1.  The symbol c_p_i records an independent
    possible order-7 quotient coefficient in that bidegree.
    """
    coeffs = defaultdict(list)
    for p in range(2, max_degree + 1):
        for i, j in mixed_bidegrees(p):
            coeffs[(i, j)].append(f"c{p}_{i}{j}")
    return coeffs


def pi_11(coeffs):
    return {(1, 1): coeffs.get((1, 1), [])}


def q7_terms(coeffs):
    terms = []
    for bideg in sorted(coeffs):
        terms.extend(coeffs[bideg])
    return terms


def main():
    coeffs = build_formal_cross_effect()
    projected = pi_11(coeffs)

    print("[formal_source_bidegrees]")
    for p in range(2, 8):
        print(f"p={p} mixed_bidegrees={mixed_bidegrees(p)}")

    print("\n[Pi_11]")
    print(f"kept_terms={q7_terms(projected)}")
    killed_terms={k: v for k, v in coeffs.items() if k != (1, 1)}
    print(f"killed_bidegrees={sorted(killed_terms)}")

    full_q7 = q7_terms(coeffs)
    projected_q7 = q7_terms(projected)
    obstruction = [term for term in full_q7 if term not in projected_q7]

    print("\n[generic_Q7_compatibility]")
    print(f"Q7_full_terms={full_q7}")
    print(f"Q7_projected_terms={projected_q7}")
    print(f"compatibility_holds_generically={len(obstruction) == 0}")
    print(f"obstruction_terms={obstruction}")

    print("\n[compatibility_if_non_11_quotient_invisible]")
    filtered = {(1, 1): coeffs[(1, 1)]}
    print(f"Q7_filtered_terms={q7_terms(filtered)}")
    print(f"Q7_filtered_equals_projected={q7_terms(filtered) == projected_q7}")

    print("\n[conclusion]")
    print("source_tags_and_Pi_11_are_formal_once_X1_is_source_linear = true")
    print("Pi_11_alone_implies_Q7_compatibility = false")
    print("needed_source_statement = Q7q_kills_all_non_11_source_bidegrees")


if __name__ == "__main__":
    main()
