'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 
8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''
import os

def calcula_salario_bruto():
    os.system('cls')    
    try:
        valor_hora = float(input('Qual o valor da hora trabalhada? > '))
        qtd_horas_trab = float(input('Quantas horas você trabalhou no mês? > '))
    except ValueError:
        print('Valor Inválido!')
    return (valor_hora * qtd_horas_trab)    

def calcula_salario_liquido(salario_bruto):
    valor_ir = (salario_bruto / 100) * 11
    valor_inss = (salario_bruto / 100) * 8
    valor_sind = (salario_bruto / 100) * 5
    salario_liquido = salario_bruto - valor_ir - valor_inss - valor_sind
    print('+ Salário Bruto   : R$', round(salario_bruto,2))
    print('- IR (11%)        : R$ ', round(valor_ir,2))    
    print('- INSS (8%)       : R$ ', round(valor_inss,2))
    print('- Sindicato (5%)  : R$ ', round(valor_sind,2))
    print('= Salario Liquido : R$ ', round(salario_liquido,2))        

calcula_salario_liquido(calcula_salario_bruto())