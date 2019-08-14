cmake_minimum_required (VERSION 3.5 FATAL_ERROR)
project (CppPythonSocketTesting)

find_package(CppPythonSocket REQUIRED)

add_executable (testing test.cpp)
target_link_libraries (testing cpp_sockets)
