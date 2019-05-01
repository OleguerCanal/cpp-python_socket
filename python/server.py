#!/usr/bin/python
import numpy as np
import time
import socket

# Workaround fro ROS Kinetic issue importing cv
import sys
try:
  sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
  pass
import cv2

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

  def receive(self, decode=True):
    length = self.__receive_value(self.conn, self.__size_message_length)
    if length is not None:  # If None received, no new message to read
      message = self.__receive_value(self.conn, int(length), decode)  # Get message
      return message
    return None

  def receive_image(self):
    data = self.receive(False)
    if data is not None:
      data = np.fromstring(data, dtype='uint8')
      decimg = cv2.imdecode(data, 1)
      return decimg
    return None

  def __receive_value(self, conn, buf_lentgh, decode=True):
    buf = b''
    while buf_lentgh:
      newbuf = conn.recv(buf_lentgh)
      # if not newbuf: return None  # Comment this to make it non-blocking
      buf += newbuf
      buf_lentgh -= len(newbuf)
    if decode:
      return buf.decode()
    else:
      return buf

  def clear_buffer(self):
    try:
      while self.conn.recv(1024): pass
    except:
      pass
    return


if __name__ == "__main__":
  server = Server("127.0.0.1", 5002)
  message = server.receive()
  print(message)
  server.send("Shut up and send an image")

  image = server.receive_image()
  server.send("Okioki")
  cv2.imshow('SERVER', image)
  cv2.waitKey(1000)