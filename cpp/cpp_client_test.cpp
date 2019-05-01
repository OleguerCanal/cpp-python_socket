#include <iostream>
#include "client.hpp"

int main() {
    socket_communication::Client client("127.0.0.1", 5001);
    client.Send("Hello hello!");
    std::string answer = client.Receive();
    std::cout << "[SERVER]: " << answer << std::endl;
}