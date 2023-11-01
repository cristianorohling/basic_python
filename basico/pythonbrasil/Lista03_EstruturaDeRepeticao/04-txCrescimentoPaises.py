'''
Supondo que a população de um país 
A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 

Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

populacaoA = 80000
txCrescAnoA = 0.03

populacaoB = 200000
txCrescAnoB = 0.015

anos = 0

while populacaoA < populacaoB:
    populacaoA = populacaoA + populacaoA * txCrescAnoA
    populacaoB = populacaoB + populacaoB * txCrescAnoB
    print(f'Ano: {anos}\nPopulação de A: {populacaoA:.2f}\nPopulação de B: {populacaoB:.2f}\n')    
    anos += 1

print(f'Em {anos} anos, a população do país A será maior ou igual que a do país B')