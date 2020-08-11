/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-08-11 23:17:12 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-11 23:26:12
 */

#include <string>
#include <vector>
#include <iostream>
struct book
{
    double price;
    std::string text;
};

bool operator < (const book & b1, const book & b2);

void show_book(const book & b);

void play_operator();
