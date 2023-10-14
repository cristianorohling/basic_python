#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 

nota1 = float(input('Digite a nota da prova 1 > '))
nota2 = float(input('Digite a nota da prova 2 > '))

media = (nota1 + nota2) / 2

print('Sua media foi: ', media)

if media >=6:
    print('Aprovado')
else:
    print('Reprovado')