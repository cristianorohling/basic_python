#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

try:
    raio = float(input('Digite o raio do circulo: '))
    print('A área do círculo é ', round((math.pi * raio*raio),2))
except ValueError:
    print('O valor digitado não é válido!')