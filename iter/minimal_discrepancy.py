import numpy as np


def get_discrepancy(a, sol_col, right_col):
    count_col = a.dot(sol_col)
    discrepancy = right_col - count_col
    return discrepancy


def make_min_discrepancy_iter(a, f, x0, iterations):
    # Iterating
    for i in range(iterations):
        discrepancy = get_discrepancy(a, x0, f)

        ar = np.dot(a, discrepancy)
        ar_string = ar.T

        t = np.dot(ar_string, discrepancy) / np.dot(ar_string, ar)
        x0 = x0 + t[0, 0] * discrepancy
        print("Iter:", i + 1, "sol:", x0)


matrix = np.matrix([[18, 6, 0],
                    [6, 6, -7],
                    [0, -7, 18]])
right = np.array([90, 102, 150]).reshape((3, 1))
x_start = np.array([0, 0, 1]).reshape((3, 1))
make_min_discrepancy_iter(matrix, right, x_start, 1)
