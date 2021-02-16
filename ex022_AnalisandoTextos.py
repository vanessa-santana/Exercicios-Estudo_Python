'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. '''


nome=str(input('Digite o nome completo: ')).strip() #strip() elimina os espaços antes e depois

print('Nome com letras maiuscula: {}'.format(nome.upper()))
print('Nome com letras maiuscula: {}'.format(nome.lower()))
print('Qtde letras sem espaço: {} '.format(len(nome)-nome.count(' ')))
#print('O primeiro nome tem {} letras. '.format(nome.find(' ')))
separa=nome.split() #separa as variaveis em lista
print('Primeiro nome é {} e tem {} letras '.format(separa[0],len(separa[0])))

