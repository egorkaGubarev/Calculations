import numpy as np


def gauss_pivot(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    dim = len(b)

    for k in range(dim):

        # pivoting
        for i in range(k + 1, dim):
            if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                for j in range(k, dim):
                    a[k, j], a[i, j] = a[i, j], a[k, j]
                b[k], b[i] = b[i], b[k]
        # end of pivoting

        pivot = a[k, k]
        for j in range(k, dim):
            a[k, j] /= pivot
        b[k] /= pivot
        for i in range(dim):
            if i == k or a[i, k] == 0:
                continue
            factor = a[i, k]
            for j in range(k, dim):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]
    return b


def get_rand_vect(dim):
    vect = np.zeros(dim)
    for coord_num in range(0, dim):
        coord = np.random.rand()
        vect[coord_num] = coord
    column = vect.T
    return column


# Rotation of vector to the direction of eigenvector
def get_max_abs_eigenvalue(matrix, epsilon=1e-16):
    dim = np.shape(matrix)[0]
    vect = get_rand_vect(dim)
    length_prev = 0
    epsilon_curr = 1

    # Rotation
    while epsilon_curr > epsilon:
        image = np.dot(matrix, vect)
        length = np.sqrt(np.dot(image.T, image))
        normal = image / length

        delta_length = length - length_prev
        epsilon_curr = np.abs(delta_length / length)

        vect = normal
        length_prev = length

    return length_prev


def get_discrepancy(matrix, sol_col, right_col):
    count_col = matrix.dot(sol_col)
    discrepancy = right_col - count_col
    return discrepancy


def get_low_up(matrix):
    dim = np.shape(matrix)[0]

    low = np.zeros((dim, dim))
    up = np.zeros((dim, dim))

    # Initial values
    for i in range(dim):
        for j in range(dim):
            up[i, j] = 0
            low[i, j] = 0
            low[i, i] = 1

    # Build low and up
    for i in range(dim):
        for j in range(dim):
            part_sum = 0
            if i <= j:
                for k in range(i):
                    part_sum += low[i, k] * up[k, j]
                up[i, j] = matrix[i, j] - part_sum
            else:
                for k in range(j):
                    part_sum += low[i, k] * up[k, j]
                low[i, j] = (matrix[i, j] - part_sum) / up[j, j]

    return low, up


def get_rev_up(up):
    dim = np.shape(up)[0]
    rev = np.zeros((dim, dim))

    for i in range(dim):
        for j in range(dim):
            if i == j:
                rev[i, j] = 1 / up[i, j]
            elif i > j:
                rev[i, j] = 0
            else:
                part_sum = 0
                for k in range(i + 1):
                    part_sum += rev[i, k] * up[k, j]
                rev[i, j] = -part_sum / up[j, j]

    return rev


def get_rev_low(low):
    up = low.T
    rev_up_matrix = get_rev_up(up)
    rev = rev_up_matrix.T
    return rev


def get_min_abs_eigenvalue(matrix, epsilon=1e-16):
    low, up = get_low_up(matrix)

    up_rev = get_rev_up(up)
    low_rev = get_rev_low(low)

    rev = np.dot(up_rev, low_rev)
    rev_eigen = get_max_abs_eigenvalue(rev, epsilon)
    eigen = 1 / rev_eigen
    return eigen


def solve_by_seidel(matrix, column, epsilon=1e-2):
    dim = np.shape(matrix)[0]
    column_transposed = column.T

    up = np.zeros((dim, dim))
    low = np.zeros((dim, dim))

    # Build low and up
    for i in range(dim):
        for j in range(dim):
            if i >= j:
                low[i, j] = matrix[i, j]
            else:
                up[i, j] = matrix[i, j]

    low_rev = get_rev_low(low)
    operator = np.dot(low_rev, up)
    res_prev = np.zeros(dim).T
    converged = False

    # Iterations
    while not converged:
        res = - np.dot(operator, res_prev) + np.dot(low_rev, column_transposed)
        discrepancy = get_discrepancy(matrix, res, column_transposed)

        epsilon_curr = np.dot(discrepancy.T, discrepancy) / np.dot(res.T, res)

        # Convergence check
        if np.abs(epsilon_curr) < epsilon:
            converged = True

        res_prev = res

    return res_prev


# Data for matrix creation
n = 20
a_diagonal = 10

# Creating matrix
E = np.eye(n)
A = a_diagonal * E
for string_numb in range(0, n):
    for col_numb in range(0, n):
        if string_numb != col_numb:
            i_pos = string_numb + 1
            j_pos = col_numb + 1
            A[string_numb, col_numb] = 1 / (i_pos + j_pos)

# Creating column
f = np.zeros(n)
for string_numb in range(0, n):
    i_pos = string_numb + 1
    f[string_numb] = 1 / i_pos

# Solution
answer = gauss_pivot(A, f)
print("Answer:", answer)

# Seidel solution
answer_seid = solve_by_seidel(A, f)
print("Seidel answer:", answer_seid)

# Max eigenvalue
max_eigen = get_max_abs_eigenvalue(A)
print("Max eigenvalue:", max_eigen)

# Min eigenvalue
min_eigen = get_min_abs_eigenvalue(A)
print("Min eigenvalue:", min_eigen)

# Condition number
mu = max_eigen * min_eigen
print("Condition number:", mu)

# Discrepancy
delta = get_discrepancy(A, answer, f)
print("Discrepancy:", delta)

# Discrepancy seidel
delta = get_discrepancy(A, answer_seid, f)
print("Seidel discrepancy:", delta)

# Test
print("----- Test -----")

test_matrix = np.zeros((2, 2))
test_matrix[0, 0] = 6
test_matrix[0, 1] = 6
test_matrix[1, 0] = 6
test_matrix[1, 1] = 4

test_column = np.zeros(2)
test_column[0] = 5
test_column[1] = -6

solution = gauss_pivot(test_matrix, test_column)
max_test = get_max_abs_eigenvalue(test_matrix)
min_test = get_min_abs_eigenvalue(test_matrix)
test_discrepancy = get_discrepancy(test_matrix, solution, test_column)
low_test, up_test = get_low_up(test_matrix)
rev_up = get_rev_up(up_test)
rev_low = get_rev_low(low_test)

print("Solution:", solution)
print("Max eigenvalue:", max_test)
print("Min eigenvalue:", min_test)
print("Discrepancy:", test_discrepancy)
print("Low:", low_test)
print("Up:", up_test)
print("Reversed up:", rev_up)
print("Reversed low:", rev_low)
