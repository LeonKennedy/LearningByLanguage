#include <iostream>
#include "stringbad.hpp"

using std::cout;
int StringBad::num_strings = 0;

StringBad::StringBad()
{
    len = 0;
    ar = new char[len + 1];
    ar[0] = '\0';
    num_strings++;
}

StringBad::StringBad(const char * s)
{
    len = std::strlen(s);
    ar = new char[len + 1];
    std::strcpy(ar, s);
    num_strings++;
    cout << num_strings << ": <" << ar << "> object created by char*\n";
}

StringBad::StringBad(StringBad & sb)
{
    len = sb.len;
    ar = new char[len + 1];
    std::strcpy(ar, sb.ar);
    num_strings++;
    cout << num_strings << ": <" << ar << "> object created\n";
}

StringBad::~StringBad()
{
    cout << "<" << ar << "> object delete,";
    cout << --num_strings << " left\n";
    delete [] ar;
}

int StringBad::length()
{
    return len;
}

StringBad & StringBad::operator = (const StringBad & sb)
{
    if (this == &sb)
        return *this;
    delete [] ar;
    len = sb.len;
    ar = new char[len + 1];
    std::strcpy(ar, sb.ar);
    cout << num_strings << ": <" << ar << "> object created by assign\n";
    return *this;
}

bool StringBad::operator < (const StringBad & sb)
{
    return ar < sb.ar;
}

bool StringBad::operator > (const StringBad & sb)
{
    return (std::strcmp(ar, sb.ar) > 0);
}

std::ostream & operator << (std::ostream & os, const StringBad & sb)
{
    os << sb.ar;
    return os;
}
std::istream & operator >> (std::istream & is, const StringBad & sb)
{
    is >> sb.ar;
    return is;
}

bool operator == (const StringBad & sb1, const StringBad & sb2)
{
    return (std::strcmp(sb1.ar,sb2.ar) == 0);
}

char & StringBad::operator [](int i)
{
    return ar[i];
}

char & StringBad::operator [](int i) const
{
    return ar[i];
}

void callme1(StringBad & sb)
{
    cout << "String pass by reference: " << "<" << sb << ">\n";
}

// 会自动生成默认构造函数 StringBat(const StringBad &)
void callme2(StringBad sb)
{
    cout << "String pass by value: " << "<" << sb << ">\n";
}

void play_string_bad() {
    using std::endl;
    cout << "Starting an inner block.\n";
    StringBad headline1("Celery Stalks at Midnight");
    StringBad headline2("Lettuce Prey");
    StringBad sports("Spinach Leaves Bow1 for Dollars");
    cout << headline1 << endl;
    cout << headline2 << endl;
    cout << sports << endl;
    callme1(headline1);
    callme2(headline2);
    cout << "headline2: " << headline2 << endl;
    cout << "Initialize one object to another: \n";
    StringBad sailor = sports; // 复制构造函数
    cout << "sailor: " << sailor << endl;
    cout << "Assign one object to anther: \n ";
    StringBad knot;
    knot = headline1;  // 赋值构造函数
    cout << "knot: " << knot << endl;
    cout << " -- Exiting the block. -- \n";

    cout << (headline1 < headline2) << endl;
    cout << (headline1 > headline2) << endl;
    cout << (headline1 == knot) << endl;

    headline1[2] = 'r';
    cout << headline1 << endl;

    const StringBad answer("futile");
    cout << answer[2] <<  endl;

    knot = "hell olenji";
}

void saying()
{
    using namespace std;
    const int ArSize = 10;
    const int MaxLen = 81;
    // StringBad sayings[ArSize] = {
    //     StringBad("ccdsadfe"), 
    //     StringBad("ccbbb aaaadsadfe"), 
    //     StringBad("sdfaefv sdafe")
    // };

    StringBad sayings[ArSize];

    const int total = 3;
    char * dfe[total] =  {"ccdsadfe","ccbbb aaaadsadfe",  "sdfaefv sdafe"};
    cout << "Here are your sayings: \n";
    for (int i = 0; i < total; i++) {
        sayings[i] = dfe[i];
        cout << sayings[i] << endl;
    }

    StringBad * shortest = &sayings[0];
    StringBad * first = &sayings[1];
    for (int j = 1; j < total; j++) {
        if (sayings[j].length() < shortest[j].length()) 
            shortest = &sayings[j];
        if (sayings[j] < *first) 
            first = &sayings[j];
    }

    srand(time(0));
    int choice = rand() % total;
    StringBad * favorite = new StringBad(sayings[choice]);
    delete favorite;
    cout << "Bye!" << endl;
}


