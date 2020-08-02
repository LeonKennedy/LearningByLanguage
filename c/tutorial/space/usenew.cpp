/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-27 23:57:08 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-28 00:38:25
 */
#include <iostream>

struct chaff
{
    char dross[20];
    int slag;
};
char buffer1[50];
char buffer2[200];

void exp1()
{
    using namespace std;
    int * a = new int(6);
    int * ar = new int[4] {2,4,5,6};
    struct where {double x; double y; double z;};
    where * one = new where {2.5, 3.6, 4.8};

    cout << *a << '\t' << *(ar+1)<<'\t' << (*one).x << endl; delete a;  delete one; delete [] ar;

    // -----

    
    chaff *p1, *p2;
    int *p3, *p4;
    p1 = new chaff;
    p3 = new int[20];

    //  指定内存
    p2 = new (buffer1) chaff;
    p4 = new (buffer2) int[20];

    delete p1; delete p2; delete [] p3; delete [] p4;

    

}