
template <typename T>
class SmartPtr
{
    private:
        T * ptr_;
    public:
        explicit SmartPtr(T * p=nullptr)
            : ptr_(p) {}
        SmartPtr(SmartPtr&&);
        ~SmartPtr() { delete ptr_; };

        SmartPtr& operator=(SmartPtr);
        T& operator*() const { return *ptr_;}
        T* operator->() const { return ptr_;}
        operator bool() const { return ptr_;}
        T * get() const { return ptr_; };
        T * release();
        void swap(SmartPtr&);
};

class Box
{
    private:
        int size_;
    public:
        Box(int size = 0): size_(size) {};
        int& count() {return size_;}
};
