# Python3.7+

# import necessary modules
import socket

# set the host and port to bind the server
HOST, PORT = '', 8888

# create a socket object, set some options, and bind it to the host and port
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))

# start listening for incoming connections:
listen_socket.listen(1)

# print a message indicating that the server is running 
print(f'Serving HTTP on port {PORT} ...') # http://localhost:8888/hello

# enter a loop to continuously accept connections
while True:
    
    # accept a client connection and get the client socket and address
    client_connection, client_address = listen_socket.accept()
    
    # receive the request data (up to 1024 bytes) from the client
    request_data = client_connection.recv(1024)
    
    # print the received request data as a UTF-8 decoded string
    print(request_data.decode('utf-8'))

    # prepare the http response message
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # send the response message back to the client
    client_connection.sendall(http_response)
    
    # close the client connection
    client_connection.close()
    
# use telnet localhost 8888 to fire up a telnet session, specifying a host to connect to "localhost" 
#   and the port to connect to "8888"
#     then, use $ GET /hello HTTP/1.1 -- <HTTP method> <path> <HTTP version>
#       to receive response $ HTTP/1.1 200 OK \n Hello, World! -- <HTTP version> <HTTP status code> \n <HTTP response body>

    """
    To sum it up: The Web server creates a listening socket and starts accepting new connections in a loop. 
    The client initiates a TCP connection and, after successfully establishing it, the client sends an HTTP request to the server 
    and the server responds with an HTTP response that gets displayed to the user. 
    To establish a TCP connection both clients and servers use sockets.
    """