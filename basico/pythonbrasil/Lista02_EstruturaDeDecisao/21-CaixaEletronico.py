'''
Faça um Programa para um caixa eletrônico. 
- O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
- As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 999 reais. 
- O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

import os

def calcularSaque(valor):
    valorOriginal = valor
    #qtd notas de 100    
    valor100 = int(valor / 100)
    valor = valor - (valor100 * 100)
    #qtd notas de 50
    valor50 = int(valor / 50)
    valor = valor - (valor50 * 50)
    #qtd notas de 10
    valor10 = int(valor / 10)
    valor = valor - (valor10 * 10)
    #qtd notas de 5
    valor5 = int(valor / 5)
    valor = valor - (valor5 * 5)
    #qtd notas de 1
    valor1 = int(valor / 1)
    valor = valor - (valor1 * 1)

    print(f'Foram solicitados R$ {valorOriginal}.\n\nSerão fornecidas:\n\n')

    if valor100 != 0:        
        print(f'* {valor100} nota(s) de R$ 100')
          
    if valor50 != 0:
        print(f'* {valor50} nota(s) de R$ 50')

    if valor10 != 0:
        print(f'* {valor10} nota(s) de R$ 10')

    if valor5 != 0:
        print(f'* {valor5} nota(s) de R$ 5')

    if valor1 != 0:
        print(f'* {valor1} nota(s) de R$ 1')
    
os.system('cls')
print('*** Caixa Eletrônico ***')

valorSacar = int(input('Quanto deseja sacar hoje (Valor máximo: R$ 999)? > '))

if (valorSacar > 999):
    print(f'O valor de R$ {valorSacar} é inválido!')
else:
    calcularSaque(valorSacar)