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

void Stack::operator+ (Item & item)
{
    this->push(item);
}

void operator + (Item & m, Stack & s)
{
    s.push(m);
}

std::ostream & operator << (std::ostream & os, const Stack & s)
{
    for (int i = 0; i < s.top; i++) 
        os << s.items[i] << '\t';
    return os;
}

void play()
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
}