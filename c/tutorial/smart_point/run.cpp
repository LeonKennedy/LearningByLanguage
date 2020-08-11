#include "report.hpp"
#include <memory>

int main()
{
    {
        // reference counting
        std::shared_ptr<Report> ps(new Report("shared_ptr"));
        ps->comment();
    }
    {
        // ownership
        std::unique_ptr<Report> ps(new Report("unique_ptr"));
        ps->comment();
    }
    return 0;
}