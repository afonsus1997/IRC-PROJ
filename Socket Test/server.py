import socket

# Recebe no porto SERVER PORT os comandos "IAM <nome>", "HELLO",
#    "HELLOTO <nome>" ou "KILLSERVER" 
# "IAM <nome>" - regista um cliente como <nome>
# "HELLO" - responde HELLO ou HELLO <nome> se o cliente estiver registado
# "HELLOTO <nome>" - envia HELLO para o cliente <nome>
# "KILLSERVER" - mata o servidor

#INICIALIZACAO

SERVER_PORT=12007
SERVER_PORT = int(input("Input Port > "))

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('',SERVER_PORT))
print("Server Started...\n")
addrs   = {} # dict: nome -> endereco. Ex: addrs["user"]=('127.0.0.1',17234)
clients = {} # dict: endereco -> nome. Ex: clients[('127.0.0.1',17234)]="user"


#FUNCOES DE CADA OPERACAO

def register_client(name,addr):
  # se o nome nao existe e o endereco nao esta a ser usado
  if not name in addrs and not addr in clients:
    addrs[name] = addr
    clients[addr] = name

def respond_hello(addr):
  respond_msg = "HELLO"
  if addr in clients: #se addr estiver no dicinario clients, o utilizador existe
    respond_msg += " " + clients[addr]
  respond_msg += "\n"
  server.sendto(respond_msg.encode(),addr)

def forward_hello(name):
  if name in addrs: #novamente, se estiver no dicionario o utilizador existe
    respond_msg = "HELLO " + name + "\n" 
    addr = addrs[name]
    server.sendto(respond_msg.encode(),addr)

def respond_error(addr):
  respond_msg = "INVALID MESSAGE\n"
  server.sendto(respond_msg.encode(),addr)

#CORPO PRINCIPAL

def echo(msg):
  server.sendto(msg.encode(),addr)
  

infomessage = "INFO MESSAGE"
statusmessage = "STATUS MESSAGE"






while True:
  (msg,addr) = server.recvfrom(1024)
  cmds = msg.decode().split()
  if(cmds[0]=="IAM"):
    register_client(cmds[1],addr)
    registerOutput = str("Registered " + str(cmds[1]) + " with address " + str(addr) + "\n") 
    print(registerOutput)


  elif(cmds[0]=="HELLO"):
    respond_hello(addr)


  elif(cmds[0]=="HELLOTO"):
    forward_hello(cmds[1])

  elif(cmds[0] == "status"):
    if (len(cmds)>1 and cmds[1] == "-help"):
      echo("infomessage")
    else:
      echo(statusmessage)
  

  elif(cmds[0]=="KILLSERVER"):
    println("Killing Server");
    echo("Killing Server")
    break
  else:
    respond_error(addr)
  
  

server.close()
