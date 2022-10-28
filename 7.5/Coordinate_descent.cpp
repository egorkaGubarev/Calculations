#include <array>
#include <iostream>

double f(const double x, const double y)
{
    const double result = std::pow(std::pow(x, 2) + std::pow(y, 2) - 1, 2) + std::pow(y - x * std::sin(x), 2);
    return result;
}

double minimum_splitting_x(double (*f_ptr)(const double, const double), const double y, const double left, const double right, const double epsilon)
{
    const double center = (left + right) / 2;
    double x_min = center;
    const double epsilon_curr = (right - left) / 2;

    if (epsilon < epsilon_curr) {
        const double u1 = center - epsilon / 2;
        const double u2 = center + epsilon / 2;

        const double f1 = (*f_ptr)(u1, y);
        const double f2 = (*f_ptr)(u2, y);

        if (f1 > f2) {
            x_min = minimum_splitting_x(f_ptr, y, u1, right, epsilon);
        }
        else {
            x_min = minimum_splitting_x(f_ptr, y, left, u2, epsilon);
        }
    }

    return x_min;
}

double minimum_splitting_y(double (*f_ptr)(const double, const double), const double x, const double left, const double right, const double epsilon)
{
    const double center = (left + right) / 2;
    double x_min = center;
    const double epsilon_curr = (right - left) / 2;

    if (epsilon < epsilon_curr) {
        const double u1 = center - epsilon / 2;
        const double u2 = center + epsilon / 2;

        const double f1 = (*f_ptr)(x, u1);
        const double f2 = (*f_ptr)(x, u2);

        if (f1 > f2) {
            x_min = minimum_splitting_y(f_ptr, x, u1, right, epsilon);
        }
        else {
            x_min = minimum_splitting_y(f_ptr, x, left, u2, epsilon);
        }
    }

    return x_min;
}

std::array<double, 2> make_coord_descent(double (*f_ptr)(const double, const double),
    const double x_min, const double x_max, const double y_min, const double y_max, const double epsilon)
{
    double current_epsilon = 1;

    double x_prev = (x_max + x_min) / 2;
    double y_prev = (y_max + y_min) / 2;

    while (current_epsilon > epsilon) {
        const double x = minimum_splitting_x(f_ptr, y_prev, x_min, x_max, epsilon);
        const double y = minimum_splitting_y(f_ptr, x, y_min, y_max, epsilon);

        const double new_value = f(x, y);
        current_epsilon = std::abs((new_value - f(x_prev, y_prev)) / new_value);

        x_prev = x;
        y_prev = y;
    }

    const std::array<double, 2> result{ x_prev, y_prev };
    return result;
}

int main()
{
    double (*f_ptr)(const double, const double) = nullptr;
    f_ptr = &f;
    const std::array<double, 2> result = make_coord_descent(f_ptr, -1, 1, -1, 1, 0.01);

    const double x = result[0];
    const double y = result[1];

    std::cout << "x: " << x << '\n';
    std::cout << "y: " << y << '\n';
}
