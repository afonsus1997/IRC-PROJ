import os
from auxfuncs import*

path = os.getcwd() + "/elecfiles/"






def checkManager(cmd, addr):
	import server	
	send = ""
	sendMessage(send, addr)

	lengh = len(cmd)

	if lengh>=1:


		#INFO
		if cmd[0] == "info" and lengh == 1:
			info("all", 0, addr)
		elif cmd[0] == "info" and lengh == 2: 
			if cmd[1] == "-help":
				sendMessage(helpTextManager.info, addr)
			else:	
				info("espec", cmd[1], addr)
		elif cmd[0] == "info" and lengh > 2:
			sendMessage(errorsManager.more, addr)


		#CRIA ELEICAO
		elif cmd[0] == "cria_votacao":
			if lengh == 2:
				if cmd[1] == "-help":
					sendMessage(helpTextManager.criaeleicao, addr)
				else:
					criaVotacao(cmd[1], addr)
				
			elif lengh == 1:
				sendMessage(errorsManager.less, addr)
			else:
				sendMessage(errorsManager.more, addr)


		elif cmd[0] == "abre":
			if lengh == 2:
				if cmd[1] == "-help":
					sendMessage(helpTextManager.abre, addr)
				else:
					abre(cmd[1], addr)
			elif len== 1:
				
				sendMessage(errorsManager.less, addr)
			elif len > 2:
				sendMessage(errorsManager.more, addr)


		elif cmd[0] == "fecha":
			if lengh == 2:
				if cmd[1] == "-help":
					sendMessage(helpTextManager.fecha, addr)
				else:
					fecha(cmd[1], addr)
			elif len== 1:
				sendMessage(errorsManager.less, addr)
			elif len > 2:
				sendMessage(errorsManager.more, addr)

		elif cmd[0] == "cleandir":
			if lengh == 1:
				server.fileHandler("clean&init")
				sendMessage(color.RED + color.BOLD + "\n\nDirectory Cleaned!\n\n" + color.END, addr)
			if lengh == 2:
				if cmd[1] == "-help":
					sendMessage(helpText.cleandir, addr)
				else:
					sendMessage(errorsManager.errogen, addr)


		elif cmd[0] == "commands":
			if lengh == 1:
				sendMessage(helpTextManager.comandos, addr)
			else:
				sendMessage(errorsManager.more, addr)

		else:
			sendMessage(errorsManager.unknwn, addr)



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
		sendMessage(send, addr)
	else:
		sendMessage(errorsManager.votexiste, addr)

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
		sendMessage(send, addr)


	elif str(tipo) == "espec":
		
		lista = ficheiroToList("votacoes.txt")
		indice = votacaoIndice(lista, nome)
		if indice == "erro":
			return sendMessage(errorsManager.voteinexist, addr)
		send = "\n\n\n"
		send += createInfo(lista[indice]) + "\n"
		sendMessage(send, addr)
	
def abre(nome, addr):
	import server
	lista = ficheiroToList("votacoes.txt")
	indice = votacaoIndice(lista, nome)
	if indice == "erro":
		return sendMessage(errorsManager.voteinexist, addr)
	if votacaoEstado(lista[indice]) == "1":
		return sendMessage(errorsManager.voteabrt, addr)
	if votacaoEstado(lista[indice]) == "2":
		return sendMessage(errorsManager.voteconc, addr)

	lista[indice] = nome + " 1"
	f = open(path + "votacoes.txt", 'w')
	for x in range(len(lista)):
		f.write(lista[x] + "\n")
	f.close()
	
	send = "Votacao " + color.GREEN + color.BOLD + nome + color.END + " aberta"
	sendMessage(send, addr)

def fecha(nome, addr):
	import server
	lista = ficheiroToList("votacoes.txt")
	indice = votacaoIndice(lista, nome)
	if indice == "erro":
		return sendMessage(errorsManager.voteinexist, addr)
	if votacaoEstado(lista[indice]) == "0":
		return sendMessage(errorsManager.voteinic, addr)	
	if votacaoEstado(lista[indice]) == "2":
		return sendMessage(errorsManager.votefec, addr)
	

	lista[indice] = nome + " 2"
	f = open(path + "votacoes.txt", 'w')
	for x in range(len(lista)):
		f.write(lista[x] + "\n")
	f.close()
	
	send = "Votacao " + color.GREEN + color.BOLD + nome + color.END + " fechada"
	sendMessage(send, addr)