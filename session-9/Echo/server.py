import socket
import termcolor
import sys
#i have to import sys to run the sys.exit.

# Configure the Server's IP and PORT

IP = "127.0.0.1"
PORT = 8087
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    termcolor.cprint(msg, 'magenta')
    #here we will put the program to exit with a if loop.
    #if the mesage send is exit, the program will recognise we have to termiante.
    #Writing exit is like ending the connection with the client.
    #you end the connection so when you write you don't have any connection.
    if (msg == "EXIT"):
        sys.exit(0)

    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)