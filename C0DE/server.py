import atexit
import os
import socket
from manager import*
from voter import*
from comission import*
from time import gmtime, strftime
import shutil
from auxfuncs import*


path = str(os.getcwd()) + "/elecfiles/"




SERVER_PORT=0


 # dict: nome -> endereco. Ex: serverInfo.addrs["user"]=('127.0.0.1',17234)


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






def fileHandler(op):
	if op == "init":
		path = str(os.getcwd()) + "/elecfiles/"
		if not os.path.exists(path):
			os.makedirs(path)
		path += "votacoes.txt"
		if not os.path.exists(path):
			file = open(path,"w")
			file.close()
	if op =="clean&init":
		path = str(os.getcwd()) + "/elecfiles/"
		shutil.rmtree(path)
		fileHandler("init")

'''
def verifyFiles():
	if os.path.exists(path + "votacoes.txt"):
		file = open(path + "votacoes.txt", "r")
		votacoes = file.split()
		if len(votacoes) == 0:
			return False
		for x in range(len(votacoes)):
			if not (os.path.exists(path + str(votacoes[x]) + ".txt")):
				return False
		return True
	return True
'''


def startup():
	serverInfo.SERVER_PORT = int(input("Input Port > "))
	try:
		serverInfo.server.bind(('',serverInfo.SERVER_PORT))
	except:
		raise Exception('Error Binding port')
		exit()
	print("\n")
	writeLOG("Server Started...\n")

	'''
	if verifyFiles() == True:
		fileHandler("init")
	else:
		fileHandler("clean&init")
	
	'''
	fileHandler("init")#create txt folder





	

def register_users(type, addr):
	
	if (type == "manager" or type == "comission") and type in serverInfo.clients:
		writeLOG(color.RED + color.RED + "WARNING: " + color.END + str(addr[0]) + "Tried to login to an existent user")
		logerror = "ERROR_USERTAKEN"
		sendMessage(logerror, addr)
		#server.sendto(logerror.encode(),addr)

	else:	
		serverInfo.addrs[addr] = type
		serverInfo.clients[type] = addr
		logaccept = "LOGACCEPT"
		writeLOG("Registered " + str(addr) + " as " + color.BOLD + str(type) + color.END)
		sendMessage(logaccept, addr)
		#server.sendto(logaccept.encode(),addr)





def loginHandler(cmd, addr):
	if cmd[0] == "LOGFUNC" and len(cmd) == 2:
		register_users(cmd[1], addr)




	
def logoutHandler(cmd, addr):
	writeLOG("User " + color.BOLD + serverInfo.addrs[addr] + color.END + " with address " + color.BOLD + str(addr) + color.END +" has sucessfully logged out\n")
	del serverInfo.clients[serverInfo.addrs[addr]] 
	del serverInfo.addrs[addr]
	loginHandler(cmd, addr)






def writeLOG(msg):
	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " -> " + msg)




def verifyFiles():
	if os.path.exists(path + "votacoes.txt"):
		file = open(path + "votacoes.txt", "r")
		votacoes = file.split()
		for x in range(len(votacoes)):
			if not (os.path.exists(path + str(votacoes[x]) + ".txt")):
				return False
		return True





splashscreen()
startup()

#MAIN CICLE
while (True):
	(msg,addr) = serverInfo.server.recvfrom(1024)
	cmd = msg.decode().split()
	print(str(cmd))
	if len(cmd)>0:

		if cmd[0] == "killserver": #SO MANAGER PODERA FAZER ISTO!!!!!
			stopServer()			#AGORA INDEPENDENTE DO USER!!!
		
		if cmd[0] == "logout":
			logoutHandler(cmd, addr)

		if(addr not in serverInfo.addrs):
			loginHandler(cmd, addr)

		elif(serverInfo.addrs[addr] == "manager"):
			
			checkManager(cmd, addr)

		elif(serverInfo.addrs[addr] == "voter"):
			
			checkVoter()

		elif(serverInfo.addrs[addr] == "comission"):
			checkComission(cmd, addr)
			#checkManager(cmd, addr)
		


