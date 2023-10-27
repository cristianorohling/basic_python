#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

def parOuImpar(numero):
    if (numero % 2) != 0:
        print(f'\n\n{numero} é um número Ímpar!\n\n')
    else:
        print(f'\n\n{numero} é um número Par!\n\n')
    menu()

def positivoOuNegativo(numero):
    if numero > 0:
        print(f'\n\n{numero} é um número Positivo!\n\n')
    else:
        print(f'\n\n{numero} é um número Negativo!\n\n')
    menu()

def inteiroOuDecimal(numero):
    valorInteiro = round(numero,0)
    valorDecimal = numero - valorInteiro 
    if (valorDecimal != 0):
        print(f'\n\n{numero} é um número Decimal!\n\n')
    else:
        print(f'\n\n{numero} é um número Inteiro!\n\n')
    menu()

def menu():
    numero = float(input('Digite um número: '))
    print('\n\nO que você deseja saber sobre esse número? \n\na) Se é Par ou Ímpar? \nb) Se é Positivo ou Negativo?\nc) Se é Inteiro ou Decimal?')
    opcao = input('Digite a Opção desejada (ou digite "q" para sair): ')

    opcao = opcao.upper()

    match opcao:
        case 'A':
            parOuImpar(numero)
        case 'B':
            positivoOuNegativo(numero)
        case 'C':
            inteiroOuDecimal(numero)
        case 'Q':
            exit()

menu()

