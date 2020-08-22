#include <stdio.h>
#include <iostream>

template <typename T, typename F>
double use_f(T t, F f)
{
    const static int count= 0;
    std::cout << "count=\t" << count << "\t" << &count << std::endl;
    return f(t);
}

