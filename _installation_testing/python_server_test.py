#!/usr/bin/python
from CppPythonSocket import Server
import cv2

if __name__=="__main__":
    print("Hi")
    server = Server("127.0.0.1", 5002)
    message = server.receive()
    print("[Client]:", message)
    server.send("Shut up and send an image")