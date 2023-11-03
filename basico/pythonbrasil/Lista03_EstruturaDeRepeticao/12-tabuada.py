'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

'''

import os

def criaTabuada(numero):
    print(f'\nTabuada do {numero}:\n\n')
    for i in range(10): 
        print(f'{numero} x {i+1} = {numero * (i+1)}')
    
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        numero = int(input('Digite um número entre 1 e 10: '))
        if (numero >= 1) and (numero <=10):
            criaTabuada(numero)
            break
        else:
            print('Erro! O número precisa ser entre 1 e 10!')
    except ValueError:
        print('Entre com um número válido!')