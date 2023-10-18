#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente. 

#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.
try:
    quilos = float(input('Quantos Quilos de Peixe foram pescados: '))
    print(f'João apanhou {quilos} Kg de peixe.')
    excesso = quilos - 50
    if excesso > 0:
        print(f'Houve um excesso de {excesso} Kg de peixe.')
        multa = excesso * 4
        print(f'João pagará uma multa de R$ {multa} pelos quilos excedentes!')
    else:
        multa = 0
        print('Não houve excesso de peso.\nJoão não pagará uma multa pelos quilos excedentes.')
except ValueError:
    print('Valor inválido! Digite um valor em KG!')









