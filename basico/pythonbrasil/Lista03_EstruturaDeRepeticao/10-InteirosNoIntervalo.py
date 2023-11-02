#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

while True:
    try:
        a = int(input('Digite o primeiro número: '))
        b = int(input('Digite o segundo número: '))        
        break
    except ValueError:
        print('Digite um número inteiro válido!')

numeroMaior = max(a,b)
numeroMenor = min(a,b)

diferencaNumeros = numeroMaior - numeroMenor

i = numeroMenor
while i <= numeroMaior:
    print(i)
    i += 1