/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-18 17:19:14 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-18 22:47:00
 */
#include <iostream>

typedef char * pstring;

void ConstPointerShow()
{
    using namespace std;
    const int i =2;
    constexpr int ii = 3;
    const int * pi = &i;
    const int * pii = &ii;
    pii = &i;
    const int *const pcii = &ii;
    // pcii = &i;    //error
    
    char works[5] = {'a','b','c','e','g'};
    const char * pchar;
    pchar = works;
    const pstring cstr = 0;
    // cstr = works;  //error
    const pstring *ps = &cstr;

    auto lba = *pi;
    decltype(*pi) fei = i;
    auto sfji = (i);
    auto fjdisfa = &i;

}

void PointerArithmetic()
{
    using namespace std;
    double wages[3] {10000.0, 20000.0, 30000.0};
    short stacks[3] {3, 2, 1};
    
    double * pw = wages;
    short * ps = &stacks[0];

    pw  = pw + 1;
    cout << *pw << endl;

    short tell[10];
    cout << tell << endl;
    cout << &tell << endl;

    int * pz = new int [10];
    delete [] pz;

}


struct antarctia_years_end
{
    int year;
};

void CombineType()
{
    using namespace std;
    antarctia_years_end s01, s02, s03;;
    
    s01.year = 1998;
    antarctia_years_end * pa = &s02;
    pa->year = 2000;

    antarctia_years_end trio[3];
    trio[0].year = 2003;
    (trio+1)->year = 2004;

    const antarctia_years_end * arp[3] {&s01, &s02, &s03};
    cout << arp[0]->year << endl;
    //const antarctia_years_end ** ppa = arp;
    auto ppa = arp;

    cout << (*ppa)->year << endl;
    cout << (*(ppa+1))->year << endl;
}


void plusplus()
{
    using namespace std;
    int a[3] {1,2,3};
    int * pa = a;
    cout << *++pa << endl; // 2
    cout << *pa++ << endl; // 2 change list
    cout << ++*pa << endl; // 2 change list
    for (int i = 0 ; i < 3; i++)
        cout << a[i];
    cout << endl;
}