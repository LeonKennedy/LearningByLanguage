#include <iterator>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <forward_list>
#include <queue>
#include <set>
#include <functional>
#include <map>
#include <valarray>
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
void output(const T & n) {std::cout << n << " ";}

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
    vector<double> gr8(arr1, arr1+LIM);

    copy(arr1, arr1 + LIM, out);
    
    vector<double> sum(LIM);
    transform(gr8.begin(), gr8.end(), arr2, out, plus<double>());
    cout << endl;
    copy(arr1, arr1 + LIM, out);
    cout << endl;

    // vector<double> prod(LIM);
    // transform(gr8.begin(), gr8.end(), prod.begin(), bind1st(multiplies<double> (), 2.5));
}

std::string & ToLower(std::string & s)
{
    std::transform(s.begin(), s.end(), s.begin(), tolower);
    return s;
}

void  play_transfrom()
{
    using namespace std;
    vector<string> words {"sfjie", "jiei", "qpjg"};
    for_each(words.begin() , words.end(), output<string>);

    set<string> wordset;
    transform(words.begin(), words.end(), 
        insert_iterator<set<string> >(wordset, wordset.begin()), ToLower);
    cout << "\nAlphabetic list of words:\n";
    for_each(wordset.begin() , wordset.end(), output<string>);

    map<string, int> wordmap;
    set<string>::iterator si;
    for(si = wordset.begin(); si!=wordset.end(); si++)
        wordmap[*si] = count(words.begin(), words.end(), *si);

    cout << "\nWord frequence:\n";
    for(si = wordset.begin(); si!=wordset.end(); si++)
        cout << *si << ": " << wordmap[*si] << endl;


}

void play_valarray()
{
    using namespace std;
    vector<double> data {3,4,56,2,4,2,6,6,47};
    sort(data.begin(), data.end());
    int size = data.size();
    valarray<double> numbers(size);
    copy(data.begin(), data.end(), begin(numbers));
    for_each(begin(numbers), end(numbers), output<double>);
    cout << endl;
    valarray<double> sq_rts(size);
    sq_rts = sqrt(numbers);
    cout.precision(4);
    for_each(begin(sq_rts), end(sq_rts), output<double>);
    cout << endl;
}

typedef std::valarray<int> vint;
void play_slice()
{
    using namespace std;
    vint numbres(20);
    numbres = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    numbres[slice(0,4,3)] = -1;
    for_each(begin(numbres), end(numbres), output<int>);
    vint vcol(numbres[slice(1,4,2)]);
    cout << "\nUse slice: \n";
    for_each(begin(vcol), end(vcol), output<double>);
    cout << "\n Set first columns to sum next two:\n";
    numbres[slice(0,4,3)] = vint(numbres[slice(1,4,3)]) + vint(numbres[slice(2,4,3)]);
    for_each(begin(numbres), end(numbres), output<int>);
    cout << endl;
}