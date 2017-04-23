import os
from auxfuncs import*

path = os.getcwd() + "/elecfiles/"




def checkComission(cmd, addr):

	lengh = len(cmd)

	if lengh == 1:
		if cmd[0] == "commands":
			return sendMessage(helpTextComission.comandos, addr)
		
		elif cmd[0] == "adiciona_candidato" or cmd[0] == "info":
			return sendMessage(errorsComission.less, addr)
		else:
			return sendMessage(errorsComission.unknwn, addr)

	elif lengh == 0:
		return sendMessage(errorsComission.less, addr)

	elif lengh == 2:
	
		if cmd[0] == "info" and cmd[1] == "-help":
			return sendMessage(helpTextComission.info, addr)
		if cmd[0] == "adiciona_candidato" and cmd[1] == "-help":
			return sendMessage(helpTextComission.adicionacandidato, addr)
		if cmd[0] == "adiciona_candidato":
			return sendMessage(errorsComission.less, addr)			
		if cmd[0] == "info":
			info(cmd[1], addr)
		else:	
			return sendMessage(errorsComission.unknwn, addr)

	elif lengh == 3:
		if cmd[0] == "adiciona_candidato":
			return adicionaCandidato(cmd[2], cmd[1], addr)
		else:
			return sendMessage(errorsComission.unknwn, addr)	

	elif lengh >3 and cmd[0] == "adiciona_candidato":
		sendMessage(errorsComission.more, addr)	

	else:
		return sendMessage(errorsComission.unknwn, addr)




def info(nome, addr):

	send = "\n\n"
	lista_elei = ficheiroToList("votacoes.txt")
	send += "Existem os seguintes candidatos para a votacao " + str(nome) + ":\n"
	if nome + " 0" in lista_elei or nome + " 1" in lista_elei or nome + " 2" in lista_elei:	
		lista_cand = ficheiroToList(nome +".candidates")
		for x in range(len(lista_cand)):
			send += "-" + lista_cand[x] + "\n"
		
		sendMessage(send, addr)
	else:
		sendMessage(errorsComission.votacaoinexist, addr)
		


def ficheiroToList(nome):
	
	ret = open(path + nome, "r")
	with open(path + nome) as f:
		content = f.readlines()
		f.close()
	ret = [x.strip() for x in content]
	return ret


def votacaoNome(votacao):
	return str(votacao[0:len(votacao)-2])

def votacaoEstado(votacao):
	return str(votacao[-1])

def votacaoIndice(lista, votacao):
	for x in range(len(lista)):
		if votacaoNome(lista[x]) == str(votacao):
			return x
	return "erro"





def adicionaCandidato(nome, votacao, addr):
	existe_candidato = False
	if not os.path.exists(path + "votacoes.txt"):
		return sendMessage(errorsComission.corr, addr)
	lista_elei = ficheiroToList("votacoes.txt")
	if not os.path.exists(path + votacao + ".candidates"):
		return sendMessage(errorsComission.votacaoinexist, addr)
	lista_cand = ficheiroToList(votacao + ".candidates")
	if votacao + " 0" in lista_elei or votacao + " 1" in lista_elei or votacao + " 2" in lista_elei:
		if votacao + " 0" in lista_elei:
			if nome in lista_cand:
				return sendMessage(errorsComission.candidatoexis, addr)#erro ja existe
			else:
				if len(lista_cand) == 0:
					lista_cand = [str(nome)]
				else:
					lista_cand.append(nome)

		else:
			return sendMessage(errorsComission.timeover, addr)
			

	else:
		return sendMessage(errorsComission.votacaoinexist, addr)
		
	
	f = open(path + votacao + ".candidates", 'w')
	for x in range(len(lista_cand)):
		f.write(lista_cand[x]+"\n")
	f.close()

	f=open(path + votacao + ".votes", 'a')
	f.write(nome + " 0" + "\n")
	f.close()

	send = "Foi adicionado o candidato " + nome + " a votacao " + votacao
	return sendMessage(send, addr)