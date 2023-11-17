'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

'''

import os

def inputNumeros(num):
    while True:
        try:
            numero = int(input(f'Digite o {num}º número! '))
            return numero
        except ValueError:
            print('Digite um número inteiro válido!')        

def inputTabuada():
    while True:
        try:
            tabuada = int(input(f'Qual tabuada iremos calcular? '))
            return tabuada
        except ValueError:
            print('Digite um número inteiro válido!')        

def entraInicioFim():
    os.system('cls')
    tabuada = inputTabuada()
    ini = inputNumeros(1)
    fim = inputNumeros(2)
    while True:
        if ini > fim:
            print('O numero final não pode ser menor que o número inicial!')
            fim = inputNumeros(2)
        else:
            montaTabuada(tabuada, ini, fim)
            break       

def montaTabuada(tabuada, ini,fim):
    for i in range(ini,fim+1):
        print(f'{tabuada} x {i} = {tabuada * i}')    
 
    
entraInicioFim()