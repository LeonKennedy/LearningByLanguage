#include <iostream>
#include <new>
#include "newplace.hpp"

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