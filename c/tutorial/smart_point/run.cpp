#include "report.hpp"
#include <memory>

int main()
{
    {
        std::shared_ptr<Report> ps(new Report("auto_ptr"));
        ps->comment();
    }
    {
        std::unique_ptr<Report> ps(new Report("auto_ptr"));
        ps->comment();
    }
    return 0;
}