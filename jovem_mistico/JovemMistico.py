import pandas as pd
import os
from unidecode import unidecode

def descobre_signo_zodiaco(dia,mes):
    if (((dia >= 21) and (dia <= 31)) and mes == 3) or (((dia >= 1) and (dia <= 19)) and mes == 4):
        return "Áries"
    elif (((dia >= 20) and (dia <= 30)) and mes == 4) or (((dia >= 1) and (dia <= 20)) and mes == 5):
        return "Touro"
    elif (((dia >= 21) and (dia <= 31)) and mes == 5) or (((dia >= 1) and (dia <= 20)) and mes == 6):
        return "Gêmeos"
    elif (((dia >= 21) and (dia <= 30)) and mes == 6) or (((dia >= 1) and (dia <= 22)) and mes == 7):
        return "Câncer"
    elif (((dia >= 21) and (dia <= 31)) and mes == 7) or (((dia >= 1) and (dia <= 20)) and mes == 8):
        return "Leão"
    elif (((dia >= 21) and (dia <= 31)) and mes == 8) or (((dia >= 1) and (dia <= 22)) and mes == 9):
        return "Virgem"
    elif (((dia >= 23) and (dia <= 30)) and mes == 9) or (((dia >= 1) and (dia <= 22)) and mes == 10):
        return "Libra"
    elif (((dia >= 23) and (dia <= 30)) and mes == 10) or (((dia >= 1) and (dia <= 21)) and mes == 11):
        return "Escorpião"
    elif (((dia >= 22) and (dia <= 30)) and mes == 11) or (((dia >= 1) and (dia <= 21)) and mes == 12):
        return "Sagitário"
    elif (((dia >= 22) and (dia <= 31)) and mes == 12) or (((dia >= 1) and (dia <= 19)) and mes == 1):
        return "Capricórnio"
    elif (((dia >= 20) and (dia <= 31)) and mes == 1) or (((dia >= 1) and (dia <= 18)) and mes == 2):
        return "Aquário"
    elif (((dia >= 19) and (dia <= 29)) and mes == 2) or (((dia >= 1) and (dia <= 20)) and mes == 3):        
        return "Peixes"
    else: 
        return "Data Invalida" 

def descobre_signo_chines(ano_nascimento):
    animais = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]
    # Calcula o índice do animal na lista com base no ano de nascimento
    indice = (ano_nascimento - 1924) % 12    
    return animais[indice]

def numero_pitagorico(nome):
    valor_letras = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
        "f": 6, "g": 7, "h": 8, "i": 9, "j": 1,
        "k": 2, "l": 3, "m": 4, "n": 5, "o": 6,
        "p": 7, "q": 8, "r": 9, "s": 1, "t": 2,
        "u": 3, "v": 4, "w": 5, "x": 6, "y": 7,
        "z": 8, " ": 0,
    }    
    soma_valores = 0
    #em letra minuscula e sem acentos...
    nome = unidecode(nome.lower())
    

    for letra in nome:
        if letra in valor_letras:
            soma_valores += valor_letras[letra]

    return numero_raiz(soma_valores)


def numero_raiz(numero):
    while numero > 9 and numero not in [11, 22]:
        soma_digitos = 0
        while numero > 0:
            soma_digitos += numero % 10
            numero //= 10
        numero = soma_digitos
    return numero


def explicacao_signo_zodiaco(signo):
    dados_signo = pd.read_csv('D:\Python\Jovem_Mistico\signo_zodiaco.csv')    
    explicacao = dados_signo.loc[dados_signo['signo'] == signo, 'significado'].values[0]
    return explicacao

def explicacao_signo_chines(signo):
    dados_signo = pd.read_csv('D:\Python\Jovem_Mistico\signo_chines.csv')    
    explicacao = dados_signo.loc[dados_signo['signo'] == signo, 'significado'].values[0]
    return explicacao


def explicacao_num_pitagorico(numero):
    dados_numerologia = pd.read_csv('D:\Python\Jovem_Mistico\pitagorico.csv')    
    explicacao = dados_numerologia.loc[dados_numerologia['numero'] == numero, 'significado'].values[0]
    return explicacao


def entrada_dados():
    os.system('cls')
    print('----------------------------------------\nJOVEM MISTICO S/A\n----------------------------------------\n')
    nome    = input('Digite o nome completo: ')
    dt_nasc = input('Digite a data de nascimento no formato DD/MM/AAAA: ')
    dia, mes, ano = map(int, dt_nasc.split('/'))        

    signo_zodiaco = descobre_signo_zodiaco(dia,mes)   
    exp_signo_zodiaco = explicacao_signo_zodiaco(signo_zodiaco)
    signo_chines = descobre_signo_chines(ano)
    exp_signo_chines = explicacao_signo_chines(signo_chines)
    num_pitagoric = numero_pitagorico(nome)
    exp_pitagoric = explicacao_num_pitagorico(num_pitagoric)

    print('Signo Zodiacal:', signo_zodiaco)
    print('Explicação Signo:', exp_signo_zodiaco)
    print('----------------------------------------')
    print('Signo Chines:', signo_chines)
    print('Explicação Signo:', exp_signo_chines)
    print('----------------------------------------')
    print('Numero Pitagorico:', num_pitagoric)
    print('Explicação Numerológica:', exp_pitagoric)

entrada_dados()
