cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(tcp_ip_communication)

set (CMAKE_CXX_STANDARD 14) # c++ 14

# Default cmake build type is Release (faster)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif(NOT CMAKE_BUILD_TYPE)

# find_package(OpenCV REQUIRED) # If you want to sen

include_directories(cpp)

add_subdirectory(cpp)