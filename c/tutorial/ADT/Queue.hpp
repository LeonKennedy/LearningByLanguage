/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-08-05 16:50:16 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-05 19:41:07
 */
#include <iostream>
#include <string>

namespace QUEUE {

class Customer
{
    private:
        long arrive;
        int processtime;
    public:
        Customer () { arrive = processtime = 0;}
        void set(long when);
        long when() const { return arrive;}
        int ptime() const { return processtime;}
        friend std::ostream & operator << (std::ostream &, const Customer &);
};

typedef Customer Item;

class Queue
{
    private:
        class Node
        {
            public:
                Item item;
                Node * p_next;
                Node(const Item & i) : item(i), p_next(0) {}
        };
        Node * front;
        Node * rear;
        int items;
        const int qsize;
    public:
        Queue(int qs = 10);
        ~Queue();
        bool is_empty() const;
        bool is_full() const;
        int length() const {return items;};
        bool append(const Item &);
        bool leftpop(Item &item);
        void show() const;
};

void customer_montecario();
}