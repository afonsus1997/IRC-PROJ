import os
from auxfuncs import*

path = os.getcwd() + "/elecfiles/"

'''
info - X

voto - X

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
	import server
    

	lengh = len(cmd)

	if lengh>=1:

		#INFO
		if cmd[0] == "infovotos" and lengh == 1:
			infovotos("all", 0, addr)
		elif cmd[0] == "infovotos" and lengh == 2: 
			if cmd[1] == "-help":
				server.sendMessage(helpText.info, addr)
			else:	
				infovotos("espec", cmd[1], addr)
		elif cmd[0] == "infovotos" and lengh > 2:
			server.sendMessage(errors.more, addr)

        if cmd[0] == "vota" and lengh < 4:
            pass
        elif cmd[0] == "vota" and lengh > 4:
            pass
        elif cmd[0] == "vota" and lengh == 4:
            votar(cmd[1], cmd[2], cmd[3], addr)
            
            
  
def infovotos(asd, dfg, ghj):
    return



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
		
		#votos = ficheiroToList(votacao + ".votes")
		candidatos = ficheiroToList(votacao + ".votes")
		indice = candidatoIndice(candidatos, candidato)
		info = candidatoinfo(candidatos[indice])
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
    #tem de existir votacao.cc + votacao.candidates + votacao.votes
    if os.path.exists(path + "votacoes.txt"):
    	lista = ficheiroToList("votacoes.txt")
    	if str(votacao + " 1") in lista:
    		return True
    else:
    	return sendMessage(errorsVoter.voteinv, addr)

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