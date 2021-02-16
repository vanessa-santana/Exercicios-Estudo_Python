#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name=str(input("Digite o nome completo: ")).strip() #strip() elimina os espaços antes e depois
print('O nome "{}" tem "SILVA"?: {}'.format(name,'SILVA' in name.upper()))