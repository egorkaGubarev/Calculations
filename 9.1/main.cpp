#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

typedef float type;

type count_exp(type x)
{
    type sum = 1;
    type term = 1;
    int i = 1;
    while (sum + term != sum){
        term = term * x / (float)i;
        sum = sum + term;
        ++ i;
    }
    return sum;
}

type count_better_exp(type x)
{
    if (x >= 0){
        const type exp = count_exp(x);
        return exp;
    }else{
        const type pos_x = -x;
        const type pos_exp = count_exp(pos_x);
        const type exp = 1 / pos_exp;
        return exp;
    }
}

int main() {
    const int precision = 7;
    std::vector<type> args = {1, 5, 10, 15, 20, 25, -1, -5, -10, -15, -20, -25};
    for (type arg: args){
        const type sum = count_exp(arg);
        const type exp = std::exp(arg);
        const type better_exp = count_better_exp(arg);
        std::cout << std::setprecision(precision) << "x: " << arg << "; sum: " << sum << "; exp: " << exp
                    <<"; better exp: " << better_exp << '\n';
    }
    return 0;
}
