def cria_chave_codigo():
    alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chave    = list('ZYXWVUTSRQPONMLKJIHGFEDCBA')
    dicionario = dict(zip(alfabeto, chave))
    print(dicionario)
    return dicionario   

def codificador(chave_codigo, codificar):
    texto_codificado = ''
    chave = chave_codigo
    texto_normal = codificar

    for i in texto_normal:
        if i in chave_codigo:
            texto_codificado = texto_codificado + chave[i]
        else:
            texto_codificado = texto_codificado + i
    return texto_codificado  

chave_codigo = cria_chave_codigo()
codificar = input('Digite um texto a ser codificado: ').upper()
texto_codificado = codificador(chave_codigo, codificar)
print(texto_codificado)