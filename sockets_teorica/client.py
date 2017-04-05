import socket

msg = input("Message: ")
ServerIP="194.210.221.83"

while(true):
	ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ClientSock.sendto(msg, (ServerIP, 5005))
	print("Message to server: " + msg)
	(ServerMsg (ServerIP, 5005)) = ClientSock.recvform (100)
	print("Message from server: " + ServerMsg)
ClientSock.close()
