/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-18 17:19:14 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-18 22:47:00
 */
#include <iostream>

void PointerShow()
{
    using namespace std;
    int updates = 6;
    int * p_updates;
    p_updates = &updates;
    
    cout << "Val: " << updates << " *point: " << *p_updates << endl;

    cout << "point: " << p_updates << " &point: " << &updates << endl;

    *p_updates = *p_updates + 1;
    cout << "after *point ++: " << updates << endl;

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


// void show_array(int[] a)
// {
//     using namespace std;
//     for (int i = 0 ; i < 3; i++)
//         cout << a[i];
//     cout << endl;
// }
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