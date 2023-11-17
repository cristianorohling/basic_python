'''
Uma academia deseja fazer um censo entre seus clientes
para descobrir o mais alto, o mais baixo, a mais gordo
e o mais magro, para isto você deve fazer um programa
que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes
'''

def entraCodigo():    
    while True:
        try:
            codigo = int(input('Digite o código numérico: '))
            return codigo
            break
        except ValueError:
            print('O código deve ser um número inteiro válido!')    

def entraAltura():
    while True:
        try:
            altura = int(input('Digite a altura em centímetros: '))       
            return(altura)     
        except ValueError:
            print('A altura deve ser um número inteiro válido!')    

def validaAltura():
    altura = 0
    while True:        
        if 100 <= altura <= 230:
            return altura
        else:            
            altura = entraAltura()

def entraPeso():
    while True:
        try:
            peso = int(input('Digite o peso em KG: '))
            return(peso)
        except ValueError:
            print('Digite o peso em valores inteiros válidos!')

def validaPeso():
    peso = 0
    while True:        
        if 30 <= peso <= 200:
            return peso
        else:            
            peso = entraPeso()

def calculaIMC(peso,altura):
    altura = altura / 100
    IMC = peso / (altura * altura)
    return round(IMC,2)

def verificaClientes(listaClientes):
    print(listaClientes)

def cadastraClientes():
    codigo = 999999999999
    num_clientes = 0    
    listaClientes = []
    
    while codigo != 0:
        print('-----------------------------------------------------')
        codigo = entraCodigo()        
        if codigo == 0:
            print('Encerramento dos cadastros...')
            break
        else:
            num_clientes += 1
            print('-----------------------------------------------------')
            print(f'Código: {codigo} - Cadastro número {num_clientes}:')
            print('-----------------------------------------------------')
            altura = validaAltura()
            peso = validaPeso()            

            # a Lista "listaClientes" contém varios dicionarios...
            novo_cliente = {"Codigo": codigo, "Altura": altura, "Peso": peso, "IMC": calculaIMC(peso,altura)}
            listaClientes.append(novo_cliente)            
            print(f'IMC: {calculaIMC(peso,altura)} ')                        
    
    verificaClientes(listaClientes)


cadastraClientes()