'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

'''

import math
import os

divisoes = 0
							
def verificaPrimo(numero):	
	global divisoes
	listaDivisiveis = []	
	primo = True
	if numero <= 1:
		primo = False
	elif numero == 2:
		primo = True
	else:
		raiz = math.ceil(numero ** 0.5)
		for i in range(2,raiz+1):
			divisoes += 1
			verifica = numero % i
			if verifica == 0:
				listaDivisiveis.append(i)
				primo = False
	return primo

os.system('cls')
print('Este programa verifica todos os números primos entre 1 e o número que você digitar.')
numeroLimite = int(input('Digite o número > '))

listaPrimos = []

for i in range(1, numeroLimite+1):
	teste = verificaPrimo(i)
	if teste == True:
		listaPrimos.append(i)
	
print(listaPrimos)
print(f'\n\nForam necessárias {divisoes} divisões para chegar a essa lista.')
