#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   

def maioridade(idade):
    try:        
        if int(idade) >= 18:
            return "Maior de Idade"
        else:
            return "Menor de Idade"
    except ValueError:
        return "Valor Invalido"
    return

verifica = maioridade(input('Digite a idade > '))

print(verifica)

