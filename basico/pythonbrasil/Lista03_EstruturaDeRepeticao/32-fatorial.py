'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

import os

os.system('cls' if os.name == 'nt' else 'clear')
try:
    numero = int(input('Entre com um número inteiro: '))
    contador = numero
    strFatorial = ''
    fatorial = 1

    while contador > 0:
        fatorial = fatorial * contador
        numeroStr = str(contador)    
        if contador == 1:
            strFatorial = strFatorial + '. 1 = '
        elif contador != numero:
            strFatorial = strFatorial + ' . ' + numeroStr           
        else:
            strFatorial = numeroStr       
        contador -= 1

    print(strFatorial, fatorial)
except ValueError:
    print('Erro! Digite um valor inteiro válido!')