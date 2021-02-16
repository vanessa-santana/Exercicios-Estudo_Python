#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''jeito 1
from math import trunc
number=(float(input('Digite um numero real: ')))
print('O numero é {} e a porção inteira é {:.0f}'.format(number,trunc(number)))
'''

#9
# jeito 2
number=(float(input('Digite um numero real: ')))
print('O numero é {} e a porção inteira é {}'.format(number,int(number)) ) 

'''jeito 3
number=(float(input('Digite um numero real: ')))
print('O numero é {} e a porção inteira é {:.0f}'.format(number,number) ) 
'''
