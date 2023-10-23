

def imprime_maximo(max):
    print(f'Valor Máximo: {max} (resolução usando "if")')

try:
    num_01 = int(input('1º numero: '))
    num_02 = int(input('2º numero: '))
    num_03 = int(input('3º numero: '))

    if (num_01 == num_02 == num_03):
        print('Observação: os três números são iguais!')

    lista = [num_01, num_02, num_03]
    maximo = max(lista)
    print(f'Valor Máximo: {maximo} (resolução usando listas)')
    

    if (num_01 > num_02) and (num_01 > num_03):
        imprime_maximo(num_01)
    elif (num_02 > num_01) and (num_02 > num_03):
        imprime_maximo(num_02)
    elif (num_03 > num_01) and (num_03 > num_02):
        imprime_maximo(num_03)
        
except ValueError:
    print('Valores inválidos!')