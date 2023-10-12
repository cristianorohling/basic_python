def real_dolar(valor, cotacao):
    resultado = valor / cotacao
    return resultado

def dolar_real(valor, cotacao):
    resultado = valor * cotacao
    return resultado

def menu():
    print('Conversor Dolar/Real')
    print('1) Dolar/Real\n2) Real/Dolar')
    
    try:
        opcao = int(input('Digite a opção desejada: '))
        
        if opcao == 1:
            valor_dolar = float(input('Digite o valor em $: '))
            resultado = dolar_real(valor_dolar, cotacao)
            print(f'Valor em reais: {resultado:.2f}')
        elif opcao == 2:
            valor_real = float(input('Digite o valor em R$: '))
            resultado = real_dolar(valor_real, cotacao)
            print(f'Valor em dólares: {resultado:.2f}')
        else:
            print('Opção inválida. Tente novamente.')
            menu()
    except ValueError:
        print('Entrada inválida. Digite um número.')
        menu()

cotacao = float(input('Digite a cotação do dólar: '))
menu()