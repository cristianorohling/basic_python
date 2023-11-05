#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import os

def entradaDados(qtdNumeros):
    listaDados = []
    for i in range(1,qtdNumeros+1):
        while True:
            try:
                numero = int(input(f'Digite o {i}º número: '))
                listaDados.append(numero)
                break
            except ValueError:
                print("Oops! O valor digitado não é um número inteiro. Tente novamente...")
    return listaDados


def imprimeRespostas(listaDados):
    print(f'\n\nMaior Valor: {max(listaDados)}')
    print(f'Menor Valor: {min(listaDados)}')
    print(f'Soma dos Valores: {sum(listaDados)}')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            qtdNumeros = int(input('Quantos números devem ser entrados? '))    
            break
        except ValueError:
            print('Digite um número inteiro válido!')        

    listaRespostas = entradaDados(qtdNumeros)            
    imprimeRespostas(listaRespostas)

main()