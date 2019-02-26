import socket

# program for client
IP = "127.0.0.1"
PORT = 8087

while True:
    info = ''
    # the information that is going to be sent
    msg = str(input(">"))
    # we put it before the connect so we can give the opportunity to decide wether we want to connect or not.
    while len(msg) > 0:
        info = info + msg + '\n'
        msg = str(input(''))

    if len(info) == 0:
        info = '\n'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we create here the "telephone".

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    # Send the request message to the server in this case the info.
    s.send(str.encode(info))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
    # always close what you have started.
