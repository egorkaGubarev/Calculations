#include <iostream>

double f(const double t)
{
    const double result = 3 * std::pow(t, 4) - 8 * std::pow(t, 3) + 6 * std::pow(t, 2);
    return result;
}

double f_deriv(const double t)
{
    const double result = 12 * t * std::pow(t - 1, 2);
    return result;
}

double make_iter(const double t)
{
    const double result = std::log(std::exp(t) - 6 * t * std::pow(t - 1, 2) / 7);
    return result;
}

double minimum_splitting(double (*f_ptr)(const double), const double left, const double right, const double epsilon)
{
    const double center = (left + right) / 2;
    double x_min = center;
    const double epsilon_curr = (right - left) / 2;

    if (epsilon < epsilon_curr) {
        const double u1 = center - epsilon / 2;
        const double u2 = center + epsilon / 2;

        const double f1 = (*f_ptr)(u1);
        const double f2 = (*f_ptr)(u2);

        if (f1 > f2) {
            x_min = minimum_splitting(f_ptr, u1, right, epsilon);
        }
        else {
            x_min = minimum_splitting(f_ptr, left, u2, epsilon);
        }
    }
    
    return x_min;
}

double solve(double (*make_iter_ptr)(const double), double (*equiat_ptr)(const double), const double left, const double right, const double epsilon)
{
    double x_prev = (left + right) / 2;
    double epsilon_curr = 1;
    int iter = 0;

    // Iterations
    while (epsilon_curr > epsilon) {
        const double x = (*make_iter_ptr)(x_prev);
        const double delta = std::abs(x - x_prev);
        epsilon_curr = delta / x;
        x_prev = x;
        ++iter;
    }

    const double descrepancy = (*equiat_ptr)(x_prev);
    std::cout << "Descrepancy in solving derivation: " << descrepancy << '\n';
    std::cout << "Iterations in solving derivation: " << iter << '\n';

    return x_prev;
}

int main()
{
    double (*f_ptr)(const double) = nullptr;
    double (*f_deriv_ptr)(const double) = nullptr;
    double (*make_iter_ptr)(const double) = nullptr;

    f_ptr = &f;
    f_deriv_ptr = &f_deriv;
    make_iter_ptr = &make_iter;

    const double x_min_split = minimum_splitting(f_ptr, -1, 1, 0.01);
    const double x_min_deriv = solve(make_iter_ptr, f_deriv_ptr, -0.13, 0.25, 0.01);

    std::cout << "x min by splitting: " << x_min_split << '\n';
    std::cout << "X min by solving derevation: " << x_min_deriv << '\n';
}
