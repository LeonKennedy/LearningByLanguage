cmake_minimum_required(VERSION 3.5.1)

project(sjfieaf)
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

#link_directories(${PROJECT_SOURCE_DIR}/static_lib)
configure_file (
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h.in"
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h"
)

include_directories(${PROJECT_SOURCE_DIR}/static_lib/include)
find_library(hello libhello.a ${PROJECT_SOURCE_DIR}/static_lib/build/ REQUIRED)
message(${HELLO_VAR})
if (${HELLO_VAR}) 
    message("cofee")
endif ()
message("cofe232")
add_executable(run run.cpp)
target_link_libraries(
    run
    ${hello}
)

