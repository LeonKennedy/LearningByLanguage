#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <complex>
#include <bitset>

struct length
{
    double value;
    enum unit
    {
        metre,
        kilometre,
        millimetre,
        centimetre,
        inch,
        foot,
        yard,
        mile,
    };
    static constexpr double factors[] = {
        1.0, 1000.0, 1e-3, 1e-2, 0.025, 0.3084, 0.9144, 1609.344};
    explicit length(double v, unit u = metre)
    {
        value = v * factors[u];
    }
};

length operator+(length lhs, length rhs)
{
    return length(lhs.value + rhs.value);
}
length operator"" _m(long double v)
{
    return length(v, length::metre);
}
length operator"" _cm(long double v)
{
    return length(v, length::centimetre);
}

int main(int argc, char const *argv[])
{
    using namespace std;
    auto l = 10.0_cm + 1.0_m;

    auto w = "Hello world"s.substr(0, 5);
    std::cout << w << std::endl;
    this_thread::sleep_for(500ms);

    unsigned mask = 0b111'000'000;
    long r_earch_equatorial = 6'378'137;
    double pi = 3.14159'26535'89793;
    const unsigned magic = 0x44'42'47'4E;
    unsigned b = 0b1010101;
    std::cout << b << ':' << bitset<7>(b) << std::endl;

    //对齐静态断言
    // static_assert((alig & (alig - 1))) == 0, "alignment must be power of two";
    return 0;
}
