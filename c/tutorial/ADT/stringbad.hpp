#include <iostream>
#ifndef STRINGBAD_H_
#define STRINGBAD_H_

class StringBad
{

    private:
        char * ar;
        int len;
        static int num_strings;
    public:
        StringBad(const char * s);
        StringBad();
        StringBad(StringBad & sb);
        ~StringBad();
        StringBad & operator = (const StringBad &);
        char & operator [](int);
        char & operator [](int) const;
        bool operator < (const StringBad &);
        bool operator > (const StringBad &);
        friend bool operator == (const StringBad &, const StringBad &);
        friend std::ostream & operator << (std::ostream & os, const StringBad & sb);
};

void play_string_bad();
#endif