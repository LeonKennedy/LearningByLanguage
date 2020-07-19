cmake_minimum_required(VERSION 3.5.1)

project(tutorial)
message("start my cmake file")
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

configure_file (
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h.in"
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h"
)

include_directories("${PROJECT_SOURCE_DIR}")

add_library(LimitFunctions typecast.cpp)
include_directories ("${PROJECT_SOURCE_DIR}/LimitFunctions")

#add_executable(Limit limits.cpp)
#add_executable(TypeCast typecast.cpp)
add_executable(Run run.cpp)