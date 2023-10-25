#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Digite uma data no formato dd/mm/aaaa:\n\n ')

dicMeses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if (data[2] != '/') and (data[5] != '/'):
    print('Data Inválida')
else:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    if mes >= 1 and mes <= 12:
        print('Mes Válido')
    else:
        print('Mes Inválido')



print(dia)
print(mes)
print(ano)