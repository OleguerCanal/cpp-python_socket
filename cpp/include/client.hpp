#pragma once

#include <arpa/inet.h>
#include <cstring>
#include <iostream>
#include <string>
#include <sys/socket.h>
#include <unistd.h>

namespace socket_communication {
class Client {
 public:
  Client();
  Client(const std::string ip, const int port);
  ~Client();

  void Init(const std::string ip = "127.0.0.1", const int port = 5001);

  void Send(std::string message);

  std::string Receive();

 private:
  int client_;
  const int size_message_length_ = 16;  // Buffer size for the length
};
}  // namespace socket_communication