def one_zero(beta, gamma, t, inverse=False):
    rho = complex(beta, gamma)
    s_left = 2j * t
    s_right = 1 + 2j * t
    # Contribution of one zero to d/ds log(Xi(2s-1)/Xi(2s)).
    log_deriv = 2 * (1 / (s_left - rho) - 1 / (s_right - rho))
    if inverse:
        log_deriv = -log_deriv
    kernel = (1 / (s_right - rho) - 1 / (s_left - rho)).real
    return kernel, log_deriv.real


tests = [
    (0.5, 0.0, 0.0),
    (0.25, 1.0, 0.2),
    (0.75, -0.4, -0.1),
]

for beta, gamma, t in tests:
    kernel, fixed = one_zero(beta, gamma, t, inverse=False)
    _, inverted = one_zero(beta, gamma, t, inverse=True)
    print(
        f"beta={beta:g} gamma={gamma:g} t={t:g} "
        f"K={kernel:.12g} fixed_plus_half={0.5 * fixed:.12g} "
        f"fixed_minus_half={-0.5 * fixed:.12g} "
        f"inverse_plus_half={0.5 * inverted:.12g}"
    )
