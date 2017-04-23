import socket
import sys
import select
import auxfuncs



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


SERVER_IP   = '127.0.0.1'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
inputs = [sock, sys.stdin]

def splashscreen():
	print("---------------------------------------------------------------------------------\n\n")
	print("\n" + color.BOLD + color.CYAN)
	print(" /$$    /$$            /$$     /$$                            /$$$$$$  /$$ /$$                       /$$")
	print("| $$   | $$           | $$    |__/                           /$$__  $$| $$|__/                      | $$    ")
	print("| $$   | $$ /$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$       | $$  \__/| $$ /$$  /$$$$$$  /$$$$$$$  /$$$$$$  ")
	print("|  $$ / $$//$$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$      | $$      | $$| $$ /$$__  $$| $$__  $$|_  $$_/  ")
	print(" \  $$ $$/| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$      | $$      | $$| $$| $$$$$$$$| $$  \ $$  | $$    ")
	print("  \  $$$/ | $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$      | $$    $$| $$| $$| $$_____/| $$  | $$  | $$ /$$")
	print("   \  $/  |  $$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$      |  $$$$$$/| $$| $$|  $$$$$$$| $$  | $$  |  $$$$/") 
	print("    \_/    \______/    \___/  |__/|__/  |__/ \____  $$       \______/ |__/|__/ \_______/|__/  |__/   \___/  ")
	print("                                             /$$  \ $$                                                      ")
	print("                                            |  $$$$$$/                                                      ")
	print("                                             \______/                                                       " + color.END)
	print("\n" + color.YELLOW + "Welcome to Online Voting System(C)\nAfonso Muralha * Joao Galamba * Nuno Miguel Macara\n" + color.END)	
	print("\n\n---------------------------------------------------------------------------------\n\n")

def startup():

	splashscreen()
	global SERVER_PORT 
	SERVER_PORT= int(input("Input Port > "))
	print(color.GREEN + "Connected to server...\n\n" + color.END)

def loginHandler():
	while True:
		print("\n\n---------------------------------------------------------------------------------\n\n")
		print(color.BOLD + color.YELLOW + "Please input your login:" + color.END + "   (voter, manager or comission)\n")
		logintype = raw_input("")
		if(logintype == ("voter") or logintype == ("manager") or logintype == ("comission")):
			print(color.YELLOW + "\nLogging in...\n" + color.END)

			logmessage = "LOGFUNC " + logintype
			sock.sendto(logmessage.encode(),(SERVER_IP,SERVER_PORT))

			while True:
				ins, outs, exs = select.select(inputs,[],[])
				  
				for i in ins:
				  if i == sock:				  
				    (msg,addr) = sock.recvfrom(1024)
				    if msg == "ERROR_USERTAKEN":
				    	print(color.BOLD + color.RED + "User taken!" + color.END + " Please try again\n\n")
				    	print("---------------------------------------------------------------------------------\n\n")
				    	break
				    elif msg == "LOGACCEPT":
						print("\nRegistered as " + color.BOLD + color.YELLOW + logintype + color.END)
						print("\n\n---------------------------------------------------------------------------------\n\n")
						return
				break				
		else:
			print("User not recognised, please input again: (voter, manager or comission)")

def logoutHandler(addr):
	sendMessage("logout", addr)


def exitHandler():
	msg = "logout"
	sock.sendto(msg.encode(),(SERVER_IP,SERVER_PORT))
	sys.exit(color.GREEN + color.BOLD + "User logged out, and exited program, have a good day!\n" + color.END)






startup()
loginHandler()
print(color.BOLD + color.YELLOW + "Input message to server:" + color.END)

while True:
  ins, outs, exs = select.select(inputs,[],[])
  
  
  for i in ins:
    if i == sys.stdin:
      msg = sys.stdin.readline()
      sock.sendto(msg.encode(),(SERVER_IP,SERVER_PORT))
      if msg == "killserver\n":
      	sys.exit("Server Exited")
      if msg == "exit\n":
      	exitHandler()
      if msg == "logout\n":
      	loginHandler()
      	print(color.BOLD + color.YELLOW + "Input message to server:" + color.END)


    elif i == sock:
      (msg,addr) = sock.recvfrom(1024)
      print(color.BOLD + color.YELLOW + "\n\nMessage received from server: "+ color.END + msg.decode() + "\n\n")
      print("---------------------------------------------------------------------------------\n\n")
      print(color.BOLD + color.YELLOW + "Input message to server:" + color.END)


