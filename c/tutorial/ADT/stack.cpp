#include <iostream>
#include "stack.hpp"

namespace STACK {
template <typename T>
Stack<T>::Stack()
{
    top = 0;
}

template <typename T>
bool Stack<T>::isempty() const
{
    return top == 0;
}

template <typename T>
bool Stack<T>::isfull() const
{
    return top == MAX;
}

template <typename T>        
bool Stack<T>::push(const T & item)
{
    if (top < MAX) {
        items[top++] = item;
        return true;
    }else
        return false;
}

template <typename T>
bool Stack<T>::pop(T & item)
{
    if (top > 0) {
        item = items[--top];
        return true;
    }else
        return false;
}

template <typename T>
void Stack<T>::show() const
{
    for (int i = 0; i < top; i++) {
        std::cout << items[i] << '\t';
    }
    std::cout << std::endl;
}

template <typename T>
void Stack<T>::operator+ (T & item)
{
    this->push(item);
}

template <typename T>
void operator + (T & m, Stack<T> & s)
{
    s.push(m);
}

template <typename T>
std::ostream & operator << (std::ostream & os, const Stack<T> & s)
{
    for (int i = 0; i < s.top; i++) 
        os << s.items[i] << '\t';
    return os;
}

void play()
{
    Stack<double> stk;
    stk.push(2.0);
    stk.push(3.0);
    double i1 = 4;
    stk + i1;
    double i2 = 52342;
    i2 + stk;
    std::cout << stk << std::endl;
    double item;
    stk.pop(item);
    std::cout << item << std::endl;
    stk.show();
}
}