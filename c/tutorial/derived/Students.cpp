#include "Students.hpp"

namespace STUDENT
{
    ostream &Student::arr_out(ostream &os) const
    {
        for (int i = 0; i < ArrayDb::size(); i++)
        {
            // os << ((ArrayDb)*this)[i] << '\t';
            os << ArrayDb::operator[](i) << '\t';
        }
        return os;
    }
    const string & Student::name() const
    {
        return (const string &)*this;
    }

    // operator Student::double() const
    // {
    //     return 3.4;
    // }
    double Student::average() const
    {
        return ArrayDb::size() > 0 ? ArrayDb::sum() / ArrayDb::size() : 0;
    }

    ostream &operator<<(ostream &os, const Student &s)
    {
        os << (const string &)s << "\t scores: ";
        s.arr_out(os);
        os << endl;
        return os;
    }

    double & Student::operator[](int i)
    {
        return ArrayDb::operator[](i);
    }

    void play()
    {
        Student ada[3] = {Student("coffee", 5),  Student("red", 5), Student("leon", 5)};
        for (int i=0; i< 3;i++) {
            set(ada[i], 5);
            cout << ada[i];
        }
    }

    void set(Student & s, int n)
    {
        for (int i=0; i< n ; i++) {
            s[i] = rand();
        }
    }
} // namespace STUDENT
