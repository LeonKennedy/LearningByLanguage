cmake_minimum_required(VERSION 3.5.1)
project(READFROMREDIS)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
find_package(hiredis)

if(HIREDIS_FOUND)
    message(${HIREDIS_INCLUDE_DIR})
    include_directories(${HIREDIS_INCLUDE_DIR})
else(HIREDIS_FOUND)
    message(FATAL_ERROR "libhiredis not be found!")
endif(HIREDIS_FOUND)

add_executable(
    run
    exp.cpp
)

target_link_libraries(
    run
    ${HIREDIS_LIBRARY}
)