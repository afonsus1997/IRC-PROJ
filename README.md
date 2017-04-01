
#Projecto IRC



##Lista de comandos
```
Eleitor:
    
    Envia:
    	info <nome_votação>
    Recebe:
    	"<nome_votacao> aberta/fechado/nao_existente"
    

    Envia:
        voto <nome_votação> <info_pessoal> <nome_candidato>  (justificação: "Eu sou ... quero votar para ... quero votar em ...)     
    Recebe:
        Se <nome_votação> <info_pessoal> <nome_candidato>, validos (votação aberta e existente):
        	Revebe: "Voto Contabilizado"
        Se um ou mais argumentos estejam inválidos (votação fechada e/ou nao existente):
        	Recebe: Erro/os especifico ao/s argumento/os

    Envia:
    	resultado <nome_votação>

    Recebe:
    	Se <nome_votação> for válido (fechado e existente):
    		Recebe: Resultado específico da votação
    	Se <nome_votação> for inválido (aberto ou nao existente):
    		Recebe: Erro específico ao estado da votação

    Envia:
    	outro
    Recebe: "Comando Inválido"



            
Comissão:


	Envia:
    	info <nome_votação>
    Recebe:
    	"<nome_votacao> aberta/fechado/nao_existente"
    Envia:
    	info
    Recebe: Info sobre todas as votações e respectivos estados



    Envia:
    	candidatos <nome_votação>
    Recebe: Informação sobre os candidatos da respectiva votação 

	Envia:
    	candidatos 
    Recebe: Informação sobre todos os candidatos


    Envia:
    	Adicionar <nome_candidato> <nome_votação>
   	Recebe:
   		Se <nome_candidato> <nome_votação> válidos (votação válida e criada)
   			Recebe: "Candidato <nome_candidato> adicionado à votação <nome_votação>""
   		Se <nome_candidato> <nome_votação> inválido (votação inválida/aberta/fechada)
   			Recebe: Erro respectivo ao argumento

    Envia:
    	outro
    Recebe: "Comando Inválido"




Manager:


	Envia:
		cria_eleiçao <nome_votação>
	Recebe:
		Se <nome_votação> já existir
			Recebe: "Eleição já criada"
		Se <nome_votação> válido


	Envia:
    	info <nome_votação>
    Recebe:
    	"<nome_votacao> aberta/fechado/nao_existente"
    Envia:
    	info
    Recebe: Info sobre todas as votações e respectivos estados


    Envia:
    	abre <nome_votação>
    Recebe:
    	Se <nome_votação> válido (criada)
    		Recebe: "Votação iniciada" 
    	Se <nome_votação> inválido (fechada/aberta/nao existente)
    		Recebe: Erro respectivo


    Envia:
    	fecha <nome_votação>
    Recebe:
    	Se <nome_votação> válido (aberta)
    		Recebe: "Votação fechada" 
    	Se <nome_votação> inválido (fechada/nao existente)
    		Recebe: Erro respectivo

    Envia:
    	outro
    Recebe: "Comando Inválido"
```

