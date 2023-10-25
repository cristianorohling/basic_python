#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

import os

def anoBissexto(ano):
    if ((ano % 400) == 0):
        return(True)
    elif ((ano % 100) == 0):
        return(False)
    elif ((ano % 4) == 0):
        return(True)
    else:
        return(False)

def main():
    os.system('cls')
    print('Validador de Datas\n\n')

    data = input('Digite uma data no formato dd/mm/aaaa: ')
    dicMeses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dicNomeMes = {1:'Janeiro', 2:'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    #Verifica se a formatação  está correta (barras e 10 caracteres)
    if (data[2] != '/') or (data[5] != '/') or (len(data) != 10):
        print('Data Inválida')
    else:
        #Caso a data esteja corretamente formatada, extrair
        #dia, mes e ano.
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        #caso o ano seja bissexto, altera o diretamente dicionário dicMeses
        if anoBissexto(ano) == True:
            print(f'\nO ano {ano} é bissexto!')
            dicMeses[2] = 29
        else:
            print(f'\nO ano {ano} não é bissexto!')

        #Verifica se a variavel mes está entre 1 e 12
        if mes >= 1 and mes <= 12:
            #verifica se o dia é valido para aquele mês
            if (dia >= 1) and (dia <= dicMeses[mes]):
                print(f'\nO dia {data} ({dia} de {dicNomeMes[mes]} de {ano}) foi digitado de forma válida!')
            else:
                print(f'\nO Dia {dia} é inválido para o mês de {dicNomeMes[mes]} (dias validos: de 1 a {dicMeses[mes]}) !')           
                exit()
        else:
            print('Mes Inválido')
            exit()

if __name__ == '__main__':
    main()