variavel_str_01 = "Cristiano"
variavel_str_02 = "Rohling"

concatenar = variavel_str_01 + ' ' + variavel_str_02
comprimento = len(concatenar)

print(concatenar)
print(concatenar[0:4])

print(comprimento)


for i in range (0,len(concatenar)):
    print(concatenar[i])


print(concatenar.lower())
print(concatenar.upper())


texto_sujo = '       MAS QUE BELA PORCARIA             '
print(texto_sujo)
print(texto_sujo.strip())

minha_frase = 'FEAR IS THE MIND KILLER'
minha_lista = minha_frase.split(' ')
print(minha_lista)

busca = minha_frase.find('MIND')


print(busca)
#imprime da posição busca até o fim da string
print(minha_frase[busca:])


substituicao = minha_frase.replace('FEAR', 'LOVE').replace('KILLER','S MIRROR')
print(substituicao)

