import socket
from time import gmtime, strftime

SERVER_PORT=0
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addrs   = {} # dict: nome -> endereco. Ex: addrs["user"]=('127.0.0.1',17234)
clients = {} # dict: endereco -> nome. Ex: clients[('127.0.0.1',17234)]="user"

def splashscreen():
	print(" /$$    /$$            /$$     /$$                            /$$$$$$       ")                                            
	print("| $$   | $$           | $$    |__/                           /$$__  $$")                        
	print("| $$   | $$ /$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$ ")
	print("|  $$ / $$//$$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$|  $$  /$$//$$__  $$ /$$__  $$")
	print(" \  $$ $$/| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$       \____  $$| $$$$$$$$| $$  \__/ \  $$/$$/| $$$$$$$$| $$  \__/")
	print("  \  $$$/ | $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$_____/| $$        \  $$$/ | $$_____/| $$      ")
	print("   \  $/  |  $$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$         \  $/  |  $$$$$$$| $$      ")
	print("    \_/    \______/    \___/  |__/|__/  |__/ \____  $$       \______/  \_______/|__/          \_/    \_______/|__/      ")
	print("                                             /$$  \ $$                                                                  ")
	print("                                            |  $$$$$$/                                                                  ")
	print("                                             \______/                                                                   ")
	print("Welcome to Online Voting System(C)\nAfonso Muralha * Joao Galamba * Nuno Miguel Macara\n")

def startup():
	SERVER_PORT = int(input("Input Port > "))
	try:
		server.bind(('',SERVER_PORT))
	except:
		raise Exception('Error Binding port')
		exit()
	print("\n")
	writeLOG("Server Started...\n")

def register_users(type, addr):
	
	if (type == "manager" or type == "comission") and type in clients:
		writeLOG("USER ALREADY LOGGED IN!!!")
		logerror = "ERROR_USERTAKEN"
		server.sendto(logerror.encode(),addr)

	else:	
		addrs[addr] = type
		clients[type] = addr
		logaccept = "LOGACCEPT"
		writeLOG("Registered " + str(addr) + " as " + str(type))
		server.sendto(logaccept.encode(),addr)

def checkSpecial(cmd, addr):
	if cmd[0] == "LOGFUNC" and len(cmd) == 2:
		register_users(cmd[1], addr)
def writeLOG(msg):
	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " -> " + msg)

splashscreen()
startup()

#MAIN CICLE
while (True):
	(msg,addr) = server.recvfrom(1024)
	cmd = msg.decode().split()
	checkSpecial(cmd, addr)
	




server.close()
writeLOG("Server Stopped...")


