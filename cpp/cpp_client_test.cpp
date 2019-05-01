#include <iostream>
#include "client.hpp"
#include <unistd.h>

int main() {
    socket_communication::Client client("127.0.0.1", 5002);
    // Check that connection works
    client.Send("Hello hello!");
    std::string answer = client.Receive();
    std::cout << "Server: " << answer << std::endl;

    // Load image
    cv::Mat img = cv::imread("cpp/lena.png");

    socket_communication::Timer timer;  // To check sending time
    timer.start();
    client.SendImage(img);
    std::string answer2 = client.Receive();
    timer.stop("Time to send image and get response");
    std::cout << "Server: " << answer2 << std::endl;
}