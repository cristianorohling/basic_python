'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais 
sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''



def imprimeSalario(ano, salario):
    print(f'Ano: {ano}: - Salario: {round(salario,2)}')

def calculaSalario(salario, percentual):
    return salario + (salario * percentual)


ano_inicial = 1995
ano_atual = 2002
percentual = 0.015

for ano in range(ano_inicial,ano_atual+1):
    if ano == 1995:
        salario = 1000
        imprimeSalario(ano,salario)
    elif ano == 1996:        
        salario = calculaSalario(salario,percentual)
        imprimeSalario(ano,salario)
    elif ano > 1996:
        percentual = percentual * 2
        salario = calculaSalario(salario,percentual)
        imprimeSalario(ano,salario)