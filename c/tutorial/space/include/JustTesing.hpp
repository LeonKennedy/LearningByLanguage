#ifndef JUSTTESTING_H_
#define JUSTTESTING_H_
#include <string>
#include <iostream>

using namespace std;

class JustTesting
{
    private:
        string words;
        int number;
    public:
        JustTesting(const string &s = "Just Tesing", int n = 0)
        {words = s; number = n ; cout << words << " constructed\n";}
        ~JustTesting() { cout << words << " destroyed\n";}
        void show() const {cout << words << ',' << number << endl;}
};
#endif