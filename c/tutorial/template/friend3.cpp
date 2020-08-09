#include <iostream>
using std::cout;
using std::endl;


template <typename T>
class HasFriend
{
    private:
        T item;
    public:
        HasFriend(const T & i): item(i) {}
        //  friend void counts<>();
        template <typename C> friend void reports(C &);
        template <typename C, typename D> friend void show(C &, D &);
};

// template <typename T>
// void counts()
// {
//     cout << "template size:\t" << sizeof(HasFriend<T>) << ';';
//     cout << " count():\t" << HasFriend<T>::ct << endl;
// }

template <typename T>
void reports (T & h)
{
    cout << "template size:\t" << sizeof(T) << ';';
    cout << "report\t" << h.item << endl;
}

template <typename C, typename D>  void show(C & c, D & d)
{
    cout << c.item << ", " << d.item << endl;
}


int main()
{
    HasFriend<int> hfi1(10);
    HasFriend<int> hfi2(20);
    HasFriend<double> hfi3(34.2);
    show(hfi1, hfi3);
    show(hfi3, hfi2);
    reports(hfi2);
    // reports(hfi3);
    // cout << "counts<int>() output:\t";
    // counts<int>();
    // cout << "counts<double>() output:\t";
    // counts<double>();
}