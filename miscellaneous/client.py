import socket

HOST = "127.0.0.1"
PORT = 5053

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.sendall("Hello".encode())

reply = client.recv(1024).decode()
print("Server:", reply)

client.close()