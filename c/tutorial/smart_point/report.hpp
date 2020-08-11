#include <string>
#include <iostream>
class Report
{
    private:
        std::string str;
    public:
        Report(const std::string s): str(s)
            { std::cout << "Object created!\n";}
        ~Report(){ std::cout << "Object deleted!\n";}
        void comment() const { std::cout << str << "\n";}
};