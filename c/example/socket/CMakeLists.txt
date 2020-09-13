cmake_minimum_required(VERSION 3.5.1)
project(SocketServer)
set(CMAKE_CXX_STANDARD 11)

add_executable(
    server
    server.cpp
)

add_executable(
    getinfo
    GetAddrInfo.cpp
)