import os 
from auxfuncs import* 
 
path = os.getcwd() + "/elecfiles/" 
 
 
def checkVoter(cmd, addr): 
 
     
 
  lengh = len(cmd) 
 
  if lengh>=1: 
 
    #INFO 
    if cmd[0] == "info" and lengh == 1: 
      return info("all", 0, addr) 
    elif cmd[0] == "info" and lengh == 2:  
      if cmd[1] == "-help": 
        return sendMessage(helpTextVoter.info, addr) 
      else:   
        return info("espec", cmd[1], addr) 
    elif cmd[0] == "info" and lengh > 2: 
      return sendMessage(errors.more, addr) 
 
    if cmd[0] == "vota" and lengh == 2: 
      if cmd[1] == "-help": 
        return sendMessage(helpTextVoter.vota, addr) 
      else: 
        sendMessage(errorsVoter.unknwn, addr) 
 
 
    if cmd[0] == "vota" and lengh < 4: 
      return sendMessage(errorsVoter.less, addr) 
    elif cmd[0] == "vota" and lengh > 4: 
      return sendMessage(errorsVoter.more, addr) 
    elif cmd[0] == "vota" and lengh == 4: 
      return votar(cmd[1], cmd[2], cmd[3], addr) 
    elif lengh == 1 and cmd[0] == "commands": 
      return sendMessage(helpTextVoter.comandos, addr) 
 
    if cmd[0] == "resultados" and lengh == 2 and cmd[1] == "-help": 
      return sendMessage(helpTextVoter.resultados, addr) 
    elif cmd[0] == "resultados" and lengh == 2 and cmd[1] != "-help": 
      return resultado(cmd[1], addr) 
    elif cmd[0] == "resultados" and lengh > 2: 
      return sendMessage(errorsVoter.more, addr) 
    elif cmd[0] == "resultados" and lengh < 2: 
      return sendMessage(errorsVoter.less, addr) 
 
 
    else: 
      return sendMessage(errorsVoter.unknwn, addr) 
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
  if votacao_existe(votacao, addr) and cc_val(cc, votacao, addr) and cc_unico(cc, votacao, addr) and candidato_val(votacao, candidato, addr): 
    print("true \n") 
    #votos = ficheiroToList(votacao + ".votes") 
 
    if not os.path.exists(path + votacao + ".votes"): 
      return sendMessage(errors.Voter.corr, addr) 
 
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
   
    if not os.path.exists(path + "votacoes.txt"): 
      return sendMessage(errors.Voter.corr, addr) 
    actual = open(path + votacao + ".votes", "w") 
    for x in range(len(candidatos)): 
        actual.write(str(candidatos[x]) + "\n") 
 
    if not os.path.exists(path + votacao + ".cc"): 
      return sendMessage(errors.Voter.corr, addr) 
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
 
 
def votacao_concluida(votacao, addr): 
  if os.path.exists(path + "votacoes.txt"): 
    lista = ficheiroToList("votacoes.txt") 
    if str(votacao + " 2") in lista: 
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
     
def cc_val(cc, votacao, addr):  
    try:  
      int(cc)  
      if len(str(cc))==8:  
        return True  
      else:  
        sendMessage(errorsVoter.ccinv, addr)  
    except:  
      return sendMessage(errorsVoter.ccinv, addr)  
 
 
 
 
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
 
    if len(lista) == 1: 
      send += createInfo(lista[0]) + "\n" 
    else: 
      for x in range(len(lista)): 
        send += createInfo(lista[x]) + "\n" 
    return sendMessage(send, addr) 
 
 
  elif str(tipo) == "espec": 
     
    lista = ficheiroToList("votacoes.txt") 
    indice = votacaoIndice(lista, nome) 
    if indice == "erro": 
      return sendMessage(errorsManager.voteinexist, addr) 
    send = "\n\n\n" 
    send += createInfo(lista[indice]) + "\n" 
    return sendMessage(send, addr) 
 
def resultado(nome, addr): 
  send = "\nOs resultados para a votacao " + nome + " sao:\n\n" 
  if votacao_concluida(nome, addr): 
    file = open(path + nome + ".votes", "r")   
    send += file.read() 
    sendMessage(send, addr) 
  else: 
    return sendMessage(errorsVoter.voteinv, addr) 