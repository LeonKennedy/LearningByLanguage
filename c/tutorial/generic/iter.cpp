#include <iterator>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <forward_list>
#include <queue>
#include <set>
#include <functional>
#include "iter.hpp"

void play_ostream_iter()
{
    int cast[10] = {6,7,8,9,10,32,44,13,4,1};
    std::vector<int> dices(10);
    std::copy(cast, cast + 10, dices.begin());
    std::ostream_iterator<int, char> out_iter(std::cout, " ");
    *out_iter++ = 15;
    std::cout << std::endl;
    copy(dices.rbegin(), dices.rend(), out_iter);
}

template <typename T>
void output(T & n) {std::cout << n << " ";}

void play_insert_iter()
{
    std::string s1[4] = {"1111", "2222", "3333", "4444"};
    std::string s2[2] = {"aaaa", "bbbb"};
    std::string s3[2] = {"gggg", "hhhh"};
    std::vector<std::string> words(4);
    copy(s1, s1 +4, words.begin());
    for_each(words.begin(), words.end(), output<std::string>);
    std::cout << std::endl;

    copy(s2, s2 +2, std::back_insert_iterator<std::vector<std::string> > (words));
    for_each(words.begin(), words.end(), output<std::string>);
    std::cout << std::endl;

    copy(s3, s3 +2, std::insert_iterator<std::vector<std::string> > (words, words.begin()));
    for_each(words.begin(), words.end(), output<std::string>);
    std::cout << std::endl;
}



void play_list_iter()
{
    using namespace std;
    list<int> one(5,2);
    int stuff[6] = {1,2,4,8,6, 2};
    list<int> two;
    two.insert(two.begin(), stuff, stuff + 6);
    int more[6] = {6,5,2,1,4,5};
    list<int> three(two);
    cout << "List three: ";
    for_each(three.begin(), three.end(), output<int>);
    cout << endl;
    three.insert(three.end(), more, more+6);
    three.remove(2);
    for_each(three.begin(), three.end(), output<int>);
    cout << endl << "list splic: ";
    list<int>::iterator it = one.begin();
    three.splice(three.begin(), one);
    for_each(three.begin(), three.end(), output<int>);
    cout << endl;
    for_each(one.begin(), one.end(), output<int>);
    cout << endl;
    cout << *it << endl << "after sort & unique: ";
    three.sort();
    three.unique();
    for_each(three.begin(), three.end(), output<int>);
    cout << endl << "merge sort two: ";
    two.sort();
    three.merge(two);
    for_each(three.begin(), three.end(), output<int>);
    cout << endl;
}

void show_queue(std::priority_queue<std::string> & pq)
{
    std::string s = pq.top();
    while (!pq.empty()) {
        std::string s = pq.top();
        std::cout << s << " ";
        pq.pop();
    }
    std::cout << std::endl;
    
}
void play_new_container()
{
    using namespace std;
    forward_list<int> fl(3, 2);
    for_each(fl.begin(), fl.end(), output<int>);
    cout << endl;
    std::string wrds[4] { "one", "two", "three", "four"};
    std::priority_queue<std::string> words { std::begin(wrds), std::end(wrds)};
    show_queue(words);
}

void play_set()
{
    using namespace std;
    const int N = 6;
    string s1[N] {"buffoon", "thinker", "for", "heavy", "can", "for"};
    string s2[N] {"metal", "any", "food", "elegant", "deliver", "for"};

    set<string> A(s1, s1 +N);
    set<string> B(s2, s2 +N);
    ostream_iterator<string, char> out (cout, " ");
    cout << "set A: ";
    copy(A.begin(), A.end(), out);
    cout << endl << "Union of A and B: \n";
    set_union(A.begin(), A.end(), B.begin(), B.end(), out);

    cout << endl << "Intersection of A and B:\n";
    set_intersection(A.begin(),A.end(), B.begin(), B.end(), out);

    cout << endl << "Difference of A and B:\n";
    set_difference(A.begin(),A.end(), B.begin(), B.end(), out);

    set<string> C;
    cout << endl << "Set C:\n";
    set_union(A.begin(), A.end(), B.begin(), B.end(), insert_iterator<set<string> >(C, C.begin()));
    copy(C.begin(), C.end(), out);

    string s3("grungy");
    C.insert(s3);
    cout << endl;
    copy(C.begin(), C.end(), out);

    cout << endl << "showing a range:\n";
    copy(C.lower_bound("bhost"), C.upper_bound("spool"), out);
    cout << endl;
}

void play_funadap()
{
    using namespace std;
    ostream_iterator<double, char> out(cout, " ");
    const int LIM = 6;
    double arr1[LIM] {28,29,30,35,38,59};
    double arr2[LIM] {63,64,69,75,80,99};
    copy(arr1, arr1 + LIM, out);
    
    vector<double> sum(LIM);
    transform(arr1, arr1+LIM, arr2, arr2+LIM, plus<double>());
    cout << endl;
    copy(arr1, arr1 + LIM, out);
    cout << endl;

    vector<double> gr8(arr1, arr1+LIM);
    vector<double> prod(LIM);
    transform(gr8.begin(), gr8.end(), prod.begin(), bind1st(multiplies<double> (), 2.5));
    

}