cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(tcp_ip_communication)

set (CMAKE_CXX_STANDARD 14) # c++ 14

# Default cmake build type is Release (faster)
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif(NOT CMAKE_BUILD_TYPE)

find_package(OpenCV REQUIRED) # Transfer images (no need to be 3.3.1)

include_directories(include)

add_library(cpp_sockets
    src/client.cpp
    # src/server.cpp
)
target_link_libraries(cpp_sockets ${OpenCV_LIBS})  # If image sending capabilities

add_executable(cpp_client_test cpp_client_test.cpp)
target_link_libraries(cpp_client_test cpp_sockets)





