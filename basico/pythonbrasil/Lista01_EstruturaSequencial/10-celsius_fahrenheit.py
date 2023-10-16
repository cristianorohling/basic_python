#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


C = float(input('Digite a temperatura em graus Celsius: '))
F = C * 1.8 + 32
print(C, 'graus Celsius equivalem a ', round(F,2), ' graus Fahrenheit.')
