#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 1280,00 (incluindo) : aumento de 20%
#salários entre R$ 1280,00 e R$ 1700,00 : aumento de 15%
#salários entre R$ 1700,00 e R$ 2500,00 : aumento de 10%
#salários de R$ 2500,00 em diante : aumento de 5% 

#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

import os

os.system('cls')

try:
    nome = input('Digite o nome do colaborador: ')
    salario_antigo = float(input('Digite o salario do colaborador: '))

    if salario_antigo <= 1280:
        reajuste = salario_antigo * 0.2
        percentual = '20%'
    elif salario_antigo > 1280 and salario_antigo <= 1700:
        reajuste = salario_antigo * 0.15
        percentual = '15%'
    elif salario_antigo > 1700 and salario_antigo <= 2500:
        reajuste = salario_antigo * 0.1
        percentual = '10%'
    elif salario_antigo > 2500:
        reajuste = salario_antigo * 0.05
        percentual = '5%'

    print(f'Colaborador: {nome}')
    print(f'Salario: {salario_antigo:.2f}')
    print(f'Percentual de Reajuste: {percentual}')
    print(f'Valor de Reajuste: {reajuste:.2f}')
    print(f'Salario reajustado: {(salario_antigo + reajuste):.2f}')
except ValueError:
    print('Valores inválidos!')


