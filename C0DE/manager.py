import os

path = os.getcwd() + "/elecfiles/"

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
	votexiste = color.BOLD + color.RED + "Erro: " + color.END + "Ja existe uma votacao com o nome indicado"
	voteinexist = color.BOLD + color.RED + "Erro: " + color.END + "Nao existe uma votacao com o nome indicado"
	voteabrt = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja aberta"
	voteconc = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja concluido"
	voteinic = color.BOLD + color.RED + "Erro: " + color.END + "Votacao nao inicializada"
	votefec = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja fechada"



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
				info("espec", cmd[1], addr)
		elif cmd[0] == "info" and lengh > 2:
			server.sendMessage(errors.more, addr)


		#CRIA ELEICAO
		elif cmd[0] == "cria_votacao":
			if lengh == 2:
				if cmd[1] == "-help":
					server.sendMessage(helpText.criaeleicao, addr)
				else:
					criaVotacao(cmd[1], addr)
				
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
					fecha(cmd[1], addr)
			elif len== 1:
				server.sendMessage(errors.less, addr)
			elif len > 2:
				server.sendMessage(errors.more, addr)

		elif cmd[0] == "cleandir":
			server.fileHandler("clean&init")


		elif cmd[0] == "commands":
			if lengh == 1:
				server.sendMessage(helpText.comandos, addr)
			else:
				server.sendMessage(errors.more, addr)

		else:
			server.sendMessage(errors.unknwn, addr)

def ficheiroToList(nome):
	ret = open(path + nome, "r")
	#votacoes = votacoes.split()
	with open(path + nome) as f:
		content = f.readlines()
		f.close()
	ret = [x.strip() for x in content]
	return ret

def criaVotacao(nome, addr):
	import server
	votacoes = ficheiroToList("votacoes.txt")
	if not ((nome + " 0" in votacoes) or (nome + " 1" in votacoes) or (nome + " 2" in votacoes)):
		votacoes.append(nome)
		actualz = open(path + "votacoes.txt", "a")
		actualz.write(votacoes[len(votacoes)-1] + " 0" + "\n")
		actualz.close()
		novo = open(path + nome + ".txt", "w")
		novo.close()
		send = "Criada votacao com nome " + str(nome) 	
		server.sendMessage(send, addr)
	else:
		server.sendMessage(errors.votexiste, addr)

def votacaoNome(votacao):
	return str(votacao[0:len(votacao)-2])

def votacaoEstado(votacao):
	return str(votacao[-1])

def votacaoIndice(lista, votacao):
	for x in range(len(lista)):
		if votacaoNome(lista[x]) == str(votacao):
			return x
	return "erro"

def createInfo(vot):
	part = color.BOLD + votacaoNome(vot)+ color.END + "\n-"
	if votacaoEstado(vot) == "0":
		part += "Criada\n"
	elif votacaoEstado(vot) == "1":
		part += color.BOLD + color.YELLOW + "Aberta\n" + color.END
	elif votacaoEstado(vot) == "2":
		part += "Fechada\n"
	return part


def info(tipo, nome, addr):
	import server
	if str(tipo) == "all":
		send = "\n\n"
		lista = ficheiroToList("votacoes.txt")

		for x in range(len(lista)):
			send += createInfo(lista[x]) + "\n"
		server.sendMessage(send, addr)


	elif str(tipo) == "espec":
		
		lista = ficheiroToList("votacoes.txt")
		indice = votacaoIndice(lista, nome)
		if indice == "erro":
			return server.sendMessage(errors.voteinexist, addr)
		send = "\n\n\n"
		send += createInfo(lista[indice]) + "\n"
		server.sendMessage(send, addr)
	
def abre(nome, addr):
	import server
	lista = ficheiroToList("votacoes.txt")
	indice = votacaoIndice(lista, nome)
	if indice == "erro":
		return server.sendMessage(errors.voteinexist, addr)
	if votacaoEstado(lista[indice]) == "1":
		return server.sendMessage(errors.voteabrt, addr)
	if votacaoEstado(lista[indice]) == "2":
		return server.sendMessage(errors.voteconc, addr)

	lista[indice] = nome + " 1"
	f = open(path + "votacoes.txt", 'w')
	for x in range(len(lista)):
		f.write(lista[x] + "\n")
	f.close()
	
	send = "Votacao " + color.GREEN + color.BOLD + nome + color.END + " aberta"
	server.sendMessage(send, addr)

def fecha(nome, addr):
	import server
	lista = ficheiroToList("votacoes.txt")
	indice = votacaoIndice(lista, nome)
	if indice == "erro":
		return server.sendMessage(errors.voteinexist, addr)
	if votacaoEstado(lista[indice]) == "0":
		return server.sendMessage(errors.voteinic, addr)	
	if votacaoEstado(lista[indice]) == "2":
		return server.sendMessage(errors.votefec, addr)
	

	lista[indice] = nome + " 2"
	f = open(path + "votacoes.txt", 'w')
	for x in range(len(lista)):
		f.write(lista[x] + "\n")
	f.close()
	
	send = "Votacao " + color.GREEN + color.BOLD + nome + color.END + " fechada"
	server.sendMessage(send, addr)