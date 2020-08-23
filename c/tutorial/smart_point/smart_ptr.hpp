#include <iostream>

class UseCount
{
    private:
        long cnt_;
    public:
        UseCount(long c=1): cnt_(c) {}
        void add() { cnt_++; }
        long sub() { return --cnt_ ;}
        long count() const { return cnt_;}
};

template <typename T>
class SmartPtr
{
    private:
        T * ptr_;
        UseCount * shared_cout_;
    public:
        template <typename U>
        friend class SmartPtr;
        explicit SmartPtr(T * p=nullptr)
            : ptr_(p) 
        {
            if (p) {
                shared_cout_ = new UseCount;
            }
        }
        template <typename U>
        SmartPtr(SmartPtr<U>&);
        SmartPtr(SmartPtr&&);
        template <typename U>
        SmartPtr(const SmartPtr<U>&, T*);
        ~SmartPtr();

        SmartPtr& operator=(SmartPtr);
        T& operator*() const { return *ptr_;}
        T* operator->() const { return ptr_;}
        operator bool() const { return ptr_;}
        T * get() const { return ptr_; };
        long use_count() const;
        T * release();
        void swap(SmartPtr&);

        // friend std::ostream & operator<< (std::ostream &, SmartPtr<T> &);
};

class shape
{
    public:
        virtual ~shape() {}
};

class Box: public shape
{
    private:
        int size_;
    public:
        Box(int size = 0): size_(size) {};
        int& count() {return size_;}
        ~Box() { puts("~Box()");}
};


