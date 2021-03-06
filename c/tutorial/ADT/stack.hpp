#ifndef STACK_H_
#define STACK_H_

namespace STACK
{
    template <typename T>
    class Stack
    {
        private:
            int size;
            T * items;
            int top;
        public:
            Stack();
            Stack(const int s);
            ~Stack();
            Stack(const Stack &);
            bool isempty() const;
            bool isfull() const;
            bool push(const T & item);
            T & pop();
            void show() const;
            Stack & operator=(const Stack &);
            // void operator + (T & item);
            // friend void operator + (T & item, Stack<T> & s);
            // friend std::ostream & operator << (std::ostream & os, const Stack<T> & s);
    };

    void play();
}

#endif