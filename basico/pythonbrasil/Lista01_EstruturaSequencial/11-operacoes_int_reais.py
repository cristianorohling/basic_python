#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.


try:
    inteiro1 = int(input('Digite o primeiro numero inteiro: '))
    inteiro2 = int(input('Digite o segundo  numero inteiro: '))
    num_real = int(input('Digite um número real: '))
    print('O produto do dobro do primeiro com metade do segundo:')
    print((2 * inteiro1) * (inteiro2 / 2))
    print('A soma do triplo do primeiro com o terceiro:')
    print((3 * inteiro1) + inteiro2)
    print('O terceiro elevado ao cubo:')
    print(num_real ** 3)

except ValueError:
    print('Valor inválido!')


