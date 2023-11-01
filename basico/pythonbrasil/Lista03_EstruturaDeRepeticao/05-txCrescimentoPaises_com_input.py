'''
Supondo que a população de um país 
A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 

Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

def entraPopulacao(pais):
    while True:
        try:
            populacao = int(input(f'Digite a população do país {pais}: '))    
            if populacao > 0:
                return populacao
            else:
                 print(f'A população do país {pais} deve ser maior que zero.')
        except ValueError:
            print('Valor Inválido! Digite um número inteiro maior que zero!')

def entraTxCrescPais(pais):
    while True:
        try:
            txCrescAno = (float(input(f'Digite a taxa de crescimento do país {pais} (em %): '))) / 100
            if txCrescAno != 0:
                return txCrescAno
            else:
                print('Digite um numero maior que zero!')
        except ValueError:
            print('Valor Inválido!')
    return txCrescAno

def verificaQuantosAnos(populacaoA,populacaoB,txCrescAnoA,txCrescAnoB):
    anos = 0
    while populacaoA < populacaoB:
        populacaoA = populacaoA + populacaoA * txCrescAnoA
        populacaoB = populacaoB + populacaoB * txCrescAnoB
        print(f'Ano: {anos}\nPopulação de A: {populacaoA:.2f}\nPopulação de B: {populacaoB:.2f}\n')    
        anos += 1

    print(f'Em {anos} anos, a população do país A será maior ou igual que a do país B')

def entradaDados():
    populacaoA = entraPopulacao('A')
    txCrescAnoA = entraTxCrescPais('A')
    populacaoB = entraPopulacao('B')
    txCrescAnoB = entraTxCrescPais('B')
    verificaQuantosAnos(populacaoA,populacaoB,txCrescAnoA,txCrescAnoB)

entradaDados()