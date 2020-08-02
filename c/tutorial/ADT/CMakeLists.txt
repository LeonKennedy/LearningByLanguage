cmake_minimum_required(VERSION 3.5.1)
project(stack)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

include_directories("${PROJECT_SOURCE_DIR}")

add_executable(run run.cpp stack.cpp)