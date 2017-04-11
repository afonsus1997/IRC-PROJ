
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

class helpText:
	info = "info de info incpeption"
	criaeleicao = "help de criaeleicao"
	abre = "help abre"
	fecha = "help fecha"
	commands = "help comands"

class errors:
	more = color.BOLD + color.RED + "Erro: " + color.END + "Demasiados argumentos!\nUse o unico argumento -help para mais informacoes"
	less = color.BOLD + color.RED + "Erro: " + color.END + "Faltam argumentos!\nUse o unico argumento -help para mais informacoes"
	unknwn = color.BOLD + color.RED + "Erro: " + color.END + "Comando deconhecido\nUse o comando commands para listar todos os comandos possiveis"



def checkManager(cmd, addr):
	import server	
	send = ""
	server.sendMessage(send, addr)

	lengh = len(cmd)

	if lengh>=1:


		#INFO
		if cmd[0] == "info" and lengh == 1:
			info("all", 0, addr)
		elif cmd[0] == "info" and lengh == 2: 
			if cmd[1] == "-help":
				server.sendMessage(helpText.info, addr)
			else:	
				info("esp", cmd[1], addr)
		elif cmd[0] == "info" and lengh > 2:
			server.sendMessage(errors.more, addr)


		#CRIA ELEICAO
		elif cmd[0] == "cria_eleicao":
			if lengh == 2:
				if cmd[1] == "-help":
					server.sendMessage(helpText.criaeleicao, addr)
				else:
					criaEleicao(cmd[1], addr)
				
			elif lengh == 1:
				server.sendMessage(errors.less, addr)
			else:
				server.sendMessage(errors.more, addr)


		elif cmd[0] == "abre":
			if lengh == 2:
				if cmd[1] == "-help":
					server.sendMessage(helpText.abre, addr)
				else:
					abre(cmd[1], addr)
			elif len== 1:
				
				server.sendMessage(errors.less, addr)
			elif len > 2:
				server.sendMessage(errors.more, addr)


		elif cmd[0] == "fecha":
			if lengh == 2:
				if cmd[1] == "-help":
					server.sendMessage(helpText.fecha, addr)
				else:
					fecha([1], addr)
			elif len== 1:
				server.sendMessage(errors.less, addr)
			elif len > 2:
				server.sendMessage(errors.more, addr)


		elif cmd[0] == "commands":
			if lengh == 1:
				server.sendMessage(helpText.comandos, addr)
			else:
				server.sendMessage(errors.more, addr)

		else:
			server.sendMessage(errors.unknwn, addr)

def criaEleicao(nome, addr):
	import server
	send = "Cria votacao com nome " + str(nome) 
	server.sendMessage(send, addr)

def info(tipo, nome, addr):
	import server
	if str(tipo) == "all":
		send = "todas as infos!"
		server.sendMessage(send, addr)
	elif str(tipo) == "espec":
		send = "info da vot " + str(nome)
		server.sendMessage(send, addr)
	
def abre(nome, addr):
	import server
	send = "Abre votacao com nome " + str(nome)
	server.sendMessage(send, addr)

def fecha(nome, addr):
	import server
	send = "Fecha votacao com nome " + str(nome)
	server.sendMessage(send, addr)
