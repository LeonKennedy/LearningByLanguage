#include <iostream>
#include "stack.hpp"

template <template <typename T> class Thing>
class Crab
{
    private:
        Thing<int> s1;
        Thing<double> s2;
    public:
        Crab() {};
        bool push(int a, double x) { return s1.push(a) && s2.push(x);}
        void pop() { std::cout << s1.pop() << '\t' << s2.pop() << std::endl;}
};

int main()
{
    Stack<double> std;
    Crab<Stack> nebula;
    // int ni = 5;
    // double nb = 2.3;
    // nebula.push(ni, nb);
    // nebula.pop();
    return 0;
}

