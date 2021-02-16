#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

nome1=str(input('Digite o 1 nome: '))
nome2=str(input('Digite o 2 nome: '))
nome3=str(input('Digite o 3 nome: '))
nome4=str(input('Digite o 4 nome: '))

lista=[nome1,nome2,nome3,nome4]

escolhido=choice(lista)

print('E o escolhido foi: {}'.format(escolhido))

