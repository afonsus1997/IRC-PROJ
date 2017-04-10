import socket
import sys
import select

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
SERVER_PORT=0
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
inputs = [sock, sys.stdin]

def splashscreen():
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


def startup():

	splashscreen()
	SERVER_PORT = int(input("Input Port > "))
	print("Connected to server...\n\n")

	while True:
		print("Please input your login:  (voter, manager or comission)\n")
		logintype = raw_input("")
		if(logintype == ("voter") or logintype == ("manager") or logintype == ("comission")):
			print("\nLogging in...\n")

			logmessage = "LOGFUNC " + logintype
			sock.sendto(logmessage.encode(),(SERVER_IP,SERVER_PORT))

			while True:
				ins, outs, exs = select.select(inputs,[],[])
				  
				for i in ins:
				  if i == sock:				  
				    (msg,addr) = sock.recvfrom(1024)
				    if msg == "ERROR_USERTAKEN":
				    	print("User taken! Please try again\n\n")
				    	break
				    elif msg == "LOGACCEPT":
						print("\nRegistered as " + color.BOLD + color.YELLOW + logintype + color.END + "\n")
						return
				break				
		else:
			print("User not recognised, please input again: (voter, manager or comission)")


print("----------------------------------------------\n\n")





startup()

print(color.BOLD + color.YELLOW + "Input message to server:" + color.END)

while True:
  ins, outs, exs = select.select(inputs,[],[])
  #select devolve para a lista ins quem esta a espera de ler
  
  for i in ins:
    # i == sys.stdin - alguem escreveu na consola, vamos ler e enviar
    if i == sys.stdin:
      # sys.stdin.readline() le da consola
      msg = sys.stdin.readline()
      # envia mensagem da consola para o servidor
      sock.sendto(msg.encode(),(SERVER_IP,SERVER_PORT))
    # i == sock - o servidor enviou uma mensagem para o socket
    elif i == sock:
      (msg,addr) = sock.recvfrom(1024)
      print("\n\nMessage received from server: " + msg.decode() + "\n")
      print("----------------------------------------------\n\n")
      print("Input message to server:")


server.close()
print("Server Stopped...")