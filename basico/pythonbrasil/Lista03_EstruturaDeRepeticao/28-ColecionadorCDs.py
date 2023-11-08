'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade 
de CDs e o valor para em cada um.
'''

valorTotal = 0
try:
    qtdCDs = int(input('Digite quantos CDs há na coleção: '))
except ValueError:
    print('Digite um valor inteiro válido!')

for i in range(0,qtdCDs):
    try:
        valor = float(input(f'Digite quanto custou o CD {i+1}: '))
    except ValueError:
        print('Digite um preço válido!')
    valorTotal = valorTotal + valor

print(f'\n\nO colecionador tem {qtdCDs} CDs, e a coleção custou {valorTotal}.\n\nO valor médio de cada CD é de {valorTotal/qtdCDs}')