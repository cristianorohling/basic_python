def menu():
	print('Conversor Dolar/Real')
	print('1) Dolar/Real\n2) Real/Dolar')
	opcao = int(input('Digite a opcao desejada: '))
	if opcao == 1:
		dolar_real(float(input('Digite o valor em $: ')))
	else:
		if opcao == 2:
			real_dolar(float(input('Digite o valor em R$: ')))
		else:
			menu()

def real_dolar(valor):
	print('Valor em dolares:' + str(round(valor/cotacao, 2)))
	
def dolar_real(valor):
	print('Valor em reais:'+ str(round(cotacao*valor, 2)))
	

cotacao =float(input('Digite a cotacao do dólar: '))
menu()