import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind and listen
server.bind((HOST, PORT))
server.listen(1)

print(f"Server is listening on {HOST}:{PORT}")

conn, addr = server.accept()
print("Connected by:", addr)

message = conn.recv(1024).decode()
print("Client:", message)

conn.sendall("Hello".encode())

conn.close()
server.close()

print("Connection closed.")