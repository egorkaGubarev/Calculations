#include <iostream>
#include <cmath>

float solve(const float epsilon)
{
    const float left = (float) (1 * 0.1);
    const float right = 1;

    float x_prev = (left + right) / 2;
    float epsilon_curr = 1;
    int iter = 0;

    // Iterations
    while (epsilon_curr > epsilon) {
        const float x = 1 / std::sqrt(1 + x_prev);
        const float delta = std::abs(x - x_prev);
        epsilon_curr = delta / x;
        x_prev = x;
        ++ iter;
    }

    const float descrepancy = std::sqrt(1 + x_prev) - 1 / x_prev;
    std::cout << "Descrepancy: " << descrepancy << '\n';
    std::cout << "Iterations: " << iter << '\n';

    return x_prev;
}

int main()
{
    const float epsilon = (float) 1.e-7;
    const float x = solve(epsilon);
    std::cout << "Solution: " << x << '\n';
}
