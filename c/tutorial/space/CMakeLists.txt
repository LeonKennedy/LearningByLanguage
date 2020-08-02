cmake_minimum_required(VERSION 3.5.1)
project(space)
message("start my cmake file")
#message("CMAKE_SOURCE_DIR=" ${CMAKE_SOURCE_DIR})
#message("PROJECT_SOURCE_DIR=" ${PROJECT_SOURCE_DIR})
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

include_directories("${PROJECT_SOURCE_DIR}/include")
include_directories("${PROJECT_SOURCE_DIR}")
add_library(space 
newplace.cpp
usenew.cpp)
add_executable(run run.cpp)
TARGET_LINK_LIBRARIES(run space)