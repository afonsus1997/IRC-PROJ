import socket
import sys
import select

SERVER_PORT = 12000
SERVER_PORT=12007
SERVER_PORT = int(input("Input Port > "))
SERVER_IP   = '127.0.0.1'
print("\n")

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# o select quer ficar a espera de ler o socket e ler do stdin (consola)
inputs = [sock, sys.stdin]
print("Connected to server...\n")
print("----------------------------------------------\n\n")

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

    



