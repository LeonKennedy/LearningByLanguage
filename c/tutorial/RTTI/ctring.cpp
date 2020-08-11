#include <iostream>
#include <string>

void play_string()
{
    using namespace std;
    string one("Lottery Winner");
    cout << one << endl;
    string two(20, '$');
    cout << two << endl;


    const int i = 2000;
    int * pc = const_cast<int *> (&i);
    char alls[] = "All's well that ends well";
    string six(alls+6, alls+10);
    string seven(&alls[6], &alls[10]);
    cout << six << "," << seven << endl;
}

void capacity()
{
    using namespace std;
    cout << " ===  size  ===" << endl;
    string empty;
    string small = "bit";
    string larger = "Elephants are a girls best friend";
    cout << "Sizes:\n";
    cout << "\ttempty: " << empty.size() << endl;
    cout << "\tsmall: " << small.size() << endl;
    cout << "\tlarger: " << larger.size() << endl;
    cout << "Capacities:\n";
    cout << "\ttempty: " << empty.capacity() << endl;
    cout << "\tsmall: " << small.capacity() << endl;
    cout << "\tlarger: " << larger.capacity() << endl;

    empty.reserve(50);
    cout << "Capacity after empty reserve(50): "
        << empty.capacity() << endl;
}