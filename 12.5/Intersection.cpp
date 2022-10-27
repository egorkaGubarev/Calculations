#include <iostream>
#include <cmath>

float solve(const float epsilon)
{
    const float left = (float)(1 * 0.1);
    const float right = 1;

    float x_prev = (left + right) / 2;
    float epsilon_curr = 1;
    int iter = 0;

    // Iterations
    while (epsilon_curr > epsilon) {
        const float x = (float) (0.5 - std::cos(std::cos(x_prev) + 2));
        const float delta = std::abs(x - x_prev);
        epsilon_curr = delta / x;
        x_prev = x;
        ++iter;
    }

    const float descrepancy = (float) (std::cos(std::cos(x_prev) + 2) + x_prev - 0.5);
    std::cout << "Iterations: " << iter << '\n';

    return x_prev;
}

int main()
{
    const float epsilon = (float)1.e-3;

    const float y = solve(epsilon);
    const float x = std::cos(y) + 3;

    const float descrepancy_1 = (float)(std::cos(x - 1) + y - 0.5);
    const float descrepancy_2 = (float)(x - std::cos(y) - 3);

    std::cout << "Solution (x; y): " << '(' << x << "; " << y << ')' << '\n';
    std::cout << "Descrepancy (x; y): " << '(' << descrepancy_1 << "; " << descrepancy_2 << ')' << '\n';
}