import numpy as np

def calculos(array):
    print('Maximo: ', array.max())
    print('Minimo: ', array.min())
    print('Media: ', array.mean())
    print('Desvio Padrao: ', array.std())

def povoa_lista(lista):            
    cont = 0
    while cont < 6: 
        lista[cont] = float(input(f'Digite a nota {cont + 1}: '))       
        cont = cont + 1    
    return lista

#criei uma lista com 6 zeros
lista = np.zeros(6)
#mandei povoar em uma função
povoa_lista(lista)
#entreguei a lista para uma array
array = np.array(lista)
#chamei a função que faz os calculos
calculos(array)
