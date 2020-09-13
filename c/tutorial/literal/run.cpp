struct length
{
    double value;
    enum unit {
        metre, kilometre, millimetre, centimetre, inch, foot, yard, mile,
    };
    static constexpr double factors[] = {
        1.0, 1000.0, 1e-3, 1e-2, 0.025, 0.3084, 0.9144, 1609.344
    };
    explicit length(double v, unit u = metre)
    {
        value = v * factors[u];
    }
};

length operator+ (length lhs, length rhs) 
{
    return length(lhs.value + rhs.value);
}
length operator"" _m (long double v)
{
    return length(v, length::metre);
}
length operator"" _cm (long double v)
{
    return length(v, length::centimetre);
}

int main(int argc, char const *argv[])
{
    auto l = 10.0_cm + 1.0_m;
    return 0;
}
