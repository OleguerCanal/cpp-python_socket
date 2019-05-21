from python.CppPythonSocket.server import Server
import cv2

if __name__ == "__main__":
  server = Server("127.0.0.1", 5002)
  message = server.receive()
  print("[Client]:", message)
  server.send("Shut up and send an image")

  while True:
    img = server.receive_image()
    print("[Client]: Sent image of size: " + str(img.size))
    cv2.imshow("image at server", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    a = raw_input("Server: ")
    server.send(str(a))