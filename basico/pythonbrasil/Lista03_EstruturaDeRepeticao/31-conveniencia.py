'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido 
de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar 
o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''

import os

os.system('cls' if os.name == 'nt' else 'clear')

contador = 1
valorTotal = 0
recebePreco = 9999999999

while recebePreco != 0:
    try:
        recebePreco = float(input(f'Produto {contador}: R$ '))
        valorTotal = valorTotal + recebePreco    
        contador += 1        
    except ValueError:
        print('Digite um valor numérico!')
print(f'Total: R$ {valorTotal}')        

while True:
    try:        
        valorDinheiro = float(input('Digite o valor em dinheiro fornecido pelo cliente: '))
        if valorDinheiro < valorTotal:
            print(f'Você me deu R$ {valorDinheiro}, então faltam {valorTotal-valorDinheiro} para o valor Total, que é {valorTotal}')        
        else:
            troco = valorDinheiro - valorTotal
            print(f'Troco: {troco}')
            break
    except ValueError:
        print('Digite um valor numérico!')



