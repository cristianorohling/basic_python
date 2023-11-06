#Faça um programa que calcule o mostre a média aritmética de N notas.

import os

def recebeNotas(numero):
    while True:
        try:
            nota = int(input(f'Digite a {numero}ª nota: '))        
            return nota
        except ValueError:
            print('Digite um valor válido!')
    


def entradaDados():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            qtdNotas = int(input('Digite quantas notas serão recebidas: '))
            somaNotas = 0
            for i in range(1,qtdNotas+1):
                somaNotas = somaNotas + recebeNotas(i)

            print(f'\n\nA média das {qtdNotas} digitadas é {somaNotas / qtdNotas}')
            break
        except ValueError:        
            print('Digite um valor inteuiro válido!')

entradaDados()