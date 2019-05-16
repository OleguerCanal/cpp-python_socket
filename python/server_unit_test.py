from server import Server

if __name__ == "__main__":
  server = Server("127.0.0.1", 5002, automatic_port=True)
  message = server.receive()
  print("[Client]:", message)
  server.send("Shut up and send an image")

  while True:
    img = server.receive_image()
    print("[Client]: Sent image of size: " + str(img.size))
    a = raw_input("Server: ")
    server.send(str(a))