import numpy as np

amount = 5
x_star = 5.0
derivative_degree = 1

x = np.array([0.0, 1.0, 3.0, 4.0, 5.0]).reshape((amount, 1))
function = np.array([0.5, 0.3, 0.3, 0.2, 0.1]).reshape((amount, 1))

A = np.zeros((amount, amount))

f = np.zeros((amount, 1))
f[derivative_degree, 0] = 1

delta_x = x - x_star

for string_number in range(amount):
    string = (delta_x ** string_number).reshape((1, amount))
    A[string_number, :] = string

c = np.linalg.solve(A, f).reshape((1, amount))
derivative = float(np.dot(c, function))

answer = -0.085
error = np.abs(answer - derivative)

print('Derivative:', derivative)
print('Correct answer:', answer)
print('Error:', error)
