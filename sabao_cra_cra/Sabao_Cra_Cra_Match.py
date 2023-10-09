def monta_musica(lista):
    for elemento in lista:
        cont = 0
        while cont < 2:
            print("Sabao Cr" + elemento + "-Cr" + elemento)
            cont += 1
        complementa_musica(elemento)

def complementa_musica(vogal):
    match vogal: 
        case 'a':
            print("Não deixa o cabelo do saco enrolar")
        case 'e':
            print("Não deixa o cabelo do saco de pé")
        case 'i':
            print("Não deixa o cabelo do saco cair")
        case 'o':
            print("Não deixa o cabelo do saco dar nó")
        case 'u':
            print("Não deixa o cabelo do saco enrolar com os do c" + vogal)                    

vogais = ['a', 'e', 'i', 'o' , 'u']
monta_musica(vogais)