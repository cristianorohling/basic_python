#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calcula_media(a, b, c, d):
    print((a + b + c + d) / 4)

def entrada_notas():
    try:
        bim1 = float(input('Digite a nota do 1º Bimestre: '))
        bim2 = float(input('Digite a nota do 2º Bimestre: '))
        bim3 = float(input('Digite a nota do 3º Bimestre: '))
        bim4 = float(input('Digite a nota do 4º Bimestre: '))
    except ValueError:
        "Valor Inválido!"    
    if (bim1 > 100) or (bim2 >100) or (bim3>100) or (bim4>100):
        print('Valor maior que 100!')
    else:
        calcula_media(bim1, bim2, bim3, bim4)

entrada_notas()
