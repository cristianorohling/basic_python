#Faça um Programa que peça dois números e imprima a soma.

def soma(a,b):
    print(a + b)    

def entrada():
    try:
        a = float(input('Digite o primeiro numero: '))
        b = float(input('Digite o primeiro numero: '))
        soma(a, b)
    except ValueError:
        print('Valor inválido!')

entrada()