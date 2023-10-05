def complementa_musica(vogal):
    vogal_dict = {
        'a': "Não deixa o cabelo do saco enrolar",
        'e': "Não deixa o cabelo do saco de pé",
        'i': "Não deixa o cabelo do saco cair",
        'o': "Não deixa o cabelo do saco dar nó",
        'u': f"Não deixa o cabelo do saco enrolar com os do c{vogal}"
    }
    if vogal in vogal_dict:
        return vogal_dict[vogal]
    return ""

def monta_musica(lista):
    for elemento in lista:
        for _ in range(2):
            print(f"Sabao Cr{elemento}-Cr{elemento}")
        complemento = complementa_musica(elemento)
        if complemento:
            print(complemento)

if __name__ == "__main__":
    vogais = ['a', 'e', 'i', 'o', 'u']
    monta_musica(vogais)
