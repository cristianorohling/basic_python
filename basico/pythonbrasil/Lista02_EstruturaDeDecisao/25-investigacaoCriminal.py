'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 
2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

print('Você está em um interrogatório policial. Responda apenas "S" ou "N":\n\n')

listaPerguntas = ["Telefonou para a vítima? ",
"Esteve no local do crime? ",
"Mora perto da vítima? ",
"Devia para a vítima? ",
"Já trabalhou com a vítima? "]

listaRespostas = []
numResposta = 0

for pergunta in listaPerguntas:
	resposta = input(pergunta).lower()
	while resposta != 's' and resposta != 'n':
		perguntaAgressiva = f'{pergunta}Responde, "S" ou "N", ô meliante! '
		resposta = input(perguntaAgressiva).lower()
	listaRespostas.append(resposta)
				
positivas = listaRespostas.count('s')

print('\n\nConclusão do Interrogatório:\n\n')

if (positivas == 5):
	print('Assassino')
elif (positivas >= 3) and (positivas <= 4):
	print('Cúmplice')
elif (positivas == 2):
	print('Suspeito')
else:
	print('Inocente')