'''
Faça um programa que peça um número inteiro e 
determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente 
por ele mesmo e por 1.

1) Verifique se o número é menor ou igual a 1. 
Se for, ele não é primo.

2) Verifique se o número é igual a 2. 
Se for, ele é primo.

3) Verifique se o número é divisível por
algum número inteiro de 2 até a raiz quadrada
do número. Se for, ele não é primo. 
Isso ocorre porque, se houver um divisor maior que 
a raiz quadrada, também deve haver um divisor menor
do que a raiz quadrada. Portanto, não é necessário
verificar além da raiz quadrada.
'''

import math
import os
							
def verificaPrimo(numero):
	primo = True
	if numero <= 1:
		print('Não Primo.')
	elif numero == 2:
		print('Primo')
	else:
		raiz = math.ceil(numero ** 0.5)
		for i in range(2,raiz+1):
			verifica = numero % i
			if verifica == 0:
				primo = False
	return primo

def entraNumero():
	while True:
		try:
			numero = int(input('Digite um numero: '))
			break
		except ValueError:
			print('Deu certo não')
	return(numero)

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	if verificaPrimo(entraNumero()) == True:
		print('Primo')
	else:
		print('Não Primo')

main()



