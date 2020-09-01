#include "json.hpp"
#include <iostream>
#include <vector>

const static std::vector<std::string> interest_tags {
    "Niels",
    "ELFD",
    "djaief"
};


int main(int argc, char const *argv[])
{
    nlohmann::json j;
    j["pi"] = 3.141;
    j["happy"] = true;
    j["nothing"] = nullptr;
    j["answer"]["everything"] = 42;
    j["list"] = { 1, 0, 2 };
    j["object"] = { {"currency", "USD"}, {"value", 42.99} };
    std::cout << j.dump() << std::endl;
    nlohmann::json j2 = {
        {"pi", 3.141},
        {"happy", true},
        {"name", "Niels"},
        {"nothing", nullptr},
        {"answer", {
            {"everything", 42}
        }},
        {"list", {1, 0, 2}},
        {"object", {
            {"currency", "USD"},
            {"value", 42.99}
        }}
    };
    std::cout << j2.dump() << std::endl;
    nlohmann::json j3 = "{ \"happy\": true, \"pi\": 3.141 }"_json;
    std::cout << j3.dump() << std::endl;
    auto j4 = nlohmann::json::parse("{ \"happy\": true, \"pi\": 3.141 }");
    std::cout << j4.dump() << std::endl;
    std::string s = "Niels";

    if(std::find_if(interest_tags.begin(), interest_tags.end(), [&j2](std::string v){
        if (j2["name"].get<std::string>() == v)
            return true;
        else
            return false;
        }) != interest_tags.end()) {
            std::cout << "dfei" << std::endl;
        }
    return 0;
}
