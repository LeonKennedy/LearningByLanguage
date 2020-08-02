cmake_minimum_required(VERSION 3.5.1)

message("start reference")
project(reference)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

include_directories(include)
add_library(reference  
example.cpp
twoswap.cpp)
