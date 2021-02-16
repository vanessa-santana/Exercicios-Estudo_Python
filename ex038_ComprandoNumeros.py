'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))


if num1 - num2 > 0:
    maior = num1
    print('O maior numero é o {}'.format(maior))
elif num1 - num2 < 0:
    maior = num2
    print('O maior numero é o {}'.format(maior))
else:
    print('Os numeros são iguais')

#outroModo
if num1 > num2 :
    print('O maior numero é o {}'.format(maior))
elif num1 < num2:
    print('O maior numero é o {}'.format(maior))
else:
    print('Os numeros são iguais')
    