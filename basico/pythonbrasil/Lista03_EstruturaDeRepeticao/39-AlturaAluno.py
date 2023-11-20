'''
Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

import os

def codAluno(aluno):    
    while True:    
        try:
            codAluno = int(input(f'Digite o código do {aluno}º aluno: '))
            return codAluno
        except ValueError:
            print('Digite um valor inteiro válido!')

def alturaAluno(aluno):    
    while True:    
        try:
            altura = int(input(f'Digite a altura do aluno {aluno} em cm: '))
            return altura
        except ValueError:
            print('Digite um valor inteiro válido!')


def main():
    maiorAltura = 0
    codMaiorAltura = 0

    for i in range(0,10):
        os.system('cls' if os.name == 'nt' else 'clear')
        aluno = i + 1    
        codigoAluno = codAluno(aluno)
        altura = alturaAluno(aluno)    
        while True:
            if altura < 100:
                print('Altura inválida! Aluno com altura inferior a 100 cm!')
                altura = alturaAluno(aluno)            
            elif altura > 230:
                print('Altura inválida! Aluno com altura superior a 230 cm!')
                altura = alturaAluno(aluno)            
            else:
                break
        
        if i == 0:
            maiorAltura = altura
            codMaiorAltura = codigoAluno
        elif altura > maiorAltura:
            maiorAltura = altura
            codMaiorAltura = codigoAluno
        
    print(f'\nO aluno com a maior altura é o de código {codMaiorAltura}, com a altura de {maiorAltura} cm!')


main()