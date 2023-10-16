#Faça um Programa que converta metros para centímetros.


def metros_centimetros(valor):
    return valor*100
    
def centimetros_metros(valor):
    return valor/100

def define_funcao(tipo):
    try:
        valor = float(input('Digite o valor a ser convertido > '))
        match tipo:
            case 1:
                print(valor, 'centímetros é igual a ', centimetros_metros(valor), 'metro(s)!')
            case 2:
                print(valor, 'metros é igual a ', metros_centimetros(valor), 'centímetro(s)!')
    except ValueError:
        print('Valor inválido!')
        menu()    
    
            
    
def menu():
    print('Escolha o tipo de conversão: \n1) Centímetros -> Metros \n2) Metros -> Centímetros')    

    try:
        tipo = int(input('Escolha > '))
        match tipo:
            case 1:
                print('Você escolheu Centímetros para Metros!')

            case 2:
                print('Você escolheu Metros para Centímetros!')    
            case _:
                print('Digite uma opção válida!')    
                menu()
        define_funcao(tipo)
    except ValueError:
        print('Caractere inválido! Tente novamente!')
        menu()


menu()

