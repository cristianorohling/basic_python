#Faça um Programa que peça dois números e imprima o maior deles.

def imprime_resultado(x,y):
    print(f'Maior número: {x}')

try:
    a = int(input('Digite o primeiro valor inteiro > '))
    b = int(input('Digite o segundo valor inteiro > '))
    if (a > b):
        imprime_resultado(a)
    else:
        imprime_resultado(b)
except ValueError:
    print('Entre com valores válidos!')