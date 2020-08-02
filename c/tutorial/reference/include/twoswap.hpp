#ifndef TWOSWAP_H_
#define TWOSWAP_H_
struct job
{
    char name[40];
    double salary;
    int floor;
};
template <typename T>
void Swap(T &a, T &b);
template <> void Swap<job>(job &j1, job &j2);  // explicit instantiation

void TwoSwapExp();
double belm = 10.3;

#endif