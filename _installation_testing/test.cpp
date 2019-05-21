#include <iostream>
#include "client.hpp"
#include <unistd.h>

int main() {
    socket_communication::Client client("127.0.0.1", 5002);
    // Check that connection works
    client.Send("Hello hello!");
    std::string answer = client.Receive();
    std::cout << "[Server]: " << answer << std::endl;

    // Load image
    cv::Mat img = cv::imread("lena.png");
    while (true) {
        client.SendImage(img);
        std::string msg = client.Receive();
        std::cout << "[Server]: " << msg << std::endl << "Client: ";
        int a ;
        std::cin >> a;
        std::cout << std::endl;
    }
}