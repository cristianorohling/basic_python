'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
'''

numero = int(input('Digite um número:'))

def verificaPrimo(numero):
    primo = True
    for i in range(2,numero):
        resto = numero % i
        if resto == 0:
            primo = False
    return primo

listaString = ' '

for i in range(2,numero + 1):
    numeroPrimo = verificaPrimo(i)
    if numeroPrimo == True and i < numero + 1:
        listaString = listaString + str(i) + ' '    
    
print(f'Os números primos entre 1 e {str(numero)} são: \n{listaString}')

    
