import numpy as np


def get_integral(k, left, right, c0, c1, c2, c3):
    integral_0 = c0 * (np.cos(k * left) - np.cos(k * right)) / k
    integral_1 = c1 * (k * (left - right) * np.cos(right * k) - np.sin(left * k) + np.sin(right * k)) / (k ** 2)
    integral_2 = c2 * (-(k ** 2 * (left - right) ** 2 - 2) * np.cos(right * k)
                       + 2 * k * (right - left) * np.sin(right * k) - 2 * np.cos(left * k)) / (k ** 3)
    integral_3 = c3 * (3 * (k ** 2 * (left - right) ** 2 - 2) * np.sin(right * k) +
                       k * (left - right) * (k ** 2 * (left - right) ** 2 - 6) * np.cos(right * k) +
                       6 * np.sin(left * k)) / (k ** 4)
    integral = integral_0 + integral_1 + integral_2 + integral_3
    return integral


n = 4
omega = 30
f = np.zeros(n + 1).reshape(n + 1, 1)
f[0] = 1
f[1] = 1.5403
f[2] = 1.5839
f[3] = 2.01
f[4] = 3.3464

A = np.zeros((n + 1, n + 1))
a = np.zeros(n).reshape(n, 1)
b = np.zeros(n).reshape(n, 1)
d = np.zeros(n).reshape(n, 1)
df = np.zeros(n + 1).reshape(n + 1, 1)

a[0: n] = f[0: n]

# Find c
A[0, 0] = 1
A[n, n] = 1

for i in range(1, n):
    A[i, i - 1] = 1 / 2
    A[i, i + 1] = 1 / 2
    A[i, i] = 2

    df[i] = 3 * (f[i + 1] - 2 * f[i] + f[i - 1]) / 2

c = np.linalg.solve(A, df)

# Find b
for i in range(n):
    b[i] = f[i + 1] - f[i] - (c[i + 1] + 2 * c[i]) / 3

# Find d
for i in range(n):
    d[i] = (c[i + 1] - c[i]) / 3

term_0 = get_integral(omega, 0, 1, a[0, 0], b[0, 0], c[0, 0], d[0, 0])
term_1 = get_integral(omega, 1, 2, a[1, 0], b[1, 0], c[1, 0], d[1, 0])
term_2 = get_integral(omega, 2, 3, a[2, 0], b[2, 0], c[2, 0], d[2, 0])
term_3 = get_integral(omega, 3, 4, a[3, 0], b[3, 0], c[3, 0], d[3, 0])

result = term_0 + term_1 + term_2 + term_3
print(result)
