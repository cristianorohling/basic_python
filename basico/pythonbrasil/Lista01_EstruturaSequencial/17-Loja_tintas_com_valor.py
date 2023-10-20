'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 
ou em galões de 3,6 litros, 
que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor. 
* Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
'''
import os

def valor_lata_18(litros_tinta, preco_lata_18):
    latas_tinta = int(round((litros_tinta / 18),0))
    mod_latas_tinta = litros_tinta % 18
    if mod_latas_tinta != 0:
        latas_tinta += 1
    valor_18 = latas_tinta * preco_lata_18
    print(f'* {latas_tinta} latas de 18 litros, totalizando R$ {valor_18:.2f}')

def valor_lata_36(litros_tinta, preco_lata_36):
    latas_tinta = int(round((litros_tinta / 3.6),0))
    mod_latas_tinta = litros_tinta % 3.6
    if mod_latas_tinta != 0:
        latas_tinta += 1
    valor_36 = latas_tinta * preco_lata_36
    print(f'* {latas_tinta} latas de 3.6 litros, totalizando R$ {valor_36:.2f}')

def valor_lata_misto(litros_tinta, preco_lata_18, preco_lata_36):
    latas_tinta_grande = int(round((litros_tinta / 18),0))
    litros_excedentes =  (latas_tinta_grande * 18) - litros_tinta
    latas_tinta_pequenas = round((litros_excedentes / 3.6),0)
    mod_latas_pequenas = litros_excedentes % 3.6    
    if (mod_latas_pequenas != 0):
        latas_tinta_pequenas += 1
    valor_misto = (latas_tinta_grande * preco_lata_18) + (latas_tinta_pequenas * preco_lata_36)    
    print(f'* {latas_tinta_grande} latas de 18 litros e {latas_tinta_pequenas} latas de 3.6 litros, totalizando {valor_misto:.2f}')

os.system('cls')

print('********************************************************************************')
print('**                              MANECO TINTAS                                 **')
print('********************************************************************************')
print('              Quantidade de Latas de Tinta por Metro Quadrado')
print('********************************************************************************')

preco_lata_18 = 80
preco_lata_36 = 25

try:    
    area_pintura = float(input('Quantos metros quadrados serão cobertos? > '))
    litros_tinta = (area_pintura / 6)    
    litros_tinta_folga = litros_tinta + litros_tinta *  0.10
    print('********************************************************************************')
    print('QUANTIDADE: São necessários ', round(litros_tinta, 2), ' litros de tinta para cobertura desta área.')
    print('Recomenda-se comprar 10% a mais, então consideraremos ', round(litros_tinta_folga, 2), ' litros.')
    print('********************************************************************************')
    print('                        Opções disponíveis para compra:')
    print('********************************************************************************')
    valor_lata_misto(litros_tinta_folga, preco_lata_18, preco_lata_36)
    valor_lata_18(litros_tinta_folga, preco_lata_18)   
    valor_lata_36(litros_tinta_folga, preco_lata_36) 
except ValueError:
    print('Valor Inválido! Tente novamente!')
