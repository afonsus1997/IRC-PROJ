import os
from auxfuncs import*

path = os.getcwd() + "/elecfiles/"






def checkManager(cmd, addr):
	
	lengh = len(cmd)

	if cmd == []:
		return sendMessage(errorsManager.unknwn, addr)	

	if lengh>=1:


		#INFO
		if cmd[0] == "info" and lengh == 1:
			info("all", 0, addr)
		elif cmd[0] == "info" and lengh == 2: 
			if cmd[1] == "-help":
				return sendMessage(helpTextManager.info, addr)
			else:	
				info("espec", cmd[1], addr)
		elif cmd[0] == "info" and lengh > 2:
			return sendMessage(errorsManager.more, addr)


		#CRIA ELEICAO
		elif cmd[0] == "cria_votacao":
			if lengh == 2:
				if cmd[1] == "-help":
					return sendMessage(helpTextManager.criaeleicao, addr)
				else:
					criaVotacao(cmd[1], addr)
				
			elif lengh == 1:
				return sendMessage(errorsManager.less, addr)
			else:
				return sendMessage(errorsManager.more, addr)


		elif cmd[0] == "abre":
			if lengh == 2:
				if cmd[1] == "-help":
					return sendMessage(helpTextManager.abre, addr)
				else:
					abre(cmd[1], addr)
			elif lengh < 2:
				return sendMessage(errorsManager.less, addr)
			elif lengh > 2:
				return sendMessage(errorsManager.more, addr)
			

		elif cmd[0] == "fecha":
			if lengh == 2:
				if cmd[1] == "-help":
					return sendMessage(helpTextManager.fecha, addr)
				else:
					fecha(cmd[1], addr)
			elif lengh== 1:
				return sendMessage(errorsManager.less, addr)
			elif lengh > 2:
				return sendMessage(errorsManager.more, addr)

		elif cmd[0] == "cleandir":
			if lengh == 1:
				fileHandler("clean&init")
				return sendMessage(color.RED + color.BOLD + "\n\nDirectory Cleaned!" + color.END, addr)
			if lengh == 2:
				if cmd[1] == "-help":
					return sendMessage(helpTextManager.cleandir, addr)
				else:
					return sendMessage(errorsManager.errogen, addr)


		elif cmd[0] == "commands":
			if lengh == 1:
				return sendMessage(helpTextManager.comandos, addr)
			else:
				return sendMessage(errorsManager.more, addr)

		else:
			return sendMessage(errorsManager.unknwn, addr)
	else:
		return sendMessage(errorsManager.unknwn, addr)



def criaVotacao(nome, addr):
	votacoes = ficheiroToList("votacoes.txt")
	if not ((nome + " 0" in votacoes) or (nome + " 1" in votacoes) or (nome + " 2" in votacoes)):
		votacoes.append(nome)
		actualz = open(path + "votacoes.txt", "a")
		actualz.write(votacoes[len(votacoes)-1] + " 0" + "\n")
		actualz.close()
		novo = open(path + nome + ".candidates", "w")
		novo.close()
		votos = open(path + nome + ".votes", "w")
		votos.close()
		cc = open(path + nome + ".cc", "w")
		cc.close()
		send = "Criada votacao com nome " + str(nome) 	
		sendMessage(send, addr)
	else:
		sendMessage(errorsManager.votexiste, addr)


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
	if str(tipo) == "all":
		send = "\n\n"
		lista = ficheiroToList("votacoes.txt")

		for x in range(len(lista)):
			send += createInfo(lista[x]) 
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

	
	lista = ficheiroToList(nome + ".votes")
	for x in range(len(lista)):
		lista[x] = lista[x].split()
	candidatoNome = []
	numeroVotos = []
	for x in range(len(lista)):
		candidatoNome.append(lista[x][0]) 
		numeroVotos.append(int(lista[x][1]))
	valorvencedor = max(numeroVotos)
	indicevencedor = [i for i, x in enumerate(numeroVotos) if x == valorvencedor]
	if len(indicevencedor) == 1:
		vencedor = candidatoNome[indicevencedor[0]]
		text = "Ganhou " + vencedor + " com " + str(valorvencedor) + " votos"
	elif len(indicevencedor) == 2:
		text = "Empate entre " + candidatoNome[indicevencedor[0]] + " e " + candidatoNome[indicevencedor[1]] + " com " + str(valorvencedor) + " votos"
		
	else:
		text = "Empate entre "
		for x in range(len(indicevencedor)-1):
			text += candidatoNome[indicevencedor[x]] + ", "
		text = text[:-2]
		text += " e " + candidatoNome[indicevencedor[-1]] + " com " + str(valorvencedor) + " votos"

	file = open(path + nome + ".votes", "a")
	file.write(text)

	
	
	send = "Votacao " + color.GREEN + color.BOLD + nome + color.END + " fechada\n" + text
	sendMessage(send, addr)