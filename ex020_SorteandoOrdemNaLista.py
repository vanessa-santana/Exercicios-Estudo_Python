#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1=str(input('Digite o 1 nome: '))
nome2=str(input('Digite o 2 nome: '))
nome3=str(input('Digite o 3 nome: '))
nome4=str(input('Digite o 4 nome: '))

lista=[nome1,nome2,nome3,nome4]

newOrder=shuffle(lista)

print('E os nomes são {}, {}, {}, {}. E a nova ordem será:'.format(nome1,nome2,nome3,nome4))
print(lista)



