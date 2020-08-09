#include <iostream>
#include "stack.hpp"
#include "friend1.cpp"


template <typename T>
class Beta
{
    private:
        template <typename V>
        class hold
        {
            private:
                V val;
            public:
                hold(V v=0): val(v) {}
                void show() const { std::cout << val << std::endl;}
                V Value() const {return val;}
        
        };
        hold<T> q;
        hold<int> n;
    public:
        Beta(T t, int i): q(t), n(i) {}
        template<typename U>
        U blab(U u, T t) { return (n.Value() + q.Value()) * u / t;}
        void show() const { q.show(); n.show();}
};

void play_beta()
{
    Beta<double> guy(3.5, 3);
    std::cout << "T was set to double \n";
    guy.show();
    std::cout << "V was set to T, which is double, then V was set to int\n";
    std::cout << guy.blab(10, 2.3) << std::endl;
    std::cout << "U was set to int\n";
    std::cout << guy.blab(10.0, 2.3) << std::endl;
    std::cout << "U was set to double\n";
}

int main()
{
    // play_beta();
    play1();
}