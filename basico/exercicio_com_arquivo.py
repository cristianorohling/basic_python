# coding=<utf-8>
arq = open('./basic_python/arquivo.txt')

#printa apenas informacoes do arquivo
print(arq)

#le todas as linhas e cria uma lista
linhas = arq.readlines()

#observe que ele vai imprimir como uma lista, acrescentando \n para substituir as quebras de linha
print(linhas)

for i in linhas:
    print(i)

#abre todo o texto
texto_full = arq.read()
print(texto_full)


#criar arquivo
file = open('./basic_python/arquivo_criado.txt','w')
file.write('Este é o arquivo que eu criei com Python')
file.close

#fazer append em arquivo
file = open('./basic_python/arquivo_criado.txt','a')
file.write('\nO segredo é aprender sempre!')
file.close