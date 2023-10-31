'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
(COMO OS DESCONTOS NÃO FAZIAM MUITO SENTIDO, ALTEREI O EXERCICIO PARA DAR 10% DE DESCONTO ACIMA DE 5KG DE CARNE)

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário 
e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

import os

def checkOut(tipo, kgCarne, valor, valorTotal):
    cartaoTabajara = input('\n\nDeseja usar o Cartão Tabajara?\nEm caso afirmativo, você terá ainda mais 5% de desconto!\nDigite "S" ou "N": ').lower()
    match cartaoTabajara:
        case 's':
            desconto = valorTotal * 0.01
            valorComDesconto = valorTotal - desconto
            print(f'\nCupom fiscal:\nTipo de Carne {tipo}  | Kg: {kgCarne} | Valor Kg:  {valor:.2f} | Valor Total: {valorTotal:.2f}| Desconto Tabajara: {desconto:.2f}|  Preço Total: {valorComDesconto:.2f}')
        case 'n':
            print(f'\nCupom fiscal:\nTipo de Carne {tipo}  | Kg: {kgCarne} | Valor Kg:  {valor:.2f} | Preço Total: {valorTotal:.2f}')
        case '_':
            print('Opção inválida!')
            checkOut()
        

def fazerCompra(tipo, valor):
    print(f'\n\nExcelente escolha! {tipo} está por R$ {valor:.2f}.\nNa nossa promoção, estamos oferecendo ainda mais 10%\nde desconto se você comprar acima de 5 kg.')
    kgCarne = float(input('\nQuantos quilos você vai levar hoje?\n> '))
    if kgCarne > 5:
        desconto = valor * 0.1
        valorComDesconto = valor - desconto 
        valorTotal = kgCarne * valorComDesconto       
        print(f'Como você pediu acima de 5 kg, o Kg sairá de R$ {valor:.2f} por R$ {valorComDesconto:.2f}')
        valorTotal = kgCarne * valorComDesconto
        checkOut(tipo, kgCarne, valorComDesconto, valorTotal)
    else:
        print(f'Como você pediu menos de 5 kg (ou exatamente 5kg), o quilo sairá pelo preço normal, que é R$ {valor:.2f}')
        valorTotal = kgCarne * valor
        checkOut(tipo, kgCarne, valor, valorTotal)
    

def menu():
    os.system('cls')
    print('Bem vindo ao açougue do Supermercado Tabajara.\n\nEscolha o que vai querer levar hoje e aproveite nossas promoções!')
    print('a) Filé Duplo\nb) Alcatra\nc) Picanha')
    opcao = input('> ').lower()

    match opcao:
        case 'a':
            fazerCompra('Filé Duplo', 22.85)
        case 'b':
            fazerCompra('Alcatra', 28.50)
        case 'c':
            fazerCompra('Picanha', 59.99)
        case '_':
            print('Valor inválido!')

menu()

    