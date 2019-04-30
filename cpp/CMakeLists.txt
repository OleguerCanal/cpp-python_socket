include_directories(include)

add_library(cpp_sockets
    src/client.cpp
# server.cpp
)
# target_link_libraries( cpp_sockets ${OpenCV_LIBS})  # If image sending capabilities

add_executable(cpp_client_test cpp_client_test.cpp)
target_link_libraries(cpp_client_test cpp_sockets)