#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import os

def entradaDados(qtdNumeros):
    listaDados = []    
    for i in range(1,qtdNumeros+1):
        while True:
            try:
                numero = int(input(f'Digite o {i}º número: '))
                while numero < 0 or numero > 1000:
                    print('Digite um número entre 0 e 1000:')
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
    #os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            qtdNumeros = int(input('Quantos números devem ser entrados? '))    
            break
        except ValueError:
            print('Digite um número inteiro válido!')        

    listaRespostas = entradaDados(qtdNumeros)            
    imprimeRespostas(listaRespostas)

main()

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
    #os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            qtdNumeros = int(input('Quantos números devem ser entrados? '))    
            break
        except ValueError:
            print('Digite um número inteiro válido!')        

    listaRespostas = entradaDados(qtdNumeros)            
    imprimeRespostas(listaRespostas)
    

main()