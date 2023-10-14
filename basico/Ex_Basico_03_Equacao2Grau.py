#Escreva um programa que resolva uma equação de segundo grau.   


a = int(input('entre com o valor de A: '))
b = int(input('entre com o valor de B: '))
c = int(input('entre com o valor de C: '))

delta = (b * b) - (4 * a * c)

print('Delta = ', delta)

x1 = (-b + (delta ** (1/2)))/ 2 * a
x2 = (-b - (delta ** (1/2)))/ 2 * a

print('X1 = ', x1)
print('X2 = ', x2)
