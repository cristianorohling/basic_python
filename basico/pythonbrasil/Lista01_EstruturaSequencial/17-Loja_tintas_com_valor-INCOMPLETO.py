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

def valor_lata_18(litros_tinta):
    latas_tinta = round((litros_tinta / 18),0)
    mod_latas_tinta = litros_tinta % 18
    if mod_latas_tinta != 0:
        latas_tinta += 1
    valor_18 = latas_tinta * 80
    print(latas_tinta, ' latas de 18 litros, totalizando R$ ', valor_18)

def valor_lata_36(litros_tinta):
    latas_tinta = round((litros_tinta / 3.6),0)
    mod_latas_tinta = litros_tinta % 3.6
    if mod_latas_tinta != 0:
        latas_tinta += 1
    valor_18 = latas_tinta * 25
    print(latas_tinta, ' latas de 3.6 litros, totalizando R$ ', valor_18)


def valor_lata_misto(litros_tinta):
    latas_tinta_grande = round((litros_tinta / 18),0)
    litros_fracionar =  (latas_tinta_grande * 18) - litros_tinta 
    print(latas_tinta_grande)
    if (litros_fracionar < 18):
        latas_pequenas = round(((litros_fracionar + ((litros_fracionar * 10)/100)) / 3.6),0)
        mod_latas_tinta_peq = (litros_fracionar + ((litros_fracionar * 10)/100)) % 3.6
        if mod_latas_tinta_peq != 0:
            latas_pequenas += 1
        print(latas_pequenas)


os.system('cls')
try:
    area_pintura = float(input('Quantos metros quadrados serão pintados? > '))
    litros_tinta = (area_pintura / 6)    
    print('Serão necessarios ', round(litros_tinta, 2), ' litros de tinta.')
    print('Opções de compra:')
    valor_lata_18(litros_tinta)    
    valor_lata_36(litros_tinta) 
    valor_lata_misto(litros_tinta)
except ValueError:
    print('Valor Inválido! Tente novamente!')