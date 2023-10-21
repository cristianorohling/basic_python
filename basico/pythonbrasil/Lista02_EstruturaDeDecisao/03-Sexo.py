#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

import os

os.system('cls')

print('M) MASCULINO\nF) FEMININO\nO) OUTRO\nN) NÃO INFORMAR')

sexo = input('Entre com o seu sexo: ')
sexo = sexo.upper() 

match sexo: 
    case 'M':
        print('MASCULINO')
    case 'F':
        print('FEMININO')
    case 'O':
        print('OUTRO')
    case 'N':
        print('NÃO INFORMAR')
    case _:
        print('Sexo Inválido!')
