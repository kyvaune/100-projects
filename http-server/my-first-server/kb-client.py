import socket

# as a client, we are interested in the IP of the server we intend to connect to
# if attempting connection from a separate client in the LAN, this IP would differ from the one set in kb-server.py
# if attempting connection from a client outside of my LAN, specify the server's public IP address -- use myip.is website to find public IP
HOST = '127.0.0.1'
PORT = 8573

# declare socket -- AF_NET = Internet Socket, SOCK_STREAM = TCP protocol (use SOCK_DGRAM for UDP)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# since we are connecting rather than hosting (as seen in kb-server.py), call connect() rather than bind()
socket.connect((HOST, PORT))

# once we're connected...
socket.send(f"[Client]: Hey there! Send me what I requested!".encode('utf-8'))

# print the response received from server via the connection socket established on the server
print(socket.recv(1024).decode('utf-8'))