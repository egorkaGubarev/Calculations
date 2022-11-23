#include <iostream>
#include <vector>

std::vector<float> function(const std::vector<float>& x)
{
    const size_t nodes = std::size(x);
    std::vector<float> result(nodes);
    for (size_t i = 0; i < nodes; ++i) {
        const float xi = x[i];
        result[i] = (float) (std::tan(xi) * std::sqrt(1 - std::pow(xi, 2)));
    }
    return result;
}

float trapez(const std::vector<float>& x, const std::vector<float>& f)
{
    float sum = 0;
    const size_t nodes = std::size(x);
    const size_t intervals = nodes - 1;
    for (size_t i = 0; i < intervals; ++i) {
        const float h = x[i + 1] - x[i];
        sum += h * (f[i] + f[i + 1]) / 2;
    }
    return sum;
}

float richard(const float integr_good, const float integr_bad, const float p)
{
    const float extrap = (float) ((std::pow(2, p) * integr_good - integr_bad) / (std::pow(2, p) - 1));
    return extrap;
}

float simpson(const std::vector<float>& x, const std::vector<float>& f, const float h)
{
    const size_t nodes = std::size(x);
    float integr = 0;

    for (size_t i = 0; i < nodes / 2; ++i) {
        integr += h * (f[2 * i] + 4 * f[2 * i + 1] + f[2 * i + 2]) / 3;
    }

    return integr;
}

int main()
{
    const float h = 0.125;

    std::vector<float> x{ 0.0f, 0.125f, 0.25f, 0.375f, 0.5f, 0.625f, 0.75f, 0.875f, 1.0f };
    std::vector<float> x2{ 0.0f, 0.25f, 0.5f, 0.75f, 1.0f };

    std::vector<float> f{ 0.0f, 0.12467f, 0.247234f, 0.364902f, 0.473112f, 0.563209f, 0.616193f, 0.579699f, 0.0f };
    std::vector<float> f2 = function(x2);

    const float integr_trapez = trapez(x, f);
    const float trapez_2 = trapez(x2, f2);

    const float extrap = richard(integr_trapez, trapez_2, 2);
    const float simpson_integr = simpson(x, f, h);

    std::cout << "Trapezoid: " << integr_trapez << '\n';
    std::cout << "Trapezoid 2: " << trapez_2 << '\n';
    std::cout << "Extrapolation: " << extrap << '\n';
    std::cout << "Simpson: " << simpson_integr << '\n';

    return 0;
}
