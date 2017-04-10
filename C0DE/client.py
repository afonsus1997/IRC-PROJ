import socket
import sys
import select


SERVER_IP   = '127.0.0.1'
SERVER_PORT=0
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
inputs = [sock, sys.stdin]

def splashscreen():
	print("\n")
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
	print("                                             \______/                                                       ")
	print("\nWelcome to Online Voting System(C)\nAfonso Muralha * Joao Galamba * Nuno Miguel Macara\n")	


def startup():

	splashscreen()
	print("Connected to server...\n")
print("----------------------------------------------\n\n")





startup()

print("Input message to server:")

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