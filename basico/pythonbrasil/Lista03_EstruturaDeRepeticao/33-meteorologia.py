#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
#programa que leia as um conjunto indeterminado de temperaturas,
#e informe ao final a menor e a maior temperaturas informadas,
#bem como a média das temperaturas.


def leTemperatura():
    temp = input('Digite a temperatura: ')
    return temp


i = 0
tempAcumulada = 0
#tempNumero = 0
tempAnterior = 0


while True:
    i += 1
    temp = leTemperatura()
    if temp.lower() == 'q':
        print('\n\nEfetuar cálculos...')
        break
    else:
        tempAnterior = tempNumero
        tempNumero = float(temp)
        tempAcumulada += tempNumero     
        if i == 1:
            tempMax = max(tempAnterior,tempNumero)    
            tempMin = min(tempAnterior,tempNumero)    
        else:
            tempMax = max(tempMax,tempNumero)
            tempMin = min(tempMin,tempNumero)
        print(f'i: {i} ant: {tempAnterior} num: {tempNumero}, max: {tempMax}, min: {tempMin} )')


print(f'Foram digitadas {i-1} temperaturas.')
print(f'A temperatura média é {round((tempAcumulada / (i - 1)),2)}.')
print(f'A temperatura máxima é {tempMax}.')
