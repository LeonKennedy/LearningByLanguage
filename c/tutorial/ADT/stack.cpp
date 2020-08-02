#include <iostream>
#include "stack.hpp"

Stack::Stack()
{
    top = 0;
}

bool Stack::isempty() const
{
    return top == 0;
}


bool Stack::isfull() const
{
    return top == MAX;
}
        
bool Stack::push(const Item & item)
{
    if (top < MAX) {
        items[top++] = item;
        return true;
    }else
        return false;
}
        
bool Stack::pop(Item & item)
{
    if (top > 0) {
        item = items[--top];
        return true;
    }else
        return false;
}

void Stack::show() const
{
    for (int i = 0; i < top; i++) {
        std::cout << items[i] << '\t';
    }
    std::cout << std::endl;
}