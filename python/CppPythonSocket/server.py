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
  If automatic_port == True, will iterate over port until find a free one
  """
  def __init__(self, ip, port, automatic_port=True):
    self.__size_message_length = 16  # Buffer size for the length
    max_connections_attempts = 5

    # Start and connect to client
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if automatic_port:
      connected = False
      while (not connected) and (max_connections_attempts > 0):
        try:
          self.s.bind((ip, port))
          connected = True
        except:
          print("[Server]: Port", port, "already in use. Binding to port:", port+1)
          port += 1
          max_connections_attempts -= 1
      if not connected:
        print("[Server]: Error binding to adress!")
    else:
      self.s.bind((ip, port))

    self.s.listen(True)
    print("[Server]: Waiting for connection...")
    self.conn, addr = self.s.accept()
    print("[Server]: Connected")

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
