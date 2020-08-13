/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-08-11 23:25:45 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-12 00:27:06
 */
#include <string>
#include <vector>
#include <iostream>
#include "oper.hpp"

bool operator < (const book & b1, const book & b2)
{
    return b1.price < b2.price;
}
void show_book(const book & b)
{
    std::cout << b.text << "\t:\t" << b.price << std::endl;
}

void play_operator()
{
    std::vector<book> books;
    book a = {3.24, "aaaaa"};
    books.push_back(a);
    book b = {2.24, "bbbbb"};
    books.push_back(b);
    book c = {1.24, "ccccc"};
    books.push_back(c);
    for_each(books.begin(), books.end(), show_book);
    std::cout << "After sort ("<< books.size() <<"):" << std::endl;
    sort(books.begin(), books.end());
    for_each(books.begin(), books.end(), show_book);
}