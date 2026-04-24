"""Order bookkeeping for UV-023 transfer-filtration.

The paper's corrected-whitening transfer gives coefficient bounds for
T_{p,n}. This script checks what those bounds alone can rule out for the
order-7 quotient channel.
"""

from itertools import product


MAX_ORDER = 7
MAX_P = 8


def first_visible_partition(min_input_order, p):
    for n in range(MAX_ORDER + 1):
        for parts in product(range(min_input_order, n + 1), repeat=p):
            if sum(parts) <= n:
                return n, parts
    return None


print("[coefficient_order_filter]")
for min_order in range(5):
    witness = None
    for p in range(3, MAX_P + 1):
        current = first_visible_partition(min_order, p)
        if current is not None:
            witness = (p, current[0], current[1])
            break
    print(f"input_min_w_order = {min_order}")
    print(f"higher_p_visible_through_7 = {witness is not None}")
    if witness is not None:
        p, n, parts = witness
        print(f"first_visible = p:{p}, n:{n}, input_orders:{parts}")
    else:
        print("first_visible = none")

print()
print("[source_degree_filter]")
for p in range(2, 7):
    mixed_bidegrees = [(i, p - i) for i in range(1, p)]
    contains_11 = (1, 1) in mixed_bidegrees
    print(f"homogeneous_degree = {p}")
    print(f"mixed_bidegrees = {mixed_bidegrees}")
    print(f"bidegree_1_1_projection_keeps = {contains_11}")
    print(f"full_cross_effect_has_mixed_terms = {bool(mixed_bidegrees)}")

print()
print("[conclusion]")
print("coefficient_bound_alone_kills_p_ge_3_through_order_7 = false")
print("sufficient_input_w_order_for_p_ge_3_invisibility = 3")
print("bidegree_1_1_projection_kills_p_ge_3_by_source_degree = true")
