#include <string>
#include <valarray>
#include <iostream>

namespace STUDENT
{
    using namespace std;
    class Student : private std::string, private std::valarray<double>
    {
        private:
            typedef std::valarray<double> ArrayDb;
            std::ostream & arr_out(std::ostream & os) const;
        public:
            using ArrayDb::min;
            using ArrayDb::max;
            Student(const double *pd, const char * str = "coffee", int s = 5) : std::string(str), ArrayDb(pd, s) {}
            Student(): std::string("Null") , ArrayDb() {}
            explicit Student (int n): std::string("Null"), ArrayDb(n) {}
            explicit Student (const std::string & s) : std::string(s), ArrayDb() {}
            Student(const std::string & s, int n) : string(s), ArrayDb(n) {}
            Student(const std::string & s, const ArrayDb & a) :std::string(s), ArrayDb(a) {}

            const string & name() const;
            double average() const;

            double & operator[](int i);
            operator double() const {return 3.4;};
            friend ostream & operator<<(ostream & os, const Student &s);

    };

    void play();
    void set(Student & s, int n);
} // namespace STUDENT
