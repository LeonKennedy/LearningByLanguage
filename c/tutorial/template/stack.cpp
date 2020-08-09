#include <iostream>
#include "stack.hpp"

template <typename T>
Stack<T>::Stack()
{
    top = 0;
}

// template <typename T>
// Stack<T>::Stack(const Stack<T> & s)
// {
//     top = s.top;
//     for (int i=0; i< top; i++) {
//         items[i] = s.items[i];
//     }
// }

template <typename T>
Stack<T>::~Stack()
{
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
bool Stack<T>::pop(T & item)
{
    if (top > 0) {
        item = items[--top];
        return item;
    }else
        return false;
}

// template <typename T>
// void Stack<T>::show() const
// {
//     for (int i = 0; i < top; i++) {
//         std::cout << items[i] << '\t';
//     }
//     std::cout << std::endl;
// }

// template <typename T>
// Stack<T> & Stack<T>::operator=(const Stack<T> & s)
// {
//     if (this==&s)
//         return *this;
//     delete [] items;
//     size = s.size;
//     items = new T[size];
//     top = s.top;
//     for (int i=0; i< top; i++) 
//         items[i] = s.items[i];
//     return *this;
// }

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
    Stack<double> st1;
}