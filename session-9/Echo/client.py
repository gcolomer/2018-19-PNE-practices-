import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8087



while True:
    msg = input(">") #we put it before the connect so we can give the opportunity to decide wether we want to connect or not.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!


    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()