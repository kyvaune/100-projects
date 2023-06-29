'''
This server cannot handle multiple connections at once!
'''

import socket

# host = socket.gethostbyname(socket.gethostname()) -- will not work w/ virtualbox

# declare HOST and PORT constants -- use 'ifconfig' to find ip address and select a non-reserved port
HOST = '127.0.0.1'
PORT = 8573

# declare server -- AF_NET = Internet Socket, SOCK_STREAM = TCP protocol (use SOCK_DGRAM for UDP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allows the server to listen for incoming connections on that specific IP address and port number
server.bind((HOST, PORT))

# to listen for incoming connections -- passing 5 (or any #) specifies how many unaccepted connections are allowed before rejecting new ones
server.listen(5)

# in an endless loop until server is terminated..
while True:
    
    # accept() returns a connection socket we can use to talk to that client and the address of the client
    # note: we do not use the server socket to talk to the client! the server socket is simply for accepting new connections
    communication_socket, address = server.accept()
    
    print(f"[Server]: Connected to {address}")

    # the client should send a message -- if not, we'll just wait indefinitely
    # we decode because when we send messages via sockets we encode them so that they are byte streams, rather than as strings 
    message = communication_socket.recv(1024).decode('utf-8') # instead of utf-8, can also use asci or anything else 
    
    print(f"[Server]: Message from client is {message}")
    
    # send an acknowledging message to the client
    communication_socket.send(f"[Server]: Got your message!".encode('utf-8'))
    
    # close the connect
    communication_socket.close()
    print(f"[Server]: Connection with {address} ended")
    
    