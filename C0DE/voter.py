import os
from auxfuncs import*
#wololo
path = os.getcwd() + "/elecfiles/"

'''
info - V

voto - V

resultado - X

outro -X

'''


class helpText:
    info = "info de info incpeption"
    votar = "help votacao"
    listar = "help resultados"
    commands = "help comands"



######################################################################################################################################################

def checkVoter(cmd, addr):
	#import server
    

	lengh = len(cmd)

	if lengh>=1:

		#INFO
		if cmd[0] == "info" and lengh == 1:
			info("all", 0, addr)
		elif cmd[0] == "info" and lengh == 2: 
			if cmd[1] == "-help":
				return sendMessage(helpText.info, addr)
			else:	
				info("espec", cmd[1], addr)
		elif cmd[0] == "info" and lengh > 2:
			return sendMessage(errors.more, addr)

        if cmd[0] == "vota" and lengh < 4:
            return sendMessage(errorsVoter.less, addr)
        elif cmd[0] == "vota" and lengh > 4:
            return sendMessage(errorsVoter.more, addr)
        elif cmd[0] == "vota" and lengh == 4:
			return votar(cmd[1], cmd[2], cmd[3], addr)
        
		

	else:
		return sendMessage(errorsVoter.unknwn, addr)       
  



def candidatoinfo(candidato):
    infocand=candidato.split()
    return infocand
    

	
def candidatoIndice(lista, candidato):
	for x in range(len(lista)):
		nome = candidatoinfo(lista[x]) 
		if nome[0] == str(candidato):
			return x
	return "erro"

#votacao.votos - cc
def votar(votacao, cc, candidato, addr):				
	if votacao_existe(votacao, addr) and cc_unico(cc, votacao, addr) and candidato_val(votacao, candidato, addr):
		print("true \n")
		#votos = ficheiroToList(votacao + ".votes")
		candidatos = ficheiroToList(votacao + ".votes")
		print(candidatos)
		indice = candidatoIndice(candidatos, candidato)
		print(indice)
		info = candidatoinfo(candidatos[indice])
		print(info[0] + " , " + info[1])
		#info[0] = nome info[1]+votos
		info[1] = int(info[1])
		info[1] += 1
		act = info[0] + " " + str(info[1])
		candidatos[indice] = act
	
		actual = open(path + votacao + ".votes", "w")
		for x in range(len(candidatos)):
		    actual.write(str(candidatos[x]) + "\n")

		votos = open(path + votacao + ".cc", "a")
		votos.write(str(cc) + "\n")


		send = "Voto contabilizado!"
		return sendMessage(send, addr)


	

def votacao_existe(votacao, addr):
	if os.path.exists(path + "votacoes.txt"):
		lista = ficheiroToList("votacoes.txt")
		if str(votacao + " 1") in lista:
			return True
		else:
			return sendMessage(errorsVoter.voteinv, addr)
	else:
		return sendMessage(errorsVoter.corr, addr)

def cc_unico(cc, votacao, addr):
    lista = ficheiroToList(votacao + ".cc")
    if str(cc) in lista:
    	return sendMessage(errorsVoter.revote, addr)
    else:
    	return True
    
def candidato_val(votacao, candidato, addr):
    lista = ficheiroToList(votacao + ".candidates")
    if str(candidato) in lista:
    	return True
    else:
    	return sendMessage(errorsVoter.candinv, addr)
    
def votacaoNome(votacao):
	return str(votacao[0:len(votacao)-2])

def votacaoEstado(votacao):
	return str(votacao[-1])


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
	#import server
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



'''




###################################################################################

#Variaveis de teste

votacoes_existentes=['Benfica', 'Sporting']

candidatos=['candA', 'candB']

dados={'Benfica':[88888888,11111111],'Sporting':[]}

reg={'candA':1, 'candB':0}

###################################################################################

#FUNCOES

def votacao_existe(v):							#verifica se a votacao existe
	return v in votacoes_existentes


#def votacao_aberta(v):
	


def cc_val(id):								#verifica se a identificacao e valida
	return isinstance(id,str) and len(id)==8




def candidato_val(cand):						#verifica se o candidato existe na votacao
	return cand in candidatos




		

def resultados_finais(votacao):
	#if votacao_aberta==False:
	return reg
	
	'''