'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E  

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''

import os

os.system('cls' if os.name == 'nt' else 'clear')

print('Programa para Cálculo de Médias e Conceitos Escolares\n\n')

try:
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2

    if (nota1 > 100) or (nota2 > 100) or (nota1 < 0) or (nota2 < 0):
        print('\nERRO: Digite notas com valores entre 0 e 100.\n\n')
        exit()
    elif (media > 90) and (media <= 100):
        conceito = 'A'
    elif (media > 75) and (media <= 90):
        conceito = 'B'
    elif (media > 60) and (media <= 75):
        conceito = 'C'
    elif (media > 40) and (media <= 60):
        conceito = 'D'
    elif (media >= 0) and (media <= 40):
        conceito = 'E'
    
    
    print(f'\n\n1ª nota: {nota1}\n2ª nota: {nota2}\n\nMédia: {media}\nConceito : {conceito}' )
    if (conceito == 'A') or (conceito == 'B') or (conceito == 'C'):
        print('\n*** Aluno Aprovado! ***\n\n')
    else:
        print('\n*** Aluno Reprovado! ***\n\n')

except ValueError:
    print('\nERRO: Digite notas com valores válidos.\n\n')
    