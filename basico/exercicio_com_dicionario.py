meu_dicionario = {'A': 'Ameixa', 'B': 'Bola', 'C': 'Cachorro'}

#imprime tudo
print(meu_dicionario)

#imprime um elemento
print(meu_dicionario['A'])

#navegação
for chave in meu_dicionario:
    print(meu_dicionario[chave])

#converte dicionario em tupla
for i in meu_dicionario.items():
    print(i)


#mostra so os valores
for i in meu_dicionario.values():
    print(i)


#mostra so as chave
for i in meu_dicionario.keys():
    print(i)