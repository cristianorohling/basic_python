#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

import os


def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def qtdEleitores():
    eleitores = int(input('Quantos eleitores irão votar? '))
    return eleitores

def cabinaVotacao():
    candidato1Votos = 0
    candidato2Votos = 0
    candidato3Votos = 0 
    votosNulos = 0
    eleitores = qtdEleitores()

    for i in range(0, eleitores):
        limpaTela()
        candidato1 = 'Jair Inacio Lulonaro'
        candidato2 = 'Luis Messias Bolsula'
        candidato3 = 'Sargento Dacielmon'
        print(f'Eleitor {i+1} vai votar... lembre-se, o voto é secreto!\n\n')
        print(f'Tecle:\n1) {candidato1}\n2) {candidato2}\n3) {candidato3}')
        voto = int(input('Digite o número de seu candidato: '))    
        match voto:
            case 1:                
                candidato1Votos += 1
            case 2:                 
                candidato2Votos += 1
            case 3:                
                candidato3Votos += 1
            case _:
                votosNulos += 1    

    apuracaoVotos(candidato1, candidato2, candidato3, candidato1Votos, candidato2Votos, candidato3Votos, votosNulos)


def anunciaVencedor(candidato,votos):
    print(f'\n\nVitória de {candidato}, com {votos} votos!!')
    

def apuracaoVotos(candidato1, candidato2, candidato3, candidato1Votos, candidato2Votos, candidato3Votos, votosNulos):
    limpaTela()    
    print(f'Candidato 1 - {candidato1}: {candidato1Votos}')
    print(f'Candidato 2 - {candidato2}: {candidato2Votos}')
    print(f'Candidato 3 - {candidato3}: {candidato3Votos}')
    print(f'Votos Nulos: {votosNulos}')

    if (candidato1Votos > candidato2Votos) and (candidato1Votos > candidato3Votos):
        anunciaVencedor(candidato1,candidato1Votos)
    elif (candidato2Votos > candidato1Votos) and (candidato2Votos > candidato3Votos):
        anunciaVencedor(candidato2,candidato2Votos)
    elif (candidato3Votos > candidato1Votos) and (candidato3Votos > candidato2Votos):
        anunciaVencedor(candidato3,candidato3Votos)
    elif (candidato1Votos == candidato2Votos) or (candidato1Votos == candidato3Votos)  or (candidato3Votos == candidato2Votos):
        print('Houve Empate!')


cabinaVotacao()


