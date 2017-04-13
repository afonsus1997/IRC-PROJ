import os
from auxfuncs import*

path = os.getcwd() + "/elecfiles/"

'''
info - X

candidatos - X

adicionar - X

outro - X

'''







def checkComission(cmd, addr):

	lengh = len(cmd)

	if lengh == 1:
		if cmd[0] == "commands":
			return sendMessage(helpTextComission.comandos, addr)
		

		else:
			return sendMessage(errorsComission.unknwn, addr)

	elif lengh == 0:
		return sendMessage(errorsComission.less, addr)

	elif lengh == 2:
		print("entrei\n")
		if cmd[0] == "info" and cmd[1] == "-help":
			return sendMessage(helpTextComission.info, addr)
		if cmd[0] == "adiciona_candidato" and cmd[1] == "-help":
			return sendMessage(helpTextComission.adicionacandidato, addr)
		if cmd[0] == "info":
			info(cmd[1], addr)
		else:	
			return sendMessage(errorsComission.unknwn, addr)

	elif lengh == 3:
		if cmd[0] == "adiciona_candidato":
			return adicionaCandidato(cmd[2], cmd[1], addr)
		else:
			return sendMessage(errorsComission.unknwn, addr)	

	else:
		return sendMessage(errorsComission.unknwn, addr)




def info(nome, addr):
	#import server
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
	#votacoes = votacoes.split()
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
	#import server
	existe_candidato = False
	lista_elei = ficheiroToList("votacoes.txt")
	if os.path.exists(votacao + ".candidates"):
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
			sendMessage(errorsComission.timeover, addr)
			return

	else:
		sendMessage(errorsComission.votacaoinexist, addr)
		return
	
	f = open(path + votacao + ".candidates", 'w')
	for x in range(len(lista_cand)):
		f.write(lista_cand[x]+"\n")
	f.close()

	f=open(path + votacao + ".votes", 'a')
	f.write(nome + " 0" + "\n")
	f.close()

	send = "Foi adicionado o candidato " + nome + " a votacao " + votacao
	return sendMessage(send, addr)