#!/usr/bin/python
import socket

def receive_value(conn, buf_lentgh):
  buf = b''
  while buf_lentgh:
    newbuf = conn.recv(buf_lentgh)
    if not newbuf: return None
    buf += newbuf
    buf_lentgh -= len(newbuf)
  return buf.decode()


TCP_IP = '127.0.0.1'
TCP_PORT = 5001

# Start and connect to client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
print("Waiting for connection...")
conn, addr = s.accept()

# Receive message from client
length = receive_value(conn, 16)  # Get length of incomming message
message = receive_value(conn, int(length))  # Get message
print("Python server received: ")
print(message)

# Send message to client
answer = "answer"
answer_size = str(len(answer)).ljust(16).encode()
conn.sendall(answer_size)  # Send length of message (in known size, 16)
conn.sendall(answer.encode())  # Send message

s.close()