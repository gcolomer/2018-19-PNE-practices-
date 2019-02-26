import socket
from Seq import Seq

IP = "192.168.1.41"
PORT = 8081

while True:
    seq = input("Give me a ADN:")
    # PARA LA SEGUNDA PARTE PONER ESO EN EL SERVIDOR

    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)  # we create a socket so we are able to make the connection
    # between the client and the server.

    s.connect((IP, PORT))

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes


    # Receive data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)
    s.close()
