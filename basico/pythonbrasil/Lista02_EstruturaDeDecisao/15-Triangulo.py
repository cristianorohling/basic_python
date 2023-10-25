'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
A soma de cada dois lados deve ser maior que o terceiro lado. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

try:
    A = float(input('Digite a medida do 1º lado do triangulo: '))
    B = float(input('Digite a medida do 2º lado do triangulo: ' ))
    C = float(input('Digite a medida do 3º lado do triangulo: ' ))

    if (((A + B) > C) and ((B + C) > A) and ((A + C) > B)):
        print('Triângulo Válido!')
        if (A == B == C):
            print('Triângulo Equilátero!')
        elif (A != B != C):
            print('Triangulo Escaleno')
        elif (A == B) or (A == C) or (B == C):
            print('Triângulo Isósceles')
    else:
        print('Triângulo Inválido!')
except ValueError:
    print('Medida inválida! Digite um número válido.')