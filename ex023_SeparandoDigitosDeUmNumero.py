#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number=int(input('Digite um numero de 0 a 9999: '))
u=number//1 %10
d=number//10 %10
c=number//100 %10
m=number//1000 %10

print('Analisando numero {} '.format(number))
print('Milhar: {} '.format(m))
print('Centena: {} '.format(c))
print('Dezena: {} '.format(d))
print('Unidade: {} '.format(u))




