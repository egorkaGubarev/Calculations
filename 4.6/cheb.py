import numpy as np


def t0(x):
    return 1


def t1(x):
    return x


def t2(x):
    return 2 * x ** 2 - 1


def t3(x):
    return x * (4 * x ** 2 - 3)


def t4(x):
    return 8 * x ** 4 - 8 * x ** 2 + 1


def get_chebyshev_coeff_3_order(y, polynomials):
    roots_amount = 4
    coeff_amount = 4

    roots = np.zeros(roots_amount)
    coeff_list = np.zeros(coeff_amount)

    # Get roots
    for root_numb in range(roots_amount):
        root = np.cos(np.pi * (1 + 2 * root_numb) / (2 * roots_amount))
        roots[root_numb] = root

    # Get coefficients
    for coeff_numb in range(coeff_amount):
        part_sum = 0

        # Summing polynomials
        for term_numb in range(roots_amount):
            root = roots[term_numb]
            polynomial = polynomials[coeff_numb]
            part_sum += y[term_numb] * polynomial(root)

        coeff = 2 * part_sum / coeff_amount
        coeff_list[coeff_numb] = coeff

    coeff_list[0] /= 2

    return coeff_list


values = np.array([2.0, 1.0, 3.0, 0.0])
chebyshev = np.array([t0, t1, t2, t3, t4])
result = get_chebyshev_coeff_3_order(values, chebyshev)
print("Coeff:", result)
