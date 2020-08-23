#include "smart_ptr.hpp"
#include <iostream>


template <typename T>
template <typename U>
SmartPtr<T>::SmartPtr(SmartPtr<U>& other)
{
    ptr_ = other.ptr_;
    if (ptr_) {
        other.shared_cout_->add();
        shared_cout_ = other.shared_cout_;
    }
}

template <typename T>
SmartPtr<T>::SmartPtr(SmartPtr&& other)
{
    ptr_ = other.ptr_;
    if (ptr_) {
        shared_cout_ = other.shared_cout_;
        other.ptr_ = nullptr;
    }
}

template <typename T>
template <typename U>
SmartPtr<T>::SmartPtr(const SmartPtr<U>& other, T* p)
{
    ptr_ = p;
    if (ptr_) {
        other.shared_cout_->add();
        shared_cout_ = other.shared_cout_;
    }
}

template <typename T>
SmartPtr<T>& SmartPtr<T>::operator=(SmartPtr other)
{
    other.swap(*this);
    return *this;
}

template <typename T>
SmartPtr<T>::~SmartPtr()
{
    if (ptr_ && !shared_cout_->sub()) {
        delete ptr_;
        delete shared_cout_;
    }
}

template <typename T>
long SmartPtr<T>::use_count() const
{
    if (ptr_) 
        return shared_cout_->count();
    else
        return 0;
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
    std::swap(shared_cout_, s.shared_cout_);
}

// template <typename T>
// std::ostream & operator<< (std::ostream & os, SmartPtr<T> & p)
// {
//     os << p.ptr_->count() << "\tshard_count:" << p.shared_cout_->count() << std::endl; 
// }

template <typename T, typename U>
SmartPtr<T> dynamic_pointer_cast(const SmartPtr<U>& other)
{
    T * ptr = dynamic_cast<T*>(other.get());
    return SmartPtr<T>(other, ptr);
}

int main(int argc, char const *argv[])
{
    Box * b = new Box(5);
    SmartPtr<Box> p(b);
    printf("use cout of ptr1 is %ld\n", p.use_count());
    SmartPtr<shape> p2(p);
    printf("use cout of ptr2 is %ld\n", p2.use_count());
    SmartPtr<Box> p3 {std::move(p)};
    printf("use cout of ptr3 is %ld\n", p3.use_count());
    SmartPtr<Box> p4 = dynamic_pointer_cast<Box>(p3);
    printf("use cout of ptr3 is %ld\n", p4.use_count());
    // p2 = std::move(p);
    std::cout << p2.get() << std::endl;
    return 0;
}
