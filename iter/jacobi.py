import numpy as np


def make_jacobi_iter(a, f, x, n):
    dim = np.shape(a)[0]
    low = np.zeros((dim, dim))
    up = np.zeros((dim, dim))
    diagonal = np.zeros((dim, dim))

    # Building low up and diagonal
    for i in range(dim):
        for j in range(dim):
            if i < j:
                up[i, j] = a[i, j]
            elif i == j:
                diagonal[i, i] = a[i, i]
            else:
                low[i, j] = a[i, j]

    diagonal_inv = np.linalg.inv(diagonal)
    operator = - np.dot(diagonal_inv, low + up)
    term = np.dot(diagonal_inv, f.T)

    # Iterating
    for i in range(n):
        x = np.dot(operator, x) + term
        print("Iter:", i + 1, "sol:", x)


matrix = np.matrix([[18, 6, 0], [6, 6, -7], [0, -7, 18]])
right = np.array([90, 102, 150])
x_start = np.array([0, 0, 1])
make_jacobi_iter(matrix, right, x_start, 3)
