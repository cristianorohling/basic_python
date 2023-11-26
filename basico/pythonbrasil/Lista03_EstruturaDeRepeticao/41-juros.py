'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

'''

import os

vlrInicial = 1000
vlrJuros = 0
qtdParc = 0
valorParc = 0


def calculaJuros(vlrInicial, qtdParc):
    if qtdParc == 1:
        porcJuros = 0
    elif qtdParc == 3:
        porcJuros = 10/100
    elif qtdParc == 6:
        porcJuros = 15/100
    elif qtdParc == 9:
        porcJuros = 20/100
    elif qtdParc == 12:
        porcJuros = 25/100    
    vlrJuros = vlrInicial * porcJuros
    return(vlrJuros)

def printaCabecalho():    
    os.system('cls' if os.name == 'nt' else 'clear')
    strVlrDivida = 'Vlr Dívida'
    strVlrJuros = 'Vlr Juros'
    strQtdParc  = 'Qtd Parcelas'
    strVlrParc = 'Vlr Parcela'  
    print(f'{strVlrDivida:<18} {strVlrJuros:<20} {strQtdParc:<25} R$ {strVlrParc}')

printaCabecalho()
for qtdParc in range (1,13):
    if qtdParc in [1, 3, 6, 9, 12]:
        vlrJuros = calculaJuros(vlrInicial, qtdParc)
        vlrDivida = round(vlrInicial + vlrJuros,2)
        vlrParc = round(vlrDivida/qtdParc,2)
        #print(f'R$ {vlrDivida}        {round(vlrJuros,2)}        {qtdParc}        {vlrParc}')  /// jeito que eu fiz primeiro    
        print(f'R$ {vlrDivida:<15} {round(vlrJuros, 2):<20} {qtdParc:<25} R$ {vlrParc}')
