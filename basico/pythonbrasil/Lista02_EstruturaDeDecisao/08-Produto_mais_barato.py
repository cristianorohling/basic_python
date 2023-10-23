import os

os.system('cls')

def imprime_minimo(max, nome_prod):
    print(f'Mais Barato: produto "{nome_prod}", valor de R$ {max}')

try:
    nome_produto1 = input('Digite o nome do 1º produto: ')
    preco_01 = int(input(f'Preco do produto "{nome_produto1}": '))
    
    nome_produto2 = input('Digite o nome do 2º produto: ')
    preco_02 = int(input(f'Preco do produto "{nome_produto2}": '))

    nome_produto3 = input('Digite o nome do 3º produto: ')
    preco_03 = int(input(f'Preco do produto "{nome_produto3}": '))
    
    if (preco_01 == preco_02 == preco_03):
        print(f'Os produtos "{nome_produto1}", "{nome_produto2}" e "{nome_produto3}" tem valores iguais.\nTodos custam R$ {preco_01}')
    elif (preco_01 < preco_02) and (preco_01 < preco_03):
        imprime_minimo(preco_01, nome_produto1)
    elif (preco_02 < preco_01) and (preco_02 < preco_03):
        imprime_minimo(preco_02, nome_produto2)
    elif (preco_03 < preco_01) and (preco_03 < preco_02):
        imprime_minimo(preco_03, nome_produto3)


except ValueError:
    print('Valores inválidos!')