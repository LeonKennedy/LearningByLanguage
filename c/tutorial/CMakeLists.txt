cmake_minimum_required(VERSION 3.5.1)

project(tutorial)
message("start my cmake file")
message("CMAKE_SOURCE_DIR=" ${CMAKE_SOURCE_DIR})
message("PROJECT_SOURCE_DIR=" ${PROJECT_SOURCE_DIR})
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall")

configure_file (
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h.in"
    "${PROJECT_SOURCE_DIR}/CmakeConfig.h"
)

include_directories("${PROJECT_SOURCE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}/reference/include")

# --- reference ---
# add_subdirectory(reference)
link_directories(${CMAKE_SOURCE_DIR}/reference/build)

add_executable(Run run.cpp)
TARGET_LINK_LIBRARIES(Run reference)


