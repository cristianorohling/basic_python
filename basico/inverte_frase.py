def inversor_texto(frase):
				frase_reversa = ''
				qtd_char = len(frase)
				while qtd_char > 0:
								frase_reversa = frase_reversa + frase[qtd_char-1]
								qtd_char -=1
				return frase_reversa
								
frase_invertida = inversor_texto(input('Digite uma frase para ser invertida:\n'))

print('Frase invertida:\n' + frase_invertida.upper().strip())