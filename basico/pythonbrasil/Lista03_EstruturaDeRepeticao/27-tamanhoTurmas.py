'''
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
'''

import os

def defineQtdTurmas():
    while True:
        try:
            qtdTurmas = int(input('Quantas turmas tem a escola? '))            
            return qtdTurmas
            break
        except ValueError:
            print('Erro! Digite um número inteiro válido para a quantidade de turmas! ')

def entraQtdAlunos(turma):
    try:
        qtdAlunos = int(input(f'Quantos alunos tem a turma {turma} (maximo: 40)? '))
    except ValueError:
        print('Erro! Digite um número inteiro válido para a quantidade de alunos! ')
    return qtdAlunos

def defineQtdAlunos(turma):
    while True:
        qtdAlunos = entraQtdAlunos(turma)        
        if qtdAlunos > 40:
            print('Erro! Cada turma pode ter no máximo 40 alunos! ')            
        else:
            return qtdAlunos
            break

def dadosTurmas(qtdTurmas, totalAlunos):
    media = totalAlunos / qtdTurmas
    print(f'\n\nO colégio conta com {qtdTurmas} turmas, totalizando {totalAlunos} alunos.\nEm média, temos {media} alunos por sala de aula.')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    totalAlunos = 0
    qtdTurmas = defineQtdTurmas()
    for i in range(0, qtdTurmas):        
        qtdAlunos = defineQtdAlunos(i+1)
        totalAlunos = totalAlunos + qtdAlunos
    dadosTurmas(qtdTurmas, totalAlunos)

main()