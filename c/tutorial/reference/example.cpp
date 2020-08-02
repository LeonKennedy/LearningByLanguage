#include <iostream>
#include "example.hpp"

extern double belm;
void ref12132()
{
    int first = 1;
    int * pf = &first;
    int & rf = first;
    std::cout<< rf << "\t" << *pf << std::endl;
    int buindes = 50;
    std::cout << buindes << std::endl;
    pf = &buindes;
    std::cout << *pf << "\t" << first << std::endl;
}

void local()
{
    int warming;
    warming = 313;
    std::cout << "local warming: " << warming << " ::warming: " << ::warming << std::endl;
}

void update(int a)
{
    extern int warming;
    warming += a;
    std::cout << "after update warming: " << warming <<  std::endl;
}

void exp1212()
{
    std::cout << "ertern belm  is " << belm << std::endl;
    local();
    update(1);
    std::cout <<  "warming: " << warming << std::endl;
}

void static_plus(int x)
{
    static int total = 0;
    total += x;
    std::cout << "total: " << total << " by plus " << x << std::endl;
}
void exp_static()
{
    static_plus(1);
    static_plus(2);
    static_plus(3);

}
