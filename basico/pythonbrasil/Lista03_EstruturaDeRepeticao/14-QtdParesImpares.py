'''
Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''

import os

os.system('cls' if os.name == 'nt' else 'clear') 

def verificaParImpar(numero):
    if (numero % 2) == 0:
        return "Par"
    else:
        return "Ímpar"
    
def imprimeResultados(listaNumeros,listaParImpar):
    pares = 0
    impares = 0
    loops = len(listaNumeros) 
    for i in range(0,loops):        
        print(f'O Número {listaNumeros[i]} é {listaParImpar[i]}!')
        if (listaParImpar[i] == 'Par'):
            pares += 1
        else:
            impares += 1
    print(f'\n\nForam entrados {pares} números pares e {impares} números ímpares!')


def entradaNumeros():
    listaNumeros = []
    listaParImpar = []

    for i in range(1,11):
        while True:
            try:
                numero = int(input(f'Entre com o {i}º número: '))
                listaNumeros.append(numero) 
                listaParImpar.append(verificaParImpar(numero))
                break
            except ValueError:
                print('Número inválido!')
    print('\n\n')
    imprimeResultados(listaNumeros,listaParImpar)
    


entradaNumeros()