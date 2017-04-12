import socket
import os

class serverInfo:
	PORT = 0
	server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	addrs = {} # dict: endereco -> nome. Ex: clients[('127.0.0.1',17234)]="user"
	clients = {}
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

class errorsManager:
	more = color.BOLD + color.RED + "Erro: " + color.END + "Demasiados argumentos!\nUse o unico argumento -help para mais informacoes"
	less = color.BOLD + color.RED + "Erro: " + color.END + "Faltam argumentos!\nUse o unico argumento -help para mais informacoes"
	unknwn = color.BOLD + color.RED + "Erro: " + color.END + "Comando deconhecido\nUse o comando commands para listar todos os comandos possiveis"
	votexiste = color.BOLD + color.RED + "Erro: " + color.END + "Ja existe uma votacao com o nome indicado"
	voteinexist = color.BOLD + color.RED + "Erro: " + color.END + "Nao existe uma votacao com o nome indicado"
	voteabrt = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja aberta"
	voteconc = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja concluido"
	voteinic = color.BOLD + color.RED + "Erro: " + color.END + "Votacao nao inicializada"
	votefec = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja fechada"
	errogen = color.BOLD + color.RED + "Erro: " + color.END + "Comando Incorrecto"

class errorsVoter:
	more = color.BOLD + color.RED + "Erro: " + color.END + "Demasiados argumentos!\nUse o unico argumento -help para mais informacoes"
	less = color.BOLD + color.RED + "Erro: " + color.END + "Faltam argumentos!\nUse o unico argumento -help para mais informacoes"
	unknwn = color.BOLD + color.RED + "Erro: " + color.END + "Comando deconhecido\nUse o comando commands para listar todos os comandos possiveis"
	revote = color.BOLD + color.RED + "Erro: " + color.END + "O seu voto ja foi contabilizado"
	voteconc = color.BOLD + color.RED + "Erro: " + color.END + "Votacao ja concluido"
	voteinic = color.BOLD + color.RED + "Erro: " + color.END + "Votacao nao existente"
	votefec = color.BOLD + color.RED + "Erro: " + color.END + "Votacao fechada"
	voteinv = color.BOLD + color.RED + "Erro: " + color.END + "Votacao invalida (fechada ou concluida)"
	candinv = color.BOLD + color.RED + "Erro: " + color.END + "Candidato invalido"


class errorsComission:
	less = color.BOLD + color.RED + "Erro: " + color.END + "Faltam argumentos!\nUse o unico argumento commands para mais informacoes"
	unknwn = color.BOLD + color.RED + "Erro: " + color.END + "Comando deconhecido\nUse o comando commands para listar todos os comandos possiveis"
	votacaoinexist = color.BOLD + color.RED + "Erro: " + color.END + "Nao existe nenhuma votacao com o nome indicado"
	timeover = color.BOLD + color.RED + "Erro: " + color.END + "A votacao que procura ja nao aceita novos candidatos"
	candidatoexis = color.BOLD + color.RED + "Erro: " + color.END + "O candidato ja esta adicionado a esta votacao"



class helpTextManager:
	info = "\n\ninfo\n-Lista informacoes dos estados de todas as votacoes\ninfo <nome_votacao>\n-Lista informacoes do estado da votacao apresentada\n"
	criaeleicao = "\n\ncria_votacao <nome_votacao>\n-Inicializa uma votacao\n"
	abre = "\n\nabre <nome_votacao>\n-Abre uma votacao fechada\n"
	fecha = "\n\nfecha <nome_votacao>\n-Fecha uma votacao fechada\n"
	cleandir = "\n\ncleandir\n-Limpa a directoria de trabalho (APAGA TODOS OS DADOS DE VOTACOES!)\n"
	
	comandos = "\n\nComandos possiveis:       (use o argumento -help para obter info sobre cada comando)\n-info\n-cria_votacao\n-abre\n-fecha\n-cleandir\n-logout\n-exit\n-killserver"

class helpTextComission:
	info = "\n\ninfo\n-Lista informacoes dos de uma votacao\ninfo <nome_votacao>\n"
	adicionacandidato = "\n\nadiciona_candidato <votacao> <nome_candidato>\n-Adiciona um candidato a uma votacao especifica\n"

	comandos = "\n\nComandos possiveis:       (use o argumento -help para obter info sobre cada comando)\n-adiciona_candidato <votacao> <nome_candidato>\n-info <votacao>"




def sendMessage(msg, addr):
	#import server
	sending = str(msg)
	serverInfo.server.sendto(sending.encode(),addr)

def ficheiroToList(nome):
	ret = open(serverInfo.path + nome, "r")
	#votacoes = votacoes.split()
	with open(serverInfo.path + nome) as f:
		content = f.readlines()
		f.close()
	ret = [x.strip() for x in content]
	return ret
