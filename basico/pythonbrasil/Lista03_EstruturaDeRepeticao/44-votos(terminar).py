'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.
'''

import os

def contagemVotos(dictVotos):
    print(dictVotos)

def limparTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostraMenu():    
    limparTela()
    print('BEM VINDO À URNA ELETRÔNICA!\n\nOpções:\n\n1) MATEUS\n2) MARCOS\n3) LUCAS\n4) JOÃO\n5) Voto Nulo\n6) Voto Branco\n\nEscolher alguma opção que não conste do menu anulará seu voto.')
    print('Tecle 0 para encerrar votação')

def retornaCandidato(voto):
    if voto == 1:
        return 'Mateus'
    elif voto == 2:
        return 'Marcos'
    elif voto == 3:
        return 'Lucas'
    elif voto == 4:
        return 'João'
    elif voto == 5:
        return 'Voto Nulo'
    elif voto == 6:
        return 'Voto em Branco'
    else:
        return 'Voto Anulado'
  
def cabineVotacao():
    #A VOTAÇÃO VAI ACEITAR APENAS NUMEROS INTEIROS
    while True:
        try:
            mostraMenu()
            voto = int(input('Digite o seu voto: '))
            break
        except ValueError:
            print('Digite um valor válido!')
    return voto

def loopUrnaEletronica():
    dictVotos = {}
    numeroVoto = 0
    while True:
        voto = cabineVotacao()
        if voto != 0:
            candidato = retornaCandidato(voto)
            numeroVoto += 1 
            dictVotos[numeroVoto] = candidato
        else:
            limparTela()            
            print('Encerrando Votação')
            contagemVotos(dictVotos)            
            break

loopUrnaEletronica()