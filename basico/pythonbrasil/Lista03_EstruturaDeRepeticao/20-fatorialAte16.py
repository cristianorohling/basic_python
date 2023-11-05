#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
#fatorial a números inteiros positivos e menores que 16.

import os

os.system('cls' if os.name == 'nt' else 'clear')

def entraNumero():
    numero = int(input('Digite um número entre 1 e 16 para saber seu fatorial: '))
    return numero

numero = 0
while (numero <=0) or (numero >=16):        
    numero = entraNumero()

contador = numero


while (contador > 0):            
    if numero == contador:
        fatorial = numero        
    else:
        fatorial = fatorial * contador        
    contador -= 1

print(f'O fatorial de {numero} é : {fatorial}')