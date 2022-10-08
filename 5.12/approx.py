import numpy as np
import matplotlib.pyplot as plt


def get_least_square_coefficients(x, y):
    n = len(x)

    xx = x * x
    xy = x * y

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(xx)
    sum_xy = sum(xy)

    denominator = (n + 1) * sum_xx - sum_x ** 2

    k_loc = ((n + 1) * sum_xy - sum_x * sum_y) / denominator
    b_loc = (sum_y * sum_xx - sum_xy * sum_x) / denominator

    coefficients = (k_loc, b_loc)
    return coefficients


def plot_least_squares(x, y, ax_loc):
    (k, b) = get_least_square_coefficients(x, y)

    min_x = min(x)
    max_x = max(x)

    min_y = k * min_x + b
    max_y = k * max_x + b

    ax_loc.plot(x, y, '.')
    ax_loc.plot([min_x, max_x], [min_y, max_y])

    return ax_loc


years = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                  30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                  40, 41, 42, 43, 44, 45])
death = np.array([431, 409, 429, 422, 530, 505, 459, 499, 526, 563,
                  587, 595, 647, 669, 746, 760, 778, 828, 846, 836,
                  916, 956, 1014, 1076, 1134, 1024])
_, ax = plt.subplots()
ax = plot_least_squares(years, death, ax)
ax.set_xlabel('Year')
ax.set_ylabel('Deaths')
plt.show()

years_20_28 = years[0:9]
years_28_39 = years[8:20]
years_39_45 = years[19:]

death_20_28 = death[0:9]
death_28_39 = death[8:20]
death_39_45 = death[19:]

_, ax = plt.subplots()
ax.set_xlabel('Year')
ax.set_ylabel('Deaths')
ax = plot_least_squares(years_20_28, death_20_28, ax)
ax = plot_least_squares(years_28_39, death_28_39, ax)
ax = plot_least_squares(years_39_45, death_39_45, ax)
plt.show()
