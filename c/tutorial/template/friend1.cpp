#include <iostream>
using std::cout;
using std::endl;
template <typename T>
class HasFriend
{
    private:
        T item;
        static int ct;
    public:
        HasFriend(const T & i): item(i) {ct++;}
        ~HasFriend() {ct--;}
        friend void counts();
        friend void reports(HasFriend<T> &);
};

template <typename T>
int HasFriend<T>::ct = 0;

void counts()
{
    cout << "int count:\t" << HasFriend<int>::ct << ';';
    cout << "double count:\t" << HasFriend<double>::ct << endl;
}

void reports (HasFriend<int> & h)
{
    cout << "HasFriend<int>\t" << h.item << endl;
}

void reports (HasFriend<double> & h)
{
    cout << "HasFriend<double>\t" << h.item << endl;
}


int main()
{
    cout << "No object declared:\t";
    counts();
    HasFriend<int> hfi1(10);
    cout << "After hfi1 declared:\t";
    counts();
    HasFriend<int> hfi2(20);
    cout << "After hfi2 declared:\t";
    counts();
    HasFriend<double> hfi3(34.2);
    cout << "After hfi3 declared:\t";
    counts();

    reports(hfi1);
    reports(hfi2);
    reports(hfi3);
}