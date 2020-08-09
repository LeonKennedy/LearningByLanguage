#include <iostream>
using std::cout;
using std::endl;

template <typename T> void counts();
template <typename T> void reports(T &);

template <typename TT>
class HasFriend
{
    private:
        TT item;
        TT item2;
        static int ct;
    public:
        HasFriend(const TT & i): item(i) {ct++;}
        ~HasFriend() {ct--;}
        friend void counts<TT>();
        friend void reports<>(HasFriend<TT> &);
};

template <typename T>
int HasFriend<T>::ct = 0;

template <typename T>
void counts()
{
    cout << "template size:\t" << sizeof(HasFriend<T>) << ';';
    cout << " count():\t" << HasFriend<T>::ct << endl;
}

template <typename T>
void reports (T & h)
{
    cout << "template size:\t" << sizeof(HasFriend<T>) << ';';
    cout << "report\t" << h.item << endl;
}


int main()
{
    cout << "No object declared:\t";
    counts<int>();
    HasFriend<int> hfi1(10);
    HasFriend<int> hfi2(20);
    HasFriend<double> hfi3(34.2);
    reports(hfi1);
    reports(hfi2);
    reports(hfi3);
    cout << "counts<int>() output:\t";
    counts<int>();
    cout << "counts<double>() output:\t";
    counts<double>();

    
}