#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import os

os.system('cls')

try:
    numero = float(input('Digite um numero: '))
    numeroArredondado = round(numero)
    parteDecimal = numero - numeroArredondado

    if parteDecimal != 0:
        print('Número decimal!')
    else:
        print('Número inteiro!')
except ValueError:
    print('Digite um número válido!')
