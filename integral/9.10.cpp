#include <iostream>
#include <vector>

std::vector<double> function(const std::vector<double>& x)
{
    const size_t nodes = std::size(x);
    std::vector<double> result(nodes);
    for (size_t i = 0; i < nodes; ++i) {
        const double xi = x[i];
        result[i] = 2 / (1 + std::pow(xi, 2));
    }
    return result;
}

double trapez(const std::vector<double>& x, const std::vector<double>& f)
{
    double sum = 0;
    const size_t nodes = std::size(x);
    const size_t intervals = nodes - 1;
    for (size_t i = 0; i < intervals; ++i) {
        const double h = x[i + 1] - x[i];
        sum += h * (f[i] + f[i + 1]) / 2;
    }
    return sum;
}

int main()
{
    const double h = 0.007;

    std::vector<double> x;

    for (double xi = 0; xi <= 1; xi += h) {
        x.push_back(xi);
    }

    std::vector<double> f = function(x);
    const double integr = trapez(x, f);
    std::cout << integr << '\n';

    return 0;
}
