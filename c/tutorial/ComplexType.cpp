/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-18 12:26:31 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-07-18 17:09:34
 */

#include <iostream>
#include <cstring>
#include <string>

void StringsShow1()
{
    std::cout << "[String] show" << std::endl;
    const int Size = 15;
    char name1[Size];
    char name2[Size] = "C++owboy";
    std::cout << name2 << " strlen: " << strlen(name2);
    std::cout << " sizeof: " << sizeof(name2) << std::endl;

    std::cout << "Enter your name: \n";
    std::cin.getline(name1, Size);
    std::cout << "Enter your favorite games: \n";
    char games[20];
    std::cin.getline(games, 20);
    std::cout << "I like games: " << games;
    std::cout << " || " << name1 << std::endl;
    
}

void StringsShow2()
{
    std::cout << "[String] show 2" << std::endl;
    const int Size = 15;
    char charr1[20];
    char charr2[20] = "coffee";
    std::string str1;
    std::string str2 = "leon";
    str1 = str2;
    strcpy(charr1, charr2);

    str1 += " kennedy";
    strcat(charr1, "_red");

    int len1 = str1.size();
    int len2 = strlen(charr1);

    std::cout << "The string (" << str1 << ") contains " << len1 << " characters." << std::endl;
    std::cout << "The string (" << charr1 << ") contains " << len2 << " characters." << std::endl;

}

void StringsShow3()
{
    using namespace std;
    cout << R"+*(Jim "King" Tutt use "\n| instead of ( endl. )")+*" << endl;
}

void StringsShow()
{
    StringsShow1();
    StringsShow2();
    StringsShow3();
}

// --------  struct ---------
struct inflatable
{
    std::string name;
    float volume;
    double price;
};

union one3all
{
    int int_val;
    long long_val;
    double double_val;
};

void StructShow()
{
    using namespace std;
    inflatable guest = {"Glorious Gloria", 1.8, 29.99};
    inflatable pal = {"Audacious Arthur", 3.12, 32.99};
    inflatable guests[2] = {
        {"Bambi", 0.5, 21.99},
        {"Godzilla", 2000, 455.99}
    };
    one3all price;
    cin >> price.int_val;
    cout << price.int_val << " sizeof: " << sizeof (price.int_val) <<endl;
    cin >> price.long_val;
    cout << price.long_val <<  " sizeof: " << sizeof (price.int_val) << endl;
    cout << price.int_val << " sizeof: " << sizeof (price.int_val)<< endl;
}

void EnumShow()
{
    enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet};
    enum bits {one = 1, two = 2, four = 4, eight = 8};
    enum bigstep {first, second = 100, third}; //third == 101
    
    spectrum band = blue;
    std::cout << "spectrum is " << band << std::endl;
    
    int color = orange + 1;
    std::cout << "color is " << color << std::endl;

    band = spectrum(4);
    std::cout << "spectrum is " << band << std::endl;

}

void ComplexShow()
{
    StringsShow();
    // StructShow();
    // EnumShow();
}