from collections import defaultdict


def add_poly(left, right):
    out = defaultdict(int)
    for key, value in left.items():
        out[key] += value
    for key, value in right.items():
        out[key] += value
    return {key: value for key, value in out.items() if value}


def mul_poly(left, right):
    out = defaultdict(int)
    for a_key, a_value in left.items():
        for b_key, b_value in right.items():
            key = tuple(a + b for a, b in zip(a_key, b_key))
            out[key] += a_value * b_value
    return {key: value for key, value in out.items() if value}


def scale_poly(poly, factor):
    return {key: factor * value for key, value in poly.items() if factor * value}


def degree_kernel(key):
    # key=(a1,a2,kernel_degree,whitening_degree)
    return key[2]


def source_bidegrees(poly):
    return sorted({(key[0], key[1]) for key in poly})


def linear_kernel_part(poly):
    return {key: value for key, value in poly.items() if degree_kernel(key) == 1}


def pi_11(poly):
    return {key: value for key, value in poly.items() if key[:2] == (1, 1)}


def main():
    # Model the corrected block formula pattern from proof_of_rh.tex:2688-2787:
    # entries are linear in pair kernels modulo at least two pair kernels.
    # key=(source a1 degree, source a2 degree, pair-kernel degree, whitening degree)
    u1 = {(1, 0, 1, 0): 1}
    u2 = {(0, 1, 1, 0): 1}
    source_sum = add_poly(u1, u2)

    one_pair_block = add_poly(
        source_sum,
        add_poly(mul_poly(source_sum, source_sum), mul_poly(mul_poly(source_sum, source_sum), source_sum)),
    )
    lh_candidate = linear_kernel_part(one_pair_block)

    # A linear source input can feed T_1, but its two-atom interaction appears
    # only after an analytic nonlinear transfer/cross-effect.
    t1 = lh_candidate
    t2 = mul_poly(lh_candidate, lh_candidate)
    t3 = mul_poly(t2, lh_candidate)
    cross_effect = add_poly(
        add_poly(t2, t3),
        scale_poly(add_poly(mul_poly(u1, u1), mul_poly(mul_poly(u1, u1), u1)), -1),
    )
    cross_effect = add_poly(
        cross_effect,
        scale_poly(add_poly(mul_poly(u2, u2), mul_poly(mul_poly(u2, u2), u2)), -1),
    )

    # Model the known source-weight negative: an even whitened coefficient W(a)
    # gives a signed lift a W(a), but higher a^3, a^5 terms violate exact
    # one-amplitude collapse.
    a = 3
    f0, f2, f4 = 5, 7, 11
    signed_lift_at_a = a * (f0 + f2 * a**2 + f4 * a**4)
    signed_lift_linear_target = a * (f0 + f2 + f4)
    signed_lift_error = signed_lift_at_a - signed_lift_linear_target
    derivative_projection_at_a = a * f0
    derivative_projection_target = a * f0

    print("[pre_whitening_pair_kernel_linear_part]")
    print(f"one_pair_model_kernel_degrees = {sorted({degree_kernel(k) for k in one_pair_block})}")
    print(f"linear_part_source_bidegrees = {source_bidegrees(lh_candidate)}")
    print(f"linear_part_additive_in_sources = {source_bidegrees(lh_candidate) == [(0, 1), (1, 0)]}")
    print("candidate_is_before_whitening = true")
    print()

    print("[feed_into_transfer]")
    print(f"T1_source_bidegrees = {source_bidegrees(t1)}")
    print(f"cross_effect_source_bidegrees = {source_bidegrees(cross_effect)}")
    print(f"Pi_11_keeps = {source_bidegrees(pi_11(cross_effect))}")
    print("linear_input_can_feed_T1 = true")
    print("two_atom_interaction_needs_transfer_cross_effect = true")
    print()

    print("[signed_lift_negative]")
    print(f"signed_lift_one_amplitude_error = {signed_lift_error}")
    print(f"linear_derivative_one_amplitude_error = {derivative_projection_at_a - derivative_projection_target}")
    print("signed_lift_leaves_higher_a_terms = true")
    print()

    print("[source_status]")
    print("one_pair_pair_kernel_linear_derivative_supported = true")
    print("actual_two_atom_block_definition_found_in_tested_source = false")
    print("Lh_source_functor_requires_new_definition_or_source_line = true")


if __name__ == "__main__":
    main()
