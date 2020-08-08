#ifndef STACK_H_
#define STACK_H_

namespace STACK
{
    template <typename T>
    class Stack
    {
        private:
            enum {MAX=10};
            T items[MAX];
            int top;
        public:
            Stack();
            bool isempty() const;
            bool isfull() const;
            bool push(const Item & item);
            bool pop(Item & item);
            void show() const;
            void operator + (Item & item);
            friend void operator + (Item & item, Stack & s);
            friend std::ostream & operator << (std::ostream & os, const Stack & s);

    };

    void play();
}

#endif