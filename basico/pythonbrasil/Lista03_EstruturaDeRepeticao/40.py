'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
* Código da cidade;
* Número de veículos de passeio (em 1999);
* Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:

* Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
* Qual a média de veículos nas cinco cidades juntas;
* Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

import os

def entraCodCidade(num):
    try:
        codCidade = input(f'Digite o código da cidade {num}: ')
        while True:
            if codCidade == '':
                print('Valor não pode ser nulo!')
                codCidade = input(f'Digite o código da cidade {num}: ')
            else:
                break
    except ValueError:
        print('Digite um código alfanumérico!')
    return codCidade

def entraQtdVeiculos(num):
    try:
        veiculos = input(f'Digite o número de veículos de passeio da cidade  {num}: ')
        while True:
            if (veiculos == ''):
                print('Digite um valor válido!')
                veiculos = input(f'Digite o número de veículos de passeio da cidade  {num}: ')
            else:
                break
    except ValueError:
        print('Digite um numero inteiro válido.')
    return int(veiculos)

def entraAcidentes1999(num):
    try:
        acidentes = input(f'Digite o número de acidentes com vítimas em 1999 na cidade  {num}: ')
    except ValueError:
        print('Digite um valor inteiro válido.')
    return int(acidentes)


def mostraInfo(maiorIndiceAcidentes, cidadeMaiorIndice, menorIndiceAcidentes, cidadeMenorIndice, somaTodosAcidentes, cont, somaAcidentesCidadesPequenas, contCidadesPequenas):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\nCidade com Maior Índice de Acidentes: {cidadeMaiorIndice}')
    print(f'Número de Acidentes: {maiorIndiceAcidentes}')

    print(f'\nCidade com Menor Índice de Acidentes: {cidadeMenorIndice}')
    print(f'Número de Acidentes: {menorIndiceAcidentes}')

    print(f'\n\nMédia de Acidentes (todas as Cidades): {round(somaTodosAcidentes / cont, 2)}')

    print(f'\n\nMédia de Acidentes (Cidades com menos de 2000 veiculos): {round(somaAcidentesCidadesPequenas / contCidadesPequenas, 2)}')



def entraDados():
    maiorIndiceAcidentes = 0
    menorIndiceAcidentes = 0
    somaTodosAcidentes = 0
    somaAcidentesCidadesPequenas = 0 
    contCidadesPequenas = 0
    cidadeMaiorIndice = ''
    cidadeMenorIndice = ''
    
    for i in range(0,5):
        os.system('cls' if os.name == 'nt' else 'clear')
        cont = i + 1
        codigo = entraCodCidade(cont)
        veiculos = entraQtdVeiculos(cont)
        acidentes = entraAcidentes1999(cont)

        somaTodosAcidentes = somaTodosAcidentes + acidentes

        if acidentes > maiorIndiceAcidentes:            
            maiorIndiceAcidentes = acidentes
            cidadeMaiorIndice = codigo
        
        if menorIndiceAcidentes == 0:
            menorIndiceAcidentes = acidentes
            cidadeMenorIndice = codigo
        elif (acidentes < menorIndiceAcidentes):
            menorIndiceAcidentes = acidentes
            cidadeMenorIndice = codigo

        if veiculos <= 2000:
            somaAcidentesCidadesPequenas = somaAcidentesCidadesPequenas + acidentes
            contCidadesPequenas += 1
    
    mostraInfo(maiorIndiceAcidentes, cidadeMaiorIndice, menorIndiceAcidentes, cidadeMenorIndice, somaTodosAcidentes, cont, somaAcidentesCidadesPequenas, contCidadesPequenas)
        

entraDados()