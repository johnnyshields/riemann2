from itertools import product


SEPTIC_ORDER = 7


def first_visible_by_w_order(min_orders, min_p=3, max_p=6, max_n=SEPTIC_ORDER):
    for p in range(min_p, max_p + 1):
        for orders in product(min_orders, repeat=p):
            n = sum(orders)
            if n <= max_n:
                return p, n, orders
    return None


def mixed_bidegrees(p):
    return [(i, p - i) for i in range(1, p)]


def p_ge3_bidegree_11_survives(max_p=7):
    survivors = {}
    for p in range(3, max_p + 1):
        survivors[p] = (1, 1) in mixed_bidegrees(p)
    return survivors


def first_visible_q7_grade(q7_grade=5, lower_grades=(1, 2, 3, 4), max_p=5):
    atoms = list(lower_grades) + [q7_grade]
    for p in range(3, max_p + 1):
        for grades in product(atoms, repeat=p):
            if grades.count(q7_grade) != 1:
                continue
            if sum(grades) <= SEPTIC_ORDER:
                return p, sum(grades), grades
    return None


def main():
    # From proof_of_rh.tex:2688-2787, after D_Q normalization some weighted
    # entries have no forced positive w-order (G/V channels), while others
    # start at w or w^2. This is the weakest source-supported input order set.
    dq_supported_w_orders = (0, 1, 2)
    visible_w = first_visible_by_w_order(dq_supported_w_orders)

    # If a separate theorem forced all actual quotient-visible input entries to
    # start at w^3, the coefficient bound in prop:differentiated-whitening-transfer
    # would push p>=3 beyond order 7. This is a sufficient condition, not source.
    w3_visible = first_visible_by_w_order((3,))

    # One-pair septic grading says the first genuinely new q^(7) slice enters
    # at finite order 5. Lower order transport/source factors of grade 1 can
    # combine with it to reach grade 7 unless a projection/invisibility theorem
    # removes those higher homogeneous source degrees.
    visible_grade = first_visible_q7_grade(q7_grade=5, lower_grades=(1, 2, 3, 4))

    survivors = p_ge3_bidegree_11_survives()

    print("[dq_w_order_filter]")
    print(f"supported_input_w_orders = {dq_supported_w_orders}")
    print(f"p_ge3_visible_through_order_7 = {visible_w is not None}")
    print(f"first_visible = {visible_w}")
    print(f"w3_divisibility_sufficient = {w3_visible is None}")
    print()

    print("[finite_order_q7_filter]")
    print("q7_first_grade = 5")
    print("lower_source_grades_tested = (1, 2, 3, 4)")
    print(f"p_ge3_with_one_q7_can_reach_septic = {visible_grade is not None}")
    print(f"first_visible = {visible_grade}")
    print()

    print("[source_bidegree_filter]")
    for p in sorted(survivors):
        print(f"p={p}: mixed_bidegrees={mixed_bidegrees(p)} keeps_(1,1)={survivors[p]}")
    print()

    print("[conclusion]")
    print("dq_scaling_alone_excludes_p_ge3 = false")
    print("finite_order_grading_alone_excludes_p_ge3 = false")
    print("bidegree_1_1_projection_would_exclude_p_ge3 = true")
    print("needed_source_statement = projection_or_quotient_invisibility_or_w3_divisibility")


if __name__ == "__main__":
    main()
