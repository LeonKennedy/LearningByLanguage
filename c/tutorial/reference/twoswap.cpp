/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-26 14:58:35 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-27 17:26:48
 * @Function: explicit specialization & explicit instantiaion
 */

#include <iostream>
#include "twoswap.hpp"

void show_2fds(job &j)
{
    std::cout << j.name << ": $" << j.salary << " on floor " << j.floor << std::endl;
}

void TwoSwapExp()
{
    using namespace std;
    cout.precision(2);
    cout.setf(ios::fixed, ios::floatfield);
    int i =10, j =20;
    cout << "i, j " << i << ", " << j << endl;
    Swap(i, j);  //implicit instantiation
    cout << "After swap : i, j " << i << ", " << j << endl;

    job sue = {"Susan Yaffee", 32423.2, 8};
    job sideny = {"Sideny Taffer", 42423.68, 3};
    show_2fds(sue);
    show_2fds(sideny);
    Swap(sue, sideny);
    std::cout << "After job swapping:" << endl;
    show_2fds(sue);
    show_2fds(sideny);
}

template <typename T>
void Swap(T &a, T &b)  // general version
{
    T t = a;
    a = b;
    b = t;
}

template <> void Swap<job>(job &j1, job &j2) 
{
    double t1 = j1.salary;
    j1.salary = j2.salary;
    j2.salary = t1;

    int t2 = j1.floor;
    j1.floor = j2.floor;
    j2.floor = t2;
}