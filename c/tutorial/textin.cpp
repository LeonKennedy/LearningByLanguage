#include <iostream>

void TextInShow()
{
    using namespace std;
    char ch;
    int count;
    cin.get(ch);
    while (cin.fail() == false)
    {
        cout << ch;
        ++count;
        cin.get(ch);
    }
    cout << endl << count << " characters read\n";
    
}