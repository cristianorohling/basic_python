'''
Faça um programa que leia e valide as seguintes informações:
* Nome: maior que 3 caracteres;
* Idade: entre 0 e 150;
* Salário: maior que zero;
* Sexo: 'f' ou 'm';
* Estado Civil: 's', 'c', 'v', 'd';
'''

import os

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastraNome():
    nome = input('Digite o seu nome: ')
    while len(nome) <= 3:
        print('O nome precisa ter mais que três caracteres!')
        nome = input('Digite o seu nome: ')
    return nome

def cadastraIdade():
    try:
        idade = int(input('Digite a sua idade: '))
        while idade < 0 or idade > 150:
            print('A idade precisa ser um número inteiro entre 1 e 150!')
            idade = int(input('Digite a sua idade: '))
    except ValueError:
        print('Idade inválida! Digite um número inteiro entre 1 e 150!')
    return idade

def cadastraSalario():
    try:
        salario = float(input('Digite o seu salario: '))
        while salario <= 0:
            print('O salário precisa ser um número inteiro maior que 0!')
            salario = float(input('Digite o seu salario: '))
    except ValueError:
        print('Salário inválidoa! Digite um número inteiro maior que 0!')
    return salario

def cadastraSexo():
    sexo = input('Digite o seu sexo ("m" ou "f"): ').lower()
    while sexo != 'm' and sexo != 'f':
        print('O sexo tem que ser "m" ou "f"!')
        sexo = input('Digite o seu sexo ("m" ou "f"): ').lower()

    if sexo == 'm':
        sexo = 'Masculino'
    else:
        sexo = 'Feminino'
    return sexo

def cadastraEstadoCivil():
    estadoCivil = input('Digite o seu estado civil ("s" para solteiro / "c" para casado / "v" para viúvo / "d" para divorciado): ').lower()
    while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
        print('O estado civil tem que ser "s" / "c" / "v" / "d"!')
        estadoCivil = input('Digite o seu estado civil ("s" para solteiro / "c" para casado / "v" para viúvo / "d" para divorciado): ').lower()
    
    match estadoCivil:
        case 'c':
            estadoCivil = 'Casado(a)'
        case 's':
            estadoCivil = 'Solteiro(a)'
        case 'v':
            estadoCivil = 'Viúvo(a)'
        case 'd':
            estadoCivil = 'Divorciado(a)'
    return estadoCivil

def imprimeCadastro(nome, idade, salario, sexo, estadoCivil):
    limpaTela()
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Salário: R$ {salario:.2f}')
    print(f'Sexo: {sexo}')
    print(f'Estado Civil: {estadoCivil}')

def cadastro():
    limpaTela()
    nome = cadastraNome()
    idade = cadastraIdade()
    salario = cadastraSalario()
    sexo = cadastraSexo()
    estadoCivil = cadastraEstadoCivil()
    imprimeCadastro(nome, idade, salario, sexo, estadoCivil)

cadastro()