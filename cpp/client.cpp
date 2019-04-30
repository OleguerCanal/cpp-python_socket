#include <iostream>
#include <cstring>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	char * ip = "127.0.0.1";
	int portnum = 5001;

	int client;
	client = socket(AF_INET, SOCK_STREAM, 0);
	if (client < 0) {
		std::cout << "ERROR establishing socket\n" << std::endl;
		exit(1);
	}

	struct sockaddr_in serv_addr;
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(portnum);
	inet_pton(AF_INET, ip, &serv_addr.sin_addr);
	std::cout << "\n--> Socket client created...\n";

	if (
    connect(client, (const struct sockaddr*)&serv_addr, sizeof(serv_addr)) == 0)
      std::cout << "Cpp Client Connected" << std::endl; 

  // Send message to server
  std::string length = "0000000000000002";  // Send length in known length (16)
  send(client, length.c_str(), 16, 0);
  std::string msg = "ok";  // Then send message of size lentgh
  send(client, msg.c_str(), 2, 0);

  // Receive message form server
  char message_length[16] = {0};
  int n = recv(client, message_length, 16, 0);
	std::cout << message_length << std::endl;
	int length_int = std::stoi(message_length);
  char message[length_int] = {0};
  n = recv(client, message, length_int, 0);
	std::cout << message << std::endl;

	close(client);
	std::cout << "\nDisconnected..." << std::endl;
	return 0;
}
