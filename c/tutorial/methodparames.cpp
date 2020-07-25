/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-19 22:03:01 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-19 22:38:14
 */
#include <iostream>
#include <string>
#include <array>
using namespace std;

void show_array(int[], int);
void show_array_point(int *, int);
void show_array2(std::array<string, 4>);
void show_array_point2(const std::array<string, 4> *);

void PassParamsMethod()
{
    const int arr_size = 5;  
    int prices[arr_size] = {3,4,5, 6, 7};

    cout << "array( " << prices <<") size: " << sizeof(prices) << endl;
    show_array(prices, arr_size);
    show_array_point(prices, arr_size);

    const std::array<std::string, 4> snames = {"Spring", "Summer", "Fall", "Winter"};
    cout << "array2( " << &snames <<") size: " << sizeof(snames) << endl;
    show_array2(snames);
    show_array_point2(&snames);
}

void show_array(int x[], int size)
{
    cout << "show point("<< x <<") iterator, size: " << sizeof(x) << endl;
    for (int i=0; i < size; i++) {
        cout << x[i] << ' ';
    }
    cout << endl;
}

void show_array_point(int * x, int size)
{
    cout << "show point(" << x <<  ") iterator, size: " << sizeof(x) << endl;
    for (int i=0; i < size; i++) {
        cout << x[i] << ' ';
    }
    cout << endl;
}

void show_array2(std::array<string, 4> sname)
{
    cout << "show point("<< &sname <<") iterator, size: " << sizeof(sname) << endl;
    for (auto str : sname){
        cout << str << ' ';
    }
    cout << endl;
}

void show_array_point2(const std::array<string, 4> * psname)
{
    cout << "show point("<< psname <<") iterator, size: " << sizeof(psname) << endl;
    for (auto str : *psname){
        cout << str << ' ';
    }
    cout << endl;
}