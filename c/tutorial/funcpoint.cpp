#include <iostream>

int JustSum(int x)
{
    std::cout << x * 2 << std::endl;
    return x * 2;
}

int JustPlus(int x)
{
    return x++;
}

void show_function_point()
{
    int x = 3;
    int (*pfunc)(int) = JustSum;
    int y = pfunc(x);
    std::cout << y << std::endl;
}