import numpy as np

alunos = ['Jose', 'Pedro', 'Mateus', 'Luiz', 'Marcos']
notas_turma = np.array([4.0, 8.0, 10.0, 5.5, 3.0])


mascara_recuperacao = notas_turma < 5
print(mascara_recuperacao)

cont = 0 

while cont < len(alunos):
    print('Aluno:', alunos[cont])
    print('Nota:', notas_turma[cont])    
    print('Recuperacao:', mascara_recuperacao[cont])
    
    if mascara_recuperacao[cont] == True:
        nota_recuperacao = float(input('Nota da Recuperação: '))
        notas_turma[cont] = nota_recuperacao
        if nota_recuperacao >= 5:            
            print('Aprovado na Recuperação')
        elif nota_recuperacao < 5:
            print('Não recuperado')        
    else:
        print('Aluno Aprovado!')
    print('--------------------------------------')
    cont += 1


print(notas_turma)
