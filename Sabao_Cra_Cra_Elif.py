def monta_musica(lista):
    for elemento in lista:
        cont = 0
        while cont < 2:
            print("Sabao Cr" + elemento + "-Cr" + elemento)
            cont += 1
        complementa_musica(elemento)

def complementa_musica(vogal):
    if vogal == 'a':
        print("Não deixa o cabelo do saco enrolar")
    elif vogal == 'e':
        print("Não deixa o cabelo do saco de pé")
    elif vogal == 'i':
        print("Não deixa o cabelo do saco cair")
    elif vogal == 'o':
        print("Não deixa o cabelo do saco dar nó")
    elif vogal == 'u':
        print("Não deixa o cabelo do saco enrolar com os do c" + vogal)
                    

vogais = ['a', 'e', 'i', 'o' , 'u']
monta_musica(vogais)