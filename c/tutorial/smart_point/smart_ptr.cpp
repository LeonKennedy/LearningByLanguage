#include "smart_ptr.hpp"
#include <iostream>

template <typename T>
SmartPtr<T>::SmartPtr(SmartPtr&& other)
{
    ptr_ = other.release();
}

template <typename T>
SmartPtr<T>& SmartPtr<T>::operator=(SmartPtr<T> other)
{
    other.swap(*this);
    return *this;
}


template <typename T>
T * SmartPtr<T>::release()
{
    T * t = ptr_;
    ptr_ = nullptr;
    return t;
}

template <typename T>
void SmartPtr<T>::swap(SmartPtr & s)
{
    std::swap(ptr_, s.ptr_);
}

int main(int argc, char const *argv[])
{
    Box * b = new Box(5);
    SmartPtr<Box> p(b);
    SmartPtr<Box> p2 {std::move(p)};
    // p2 = std::move(p);
    std::cout << p2.get()->count() << std::endl;
    return 0;
}
