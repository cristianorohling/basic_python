def entrada_dados():
    Num_01 = input('Digite o primeiro numero: ')
    Operador = input('Digite o operador: ')
    Num_02 = input('Digite o segundo numero: ')
    lista_operacao = [Num_01, Num_02, Operador]
    return lista_operacao

def valida_dados(lista_operacao):
    try:
        Num_01 = float(lista_operacao[0])
        Num_02 = float(lista_operacao[1])
        Operador = lista_operacao[2]       
        match Operador:
            case '+':
                Operador = '+'
            case '-':
                Operador = '-'
            case '*':
                Operador = '*'
            case '/':
                Operador = '/'
            case _:
                Operador = 'Invalido'
    except ValueError:
        print('Valores inválidos!')
        lista_operacao = entrada_dados()                
    lista = [Num_01,Num_02,Operador]
    return lista

def realiza_operacao(lista_validada):
    match lista_validada[2]:
        case 'Invalido':
            print('Operador Inválido!')
        case '+':
            print(lista_validada[0] + lista_validada[1])
        case '-':
            print(lista_validada[0] - lista_validada[1])
        case '*':
            print(lista_validada[0] * lista_validada[1])
        case '/':
            print(lista_validada[0]  / lista_validada[1])
    
        


lista_operacao = entrada_dados()
lista_validada = valida_dados(lista_operacao)
realiza_operacao(lista_validada)


