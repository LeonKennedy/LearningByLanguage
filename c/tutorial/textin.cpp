#include <iostream>

void TextInShow()
{
    using namespace std;
    const int Size = 20;
    char ch[80];
    int count;
    cin >> ch;
    while (cin.fail() == false)
    {
        cout << ch;
        ++count;
        cin.get(ch, Size);
    }
    cout << endl << count << " characters read\n";
    
}