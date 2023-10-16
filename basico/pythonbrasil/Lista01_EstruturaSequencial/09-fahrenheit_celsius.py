#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.


F = float(input('Digite a temperatura em graus Fahrenheit: '))
C = 5 * ((F-32) / 9)
print(F, 'graus Fahrenheit equivalem a ', round(C,2), ' graus Celsius.')
