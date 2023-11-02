#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
a = 1
listaImpares = []

while a <= 50:
    if (a % 2) != 0:
        print(a)
        listaImpares.append(a)
    a += 1

print(listaImpares)