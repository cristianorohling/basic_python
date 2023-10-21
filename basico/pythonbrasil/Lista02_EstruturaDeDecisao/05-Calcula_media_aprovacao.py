#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
 

try:
    nota1 = float(input('Digite a primeira nota > '))
    nota2 = float(input('Digite a segunda nota  > '))
    
    if 0 <= nota1 <= 100 and 0 <= nota2 <= 100:
        media = (nota1 + nota2)/2
        print(f'Média: {media}')
        if (media == 100):
            print('Aprovado com Distinção')
        elif (media >= 70):
            print('Aprovado')
        elif (media < 70):
            print('Reprovado')
    else:
        print('Você digitou notas inválidas!')
except ValueError:
    print('Valores Inválidos!')