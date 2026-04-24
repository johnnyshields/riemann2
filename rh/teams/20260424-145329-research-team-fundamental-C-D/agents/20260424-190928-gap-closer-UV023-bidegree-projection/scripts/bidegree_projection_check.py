from collections import defaultdict
from math import comb


def cross_effect_bidegrees(p):
    """Mixed source bidegrees of (aX + bY)^p - (aX)^p - (bY)^p."""
    terms = defaultdict(int)
    for i in range(p + 1):
        j = p - i
        coeff = comb(p, i)
        if i == p and j == 0:
            coeff -= 1
        if i == 0 and j == p:
            coeff -= 1
        if coeff:
            terms[(i, j)] += coeff
    return {k: v for k, v in terms.items() if k[0] > 0 and k[1] > 0}


def project_11(terms):
    return {k: v for k, v in terms.items() if k == (1, 1)}


def main():
    print("[formal_cross_effect_bidegrees]")
    all_higher_killed = True
    for p in range(1, 8):
        mixed = cross_effect_bidegrees(p)
        projected = project_11(mixed)
        if p >= 3 and projected:
            all_higher_killed = False
        print(
            f"p={p} mixed_bidegrees={sorted(mixed)} "
            f"projection_11={projected if projected else 'none'}"
        )

    print()
    print("[conclusion]")
    print(f"bidegree_11_keeps_quadratic_transfer = {bool(project_11(cross_effect_bidegrees(2)))}")
    print(f"bidegree_11_kills_p_ge_3_formally = {all_higher_killed}")
    print("requires_source_defined_projection_before_quotient = true")
    print("requires_commutation_with_order7_quotient_extraction = true")


if __name__ == "__main__":
    main()
