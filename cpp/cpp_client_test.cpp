#include <iostream>

#include "client.hpp"

int main() {
    // Client lient;
    Client client("127.0.0.1", 5001);
    client.Send("Hello hello!");
    std::string answer = client.Receive();
    std::cout << answer << std::endl;
}