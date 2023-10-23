#Faça um Programa que leia três números e mostre-os em ordem decrescente.



try:
    num_01 = int(input('1º numero: '))
    num_02 = int(input('2º numero: '))
    num_03 = int(input('3º numero: '))

    if (num_01 == num_02 == num_03):
        print('Observação: os três números são iguais!')

    if (num_01 > num_02) and (num_01 > num_03):
        maximo = num_01
    elif (num_02 > num_01) and (num_02 > num_03):
        maximo = num_02
    elif (num_03 > num_01) and (num_03 > num_02):
        maximo = num_03

    if (num_01 < num_02) and (num_01 < num_03):
        minimo = num_01
    elif (num_02 < num_01) and (num_02 < num_03):
        minimo = num_02
    elif (num_03 < num_01) and (num_03 < num_02):
        minimo = num_03

    if (num_01 != maximo) and (num_01 != minimo):
        meio = num_01
    elif (num_02 != maximo) and (num_02 != minimo):
        meio = num_02
    elif (num_03 != maximo) and (num_03 != minimo):
        meio = num_03

    print(f'Números em ordem decrescente: {maximo}, {meio} e {minimo}')


except ValueError:
    print('Valores inválidos!')