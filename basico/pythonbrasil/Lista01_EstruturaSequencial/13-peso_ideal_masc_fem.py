#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas

def masc_fem():
    while True:
        sexo = input('Entre (M) para masculino e (F) para feminino > ')
        if sexo == 'M' or sexo == 'F':
            return sexo
        else:
            print('Entrada Inválida!')

def solicita_altura():
    try:
        h = float(input('Entre com sua altura em metros > '))
        return(h)
    except ValueError:
        print('Peso inválido!')

def calcula_peso_ideal(sexo, altura):
    if sexo == 'M':
        return (72.7 * altura) - 58
    elif sexo == 'F':
        return (62.1 * altura) - 44.7

sexo = masc_fem()  
altura = solicita_altura()
print('Seu peso ideal é de', round(calcula_peso_ideal(sexo,altura),2), ' kg')

        