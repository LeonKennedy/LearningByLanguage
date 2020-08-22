/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-08-22 14:43:48 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-22 14:57:31
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
    std::function<double(double &) > ef1 = dub;
    std::function<double(double &) > ef2 = sqr;
    std::function<double(double &) > ef3 = [](double & x){ return x*x;};
    std::function<double(double &) > ef4 = lamdub;

    std::cout << use_f(y, ef1) << std::endl;
    std::cout << use_f(y, ef2) << std::endl;
    std::cout << use_f(y, ef3) << std::endl;
    std::cout << use_f(y, ef4) << std::endl;
    return 0;
}
