import socket
from Seq import Seq


IP = "192.168.1.41"
PORT = 8081

while True:
	seq = input("Give me a ADN:")
	#PARA LA SEGUNDA PARTE PONER ESO EN EL SERVIDOR
	s1 = Seq(seq)
	s2 = s1.complement()
	s3 = s2.reverse()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#we create a socket so we are able to make the connection
	#between the client and the server.

	s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
	sequence1 = '\n'+'The complement is: '+ s2.strbase + '\n'
	sequence2 ='The reverse sequence is: '+ s3.strbase
	s.send(str.encode(sequence1) )
	s.send(str.encode(sequence2) )



# Receive data from the server
	msg = s.recv(2048).decode("utf-8")
	print("MESSAGE FROM THE SERVER:\n")
	print(msg)
	s.close()
