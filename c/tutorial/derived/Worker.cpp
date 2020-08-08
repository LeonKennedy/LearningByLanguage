#include <iostream>
#include "Worker.hpp"

namespace WORKER
{
    Worker::~Worker() {}
    void Worker::show() const
    {
        std::cout << name << "(" << id <<") ";
    }

    void Singer::show() const
    {
        Worker::show();
        std::cout << "voice: " << voice << std::endl;
    }

    void Waiter::show() const
    {
        Worker::show();
        std::cout << "panache: " << panache << std::endl;
    }

    void SingeWaiter::show() const
    {
        Worker::show();
        // std::cout << "panache: " << panache << " voice: " << voice << std::endl;
    }

    void play()
    {
        Waiter waiter("a", 2, 3);
        Singer singer("b", 3 , 7);
        Waiter w_tmp;
        Singer s_tmp;
        Worker * pw[4] = {&waiter, &singer, &w_tmp, &s_tmp};
        for (int i=0; i< 4;i++) {
            pw[i]->show();
        }

        SingeWaiter sw;
        Worker * p = &sw;
    }
} // namespace WORKER