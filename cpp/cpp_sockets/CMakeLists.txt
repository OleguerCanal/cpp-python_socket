# add OpenCV library?
# Building options (before configure files)
if (USE_OPENCV)
    find_package(OpenCV REQUIRED) # Transfer images (no need to be 3.3.1)
    set (EXTRA_LIBS ${EXTRA_LIBS} ${OpenCV_LIBS})
endif (USE_OPENCV)

include_directories (include)

# Create library
add_library(cpp_sockets
    src/client.cpp
    # src/server.cpp  # TODO(oleguer): Write the server
)
target_link_libraries(cpp_sockets ${EXTRA_LIBS})

# Library installation:
install (TARGETS cpp_sockets DESTINATION bin)
install (FILES include/client.hpp DESTINATION include)