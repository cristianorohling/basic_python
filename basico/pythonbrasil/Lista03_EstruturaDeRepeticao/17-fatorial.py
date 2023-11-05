#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
import os

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input('Digite o número sobre o qual deseja saber o fatorial: '))
contador = numero


while (contador > 0):            
    if numero == contador:
        fatorial = numero        
    else:
        fatorial = fatorial * contador        
    contador -= 1

print(f'O fatorial de {numero} é : {fatorial}')