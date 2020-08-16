#include "move_semantics.hpp"
#include <iostream>

int Useless::ct = 0;

Useless::Useless()
{
    using namespace std;
    ++ct;
    n = 0;
    pc = nullptr;
    cout << "default constructor called; number of object: " << ct << endl;
    ShowObject();
}

Useless::Useless(int k): n(k)
{
    using namespace std;
    ++ct;
    cout << "$ int constructor called; number of object: " << ct << endl;
    pc = new char[n];
    ShowObject();
}

Useless::Useless(int k, char ch): n(k)
{
    using namespace std;
    ++ct;
    cout << "$ int, char constructor called; number of object: " << ct << endl;
    pc = new char[n];
    for(int i=0; i< n;i++)
        pc[i] = ch;
    ShowObject();
}

Useless::Useless(const Useless & f): n(f.n)
{
    using namespace std;
    ++ct;
    cout << "$ const constructor called; number of object: " << ct << endl;
    pc = new char[n];
    for(int i=0; i< n;i++)
        pc[i] = f.pc[i];
    ShowObject();
}

Useless::Useless(Useless && f): n(f.n)
{
    using namespace std;
    ++ct;
    cout << "$ move constructor called; number of object: " << ct << endl;
    pc = f.pc;
    f.pc = nullptr;
    f.n = 0;
    ShowObject();
}

Useless::~Useless()
{
    using namespace std;
    cout << "destructor called; objects left: " << --ct << endl;
    cout << "deleted object: \n";
    ShowObject();
    delete [] pc; 
}

Useless Useless::operator+(const Useless & f) const
{
    using namespace std;
    cout << "Entering operator+()\n";
    Useless tmp = Useless(n + f.n);
    for (int i=0;i< n;i++)
        tmp.pc[i] = pc[i];
    for (int i = n; i < tmp.n; i++)
    {
        tmp.pc[i] = f.pc[i-n];
    }
    cout << "temp object:\n";
    cout << "Leaving operator+()\n";
    return tmp;
}

void Useless::ShowObject() const
{
    using namespace std;
    cout << "Number of elements: " << n;
    cout << " Data address: " << (void*) pc << endl;
}

void Useless::ShowData() const
{
    using namespace std;
    if (n == 0)
        cout << "(object empty)";
    else 
        cout << (void *) pc << " ";
        for (int i = 0; i < n; i++)
        {
            cout << pc[i];
        }
    cout << endl;
}

void play_useless()
{
    int ct = 0;
    Useless one(10, 'x');
    Useless two = one;
    Useless three(20, 'o'); 
    Useless four (one + three);
    std::cout << "object one: ";
    one.ShowData();
    std::cout << "object two: ";
    two.ShowData();
    std::cout << "object three: ";
    three.ShowData();
    std::cout << "object four: ";
    four.ShowData();
    std::cout << " == Bey == \n";  
}