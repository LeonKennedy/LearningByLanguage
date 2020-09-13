/*
 * @Author: LeonSccotKennedy 
 * @Date: 2020-07-18 12:26:06 
 * @Last Modified by: LeonSccotKennedy
 * @Last Modified time: 2020-08-22 15:02:40
 */
#include "ComplexType.cpp"
#include "pointer.cpp"
#include "ofstream.cpp"
#include "methodparames.cpp"
#include "example.hpp"

int main()
{
    char w[] = "abcd";
    char *pw = "abcd";
    std::cout << sizeof(w) << std::endl;
    std::cout << sizeof(pw) << std::endl;
    ConstPointerShow();
    // PointerArithmetic();
    // CombineType();
    // plusplus();
    // fileInOut();
    // PassParamsMethod();
    // show_function_point();
    // ComplexShow();
    // TwoSwapExp();
    // exp_static();
    return 0;
}