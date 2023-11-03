'''
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

import os

os.system('cls' if os.name == 'nt' else 'clear')

try:
    base = int(input('Digite a base: '))
    expoente = int(input('Digite o expoente: '))

    if expoente == 0: 
        #todo número elevado a 0 é igual a 1   
        resultado = 1
    elif expoente == 1:
        #todo número elevado a 1 é igual a ele mesmo
        resultado = base
    elif expoente == -1:
        resultado = 1 / base
    elif (expoente >= 0):
        resultado = base * base
        for i in range(expoente-2):
            resultado = resultado * base
    elif (expoente < -1):
        expoenteInvertido = expoente * (-1)    
        resultado = (1 / base) * (1 / base)
        for i in range(expoenteInvertido-2):
            resultado = resultado * (1/base)

    print(f'\n\n{base}^{expoente} = {resultado}')
except ValueError:
    print('ERRO: Digite apenas valores inteiros válidos!')