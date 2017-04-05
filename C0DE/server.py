import socket

SERVER_PORT=0
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

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
	print("\nServer Started...\n")


splashscreen()
startup()
server.close()
print("Server Stopped...")


