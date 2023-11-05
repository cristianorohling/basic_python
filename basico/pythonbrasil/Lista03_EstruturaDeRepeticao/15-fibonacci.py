#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.

nterm = int(input('Digite o n-esimo termo da sequencia de Fibonacci: '))


def imprimeTermos(cont, numero):
    print(f'{cont+1}º termo: {numero}')

termo1 = 0
termo2 = 1

for i in range(0,nterm):
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    imprimeTermos(i,termo1)