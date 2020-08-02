#include <iostream>

enum egg_old {Small=7, Meduim, Large};
enum class egg {Small, Meduim, Large};
enum class shirt {Small, Meduim, Large};
int main()
{
    std::cout << "egg: " << "\t" << int(egg::Small)
            <<  '\t' << (int)egg::Meduim
            <<  '\t' << int(egg::Large) << std::endl;
    std::cout << "egg: " << '\t' << int(egg::Small)
            <<  '\t' << int(egg::Meduim)
            <<  '\t' << int(egg::Large) << std::endl;

    egg choice = egg::Large;
    shirt floyd = shirt::Meduim;

    egg_old one = Meduim;
    int king = one;
    // int ring = floyd;  作用域内枚举不能隐士转换
    if (king < Large)
        std::cout << 1 << std::endl;
    // if (king < shirt::Meduim)
    //     std::cout << 2 << std::endl;
    return 0;
}