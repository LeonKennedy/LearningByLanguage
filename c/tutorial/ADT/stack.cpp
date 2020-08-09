#include <iostream>
#include "stack.hpp"

namespace STACK {
template <typename T>
Stack<T>::Stack(): size(10), top(0)
{
    items = new T[size];
}

template <typename T>
Stack<T>::Stack(const int s): size(s), top(0)
{
    items = new T[size];
}

template <typename T>
Stack<T>::Stack(const Stack<T> & s)
{
    size = s.size;
    items = new T[size];
    top = s.top;
    for (int i=0; i< top; i++) {
        items[i] = s.items[i];
    }
}

template <typename T>
Stack<T>::~Stack()
{
    delete [] items;
}

template <typename T>
bool Stack<T>::isempty() const
{
    return top == 0;
}

template <typename T>
bool Stack<T>::isfull() const
{
    return top == size;
}

template <typename T>        
bool Stack<T>::push(const T & item)
{
    if (top < size) {
        items[top++] = item;
        return true;
    }else
        return false;
}

template <typename T>
T & Stack<T>::pop()
{
    if (top > 0) {
        T item = items[--top];
        return item;
    }else
        return *(T*)nullptr;
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
Stack<T> & Stack<T>::operator=(const Stack<T> & s)
{
    if (this==&s)
        return *this;
    delete [] items;
    size = s.size;
    items = new T[size];
    top = s.top;
    for (int i=0; i< top; i++) 
        items[i] = s.items[i];
    return *this;
}

// template <typename T>
// void Stack<T>::operator+ (T & item)
// {
//     this->push(item);
// }

// template <typename T>
// void operator + (T & m, Stack<T> & s)
// {
//     s.push(m);
// }

// template <typename T>
// std::ostream & operator << (std::ostream & os, const Stack<T> & s)
// {
//     for (int i = 0; i < s.top; i++) 
//         os << s.items[i] << '\t';
//     return os;
// }

void play()
{
    Stack<double> std;
    Stack<char *> stk(6);
    char c1[] = "feji";
    char c2[] = "ifbnd";
    char c3[] = "erkl";
    // char *c[] = {"dfeic", "acd", "efdw"};
    stk.push(c1);
    stk.push(c2);
    stk.push(c3);
    Stack<char *> stk1(5);
    stk1 = stk;
    stk1.show();
    char * p = stk.pop();
    stk.show();
    // stk.push(2.0);
    // stk.push(3.0);
    // double i1 = 4;
    // stk + i1;
    // double i2 = 52342;
    // i2 + stk;
    // std::cout << stk << std::endl;
    // double item;
    // stk.pop(item);
    // std::cout << item << std::endl;
    // stk.show();
}
}