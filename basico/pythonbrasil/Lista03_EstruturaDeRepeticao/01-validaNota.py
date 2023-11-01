'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o 
usuário informe um valor válido.
'''

def solicitaNumero():
    try:
        nota = int(input('Digite uma nota entre entre 0 e 10: '))
        return nota
    except ValueError:
        print('Valor Inválido!')
        return 999

nota = solicitaNumero()

while nota < 0  or nota > 10:
    print('Numero invalido!')
    nota = solicitaNumero()

print(f'O número solicitado é {nota}')