#include <fstream>
#include <ostream>
#include <string>
#include <iostream>

void fileInOut()
{
    std::ifstream input_file;
    std::ofstream output_file;
    std::string filename = "ofstream_data.txt";
    input_file.open(filename);
    output_file.open("tmp.txt");

    int year;
    double a_price;
    double d_price;
    if (!input_file.is_open()) {
        std::cout << "Could not open the file " << filename << std::endl;
    }
    while (input_file.good())
    {
        input_file >> year;
        std::cout << year << std::endl;
        output_file << year;

        input_file >> a_price;
        std::cout << a_price << std::endl;
        output_file << a_price;
    }
    if (input_file.eof()) {
        output_file.close();
        input_file.close();
    }

}