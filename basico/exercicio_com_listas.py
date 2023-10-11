import pandas

def imprime_lista(lista):    
    for i in range(len(lista)):
        print(lista[i])

def imprime_separador():
    print('*************************************')

#criação de listas
minha_lista = ['abacaxi','melancia','abacate','ameixa','blueberry']
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]
minha_lista_4 = []

#chamo a funcao para imprimir minha_lista
imprime_lista(minha_lista)
imprime_separador()

#Append: apenas um elemento por vez
minha_lista.append('tamarindo')
minha_lista.append('limao')
minha_lista.append('maracujá')

#chamo a funcao para imprimir minha_lista
imprime_lista(minha_lista)
imprime_separador()


numero = int(input('Digite um numero: '))

if numero in minha_lista_2:
    print('Tem!')
else:
    print('Tem não!')

#remover itens
del minha_lista[2:]

imprime_separador()

#chamo a funcao
imprime_lista(minha_lista)