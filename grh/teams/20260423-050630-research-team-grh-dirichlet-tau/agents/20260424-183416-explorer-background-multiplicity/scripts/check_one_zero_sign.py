from fractions import Fraction


def real_part(z):
    return z.real


beta = Fraction(1, 2)
gamma = Fraction(0, 1)
t = Fraction(0, 1)

# Contribution of one simple zero rho=beta+i gamma to
# d/ds log(Xi(2s-1)/Xi(2s)) at s=1/2+i t.
# At t=0 and gamma=0 this is real, so complex arithmetic is avoidable.
log_derivative_contribution = 2 * (
    Fraction(1, 1) / (2j * float(t) - float(beta) - 1j * float(gamma))
    - Fraction(1, 1) / (1 + 2j * float(t) - float(beta) - 1j * float(gamma))
)

kernel = real_part(
    1 / (1 + 2j * float(t) - float(beta) - 1j * float(gamma))
    - 1 / (2j * float(t) - float(beta) - 1j * float(gamma))
)

print(f"log_derivative_contribution={log_derivative_contribution.real:g}")
print(f"positive_kernel={kernel:g}")
print(f"minus_half_log_derivative={(-0.5 * log_derivative_contribution).real:g}")
print(f"plus_half_log_derivative={(0.5 * log_derivative_contribution).real:g}")
