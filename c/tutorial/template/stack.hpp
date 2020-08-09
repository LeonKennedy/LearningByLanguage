#ifndef STACKTP_H_
#define STACKTP_H_

    template <typename T>
    class Stack
    {
        private:
            const static int size = 10;
            T items[size];
            int top;
        public:
            Stack();
            ~Stack();
            // Stack(const Stack &);
            bool isempty() const;
            bool isfull() const;
            bool push(const T & item);
            bool pop(T & item);
            // void show() const;
            // Stack & operator=(const Stack &);
            // void operator + (T & item);
            // friend void operator + (T & item, Stack<T> & s);
            // friend std::ostream & operator << (std::ostream & os, const Stack<T> & s);
            
    };
    void play();

#endif