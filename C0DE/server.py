import atexit
import socket
from manager import*
from voter import*
from comissioner import*
from time import gmtime, strftime



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


SERVER_PORT=0
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addrs   = {} # dict: endereco -> nome. Ex: clients[('127.0.0.1',17234)]="user"
clients = {} # dict: nome -> endereco. Ex: addrs["user"]=('127.0.0.1',17234)


def stopServer():

	server.close()
	writeLOG("Server Stopped...")


#atexit.register(stopServer)


def splashscreen():
	print(color.RED + color.BOLD + " /$$    /$$            /$$     /$$                            /$$$$$$       ")                                            
	print("| $$   | $$           | $$    |__/                           /$$__  $$")                        
	print("| $$   | $$ /$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$ ")
	print("|  $$ / $$//$$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$|  $$  /$$//$$__  $$ /$$__  $$")
	print(" \  $$ $$/| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$       \____  $$| $$$$$$$$| $$  \__/ \  $$/$$/| $$$$$$$$| $$  \__/")
	print("  \  $$$/ | $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$_____/| $$        \  $$$/ | $$_____/| $$      ")
	print("   \  $/  |  $$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$         \  $/  |  $$$$$$$| $$      ")
	print("    \_/    \______/    \___/  |__/|__/  |__/ \____  $$       \______/  \_______/|__/          \_/    \_______/|__/      ")
	print("                                             /$$  \ $$                                                                  ")
	print("                                            |  $$$$$$/                                                                  ")
	print("                                             \______/                                                                   "+ color.END)
	print(color.YELLOW+ "Welcome to Online Voting System(C)\nAfonso Muralha * Joao Galamba * Nuno Miguel Macara\n" + color.END)

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
		writeLOG(color.RED + color.RED + "WARNING: " + color.END + str(addr[0]) + "Tried to login to an existent user")
		logerror = "ERROR_USERTAKEN"
		server.sendto(logerror.encode(),addr)

	else:	
		addrs[addr] = type
		clients[type] = addr
		logaccept = "LOGACCEPT"
		writeLOG("Registered " + str(addr) + " as " + color.BOLD + str(type) + color.END)
		server.sendto(logaccept.encode(),addr)

def loginHandler(cmd, addr):
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

	if cmd[0] == "killserver": #SO MANAGER PODERA FAZER ISTO!!!!!
		stopServer()			#AGORA INDEPENDENTE DO USER!!!
	

	if(addr not in addrs):
		loginHandler(cmd, addr)

	elif(addrs[addr] == "manager"):
		print("OLHO MANAGEIRO")
		checkManager()

	elif(addrs[addr] == "voter"):
		print("OLHO VOTADEIRO")
		checkVoter()

	elif(addrs[addr] == "comissioner"):
		print("OLHO COMISSIONEIRO!")
		checkComission()
	


