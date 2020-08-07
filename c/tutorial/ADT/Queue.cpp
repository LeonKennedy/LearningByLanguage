#include "Queue.hpp"
#include <iostream>
namespace QUEUE{

void Customer::set(long when)
{
    processtime = std::rand() % 3 + 1;
    arrive = when;
}

std::ostream & operator << (std::ostream & os,const Customer & c)
{
    os << "(arrive: " << c.arrive << " process time: ";
    os << c.processtime << ")";
    return os;
}

Queue::Queue(int qs): qsize(qs) , items(0)
{
    front = nullptr;
    rear = nullptr;
}

Queue::~Queue()
{
    Node * p;
    while (front != nullptr) {
        p = front;
        front = front->p_next;
        delete p;
    }
}

bool Queue::is_empty() const
{
    return (items == 0);
}

bool Queue::is_full() const
{
    return (items == qsize);
}

bool Queue::append(const Item & item)
{
    if (is_full())
        return false;
    Node * add = new Node;
    add->item = item;
    add->p_next = nullptr;
    items++;
    if (front == nullptr)
        front = add;
    else {
        rear->p_next = add;
    }
    rear = add;
    return true;
}

bool Queue::leftpop(Item & item)
{
    if (is_empty())
        return false;
    item = front->item;
    Node * p = front;
    front = front->p_next;
    delete p;
    items--;
    if (items == 0)
        rear = nullptr;
    return true;
}

void Queue::show() const
{
    Node * p = front;
    while (p != nullptr) {
        std::cout << p->item << '|';
        p = p->p_next;
    }
    std::cout << std::endl;
}

bool is_coming_new_customer(double x)
{
    return (std::rand() * x) / RAND_MAX < 15;
}

void customer_montecario()
{
    using namespace std;
    srand(time(0));
    cout << "Case Study: Bank of Heather Automatic Teller\n";
    Queue line(20);
    int hours = 2;
    double min_per_cust = 60;
    double cyclelimit = min_per_cust * hours;
    Item temp;
    long turnaways = 0;
    long customers = 0;
    long served = 0;
    long sum_line = 0;
    int wait_time = 0;
    long line_wait = 0;

    for (int cycle=0; cycle < cyclelimit; cycle++) {
        if (is_coming_new_customer(min_per_cust)) {
            if (line.is_full())
                turnaways++;
            else{
                customers++;
                temp.set(cycle);
                line.append(temp);
            }
        }
        
        if (wait_time <= 0 && !line.is_empty()) {
            line.leftpop(temp);
            cout << "sever a customer: " << temp << endl;
            wait_time = temp.ptime();
            line_wait += cycle - temp.when();
            served++;
        }
        if (wait_time > 0) {
            wait_time--;
            cout << "process 1 minues" << endl;
        }

        sum_line += line.length();
    }
    
    if (customers > 0) {
        cout << "customers accpeted:\t" << customers << endl;
        cout << "customers served:\t" << served << endl;
        cout << "turnaways:\t" << turnaways << endl;
        cout << "avaerage queue size:\t";
        cout.precision(2);
        cout.setf(ios_base::fixed, ios_base::floatfield);
        cout << (double) sum_line / cyclelimit << endl;
        cout << "average wait time:\t" ;
        cout << (double)line_wait / served << " minutes\n";
    }else 
        cout << "No coustomers!\n";
    cout << "Bye!\n";
}
}