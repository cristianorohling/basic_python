'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

def numeroPrimo():
    numero = int(input('Digite um número: '))
    i = 0
    primo = True

    for i in range (2, numero):
        resto = numero % i
        if resto == 0:
            primo = False    

    if primo == True:
        print(f'O número {numero} é Primo')
    else:
        print(f'O número {numero} não é Primo')

numeroPrimo()