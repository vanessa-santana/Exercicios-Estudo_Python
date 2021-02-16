#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

print('-'*30)
print('Squencia de Fibonacci')
print('-'*30)

termos=int(input('Quantos termos quer mostrar? '))


primeiro=0
segundo=1
print('~'*30)
print('{} -> {} '.format(primeiro,segundo),end='')
contador=3
while contador <=termos:
    terceiro=primeiro+segundo
    print('-> {} '.format(terceiro),end='')
    primeiro=segundo
    contador+=1
print('-> FIM')
print('~'*30)