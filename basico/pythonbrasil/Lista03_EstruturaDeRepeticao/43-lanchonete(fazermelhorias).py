'''
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

import os

def calcularValorPedido(listaLanches):
    totalPedido = 0
    print("{:<15} {:<15} {:<15}".format('Codigo', 'Qtd', 'Valor'))
    for sublista in listaLanches:        
        totalPedido = totalPedido + sublista[2]
        print("{:<15} {:<15} {:<15}".format(sublista[0], sublista[1], sublista[2]))
    print(f'\nTotal do Pedido: {round(totalPedido,2)}')


def verificaValorUnitario(codigo):
    if codigo == 100:
        return 1.20
    elif codigo == 101:
        return 1.30
    elif codigo == 102:
        return 1.50
    elif codigo == 103:
        return 1.20
    elif codigo == 104:
        return 1.30
    elif codigo == 105:
        return 1.00

def escolherLanches():
    codigo = 9999999999
    listaLanches = []
    while codigo != 0:
        mostraCardapio()
        codigo = int(input('Digite o código do lanche (ou "0" para encerrar o pedido): '))        
        if (codigo != 0):            
            if  (codigo in [100, 101, 102, 103, 104, 105]):
                qtd = int(input('Digite a quantidade: '))     
                valorUnitario = verificaValorUnitario(codigo)                               
                valorTotalCodigo = valorUnitario * qtd
                listaLanches.append([codigo,qtd,valorTotalCodigo])
            else:
                print('Código inválido!')
        else:
            print('Pedido encerrado!')
            calcularValorPedido(listaLanches)

def mostraCardapio():
    print('Especificação   Código  Preço')
    print('Cachorro Quente 100     R$ 1,20')
    print('Bauru Simples   101     R$ 1,30')
    print('Bauru com ovo   102     R$ 1,50')
    print('Hambúrguer      103     R$ 1,20')
    print('Cheeseburguer   104     R$ 1,30')
    print('Refrigerante    105     R$ 1,00')    

def iniciar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nSeja bem vindo à nossa lanchonete!\nSiga as instruções na tela para solicitar seu lanche.')
    
    while True:
        pedido = input('Deseja fazer um pedido (s/n)? ').lower()
        if pedido == 'n':
            print('Até logo!')    
            break
        elif pedido == 's':
            print('Ótimo! Vamos dar uma olhada no nosso cardápio.\n')             
            escolherLanches()
            break
        else:
            print('Opção inválida! Por favor, digite "s" para sim ou "n" para não.')       



iniciar()

