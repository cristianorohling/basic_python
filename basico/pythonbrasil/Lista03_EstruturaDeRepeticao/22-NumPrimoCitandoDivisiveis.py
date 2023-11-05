'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais números ele é divisível.
'''

import math
import os
							
def verificaPrimo(numero):
	listaDivisiveis = []	
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
				listaDivisiveis.append(i)
				primo = False
	print(f'Divisível por: {listaDivisiveis}')
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



