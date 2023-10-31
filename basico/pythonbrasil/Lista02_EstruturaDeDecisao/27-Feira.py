'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
import os

listaCompras = []

def caixaFrutaria():
    global listaCompras
    kgTotal = 0
    vlrTotal = 0

    for i in listaCompras:
        fruta, kgFrutas, valor = i
        print(f'Fruta: {fruta}, Kg: {kgFrutas}, Valor Total: {valor}')
        kgTotal = kgTotal + kgFrutas
        vlrTotal = vlrTotal + valor
    
    print(f'Você comprou {kgTotal} kg de frutas, totalizando R$ {vlrTotal}')
    if (kgTotal > 8) or (vlrTotal > 25):        
        desconto = vlrTotal * 0.1
        print(f'\n\nComo você é nosso cliente premium, você terá um desconto\nde 10% totalizando {desconto}, então você só pagará R$ {vlrTotal - desconto}!')

def gravaCompra(opcao, kgFrutas, valor):
    global listaCompras
    compra = [opcao, kgFrutas, valor]
    listaCompras.append(compra)
    print(f'Compra registrada: {kgFrutas} kg de {opcao} por R$ {valor:.2f}')
    menu()

def perguntaKg():
    kgFrutas = float(input('Quantos quilos vai querer, patrão?\n> '))
    return kgFrutas

def comprarFrutas(opcao):
    if opcao == 'a':
        print('\n\nO morango está em promoção!\nAté 5 kg, você paga R$ 2,50.\nAcima de 5kg, o preço cai para R$ 2,20 por quilo!')
        kgFrutas = perguntaKg()
        if kgFrutas < 5:
            valor = kgFrutas * 2.5
        elif kgFrutas >= 5:
            valor = kgFrutas * 2.2
        print(f'Valor Total: {kgFrutas} kg sairão por R$ {round(valor,2)}!')
        gravaCompra('Morango',kgFrutas,valor)
    elif opcao == 'b':
        print('\n\nA maçã está em promoção!\nAté 5 kg, você paga R$ 1,80.\nAcima de 5kg, o preço cai para R$ 2,20 por quilo!')
        kgFrutas = perguntaKg()
        if kgFrutas < 5:
            valor = kgFrutas * 1.8
        elif kgFrutas >= 5:
            valor = kgFrutas * 1.50
        print(f'Valor Total: {kgFrutas} kg sairão por R$ {round(valor,2)}!')
        gravaCompra('Maçã',kgFrutas,valor)

def menu():    
    print('\n\nBem vindo à nossa frutaria!\n\nFaça sua escolha:\na) Comprar Morangos\nb) Comprar Maçãs\nc) Ir para o caixa')
    opcao = input('> ').lower()
    match opcao:
        case 'a':
            comprarFrutas(opcao)
        case 'b':
            comprarFrutas(opcao)
        case 'c':
            caixaFrutaria()
        case '_':
            print('Opção inválida!')


os.system('cls')
menu()
