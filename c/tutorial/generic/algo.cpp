#include "algo.hpp"
#include <algorithm>
#include <vector>
#include <list>
#include <iostream>

template <typename T>
void show(const T &s) { std::cout << s << " ";}

void play_permutation()
{
    using namespace std;
    vector<int> rank {3,4,5,3};
    while (next_permutation(rank.begin(), rank.end())) {
        for_each(rank.begin(), rank.end(), show<int>);
        cout << endl;
    }
}

void remove_and_erase()
{
    using namespace std;
    list<int> lran {3,6,1,6,9,8};
    list<int>::iterator last = remove(lran.begin(), lran.end(), 6);
    for_each(lran.begin(), lran.end(), show<int>);
    cout << endl << "After erase: " << endl;
    lran.erase(last, lran.end());
    for_each(lran.begin(), lran.end(), show<int>);
}