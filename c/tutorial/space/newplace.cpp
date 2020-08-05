#include <iostream>
#include <new>
#include "newplace.hpp"
#include "JustTesing.hpp"

const int BUF = 512;
const int N = 5;
char buffer[BUF];

void ExpNewPlace()
{
    using namespace std;
    double *pd1, *pd2;
    int i;
    cout << "Calling new and placement new:\n";
    pd1 = new double[N];
    pd2 = new (buffer) double[N];
    show_memory(pd1, pd2, 20);

    cout << "\nCalling new and placement new a second time:\n";
    double *pd3, *pd4;
    pd3 = new double[N];
    pd4 = new (buffer) double[N];   // overwrite old data
    show_memory(pd3, pd4, 40);
    cout << "\nCalling new and placement new a third time:\n";
    delete [] pd1;
    pd1 = new double[N];
    pd2 = new (buffer + N * sizeof(double)) double[N];
    show_memory(pd1, pd2, 60);

    delete [] pd1;
    delete [] pd3;
    // delete [] pd2 会报错 不可以delete static上
}

void show_memory(double * p1, double *p2, double inc)
{
    using namespace std;
    cout << "Memory contents: \n";
    for (int i=0; i < N; i++)
        p2[i] = p1[i] = 1000 + inc * i;
    cout << "Memory addresses: \n" << "   heap: " << p1 << "  static:" << (void *)buffer << endl;
    for (int i=0; i< N; i++) {
        cout << '\t' << p1[i] << "\at " << &p1[i] << ";";
        cout << '\t' << p2[i] << " at " << &p2[i] << endl;
    }
}

void ExpNewPlace2()
{
    char * buffer = new char[BUF];
    JustTesting *pc1, *pc2;
    
    pc1 = new (buffer) JustTesting;
    pc2 = new JustTesting("Heap1", 20);

    cout << "Memory block addresses: \n" << "buffer: " << (void *) buffer;
    cout << " pure buffer: " << buffer;
    cout << "  heap: " << pc2 << endl;
    cout << "Memory contents: \n";
    cout << pc1 << ": ";
    pc1->show();
    cout << pc2 << ": ";
    pc2->show();

    JustTesting *pc3, *pc4;
    pc3 = new (buffer + sizeof(JustTesting)) JustTesting("Bad Idea", 6);
    pc4 = new JustTesting("Heap2", 10);
    cout << " pure buffer: " << buffer << endl;
    cout << "Memory contents:\n" << pc3 << ": " ;
    pc3->show();
    cout << pc4 << ": " ;
    pc4->show();

    delete pc2;
    delete pc4;
    pc3->~JustTesting();
    pc1->~JustTesting();
    delete [] buffer;
    cout << "Bye" << endl;
}