#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number=int(input('Digite um numero: '))

if number % 2 == 0:
    print('O num {} é par'.format(number))
else:
    print('O num {} é impar'.format(number))
