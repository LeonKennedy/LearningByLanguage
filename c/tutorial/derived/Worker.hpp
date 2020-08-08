#ifndef WORKER_H_
#define WORKER_H_
#include <string>
namespace WORKER
{
    using namespace std;
    class Worker
    {
        private:
            string name;
            int id;
        public:
            Worker() : name("nobody"), id(0L) {}
            Worker(const string & s, long i = 0L) : name(s) , id(i) {}
            virtual ~Worker() = 0;
            virtual void show() const;
    };

    class Singer: virtual public Worker 
    {
        protected:
            enum {other, alto, contralto, soprano, bass, baritone, tenor};
            enum {Vtypes = 7};
        private:
            static char *pv[Vtypes];
            int voice;

        public:
            Singer(): Worker(), voice(other) {}
            Singer(const string & s, long n=0L, int v = other) : Worker(s, n), voice(v) {}
            Singer(const Worker & w, int v = other): Worker(w), voice(v) {}
            void show() const;


    };

    class Waiter: virtual public Worker 
    {
        private:
            int panache;
        public:
            Waiter(): Worker(), panache(0) {}
            Waiter(const string & s, long n=0L, int v = 0) : Worker(s, n), panache(v) {}
            Waiter(const Worker & w, int v = 0): Worker(w), panache(v) {}
            void show() const;
    };

    class SingeWaiter: public Waiter, public Singer
    {
        public:
            SingeWaiter(): Waiter(), Singer() {}
            void show() const;
    };

    void play();
} // end namespace

#endif