# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num=int(input('Digite um numero: '))
cont=0
for i in range (1,num+1):
    if num % i==0:
        print ('\033[33m',end='') #codigo para cor amarela
        cont+=1
    else:
        print ('\033[31m',end='') #codigo para cor vermelha
    print('{} '.format(i), end='')
print('\033[m') #encerra a cor das letras
if cont==2:
    print('O numero {} É PRIMO'.format(num))
else:
    print('O numero {} foi divisivel {} vezes.\nE por isso NÃO É PRIMO!'.format(num,cont))
