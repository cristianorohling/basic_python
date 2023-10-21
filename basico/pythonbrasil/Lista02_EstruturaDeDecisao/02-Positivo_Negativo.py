#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um número: '))

if (valor == 0):
    print(f'O Zero é um número neutro!')
elif (valor > 0):
    print(f'O número {valor} é POSITIVO!')
elif (valor < 0):   
    print(f'O número {valor} é NEGATIVO!')