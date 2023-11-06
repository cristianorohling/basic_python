'''
Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma 
varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
import os

def entraIdades(numero):
    while True:
        try:
            idade = int(input(f'Digite a idade da {numero}ª pessoa? '))
            if idade <= 120:
                return idade
            else:
                print('Você só pode estar de sacanagem comigo, digite uma idade até 120 anos!')
        except ValueError:
            print('Digite uma idade válida!')
    

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    idadeAcumulada = 0
    while True:
        try:
            qtdPessoas = int(input('Quantas pessoas? '))
            for i in range(0, qtdPessoas):
                idadeAcumulada = idadeAcumulada + entraIdades(i+1)

            media = idadeAcumulada / qtdPessoas

            if media >=0 and media <= 25:
                print('Turma jovem')
            elif media >= 26 and media <= 60:
                print('Turma Adulta')
            elif media > 60:
                print('Turma Idosa')                
        except ValueError:
            print('Digite um valor válido!')

main()