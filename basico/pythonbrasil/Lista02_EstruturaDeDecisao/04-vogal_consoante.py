#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
from unidecode import unidecode


vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

letra = input('Entre com uma letra e eu direi se é vogal ou consoante: ')
letra = unidecode(letra.lower())

if letra in vogais:
    print('Vogal')
elif letra in consoantes:
    print('Consoante')
else:
    print("Entrada Inválida!")