
# Projecto IRC

## 15/4/17 - Everithing is working! FINAL

## Lista de comandos
```
Eleitor:
    
    Envia:
        info <nome_votacao>
    Recebe:
        "<nome_votacao> aberta/fechado/nao_existente"
    

    Envia:
        voto <nome_votacao> <info_pessoal> <nome_candidato>  
        (justificacao: "Eu sou ... quero votar para ... quero votar em ...)     
    Recebe:
        Se <nome_votacao> <info_pessoal> <nome_candidato>, validos (votacao aberta e existente):
            Recebe: "Voto contabilizado"
        Se um ou mais argumentos estejam invalidos (votacao fechada e/ou nao existente):
            Recebe: Erro/os especifico ao/s argumento/os

    Envia:
        resultado <nome_votacao>

    Recebe:
        Se <nome_votacao> for valido (fechado e existente):
            Recebe: Resultado específico da votacao
        Se <nome_votacao> for invalido (aberto ou nao existente):
            Recebe: Erro específico ao estado da votacao

    Envia:
        outro
    Recebe: "Comando Invalido"


----------------------------------///----------------------------------

            
Comissao:


    Envia:
        info <nome_votacao>
    Recebe:
        "<nome_votacao> aberta/fechado/nao_existente"
    Envia:
        info
    Recebe: Info sobre todas as votacões e respectivos estados



    Envia:
        candidatos <nome_votacao>
    Recebe: Informacao sobre os candidatos da respectiva votacao 

    Envia:
        candidatos 
    Recebe: Informacao sobre todos os candidatos


    Envia:
        adicionar <nome_candidato> <nome_votacao>
    Recebe:
        Se <nome_candidato> <nome_votacao> validos (votacao valida e criada)
            Recebe: "Candidato <nome_candidato> adicionado a votacao <nome_votacao>"
        Se <nome_candidato> <nome_votacao> invalido (votacao invalida/aberta/fechada)
            Recebe: Erro respectivo ao argumento

    Envia:
        outro
    Recebe: "Comando Invalido"


----------------------------------///----------------------------------


Manager:


    Envia:
        cria_eleicao <nome_votacao>
    Recebe:
        Se <nome_votacao> ja existir
            Recebe: "Eleicao ja criada"
        Se <nome_votacao> valido
            Recebe: "Eleicao criada"


    Envia:
        info <nome_votacao>
    Recebe:
        "<nome_votacao> aberta/fechado/nao_existente"
    Envia:
        info
    Recebe: Info sobre todas as votacões e respectivos estados


    Envia:
        abre <nome_votacao>
    Recebe:
        Se <nome_votacao> valido (criada)
            Recebe: "<nome_votacao> iniciada" 
        Se <nome_votacao> invalido (fechada/aberta/nao existente)
            Recebe: Erro respectivo


    Envia:
        fecha <nome_votacao>
    Recebe:
        Se <nome_votacao> valido (aberta)
            Recebe: "<nome_votacao> fechada" 
        Se <nome_votacao> invalido (fechada/nao existente)
            Recebe: Erro respectivo

    Envia:
        outro
    Recebe: "Comando Invalido"


----------------------------------///----------------------------------
```

