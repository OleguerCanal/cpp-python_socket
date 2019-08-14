cmake_minimum_required (VERSION 3.5 FATAL_ERROR)
project (CppPythonSocket)

# Version number
set (CppPythonSocket_VERSION_MAJOR 0)
set (CppPythonSocket_VERSION_MINOR 0)
set (CppPythonSocket_VERSION_PATCH 1)

# Default cmake build type is Release (faster)
if (NOT CMAKE_BUILD_TYPE)
    set (CMAKE_BUILD_TYPE Release)
endif (NOT CMAKE_BUILD_TYPE)

# Cpp standard
set (CMAKE_CXX_STANDARD 14) # c++ 14

# Building options (before configure files)
option (USE_OPENCV
        "Use image transferring capabilities (relies on OpenCV being installed)" ON)

# Message example
if (USE_OPENCV MATCHES ON)
  message(STATUS "#### using opencv")
else()
  message(STATUS "#### NOT using opencv")
endif()

      
# Pass some of the CMake settings
configure_file (
  "${PROJECT_SOURCE_DIR}/CppPythonSocketConfig.h.in"
  "${PROJECT_BINARY_DIR}/CppPythonSocketConfig.h"
)
include_directories ("${PROJECT_BINARY_DIR}")  # add binary dir to find CppPythonSocketConfig.h

# Append cpp_sockets library
# (the only one of the package in this case, but we could have more)
include_directories ("${PROJECT_SOURCE_DIR}/cpp_sockets/include")
add_subdirectory (cpp_sockets)

# Create executable unit test
add_executable (cpp_client_test cpp_client_test.cpp)
target_link_libraries (cpp_client_test cpp_sockets)


# add the install targets NOTE(oleguer): Not sure if this is necessary
set(include_dest "include/CppPythonSocket")
set(main_lib_dest "lib/CppPythonSocket")
install (TARGETS cpp_client_test DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/CppPythonSocketConfig.h" DESTINATION include)
install(FILES cpppythonsocket-config.cmake DESTINATION "${main_lib_dest}")
