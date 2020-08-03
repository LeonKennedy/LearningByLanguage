#include <iostream>
#include "stack.hpp"


int main()
{
    Stack stk;
    stk.push(2.0);
    stk.push(3.0);
    Item i1 = 4;
    stk + i1;
    Item i2 = 52342;
    i2 + stk;
    std::cout << stk << std::endl;
    Item item;
    stk.pop(item);
    std::cout << item << std::endl;
    stk.show();
    return 0;
}