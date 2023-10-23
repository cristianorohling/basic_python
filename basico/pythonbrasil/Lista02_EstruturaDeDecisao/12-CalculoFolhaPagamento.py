'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não
é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No
exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

import os
import sys

def calculaSalarioBruto():
        try:
                valorHora = float(input('Qual é o valor da hora trabalhada? '))
                qtdHorasTrabalhadas = float(input('Qual é a quantidade de horas trabalhadas? '))
                salarioBruto = valorHora * qtdHorasTrabalhadas
                return salarioBruto, valorHora ,qtdHorasTrabalhadas
        except ValueError:
                print('Valores Inválidos! Certifique-se de inserir números válidos.')
                sys.exit()


def calculaDescontoIr(salarioBruto):
        if salarioBruto <= 900:
                porcentagemDescontoIr = 0
        elif salarioBruto > 900 and salarioBruto <= 1500:
                porcentagemDescontoIr = 0.05
        elif salarioBruto > 1500 and salarioBruto <= 2500:
                porcentagemDescontoIr = 0.1
        elif salarioBruto > 2500:
                porcentagemDescontoIr = 0.2                
        valorDescontoIr = salarioBruto * porcentagemDescontoIr
        return valorDescontoIr, porcentagemDescontoIr


def imprimeRelatorio(salarioBruto, valorHora, qtdHorasTrabalhadas, valorDescontoIr, porcentagemDescontoIr):
        valorInss = salarioBruto * 0.1
        valorFgts = salarioBruto * 0.11
        totalDescontos = valorInss + valorDescontoIr
        print(f'Salário Bruto: ({valorHora} * {qtdHorasTrabalhadas}): R$ {salarioBruto}')
        print(f'(-) IR ({porcentagemDescontoIr * 100}%): R$   {valorDescontoIr}')  
        print(f'(-) INSS (10%) : R$  {valorInss}')
        print(f'FGTS (11%): R$  {valorFgts}')
        print(f'#Total de descontos: {totalDescontos}')
        print(f'Salário Liquido: R$  {salarioBruto - totalDescontos}')


def main():
        os.system('cls')
        dadosSalarioBruto = calculaSalarioBruto()
        salarioBruto = dadosSalarioBruto[0]
        valorHora = dadosSalarioBruto[1]
        qtdHorasTrabalhadas = dadosSalarioBruto[2]
        dadosValorPorcentagemIR = calculaDescontoIr(salarioBruto)
        valorDescontoIr = dadosValorPorcentagemIR[0]
        porcentagemDescontoIr  = dadosValorPorcentagemIR[1]
        imprimeRelatorio(salarioBruto, valorHora, qtdHorasTrabalhadas, valorDescontoIr, porcentagemDescontoIr)


# Chama a função main() para iniciar o programa
if __name__ == "__main__":
    main()