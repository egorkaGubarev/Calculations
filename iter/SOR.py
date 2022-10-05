import numpy as np


def make_sor_iter(a, f, x0, tau, iterations):
    strings, columns = np.shape(a)
    diagonal = np.zeros((strings, columns))
    up = np.zeros((strings, columns))

    for i in range(strings):
        diagonal[i, i] = a[i, i]
        for j in range(i + 1, columns):
            up[i, j] = a[i, j]
    low = a - up - diagonal
    tmp = np.linalg.inv(diagonal + tau * low)
    b = tau * tmp @ f
    B = -tmp @ (tau * up + (tau - 1) * diagonal)
    x = x0

    for i in range(iterations):
        x = B @ x + b
        print("Iter:", i + 1, "sol:", x)


matrix = np.matrix([[18, 0, 6],
                    [0, 18, -7],
                    [6, -7, 6]])
right = np.array([90, 150, 102]).reshape((3, 1))
x_start = np.array([0, 1, 0]).reshape((3, 1))
make_sor_iter(matrix, right, x_start, 1.4, 25)
