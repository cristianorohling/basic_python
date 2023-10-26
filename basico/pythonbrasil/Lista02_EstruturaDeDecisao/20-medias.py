'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
import os
import numpy as np

def verificaValores(valor):
    if (valor < 0):
        print(f'Valor {valor} inválido por ser número negativo!')
        exit()
    elif (valor > 100):
        print(f'Valor {valor} inválido por ser maior que 100!')
        exit()
    else:
        return(valor)

os.system('cls')
notas = [0, 0, 0] 

try:
    notas[0] = verificaValores(float(input('Digite a 1ª nota: ')))
    notas[1] = verificaValores(float(input('Digite a 2ª nota: ')))
    notas[2] = verificaValores(float(input('Digite a 3ª nota: ')))    

    #Entrego a lista para uma array
    array = np.array(notas)
    #calculo a média
    media = array.mean()

    if media == 100:
        print(f'\nMédia {round(media,1)}\n\nAprovado com distinção!')
    elif media >= 70:
        print(f'\nMédia {round(media,1)}\n\nAprovado!')    
    else:
        print(f'\nMédia {round(media,1)}\n\nReprovado!')

except ValueError:
    print('Digite um número válido entre 1 e 100')