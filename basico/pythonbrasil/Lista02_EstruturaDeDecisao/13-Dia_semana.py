#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

try:
    diaNum = int(input('Digite o número correspondente ao dia (de 1 a 7): '))

    match diaNum:
        case 1: 
            print('Domingo')
        case 2: 
            print('Segunda-feira')
        case 3: 
            print('Terça-feira')
        case 4: 
            print('Quarta-feira')
        case 5: 
            print('Quinta-feira')
        case 6: 
            print('Sexta-feira')
        case 7: 
            print('Sábado')
        case _:
            print('Valor Inválido!')
except ValueError:
    print('Valor inválido! Digite um número de 1 a 7!')