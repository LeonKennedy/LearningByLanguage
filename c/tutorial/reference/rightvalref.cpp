#include "rightvalref.hpp"
#include <iostream>

inline double f(double tf) {return 5.0 * (tf -32.0) /9;}
void play_right_val_ref()
{
    using namespace std;
    int x = 14;
    int y = 12;
    int && rvr = x + y;

    double tc = 21.5;
    double && rd1 = 7.07;
    double && rd2 = 1.8 * tc + 32.1;
    double && rd3 = f(rd2);

    cout << "tc:\t" << tc << "\t" << &tc <<  endl;
    cout << "rd1:\t" << rd1 << "\t" << &rd1 << endl;
    cout << "rd2:\t" << rd2 << "\t" << &rd2 << endl;
    cout << "rd3:\t" << rd3 << "\t" << &rd3 << endl;
}
