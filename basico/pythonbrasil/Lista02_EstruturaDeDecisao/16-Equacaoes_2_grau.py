'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
* Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
* Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
* Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
* Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import os
import math

def x1(a, b, delta):
    return (-b + math.sqrt(delta)) / 2 * a

def x2(a, b, delta):
    return (-b - math.sqrt(delta)) / 2 * a

def equacaoSegundoGrau():
    try:
        os.system('cls')
        print('Resolução de Equações do Segundo Grau\n\nEntre com os termos a, b e c, como em "ax2 + bx + c = 0:"\n\n')
        a = float(input('Entre com o termo "a": '))
        b = float(input('Entre com o termo "b": '))
        c = float(input('Entre com o termo "c": '))
        delta = (b ** 2) - 4 * a * c

        print(f'\n\nEquação: {a}^2 + {b}x + {c} = 0')

        if (a == 0):
            print('\n\nSe "a" for igual a 0, então esta não pode ser uma Equação do Segundo Grau!\n')
            exit()
        elif (delta < 0):
            print(f'\n\nDELTA = {delta}.\n\nEsta equação não possui raízes reais, uma vez que DELTA é negativo.\n')
            exit()
        elif (delta == 0):
            print(f'\n\nDELTA = {delta}.\n\nEsta equação possui apenas uma raiz real.\n')
            print('x1 = ', x1(a, b, delta))
        elif (delta > 0):
            print(f'\n\nDELTA = {delta}.\n\nEsta equação possui duas raízes reais.\n')
            print('x1 = ', x1(a, b, delta))
            print('x2 = ', x2(a, b, delta))
    except ValueError:
        print('\n\nEntre com valores válidos para a, b e c!\n')


equacaoSegundoGrau()