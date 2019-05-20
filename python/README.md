**IMPORTANT NOTE**: This is more an exercice for me to learn how to make installable packages than an actual useful package. It is not finished, so expect errors and a lot of missing stuff.

# cpp_python_socket
Simple TCP/IP socket comunication wrapper between c++ and Python for IPC.

## General Information
To install c++ package, read/edit source code and more info check out the repo:
https://github.com/OleguerCanal/cpp_python_socket.git

## Usage examples
Python Server:
```Python
from CppPythonSocket import Server
import cv2

if __name__ == "__main__":
  server = Server("127.0.0.1", 5002)

  # Check that connection works
  message = server.receive()
  print("[CLIENT]:" + message)
  server.send("Shut up and send an image")

  # Receive and show image
  image = server.receive_image()
  cv2.imshow('SERVER', image)
  cv2.waitKey(1000)
  server.send("Thanks!")
```

C++ client:
```cpp
#include <iostream>
#include "client.hpp"

int main() {
    socket_communication::Client client("127.0.0.1", 5002);

    // Check that connection works
    client.Send("Hello hello!");
    std::string answer = client.Receive();
    std::cout << "Server: " << answer << std::endl;

    // Load image and send image
    cv::Mat img = cv::imread("cpp/lena.png");
    client.SendImage(img);
    std::string answer2 = client.Receive();
    std::cout << "Server: " << answer2 << std::endl;
}
```
