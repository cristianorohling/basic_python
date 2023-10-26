'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

import os

def decompoeNumero(numero):
    numeroOriginal = numero
    centena = int(numero / 100)
    numero = numero - (centena * 100)
    dezena = int(numero / 10)
    numero = numero - (dezena * 10)
    unidade =  numero    
    imprimeNumeroDecomposto(numeroOriginal, centena, dezena, unidade)

def imprimeNumeroDecomposto(numeroOriginal, centena, dezena, unidade):
    stringMensagem = f'O número {numeroOriginal} pode ser decomposto em '  # Correção da variável

    # Verifica os plurais
    pluralCentena = 's' if centena > 1 else ''
    pluralDezena = 's' if dezena > 1 else ''
    pluralUnidade = 's' if unidade > 1 else ''

    if centena != 0:
        stringMensagem += f'{centena} centena{pluralCentena}'

    if dezena != 0:
        virgulaDezena = ',' if (centena != 0) else ''
        stringMensagem += f'{virgulaDezena} {dezena} dezena{pluralDezena} '
    
    eUnidade = 'e ' if ((centena != 0) or (dezena != 0))  else ''

    if unidade != 0 and (centena !=0 or dezena !=0) :
        stringMensagem += f'{eUnidade}{unidade} unidade{pluralUnidade}'
    elif unidade != 0:
        stringMensagem += f'{eUnidade}{unidade} unidade{pluralUnidade}'

    print(stringMensagem)


os.system('cls' if os.name == 'nt' else 'clear')

try:
    numero = int(input('Digite um número de 1 a 999: '))

    if (numero < 0) or (numero >= 1000):
        print('Número inválido! O valor deve estar entre 1 e 999!')
        exit()
    else:
        decompoeNumero(numero)
except ValueError:
    print('Digite um valor numérico válido!')