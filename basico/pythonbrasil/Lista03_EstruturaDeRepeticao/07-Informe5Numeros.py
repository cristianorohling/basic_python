#Faça um programa que leia 5 números e informe o maior número.
import os

listaNumeros = [] 

os.system('cls')

def cadastraNumero(i):
    while True:
        try:
            numero = int(input(f'Digite o {i}º número: '))
            return numero
        except ValueError:
            print('Valor inválido! Digite um número inteiro!')


i = 0
while (i < 5): 
    numero = cadastraNumero(i + 1)
    listaNumeros.append(numero)
    i +=1

maiorValor = max(listaNumeros)

print(f'\n\nMaior Valor (calculado pela Lista): {maiorValor}')

