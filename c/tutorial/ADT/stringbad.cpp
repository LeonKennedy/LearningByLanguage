#include <iostream>
#include "stringbad.hpp"

using std::cout;
int StringBad::num_strings = 0;

StringBad::StringBad()
{
    len = 0;
    ar = new char[len + 1];
    ar[0] = '\0';
}

StringBad::StringBad(const char * s)
{
    len = std::strlen(s);
    ar = new char[len + 1];
    std::strcpy(ar, s);
    num_strings++;
    cout << num_strings << ": <" << ar << "> object created\n";
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

StringBad & StringBad::operator = (const StringBad & sb)
{
    if (this == &sb)
        return *this;
    delete [] ar;
    len = sb.len;
    ar = new char[len + 1];
    std::strcpy(ar, sb.ar);
    num_strings++;
    cout << num_strings << ": <" << ar << "> object created\n";
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


