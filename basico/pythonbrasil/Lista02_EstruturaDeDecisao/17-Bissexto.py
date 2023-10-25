#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
#* Um ano é bissexto se for divisível por 4.
#* No entanto, anos divisíveis por 100 não são bissextos, a menos que sejam divisíveis por 400.

def anoBissexto(bissexto):
    if bissexto == True:
        print('Ano Bissexto!')
    else:
        print('Ano não Bissexto!')

try:
    ano = int(input('Digite o ano: '))

    if ((ano % 400) == 0):
        anoBissexto(True)
    elif ((ano % 100) == 0):
        anoBissexto(False)
    elif ((ano % 4) == 0):
        anoBissexto(True)
    else:
        anoBissexto(False)
except ValueError:
    print('Digite um ano válido!')