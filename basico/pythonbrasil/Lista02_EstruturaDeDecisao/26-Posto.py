'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: 
* até 20 litros, desconto de 3% por litro
* acima de 20 litros, desconto de 5% por litro

Gasolina:
*até 20 litros, desconto de 4% por litro
* acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que:

1) leia o número de litros vendidos
2) o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
3) calcule e imprima o valor a ser pago pelo cliente sabendo-se que:

o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90.

'''

import os

def perguntaCombustivel():
    combustivel = input('O que vai ser hoje, meu consagrado?\nTecle "A" para Álcool e "G" para Gasolina\n\n> ').lower()
    return(combustivel)

def perguntaLitros():
    try:
        litros = float(input('\nQuantos litros, meu patrão?\n\n> '))
    except ValueError:
        print('Valor Inválido!')
        perguntaLitros()
    return(litros)

def imprimeValores(valorBruto,valorDesconto):
    print(f'\nDeu R$ {round(valorBruto,2)}, mas pela nossa promoção, você vai pagar só R$ {round(valorDesconto,2)}!\nVolte sempre! ')    

def calculaAlcool(litros):
    preco_alcool = 1.90
    valorBruto = litros * preco_alcool
    #Calcula desconto
    if (litros <= 20):        
        desconto = valorBruto * 0.03
    else:
        desconto = valorBruto * 0.05
    valorDesconto = valorBruto - desconto
    imprimeValores(valorBruto,valorDesconto)

def calculaGasolina(litros):
    preco_gasolina = 2.50
    valorBruto = litros * preco_gasolina
    #Calcula desconto
    if (litros <= 20):        
        desconto = valorBruto * 0.04
    else:
        desconto = valorBruto * 0.06
    valorDesconto = valorBruto - desconto
    imprimeValores(valorBruto,valorDesconto)


def menu():
    os.system('cls')
    print('BEM VINDO AO POSTO DE COMBUSTÍVEIS!\n\n')
    combustivel = perguntaCombustivel()
    
    while combustivel != 'g' and combustivel != 'a':
        combustivel = perguntaCombustivel()

    match combustivel:
        case 'g':
            print('Certo! Você escolheu Gasolina!')
            litros = perguntaLitros()
            calculaGasolina(litros)
        case 'a':
            print('Certo! Você escolheu Álcool!')
            litros = perguntaLitros()              
            calculaAlcool(litros)


menu()