import numpy as np


def make_seid_iter(a, column, x, n):
    dim = np.shape(a)[0]
    column_transposed = column.T

    up = np.zeros((dim, dim))
    low = np.zeros((dim, dim))

    # Build low and up
    for i in range(dim):
        for j in range(dim):
            if i >= j:
                low[i, j] = a[i, j]
            else:
                up[i, j] = a[i, j]

    low_rev = np.linalg.inv(low)
    operator = np.dot(low_rev, up)
    term = np.dot(low_rev, column_transposed)

    # Iterations
    for i in range(n):
        x = - np.dot(operator, x) + term
        print("Iter:", i + 1, "sol:", x)


matrix = np.matrix([[18, 0, 6],
                    [0, 18, -7],
                    [6, -7, 6]])
right = np.array([90, 150, 102])
x_start = np.array([0, 1, 0])
make_seid_iter(matrix, right, x_start, 3)
