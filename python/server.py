#!/usr/bin/python
import socket

class Server():
  """TCP IP communication server
  """
  def __init__(self, ip, port):
    self.__size_message_length = 16  # Buffer size for the length

    # Start and connect to client
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((ip, port))
    self.s.listen(True)
    print("Waiting for connection...")
    self.conn, addr = self.s.accept()
    print("Connected")

  def __del__(self):
    self.s.close()

  def send(self, message):
    message_size = str(len(message)).ljust(self.__size_message_length).encode()
    self.conn.sendall(message_size)  # Send length of msg (in known size, 16)
    self.conn.sendall(message.encode())  # Send message

  def receive(self):
    length = self.__receive_value(self.conn, self.__size_message_length)
    message = self.__receive_value(self.conn, int(length))  # Get message
    return message

  def __receive_value(self, conn, buf_lentgh):
    buf = b''
    while buf_lentgh:
      newbuf = conn.recv(buf_lentgh)
      if not newbuf: return None
      buf += newbuf
      buf_lentgh -= len(newbuf)
    return buf.decode()


if __name__ == "__main__":
  server = Server("127.0.0.1", 5001)
  message = server.receive()
  print("[CLIENT]:" + message)
  server.send("Shut up")