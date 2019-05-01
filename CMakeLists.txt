cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(tcp_ip_communication)

set (CMAKE_CXX_STANDARD 14) # c++ 14

# Default cmake build type is Release (faster)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif(NOT CMAKE_BUILD_TYPE)

find_package(OpenCV 3.3.1 EXACT REQUIRED) # Transfer images (no need to be 3.3.1)

include_directories(cpp/include)
add_subdirectory(cpp)