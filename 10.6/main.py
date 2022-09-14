import numpy as np


def gauss_pivot(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    dim = len(b)

    for k in range(dim):

        # pivoting
        for i_1 in range(k + 1, dim):
            if np.fabs(a[i_1, k]) > np.fabs(a[k, k]):
                for j_1 in range(k, dim):
                    a[k, j_1], a[i_1, j_1] = a[i_1, j_1], a[k, j_1]
                b[k], b[i_1] = b[i_1], b[k]
        # end of pivoting

        pivot = a[k, k]
        for j_1 in range(k, dim):
            a[k, j_1] /= pivot
        b[k] /= pivot
        for i_1 in range(dim):
            if i_1 == k or a[i_1, k] == 0:
                continue
            factor = a[i_1, k]
            for j_1 in range(k, dim):
                a[i_1, j_1] -= factor * a[k, j_1]
            b[i_1] -= factor * b[k]
    return b


def diagonalize(a, dim):
    a = np.array(a, float)
    for k in range(dim):

        # pivoting
        for i_1 in range(k + 1, dim):
            if np.fabs(a[i_1, k]) > np.fabs(a[k, k]):
                for j_1 in range(k, dim):
                    a[k, j_1], a[i_1, j_1] = a[i_1, j_1], a[k, j_1]
        # end of pivoting

        for i_1 in range(k, dim):
            if i_1 == k or a[i_1, k] == 0:
                continue
            factor = a[i_1, k] / a[k, k]
            for j_1 in range(k, dim):
                a[i_1, j_1] -= factor * a[k, j_1]
    return a


n = 20
a_diagonal = 10

# Creating matrix
E = np.eye(n)
A = a_diagonal * E
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            i_pos = i + 1
            j_pos = j + 1
            A[i, j] = 1 / (i_pos + j_pos)

# Creating column
f = np.zeros(n)
for i in range(0, n):
    i_pos = i + 1
    f[i] = 1 / i_pos

answer = gauss_pivot(A, f)
print("Answer:", answer)

Diagonal = diagonalize(A, n)
lambdas = np.diagonal(Diagonal)
lambda_min = np.min(lambdas)
lambda_max = np.max(lambdas)
print("Lambda min:", lambda_min)
print("Lambda max:", lambda_max)

abs_lambdas = np.abs(lambdas)
abs_lambda_min = np.min(abs_lambdas)
abs_lambda_max = np.max(abs_lambdas)
mu = abs_lambda_max / abs_lambda_min
print("Mu:", mu)

count_column = A.dot(answer)
delta = f - count_column
print("Deltas:", delta)
