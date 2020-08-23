/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-08-22 14:43:48 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-22 15:24:31
 */
#include "func.hpp"
#include <iostream>
#include <functional>
double dub(double & a) { return 2.0 * a;}
double sqr(double & b) { return b * b;}
auto lamdub = [](double & x) { return 2.0 * x;};

int main(int argc, char const *argv[])
{
    const double y = 0.25;
    std::cout << use_f(y, dub) << std::endl;
    std::cout << use_f(y, sqr) << std::endl;
    std::cout << use_f(y, [](double & x){ return x*x;}) << std::endl;
    std::cout << use_f(y, lamdub) << std::endl;


    std::cout << " ====  use wrapper for all ====" << std::endl;
    std::cout << "只初始化一次" << std::endl;
    typedef std::function<double(double &) > eff;
    std::cout << use_f(y, eff(dub)) << std::endl;
    std::cout << use_f(y, eff(sqr)) << std::endl;
    std::cout << use_f(y, eff([](double & x){ return x*x;})) << std::endl;
    std::cout << use_f(y, eff(lamdub)) << std::endl;
    return 0;
}
