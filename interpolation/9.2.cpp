#include <iostream>
#include <vector>

float interpolate_derivative(const size_t amount, std::vector<float> x, std::vector<float> f, const float x_star)
{
    float result = 0;

    for (size_t m = 0; m < amount; ++ m) {
        float numerator = 0;
        float denominator = 1;

        for (size_t k = 0; k < amount - 1; ++k) {
            float product = 1;
            size_t lost_index = 0;
            
            if (k >= m) {
                lost_index = k + 1;
            }
            else {
                lost_index = k;
            }

            for (size_t l = 0; l < amount; ++l) {
                if ((l != lost_index) && (l != m)) {
                    const float x_l = x[l];
                    product *= (x_star - x_l);
                }
            }
            numerator += product;
        }

        const float x_m = x[m];

        for (size_t k = 0; k < amount; ++k) {
            if (k != m) {
                const float x_k = x[k];
                denominator *= (x_m - x_k);
            }
        }

        const float aux = numerator / denominator;
        const float f_m = f[m];
        const float term = aux * f_m;
        result += term;
    }
    return result;
}

int main()
{
    const size_t amount = 5;
    const float answer = -0.085f;
    const float x_star = 5.0f;

    std::vector<float> x{ 0.0f, 1.0f, 3.0f, 4.0f, 5.0f};
    std::vector<float> f{ 0.5f, 0.3f, 0.3f, 0.2f, 0.1f};

    const float zero = interpolate_derivative(amount, x, f, x_star);
    const float error = std::abs(answer - zero);

    std::cout << "Derivative by interpolation: " << zero << '\n';
    std::cout << "Real derivative: " << answer << '\n';
    std::cout << "Error: " << error << '\n';
    return 0;
}