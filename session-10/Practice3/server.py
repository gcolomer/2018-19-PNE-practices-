import socket
# import termcolor
from Seq import Seq

IP = "127.0.0.1"
PORT = 8087
MAX_OPEN_REQUESTS = 5
# number of users that can be connected at the same time

def okSequence(s):
    valid = 'AGCT'
    for letter in s:
        if letter not in valid:
            return False
    return True

def options(s1, comand):

    print("Working using the comand:", comand)
    if comand == "len":
        return s1.len()
    elif comand == "complement":
        return s1.complement().get_strbase()
    elif comand == "reverse":
        return s1.reverse().get_strbase()
    elif comand == "countA":
        return s1.count('A')
    elif comand == "countT":
        return s1.count('T')
    elif comand == "countG":
        return s1.count('G')
    elif comand == "countC":
        return s1.count('C')
    elif comand == "percA":
        return s1.perc("A")
    elif comand == "percT":
        return s1.perc("T")
    elif comand == "percG":
        return s1.perc("G")
    elif comand == "percC":
        return s1.perc("C")
    else:
        return"ERROR"
def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    # termcolor.cprint(msg, 'magenta')#using termcolor I decided to put it magenta!!!!

    if msg == '\n':
        response = 'Still connected'
        # here we know the program is still running
    else:
        trace = msg.split('\n')
        print("Validating", trace[0])
        if okSequence(trace[0]):
            response = 'OK\n'

            s1 = Seq(trace[0])
            for i in range(1, len(trace)-1):
                print("Validating command", i, trace[i])
                r = options(s1, trace[i])
                response = response + str(r) + '\n'

        else:
            response = 'ERROR'
    print('Request message: {}'.format(msg))
    cs.send(str.encode(response))

# MAIN PROGRAM
# the main program I used is provided by the teacher.

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