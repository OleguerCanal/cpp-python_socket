#include "client.hpp"
#include <unistd.h>

namespace socket_communication {
Client::Client() {}
Client::Client(const std::string ip, int port) { Init(ip, port); }
Client::~Client() { close(client_); }

void Client::Init(const std::string ip, int port) {
  client_ = socket(AF_INET, SOCK_STREAM, 0);
  if (client_ < 0) {
    std::cout << "[Client]: ERROR establishing socket\n" << std::endl;
    exit(1);
  }

  bool connected = false;
  int connection_attempts = 5;

  while ((!connected) && (connection_attempts > 0)) {
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip.c_str(), &serv_addr.sin_addr);

    if (connect(client_, (const struct sockaddr*)&serv_addr,
                sizeof(serv_addr)) == 0) {
      connected = true;
      std::cout << "[Client]: Cpp socket client connected." << std::endl;
    } else {
      port += 1;
      connection_attempts -= 1;
      std::cout << "[Client]: Error connecting to port " << port - 1
                << ". Attepting to connect to port: " << port << std::endl;
    }
  }
}

void Client::Send(std::string message) {
  // Send length of the message
  int length = message.length();
  std::string length_str = std::to_string(length);
  std::string message_length =
      std::string(size_message_length_ - length_str.length(), '0') + length_str;
  send(client_, message_length.c_str(), size_message_length_, 0);

  // Send message
  send(client_, message.c_str(), length, 0);
}

std::string Client::Receive() {
  // TODO(oleguer): try catch, if connection dropped print notification and try
  // to reconnect

  // Receive length of the message
  char message_length[size_message_length_] = {0};
  int n = recv(client_, message_length, size_message_length_, 0);
  std::string message_length_string(message_length);
  int length = std::stoi(message_length_string);
  // if (length == 0) return "";

  // receive message
  char message[length] = {0};
  n = recv(client_, message, length, 0);
  return message;
}

#ifdef USE_OPENCV
void Client::SendImage(cv::Mat img) {
  int pixel_number = img.rows * img.cols / 2;

  std::vector<uchar> buf(pixel_number);
  cv::imencode(".jpg", img, buf);

  int length = buf.size();
  std::string length_str = std::to_string(length);
  std::string message_length =
      std::string(size_message_length_ - length_str.length(), '0') + length_str;

  send(client_, message_length.c_str(), size_message_length_, 0);
  send(client_, buf.data(), length, 0);
}
#endif

}  // namespace socket_communication