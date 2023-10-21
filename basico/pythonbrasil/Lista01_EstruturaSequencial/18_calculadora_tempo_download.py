#Faça um programa que peça o tamanho de um arquivo para download (em MB) 
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

import os

os.system('cls')

try:
    tamanho_arquivo = float(input('Qual é o tamanho do arquivo em Mb? > '))
    velocidade_link = float(input('Qual é a velocidade do link de internet, em Mbps? > '))
    tempo_download_min = (tamanho_arquivo / velocidade_link) / 60
    tempo_download_seg = (tamanho_arquivo / velocidade_link) 
    print(f'A estimativa é que o arquivo seja baixado em {round(tempo_download_min,3)} minutos, ou aproximadamente {round((tempo_download_seg),0)} segundos!')
except ValueError:
    print('Digite valores válidos!')