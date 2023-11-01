#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

while (usuario == senha):
    print('A senha não pode ser igual ao nome do usuário!')
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

print('Usuario criado!')

