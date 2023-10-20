'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
try:
    area_pintura = float(input('Quantos metros quadrados serão pintados? > '))
    litros_tinta = area_pintura / 3
    latas_tinta = round((litros_tinta / 18),0)
    mod_latas_tinta = litros_tinta % 18

    if mod_latas_tinta != 0:
        latas_tinta += 1

    print('Serão necessárias ', latas_tinta, ' latas de tinta para cobrir ', area_pintura, ' metros quadrados de área.')
except ValueError:
    print('Valor Inválido! Tente novamente!')